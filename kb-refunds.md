# KB Entries: Refunds & Order Issues

Extracted from: Sauce CC Team Playbook
Source date: Playbook content as of 2025
Last extracted: 2026-02-25
Entry count: 29

---

## Entry 1: General Refund Processing — ePayments Pipeline

**Title:** General Refund Processing — ePayments Pipeline
**Issue Type:** Refunds & Credits
**Situation:** Any time a refund needs to be submitted to the ePayments team for processing.
**Resolution:**
1. Name the ticket: `Resto Name | Cx Name | Date order placed | Delivery ID (if any) | Invoice ID`
2. If there's a BaD (book-a-driver): `Resto Name | Cx Name | Date | Delivery ID | BaD (delivery ID of BaD) | Invoice ID`
3. Ensure the ticket request is complete and updated before sending.
4. Double-check Invoice ID — confirm it matches the correct order (customers sometimes have multiple orders).
5. Move ticket to the ePayments pipeline.

**Exceptions:**
- If ePayments returns the ticket saying a refund cannot be processed, ALWAYS send the customer the **End Client: Refund Denial** template — unless ePayments Manager (Yuval) writes "just close" in the notes.

**Approval Required:** No (for submission). ePayments team makes final determination.
**Critical Rule:** NEVER confirm or guarantee a refund to a customer. Use language like: "We will submit a refund request" or "Our Payments Team will investigate what happened with this order."
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry 2: Restaurant-Specific Refund Restrictions

**Title:** Restaurant-Specific Refund Restrictions — Restaurants That Handle Their Own Refunds
**Issue Type:** Refunds & Credits
**Situation:** Customer has an issue with an order from one of the restaurants on the restricted list. These restaurants handle their own refunds for order quality issues — CS does NOT send those to ePayments without their approval.
**Resolution:**
- If the issue is a **delivery problem** (driver dropped off incorrectly, dispatch bug, wrong bag delivered) OR the customer wants to **cancel their order**: move ticket to ePayments normally.
- If the issue is with the **order itself** (e.g., wrong item but bag has their name): redirect customer to contact the restaurant directly. Use snippet: `#restorefund` or template at HubSpot.

**Restricted Restaurant List (must get restaurant approval for order issues):**
- Pelicana (all branches)
- TheBoil (all branches)
- Falafel Tanami (NOT Greenwich) — contact Snir ("the next google" on Slack) first; if unavailable, call the store
- Mendy's
- Mr Broadway — wants to offer credit, not cash refund
- Vito's and Pizza Piez — speak with owner Joe Shane: +1 (561) 880-7861
- Bo's Bagels
- El Tambo Grill Restaurant — manager Melissa must approve; contact: +1 (786) 246-0062
- Papa Ricco's Restaurant and Pizzeria
- Priscillo Italian Panini — refunds only approved by Antonella
- Baji Baji
- JoJo's NY Style Pizza (Lake Worth & Hollywood) — call restaurant directly for approval
- ALL iPizza NY locations, Vinny's Gluten Free Kitchen, Chelsea Acai Cafe — owner Mahbubur Rahman: +1 (917) 392-5391
- Tacolmos
- Tiberias

**Exceptions:** Delivery issues and cancellations bypass this restriction — those go to ePayments regardless.
**Approval Required:** Yes — restaurant must approve before CS moves to ePayments.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry 3: Cancel Order — ASAP Orders

**Title:** Cancel Order — ASAP Orders
**Issue Type:** Refunds & Credits
**Situation:** Customer requests to cancel an ASAP order they just placed.
**Resolution:**
1. Call the restaurant and confirm whether the order can still be canceled (key question: has a driver already picked it up?).
2. If the restaurant says it **can** be canceled: change the order status to "Canceled" in the dashboard → refund the customer in full.
3. If the restaurant says it **cannot** be canceled (already prepared or picked up): inform the customer that cancellation is not possible.

**Effects of canceling an order in the dashboard:**
- Delivery is automatically canceled (unless already picked up)
- Dashboard shows "CANCELED ORDER" banner on the receipt
- Customer receives SMS notification
- Customer gets a refund email when refund is processed

**Exceptions:** If a driver has already picked up the order, the delivery cannot be canceled.
**Approval Required:** Yes — restaurant must confirm before canceling.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry 4: Cancel Order — Future Orders

**Title:** Cancel Order — Future Orders
**Issue Type:** Refunds & Credits
**Situation:** Customer requests to cancel a future (pre-scheduled) order.
**Resolution:**
1. If there are **more than 3 hours** before the order time: confirm cancellation immediately and process refund.
2. If there are **less than 3 hours** before the order time: explain to the customer that you need the store's approval first and cannot confirm right away.
   - Call the restaurant, send an email, and send an SMS.
   - Schedule a Slack reminder to the `#cc-team-chat` channel (tag @support) to call the restaurant at least 1 hour before scheduled pickup to confirm cancellation.
   - If the restaurant doesn't answer when you first call, send an email and SMS.

**Example edge case:** Customer calls at 9 PM, store is closed, order is for 10 AM next day, store opens at 9 AM → cannot confirm cancellation right away since < 3 hours notice.

**Exceptions:** None — the 3-hour threshold is firm.
**Approval Required:** Yes — if < 3 hours to order time, requires restaurant confirmation.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry 5: Tip Refund — Delivery Orders

**Title:** Tip Refund — Delivery Orders
**Issue Type:** Refunds & Credits
**Situation:** Customer wants a refund on the tip they paid for a delivery order.
**Resolution:**

**If the order is still active and the driver has NOT yet picked up:**
1. Cancel the tracking link.
2. Book a new driver with the correct (lower) tip amount.
3. Open a ticket to ePayments to refund the original tip amount or the difference.

**If the order has already been delivered (or is close to pickup):**
- Do NOT process a tip refund — this is not eligible.
- Send the `#automatic tip` snippet to the customer explaining the tip cannot be refunded.
- No refund can be guaranteed.

**Exceptions:** If the driver was rude or did not perform their job properly, submit a refund request to ePayments. Include a description of the driver's behavior in the ticket request. ePayments makes the final determination.
**Approval Required:** No for active orders. No pre-approval needed for exceptions — submit to ePayments with behavior documented.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry 6: Tip Refund — Pickup Orders

**Title:** Tip Refund — Pickup Orders
**Issue Type:** Refunds & Credits
**Situation:** Customer wants a refund on the tip they paid for a pickup order.
**Resolution:**
1. Call the restaurant and confirm they approve the tip refund.
2. Once confirmed, attach the restaurant's approval to the ticket.
3. Move the ticket to ePayments pipeline with the approval attached.

**Exceptions:** None documented.
**Approval Required:** Yes — restaurant must approve before submitting to ePayments.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry 7: Remove an Item from an Order

**Title:** Remove an Item from an Active Order
**Issue Type:** Refunds & Credits
**Situation:** Customer requests to remove one or more items from an order they already placed.
**Resolution:**
1. Contact the restaurant and get their confirmation/approval to not prepare the item(s). (CS cannot edit the restaurant's dashboard directly.)
2. Attach the restaurant's approval to the ticket.
3. Move the ticket to ePayments to refund the removed item(s).
4. If it is a **future order**, also:
   - Create a separate reminder ticket (leave in "Waiting On CC Team" column)
   - Schedule a Slack message in `#cc-team-chat` tagging @support to call the store on the order date, 1 hour before pickup time, to remind them of the change.

**Exceptions:** None — restaurant approval is always required since CS cannot modify their dashboard.
**Approval Required:** Yes — restaurant confirmation required before sending to ePayments.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry 8: Order Not Received — Pickup Orders

**Title:** Order Not Received — Pickup Order
**Issue Type:** Order Issues
**Situation:** Customer contacts us saying they never received their pickup order (restaurant was closed, order wasn't prepared, customer left due to wait, etc.).
**Resolution:**
1. Check order status on Sauce Dashboard:
   - **Canceled** → move directly to ePayments for refund.
   - **Overdue / Completed / Unknown** → call the restaurant. Ask if they were open/closed, and explain that the customer is requesting a refund.
     - Restaurant approves refund → move to ePayments.
     - Restaurant denies refund → send the **Refund Denial** template to the customer and close the ticket.

**Exceptions:** None documented.
**Approval Required:** Yes — restaurant confirmation needed when status is ambiguous.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry 9: Order Not Received — Delivery, Tracking Shows "Completed"

**Title:** Order Not Received — Delivery Order Marked Completed
**Issue Type:** Order Issues
**Situation:** Customer says they never received their delivery order, but the tracking link shows it as completed/delivered.
**Resolution:**
1. Confirm the customer's delivery address.
2. Check the Proof of Delivery (PoD) photo:
   - PoD is available for **Uber** and **Relay** deliveries. **DoorDash** may have it occasionally.
   - Share the PoD with the customer only if it's a valid, clear photo that makes sense.
3. If the customer doesn't recognize the PoD OR there is no PoD, and they confirm the address on the order was correct: contact the delivery company (or ask the Dispatch team to contact them).
4. After investigating:
   - **Customer still wants the order**: check if the restaurant can remake it. If yes, BaD (book-a-driver) and open a refund ticket for the delivery company to reimburse the restaurant.
   - **Customer does not want the order anymore**: open a refund ticket for the customer.

**How to check PoD (V2 Dispatch):**
Go to: https://dashboard.getsauce.com/managers/find-delivery
Enter: Sauce Delivery ID, Invoice ID, Provider Order ID, or Uber ID → click Find Delivery.

**Exceptions:** None documented.
**Approval Required:** No — but document all findings in the ticket before submitting to ePayments.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry 10: Order Not Received — Delivery, Wrong Address

**Title:** Order Not Received — Delivery Went to Wrong Address
**Issue Type:** Order Issues
**Situation:** Customer says they didn't receive their order and the delivery address was wrong.
**Resolution:**
1. Confirm with the customer whether the address on the order was incorrect.
2. Check with Tier 2 to determine: did the customer enter the wrong address, or did the Sauce system change it? Add their findings and a Slack thread link to the ticket notes.
3. **If it was the customer's fault:**
   - Do NOT offer redelivery.
   - You may move to ePayments if the customer confirms they didn't receive the order, but explicitly tell them a refund is not guaranteed because the order was delivered to the address they entered.
4. **If it was the system's fault:**
   - Offer redelivery.

**Exceptions:** Fault determination changes the resolution entirely — always verify with Tier 2 before deciding.
**Approval Required:** No — but Tier 2 investigation required to assign fault.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry 11: Order Not Received — Canceled Tracking, Driver Says Order Was Already Picked Up

**Title:** Order Not Received — Tracking Canceled, "Already Picked Up" Reason
**Issue Type:** Order Issues
**Situation:** The delivery tracking link was canceled and the reason given was "order was already picked up." Customer says they never received it.
**Resolution:**
1. Contact the customer and ask if they received the order.
2. If they did NOT receive it: check with the restaurant whether the order is still at the store.
   - If the order is still at the store → BaD (book-a-driver) and inform the customer.
   - If the order is NOT at the store, inform the customer there was an issue, then ask if they still want it:
     - **Customer still wants order**: check if restaurant can remake. If yes, BaD and open a refund ticket for the delivery company to reimburse the restaurant for making the food twice.
     - **Customer doesn't want it**: open a refund ticket for the customer.

**Exceptions:** Do not blindly trust the delivery company's "already picked up" reason — always verify with the customer first.
**Approval Required:** No — unless restaurant is on the restricted refund list.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry 12: Order Not Received — Canceled Tracking, Order Unfulfilled or Restaurant Didn't See It

**Title:** Order Not Received — Tracking Canceled, Unfulfilled or Restaurant Missed the Order
**Issue Type:** Order Issues
**Situation:** Tracking was canceled because the store didn't prepare the order (didn't see it in the system, item unavailable, etc.).
**Resolution:**
1. Contact the restaurant to find out why the order wasn't prepared.
2. **If the restaurant simply missed it but can see it now:**
   - Use judgment: if it wouldn't be extremely late, ask them to make it and BaD.
   - If a lot of time has passed, confirm with the customer first whether they still want the order.
     - Customer still wants it → ask restaurant to make it and BaD. No refund needed (unless customer later complains about lateness).
     - Customer doesn't want it → do not ask restaurant to make it; create a refund ticket for the customer.
3. **If the restaurant has the order and prepared it:** BaD and update the customer on the delivery status.

**Exceptions:** If time has passed significantly, always confirm with the customer before asking the restaurant to remake.
**Approval Required:** No formal approval — but confirm customer preference before creating refund.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry 13: Order Not Received — Restaurant Was Closed (Pickup, Customer Reports Later)

**Title:** Order Not Received — Restaurant Was Closed, Pickup, Customer Reports After the Fact
**Issue Type:** Order Issues
**Situation:** Customer contacts CS on a different day to report their pickup order was never received because the restaurant was closed.
**Resolution:**
1. Check order status in Sauce Dashboard:
   - **Canceled** → move to ePayments for refund directly.
   - **Overdue / Completed / Unknown** → call the restaurant and ask if they were open or closed. Explain customer is requesting a refund.
     - Restaurant approves refund → move to ePayments.
     - Restaurant denies refund → send **Refund Denial** template to customer and close ticket.

**Exceptions:** None documented.
**Approval Required:** Yes — restaurant confirmation required.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry 14: Order Not Received — Restaurant Was Closed (Real-Time)

**Title:** Order Not Received — Restaurant Was Closed, Real-Time Report (Pickup or Delivery)
**Issue Type:** Order Issues
**Situation:** Customer or delivery company reports in real time that the restaurant appears to be closed.
**Resolution:**
1. Call the restaurant at least 3-4 times, at different times if possible, to verify closure.
2. **If restaurant confirms they're open**: check if they prepared the specific order. Based on their response, either send refund denial or move to ePayments.
3. **If restaurant does not answer**: treat the restaurant as closed.
   - Close the restaurant until next opening hours on the Sauce Dashboard.
   - Send the restaurant the "Store Reported as Closed / Closed Resto" template and CC the CS owner.
   - Check for other open orders for the day — create tickets for those and check with each customer if they received their order.
   - Move the original customer's ticket to ePayments for a refund.
4. **For delivery specifically**: if the end customer did NOT report it (you learned from the delivery company), confirm with the customer before moving to refunds.

**Exceptions:** Delivery closure reported by delivery company (not customer) — must confirm with customer before creating refund ticket.
**Approval Required:** No — if restaurant confirmed closed (or no answer after multiple attempts).
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry 15: ETA Issue — Delivery Order Was Late

**Title:** ETA Complaint — Late Delivery
**Issue Type:** Order Issues
**Situation:** Customer claims their delivery order arrived late.
**Resolution:**
1. Verify the complaint is valid: a delivery is only considered "late" if it arrived **15+ minutes past the latest arrival time** shown on the B2C tracking link.
2. If the order was less than 15 minutes late: the complaint does not qualify for a refund — explain to the customer.
3. If the order was 15+ minutes late: refer to the ETA Response Flow and Delivery ETA Snippets pages in Confluence for the appropriate response steps.

**References:**
- ETA Response Flow: https://say2eat.atlassian.net/wiki/spaces/SD/pages/1517027335/ETA+Response+Flow
- Delivery ETA Snippets: https://say2eat.atlassian.net/wiki/spaces/SD/pages/1517092877/Delivery+ETA+Snippets+-+New

**Exceptions:** Orders less than 15 minutes late are not eligible.
**Approval Required:** No — but must confirm lateness using tracking link.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry 16: ETA Issue — Pickup Order Was Late

**Title:** ETA Complaint — Late Pickup
**Issue Type:** Order Issues
**Situation:** Customer claims their pickup order was not ready on time.
**Resolution:**
- CS cannot assist with late pickup orders — we have no visibility into whether the order was ready on time.
- Direct the customer to contact the restaurant directly for further assistance.

**Exceptions:** None — this is a firm limitation.
**Approval Required:** N/A
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry 17: Order Arrived Early (Future Orders Only)

**Title:** Order Delivered Earlier Than Scheduled
**Issue Type:** Order Issues
**Situation:** Customer complains their order was delivered earlier than the scheduled time. Only applies to future (pre-scheduled) orders.
**Resolution:**
1. Check the Dispatch Service to confirm the order was actually delivered early.
2. If the delivery provider is **DoorDash**: call DoorDash directly to request a refund over the phone.
3. If the customer explicitly requests a refund/compensation: send ticket to ePayments.
4. If the customer is just reporting the issue without requesting a refund: apologize for the inconvenience and report the issue to the dispatch team. No refund ticket needed.

**Exceptions:** Does not apply to ASAP orders — ASAP means "as soon as possible" so there is no guaranteed time window.
**Approval Required:** No.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry 18: Excessive Wait Time (Driver-Side)

**Title:** Excessive Wait Time — Driver Reported Delay
**Issue Type:** Order Issues
**Situation:** The delivery tracking was canceled or flagged because the store did not prepare the order on time.
**Resolution:**
1. Contact the store to confirm they are making the order and get an estimated ready time.
2. BaD (book-a-driver) once the order will be ready.
3. Update the customer on the delivery status proactively — make it clear the order has not been canceled.

**Exceptions:** None documented.
**Approval Required:** No.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry 19: Driver App Issue — Order Shows Canceled

**Title:** Order Shows Canceled — Driver App Issue
**Issue Type:** Order Issues
**Situation:** Delivery tracking shows canceled and the driver claims it was due to an app issue (couldn't mark order as completed). Customer may or may not have received the order.
**Resolution:**
1. Contact the customer and confirm whether they actually received the order.
2. If they **received** it: no action needed.
3. If they **did not receive** it:
   - Check if a redelivery is possible, OR
   - Process a refund if the customer doesn't want a redelivery.

**Exceptions:** 99% of the time these orders were actually delivered — always confirm with the customer before assuming non-delivery.
**Approval Required:** No.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry 20: Missing Item — Add-on or Ingredient

**Title:** Missing Item — Add-on or Ingredient (e.g., Missing Sauce, Missing Avocado)
**Issue Type:** Order Issues
**Situation:** Customer reports a missing add-on or ingredient that was part of their order (not a standalone item). Examples: missing salmon in a salad, missing sauce, missing avocado add-on.
**Resolution:**
**Step 1 — Confirm the item was actually ordered:**
- Check HubSpot ticket details (left sidebar, scroll down for item breakdown). Refresh if details are missing.
- Alternatively, search the Slack `#orders` channel by customer name, email, or order ID. Verify restaurant name, order date, and item breakdown.
- Double-check location, name, and date before proceeding.

**Step 2 — Request a photo:**
- If photo provided → submit to ePayments (unless restaurant is on the restricted list).
- If no photo → let the customer know a photo helps, but you'll forward the request to ePayments for review. Clarify refund is not guaranteed.

**Step 3 — Restricted restaurant handling:**
- If the restaurant handles their own refunds: call for approval. If no answer, send an email.
- Tell the customer: "We're checking with the restaurant for their approval. Once they respond, we'll follow their guidelines. If we don't hear back promptly, our management team may review it."
- Do NOT call restaurants that are NOT on the mandatory-approval list for minor ingredient issues.

**Exceptions:** Restaurants on the restricted refund list require approval before sending to ePayments.
**Approval Required:** Only if restaurant is on restricted list.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry 21: Missing Item — Standalone Main or Side Item

**Title:** Missing Item — Standalone Main or Side Item (e.g., Missing Entire Pizza, Missing Combo Drink)
**Issue Type:** Order Issues
**Situation:** Customer reports a completely missing standalone item from their order (not an add-on). Examples: missing entire pizza, missing combo drink.
**Resolution:**
**Step 1 — Confirm the item was ordered:**
- Same as Entry 20 — check HubSpot or Slack `#orders`.

**Step 2 — Request photo and verify:**
- If item appears in the photo → let the customer know it's visible in the picture.
- If item does not appear in the photo, or no photo was provided → check the PoD image if available, then proceed.

**Step 3 — Determine: Remake or Refund:**

*Remake (Pickup or Restaurant Delivery):*
1. Call the restaurant to find out if the item was sent or forgotten.
2. If courier error → move ticket to ePayments to compensate restaurant for remaking.
3. If restaurant approves remake:
   - Inform the customer.
   - Pickup: customer can collect the missing item.
   - Delivery: request driver via Slack `#dispatch-cc` or BaD if unavailable.

*Refund:*
1. Confirm all order details and document in ticket notes.
2. Move ticket to ePayments (unless restaurant handles own refunds).
3. If restaurant does their own deliveries: call for approval before sending to ePayments.

**Exceptions:** Restaurant-delivered orders require mandatory restaurant call for approval (see Entry 22).
**Approval Required:** Depends — restaurant approval needed if on restricted list or restaurant handles delivery.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry 22: Missing Item — Restaurant In-House Delivery

**Title:** Missing Item — Restaurant Handles Their Own Delivery
**Issue Type:** Order Issues
**Situation:** Customer reports a missing item on an order that was delivered by the restaurant's own drivers (not Uber/DoorDash/Relay).
**Resolution:**
- Calling the restaurant to get approval is **mandatory** before processing any refund for missing items on restaurant-delivered orders.
- Do not submit to ePayments without restaurant confirmation.

**Exceptions:** None — calling the restaurant is always required for in-house delivery missing item claims.
**Approval Required:** Yes — restaurant approval required.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry 23: Wrong Order or Wrong Item — Pickup

**Title:** Wrong Order / Wrong Item Received — Pickup
**Issue Type:** Order Issues
**Situation:** Customer received the wrong order or wrong item on a pickup order.
**Resolution:**
1. Ask for a photo of the order received.
2. Compare the photo to the order details to confirm the complaint is valid.
3. If complaint is confirmed valid → move ticket to ePayments.
4. If customer has no photo:
   - Thank them for the feedback.
   - If they explicitly ask for a refund: explain a photo is needed to proceed.
   - If they insist without a photo: move to ePayments anyway — the ePayments team will decide whether to refund.

**Special Case — Notes not followed (e.g., customer asked for no onions in order notes):**
- Always direct customer to the restaurant directly. CS cannot guarantee restaurants follow order notes.

**Note (internal):** Wrong ingredients (not missing, but wrong) → move to refunds without restaurant approval.

**Exceptions:** If the customer did not follow up with a photo and insists, escalate to ePayments for final decision.
**Approval Required:** No — ePayments decides.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry 24: Wrong Order or Wrong Item — Delivery

**Title:** Wrong Order / Wrong Item Received — Delivery
**Issue Type:** Order Issues
**Situation:** Customer received the wrong order or wrong item on a delivery order.
**Resolution:**
1. Ask for a photo of the order received. Ideally, a photo of the receipt attached to the bag (helps determine if it was a restaurant or delivery error).
2. Compare photo to order details to confirm the complaint is valid.
3. Contact the delivery company (or ask dispatch team to contact them) for more information from the driver.
4. Check if the customer still wants the correct order:
   - **Does not want the food** → open a refund ticket for receiving the wrong order.
   - **Still wants the food** → check with the restaurant and BaD.
     - Restaurant remaking (original order no longer at store) → open a refund ticket for the restaurant (making food twice).
     - Restaurant not remaking (original order still at store) → no refund needed.

**Exceptions:** None documented.
**Approval Required:** No (unless restaurant is on restricted list).
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry 25: Damaged Order — Pickup

**Title:** Damaged Order — Pickup
**Issue Type:** Order Issues
**Situation:** Customer reports their pickup order was damaged or the delivery was messy.
**Resolution:**
- CS cannot assist with damaged pickup orders.
- Advise the customer to contact the restaurant directly.

**Exceptions:** None — CS has no authority over restaurant packaging for pickup orders.
**Approval Required:** N/A
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry 26: Damaged Order — Delivery

**Title:** Damaged Order — Delivery
**Issue Type:** Order Issues
**Situation:** Customer reports their delivery order arrived damaged or messy.
**Resolution:**
1. Ask for a photo of the damaged order.
2. Confirm the damage is visible and the complaint is valid.
3. Check if the customer wants the order remade:
   - **Does not want it remade** → open a refund ticket for receiving a damaged order.
   - **Still wants the food** → check if the restaurant can remake it and BaD. If restaurant remakes it → open a refund ticket for the restaurant (making food twice).

**Exceptions:** None documented.
**Approval Required:** No (unless restaurant is on restricted list).
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry 27: Food Quality Complaint — Non-Safety Issues

**Title:** Food Quality Complaint — Non-Safety (Cold, Undercooked, Poorly Prepared)
**Issue Type:** Order Issues
**Situation:** Customer complains about food quality that is not a safety risk — e.g., food was cold, undercooked, or poorly prepared.
**Resolution:**
1. Send the customer the `#foodqualityB2C` snippet informing them:
   - You've shared their complaint with the restaurant.
   - The restaurant will follow up if needed.
   - For faster resolution, they may contact the restaurant directly.
2. Send the restaurant the **"B2B EMAIL: Food Quality Issue Notification"** template with the customer's feedback details.
3. Close the ticket after both messages are sent.
4. If the restaurant responds and requests further action → reopen the ticket and follow their guidance.

**Do NOT use this flow for:** Reports of illness, mold, spoilage, or expired products — those are food safety issues (see Entry 28).

**Exceptions:** CS cannot independently refund for food quality. Only the restaurant can initiate further action.
**Approval Required:** No — but restaurant may respond requesting a refund be issued.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry 28: Food Quality Complaint — Food Safety (Illness, Mold, Spoilage)

**Title:** Food Safety Complaint — Illness, Mold, or Spoiled Food
**Issue Type:** Escalation Paths
**Situation:** Customer reports a food safety issue — illness after eating, visibly moldy food, expired or spoiled food, or any suggestion the food posed a health risk. These must be treated with urgency.
**Resolution:**
1. **Immediately notify the restaurant** via their preferred contact channel (text, call, or dashboard message).
2. Inform them of the customer's report and the specific nature of the issue.
3. Ask for their guidance on how to proceed.
4. Document all outreach clearly in the ticket for visibility and audit purposes.

**Do NOT handle under the general food quality flow.** This requires immediate escalation.

**Exceptions:** None — all food safety reports require immediate restaurant notification.
**Approval Required:** Yes — restaurant must be engaged immediately; they determine next steps.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry 29: Fees and Price Difference Complaints

**Title:** Fees and Price Difference Complaints — No Refunds on Service Fees
**Issue Type:** Policies & Rules
**Situation:** Customer complains about fees charged by Sauce or claims the price differs from the in-store price.
**Resolution:**

**If the customer is confused about price difference (in-store receipt vs. online order):**
- Use the **"Sauce Fees / Pricing Difference"** HubSpot template.
- Key explanation: "The printed receipt is from the store's cashier and doesn't properly reflect online menu prices. The correct prices, including fees and tips, show on your email confirmation."

**If the customer is complaining about being charged fees:**
- Use the **"Sauce Fees Explanation"** HubSpot template.
- Key explanation: "Our platform has a service fee per order. This small fee goes toward maintaining customer support while covering all issues that arise to ensure your order arrives safely and on time."

**Policy:** CS does NOT process refunds for order fees. These fees are visible on the website when the customer places the order.

**Exceptions:** None — fee refunds are not offered.
**Approval Required:** No.
**Last Updated:** 2026-02-25 — extracted from Playbook
