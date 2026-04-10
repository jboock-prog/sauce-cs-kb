# KB Entries: Support Operations — Guidelines, Dispatch, ePayments

Extracted from: Sauce CC Team Playbook
Source date: Playbook content as of 2025
Last extracted: 2026-02-25
Entry count: 18

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

## Entry OPS-3: WhatsApp Message Handling

**Title:** How to Handle WhatsApp Messages
**Issue Type:** Policies & Rules
**Situation:** A customer or restaurant contacts CS via WhatsApp. WhatsApp messages do not auto-create HubSpot tickets.
**Resolution:**
1. Assign yourself to the WhatsApp conversation (not auto-assigned).
2. Acknowledge you're working on it and provide updates as needed.
3. Create a ticket from scratch manually in HubSpot for the request.
4. Add a comment on the inbox linking to the ticket so the connection is visible.
5. Unassign yourself from the WhatsApp chat and close the conversation.
6. Make sure the ticket includes a link to the WhatsApp conversation as the source.

**Exceptions:** None — a manual ticket must always be created; WhatsApp will not auto-generate one.
**Approval Required:** No.
**Last Updated:** 2026-02-25 — extracted from Playbook

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

**Exceptions:** None.
**Approval Required:** No.
**Last Updated:** 2026-02-25 — extracted from Playbook

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

**Login:** https://expedite.dlivrd.io/dashboard — see REF-6 for credentials.

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

**Exceptions:** Always inform the store before placing a test order. Never skip dropoff instructions check.
**Approval Required:** No.
**Last Updated:** 2026-02-25 — extracted from Playbook

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

**Exceptions:** Always confirm with the restaurant before ePayments cancels an uncaptured charge.
**Approval Required:** No — ePayments handles the cancellation.
**Last Updated:** 2026-02-25 — extracted from Playbook

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
