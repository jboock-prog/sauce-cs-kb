import unittest
from unittest.mock import Mock, patch

import requests

import sync_to_confluence as sync


class SyncRetryTests(unittest.TestCase):
    def setUp(self):
        self.sleep = patch.object(sync.time, "sleep").start()
        self.lookup = patch.object(sync, "get_page_by_title").start()
        self.create = patch.object(sync, "create_page").start()
        self.update = patch.object(sync, "update_page").start()
        self.addCleanup(patch.stopall)

    def upsert(self):
        return sync.upsert_page("Example", "<p>Body</p>", "KB", "parent")

    def test_connection_reset_during_lookup_is_retried(self):
        self.lookup.side_effect = [requests.ConnectionError("reset by peer"), None]
        self.create.return_value = {"id": "new"}
        self.assertEqual(self.upsert(), "new")
        self.sleep.assert_called_once_with(2)
        self.create.assert_called_once_with("Example", "<p>Body</p>", "KB", "parent")

    def test_lost_update_response_reads_latest_version(self):
        self.lookup.side_effect = [
            {"id": "page", "version": {"number": 3}},
            {"id": "page", "version": {"number": 4}},
        ]
        self.update.side_effect = [requests.ConnectionError("response lost"), {}]
        self.assertEqual(self.upsert(), "page")
        self.assertEqual([c.args[-1] for c in self.update.call_args_list], [3, 4])
        self.create.assert_not_called()

    def test_lost_create_response_discovers_existing_page(self):
        self.lookup.side_effect = [None, {"id": "new", "version": {"number": 1}}]
        self.create.side_effect = requests.ReadTimeout("response lost")
        self.assertEqual(self.upsert(), "new")
        self.create.assert_called_once()
        self.update.assert_called_once_with("new", "Example", "<p>Body</p>", 1)

    def test_persistent_failure_stops_after_bounded_backoff(self):
        self.lookup.side_effect = requests.ConnectionError("reset by peer")
        with self.assertRaises(requests.ConnectionError):
            self.upsert()
        self.assertEqual(self.lookup.call_count, 4)
        self.assertEqual([c.args[0] for c in self.sleep.call_args_list], [2, 4, 8])
        self.create.assert_not_called()

    def test_http_errors_are_not_retried(self):
        self.lookup.side_effect = requests.HTTPError("401 Unauthorized")
        with self.assertRaises(requests.HTTPError):
            self.upsert()
        self.lookup.assert_called_once()
        self.sleep.assert_not_called()

    def test_certificate_errors_are_not_retried(self):
        self.lookup.side_effect = requests.exceptions.SSLError("invalid certificate")
        with self.assertRaises(requests.exceptions.SSLError):
            self.upsert()
        self.lookup.assert_called_once()
        self.sleep.assert_not_called()


class ApiTests(unittest.TestCase):
    @patch.object(sync, "SESSION")
    @patch.dict(sync.CONFIG, {"url": "https://example.atlassian.net"})
    def test_api_reuses_session_with_connect_and_read_timeouts(self, session):
        response = Mock(ok=True, text='{"results": []}')
        response.json.return_value = {"results": []}
        session.request.return_value = response
        self.assertEqual(sync.api("get", "/content"), {"results": []})
        sync.api("put", "/content/page", json={"title": "Example"})
        self.assertEqual(session.request.call_count, 2)
        for call in session.request.call_args_list:
            self.assertEqual(call.kwargs["timeout"], (10, 60))
        self.assertEqual(session.request.call_args.args[:2], (
            "put", "https://example.atlassian.net/wiki/rest/api/content/page",
        ))


if __name__ == "__main__":
    unittest.main()
