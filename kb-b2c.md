# KB Entries: B2C Order Modifications

Extracted from: Sauce CC Team Playbook
Source date: Playbook content as of 2025
Last extracted: 2026-02-25
Entry count: 8

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
1. Cancel the tracking link only.
2. **Make absolutely sure the customer understands: only the delivery is canceled — the order itself is NOT canceled.**
3. Only open a refund ticket for the delivery fee and tip if the customer **explicitly asks** for a refund of those amounts. Do not proactively create a refund ticket.

**Exceptions:** None.
**Approval Required:** No — no restaurant approval needed, no ePayments needed unless customer requests refund of delivery fee/tip.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry B2C-3: Add an Item to an Existing Order

**Title:** Add an Item to an Existing Order
**Issue Type:** Order Issues
**Situation:** Customer wants to add an item to an order they've already placed.
**Resolution:**
1. Look up the item price on the **restaurant's website** (not the menu editor). The upcharge = website price + tax. Do not ask the restaurant for the price.
2. Contact the restaurant and confirm they can add the item.
3. Get the customer's approval for the upcharge amount.
4. Once both restaurant and customer have confirmed, request the upcharge via the ePayments Task.

**Dashboard caveat:** The dashboard details cannot be changed — the item will not appear on the restaurant's POS/Tablet. The restaurant has to remember to add it manually.

**If it's a future order:**
- Keep a ticket open in PENDING — WAITING ON CC TEAM so Support calls the restaurant on the order date to remind them to add the item.
- Schedule a Slack reminder in `#cc-team-chat` with enough lead time before the pickup time.

**Exceptions:** None — both restaurant confirmation and customer approval are always required before upcharging.
**Approval Required:** Yes — restaurant must confirm; customer must approve upcharge.
**Last Updated:** 2026-02-25 — extracted from Playbook

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
