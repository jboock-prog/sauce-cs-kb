# KB Entries: B2C Order Modifications

Extracted from: Sauce CC Team Playbook
Source date: Playbook content as of 2025
Last extracted: 2026-02-25
Entry count: 9

---

## Entry B2C-1: Change Order from Pickup to Delivery

**Title:** Change Order from Pickup to Delivery
**Issue Type:** Order Issues
**Situation:** Customer wants to switch their pickup order to a delivery (wrong location, can't go to the store, placed order incorrectly).
**Resolution:**
1. **Do not confirm the change is possible** — tell the customer you'll check first. The delivery address may be outside the delivery zone.
2. Look up the order in the Slack `#orders` channel to get the subtotal.
3. Simulate placing the order on the restaurant's website to determine the delivery fee:
   - Match the order subtotal above or below $30 (to replicate whether the customer qualifies for free delivery). You don't need to add the same items — just match the subtotal threshold.
4. Once you have the delivery fee, ask the customer if they approve the upcharge.
5. If approved, proceed with BaD (book-a-driver).

**Tip handling:**
- If the pickup order already had a tip: use that same tip amount on the BaD. Create a refund ticket from the restaurant to the delivery company for the tip amount.
- If no tip on the pickup order: ask the customer if they want to add one. If yes, upcharge them. If no, don't add a tip on the BaD.

**Exceptions:** Change is not possible if the delivery address is outside the restaurant's delivery zone.
**Approval Required:** Yes — customer must approve any delivery fee upcharge before proceeding.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2C-2: Change Order from Delivery to Pickup

**Title:** Change Order from Delivery to Pickup
**Issue Type:** Order Issues
**Situation:** Customer wants to switch their delivery order to a pickup (they'll go to the store themselves).
**Resolution:**

**Step 1 — Check driver status before doing anything:**

If the order has a driver assigned:
- If driver is close to the restaurant → call the restaurant and tell them NOT to give the order to the driver.
  - Restaurant confirms → cancel the tracking link → proceed to Step 2.
  - Restaurant says the order was already picked up → tell the customer we can no longer cancel the delivery.
  - Restaurant doesn't answer → tell the customer the restaurant is unresponsive and we are unable to cancel the delivery.
- If the driver is very far from the restaurant → cancel the tracking link → proceed to Step 2.

If no driver is assigned → cancel the tracking link → proceed to Step 2.

If the order is already marked as picked up on the system → tell the customer the driver already has it and is on the way — we cannot cancel the delivery.

**Step 2 — Handle the refund:**
- **Make absolutely sure the customer understands: only the delivery is canceled — the order itself is NOT canceled.**
- If the customer placed a tip and asks for a refund on the tip and/or delivery fee → send the ticket to Refund Request as a refund request for those amounts.
- If the customer placed a tip but does not ask for a refund → close the ticket.
- If the customer placed no tip → they can only request a refund for the delivery fee. If they don't request it, close the ticket.

**Exceptions:** None.
**Approval Required:** No — no restaurant approval needed. ePayments needed only if customer requests refund of delivery fee/tip.
**Last Updated:** 2026-02-26 — added driver proximity check and restaurant call step; added tip/fee refund logic

---

## Entry B2C-3: Add an Item to an Existing Order

**Title:** Add an Item to an Existing Order
**Issue Type:** Order Issues
**Situation:** Customer wants to add an item to an order they've already placed.
**Resolution:**
1. **Check if the order has been picked up first.**
   - If already picked up → we can no longer add items. Inform the customer.
   - If not yet picked up → proceed.
2. Find the item price on the **restaurant's website**. The upcharge = website price + tax.
   - If the item is not listed on the website (e.g., customer wants to add chicken to a salad but there's no price for it): call the restaurant and ask how much it would cost to make that change.
3. Ask the customer if they agree to be charged on their original payment method if the restaurant approves.
   - If yes → proceed.
   - If no → tell them we cannot assist; they need to speak with the restaurant directly.
4. Call the restaurant and ask if they can add the item.
   - If yes → tell them we will charge the customer on our end, or they can use the "Adjust button" on the dashboard. Note: the item will not appear on the system — we can only charge internally. If the restaurant wants to see it on the system, offer to send a test order so it prints in their kitchen.
   - If no → inform the customer that adding the item is not possible.
5. Once both the restaurant and customer have confirmed → set ticket to ePayments Task Status and request the upcharge. You can share a screenshot of the item online as proof of the correct price.
   - Note: after the upcharge, the ticket will return to Next Action in the Support Pipeline.

**If it's a future order:**
- Keep a ticket open in PENDING — WAITING ON CC TEAM so Support calls the restaurant on the order date to remind them to add the item.
- Schedule a Slack reminder in `#cc-team-chat` with enough lead time before the pickup time.

**Exceptions:** None — both restaurant confirmation and customer approval are always required before upcharging.
**Approval Required:** Yes — restaurant must confirm; customer must approve upcharge.
**Last Updated:** 2026-02-26 — updated from Process Notes to fix price-check rule and add pickup status check

---

## Entry B2C-4: Change Order Time or Delivery ETA

**Title:** Change Order Time or Delivery ETA
**Issue Type:** Order Issues
**Situation:** Customer wants to change the scheduled time or ETA for their order.
**Resolution:**
1. **Do not confirm a new ETA without restaurant approval.** Always tell the customer you'll check with the restaurant first.
2. Contact the restaurant and get their confirmation that the time change is possible.
3. If approved, change the ETA using one of two methods:
   - **Option A:** Cancel the current tracking link and BaD with the correct time/ETA.
   - **Option B:** Use the "Edit ETA" button in the restaurant view (`/r/` link) of the tracking link. Note: available ETA options are limited — if the time you need isn't available, you must use Option A.
4. Inform the customer if you cancel and BaD.

**Important caveat:** Changing the ETA on the tracking link does NOT update the pickup time shown on the restaurant's dashboard. The restaurant's dashboard shows the original pickup time. Keep this in mind when communicating with the restaurant.

**Exceptions:** None — restaurant approval is always required.
**Approval Required:** Yes — restaurant must confirm the time change.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2C-5: Change Order Date (Future Orders)

**Title:** Change the Date of a Future Order
**Issue Type:** Order Issues
**Situation:** Customer wants to reschedule a future order to a different date.
**Resolution:**
1. Get the restaurant's approval/confirmation that the date change is possible.
2. Note: the dashboard cannot be updated — the new date will not appear on the restaurant's POS/Tablet. The restaurant must remember the change manually.
3. Keep a ticket open in PENDING — WAITING ON CC TEAM for Support to:
   - Call the restaurant on the **original order date** to remind them NOT to prepare the order (it will still print).
   - Call the restaurant on the **new date** to remind them to prepare the order.
4. Schedule Slack reminders in `#cc-team-chat` for both dates with enough lead time before pickup.

**Exceptions:** Even with restaurant approval, the dashboard cannot reflect the change — manual follow-up is mandatory.
**Approval Required:** Yes — restaurant must confirm the date change.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2C-6: Add Delivery Instructions to an Active Order

**Title:** Add Delivery Instructions to an Active Order
**Issue Type:** Order Issues
**Situation:** Customer needs to add or update delivery instructions after the order has been placed (often comes in through the chat bot — check chat history for the request).
**Resolution:**
When the request comes in via chat, greet with the `#Hello delivery-instructions` snippet first.

If the Dispatch team is online, ask them to handle it. Otherwise, follow the procedure by delivery company:

**Relay:**
- Add instructions via the Relay dashboard at any time — even after pickup.

**Uber (order NOT yet picked up):**
- Go to the Uber tracking link → find "Drop off notes" section → edit directly.

**Uber (order already picked up):**
- Call Uber support to relay the instructions to the driver.

**DoorDash:**
- Call DoorDash support to add the instructions. Some DoorDash tracking links allow self-service if the order hasn't been picked up, but this is inconsistent — calling is the reliable method.

**Exceptions:** Relay is the only provider where instructions can be added post-pickup without calling. Uber and DoorDash require calls once the order is picked up.
**Approval Required:** No.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2C-7: Change Delivery Address

**Title:** Change Delivery Address on an Active Order
**Issue Type:** Order Issues
**Situation:** Customer needs to change their delivery address (full address change or updated delivery instructions). May be the customer's fault (wrong input) or a Sauce system issue (dispatch bug).
**Resolution:**
First, determine fault if unclear — ask Tier 2 to investigate. Fault matters for: whether redelivery is possible, and for the refund process.

**If driver is NOT assigned or is not near the restaurant:**
- Cancel the tracking link and BaD with the correct address.

**If driver is assigned and near the restaurant (but order not yet picked up):**
- Do NOT cancel the tracking link. GPS may be delayed and the driver may have already taken the order — canceling could leave the food stranded.
- Advise the customer you'll do your best to inform the driver of the correct address.
- Encourage the customer to try reaching the driver themselves (driver's number is visible on the customer's tracking link view).

**If order is already picked up:**
- Do NOT cancel the tracking link.
- Advise the customer you'll do your best to inform the driver of the correct address/instructions.
- Encourage the customer to try reaching the driver themselves.

**Exceptions:** Never cancel a tracking link when the driver is near the restaurant or has already picked up — the food will be stranded.
**Approval Required:** No — but Tier 2 investigation required to determine fault when unclear.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2C-8: Customer Calling to Reach the Restaurant

**Title:** Customer Calling to Reach the Restaurant Directly
**Issue Type:** Order Issues
**Situation:** A customer calls Sauce support but actually wants to speak with the restaurant (e.g., food quality feedback, rude staff, order placed at the store or through a different service).
**Resolution:**
1. Inform the customer: "We are the support team for orders made through the store's website — we're not the store itself. Can I help you with anything?"
2. If the issue is something CS cannot handle (food quality, rude staff, order not through Sauce): attempt to transfer them to the restaurant directly, or tell them they can call the same number and press the option for restaurant staff (usually option 3 or 4).

**How to transfer a call to the restaurant (Aircall):**
1. Go to the store's Sauce Dashboard → Virtual Answering → Edit Phone Number. This is the store's direct number.
2. In Aircall, click "Transfer" and paste the store's direct number.
3. After clicking Transfer, the call will hang up on your end.
4. If the store doesn't answer, the call returns to you — but you are not obligated to pick it up again.

**Exceptions:** None.
**Approval Required:** No.
**Last Updated:** 2026-02-25 — extracted from Playbook


---

## Entry B2C-9: Sauce iOS App Version 1.0.9 Release

**Title:** Sauce iOS App Version 1.0.9 — New Reorder Experience, Faster Checkout & Reliability Improvements

**Issue Type:** Product Update / New Feature

**Situation:** Reference this entry when a customer contacts support with questions about the Sauce iOS app version 1.0.9, including questions about the new reorder gallery, checkout flow changes, login/session persistence, deep linking issues, restaurant badging, or general "what's new" inquiries following the app update.

**Resolution:**

1. **Confirm the customer is on iOS and has updated to v1.0.9.**
   - Ask: *"Could you confirm which version of the Sauce app you're using? You can find this in your App Store update history or on the App Store listing."*
   - If they haven't updated yet, direct them to the App Store and note the update may take 24–48 hours to appear following Apple's review.

2. **Reorder Tab / Scrollable Gallery Questions:**
   - Explain that the Reorder tab has been redesigned with a scrollable gallery for quicker access to past meals.
   - If the tab looks unchanged after updating, advise the customer to force-close the app and reopen it. If still unresolved, escalate to Tier 2.

3. **Faster Checkout (Reorder Button Behavior Change):**
   - Clarify that tapping "Reorder" now goes **directly to checkout**, skipping intermediate steps. This is intentional behavior in v1.0.9.
   - If a customer is confused or frustrated by the change, acknowledge the adjustment and highlight that it is designed to save time.

4. **Login / Session Persistence Issues:**
   - In v1.0.9, users should remain signed in while browsing menus and reordering.
   - If a customer reports being repeatedly logged out, confirm they are on v1.0.9. If confirmed and the issue persists, collect device details (iOS version, device model) and escalate to Tier 2 with a bug report.

5. **Deep Linking Issues (Links Not Opening Correct Menu):**
   - Deep linking has been improved in this version. If a customer reports a link not opening the correct menu page, first confirm they are on v1.0.9.
   - If the issue continues after updating, gather the specific link/URL they are using and escalate to the technical team for investigation.

6. **'Highly Rated' Badging / Popularity Scores:**
   - Explain that restaurant popularity scores are now powered by real ratings data, and 'Highly Rated' badges reflect this improved data sourcing.
   - If a restaurant owner contacts support about their badge status changing, escalate to the Restaurant Partner team — do not make manual badge adjustments.

7. **Android / General Platform Questions:**
   - This release (v1.0.9) is for **iOS (Apple App Store) only**. Direct Android users to check the Google Play Store for the latest available version separately.

8. **General Bug Reports Post-Update:**
   - Collect: app version, iOS version, device model, steps to reproduce, and any screenshots if available.
   - Log the report and escalate to Tier 2 / engineering as appropriate.

**Exceptions:**
- This release is iOS-only. Do not apply this entry to Android-related queries.
- Badge status for restaurant partners should never be manually adjusted by CS — always escalate.
- App Store availability may be delayed up to 48 hours post-submission due to Apple's review process; set customer expectations accordingly.
- Users on older iOS versions may not be able to update to v1.0.9 — advise them to check minimum iOS requirements in the App Store listing.

**Approval Required:** No

**Last Updated:** 2026-04-09 — added via product release workflow

---
