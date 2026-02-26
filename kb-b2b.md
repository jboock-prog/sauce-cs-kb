# KB Entries: B2B Restaurant Requests

Extracted from: Sauce CC Team Playbook
Source date: Playbook content as of 2025
Last extracted: 2026-02-25
Entry count: 25

---

## Entry B2B-1: Enable / Disable a Store

**Title:** Enable or Disable a Store's Online Ordering
**Issue Type:** Restaurant Relations
**Situation:** A restaurant asks to pause or disable their online ordering (temporarily busy, holiday, vacation, renovation, etc.).
**Resolution:**
1. Go to the store's dashboard → Store Settings → click the "Store Enabled" slider.
2. Select the appropriate disable option:
   - **Pause for 1 hour** — auto re-enables after 1 hour.
   - **Until next opening time** — disables for the rest of the current session; auto re-enables at next opening time.
   - **Until specific date and hour** — select exact re-enable date/time (max 3-day limit).
   - **Future dates** — set both a disable date/time AND an enable date/time; use for known upcoming closures.
3. Select a closure reason — note this **will be displayed on the store's website** until it reopens.
4. Click "Disable store" and stay on the page until the progress bar completes.

**Ticket documentation:**
- Name the ticket: `[Resto name] | Disable request | [date/dates]`
- Fill out the ticket request explaining the closure.
- Add a note with a screenshot of the dashboard showing the store was disabled.
- If no future follow-up needed: close the ticket.
- If follow-up needed on a future date: move ticket to "Dashboard Disable Requests — Pending Reopen" column.

**Exceptions:** None.
**Approval Required:** No — restaurant or CS manager request is sufficient.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2B-2: Change or Update Permanent Opening Hours

**Title:** Change a Restaurant's Permanent Opening Hours
**Issue Type:** Restaurant Relations
**Situation:** A restaurant requests a permanent change to their weekly opening hours.
**Resolution:**
1. Go to the store's dashboard → Store Settings → scroll down to "Opening Days and Hours."
2. Click the clock icon fields to change opening/closing times for the selected days.
3. If a day is grayed out, it belongs to a separate set of opening hours — scroll down to find it.
4. To add a new set of hours for specific days: scroll to "Add another opening day" (only visible if not all days are already assigned).
5. To set split hours for a single day (e.g., 9 AM–2 PM and 6 PM–11 PM): use the "Add hours" button.
6. **Always click Save after any changes.**

**Exceptions:** None.
**Approval Required:** No — restaurant request is sufficient.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2B-3: Temporary Change to Opening Hours

**Title:** Temporary Change to Opening Hours (Reverts After a Set Period)
**Issue Type:** Restaurant Relations
**Situation:** A restaurant or account manager requests a temporary hours change that needs to revert to the original schedule after a specific date.
**Resolution:**
1. Before making changes, take a screenshot of the current opening hours and paste it as a note in the ticket.
2. Update the hours to the temporary schedule.
3. Add the new hours to the ticket note for reference.
4. Keep the ticket open in the "Dashboard Disable Requests — Pending Reopen" column.
5. Set a reminder (Slack scheduled message, personal reminder, or ticket follow-up) to revert the hours on the end date.
6. When the end date arrives, revert the hours back to the original and close the ticket.

**Exceptions:** None — at least one reminder mechanism is required to ensure the revert doesn't get missed.
**Approval Required:** No — restaurant or account manager request is sufficient.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2B-4: Update a Restaurant's Bank / Banking Details

**Title:** Restaurant Requests a Change to Their Banking Details
**Issue Type:** Restaurant Relations
**Situation:** A restaurant needs to update the bank account where they receive their payouts.
**Resolution:**
1. Open a ticket to CS.
2. Include the restaurant's contact information in the ticket.
3. Associate the company on the ticket.
4. Set the CS manager as the ticket owner.
5. CS will reach out to the restaurant directly to handle the change.

**How to find the CS manager:**
HubSpot → Companies → Customer Care View → search for the specific restaurant.

**Exceptions:** Do not attempt to make banking changes directly — always route through CS.
**Approval Required:** Yes — handled entirely by CS.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2B-5: Specific Phone Numbers for Certain Restaurants

**Title:** Restaurant-Specific Phone Numbers Reference
**Issue Type:** Restaurant Relations
**Situation:** Agent needs to call a specific restaurant that has a non-standard contact number.
**Resolution:**
Refer to the dedicated phone number spreadsheet for the following restaurants:
- 2 Bros Pizza
- El Tambo
- Shelsky's
- Freddo Miami
- Vito's
- Pizza Piez
- SRHouston / Shokku Ramen
- Jus by Julie NYC
- La Taqueria Diana

**Reference:** [Restaurant Phone Numbers Spreadsheet](https://docs.google.com/spreadsheets/d/1iDL75VFvl1wExXKpFT-SAMvl-EXXgvzHp9mOeHkdeUA/edit?gid=1847937947#gid=1847937947)

**Exceptions:** None.
**Approval Required:** No.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2B-6: Explaining a Refund to a Restaurant (Sales Report)

**Title:** Help a Restaurant Understand a Refund Deduction from Their Payout
**Issue Type:** Restaurant Relations
**Situation:** A restaurant reaches out confused about why a specific dollar amount was deducted from their payout.
**Resolution:**
1. Download the Sales Report from the restaurant's Sauce Dashboard for the relevant date.
2. In the report, locate the refunded order — it will show the customer info and Order ID.
3. Search for that customer's ticket in the ePayments pipeline using the Order ID.
4. Review the ticket request to understand what was refunded and why.
5. Provide this explanation to the restaurant.

**Exceptions:** None.
**Approval Required:** No.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2B-7: Sending Tickets to Internal Teams (CS, BO, Menu, OB)

**Title:** How to Route Tickets to Internal Teams (CS, BO, Menu, OB)
**Issue Type:** Policies & Rules
**Situation:** A request needs to be forwarded to an internal team (CS, BO, Menu, or OB).
**Resolution:**
**Required ticket fields before sending:**
- Company (attach the correct restaurant location — check for multiple locations)
- Ticket Owner (CS tickets: CS manager must be the owner)
- Ticket Request (short summary or copy of the received request)
- Category (determines which team receives it)

**Category guide:**

*CS:*
- `CS B2B: Billing questions/accounting` — restaurant questions about reports/payouts
- `CS B2B: Changing Bank Details` — restaurant changing payout bank
- `CS B2B: Feature Request` — restaurant suggestions for new system features
- `CS B2B: Stripe` — Stripe questions
- `CS Change of Plan` — restaurant changing subscription plan
- `CS Restaurant Cancellation` — restaurant ending Sauce subscription
- `CS Tablet Requested` — restaurant needs a new tablet
- `CS Subscription questions` — subscription questions

*BO:*
- `BO B2B: Flyer Request` — flyer or QR code requests
- `BO B2B: Website Changes` — background, fonts, images, slogans, logo (not menu items)
- `BO Config Changes` — delivery companies, delivery radius, credit card fees, etc.
- `BO Ordermark` — Ordermark changes
- `BO Toast Menu Changes` — Toast changes (except photos)

*Menu:*
- `Menu B2B: Menu changes (Sauce dashboard)` — menu changes for stores with Menu Editor
- `Menu: Toast Photos` — adding photos to Toast

*OB:*
- `OB Change POS/Integration` — restaurant changing their integration or POS
- `OB Onboarding` — general OB requests
- `OB Virtual Number` — Virtual Number/Virtual Answering changes

**To send the ticket:**
Move it to the column **"Received — triggers automation."** This automatically routes it to the correct team pipeline.

**DO NOT** manually change the pipeline and status to move it to the other team.

**Ticket naming format:** `Restaurant Name | Task` (e.g., "Shelsky's Of Brooklyn | Flyer" or "Smash House Miami | Change of plan")
**Request type:** "Internal" if an internal agent requested it; "B2B" if the store reached out.

**Exceptions:** None — always use the automation column, never manual pipeline changes.
**Approval Required:** No.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2B-8: Churn Requests (Restaurant Cancelling Sauce Subscription)

**Title:** Restaurant or Internal Team Requests to Churn a Restaurant
**Issue Type:** Escalation Paths
**Situation:** Someone from Sauce requests to churn (cancel the subscription of) a restaurant.
**Resolution:**
1. Move the ticket to CS.
2. Follow the specific guidelines for routing tickets to CS (see Entry B2B-7).

**Exceptions:** None — all churn requests go through CS.
**Approval Required:** Yes — handled by CS.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2B-9: Tablet Troubleshooting — Not Connecting to WiFi

**Title:** Tablet Troubleshooting — Tablet Not Connecting to WiFi
**Issue Type:** Restaurant Relations
**Situation:** Restaurant reports their tablet cannot connect to WiFi.
**Resolution:**
1. Verify the tablet is not in Airplane mode.
2. Check that WiFi is enabled: swipe down from the top of the tablet to view settings summary — confirm WiFi is on, Bluetooth is on, and Airplane mode is off.
3. Double-check the WiFi password and confirm they're connecting to the correct network.
4. Restart the tablet: hold the power button → tap "Restart" → attempt to reconnect after reboot.

**Exceptions:** None — if issues persist after all steps, escalate.
**Approval Required:** No.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2B-10: Tablet Troubleshooting — Cannot Log In to Dashboard

**Title:** Tablet Troubleshooting — Tablet Not Logging In to Dashboard
**Issue Type:** Restaurant Relations
**Situation:** Restaurant cannot log into the Sauce Dashboard on their tablet.
**Resolution:**
1. Double-check the login credentials — an "invalid email or password" error confirms a credentials issue.
2. Try resetting the password via the "Forgot password" link on the login screen.
3. If the store cannot reset the password themselves, reset it manually (see Entry B2B-13 — note: identity verification is required before resetting for any caller not recognized in Aircall).
4. Ensure the tablet is connected to the internet — login will not work without internet.

**Exceptions:** None.
**Approval Required:** No.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2B-11: Tablet Troubleshooting — Not Receiving Orders

**Title:** Tablet Troubleshooting — Tablet Not Receiving Orders
**Issue Type:** Restaurant Relations
**Situation:** Restaurant reports their tablet is not showing incoming orders.
**Resolution:**
1. Confirm the Sauce App is open and actively running.
2. Swipe down from the top of the tablet — check if the app appears as running. If not, reopen it.
3. If the app is open and running but orders are still not appearing when they should be: this is no longer a tablet hardware issue — escalate to the appropriate team.

**Exceptions:** If app is running but orders are still missing, do not continue troubleshooting hardware — escalate.
**Approval Required:** No for basic troubleshooting. Escalation required if hardware steps don't resolve.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2B-12: Tablet Replacement

**Title:** Tablet Replacement Request
**Issue Type:** Restaurant Relations
**Situation:** Restaurant has exhausted all tablet troubleshooting steps and still has issues.
**Resolution:**
1. Tell the restaurant you'll contact their account manager to look into sending a replacement tablet, and that their account manager will follow up with an update.
2. Collect a contact phone number or email for the restaurant if you don't already have one.
3. Create a ticket with the category **"CS Tablet Requested."**
4. Assign the CS agent as the ticket owner.
5. Move the ticket to the "Triggers automation" column.

**Exceptions:** Only initiate replacement after completing all troubleshooting steps (Entries B2B-9 through B2B-11).
**Approval Required:** Yes — handled by CS and account manager.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2B-13: Manually Reset Restaurant Dashboard Login

**Title:** Manually Reset a Restaurant's Dashboard Password
**Issue Type:** Restaurant Relations
**Situation:** A restaurant owner or staff is locked out of their dashboard and cannot reset the password themselves.
**Resolution:**
**Before resetting, verify identity:**
- Check if the caller's number is recognized in Aircall.
- If not recognized: ask for identification OR confirm with the restaurant's CS account manager that it's okay to change the login.

**Once confirmed:**
1. Open the restaurant's dashboard → go to the "Team" section.
2. Confirm you are on the correct restaurant location.
3. In User Management, find the account and reset the password.
4. Default reset password: **123456** (easy to communicate by phone; easy to remember).

**Note:** You cannot see the previous password — you can only overwrite it.

**Exceptions:** Identity verification is mandatory before any password reset for unrecognized callers.
**Approval Required:** Yes — identity check or CS account manager confirmation required for unrecognized callers.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2B-14: Add or Remove Email Order Notifications

**Title:** Add or Remove Email Order Notifications for a Restaurant
**Issue Type:** Restaurant Relations
**Situation:** A restaurant wants to add or remove an email address from their order notifications.
**Resolution:**
1. Open the restaurant's Sauce Dashboard.
2. Go to Orders → Notifications → Email.
3. Confirm the Email notifications toggle is turned on.
4. Add or remove the email address as requested.

**Exceptions:** None.
**Approval Required:** No.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2B-15: Add or Remove SMS Order Notifications

**Title:** Add or Remove SMS Order Notifications for a Restaurant
**Issue Type:** Restaurant Relations
**Situation:** A restaurant wants to add or remove a phone number from their SMS order notifications.
**Resolution:**
1. Open a ticket to the BO team.
2. Include the phone number where orders should be sent (or the number to remove) in the ticket request.
3. Use the category: **BO Config Changes.**
4. Move ticket to the "Received — triggers automation" column.

**Exceptions:** SMS notifications cannot be managed directly from the dashboard — must always go through BO.
**Approval Required:** No — BO handles the change.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2B-16: Invite a New User to a Restaurant's Dashboard

**Title:** Invite a New User to a Restaurant's Dashboard
**Issue Type:** Restaurant Relations
**Situation:** A restaurant requests that a new staff member or owner be added to their Sauce Dashboard.
**Resolution:**
1. Log into the restaurant's dashboard.
2. Select "Team" from the left-hand navigation.
3. Click "Add New" in the top right.
4. Enter the user's Email, First Name, and Last Name.
5. Select "Admin" by default unless the restaurant specifies a different role.
6. Click "Add New User."
7. The new user will receive an email to set up their password.

**Exceptions:** None.
**Approval Required:** No — restaurant request is sufficient.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2B-17: Add Emails to a Restaurant's Weekly Sales Report

**Title:** Add Emails to a Restaurant's Weekly Sales Report
**Issue Type:** Restaurant Relations
**Situation:** A restaurant wants to add one or more email addresses to receive their weekly sales report.
**Resolution:**
1. Log into the restaurant's dashboard.
2. Go to Store Settings.
3. Find "Mail for Weekly Report" and add the email addresses, separated by commas.
4. Click Save in the top right corner.

**Exceptions:** None.
**Approval Required:** No — restaurant request is sufficient.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2B-18: Create a Discount or Coupon Code

**Title:** Create a Discount / Coupon Code for a Restaurant
**Issue Type:** Restaurant Relations
**Situation:** A restaurant requests a promotional discount or coupon code be created on their dashboard.
**Resolution:**
1. Log into the restaurant's dashboard.
2. Go to Discounts → Add New.
3. Select one of the 4 discount type options.
4. Select the Wizard.
5. Enter the percentage or dollar amount and any minimum order requirement (no minimum needed unless specified; no expiration dates unless specified).
6. Ensure "Promo Code" is set to Enabled.
7. Enter the promo code text.
8. **Do not select** Single Use, Email Marketing, or Display Above Menu unless specifically requested.
9. Click Apply Changes.

**Exceptions:** None.
**Approval Required:** No — restaurant request is sufficient.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2B-19: Restaurant Requests Their 1099-K Form

**Title:** Restaurant Requests Their 1099-K Tax Form
**Issue Type:** Restaurant Relations
**Situation:** A restaurant asks CS to provide their 1099-K form.
**Resolution:**
**Preferred — self-service:**
Send the restaurant the **"1099-K Form"** HubSpot template, which directs them to retrieve it from their Stripe account. Reference guide: https://support.getsauce.com/sauce-guide-for-taxes

**If the CS manager requests it on behalf of the restaurant:**
Forward the request to Yuval (yuval.s@getsauce.com) and she will retrieve and send it.

**If sending the form directly via email:**
This requires **express written consent from the restaurant owner.** They must send an email stating:
> "My name is [Name], I am the [owner/role] of [Location Name], located at [Address]. I allow Sauce to send me my 1099-K form for [Year] via email."

**Exceptions:** The form cannot be sent via email without the written consent statement above.
**Approval Required:** Yes — written owner consent required before emailing the form directly.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2B-20: How Taxes Work (Restaurant Questions)

**Title:** Tax Policy — How Sauce Handles Sales Tax
**Issue Type:** Policies & Rules
**Situation:** A restaurant asks how sales taxes are handled on their orders.
**Resolution:**
Sauce pays all sales taxes to the restaurant at the same time as the order payout. The restaurant is then responsible for paying their local taxes from those funds.

**Exceptions:** None.
**Approval Required:** No.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2B-21: Tax-Exempt Order Refund Requests

**Title:** Tax-Exempt Order — Refund Request
**Issue Type:** Policies & Rules
**Situation:** A customer or restaurant requests a refund because the order qualifies as tax-exempt.
**Resolution:**

**If the customer makes the request:**
- CS cannot process a refund for tax-exempt orders directly.
- Send the customer the **"Tax-exempt request (to cx)"** HubSpot template, which directs them to contact the restaurant for this type of request.

**If the restaurant makes the request:**
- Send the restaurant the **"Tax-exempt request (to resto)"** HubSpot template.
- Explain that if the restaurant wishes to refund the tax to the customer, the refund comes from the store.
- If the restaurant consents to refunding the customer, process the refund as requested.

**Exceptions:** Tax-exempt refunds are only possible if the restaurant explicitly consents to issuing them.
**Approval Required:** Yes — restaurant consent required for tax-exempt refunds.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2B-22: Sending Test Orders to Restaurants

**Title:** Send a Test Order to a Restaurant
**Issue Type:** Restaurant Relations
**Situation:** A test order needs to be sent to a restaurant (new restaurant onboarding, system check, resend missed order, etc.).
**Resolution:**
**ALWAYS inform the store before sending** — they must know not to prepare it.

**For Wix restaurants:**
1. Add item(s) to the cart on the restaurant's Wix site.
2. At checkout, use:
   - Name: TEST / Surname: ORDER
   - Phone: 8884771537
   - Email: testorder@getsauce.com
   - Order notes: "TEST ORDER — DO NOT PREPARE"
3. Card info: Use 42424242 for all card fields except expiration date (use any future date).

**For Storefront (SF) restaurants:**
1. Before adding items: click the restaurant's address under the name multiple times until the "test order" sign appears on the right.
2. Add item(s) to the cart.
3. At checkout, use:
   - Name: TEST / Surname: ORDER
   - Phone: 8884771537
   - Email: testorder@getsauce.com (or automation@getsauce.com for an invisible test order the store won't see)
4. Card info: Use 42424242 for all fields except expiration date (use any future date).

**Exceptions:** Never send a test order without first notifying the restaurant.
**Approval Required:** Yes — restaurant must be informed before test order is placed.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2B-23: Change a Restaurant's Delivery Radius

**Title:** Change a Restaurant's Delivery Radius
**Issue Type:** Restaurant Relations
**Situation:** A restaurant or CS manager requests a change to the store's delivery radius.
**Resolution:**
1. Open a ticket to the BO team.
2. Category: **BO Config Changes.**
3. Include the new delivery radius in the ticket request.
4. Move ticket to the "Received — triggers automation" column.

**Exceptions:** CS cannot change delivery radius directly — always route through BO.
**Approval Required:** No — BO handles the change.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2B-24: Pause or Change a Payout Schedule

**Title:** Pause or Change a Restaurant's Payout Schedule
**Issue Type:** Restaurant Relations
**Situation:** An account manager requests a change to a store's payout rate or payout schedule.
**Resolution:**
1. Create a ticket with the ticket request and company name.
2. Move the ticket to the **ePayments Task** column.

**Exceptions:** None — only account managers initiate this request.
**Approval Required:** Yes — account manager must initiate the request.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2B-25: Change a Restaurant's Stripe Account

**Title:** Change a Restaurant's Stripe Account
**Issue Type:** Restaurant Relations
**Situation:** A restaurant needs to switch to a different Stripe account for payment processing.
**Resolution:**
1. Create a ticket to BO, including the new Stripe account details in the ticket request.
2. Follow the standard BO ticket guidelines (see Entry B2B-7).
3. After submitting the ticket, also send a Slack message to ePayments as an FYI to inform them of the change.

**Exceptions:** The Slack notification to ePayments is required in addition to the BO ticket — not instead of it.
**Approval Required:** No — restaurant or account manager request is sufficient.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2B-26: Update / Download the Sauce Dashboard App on a Tablet

**Title:** Update or Download the Sauce Dashboard App
**Issue Type:** Restaurant Relations
**Situation:** The Sauce Dashboard App on a restaurant's tablet is not working properly, likely due to an outdated version.
**Resolution:**
1. Ask the restaurant to open **Google Chrome** on their tablet.
2. Navigate to: **support.getsauce.com**
3. Go to the "Download the App" section.
4. Click "Click to install the Sauce Dashboard app."
5. Click the image with the red background — this downloads the APK file.
6. Once downloaded, open the file and install it.

Note: This process works for both new installs and updates — have the restaurant follow these steps even if they already have the app.

**Reference video:** https://drive.google.com/file/d/1UKH1ohawFIqaQ1gtLaY480Ry_hZSgKe_/view?usp=sharing

**Exceptions:** None — same steps for install and update.
**Approval Required:** No.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2B-27: Connect or Reconnect a Printer to the Tablet

**Title:** Connect or Reconnect a Printer to the Sauce Dashboard App
**Issue Type:** Restaurant Relations
**Situation:** A restaurant's printer is not working or needs to be reconnected to the Sauce Dashboard App.
**Resolution:**
1. First, ask the restaurant to turn the printer off and back on via Bluetooth.
2. On the tablet, open the Sauce Dashboard App → Store Settings → select the "Printer" checkbox.
3. Click "Connect Printer."
4. A loading screen will appear, followed by a list of nearby Bluetooth devices — have the restaurant select their printer.
5. If no devices are found, click "Go To Bluetooth Settings" → "Pair new Device" → find and pair the printer there.

**For printers with a Pair button:**
Some printers have a "Pair" button on the back. Hold it for 5 seconds to make the printer discoverable for pairing.

**Exceptions:** If connectivity issues persist after pairing, the issue may be hardware-related — escalate.
**Approval Required:** No.
**Last Updated:** 2026-02-25 — extracted from Playbook
