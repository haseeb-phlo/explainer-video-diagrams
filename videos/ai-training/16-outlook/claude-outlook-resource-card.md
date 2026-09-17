# Day 16 - Claude in Microsoft Outlook - Resource Card

Everything the board deliberately leaves off, in one place. **The board names the tool and never
the tier**, which is what keeps it from dating. Every product fact lives here instead.

> **When a fact moves, fix this card, not the board.** The single exception is `BETA_LINE` in
> `build_outlook.py` - the one board string that will date. See *If the beta ends* at the end.

**Post this under the Loom.** It is a deliverable of the video, not an afterthought.

> **The recording for this board is filed under Day 14.** The Outlook add-in Loom (<https://www.loom.com/share/10e4eaa90c0c4cf584c1fc562b3ed912>)
> was attached to `videos/ai-training/14-word-powerpoint/` on 2026-09-17 at the user's
> request. **Day 16 carries the board and the product detail; Day 14 carries the video.**
> Day 14's pause-and-try was widened to three strands so its task covers the reply too.


---

## ✅ Verified against Anthropic's live documentation on 2026-09-17

Primary source: **[Use Claude for Outlook](https://claude.com/docs/office-agents/outlook)**.
Every fact below was read off Anthropic's own page on that date.

**URL rot, third instance in this repo.** The support-centre article
`support.claude.com/en/articles/14855664-use-claude-for-outlook` now **301s** to the
`claude.com/docs/office-agents/…` path. Day 12 found the same for PowerPoint and Day 15 for
Excel. **Link the docs path, not the support-centre one.**

---

## Availability

> "Claude for Outlook is currently in beta and available to Pro, Max, Team, and Enterprise plans."

**Beta - and this is the odd one out in the block.** Claude for Excel, PowerPoint and Word are
**generally available** on Pro, Max, Team and Enterprise. Outlook is the only one of the four
still in beta.

Phlo is on a **Team** plan, so the plan is not the blocker here. Getting it installed is a
*Microsoft* admin job, not a Claude one - see below.

### Supported Outlook clients

| Works | Does not work |
|---|---|
| Outlook on the web | Outlook 2016 and 2019 perpetual / volume-licensed editions |
| Outlook on Windows - new **and** classic, with a Microsoft 365 subscription | Outlook on iOS |
| Outlook on Mac, with a Microsoft 365 subscription | Outlook on Android |
| | Mailboxes on Exchange **on-premises** |

**Exchange Online through Microsoft 365 is required.** There is no mobile add-in - if somebody
says "it isn't there on my phone", that is expected, not a fault.

---

## Getting it

**Install it yourself:** open the Claude for Outlook listing on
[Microsoft AppSource](https://appsource.microsoft.com/), select *Get it now*, then open Outlook,
open any email, select the **Claude** button in the message ribbon and sign in.

If the Claude button is not on the message: open the overflow menu on the reading pane, choose
**Customize actions**, and tick **Claude** under Apps. It then appears on every message and in
the Home ribbon. **Pinning the task pane** keeps it open as you move between messages.

**Deploy it to the organisation** (Microsoft 365 Admin Center - a Microsoft admin job):

1. Settings → Org Settings → User owned apps and services → turn on **Let users access the Office Store**
2. Settings → **Integrated apps** → search **Claude for Outlook** in AppSource
3. Deploy to the organisation, or to specific people or groups
4. **Grant Microsoft Graph admin consent** - see below. This is separate from the deployment and is easy to miss.

**Two documented gotchas worth knowing before anyone opens a ticket:**

- **Microsoft Entra PIM breaks deployment.** The Integrated apps page does not recognise admin
  roles activated through Privileged Identity Management, so deployment fails. It is a known
  Microsoft issue (tracking ID 11126536). Work around it by deploying from an account with the
  role **permanently active** rather than PIM-eligible. Individual users can still install it
  themselves in the meantime.
- **If your organisation has disabled Office Store access,** admin-deployed add-ins may not
  appear. Deploy from the **manifest XML** instead (Integrated apps → Upload custom apps →
  Office Add-in). Full-organisation rollout can take up to 24 hours on the Microsoft side.

### The Microsoft Graph consent step

Claude for Outlook reads mail and calendar through Microsoft Graph. This needs a **one-time,
tenant-wide grant from a Global Administrator**, separate from the add-in deployment. The
permissions screen lists exactly four delegated scopes:

`Mail.ReadWrite` · `Calendars.Read` · `User.Read` · `offline_access`

**Note what is not on that list: `Mail.Send`.** That is the mechanism behind the board's beat 2.

The grant takes effect immediately; only the add-in rollout can take 24 hours. **If this step is
skipped, every user sees "Need admin approval"** the first time Claude tries to read mail.

**If tenant policy forbids consenting to a third-party multi-tenant app,** you can register your
own single-tenant Entra application and point the add-in at it (`?graph_client_id=…` appended to
the manifest URL). The data flow is identical - the Graph token stays in the user's Outlook
client either way - but approval and Conditional Access live entirely under an application your
organisation owns. US Government and national clouds (GCC High, DoD, 21Vianet) **must** use this
route with a matching `graph_cloud` value.

---

## What it does - the six documented jobs

1. **Triage** the unread inbox into *action items for you*, *items Claude can handle for your review*, and *noise you can archive in one selection*. Each action item carries a one-line reason; handleable items arrive pre-drafted. (This is the source for the board's beat 1.)
2. **Draft** replies, reply-alls and forwards, landed **unsent** in Outlook's compose pane.
3. **Summarise** long threads into decisions made, open items and who owes what, **with per-email citations** - selecting one opens that message in Outlook.
4. **Read `.docx` and `.xlsx` attachments inline** without opening them. **PDFs are not read inline** - save the file and upload it through the sidebar. For `.pptx`, open the deck in PowerPoint with the thread loaded as context.
5. **Search the mailbox by topic**, not only by keyword, returning citations that open the source message.
6. **Find meeting times and draft invites** into Outlook's native appointment form, plus a one-page **meeting prep** brief from recent threads and attached documents.

### Two details that change what you type

- **Tone is learned from your sent folder** - it matches your sentence length and formality. The board's beat 4 deliberately makes the *narrower* claim, that choosing the register is yours, because that is the part that stays true whatever the tone-matching does.
- **Claude leaves the closing off** so Outlook can append your configured signature without duplicating it. It also **chooses reply versus reply-all deliberately and warns before adding anyone who was not on the thread.**

---

## 🔴 The governance facts - the ones to get right

**Claude never sends.** *"Claude never sends mail or invites on its own. The add-in does not
request the `Mail.Send` permission. Every draft lands unsent in Outlook's compose or appointment
form, and you click Send."* This is the load-bearing fact of the whole video.

**Where mailbox content goes.** Claude reads the open item via Office.js; anything spanning the
mailbox (thread retrieval, search, free/busy, move or flag) goes through Microsoft Graph. **All
Graph calls run in your browser and the Graph token is never sent to Anthropic.** When you sign
in with a Claude account, mailbox content Claude reads **becomes part of the prompt sent to
`api.anthropic.com`**. The add-in keeps no server-side copy or index of your mailbox.

**Retention and audit - read this twice on a Team plan.**

- Inputs and outputs are **deleted on Anthropic's backend within 30 days**.
- Claude for Outlook **does not inherit custom data retention settings** your organisation has configured.
- It is **not included in Enterprise audit logs**.
- **On Pro, Max and Team plans, observability and audit export are not available.** Only Enterprise can route audit telemetry to its own OpenTelemetry collector, and only Enterprise with the Compliance API enabled gets sessions included there (public beta).

**Chat history is local.** Stored in the browser's IndexedDB, not on Anthropic's servers, not
synced across devices, cleared when you clear browser data. Outlook and Excel histories are
separate.

**Prompt injection.** *"Email bodies and attachments are untrusted input and may contain
instructions intended to manipulate Claude rather than you."* A routine inbound email can carry
hidden text telling Claude to forward a thread or draft a reply you never asked for. **Review
every draft and inbox action before accepting it, especially from external senders.** This is
the second half of the board's beat 5 caution.

### The beta's own "not recommended for" list

Anthropic's page says Claude for Outlook is **not recommended for**:

- Unattended sending
- Client-facing or counterparty correspondence **without reading the draft first**
- Replacing your judgment on which emails matter or how to handle a relationship
- **Mailboxes containing privileged or regulated data without appropriate organizational controls**

That last line is the source of the board's beat 5 chip, and it is the one that matters most in
a regulated pharmacy. The board keeps it generic on purpose; this card is where the specific
version lives. **Nobody should point this at a mailbox carrying clinical or patient
correspondence until somebody has decided, in writing, that the controls are in place.** That is
a decision for the AI Use Policy, not for the person installing the add-in.

And their four safe-use rules:

- Review drafted replies and invites before sending, **especially recipient lists**
- Verify thread summaries against the cited source emails for high-stakes conversations
- Apply appropriate Microsoft 365 permissions and Conditional Access policies
- **Maintain human oversight for anything leaving your organization**

---

## ⚠️ The fastest-dating line on this card

**Model availability.** The docs list a choice of **Claude Opus 4.7, Opus 4.6 and Sonnet 4.6**
when signed in with a Claude account, and **Opus 4.7 only** when connected through a third-party
platform (Vertex AI, Azure AI Foundry, an LLM gateway). Model line-ups move faster than anything
else here. **The board names no model, so this cannot date the video** - re-check it before
re-recording and fix it here.

**Third-party platforms.** If an organisation routes API traffic through Amazon Bedrock, Vertex
AI, Azure AI Foundry or an internal gateway, the add-in can be used **without Claude accounts** -
the same gateway pattern Claude Code uses. On Bedrock, Vertex or a gateway routing to them,
**no mailbox content reaches Anthropic at all.**

---

## Where this sits

**Day 16**, and the fourth and last of the Microsoft block: **Word → Excel → PowerPoint →
Outlook** (Days 14, 15, 14 and 16 respectively - Word and PowerPoint share Day 14). It is last
because it is the only one whose output leaves the building, and because beat 7 - one
conversation touching the document, the sheet, the deck and the reply - only makes sense once a
viewer has the other three.

The cross-app behaviour is documented: *"Claude for Outlook shares context with Claude for
Excel, PowerPoint, and Word, so Claude can work across your open Office apps in a single
conversation."* See the **Work across M365 apps** page for setup.

## If the beta ends

Beat 2 is the only beat that needs rebuilding, and the board was built that way on purpose:

1. Edit **`BETA_LINE`** in `build_outlook.py` - one constant, used once. Keep the replacement
   **the same length or shorter** and nothing on the board reflows.
2. Rebuild: `python3 videos/ai-training/16-outlook/build_outlook.py`, then `python3 build_all.py`.
3. Change the second paragraph of beat 2 in `claude-outlook-script.md`. Nothing else in the narration
   mentions beta.
4. Update *Availability* on this card.

If the video is already recorded, a line in the Loom description is enough - it does not need a
re-record. That is the same call Day 10 made when its beat 2 pointer chip was regenerated.
