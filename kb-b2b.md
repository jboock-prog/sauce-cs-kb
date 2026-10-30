# KB Entries: B2B Restaurant Requests

Extracted from: Sauce CC Team Playbook
Source date: Playbook content as of 2025
Last extracted: 2026-02-25
Entry count: 55

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

**Holiday Hours feature (updated behavior, 2026-05-24):**
- Select only the **days impacted** — do not enter the day before or the day after, and multiple days now mean the days impacted (no longer "last day closed + first day open" like before).
- For each impacted day choose **closed** or **custom hours**.
- Example: restaurant closed from the 21st to the 23rd → select the 21st through the 23rd. Closed just for Memorial Day → select only the 25th.

**Exceptions:** None — at least one reminder mechanism is required to ensure the revert doesn't get missed.
**Approval Required:** No — restaurant or account manager request is sufficient.
**Last Updated:** 2026-07-16 — added new Holiday Hours day-selection behavior

---

## Entry B2B-4: Update a Restaurant's Bank / Banking Details

**Title:** Restaurant Requests a Change to Their Banking Details
**Issue Type:** Restaurant Relations
**Situation:** A restaurant needs to update the bank account where they receive their payouts.
**Resolution:**
- Bank account updates are done by the restaurant directly through their **Stripe Connect** account — the same login they use to access their 1099-K.
- **CS cannot update bank details on a restaurant's behalf.**
- CS can only help the restaurant identify the correct Stripe Connect login email (see process below).

**If the restaurant can't log in to Stripe Connect:**
1. Send the Stripe access troubleshooting template:

> Sorry to hear you're having trouble accessing your Stripe account — we're happy to help get this sorted.
> To move forward, can you please confirm the following:
> - Do you know the email address associated with your Stripe account, and do you currently have access to that inbox?
> - Do you know the phone number linked to the account, and do you have access to that phone?
> - Are you seeing any specific error message when trying to log in?
> Once we have this information, we can assist you with next steps.
> Thank you,

2. Once you have their email: verify the correct Stripe Connect email via ePayments (Stripe Connect email check).
3. Share the verified email so they can request a login code and access their account.
4. If they still cannot access their email or phone, send the Stripe account recovery template:

> Please head to Stripe's account recovery page using the link below (we recommend opening this in a new incognito/private browser window):
> https://support.stripe.com/contact/login
> Once there, click "I can't sign in" and answer as many of the prompted questions as apply to your situation. Stripe's support team will then review your request and assist you directly with regaining access to your account.

5. If still stuck after all steps → escalate to the Supervisor column.

**Do NOT escalate to CS by default for Stripe login/access issues** — most are resolved once the restaurant has the correct email.

**Stripe scope for Support (policy 2026-05-24):** Stripe-related issues should NOT be escalated to CS by default. Support handles:
- **Missing last payment reports**
- **Bank account update requests** (guide the restaurant per this entry — email template: "How to Update Your Bank Account on Stripe: Step-by-Step Instructions"; snippet: `#B2B - Stripe Issues/Change Bank Account`)

Anything related to **taxes, payout setup, payment configuration, or subscriptions** must still go to CS — subscription models vary by location and tax preference, and Support has no visibility into that. Note: Support has no direct Stripe account access — only ePayments information. Full guide: Confluence "Stripe Login and Troubleshooting" (https://say2eat.atlassian.net/wiki/spaces/SD/pages/2064547848).

**How to find the CS manager (if escalation is truly needed):**
HubSpot → Companies → Customer Care View → search for the specific restaurant.

**Exceptions:** CS cannot make banking changes directly. Only the restaurant can update their own Stripe Connect account.
**Approval Required:** N/A — restaurant self-serves through Stripe Connect.
**Last Updated:** 2026-07-16 — added Support vs CS Stripe scope policy and Confluence reference

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
**Situation:** A restaurant reaches out confused about why a specific dollar amount was deducted from their payout (e.g., "Why was $8.37 taken from my payout on July 23rd?").
**Resolution:**
1. Open the Sauce Dashboard → navigate to the restaurant's account.
2. Go to **Store Settings → Reports** and download the Sales Report for the date in question.
3. In the spreadsheet, search or sort for a **negative value** matching the deduction amount. Confirm the Invoice ID, Customer Name, and Refund Amount.
4. Go to HubSpot → **ePayments pipeline**. Search using the Invoice ID, customer name, or order date to find the related ticket.
5. Open the ticket and read the request — confirm what was refunded and why (e.g., missing item, cancellation, delivery issue).
6. Respond to the restaurant with: the customer name, order date and Invoice ID, and a clear reason the refund was issued.

**Sample response:**
> "Hi [Restaurant Name], I looked into the $[amount] deduction from your [date] payout. It was related to a refund for an order placed by [Customer Name] on [date] (Invoice ID #[ID]). The refund was issued due to [reason]. Please let me know if you have any other questions."

**Exceptions:** None.
**Approval Required:** No.
**Last Updated:** 2026-04-30 — expanded with Dashboard navigation steps and sample response (from Confluence: Refunds & Sales Report Matching)

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
Move it to the column **"BO, CS, or Menu (Check Category)."** This automatically routes it to the correct team pipeline.

**DO NOT** manually change the pipeline and status to move it to the other team.

**Ticket naming format:** `Restaurant Name | Task` (e.g., "Shelsky's Of Brooklyn | Flyer" or "Smash House Miami | Change of plan")
**Request type:** "Internal" if an internal agent requested it; "B2B" if the store reached out.

**Slack tagging rule:** Do NOT tag all of CS when a restaurant has a CS Owner — tag the restaurant's **CS Owner** directly. If the restaurant has no owner, tag **Mariana**.

**Exceptions:** None — always use the automation column, never manual pipeline changes.
**Approval Required:** No.
**Last Updated:** 2026-07-16 — added CS Owner tagging rule (Josh, 2026-07-07)

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

**Important — remind the restaurant they have other ways to receive orders while the issue is being resolved:**
- **Email:** Usually already set up — orders are sent automatically.
- **Dashboard:** They can always view and manage orders at dashboard.getsauce.com.
- **Fax:** Can be set up directly in the Sauce Dashboard.
- **SMS:** Can be set up via BO (send a BO Config Changes ticket — see B2B-15).

**Exceptions:** If app is running but orders are still missing, do not continue troubleshooting hardware — escalate.
**Approval Required:** No for basic troubleshooting. Escalation required if hardware steps don't resolve.
**Last Updated:** 2026-02-26 — added reminder to inform restaurant of alternative order-receiving methods

---

## Entry B2B-12: Tablet Replacement

**Title:** Tablet Replacement Request
**Issue Type:** Restaurant Relations
**Situation:** Restaurant has exhausted all tablet troubleshooting steps and still has issues.
**Resolution:**
1. Send the **#new_tablet** snippet (see below) to acknowledge the request and set expectations.
2. Collect a contact phone number or email for the restaurant if you don't already have one.
3. Create a ticket with the category **"CS Tablet Requested."**
4. Assign the CS agent as the ticket owner.
5. Move the ticket to the "BO, CS, or Menu (Check Category)" column.

**Remind the restaurant they have other ways to receive orders while waiting for the replacement:**
- **Email:** Usually already set up — orders are sent automatically.
- **Dashboard:** They can always view and manage orders at dashboard.getsauce.com.
- **Fax:** Can be set up directly in the Sauce Dashboard.
- **SMS:** Can be set up via BO — offer to set it up if they'd like (the #new_tablet snippet already prompts this).

**#new_tablet snippet:**
> Hi {name},
> We will have your account manager work on your request. For now, your orders are being sent to {email} and can be viewed at dashboard.getsauce.com. We can also set up SMS to a phone number of your choosing so that no orders are lost.
> Please let us know if you would like to setup SMS.
> Best Regards,
> Sauce Support

**Exceptions:** Only initiate replacement after completing all troubleshooting steps (Entries B2B-9 through B2B-11).
**Approval Required:** Yes — handled by CS and account manager.
**Last Updated:** 2026-02-26 — added #new_tablet snippet; added reminder to inform restaurant of alternative order-receiving methods (email, dashboard, fax, SMS)

---

## Entry B2B-13: Manually Reset Restaurant Dashboard Login

**Title:** Manually Reset a Restaurant's Dashboard Password
**Issue Type:** Restaurant Relations
**Situation:** A restaurant owner or staff is locked out of their dashboard and cannot reset the password themselves.
**Resolution:**
**Before resetting, verify identity:**
- Check if the caller's number is recognized in Aircall.
- If not recognized: ask for identification OR confirm with the restaurant's CS account manager that it's okay to change the login.

**Method 1 — Reset from Team Tab (use when you don't have their email):**
1. Log into the restaurant's Dashboard.
2. Click **Team** in the left navigation.
3. Click the three dots (⋮) next to the user.
4. Click **Reset Password**.
5. Set the new password to: **123456**
6. Click **Change Password**.
7. Give the restaurant:
   - The new password: **123456**
   - Confirm the email address they are using to log in.

**Method 2 — Reset from Users Tab (use when you have their email):**
1. Go to **Users**.
2. Search by the user's email address.
3. Click **Reset Password**.
4. Set the new password to: **123456**
5. Confirm the change.

**Note:** You cannot see the previous password — you can only overwrite it.

**Exceptions:** Identity verification is mandatory before any password reset for unrecognized callers.
**Approval Required:** Yes — identity check or CS account manager confirmation required for unrecognized callers.
**Last Updated:** 2026-02-26 — expanded with step-by-step for both Team Tab and Users Tab reset methods

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
4. Move ticket to the "BO, CS, or Menu (Check Category)" column.

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

**Critical rule: CS cannot retrieve or send the 1099-K directly.** Restaurants must access it themselves through their Stripe Connect account — the same login used for bank account updates.

**Resolution:**

**Step 1 — Send the self-service template first:**
- Send the **"1099-K Form"** HubSpot template directing them to their Stripe Connect account.
- Reference guide: https://support.getsauce.com/sauce-guide-for-taxes
- Confirm the restaurant is logging into **Stripe Connect** (not a different Stripe login).

**Step 2 — If they can't log in (biggest blocker):**
1. Send the Stripe access troubleshooting template:

> Sorry to hear you're having trouble accessing your Stripe account — we're happy to help get this sorted.
> To move forward, can you please confirm the following:
> - Do you know the email address associated with your Stripe account, and do you currently have access to that inbox?
> - Do you know the phone number linked to the account, and do you have access to that phone?
> - Are you seeing any specific error message when trying to log in?
> Once we have this information, we can assist you with next steps.
> Thank you,

2. Once you have their email: verify the correct Stripe Connect email via ePayments (Stripe Connect email check).
3. Share the verified email so they can request a login code and access the account themselves.
4. If they still cannot access their email or phone, send the Stripe account recovery template:

> Please head to Stripe's account recovery page using the link below (we recommend opening this in a new incognito/private browser window):
> https://support.stripe.com/contact/login
> Once there, click "I can't sign in" and answer as many of the prompted questions as apply to your situation. Stripe's support team will then review your request and assist you directly with regaining access to your account.

5. If still stuck after all steps → escalate to the **Supervisor column**.

**Do NOT escalate to CS by default for Stripe login/access issues** — most are resolved once the restaurant has the correct email.

**Step 3 — If the CS manager reaches out with the restaurant's consent:**
- Forward the email to Yuval (yuval.s@getsauce.com) — she will retrieve and send the form.

**Step 4 — If the restaurant demands the form sent directly via email:**
- Send the restaurant the following consent request (use the **"1099-K Form by Email"** HubSpot template):

> Hi!
> For us to send a 1099 via email, the owner of the restaurant must provide explicit consent.
> Please respond to this email (or have the owner respond) in the format below:
> My name is XXX, I'm the (owner, etc) of [Location Name], located at [Address]. I allow Sauce to send me my 1099-K forms of [Year] via email.
> Thank you,

- Once the owner replies with that exact consent statement, forward the consent email to Yuval (yuval.s@getsauce.com) and she will send the form.

**Exceptions:** The form cannot be emailed without the written consent statement above. Do not escalate Stripe login issues to CS before exhausting the email verification step.
**Approval Required:** Yes — written owner consent required before emailing the form directly.
**Last Updated:** 2026-02-26 — fully rebuilt per 1099 season guidance; added Stripe Connect login flow, escalation rules, email verification step

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
4. Move ticket to the "BO, CS, or Menu (Check Category)" column.

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

---

## Entry B2B-28: Menu & Website Escalation Routing

**Title:** Routing Menu, Photo, and Website Change Requests to the Correct Team
**Issue Type:** Escalation / Internal Routing
**Situation:** A restaurant or internal team submits a request to change a menu item, food photos, or website. You need to know which team handles it.
**Resolution:**

**Route based on request type:**

| Request Type | Route To | HubSpot Category |
|---|---|---|
| Change a menu item, price, name, or category (non-POS) | Menu Team | B2B: Menu Changes |
| Add/remove food photos on Toast | Menu Team | Menu: Toast Photos |
| Update an existing website (fonts, images, slogans, logo) | BO Team | BO B2B: Website Changes |
| **New website** (restaurant wants a website built) | Restaurant's CSM — **do not ticket from Support** | CSM opens a deal in the Customer Success upsell pipeline (Mariana / Tomas), which auto-routes to BO |
| Change delivery radius, credit card fees, or POS config | BO Team | BO Config Changes |
| Change integration or POS platform (e.g. Square → Toast) | OB Team | Change POS/Integration |

**Quick check:** If the menu is editable in the Sauce Dashboard → it's Sauce-managed (Menu Team). If not → it's likely Toast-managed (also Menu Team for photos, BO for config).

**Required ticket fields for every routing ticket:**
- **Company:** Correct restaurant location
- **Ticket Owner:** The restaurant's CS Manager
- **Category:** See chart above
- **Ticket Request:** Short summary of the change
- **Task Name:** Concise (e.g., "Chifa Kendall | Add Brunch Menu")

After updating fields, move ticket to **Received** to trigger automation.

**Exceptions:** If you're unsure, check whether the menu is editable in the Dashboard first. New-website requests are no longer free requests from Support — redirect the restaurant to their CSM (or the Customer Experience team for non-VIP restaurants, see **B2B-41**).
**Approval Required:** No.
**Last Updated:** 2026-10-21 — split website row: updates to an existing site still go to BO; new websites must come from CS via the upsell pipeline, applied from KB Policy Scan backlog (weeks of 2026-09-28 – 2026-10-19), approved by Josh Boock 2026-10-21 (source: Sofia Perez, 2026-10-06; clarified by Josh Boock, 2026-10-21); 2026-04-30 — added from Confluence: Menu & Website Escalation Routing

---

## Entry B2B-29: Toast Future Order Printing

**Title:** Restaurant Complaining That Future Orders Print Too Close to Fulfillment Time
**Issue Type:** Tablet / POS Issues
**Situation:** A restaurant is unhappy with when future orders print — too close to fulfillment time, or too early.
**Resolution:**

**General rule (all restaurants):** Future orders can print in 2 different ways:
1. **Based on prep time** — e.g., 15-minute prep prints 15 minutes before the fulfillment time.
2. **When the order is placed** — prints immediately.

This is a setting on the **tablet** for restaurants that print from the tablet, or in their **POS** if they print from the POS — set it to whichever mode the restaurant wants.

**Toast-specific:**
1. Direct the restaurant (or escalate to the appropriate team) to the Toast Online Ordering admin: **https://www.toasttab.com/restaurants/admin/onlineordering**
2. In that panel, they can configure orders to print immediately rather than scheduling print time closer to fulfillment.
3. Identify which printer is printing the future order tickets and confirm auto-approval settings in Toast.

**Relevant Toast help articles for escalation notes:**
- Future Order Setup, Pickup Mode, and Auto-Send
- Scheduling Future Orders
- Managing Your Takeout and Delivery Schedule
- Item Fire by Prep Time

**Exceptions:** POS-side print timing is the restaurant's configuration — Sauce cannot make the change on their behalf. Walk them through it or escalate to BO.
**Approval Required:** No.
**Last Updated:** 2026-07-16 — generalized: two print modes (prep-time offset or at placement) apply to tablet and all POS restaurants, not just Toast

---

## Entry B2B-30: Updating a Restaurant Phone Number via Virtual Answering

**Title:** Change a Restaurant's Phone Number in the Virtual Answering System
**Issue Type:** Restaurant Account Updates
**Situation:** A restaurant requests that their phone number be updated in the Sauce Virtual Answering system.
**Resolution:**
1. Open the restaurant's location in the Sauce Dashboard.
2. Click **Virtual Answering**.
3. Click **Edit Phone Number**.
4. Select **"This is not the right number. Please change it to"**.
5. Enter the new phone number.
6. Click **Next**.
7. Confirm the update message appears indicating the phone number has been changed.

**Exceptions:** See B2B-5 for context on restaurants with specific phone number configurations.
**Approval Required:** No.
**Last Updated:** 2026-04-30 — added from Confluence: Updating Restaurant Phone Number with Virtual Answering

---

## Entry B2B-31: Restaurant Updates Handled by Support

**Title:** Other Restaurant Account Updates That Support Can Make
**Issue Type:** Restaurant Account Updates
**Situation:** A restaurant requests a change that falls outside standard B2B entries — these are tasks transferred to the Support team's scope.
**Resolution:**

Support can make the following updates directly:

| Request | How |
|---|---|
| Change prep time | Via Dashboard website only (not tablet) |
| Change sales report frequency | Via Dashboard settings |
| Add or remove restaurant phone number | See B2B-30 (Virtual Answering) |
| Locations whitelist | Via Dashboard admin |
| Restaurant address update | Via Dashboard admin |
| Google Analytics / Meta Pixel setup | Share setup link; provide guidance |
| Enable Discount v2 | Share setup link (Fathom video available) |
| Discount code setup | See B2B-18 |

**Exceptions:** If the request is not listed above, route to BO Team or escalate for guidance.
**Approval Required:** Varies — most updates do not require approval unless flagged otherwise.
**Last Updated:** 2026-04-30 — added from Confluence: Restaurant Updates Done by Support

---

## Entry B2B-32: Tablet Setup and FAQ

**Title:** Tablet Setup, Eligibility, and Common Issues
**Issue Type:** Tablet / Hardware
**Situation:** A restaurant requests a new tablet, has questions about tablet vs. dashboard differences, or needs setup guidance.
**Resolution:**

**Tablet vs. Dashboard:**
- **Tablet app** — daily operations: acts as a POS for online orders, provides tracking links, monitors incoming orders in real time.
- **Web Dashboard** — management & setup: includes all tablet features plus analytics, menu management, user management, store hours, marketing tools.
- Rule of thumb: Tablet = real-time orders. Dashboard = management & configuration.

**Who should get a tablet:**
- Best for restaurants without an existing POS (Toast, Clover, Square).
- Restaurants with their own POS may request one, but **requires Noy's approval**.
- Useful for tracking links and order visibility when owners want it.

**Printer connection methods (ranked by reliability):**
1. **USB** — direct connection, rarely fails. Best option.
2. **Bluetooth** — simple setup, generally stable.
3. **Wi-Fi** — least reliable; vulnerable to weak or unstable network.

**Physical damage:**
- Overheating, drops, or broken screens → tablet replacement.
- If urgent and within Carlos' field range → may be hand-delivered.
- Always requires Noy's approval.

**Printer connection lost:**
- Usually caused by too many tablets on one printer or weak Wi-Fi.
- Fix order: restart tablet and printer → check Wi-Fi → test print from other tablets → if others work, delete and reconnect printer on the Sauce tablet.

**Exceptions:** Tablet replacements always require Noy's approval. See B2B-12 for replacement process, B2B-26 for app updates, B2B-27 for printer reconnection.
**Approval Required:** Yes — for new tablet issuance and physical replacements (Noy).
**Last Updated:** 2026-04-30 — added from Confluence: Tablet Setup and FAQ

---

## Entry B2B-33: BYOC — Pausing Third-Party Ordering

**Title:** BYOC Restaurants — Pausing Sauce and Third-Party Ordering
**Issue Type:** Restaurant Relations
**Situation:** A BYOC restaurant (aggregating 3rd parties and/or using their own POS) wants to pause ordering — either everything or only specific third parties.
**Resolution:**
- **Pause everything:** BYOC restaurants can pause themselves **from their POS** — this affects Sauce AND all 3rd parties. (Important for Casa Louie - Waterline, which uses Toast + BYOC.)
- **Pause a subset or a single 3rd party:** Support can do this in **Stream** — we have a support login that can pause and un-pause individual 3rd parties (credentials in kb-reference REF-5).
- The ability to pause individual 3rd parties from the Sauce dashboard is in development.

**Exceptions:** Never share Stream screenshots externally (see OPS-23).
**Approval Required:** No — restaurant request is sufficient.
**Last Updated:** 2026-07-16 — added from #support-policy-process (Josh, May–June 2026)

---

## Entry B2B-34: Orders Arriving After Closing Time — Feature Flag

**Title:** Restaurant Receiving Orders After Close
**Issue Type:** Restaurant Relations
**Situation:** A restaurant complains that orders keep coming in after their closing time.
**Resolution:**
1. There is a **closing-time feature flag** that can be removed so ordering ends with a prep-time buffer before the closing time.
2. Ask **Josh or Back Office** to remove the flag for the restaurant, then confirm with the restaurant that the issue is resolved.
3. Reference example: HubSpot ticket 45740934033.

**Exceptions:** None.
**Approval Required:** Yes — Josh or Back Office removes the flag.
**Last Updated:** 2026-07-16 — added from #support-policy-process (Josh, 2026-06-15)

---

## Entry B2B-35: Reaching a Restaurant — AI Answering Services and SMS

**Title:** How to Reach a Restaurant When Calls or Texts Aren't Landing
**Issue Type:** Restaurant Relations
**Situation:** You need to reach a restaurant owner/manager (e.g., for a refund approval) but the phone is answered by an AI virtual assistant, or texts are going unanswered.
**Resolution:**
- **AI virtual assistant answers the restaurant's phone:** Google the restaurant and call the number on their **Google My Business listing** instead.
- **Texting for approvals:** Prefer **Aircall SMS** over Sakari — responses tend to come back much faster. Use it when you need a restaurant owner/manager to approve a refund ticket.

**Exceptions:** None.
**Approval Required:** No.
**Last Updated:** 2026-07-16 — added from #support-policy-process (Josh 2026-05-31, Danny 2026-07-04)

---

## Entry B2B-36: BYOC Analytics in the Merchant Dashboard

**Title:** BYOC Analytics Now Live in the Merchant Dashboard
**Issue Type:** Restaurant Relations
**Situation:** A BYOC (Bring Your Own Courier) restaurant asks how to see performance data for their self-delivery orders vs. their marketplace/direct orders.
**Resolution:**
- BYOC locations can now view self-delivery performance directly in the **Analytics tab of the Merchant Dashboard**.
- They can choose to view results for **direct orders, self-delivery orders, or both channels combined**.
- Based on the selected view, they can explore total sales, customers, average order value, peak hours, and more.
- Coming next (not yet live as of 2026-07-15): these analytics will also be added to the relevant dashboard home widget and the Owner App.

**Exceptions:** No per-3rd-party-channel breakdown yet (requested, not yet built as of 2026-07-15).
**Approval Required:** No.
**Last Updated:** 2026-07-17 — applied from KB Policy Scan (source: Ella Bar-Or announcement, 2026-07-15)

---

## Entry B2B-37: Cashback Settings in the Merchant Dashboard

**Title:** Cashback Settings Now Available in the Merchant Dashboard
**Issue Type:** Restaurant Relations
**Situation:** A restaurant asks about setting up or managing cashback for their customers.
**Resolution:**
- Cashback settings are now available directly in the **merchant dashboard** as a self-serve option.
- **Cashback report:** merchants can download a full cashback report for their location (one row per order — customer details, subtotal, cashback earned and redeemed) from the **Download button on the Loyalty page**, or as **"Cashback Summary" in the Reports dropdown**.
- Coming next: a bi-weekly cashback recap for merchants showing the ROI of their loyalty program.

**Exceptions:** Unknown — not detailed in the source announcement.
**Approval Required:** No — appears self-serve.
**Last Updated:** 2026-10-21 — added cashback report navigation, applied from KB Policy Scan backlog (weeks of 2026-09-28 – 2026-10-19), approved by Josh Boock 2026-10-21 (source: Ella Bar-Or, 2026-09-28); 2026-07-17 — applied from KB Policy Scan (source: Sofia Perez huddle notes, 2026-07-11); navigation steps pending confirmation

---

## Entry B2B-38: Merchant Feedback Dashboard Revamp — Action-Focused Feedback and Follow-Up Tools

**Title:** Merchant Feedback Dashboard Revamp — Action-Focused Feedback and Follow-Up Tools
**Issue Type:** Restaurant Relations
**Situation:** A restaurant asks about the redesigned feedback/reviews experience, follow-up tools, replying to a review, or a change to feedback emails.
**Resolution:** The feedback experience has been redesigned to help merchants act on reviews, not just read them:
- New action-focused feedback dashboard with an Insights section (satisfaction metrics split by pickup/delivery).
- "Needs reply" is the default view, with summary cards and filters.
- Full context per review: related order, new vs. repeat customer, total spend, email, phone number.
- **Reply directly from the Feedback page** — no more copying the review into their own inbox. Hitting **Reply** opens a modal with a **suggested reply already drafted (AI-generated) from the review and personalized with the customer's name**; merchants can switch tone or edit the text before sending. The email goes out **from the restaurant's own address**, replies land in the restaurant's own inbox, and once sent the review moves to the **Replied** tab. (If a restaurant instead tries to reply from the notification-email link and gets an access error, see **B2B-45**.)
- Emailed, Called, and Skipped tracking so merchants can manage follow-ups.
- Redesigned feedback emails: shorter, cleaner, with star rating + comment preview, a "Read more" CTA to the dashboard, and full UTM tracking.
- **Promo code in reply (live):** a one-time setup on the Feedback page auto-adds a promo code to the end of every suggested reply, worded to match the rating. It's a regular promo — editable on the **Promotions** page and hidden from the storefront, so the code only goes out through replies.

**Exceptions:** None.
**Approval Required:** No.
**Last Updated:** 2026-10-21 — promo-code-in-reply now live, applied from KB Policy Scan backlog (weeks of 2026-09-28 – 2026-10-19), approved by Josh Boock 2026-10-21 (source: Ella Bar-Or, 2026-09-28); 2026-09-18 — enriched from KB Policy Scan, week of 2026-09-14 (source: Ella Bar-Or, 2026-09-10, forwarded by Josh Boock); earlier 2026-07-27 update: Ella Bar-Or, 2026-07-22

---

## Entry B2B-39: Disputed Charge Notification to Restaurants

**Title:** Notifying Restaurants of Disputed Charges (incl. Pelicana)
**Issue Type:** Restaurant Relations / Billing
**Situation:** A customer disputes a charge on one of a restaurant's orders and the restaurant needs to be informed. Pelicana locations in particular have been seeing an increase in these requests.
**Resolution:**
1. Use the HubSpot email template **"B2B: Disputed Charge Info"** to notify the restaurant that a charge on one of their orders has been disputed.
2. The template applies to any restaurant needing a dispute notification — it was created in response to volume at Pelicana, but is not Pelicana-specific.
**Exceptions:** None documented.
**Approval Required:** No.
**Last Updated:** 2026-08-24 — applied from KB Policy Scan (source: Sofia Perez, 2026-08-18, #support-policy-process; restated in the 2026-08-22 weekly huddle)

---

## Entry B2B-40: Customer Insights in the Merchant Dashboard

**Title:** Customer Insights — Merchant Dashboard Feature
**Issue Type:** Restaurant-Facing Features
**Situation:** A restaurant asks about a new "Customer Insights" page in their Merchant Dashboard.
**Resolution:** A **Customers → Customer Insights** page is rolling out gradually in the Merchant Dashboard. It provides:
- A breakdown of customer segments (Total, New, Occasional, Frequent) with flexible date filters.
- Top Recommendations — win back lapsed customers, reward frequent customers, convert new customers into regulars.
- A customer-location heat map, filterable by segment and ZIP code.
- A Top Customers ranked view (order count, total spend, ZIP code).

Direct restaurants asking about this to the Dashboard, and note the gradual rollout — not every merchant will see it yet.
**Exceptions:** Gradual rollout — some restaurants may not have access yet.
**Approval Required:** No.
**Last Updated:** 2026-08-24 — applied from KB Policy Scan, week of 2026-08-03 (source: Ella Bar-Or, 2026-07-28, forwarded by Josh Boock)

---

## Entry B2B-41: Customer Experience Team — Non-VIP Restaurant Support Routing

**Title:** Customer Experience Team — Non-VIP Restaurant Support Routing
**Issue Type:** Restaurant Relations
**Situation:** A non-Tier 1 / Tier 2 restaurant (no assigned CS Owner) has an issue Support can't resolve, or a restaurant issue needs escalation and no CS contact is assigned.
**Resolution:** A **Customer Experience Team** (Mariana Fonseca, Tomas Sarmiento) launched 2026-08-05 to handle all non-VIP restaurants — any restaurant that is not Tier 1 or Tier 2. To support this, CS Owner / CS agent assignments were removed from roughly 80% of restaurants in HubSpot.

When an issue can't be resolved and the restaurant has no assigned CS contact:
1. Do **NOT** tell them you'll escalate to their Account Manager. Tell them it will be forwarded to the Customer Experience Team, who will follow up directly.
   - Equally, do **NOT** tell a restaurant that they "do not have a Success Manager." Say the **Success team** will reach out — we don't want a restaurant to feel unloved. (Terminology note: this 2026-09-02 guidance says "Success team" where this entry says "Customer Experience Team"; pending confirmation of whether these are the same function, use the positive framing above and route as described here.)
2. Open a ticket, assign it to Tomas or Mariana, and send it to their pipeline.
3. Add the restaurant name to the ticket's **Company Level** field.
4. Use the updated `#B2B - CS Transfer` snippet: "I'll forward this to our Customer Experience Team, who will follow up on your concern... You can also contact them directly at success@getsauce.com, and they'll get back to you within 24 business hours."

See also **B2B-7** for the Slack tagging rule this replaced.
**Exceptions:** Tier 1 / Tier 2 (high-volume / high-revenue) restaurants keep their existing CS Owner assignment and process.
**Approval Required:** No.
**Last Updated:** 2026-09-07 — enriched from KB Policy Scan, week of 2026-09-07 (source: Josh Boock, 2026-09-02); originally applied 2026-08-24 (source: Sofia Perez, 2026-08-05)

---

## Entry B2B-42: Direct Storefront QR Code — Self-Serve Download from Dashboard

**Title:** Direct Storefront QR Code — Self-Serve Download from Dashboard
**Issue Type:** Restaurant Relations
**Situation:** A restaurant asks for a QR code linking to their Direct Storefront.
**Resolution:** Restaurants can now download their Direct Storefront QR code directly from the Merchant Dashboard — no BO ticket needed for this specific request. B2B-7's `BO B2B: Flyer Request` category still applies to other flyer/QR requests.
**Exceptions:** None noted.
**Approval Required:** No.
**Last Updated:** 2026-08-24 — applied from KB Policy Scan, week of 2026-08-10 (source: Noy Shavit, 2026-08-04, forwarded by Josh Boock)

---

## Entry B2B-43: Storefront Banner Message — Self-Serve Edit from Dashboard

**Title:** Storefront Banner Message — Self-Serve Edit from Dashboard
**Issue Type:** Restaurant Relations
**Situation:** A restaurant wants to add or change the banner message at the top of their Storefront menu page.
**Resolution:** Merchants can now add or edit the Storefront banner message (up to 1,000 characters) directly from the Merchant Dashboard — no CS/Support ticket through Core Admin needed. It is a two-way sync, so the value stays consistent across the Dashboard, Core Admin, and Storefront.
**Exceptions:** None noted.
**Approval Required:** No.
**Last Updated:** 2026-08-24 — applied from KB Policy Scan, week of 2026-08-10 (source: Ella Bar-Or, 2026-08-06, forwarded by Josh Boock)

---

## Entry B2B-44: Sauce Manager App — Restaurant Mobile App

**Title:** Sauce Manager App — Restaurant Mobile App
**Issue Type:** Restaurant Relations
**Situation:** A restaurant asks about, or needs help downloading, the Sauce/Merchant mobile manager app — or asks about a push notification they received from it; or wants to close their store.
**Resolution:** The **Sauce Manager (Merchant) App** is available on Apple and Android. The Merchant Dashboard shows a pop-up announcing it — on desktop the pop-up includes a QR code to scan, and on mobile it provides a direct download link.

The 2026-08-27 release (confirmed live in both app stores) adds:
1. **Dashboard Reports with export and share** — all reports previously only on the Merchant Dashboard are now in the app (sales summary, feedback, payout summary and more), and merchants can export or share them from the app (email, messaging apps, saved to device).
2. **Push notifications** — the app can send pushes, with an opt-in approval screen (standard OS prompt) and a settings screen where merchants manage notification preferences. The **first push is now live: a weekly analytics push sent every Monday morning (EST)** that takes the merchant straight to the **Analytics** screen when tapped. More push types are planned.
3. **In-app update popup** — a "what's new" popup surfaces when a new version is available, so merchants learn about updates without relying on app store changelogs.
4. General bug fixes and stability improvements.

**Store closure requests (added 2026-09-17):** If a restaurant asks to close their store, CS can suggest they download the Sauce Manager Mobile App (Android or Apple via https://qr1.be/75HEC1) to do so themselves. Use the HubSpot snippet **"B2B Download the Manager App"** for this.
**Release of 2026-09-24 adds:**
- **Sales by hour** on the Analytics screen.
- **Sales by ordering channel** — filter sales by each connected channel (Uber Eats, Grubhub, DoorDash, etc.).
- **Pause store per channel** — pause on one specific channel from the app without affecting the others.
- **Out-of-stock reminder push** — automatic push when a menu item has been out of stock 24+ hours.
- **Push-permission fallback** — a follow-up pop-up for users who dismissed push permissions.

**Exceptions:** None noted.
**Approval Required:** No.
**Last Updated:** 2026-10-21 — added 2026-09-24 release features, applied from KB Policy Scan backlog (weeks of 2026-09-28 – 2026-10-19), approved by Josh Boock 2026-10-21 (source: Tanya Maslo, 2026-09-24); 2026-09-21 — store-closure download suggestion added from KB Policy Scan, week of 2026-09-21 (source: Josh Boock, 2026-09-17); 2026-09-18 — enriched from KB Policy Scan, week of 2026-09-14 (source: Gal Shvebish, 2026-09-09, forwarded by Josh Boock); earlier 2026-09-07 update: Tanya Maslo, 2026-08-27, live in both stores confirmed by Noy Shavit

---

## Entry B2B-45: Restaurant Review Replies — Dashboard Login Requirement

**Title:** Restaurant Review Replies — Dashboard Login Requirement (Email Link Bug)
**Issue Type:** Merchant Dashboard / Known Bug
**Situation:** A restaurant tries to reply to a customer review using the link in their review-notification email and gets a "you don't have access to this review" error.
**Resolution:**
1. This is a known bug — the email reply link only works if the restaurant is already logged into the Merchant Dashboard.
2. Have the restaurant log into the Merchant Dashboard first; they can then reply to the review successfully.
3. A fix to smooth this out is in progress — no ETA given yet.
**Exceptions:** None.
**Approval Required:** No.
**Last Updated:** 2026-08-24 — applied from KB Policy Scan, week of 2026-08-17 (source: Josh Boock, 2026-08-10; restated in weekly huddle, Sofia Perez, 2026-08-15)

---

## Entry B2B-46: Discount Summary Report

**Title:** Discount Summary Report (Merchant Dashboard → Reports)
**Issue Type:** Merchant Dashboard Feature
**Situation:** A restaurant asks about reviewing a summary of discounts applied to their orders.
**Resolution:**
1. Direct the restaurant to **Reports → Discount Summary** in the Merchant Dashboard.
2. No detail on report contents or fields has been announced yet — confirm specifics with the Field/Growth team if a restaurant asks.
**Exceptions:** None stated.
**Approval Required:** No.
**Last Updated:** 2026-08-24 — applied from KB Policy Scan, week of 2026-08-17 (source: Sofia Perez, 2026-08-15, weekly huddle)

---

## Entry B2B-47: DoorDash Self-Delivery Deactivation Notice — Escalation Procedure

**Title:** DoorDash Notice to Deactivate Self-Delivery — Escalation Procedure
**Issue Type:** Escalation Procedure
**Situation:** Someone reaches out reporting they received a notice from DoorDash stating they must deactivate their self-delivery service.
**Resolution:**
1. Post the report in **#ops-escalations** with the notice (screenshot or forwarded email) attached.
2. Open an **Urgent** case in CS.
3. Do not attempt to advise on whether to deactivate — this is handled by Ops.
**Exceptions:** The announcement was worded as "every customer who reaches out," but the subject matter (DoorDash self-delivery / BYOC) is restaurant-facing. Treat any report of this notice — from a restaurant or a customer — the same way, and confirm the affected party in the escalation post.
**Approval Required:** No.
**Last Updated:** 2026-09-07 — applied from KB Policy Scan, week of 2026-08-31 (source: Yuval Shalom, 2026-08-24; restated in weekly huddle, Sofia Perez, 2026-09-05)

---

## Entry B2B-48: Toast Menu Hours — Self-Service Update

**Title:** Self-Service Toast Menu Hours Update (Snippet)
**Issue Type:** Restaurant Relations
**Situation:** A Toast-integrated restaurant needs to update its menu hours, including a holiday or one-off closure.
**Resolution:**
- Use the **"#B2B - Toast Menu Hours Update"** snippet to walk the restaurant through updating and publishing their hours directly in Toast — it covers the update/publish steps, expected sync time back to Sauce, and holiday/one-off closures.
- Try the self-service path first. Escalate with the **BO Toast Menu Changes** category only if the restaurant can't make the change themselves.

**Exceptions:** Toast-managed hours only — for Sauce-dashboard hours see **B2B-2**.
**Approval Required:** No.
**Last Updated:** 2026-10-21 — applied from KB Policy Scan backlog (weeks of 2026-09-28 – 2026-10-19), approved by Josh Boock 2026-10-21 (source: Sofia Perez, 2026-09-29)

---

## Entry B2B-49: BYOC Charges Bank Account — Dashboard Self-Serve

**Title:** Viewing and Updating the Bank Account Sauce Charges for BYOC Fees
**Issue Type:** Restaurant Relations / Billing
**Situation:** A BYOC restaurant asks which bank account Sauce charges for BYOC fees, or wants to change it.
**Resolution:**
- Merchants can see which bank account is connected for **BYOC charges**, and update it themselves, from **Store Settings** in the dashboard.
- It uses the same secure flow as BYOC onboarding — connect an account or enter details manually.

**Exceptions:** This is the account Sauce **charges**; it is not the payout account (Stripe Connect) covered in **B2B-4**.
**Approval Required:** No — self-serve.
**Last Updated:** 2026-10-21 — applied from KB Policy Scan backlog (weeks of 2026-09-28 – 2026-10-19), approved by Josh Boock 2026-10-21 (source: Ella Bar-Or, 2026-09-28, forwarded by Josh Boock)

---

## Entry B2B-50: Self Delivery Report — Recipient Email and Invoice ID

**Title:** Self Delivery Report — Recipient Email Setting and Invoice ID Column
**Issue Type:** Restaurant Relations / Billing
**Situation:** A restaurant asks who receives their Self Delivery report, wants to change the recipient, or needs to match a charge to an invoice.
**Resolution:**
- Merchants can see which email address receives their **Self Delivery report** in **Store Settings**, and request a change there.
- The report now shows **Invoice ID next to Charge Date**, with totals grouped by date and invoice.

**Exceptions:** Distinct from **B2B-36** (self-delivery performance in the Analytics tab).
**Approval Required:** No.
**Last Updated:** 2026-10-21 — applied from KB Policy Scan backlog (weeks of 2026-09-28 – 2026-10-19), approved by Josh Boock 2026-10-21 (source: Ella Bar-Or, 2026-09-28, forwarded by Josh Boock)

---

## Entry B2B-51: BYOC Store Emails and Reports — HubSpot Activities

**Title:** BYOC Store Emails and Reports — Find Them in HubSpot Activities
**Issue Type:** BYOC / Internal Reference
**Situation:** An agent needs to find or re-send a BYOC email or report (invoices, charge summaries) that was sent to a restaurant.
**Resolution:**
- All BYOC emails and reports sent to a store are in **HubSpot → Companies → Activities**. Share from there when the store needs a copy.

**Exceptions:** Agent-side retrieval only — it isn't confirmed that stores can pull these themselves.
**Approval Required:** No.
**Last Updated:** 2026-10-21 — applied from KB Policy Scan backlog (weeks of 2026-09-28 – 2026-10-19), approved by Josh Boock 2026-10-21 (source: Oleg Razenblat, 2026-10-05, forwarded by Josh Boock)

---

## Entry B2B-52: Rider Request for a Phone Order — "#B2B - Asking BAD Information"

**Title:** Rider Request for Phone Orders — "#B2B - Asking BAD Information" Snippet
**Issue Type:** Dispatch / Third-Party Delivery
**Situation:** A restaurant asks via WhatsApp or chat for a rider for a phone order (frequent with Marinara locations).
**Resolution:**
1. Send the **"#B2B - Asking BAD Information"** snippet to collect what Book a Driver needs:
> "We can absolutely check if we can book a rider for your order! To help us coordinate the delivery, could you please provide the following information?
> Customer name:
> Customer phone number:
> Delivery address:
> Additional delivery details (APT number, entrance instructions, gate code, or any other relevant information)
> Order subtotal
> Rider tip:
> Number of items (how many items are included in the order)
> Once we have these details, we can check the available options for arranging a rider! 😊"
2. Once you have the details, book through the standard Book a Driver process (see **OPS-42**; tipping in **OPS-11**). If the order is over $100 or 6+ items, check whether the large-order reason applies (it charges the restaurant).

**Exceptions:** None stated.
**Approval Required:** No.
**Last Updated:** 2026-10-21 — applied from KB Policy Scan backlog (weeks of 2026-09-28 – 2026-10-19), approved by Josh Boock 2026-10-21 (source: Sofia Perez, 2026-10-14; snippet text confirmed by Josh Boock, 2026-10-21)

---

## Entry B2B-53: BYOC — Restaurant Asks to Turn Off BYOC Immediately

**Title:** Restaurant Requests Immediate BYOC Shut-Off — "#B2B – BYOC - Request to Turn Off ASAP" Snippet
**Issue Type:** BYOC
**Situation:** A BYOC restaurant asks us to turn off BYOC immediately (they'd prefer deliveries to be handled directly by the third-party platform).
**Resolution:**
1. Send the **"#B2B – BYOC - Request to Turn Off ASAP"** snippet:
> "We completely understand that you'd prefer to have these deliveries handled directly by the third-party platform. While we're unable to turn off the integration immediately, we can reach out to our team to see if the delivery radius can be reduced so that more orders are handled by the third-party provider. We can also escalate your request to our Customer Success team for further assistance with turning off the integration as soon as possible.
> We'll do our best to help! Please let us know if you'd like us to move forward with these options."
2. Goal: acknowledge their concern with empathy and set the right expectations — we can't disable the integration on the spot, but we can check whether the delivery radius can be reduced so more orders go to the third-party provider, and escalate the turn-off request to Customer Success.
3. If they want to move forward: radius changes go through BO (see **B2B-23**); escalate the turn-off request to the Customer Success team.

**Exceptions:** Never promise immediate deactivation. If the restaurant only wants to pause ordering (not remove BYOC), see **B2B-33**.
**Approval Required:** No.
**Last Updated:** 2026-10-23 — new snippet, applied by KB auto-apply (source: Sofia Perez, 2026-10-21; restated in weekly recap 2026-10-22)

---

## Entry B2B-54: Merchant Dashboard Reports — Orders By Channel Summary & Self Delivery Invoices

**Title:** New Merchant Dashboard Reports — Orders By Channel Summary and Self Delivery Invoices
**Issue Type:** Merchant Dashboard / Reporting
**Situation:** A restaurant asks how to see sales or orders broken down by channel or fulfillment type, or where to find and download their Self Delivery invoices.
**Resolution:**
1. **Orders By Channel Summary** (Reports, merchant dashboard) — for locations where Sauce aggregates their 3PD orders. Shows sales, order count and average order value broken down by channel (Sauce Storefront, Uber Eats, DoorDash, Grubhub and more) and by fulfillment type (pickup, Sauce Delivery, 3PD delivery, location delivery). The dashboard shows a daily summary; the Excel export has one row per order with channel, fulfillment type and status columns so merchants can filter it however they need.
2. **Self Delivery Invoices** (Reports, merchant dashboard) — Self Delivery reporting is now organized by invoice. Each row is one invoice with its charge date, total, fees, credits and estimated commission saved. Merchants can download the invoice PDF or that invoice's order-breakdown CSV with one click (the same files we email them), and filter by last 3 months, last 6 months or all time.

**Exceptions:** Rolling out as of 2026-10-21; a merchant announcement email is planned once in full GA. Orders By Channel Summary only applies to locations where Sauce aggregates 3PD orders.
**Approval Required:** No.
**Last Updated:** 2026-10-23 — new, applied by KB auto-apply (source: Ella Bar-Or, 2026-10-21, forwarded by Josh Boock)

---

## Entry B2B-55: Restaurant Requests a Car — "B2B - Car request" Snippet

**Title:** Restaurant Requests a Car for an Order — "B2B - Car request" Snippet
**Issue Type:** Dispatch / Book a Driver
**Situation:** A restaurant asks for a car (rather than another vehicle type) for a delivery, usually for a large non-catering order.
**Resolution:**
1. Send the **"B2B - Car request"** snippet:
> "We understand that you'd prefer to have a car assigned to this order. For non-catering orders, we're unable to guarantee a specific vehicle type. However, you can submit a **Large Order – Book a Driver** request, which allows our driver service to send multiple couriers when needed to help deliver the order.
> **To book through your dashboard:**
> 1. Go to **Orders** and select the order.
> 2. Click the red **Book a Driver** button in the top-right corner.
> 3. Complete the form and select **Large Order** as the reason.
> 4. Make sure to enter the correct order subtotal and tip, then click **Submit**.
> Would you prefer to submit the request through your dashboard, or would you like us to help you with it? 😊"
2. If they want our help, book it with the **Large Order** reason (see **OPS-42**).

**Exceptions:** Applies to non-catering orders. For catering, see **OPS-12**. Large Order is one of the BaD reasons that automatically charges the restaurant (OPS-42).
**Approval Required:** No.
**Last Updated:** 2026-10-30 — new snippet, applied by KB auto-apply (source: Sofia Perez, 2026-10-28; restated in weekly recap 2026-10-29)
