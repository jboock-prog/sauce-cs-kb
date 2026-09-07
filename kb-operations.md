# KB Entries: Support Operations — Guidelines, Dispatch, ePayments

Extracted from: Sauce CC Team Playbook
Source date: Playbook content as of 2025
Last extracted: 2026-02-25
Entry count: 40

---

## Entry OPS-1: Inbound Call Handling — Script and Standards

**Title:** How to Handle Inbound Calls
**Issue Type:** Policies & Rules
**Situation:** Agent receives an inbound call from a customer or restaurant.
**Resolution:**

**Greeting script (inbound):**
> "Hi, thank you for calling Sauce Support, my name is [name], how can I help you?"

**Before working any order issue:**
- Always confirm you are looking at the correct order before acting on a customer's claim.
- Ask the customer for their order ID / invoice ID (visible on their confirmation email), their name, or the restaurant name to locate the order.

**If you call someone and they don't pick up (no voicemail):**
- A ticket may not be automatically created.
- Take a screenshot of the attempted call in Aircall and paste it as a note in the ticket for logging purposes.

**Exceptions:** None.
**Approval Required:** No.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry OPS-2: Outbound Call Handling — Recording Disclosure

**Title:** Outbound Call Recording Disclosure — Required Script
**Issue Type:** Policies & Rules
**Situation:** Agent is making an outbound call to a customer or restaurant.
**Resolution:**

**Informing the caller of recording is OBLIGATORY on every outbound call.** After introducing yourself, say:

**English:**
> "We just want to inform you that this call is being recorded for training and quality assurance purposes, is that OK with you?"

**Spanish:**
> "Le informo que esta llamada se grabará para fines de calidad, ¿está de acuerdo?"

**Exceptions:** None — this is required on every outbound call without exception.
**Approval Required:** No.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry OPS-3: How to Handle WhatsApp Messages

**Title:** How to Handle WhatsApp Messages
**Issue Type:** 
**Situation:** A customer or restaurant contacts CS via WhatsApp. WhatsApp messages do not auto-create HubSpot tickets.
**Resolution:**
1. WhatsApp is auto assigned. Prioritize as it is usually a restaurant or internal partner with an urgent need.
2. Acknowledge you're working on it and provide updates as needed.
3. **Never create tickets directly from the WhatsApp conversation.** Create a **separate ticket from scratch** in HubSpot for each issue/order, and paste the original case ticket number into the Notes section.
4. Set the ticket **Source to "Manual WhatsApp"** — this separates active WhatsApp conversations from tickets created to document issues.
5. Add a comment on the inbox linking to the ticket so the connection is visible.
6. **Do NOT unassign yourself from the WhatsApp chat.** When the conversation is finished, **close the ticket** — if the customer comes back, it auto-assigns to someone available and moves to New. (Procedure changed 2026-06-03; the old "unassign yourself" rule no longer applies.)
7. The WhatsApp ticket itself should only ever be **closed** once processed — do not treat it as a regular ticket.

**Ticket naming:** WhatsApp tickets are renamed to the format `WA - Restaurant Name - Contact Name`. If you recognize a WA ticket (small WhatsApp icon on the interaction), rename it to this format. My Chats has been renamed **My New Conversations** and combines WhatsApp and Chat.

**Converting to email:** If you change a WhatsApp conversation to email, the WhatsApp transcript is attached by default.

**Exceptions:** None — a separate manual ticket must always be created; WhatsApp will not auto-generate one.
**Approval Required:** No.
**Last Updated:** 2026-07-16 — new close-don't-unassign procedure, Manual WhatsApp source, WA naming format, separate ticket per issue, transcript auto-attach

---

## Entry OPS-4: Handling Negative Survey Tickets

**Title:** How to Handle Negative Customer Survey Tickets
**Issue Type:** Policies & Rules
**Situation:** A survey ticket (1–3 stars) appears in the SURVEYS REQUESTS column. Surveys are not auto-assigned — agents must check this column throughout their shift.
**Resolution:**

**Ticket naming:** "Survey request from Restaurant: [Restaurant name], End client name: [Customer name]"

**Step 1 — Validate the claim.** Check if the complaint is legitimate (e.g., if they say an item was missing, confirm they actually ordered it).

**Step 2 — Determine what CS can handle:**

| Complaint Type | Pickup | Delivery |
|---|---|---|
| Wrong order | Yes | Yes |
| Missing item | Yes | Yes |
| Damaged order | No | Yes |
| Tip | Yes | Yes |
| Lateness | No | Yes |
| Rude staff | No | — |
| Never received | Yes | Yes |
| Food quality | No | No |

**If the claim is NOT something CS can handle** (rude staff, order notes not followed, etc.):
- Send the "Survey response — disappointed customer (didn't ask for a refund)" template.

**For food quality issues:**
- Send the customer the "B2C EMAIL: Food Quality Issue Notification" template.
- Send the restaurant the "B2B EMAIL: Food Quality Issue Notification" template.
- Close the ticket. Reopen if the restaurant requests further action.

**If the claim IS valid and actionable:**
- Rename the ticket: `Restaurant Name | End customer name | Date | Delivery ID | Invoice ID`
- Update the ticket request with the complaint details.
- Paste the original survey in a ticket note.
- Work it like a standard ticket using appropriate templates:
  - First response
  - Wrong item/order (asking for photo)
  - Missing item (asking which item)
  - Missing item (asking for photo)
  - Damaged order (asking for photo)
  - Checking if the order was received

**To view photos from surveys:**
- Paste the long URL in the ticket into a browser tab, OR
- Search for the survey in Slack by customer name or email and click "Photo link."

**Survey send timing (changed 2026-08-06):** For non-dispatch restaurant delivery orders, the delay between order placement and the post-order survey send has been extended, so customers no longer receive the feedback request before their order has actually been delivered. Expect fewer "I got a survey before my food" complaints on those orders.

**Exceptions:** None.
**Approval Required:** No.
**Last Updated:** 2026-08-24 — added post-order survey timing change via KB Policy Scan (source: Ella Bar-Or, 2026-08-06); 2026-02-25 — extracted from Playbook

---

## Entry OPS-5: Ticket Follow-Up — Waiting for Customer Response

**Title:** Ticket Follow-Up Policy — Waiting on End Customer
**Issue Type:** Policies & Rules
**Situation:** A ticket is waiting for a response from an end customer.
**Resolution:**
- Send **2 follow-up attempts** to the customer with a **3-day gap** between each (via phone call, email, and chat).
- If the customer still doesn't respond: close the ticket.
- If a restaurant originally asked you to contact the customer: inform the restaurant that you tried multiple times with no response, then close the ticket.
- If ePayments is waiting on the customer response: post in **#cc-epayments-connect** with a short summary that you tried to reach the customer multiple times without success, and that you are closing the ticket.

**Exceptions:** None.
**Approval Required:** No.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry OPS-6: Ticket Follow-Up — Waiting for Restaurant Response

**Title:** Ticket Follow-Up Policy — Waiting on Restaurant
**Issue Type:** Policies & Rules
**Situation:** A ticket is waiting for a response from a restaurant.
**Resolution:**
- If the restaurant has not responded after **2 outreach attempts on 2 consecutive days**: send the ticket to Refund Request (refunds).
- **Exception:** If the restaurant is on the list of restaurants that handle their own refunds, do not send to Refund Request. Instead, reach out in the Support New channel and tag CS.

**Exceptions:** Restricted refund restaurants follow a different path — tag CS instead of sending to Refund Request.
**Approval Required:** No.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry OPS-7: Outside Operating Hours — Ticket Tagging

**Title:** Tagging Tickets Received Outside Operating Hours
**Issue Type:** Policies & Rules
**Situation:** A ticket was received between 1 AM and 8 AM EST (outside operating hours) and should not count against SLA metrics.
**Resolution:**
- On the ticket, set the "Outside of operating hours" property to **YES**.
- This prevents after-hours tickets from impacting SLA measurements.

**Operating hours:** 8 AM – 1 AM EST, Monday through Sunday.

**Exceptions:** Only applies to tickets received during 1 AM – 8 AM.
**Approval Required:** No.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry OPS-8: Moving a Ticket to Another Team's Pipeline

**Title:** How to Move a Ticket to Another Team's Pipeline (CS, BO, Menu, OB)
**Issue Type:** Policies & Rules
**Situation:** A ticket needs to be routed to CS, BO, Menu, or OB after being filled out with the correct category.
**Resolution:**

**For CS, BO, Menu, or OB tickets:**
- Change the ticket status to **"CS, BO, Menu (Check Category)"**
- The category assigned to the ticket determines which pipeline and column it goes to automatically.
- Example: a ticket with category "BO B2B: Website Changes" will route to the BO pipeline when the status is changed.

**For ePayments (refund) tickets:**
- Change the ticket status to **"Refund Request"**
- All required categories will appear before saving — ensure they are filled in.

**DO NOT** manually drag tickets between pipelines — always use the status change to trigger automation.

**Exceptions:** None — manual pipeline moves bypass automation and must not be used.
**Approval Required:** No.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry OPS-9: "Could Not Deliver" Orders — Customer Fault

**Title:** Could Not Deliver — Customer Was at Fault (Wrong Address, Unresponsive)
**Issue Type:** Order Issues
**Situation:** A delivery is marked "could not deliver" because the customer was unreachable, gave the wrong address, or was unresponsive when the driver tried to deliver.
**Resolution:**

**Always do first:**
- Call the delivery company — do not rely on the #dispatch_orders channel alone. Always get more detail.
- Confirm the customer's address and phone number.
- Ask the customer if the courier called or texted them.

**If the order was returned to the restaurant and the customer still wants it:**
- Customer must pay a new delivery fee (shown on the BaD feature in the dashboard).
- Book the new driver with **no tip** unless the customer agrees to be upcharged for one.
- Confirm the customer's correct address and phone number before booking.
- **Do not book a driver until the customer explicitly agrees to pay the new delivery fee.**

**If the order was NOT returned to the restaurant and the customer still wants it:**
- Do not ask the restaurant to remake the order.
- Apologize and explain that because they were unresponsive, you cannot arrange a remake.
- Tell the customer you will check with the Payments Team but cannot guarantee a refund.

**If the customer no longer wants the order (returned or not):**
- Explain you cannot guarantee a refund since they were unresponsive, but you will check with the Payments Team and follow up by email.

**Customer snippet:** #couldnotdelivercx

**Exceptions:** None — customer fault means no free redelivery and no guaranteed refund.
**Approval Required:** No — but ePayments makes the final refund determination.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry OPS-10: "Could Not Deliver" Orders — Driver Fault

**Title:** Could Not Deliver — Driver Was at Fault (Couldn't Find Address, No Secure Dropoff)
**Issue Type:** Order Issues
**Situation:** A delivery is marked "could not deliver" and the delivery company confirms it was the driver's fault.
**Resolution:**

**Always confirm with the delivery company that it was driver fault — not customer fault.**

**If the order was returned and the customer still wants the food:**
- Book a new driver free of charge, matching the original tip amount.

**If the order was returned and the customer does not want the food:**
- Move to Refund Request for a refund.

**If the order was NOT returned and the customer wants the food:**
- Do not have the restaurant remake the food.
- Apologize and tell the customer you will forward the case to Payments for review and follow up by email.
- **Uber exception only:** If the customer insists on a remake and the order was not returned:
  - Call Uber and verify the status is "Returned" (not "Still on the way to return").
  - If Uber confirms return but the restaurant says they didn't receive it back: you can ask the restaurant to remake. Attach all call records to the ticket.
  - If Uber says it's still being returned: do not ask for a remake — the refund process will likely be cleaner after return.

**If the order was NOT returned and the customer does not want the food:**
- Move to Refund Request for a refund.

**Exceptions:** Uber-specific exception for contested non-returns — see above.
**Approval Required:** No — but ePayments makes the final refund determination.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry OPS-11: Book-a-Driver (BaD) Tip Guide

**Title:** Book-a-Driver (BaD) — Tip Amount by Scenario
**Issue Type:** Policies & Rules
**Situation:** Agent needs to know what tip amount to use when booking a replacement driver.
**Resolution:**

| Scenario | Fault | Tip for BaD |
|---|---|---|
| Canceled order — excessive wait, restaurant didn't prepare/see order | Restaurant | Match original tip (Relay/DoorDash). **$0 for Uber.** |
| Canceled order — order stolen, delivered wrong address, picked up by wrong person | Courier | Match original tip |
| Missing item — redelivery | Either | $3 regardless of fault |
| Large order — two tracking links, restaurant request | Restaurant | $5 (confirm) |
| Could not deliver — customer fault | Customer | $0 (unless customer agrees to tip upcharge) |
| Could not deliver — courier fault | Courier | $0 |
| Wrong address on order | — | $0 |
| Wrong order received — restaurant fault | Restaurant | $3 (confirm) |
| Wrong order received — courier fault | Courier | $3 |
| Damaged order — redelivery | Courier (always) | $3 if restaurant remade |
| Late order — no driver assigned, original had tip | — | Match original tip |
| Late order — no driver assigned, no tip, large order | — | $5 |
| Late order — no driver assigned, no tip, small order | — | $3 |

**Exceptions:** Note that some tip amounts are marked with "?" in the original — confirm with a team lead if unsure for large order scenarios.
**Approval Required:** No.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry OPS-12: Booking a Catering Driver via Dlivrd (Expedite)

**Title:** How to Book a Catering Driver Through Dlivrd (Expedite)
**Issue Type:** Policies & Rules
**Situation:** A catering order needs a driver booked through the Dlivrd/Expedite platform.
**Resolution:**

> **Known bug — use this process, not the dashboard (added 2026-07-30):** The in-dashboard "Catering BaD" (Book-a-Driver) flow currently sends deliveries as **standard**, not catering. Until that is fixed, **all** catering driver bookings must go through the Expedite/Dlivrd process below rather than the dashboard BaD feature. Remove this caveat once the bug is confirmed fixed.

**Login:** https://brand.expedite.io/ — see REF-6 for credentials. (The older https://expedite.dlivrd.io/dashboard URL still works, but `brand.expedite.io` is the current one; prefer it.)

**To book a driver — click "Create Order" (top left green button):**

*Pickup section:*
- **Address:** Select restaurant from dropdown.
- **Date & Time:** Use the date from Sauce Dashboard. Set the time **45 minutes earlier** than the dashboard time (e.g., dashboard shows 6 PM → set pickup for 5:15 PM). If Dlivrd won't allow 45 min, use buffer time option: set to 40 minutes.
- **Order ID:** Use the Invoice ID from the Slack #orders channel.

*Dropoff section:*
- **Contact number:** Customer's phone number — no parentheses or dashes (e.g., 1234567890 not (123) 456-7890).
- **Date & Time:** Match the time on the restaurant's dashboard.
- **Address:** Select from dropdown.
- **Recipient Name:** Customer name.
- **Value:** Order subtotal from Slack #orders.
- **Driver Tip:** Tip amount from Slack #orders.
- **Item Count:** Number of items ordered.
- **Dropoff Instructions:** Pretend to book a driver from the Sauce Dashboard to check for any apt, floor, gate, or notes. Add those here.

*Order Details section:*
- **Notes:** Same as Dropoff Instructions.
- **Value:** Order subtotal.
- **Driver Tip:** Tip amount.

Click **Create Order** then **Create**.

**After booking:**
- Ticket name: Keep as received (from spam).
- Add a screenshot of the booking confirmation to ticket notes.
- Category: CC Catering Order Delivery.
- Status: Closed.

**Exceptions:** Always inform the store before placing a test order. Never skip dropoff instructions check. Temporary: the Catering BaD caveat above applies until the dashboard bug is fixed.
**Approval Required:** No.
**Last Updated:** 2026-08-24 — added Catering BaD bug caveat and updated the login URL to brand.expedite.io (both sourced to Josh Boock, 2026-07-30; URL confirmed current by Josh 2026-08-24, old dlivrd URL still functional); 2026-02-25 — extracted from Playbook

---

## Entry OPS-13: Restaurant In-House Delivery Issues

**Title:** Delivery Issues on Restaurant-Handled Deliveries
**Issue Type:** Order Issues
**Situation:** A customer complains about a delivery issue (lateness, wrong address, etc.) on an order where the restaurant handled their own delivery (not Uber/DoorDash/Relay).
**Resolution:**
- For delivery-related complaints (lateness, wrong address, etc.): CS cannot help — direct the customer to contact the restaurant directly.
- For non-delivery issues (missing items, wrong order, etc.): handle as normal per the relevant KB entry.

**Template:** Use "Restaurant delivery issue: for resto" in HubSpot.

> Hi [First Name],
> This is [Your Name] from Sauce Support, I hope you're doing well! I'm reaching out regarding your order at [Resto Name] on [Order Date].
> We noticed that there might have been an issue with your recent delivery order, and we sincerely apologize for any inconvenience this may have caused. If you require further help for your order due to a delivery issue, kindly reach out directly to [Resto Name] as they handled the delivery.
> If you have any questions, please let us know.
> Have a nice day! Best, [Your Name]

**Exceptions:** Non-delivery order issues (missing/wrong items) are still handled by CS even on restaurant delivery orders.
**Approval Required:** No.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry OPS-14: Processing Upcharges

**Title:** How to Process an Upcharge
**Issue Type:** Policies & Rules
**Situation:** A customer needs to be charged an additional amount (e.g., delivery fee for pickup-to-delivery change, added item, new delivery fee).
**Resolution:**
1. **Always get the customer's approval** for the upcharge amount before requesting it.
2. Share the order details in Slack **#cc-epayments-connect**, specifying:
   - The amount to be upcharged
   - The reason for the upcharge
3. ePayments will process the charge.

**Important:** The "Adjust" button on the Sauce Dashboard is for ePayments team and restaurants only — CS agents must NOT use it directly. If a restaurant needs guidance on using it, CS can walk them through it.

**Exceptions:** Never upcharge a customer without explicit approval first.
**Approval Required:** Yes — customer must approve before upcharge is submitted.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry OPS-15: Unknown Charges — Customer Doesn't Recognize a Charge

**Title:** Unknown Charge — Customer Doesn't Recognize a Charge on Their Card
**Issue Type:** Order Issues
**Situation:** A customer contacts CS saying they don't recognize a charge on their card (may not remember the purchase, or suspects card fraud).
**Resolution:**
1. **Do NOT share any personal information** about the order with the customer — no name, email, phone, or address of the person who placed the order.
2. Ask the customer to provide the following details:
   - *Last 4 credit card digits (required)*
   - *Name (required)*
   - *Email (required)*
   - Phone
   - *Date of the charge (required)*
   - *Amount (required)*
   - Statement descriptor (format: "SAUCE*RESTONAME")
3. Share this information with ePayments via Slack **#cc-epayments-connect**.
4. If ePayments finds a charge that does not match the caller's information: redirect the customer to their bank.
5. No matter how much the customer insists — do not share personal information from the order.

**Exceptions:** None — the no-personal-information rule is absolute regardless of customer pressure.
**Approval Required:** No — ePayments investigates.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry OPS-16: Uncaptured Charges — Customer Was Charged but Order Didn't Go Through

**Title:** Uncaptured Charge — Customer Was Charged but No Order Was Received
**Issue Type:** Order Issues
**Situation:** A customer says they were charged but their order never went through, and you cannot find any record of their order in the system.
**Resolution:**
1. Ask the customer to provide:
   - *Last 4 credit card digits (required)*
   - Name
   - *Email (required)*
   - Phone
   - *Date of the charge (required)*
   - *Amount (required)*
   - *Statement descriptor — format: "SAUCE*RESTONAME" (required)*
2. Share this information with ePayments via Slack **#cc-epayments-connect**.
3. If ePayments confirms the charge is uncaptured, verify with the restaurant that they did NOT receive the order before ePayments cancels it:
   - **Tablet restaurants:** if the order doesn't appear on the tablet, they did not receive it.
   - **POS system restaurants:** explicitly confirm with the restaurant they did not receive it.
4. If ePayments cancels an uncaptured charge: **no refund ticket is needed** — the payment was never received on Sauce's end.

**Mandatory snippets (use in order):**
1. **#Uncaptured Payment – Asking for Info** — collect the customer details above (statement descriptor appears as "SAUCE*RESTAURANT").
2. **#Uncaptured Payment – Checking with ePayments** — after info is gathered; tells the customer the Payments Team is investigating and they'll receive an email update within 24 hours.
3. **#Uncaptured Payment – Canceled on Stripe** — once the Payments Team confirms the payment never completed; explains the transaction was denied and funds return automatically within a few days, depending on their bank.

**Follow-up after chat ends:** use the email template **"Uncaptured Payment – Canceled on Stripe (CONFIRMATION)"**.

**Critical:** Do not confirm any refund until it is confirmed by ePayments.

**Exceptions:** Always confirm with the restaurant before ePayments cancels an uncaptured charge.
**Approval Required:** No — ePayments handles the cancellation.
**Last Updated:** 2026-07-16 — added mandatory snippets, confirmation email template, and 24-hour update expectation

---

## Entry OPS-17: Connecteam — Clocking In and Out

**Title:** Clocking In and Out via Connecteam
**Issue Type:** Policies & Rules
**Situation:** Agent needs to clock in or out for their shift.
**Resolution:**
- Open Connecteam: https://app.connecteam.com/#/ui?t=bcb58170&l=en-US
- Use the **Time Clock** feature to clock IN or OUT.
- When clocking in, select the option that best matches your shift type.

**Note:** Detailed screenshots of the clock-in options are available in the Playbook. Consult your trainer or team lead for shift type guidance on first use.

**Exceptions:** None.
**Approval Required:** No.
**Last Updated:** 2026-02-25 — extracted from Playbook

---

## Entry OPS-18: Sauce Tablet Printer Settings

**Title:** Sauce Tablet Printer Settings — Receipt Format & Future Order Print Timing
**Issue Type:** Restaurant Relations
**Situation:** Use when a restaurant partner contacts CS asking how to change their receipt format (long vs. short) or reporting that future/scheduled orders are printing at the wrong time (immediately vs. at prep time).

**Resolution:**

1. Let the partner know both settings are self-serve and accessible directly from their Sauce Tablet.
2. Guide them to open the **tablet dashboard**.
3. Tap the **three horizontal lines (☰ hamburger menu)** in the top left corner.
4. Tap **Settings**, then navigate to **Printer Settings**.
5. From here, direct them to the relevant setting based on their issue:

   **A. Printed Receipt Structure** *(receipt format complaint)*
   - Toggle between **Long** or **Short**
   - **Long** — includes item categories and modifiers on the printed receipt
   - **Short** — condensed version; categories and modifiers are omitted

   **B. Future Orders** *(scheduled orders printing at wrong time)*
   - Toggle between **Immediately** or **At Start of Prep Time**
   - **Immediately** — receipt prints as soon as the scheduled order is placed/received
   - **At Start of Prep Time** — receipt prints when the prep window begins, closer to the actual delivery/pickup time

6. Confirm with the partner which option best fits their operational needs and advise them to select accordingly.
7. No CS-side action is required — both settings are fully self-serve.

**Reference:** [Sauce Tablet Printer Settings — Video Walkthrough](https://drive.google.com/file/d/1iVUNy3sACxipBWLtpnG0LqL4GEzrmrCR/view)

**Exceptions:** If the partner reports that the Printer Settings option is missing from their Settings menu, or that toggling the settings has no effect, escalate to the Tablet/Tech support team as this may indicate a tablet configuration or software issue.
**Approval Required:** No
**Last Updated:** 2026-04-09 — added via KB update workflow

---

## Entry OPS-19: Irate Customer Handling Policy

**Title:** Framework for Managing Escalating Customer Interactions
**Issue Type:** Agent Guidelines / Escalation
**Situation:** A customer interaction is escalating — the customer is using profanity, refusing resolution, or directing personal attacks at the agent.
**Resolution:**

**Core principle:** Confidence is your most important tool. Frustrated customers are looking for someone in control. Do not over-apologize, match their energy, or show hesitation — stay steady, warm, and in control. Customers are upset about a situation, not about you personally.

---

**LEVEL 1 — General Frustration or Cursing About the Situation**
**Trigger:** Customer uses profanity or strong frustration directed at the *situation*, not the agent.
**Script:** "I understand you are really frustrated with this situation. I am here to help you with the best resolution I can provide."
**Guidance:** Hold your ground. Acknowledge, redirect, and keep moving toward resolution.

---

**LEVEL 2 — Customer Refuses Resolution or Stops Communicating Constructively**
**Trigger:** Agent has offered the best available resolution and the customer continues without productive engagement — repeating the same demands, not responding to explanations, or refusing to leave the chat.
**Script:** "It seems like we are unable to communicate successfully on this matter. I will ask my supervisor to reach out as soon as possible to work toward a resolution."
**Guidance:** Once this script is sent, you are not required to continue engaging. Stop responding. When the customer closes the chat or goes inactive, close the ticket. Do not re-engage — the matter is now escalated.

---

**LEVEL 3 — Personal Attack**
**Trigger:** Customer directs a targeted personal insult or wishes harm on the agent.
**Script:** "It seems like we are no longer able to work together toward a resolution. I will have my supervisor reach out as soon as possible to help with this matter."
**Guidance:** Firm, non-negotiable exit. You do not owe further engagement. Send the message, stop responding, and close when the customer goes inactive. Log the interaction and flag for supervisor review.

---

**Documentation requirement (Level 2 and Level 3):**
Note in the ticket: which script was used and when, a brief summary of what triggered the escalation, and whether the customer closed the chat or went inactive.

**Edge cases:**
- *Customer attacked you but immediately apologized:* Use judgment — attempt to re-engage once. If behavior repeats, go straight to Level 3 with no second reset. Document both incidents.
- *Restaurant owner or operator is abusive:* Same scripts apply. Partner status does not change the threshold. Do not close unilaterally — flag for supervisor before closing. Note: "Restaurant partner — escalated per irate customer policy."
- *Customer appears in genuine distress or mentions self-harm:* Do NOT use escalation scripts. Respond with care: "I hear that you're going through something really difficult right now. If you're in crisis, please reach out to the 988 Suicide and Crisis Lifeline by calling or texting 988." Flag for supervisor immediately.
- *Customer abusive in another language:* Behavior is the trigger, not the words. Invoke the appropriate script in the customer's language if possible, or in English.
- *Customer sent escalation script but keeps messaging:* You are not required to respond. Close when inactive. If they open a new ticket, note the prior escalation for context.

**Exceptions:** Supervisor escalations for restaurant partners are prioritized. End-customer escalations are reviewed based on available capacity. Agents are not responsible for the supervisor response timeline.
**Approval Required:** No.
**Last Updated:** 2026-04-30 — added from Confluence: Irate Customer Handling Policy (Josh Boock, April 2026)

---

## Entry OPS-20: Ticket Status Guide — Aircall, Next Action, Training Tickets

**Title:** Ticket Status Usage — Aircall, Next Action, Conversation Closed, Closed Conversation, Training Tickets
**Issue Type:** Policies & Rules
**Situation:** Agent needs to know which status a Support pipeline ticket belongs in and how long it may stay there.
**Resolution:**

- **Aircall** (formerly "Aircall/Need to Organize") — used ONLY for Aircall tickets.
- **Next Action** — all open tickets that still need to be worked on. Standard flows: New → Next Action → Closed/Pending/Escalated, or New → Closed/Pending/Escalated. **Tickets returned from other teams that land in Next Action must be followed up within 24 hours** — escalate to the proper column/team to keep the pipeline clean.
- **Conversation Closed** — temporary holding status for tickets not processed immediately; clean it up every shift. Best habit: move tickets to the correct next status straight from New.
- **Closed Conversation** (rolled out 2026-07-27 — *a different status from "Conversation Closed" above; read carefully*): the status that ends a chat and sends the Chat CSAT survey. Setting it sends the survey, closes the conversation, and routes the ticket back to **New** so any remaining work can continue — it does not fully close the ticket. Confirm it worked by checking the ticket's left panel for **"Feedback survey sent."**
- **Training Tickets** — all SPAM, auto-reply, or irrelevant tickets go here so they can be excluded from reporting.
- **Refund Request / Refund Follow Up Needed** — see kb-refunds Entry 1 for definitions.
- **CSAT timing** (added 2026-07-27): since the move to Helpdesk, the CSAT survey request is NOT sent to the customer until the ticket itself is closed (not just the conversation/chat). Close resolved tickets promptly from the Helpdesk view to capture CSAT responses on quick, positive interactions.

**How to close a chat (current process as of 2026-08-15):**
Do **NOT** close chats manually by sending a snippet, and do not use the old **"End Chat" button** — both are retired. Use the **"End Chat" Macro** instead. One action (**Send and Apply → Closed Conversation → New**) sends the closing snippet, sets the ticket to Closed Conversation, and routes it to New — which is what triggers the CSAT survey send.

Macro variants available: **Inactive**, **Spanish**, and **Close Ticket**.

> ⚠️ The retired **"End Chat" button** and the current **"End Chat" Macro** share a name but are not the same thing. The macro is the supported path.

Don't skip sending the survey out of concern that a rough interaction will reflect badly — roughly 80% of negative CSATs that were reviewed turned out to be unrelated to agent performance.

**Exceptions:** None.
**Approval Required:** No.
**Last Updated:** 2026-08-24 — consolidated the chat-closing changes from the 2026-08-03, 2026-08-10 and 2026-08-17 scans into one current-state description: added the Closed Conversation status and the End Chat Macro requirement replacing manual snippet closing and the old End Chat button (sources: Josh Boock 2026-07-27 and 2026-08-13 w/ thread through 2026-08-15; Sofia Perez 2026-08-04). 2026-07-27 — added CSAT-timing detail (source: Sofia Perez, 2026-07-21)

---

## Entry OPS-21: Grubhub Connect Partner Support Guide

**Title:** Grubhub Connect — Delivery Service Partner Support Line
**Issue Type:** Dispatch / Third-Party Delivery
**Situation:** A support request involves an in-flight Grubhub Connect delivery and you need to contact Grubhub about it.
**Resolution:**
1. Call the **GH Connect live support line for Delivery Service Partners: 312-601-2093**.
2. **Always identify yourself as a Delivery Service Partner** when calling.
3. You must provide the **customer's phone number** — GH uses it to look up the delivery.

**What GH Connect support CAN do:**
- Confirm courier location/status
- Relay information to couriers
- Cancel the delivery if fulfillment isn't possible

**What GH Connect support CANNOT do:**
- Unassign couriers
- Dispatch replacement couriers
- Investigate completed deliveries

**Completed deliveries:** GH Connect support is a dead end for anything about a completed delivery — escalate internally instead.

**Exceptions:** If GH Connect support can't be reached during a critical in-flight situation, escalate to your Sauce team lead. Do not attempt to contact GH couriers directly.
**Approval Required:** No.
**Last Updated:** 2026-07-16 — consolidated from the 2026-07-06 announcement and the deployed KB entry

---

## Entry OPS-22: Escalation Channels — #ops-escalations vs Back Office

**Title:** Where to Escalate Urgent Operational Issues in Slack
**Issue Type:** Escalation Paths
**Situation:** An urgent operational issue needs another team's help, or you need a status update on a cross-team issue.
**Resolution:**
- **#ops-escalations** — for urgent cross-team operational issues (especially delivery/dispatch problems). Use it instead of Tier 2 for delivery ops issues — it gives better visibility and coordination. Also use it to find the owner/process for a ticket with no clear owner.
- **#backoffice-support-coordination** — still used for BO/Support-specific matters.
- Escalations should always go to the corresponding pipelines; these channels are for urgent resolution or status updates, not a replacement for proper ticket routing.

**Exceptions:** Tickets with a clear process and owner should be handled through their normal pipeline.
**Approval Required:** No.
**Last Updated:** 2026-07-16 — added from #support-policy-process (Josh/Danny, June 2026)

---

## Entry OPS-23: Screenshot and Data Sharing Policy

**Title:** What Information May Be Shared with Restaurants and Customers
**Issue Type:** Policies & Rules
**Situation:** Agent is about to share a screenshot or internal information with a restaurant or end customer.
**Resolution:**
- Do **NOT** share images or screenshots from **Stripe, Stream, Slack, or OpsCopilot** with end customers or restaurants.
- **Restaurants** should only receive information from the **Dashboard**.
- **End customers** should only receive the **Receipt**.
- Always use the approved sources to protect internal information and maintain data security.

**Exceptions:** None.
**Approval Required:** No.
**Last Updated:** 2026-07-16 — added from #support-policy-process (Sofia, 2026-06-09)

---

## Entry OPS-24: Email Handling Standards

**Title:** Email Handling — Reply All, New Tickets for External Emails, Accounting Contacts
**Issue Type:** Policies & Rules
**Situation:** Agent is responding to or sending emails from HubSpot.
**Resolution:**
- **Always Reply All** to an email.
- **Always reply to emails** — first-response snippets exist for every scenario: **#CC - Email Internal Response** (emails from CS/Onboarding/Sales — Sauce accounts only), **#B2C - Email First Response** (end customers), **#B2B - Email First Response** (restaurants — we should always reply to restaurant emails).
- If you're sending an **external email after an internal conversation**, create a **new ticket** to send the external email from.
- **Think twice before emailing accounting contacts.** If unsure who to email, look up the email on the order notifications; if still unsure, ask Josh. Getting the right contact speeds up approvals on large accounts.
- **AI email handoffs:** responses signed with Josh's name on tickets may be AI email handoffs — this is expected.
- Review **Escalated Emails Need Response** daily (use Table View) — these are emails across pipelines where an end customer or restaurant replied to an existing ticket.

**Exceptions:** Internal CS→B2B responses that need no reply can sit until sent back or closed — respond only if it makes sense.
**Approval Required:** No.
**Last Updated:** 2026-07-16 — consolidated from #support-policy-process (June–July 2026)

---

## Entry OPS-25: Breaks and End-of-Shift Approval

**Title:** Break and EOS Requests Require Lead Approval
**Issue Type:** Policies & Rules
**Situation:** Agent wants to take a break or end their shift.
**Resolution:**
- All **Break + EOS requests must be approved** by Josh, Danny (especially on Saturdays), or Sofia. This ensures a partner is available during challenging situations and coverage is maintained.
- You may go **unavailable 10 minutes before a break** so you can leave on time — coordinate with each other when only 2 agents are on.

**Exceptions:** None.
**Approval Required:** Yes — Josh, Danny, or Sofia.
**Last Updated:** 2026-07-16 — added from #support-policy-process (May–June 2026)

---

## Entry OPS-26: Phone/Email Role — Priority Order

**Title:** Priorities for Agents on the Phone/Email Role
**Issue Type:** Agent Guidelines
**Situation:** Agent is scheduled on the Phone/Email role type; or any agent is deciding whether to pick up a request in `#support-new` or `#support-team-help`.
**Resolution:**
Work in this priority order — you should always be on a call, answering Slack, or working a ticket:
1. Answer phones when they ring for you
2. Answer @ support requests in Slack
3. Clean up **Next Action** and **Refund Follow Up** (oldest to newest) that came back from other teams
4. Grab any unassigned tickets
5. Review **Tickets Requiring a Response**
6. Review **Pending B2B** for tickets over 72 hours old

**Agents still on mixed roles:** work as normal — stay on phones and answer as usual. You remain accountable for tickets assigned to you, especially initial processing and escalation or closure.

**Responding to waiting customers is a team effort (added 2026-07-31):** Responding to any customer who needs a response applies to **all** agents, regardless of ticket ownership or role — not just agents scheduled on the Phone/Email role. Check the views for tickets requiring a response whether or not they sit in your own pipeline, so customers are acknowledged and get whatever update is available.

**Shared responsibility for Slack support channels (added 2026-08-19):** Answering requests in `#support-new` and `#support-team-help` is everyone's responsibility — not just the more experienced or longer-tenured agents. When only a few people consistently pick these up, it overloads them and makes the team look less responsive. Every agent should keep an eye on both channels regardless of role or ticket ownership.

**Exceptions:** None.
**Approval Required:** No.
**Last Updated:** 2026-08-24 — added the team-effort framing for waiting customers (source: Josh Boock, 2026-07-31) and the shared-responsibility note for #support-new / #support-team-help (source: Sofia Perez, 2026-08-19), both via KB Policy Scan; originally added 2026-07-16 from #support-policy-process (Josh, 2026-07-15)

---

## Entry OPS-27: Closing a Restaurant Until Further Notice

**Title:** How to Close a Restaurant Until Further Notice (Indefinite Closure)
**Issue Type:** Restaurant Relations
**Situation:** A restaurant needs to be closed indefinitely (until further notice) due to operational issues, restaurant request, or other circumstances requiring an open-ended suspension of service.
**Resolution:**
1. Indefinite restaurant closures are **not performed by standard CS agents** — this action requires elevated access.
2. The closure is executed directly in **Admin** by authorized personnel only: **Director, Senior agents, or the Backoffice team**.
3. If you are not one of the above, do not attempt to process this yourself.
4. Submit a request in the **#backoffice-support-coordination** Slack channel, including:
   - Restaurant name and ID
   - Reason for closure
   - Any relevant context or urgency
5. An authorized team member will action the closure from Admin.

**Exceptions:** If the request is urgent (e.g., food safety concern, legal issue), flag it explicitly in #backoffice-support-coordination to ensure prompt handling.
**Approval Required:** Yes — must be carried out by Director, Senior, or Backoffice team member.
**Last Updated:** 2026-07-16 — recovered from deployed KB (originally added 2026-07-02 via KB update workflow)

---

## Entry OPS-28: PauseBot Alerts — Support Team Guide

**Title:** PauseBot Alerts — Support Team Guide
**Issue Type:** Dispatch / Third-Party Delivery
**Situation:** The pause/unpause bot posts an alert in **#backoffice-support-coordination** indicating a restaurant is NOT in the state it should be on a third-party platform (Uber Eats, DoorDash, Grubhub, Slice, Sauce channels).
**Resolution:**
Every alert requires immediate manual action in **Stream** (sauce.streamorders.com — credentials in REF-5).

**Case 1 — the bot gives the location:**
1. Log into the correct Stream org and open the Pause Menu for that location.
2. Perform the exact action (pause/unpause all delivery apps) for the listed duration (shown in US Eastern).
3. React ✅ on the alert once done.

**Case 2 — "location could not be found on Stream":**
1. Search Stream by address (try both abbreviated and full street forms).
2. If found: perform the action and tell Gal the address so the bot can be corrected.
3. If not found: escalate to Gal.

**Rules of thumb:** every alert is urgent — no exceptions; times are always US Eastern; never ignore an alert; anything unclear → ask Gal.

**Exceptions:** None.
**Approval Required:** No — but escalate to Gal when a location can't be found on Stream.
**Last Updated:** 2026-07-17 — applied from KB Policy Scan (source: Josh Boock guide in #backoffice-support-coordination, 2026-07-16)

---

## Entry OPS-29: Identifying a "Book-a-Driver, No Order Associated" Situation

**Title:** Identifying a "Book-a-Driver, No Order Associated" Situation
**Issue Type:** Dispatch / Third-Party Delivery
**Situation:** A restaurant partner (especially pizza places) says they are waiting for a driver or need a driver, but no matching order/driver is visible to CS at first glance.
**Resolution:** Before telling the restaurant we don't see anything, check ops-copilot or the restaurant dashboard — the driver may be booked via a "Book a Driver" with no order associated (i.e., not tied to a normal order record). Be thorough before concluding nothing is found.
**Exceptions:** None specified in source.
**Approval Required:** No.
**Last Updated:** 2026-07-27 — applied from KB Policy Scan (source: Josh Boock, 2026-07-26)

---

## Entry OPS-30: Sharing Context When Asking Josh Questions After Hours

**Title:** Sharing Context When Asking Questions After Hours
**Issue Type:** Policies & Rules
**Situation:** An agent needs to ask Josh a question after hours.
**Resolution:** Share the situation along with the ticket link — it can be difficult to review full conversations from a phone. Including the ticket link helps even when a full read of the conversation isn't needed.
**Exceptions:** None specified in source.
**Approval Required:** No.
**Last Updated:** 2026-07-27 — applied from KB Policy Scan (source: Josh Boock, 2026-07-20)

---

## Entry OPS-31: Add Invoice ID When Helping With an Order via Chat

**Title:** Add Invoice ID When Helping With an Order via Chat
**Issue Type:** Policies & Rules
**Situation:** An agent helps with any order-related issue over chat.
**Resolution:** Add the Invoice ID to the ticket so the subject line updates automatically — this makes it easier to review the ticket later.
**Exceptions:** None specified in source.
**Approval Required:** No.
**Last Updated:** 2026-07-27 — applied from KB Policy Scan (source: Josh Boock, 2026-07-22)

---

## Entry OPS-32: BYOC Miami — Reaching the Customer via Uber

**Title:** BYOC Miami — Reaching the Customer and Locating a Delivery ID via Uber
**Issue Type:** Restaurant Relations / Dispatch
**Situation:** A BYOC order in Miami needs customer contact but only an Uber masked phone number is available; or Uber support cannot find a Book-a-Driver (BaD) delivery using the standard 5-character delivery ID.
**Resolution:**
1. **Masked number:** Check the order in the Sauce dashboard — it shows the customer's real phone number and the PIN code needed to reach them directly. Use that instead of the Uber masked number.
2. **Uber can't find the delivery ID:** Open the Uber tracking link and locate the long, case-sensitive tracking number (the one with dashes) rather than the short 5-character code. Give Uber support the long tracking number — it matches more uniquely and usually resolves the lookup.
**Exceptions:** None documented.
**Approval Required:** No.
**Last Updated:** 2026-08-24 — applied from KB Policy Scan (source: Josh Boock, 2026-08-17, #support-policy-process; tracking-ID workaround from the same thread)

---

## Entry OPS-33: Do Not Merge a Call Ticket Into an Active Chat

**Title:** Do Not Merge a Call Ticket Into an Active Chat
**Issue Type:** Policies & Rules
**Situation:** An agent is handling a live chat and also has a related call ticket for the same customer interaction.
**Resolution:**
- Do **NOT** merge the call ticket into the chat ticket while the chat is still active. A current bug can make the chat disappear, which blocks reaching the customer through that channel and blocks the CSAT survey.
- Wait until the chat has ended, then merge the call ticket into it.
- If the chat has already disappeared, reach the customer by phone and relay the outcome of the case that way.
**Exceptions:** None.
**Approval Required:** No.
**Last Updated:** 2026-08-24 — applied from KB Policy Scan, week of 2026-08-10 (source: Natalia Heredia, 2026-08-05)

---

## Entry OPS-34: Pending B2B vs. Pending B2C vs. Schedule Future Action

**Title:** Choosing a Follow-Up Status — Pending B2B, Pending B2C, and Schedule Future Action
**Issue Type:** Policies & Rules
**Situation:** An agent needs to park a ticket for follow-up later and must choose the correct status.
**Resolution:**
- **Need to reach a restaurant later → Pending B2B.** Tickets here move automatically to Next Actions after 24 hours, so the automation resurfaces them for follow-up.
- **Need to reach a customer later → Pending B2C.**
- **Schedule Future Action** is ONLY for cases a specific protocol requires it — e.g. Cancel Future Order, Reschedule Future Order. In those cases also set a Slack reminder for the day of the order.
- Do **not** park regular follow-ups in Schedule Future Action. There is no automation to bring them back to the queue, so they go silent until someone stumbles on them.
**Exceptions:** None stated.
**Approval Required:** No.
**Last Updated:** 2026-08-24 — applied from KB Policy Scan, week of 2026-08-17 (source: Sofia Perez, 2026-08-12)

---

## Entry OPS-35: PTO Requests — Multi-Date Selection and Deel Coverage Note

**Title:** PTO Requests — Consecutive-Date Selection and the Deel Coverage Plan Note
**Issue Type:** Team Process
**Situation:** An agent is submitting a PTO request.
**Resolution:**
1. The PTO request form in **#cc-team-attendance** now allows selecting multiple dates when they are consecutive. Use the **start date** as the first day off and the **end date** as the last day off. Days off in the middle of that range are fine.
2. When entering the same PTO in **Deel**, add a coverage plan in the notes or HR will not approve it. For Support PTO, use: **"Coverage approved by Support Leadership."**
**Exceptions:** Non-consecutive days off still need separate requests.
**Approval Required:** Yes — PTO is approved by Support Leadership and HR (via Deel).
**Last Updated:** 2026-09-07 — applied from KB Policy Scan, week of 2026-08-31 (source: Josh Boock, 2026-08-30)

---

## Entry OPS-36: Lovable — Delivery Investigation Tool

**Title:** Lovable (sauce-delivery-hub.lovable.app) — Delivery Investigation Tool
**Issue Type:** Tools & Systems
**Situation:** An agent needs extra visibility into what happened on a delivery — where the driver actually went, or why a delivery took longer than expected.
**Resolution:**
1. Open **Lovable** at https://sauce-delivery-hub.lovable.app.
2. **Map** — shows where the driver ended up, so you can check whether they actually reached the delivery location.
3. **Delivery timestamps** — individual timestamps across the delivery process, useful for explaining why a delivery ran long.
4. **Diagnose button** — summarizes delivery performance and gives a quick overview of what happened.
5. Use it as a supporting investigation tool alongside the existing delivery-issue procedures; it does not replace any escalation path.
**Exceptions:** Credentials are shared privately by Support Leadership, not posted in channel. Full usage guidance is still pending a Tuesday/Thursday huddle walkthrough — this entry should be updated once that happens.
**Approval Required:** No.
**Last Updated:** 2026-09-07 — applied from KB Policy Scan, week of 2026-08-31 (source: Sofia Perez, 2026-08-30)

---

## Entry OPS-37: "Multiple Courier Issue" Ticket Property

**Title:** Multiple Courier Issue — Ticket Property (Yes / No / Blank)
**Issue Type:** Tools & Systems
**Situation:** A restaurant reports that multiple couriers arrived unexpectedly for the same order.
**Resolution:**
1. Set the **Multiple Courier Issue** ticket property to **Yes** on any ticket where a restaurant reports multiple couriers arriving unexpectedly for one order.
2. Leave it **No** or **Blank** otherwise — the property exists so these cases can be tracked and investigated, so accuracy matters more than volume.
3. Continue handling the underlying delivery issue through the normal process; this property is for tracking, not routing.
**Exceptions:** None.
**Approval Required:** No.
**Last Updated:** 2026-09-07 — applied from KB Policy Scan, week of 2026-09-07 (source: Josh Boock, 2026-09-03)

---

## Entry OPS-38: Aging B2B / B2C Tickets — Pipeline Hygiene and Scorecard Impact

**Title:** Aging B2B / B2C Tickets — Review Expectations and Scorecard Impact
**Issue Type:** Policies & Rules
**Situation:** An agent has B2B or B2C tickets sitting in their pipeline without recent action.
**Resolution:**
1. Review your **B2B and B2C tickets regularly**, especially while on shift. Tickets over a month old are not acceptable.
2. Be proactive about closing out or advancing aged tickets rather than waiting for them to resurface.
3. **Ticket age is part of the team scorecard** and could affect bonuses in the near future.
4. See **OPS-34** for choosing the right follow-up status so tickets resurface on their own instead of going silent.
**Exceptions:** None stated.
**Approval Required:** No.
**Last Updated:** 2026-09-07 — applied from KB Policy Scan, week of 2026-09-07 (source: Danny Canabe, 2026-09-03; Josh Boock reply in thread)

---

## Entry OPS-39: Scorecard Metric — Service Level Replaces Response Time

**Title:** Team Scorecard — "Service Level" Replaces "Response Time"
**Issue Type:** Policies & Rules
**Situation:** An agent asks how chat responsiveness is measured on the team scorecard.
**Resolution:**
1. The **response time** metric on the scorecard has been replaced with **service level**: the percentage of chats answered in under **60 seconds**.
2. The change is meant to keep a small number of outlier tickets from having an outsized impact on the metric — but consistency across all chats is now what drives the number.
**Exceptions:** None.
**Approval Required:** No.
**Last Updated:** 2026-09-07 — applied from KB Policy Scan, week of 2026-09-07 (source: Josh Boock, 2026-09-05)

---

## Entry OPS-40: "Credits Campaign" Line on a Receipt = Loyalty & Cashback Redemption

**Title:** Identifying a "Credits Campaign" Discount Line on a Receipt
**Issue Type:** Order Issues
**Situation:** A receipt or order detail shows a discount line labeled **Credits Campaign** and the agent (or restaurant) needs to know where the discount came from.
**Resolution:**
1. A **Credits Campaign** discount line means the customer redeemed **Loyalty & Cashback** credit on that order — it is not a promo code or a manually applied discount.
2. Verify it in the restaurant dashboard: **Growth → Loyalty & Cashback → Recent Cashback Orders**, and match the order.
3. Explain to the restaurant that the amount is a cashback redemption from their own Loyalty & Cashback program, not an unexpected Sauce discount.
4. Note the naming difference across surfaces: the customer-facing Storefront checkout shows this as a **Cashback Redeemed** row (see **B2C-13**), while the restaurant-side receipt / order detail labels it **Credits Campaign**. Same money, different label — not a discrepancy to escalate.
**Exceptions:** None.
**Approval Required:** No.
**Last Updated:** 2026-09-07 — applied from KB Policy Scan, week of 2026-09-07 (source: #support-team-help thread re: order BPXAA1FQ)
