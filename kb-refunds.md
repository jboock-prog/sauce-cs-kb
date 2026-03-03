# KB Entries: Refunds & Order Issues

Extracted from: Sauce CC Team Playbook
Source date: Playbook content as of 2025
Last extracted: 2026-02-25
Entry count: 31

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
5. Move the ticket to the Refund Request status, which sends it automatically to the epayments pipeline

**Exceptions:**
- If ePayments returns the ticket saying a refund cannot be processed, ALWAYS send the customer the **End Client: Refund Denial** template — unless ePayments Manager (Yuval) writes "just close" in the notes.

**Approval Required:** No (for submission). ePayments team makes final determination.
**Critical Rule:** NEVER confirm or guarantee a refund to a customer. Use language like: "We will submit a refund request" or "Our Refunds Team will review your order in 1-3 business days."
**Last Updated:** 2026-03-03 — updated

---

## Entry 2: Restaurant-Specific Refund Restrictions — Restaurants That Handle Their Own Refunds

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

**Exceptions:** Delivery issues and cancellations bypass this restriction — those go to Refund Request regardless
**Approval Required:** Yes — restaurant must approve before CC moves to Refund Request.
**Last Updated:** 2026-03-03 — updated

---

## Entry 3: Cancel Order — ASAP Orders

**Title:** Cancel Order — ASAP Orders
**Issue Type:** Refunds & Credits
**Situation:** Customer requests to cancel an ASAP order they just placed.
**Resolution:**
1. Call the restaurant and confirm whether the order can still be canceled (key question: has it been prepared?).

**If the restaurant says it CAN be canceled:**
- Change the order status to "Canceled" in the dashboard → refund the customer in full.

**If the restaurant says it CANNOT be canceled (already prepared or picked up) or does not answer
- Inform the customer that cancellation is not possible.
- For a pickup order and the customer cannot pick up the order → offer to convert to delivery (see B2C-1 for the pickup-to-delivery process).
- If the customer insists on a refund anyway → let them know Customer Support cannot override the restaurant's decision. Direct them to contact the restaurant directly.

**Effects of canceling an order in the dashboard:**
- Delivery is automatically canceled (unless already picked up)
- Dashboard shows "CANCELED ORDER" banner on the receipt
- Customer gets a refund email when the refund is processed

**Exceptions:** If a driver has already picked up the order, the delivery cannot be canceled. No answer from the restaurant = no cancellation.
**Approval Required:** Yes — restaurant must confirm before canceling.
**Last Updated:** 2026-03-03 — updated

---

## Entry 4: Cancel Order — Future Orders

**Title:** Cancel Order — Future Orders
**Issue Type:** Refunds & Credits
**Situation:** Customer requests to cancel a future (pre-scheduled) order.
**Resolution:**

**Is there more than 3 hours between the store opening and the order-ready time?**

**If YES (> 3 hours):**
1. Call the restaurant immediately and ask to cancel the order.
2. Once they approve → cancel and refund the order on the dashboard.
3. Send the restaurant an email + SMS (Template: *Canceled Order - Send Info to Restaurant*) if they answer or do not answer
4. Set a Hubspot reminder for the scheduled date, 1.5 hours before the order time on the dashboard, to remind the restaurant not to prepare the order.
5. Close the ticket.

*If no response from the restaurant, do not cancel the order on the dashboard until confirmation is confirmed

**If NO (< 3 hours):**
1. Tell the customer the cancellation is not guaranteed — you'll need to speak with the restaurant on the scheduled date.
2. Call the restaurant immediately (even today) and ask to cancel.
3. **CRITICAL: Even if the restaurant approves, do NOT cancel the order on the dashboard yet.**
4. Send the restaurant an email + SMS (Template: *Canceled Order - Send Info to Restaurant*).
5. Set a HubSpot reminder for the scheduled date, 1.5 hours before the order time on the dashboard, to remind the restaurant not to prepare the order and to process the refund in the dashboard.
6. Leave the ticket on **Scheduled Future Action**.
7. On the scheduled date:
   - If the restaurant is aware of the cancellation → cancel and refund from the dashboard, close the ticket.
   - If the restaurant doesn't answer or says they already prepared it → email the customer that, unfortunately, the order could not be canceled and will remain active. Close the ticket.

**Example edge case:** Customer calls at 9 PM, store is closed, order is for 10 AM next day, store opens at 9 AM → < 3 hours notice. Do NOT cancel in the dashboard even if you reach them today.

**Exceptions:** None — the 3-hour threshold is firm. Never cancel the dashboard order on the same day for the < 3 hours path.
**Approval Required:** Yes — if < 3 hours, requires restaurant confirmation on the scheduled date.
**Last Updated:** 2026-03-03 — updated

---

## Entry 5: Tip Refund — Delivery Orders

**Title:** Tip Refund — Delivery Orders
**Issue Type:** Refunds & Credits
**Situation:** Customer wants a refund on the tip they paid for a delivery order.
**Resolution:**

**First step always:** Send the customer the `#Automatic Tip` snippet. If they still request a refund, proceed below.

**If the order has already been delivered:**
- We cannot modify the tip — the driver already received the payment.
- Exception: if the customer claims the driver was rude or had a bad experience → send to ePayments to refund CX from COURIER.

**If the order is picked up (driver has the order):**
- We cannot modify the tip.

**If the order is NOT yet picked up:**
1. Before canceling, check if there's a driver close to the restaurant. If so, call to inform them that the driver will change.
2. Cancel the tracking link. Inform the customer that the order is still active — we are only replacing the tracking link with a new one. Use the `#Bad Before Link` snippet.
3. Send a message to `#dispatch-cc` to create a new tracking link with the updated tip amount, or create a Book-a-Driver (BaD) that matches the original order with the updated tip.
4. After creating the BaD tracking, copy the delivery ID from the tracking link to look up the customer-facing tracking link in Find Delivery.
5. Send the ticket to Refunds Request to refund CX from COURIER the difference in the tip amount.

**Exceptions:** If the driver was rude or had a bad experience on a delivered order → send to ePayments to refund CX from COURIER with behavior documented.
**Approval Required:** No — but ePayments makes the final determination on exception cases.
**Last Updated:** 2026-03-03 — updated

---

## Entry 6: Tip Refund — Pickup Orders

**Title:** Tip Refund — Pickup Orders
**Issue Type:** Refunds & Credits
**Situation:** Customer wants a refund on the tip they paid for a pickup order.
**Resolution:**
1. Call the restaurant and confirm they approve the tip refund.

**If restaurant approves:**
- Attach the restaurant's approval to the ticket.
- Move the ticket to Refund Request with the approval attached.

**If the restaurant does not answer:**
- Send the restaurant an email + SMS requesting their approval.
- Leave the ticket in **Pending B2B** (or Scheduled Future Action) and continue reaching out over the next few days.
- After 3 days with no response: send to ePayments and note that the restaurant was unresponsive.

**Exceptions:** Restaurant approval is required — but a no-answer after 3 days can be escalated to ePayments with documentation of outreach attempts.
**Approval Required:** Yes — restaurant must approve before submitting to ePayments.
**Last Updated:** 2026-03-03 — updated

---

## Entry 7: Remove an Item from an Active Order

**Title:** Remove an Item from an Active Order
**Issue Type:** Refunds & Credits
**Situation:** Customer requests to remove one or more items from an order they already placed.
**Resolution:**

**Step 1 — Check if the item is already prepared:**
- Call the restaurant and ask.

**If the item has NOT been prepared yet:**
- Ask the restaurant not to prepare it and confirm approval.
- The restaurant can also use the **"Adjust" button** on their dashboard to remove the item and process the refund on their end. If they do this, no refund ticket is needed.
- If they prefer Support to handle the refund: attach the restaurant's approval to the ticket → move to ePayments.

**If the item HAS already been prepared:**
- We cannot remove it — inform the customer that the item was already made.
- Close the ticket. No refund unless the restaurant volunteers to approve one.

**If it is a future order:**
- Create a separate reminder ticket (leave in "Scheduled future action" column).
- Schedule a Slack message on the ticket with the Slack Reminder Field for the order date, 1.5 hours before pickup time, to remind them not to prepare the removed item.

**Exceptions:** If the item is already prepared, removal is not possible, and no refund is owed unless the restaurant approves.
**Approval Required:** Yes — restaurant confirmation required before sending to ePayments.
**Last Updated:** 2026-03-03 — updated

---

## Entry 8: Order Not Received — Pickup Order

**Title:** Order Not Received — Pickup Order
**Issue Type:** Order Issues
**Situation:** Customer contacts us saying they never received their pickup order (restaurant was closed, order wasn't prepared, customer left due to wait, etc.).
**Resolution:**
1. Check order status on the Sauce Dashboard:
   - **Canceled** → move directly to Refund Request for refund.
   - **Overdue / Completed / Unknown** → call the restaurant. Ask if they were open/closed, and explain that the customer is requesting a refund.
     - Restaurant approves refund → move to Refund Request.
     - Restaurant denies refund → send the **Refund Denial** template to the customer and close the ticket.

**Exceptions:** None documented.
**Approval Required:** Yes — restaurant confirmation needed when status is ambiguous.
**Last Updated:** 2026-03-03 — updated

---

## Entry 9: Order Not Received — Delivery Order Marked Completed

**Title:** Order Not Received — Delivery Order Marked Completed
**Issue Type:** Order Issues
**Situation:** Customer says they never received their delivery order, but the tracking link shows it as completed/delivered.
**Resolution:**
1. Confirm the customer's delivery address and phone number.
2. Check the Proof of Delivery (PoD) photo:
    - Share the PoD with the customer only if it's a valid, clear photo that makes sense.
3. If the POD is invalid,  the customer doesn't recognize the PoD, and there is no clear indication of where the order was left, the order can be eligible for a remake or refund.
4. After investigating:
   - **Customer still wants the order**: check if the restaurant can remake it. If yes, BaD (book-a-driver) and open a refund ticket for the delivery company to reimburse the restaurant.
   - **Customer does not want the order anymore**: open a refund ticket for the customer from the delivery company

How to check PoD :
Go to: https://dashboard.getsauce.com/managers/find-delivery
Enter: Sauce Delivery ID, Invoice ID, Provider Order ID, or Uber ID → click Find Delivery.

**Exceptions:** None documented.
**Approval Required:** No — but document all findings in the ticket before submitting to ePayments.
**Last Updated:** 2026-03-03 — updated

---

## Entry 10: Order Not Received — Delivery Went to Wrong Address

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
   - Send to Refund Request

**Exceptions:** Fault determination changes the resolution entirely — always verify with Tier 2 before deciding.
**Approval Required:** No — but Tier 2 investigation required to assign fault.
**Last Updated:** 2026-03-03 — updated

---

## Entry 11: Order Not Received — Tracking Canceled, "Already Picked Up" Reason

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
**Last Updated:** 2026-03-03 — updated

---

## Entry 12: Order Not Received — Tracking Canceled, Unfulfilled or Restaurant Missed the Order

**Title:** Order Not Received — Tracking Canceled, Unfulfilled or Restaurant Missed the Order
**Issue Type:** Order Issues
**Situation:** Tracking was canceled because the store didn't prepare the order (didn't see it in the system, item unavailable, etc.).
**Resolution:**
1. Contact the restaurant to find out why the order wasn't prepared.
2. **If the restaurant simply missed it but can see it now:**
   - Use judgment: if it wouldn't be extremely late, ask them to make it and BaD.
   - If a lot of time has passed, confirm with the customer first whether they still want the order.
     - Customer still wants it → ask the restaurant to make it and BaD. No refund needed (unless customer later complains about lateness).
     - Customer doesn't want it → do not ask the restaurant to make it; create a refund ticket for the customer.
3. **If the restaurant has the order and prepared it:** BaD and update the customer on the delivery status.

**Exceptions:** If time has passed significantly, always confirm with the customer before asking the restaurant to remake.
**Approval Required:** No formal approval — but confirm customer preference before creating refund.
**Last Updated:** 2026-03-03 — updated

---

## Entry 13: Order Not Received — Restaurant Was Closed, Pickup, Customer Reports After the Fact

**Title:** Order Not Received — Restaurant Was Closed, Pickup, Customer Reports After the Fact
**Issue Type:** Order Issues
**Situation:** Customer contacts CS on a different day to report their pickup order was never received because the restaurant was closed.
**Resolution:**
1. Check order status in Sauce Dashboard:
   - **Canceled** → move to ePayments for refund directly.
   - **Overdue / Completed / Unknown** → call the restaurant and ask if they were open or closed. Explain customer is requesting a refund.

**If restaurant answers:**
- Restaurant approves refund → move to ePayments.
- Restaurant denies refund → send **Refund Denial** template to customer and close ticket.

**If restaurant does not answer:**
- Send the restaurant an email + SMS.
- Leave ticket in **Pending B2B** and continue reaching out.
- After 3 days with no response → send to ePayments with documentation of outreach attempts.

**Exceptions:** No-answer after 3 days = escalate to ePayments with documented outreach.
**Approval Required:** Yes — restaurant confirmation required, or 3-day escalation path.
**Last Updated:** 2026-03-03 — updated

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
**Situation:** Customer complains their order is taking too long or arrived late.
**Resolution:**

**Key rule:** Refundable late = **15+ minutes past the Latest Delivery Time** shown on the tracking link (dropoff time — not pickup time). Dispatch V2 shows both a dynamic ETA and a fixed latest delivery time. Dispatch V1 shows dynamic ETA only.

**If no driver is assigned or driver is far from pickup:**
- Uber/DoorDash → BaD to get a better driver.
- Relay/Motoclick → ask them to assign a new driver.

---

**Step 1 — Apply the correct tier based on what the customer is saying:**

**Tier 0 — Bot auto-response**
Customer selected "ETA seems too long" in the chatflow. Bot explains pre-order vs. live ETA and shows both times. If customer replies or is still concerned → move to Tier 1.

**Tier 1 — ETA looks long or increased after ordering**
Empathize and clarify how ETA recalculates. Use `#eta_explained` or `#eta_increasing`.
- Check tracking. If driver inactive > 10 min → Tier 2. If normal → close politely.

**Tier 2 — Driver appears stuck or going wrong direction**
Customer says driver isn't moving or GPS is frozen. Use `#eta_driver_stuck`.
- Verify in tracking. Contact courier or driver via Slack / Dispatch (`#dispatch-cc`). Update customer once confirmed.

**Tier 3 — Customer says "it's late" but still within the policy window**
ETA hasn't passed yet. Use `#eta_not_late_yet` or `#eta_late_definition` to show exact remaining time.
- Re-check ETA. If still within window → close. If passed → Tier 4.

**Tier 4 — ETA has passed, order not delivered**
Use `#eta_late_delivery`. Apologize and confirm follow-up. Contact courier.
- If > 15 min past Latest ETA → Tier 5.

**Tier 5 — 15+ minutes past Latest ETA, order still in progress**
Use `#eta_refund_referral`. Acknowledge lateness, set expectation for refund review. Monitor until delivery completes, then send to ePayments.

**Tier 6 — Customer wants to cancel because of the delay (order already prepared/picked up)**
Use `#eta_cancel_inflight`. Educate and preserve delivery completion — do not cancel if order is already prepared or picked up. Monitor until delivered, then refer to ePayments for possible refund.

**Tier 7 — Special ETA conditions (long distance, pre-order, BYOC)**
- Long distance → `#eta_long_distance`
- Pre-order → `#eta_preorder`
- BYOC (restaurant-managed delivery) → `#eta_byoc_explained`, contact restaurant if stalled. Escalate to Support + BO/CS.
- Continue normal tracking; no escalation unless order is actually late.

---

**Step 2 — Apply the correct delivery type rules:**

**Sauce Dispatch Delivery:**
- No refund request → empathize, reassure, follow tier above.
- Refund request, order active → tell customer: once delivered, we'll send to ePayments.
- Refund request, order completed → check dropoff time only:
  - 15+ min past Latest ETA → valid. Submit to ePayments.
  - Under 15 min → tell customer it was delivered within estimated time. Cannot guarantee a refund, but we'll review with Payments Team. Send to ePayments.

**Restaurant Delivery:**
- CS cannot assist — restaurant handled the delivery and is responsible for any refund. Direct customer to the restaurant.
- If restaurant is unresponsive → try calling ourselves. If no answer → leave on **Refund Ticket - Waiting on CC**, continue reaching out over the next few days.
  - Restaurant approves → send to ePayments.
  - Restaurant denies or never answers → tell customer we cannot assist, they must take it up with the restaurant.

**Pickup:**
- CS cannot help — we have no visibility into whether the order was ready on time. Ask customer to contact the store directly.

**Cancel Due to Delay:**
- Follow the Cancel ASAP Order protocol (Entry 3).

---

**Escalation rules (quick reference):**
| Condition | Action | Channel |
|---|---|---|
| Driver unresponsive > 15 min | Create BaD or message Dispatch | `#dispatch-cc` |
| ETA > 15 min past latest | Use `#eta_refund_referral`, flag for refund review | ePayments pipeline |
| Customer requests refund | Submit to ePayments; never promise refund | ePayments |
| Courier confirmed fault | Send details to ePayments | ePayments |

**Tone reminders:** Empathize first. Educate calmly — never assign blame. End with confidence, not open loops. Keep replies to 2–3 lines. Follow up proactively if delivery exceeds policy thresholds.

**Exceptions:** Under 15 min late by dropoff time = not eligible for guaranteed refund. Restaurant delivery and pickup late orders are not CS's responsibility.
**Approval Required:** No for Sauce Dispatch. Yes (restaurant approval) for restaurant delivery refunds.
**Last Updated:** 2026-02-26 — fully rebuilt from Process Notes + Confluence ETA Response Flow doc; removed broken links

---

## Entry 15b: ETA Snippets — What to Say to the Customer

**Title:** ETA Complaint — Exact Snippet Text by Situation
**Issue Type:** Order Issues
**Situation:** Agent needs the exact wording to use when responding to an ETA complaint. Use these alongside the tier process in Entry 15.
**Resolution:**

**#eta_explained** — ETA looks longer than expected or changed after ordering:
> "I get it — that longer time can be surprising! The first ETA you see before checkout is just an estimate. Once the restaurant accepts, it updates using live prep and driver info. You'll see two times: the current ETA and the latest possible time — most orders arrive sooner than that."

**#eta_increasing** — ETA keeps going up:
> "Thanks for checking — I know it's frustrating when the time goes up. ETAs adjust automatically based on restaurant prep or driver availability. Once it's picked up, it usually shortens again. I'll keep an eye on it for you."

**#eta_special_event** — Delay caused by weather, holiday, or local event:
> "I understand the delay is frustrating. We are seeing overall delays due to [x]. We are working to have your order delivered as soon as possible despite the circumstances."

**#eta_driver_stuck** — Driver hasn't moved or appears to be going the wrong way:
> "Thanks for flagging — I see the driver hasn't moved in a bit. That can happen if they lose GPS connection temporarily. I'll reach out and make sure it's still on track, then update you shortly."

**#eta_not_late_yet** — Customer says "it's late" but ETA is still within the window:
> "I understand it feels like it's taking a while! Your order's still within the expected delivery window with about [x mins] to go. I'll keep monitoring and let you know if anything changes."

**#eta_late_definition** — Customer insists it's late; confirm still within policy window:
> "I get why it feels late — I just checked and it still has about [x mins] left before it's considered delayed. I'll keep monitoring to be sure it stays on track."

**#eta_late_delivery** — Latest ETA has passed and order not delivered:
> "I can see your order's running a bit late — thanks so much for your patience. I'm checking with the courier to help move things along and will keep you posted."

**#eta_refund_referral** — Order is 15+ minutes past the latest delivery time:
> "I can see your order's already past the latest delivery time — I'm really sorry for the delay. It's running over 15 minutes late, and I'm checking in with the courier for an update. Once it's completed, I'll forward it to our Payments team to review for a possible refund."

**#eta_cancel_inflight** — Customer wants to cancel due to delay but order already prepared/picked up:
> "I completely understand the delay's really frustrating. The order's already prepared and on its way, so it can't be canceled mid-delivery. Once it arrives, I'll forward it to our Payments team to review for a possible refund."

**#eta_long_distance** — Delivery distance is unusually long:
> "I totally get it — that longer ETA can be surprising! Because this is a longer route than usual, the ETA looks higher upfront. Once a driver's on the way, it'll tighten up and you'll see it adjust in real time."

**#eta_preorder** — Order placed in advance, ETA shown before restaurant acceptance:
> "That first ETA is a pre-order estimate — it updates once the restaurant accepts. The live ETA after that is based on actual prep and driver times."

**#eta_byoc_explained** — BYOC (restaurant-managed delivery):
> "The initial delivery estimate uses the settings on their ordering system, so the ETA comes from them directly. It should keep updating as it moves — I can still reach out to confirm if it stalls."

**Exceptions:** None — use the snippet that matches the customer's specific situation.
**Approval Required:** No.
**Last Updated:** 2026-02-26 — extracted from Confluence Delivery ETA Snippets doc

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
- Tell the customer exactly: *"We're checking with the restaurant for their approval. Once they respond, we'll follow their guidelines. If we don't hear back promptly, our management team may review it for you."*
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
- Note: Non-delivery orders (pickup) may have a $1.99 Sauce service fee. This is standard — do not offer a refund.

**Critical rule: NEVER send the customer a Slack fee breakdown or screenshots of internal pricing data.** Use the HubSpot templates only.

**Policy:** CS does NOT process refunds for order fees. These fees are visible on the website when the customer places the order.

**Exceptions:** None — fee refunds are not offered.
**Approval Required:** No.
**Last Updated:** 2026-02-26 — added $1.99 Sauce Fee note for non-delivery orders; added critical rule against sending Slack breakdowns/screenshots

---

## Entry 30: BYOC — Bring Your Own Courier (Third-Party Marketplace Orders)

**Title:** BYOC — Delivery Issues and Refund Process
**Issue Type:** Order Issues / Refunds & Credits
**Situation:** A customer contacts CS about an order that came through a third-party marketplace (e.g., Uber Eats, DoorDash) and was routed to Sauce for delivery. These are BYOC (Bring Your Own Courier) orders — Sauce manages the delivery, but the customer paid the third-party.

**What is BYOC:**
- The customer placed their order on a third-party marketplace (not directly on the restaurant's Sauce-powered website).
- That order is routed to Sauce, and Sauce handles the delivery.
- The restaurant pays Sauce for the delivery service (invoiced). This is the reverse of standard Sauce orders — Sauce does not pay the restaurant; the restaurant pays Sauce.

**Delivery Issues (Late, Driver Stuck, Not Received, etc.):**
- Handle the same way as standard Sauce Dispatch delivery issues — follow Entry 15 (ETA/Late Order) or the relevant issue entry.
- CS manages BYOC delivery support the same as any Sauce-dispatched order.

**Refunds — Critical Difference:**
- The customer **cannot receive a refund through Sauce or ePayments** — they paid the third-party marketplace (Uber Eats, DoorDash, etc.), not Sauce.
- Direct the customer to contact the third-party marketplace directly for any refund.

**If the delivery issue was Sauce's fault:**
- Process a refund request through the **normal HubSpot ePayments pipeline** (same as standard orders).
- The refund flows from the **courier to the restaurant** — this is a credit that reduces what the restaurant owes on their BYOC invoice.
- The customer's refund comes from the third-party marketplace — that is separate and not handled by CS.

**Summary of who gets what:**
| Party | What happens |
|---|---|
| Customer | Contacts third-party marketplace for their own refund |
| Restaurant | Receives a credit on their Sauce BYOC invoice (courier → restaurant) |
| CS action | Submit normal HubSpot refund ticket — courier to restaurant |

**BYOC Snippets — Use these for all BYOC chats:**

**#long delivery BYOC** — Delivery is taking longer than expected:
> "We're sorry the delivery is taking longer than expected. This may be due to the distance from the restaurant. Could you please confirm your address so we can ensure everything is accurate and get your order to you as quickly as possible?"

**#refund request BYOC** — Customer asks for a refund:
> "We're sorry for the inconvenience with your order. While we can assist with delivery issues, refunds are managed directly by the platform where you placed your order."

**#restaurant refund BYOC** — Informing the restaurant a delivery issue has been escalated:
> "The delivery issue has been escalated to our payments team. Applicable refunds will be applied to your next BYOC invoice."

**#invoice BYOC** — Investigating an invoice concern with the restaurant:
> "We'll investigate your concern with our payments team. May we confirm this email address is best for us to follow up?"

**#restaurant refund email** — Email to restaurant about BYOC refunds:
> "Thank you for bringing these refunds to our attention. We will escalate to our ePayments team to apply the appropriate refunds to your BYOC invoice."

**Exceptions:** Delivery issue handling follows standard Entry 15 protocols. Customer refund = third-party marketplace. CS refund ticket = courier to restaurant via HubSpot.
**Approval Required:** No — follow normal ePayments process.
**Last Updated:** 2026-02-26 — added 5 BYOC snippets (#long delivery BYOC, #refund request BYOC, #restaurant refund BYOC, #invoice BYOC, #restaurant refund email)
