# Day 15 - Claude in Microsoft Excel - Resource Card

> **Audience: advanced.** This video was retargeted on 2026-09-16 at advanced users - people
> fluent in Excel *and* fluent with Claude. It is not general-audience material and does not
> behave like the rest of the AI Ops Learn series. See *Where this sits* at the end.

Everything the board deliberately leaves off, in one place. **The board names the tool and
never the tier**, which is what keeps it from dating. Every product fact lives here instead.

> **When a fact moves, fix this card, not the board.**

**Post this under the Loom.** It is a deliverable of the video, not an afterthought.

---

## ✅ Verified against Anthropic's live documentation on 2026-09-16

Primary source: **[Use Claude for Excel](https://claude.com/docs/office-agents/excel)**. Every
fact below was read off Anthropic's own pages on that date. **Three things the previous
version of this card got wrong are corrected here** - see *What the doc check changed*.

Phlo is on a **Team** plan, and for Excel that turns out to be good news: the add-in is
generally available on Team.

---

## Availability

> "Claude for Excel is generally available to Pro, Max, Team, and Enterprise plans."

**Generally available - not beta, and not "Pro and up".** Claude for Excel, PowerPoint and
Word are GA on all paid Claude plans; Claude for Outlook is in beta.

There is **no separate Claude for Excel allowance** - "your use of Claude for Excel is
associated with your existing Claude account and is subject to the same usage limits".

---

## Getting it

**Install it yourself:** open the [Claude for Microsoft 365 listing on Microsoft AppSource](https://marketplace.microsoft.com/en-us/product/office/WA200010725?tab=Overview),
select *Get it now*, then open Excel, activate the add-in and sign in with your Claude account.

**Deploy it to the organisation** (Microsoft 365 Admin Center, so this is a *Microsoft* admin
job, not a Claude owner toggle):

1. Settings → Org Settings → User owned apps and services → turn on **Let users access the Office Store**
2. Settings → **Integrated apps** → Add-ins
3. Search **Claude for Microsoft 365** in AppSource
4. Assign to the organisation, or to specific users or groups

Afterwards users activate it from **Tools → Add-ins on Mac**, or **Home → Add-ins on Windows**.

**Known Microsoft bug:** if your org uses Entra Privileged Identity Management for admin
roles, the Integrated apps page does not recognise PIM-activated roles and deployment fails
(Microsoft tracking ID 11126536). Work around it by deploying from an account whose role is
permanently active rather than PIM-eligible. Individual users can still self-install.

If "Let users access the Office Store" is off, deploy the [custom manifest XML](https://pivot.claude.ai/manifest-excel.xml) instead.

**There is no documented keyboard shortcut.** The previous script's `Ctrl+Alt+C` does not
appear anywhere in the current docs - do not put it on camera.

### Supported Excel builds

| Works on | Does **not** work on |
|---|---|
| Excel on the web | Excel 2016 and 2019 perpetual or volume licence |
| Excel on Windows, Microsoft 365 subscription, build 16.0.13127.20296 or later | Excel on iPad (no SharedRuntime support) |
| Excel on Mac, version 16.46 or later, build 21011600 or later | Excel on Android |
| | Older Microsoft 365 builds below the SharedRuntime threshold |

---

## What it can actually do

Anthropic's own list:

- Ask questions about your workbook and get answers with **cell-level citations** you can click to jump to the referenced cell
- Adjust assumptions **while keeping formula relationships intact**, so downstream cells recompute
- Identify and resolve errors and their root causes
- Generate new spreadsheet models, or populate existing templates
- Work across **multi-tab** workbooks
- Pull external context through connectors such as S&P Global, LSEG and Daloopa
- Apply enabled **Skills** automatically while you work

**Native Excel operations:** sort, filter, edit pivot tables, apply conditional formatting,
create data validation dropdowns. Just ask for them directly.

**Not supported:** data tables · macros and VBA.

> **Beat 4 of the board frames four of these as jobs you ask for, not as a feature list.**
> "Tell me which rows did not match" is a reasonable ask rather than a documented feature -
> the documented capability underneath it is multi-tab working. Do not read beat 4 back as
> though it were Anthropic's own list; this section is.

---

## Two things that change what you type

**Persistent Instructions.** Open **Settings in the add-in sidebar** → the **Instructions**
field. It applies to every conversation in Excel - formatting conventions, currency and
locale, recurring context about your workflow. **Instructions set in Excel apply only to
Excel**; PowerPoint and Word each have their own. *This is what beat 2's chip points at: you
set the model's contract once, not every chat.*

**Skills, invoked with `/`.** Skills you have enabled in Claude settings are available in
every Claude for Microsoft 365 add-in, and Claude applies relevant ones automatically. Type
`/` in the sidebar to pick one directly. **Starter Skills ship preloaded for financial
analysis** - including auditing a model for formula errors and balance-sheet integrity, LBO /
DCF / three-statement models, comps analysis and data cleaning. *This is what beat 8 points
at: the audit you want probably already exists as a Skill.*

---

## Guardrails that are actually in the product

- **Overwrite protection** - "Claude warns you before overwriting existing data to avoid accidental data loss."
- **Risky-operation confirmations** - "When Claude proposes a risky operation, you are asked to confirm before it runs."
- **Auto-compaction** - long conversations are compacted into new ones so you do not run out of context.

These are guardrails, not a safety net. They are why beat 2 says what it says, and they do
not replace beat 7.

### One claim on the board that is NOT from the docs

**Beat 5's first half - "it is not deterministic" - is a property of the model, not a
documented behaviour of Claude for Excel.** Anthropic's Excel page says nothing about
run-to-run variation. It is on the board because it is true of every LLM and because it
changes what an advanced user does (re-verify after a re-run), but if anyone challenges it,
it is not citable to this page. **Beat 5's second half IS documented**: "longer
conversations are automatically compacted into new conversations to avoid running out of
context."

---

## Anthropic's own limitations and best practices

**Claude for Excel is *not recommended* for:**

- Final client deliverables without human review
- **Audit-critical calculations without verification**
- Models containing highly sensitive or regulated data without proper controls

**Best practices, verbatim:**

- "Always review changes before finalizing your work."
- "Start with a trusted copy of the workbook before asking Claude to edit widely."
- "Be specific about what you want changed."
- "Verify that outputs match your organization's standards and your own judgment."

> **This is the whole day, in Anthropic's own words.** Beat 6 and beat 7 are not a Phlo
> invention or a cautious gloss - "audit-critical calculations without verification" is on
> the vendor's own limitations list, and "start with a trusted copy" is the chip on beat 2.

---

## Prompt injection - the documented warning

> **"Only use Claude for Excel with trusted spreadsheets. Files from external sources can
> contain hidden instructions that manipulate the add-in into extracting data, modifying
> records, or performing destructive actions."**

Anthropic states that testing "has identified scenarios where Claude for Excel can be
manipulated to extract sensitive information, modify critical data, or perform destructive
actions if allowed to act without verification". Downloaded templates, vendor files and data
imports are the named risks. **Review the confirmation prompts carefully, especially for
files from outside.** This is the half of beat 9's red rule that comes straight from the docs.

---

## Data handling - read this one properly, we are regulated

- Inputs and outputs are deleted on the backend **within 30 days**; data is cached for a few hours after deletion so recently closed workbooks stay available.
- **Chat history is stored locally in your browser (IndexedDB).** Conversations are not stored on Anthropic's servers, are not synced across devices, and can be cleared from Settings. Reinstalling the add-in does not remove it.
- ⚠️ **Claude for Excel does not inherit custom data retention settings your organisation has set.**
- ⚠️ **Activity is not included in Enterprise audit logs.**
- Compliance API coverage for Claude for Excel sessions exists for Enterprise orgs with the Compliance API enabled, and is **in public beta**.

**The practical rule for us:** the two ⚠️ lines mean a Claude for Excel session sits outside
the retention and audit controls you would otherwise assume. That is exactly why the board's
beat 9 says never to put confidential or personal data into a sheet you are going to share,
and why nothing patient-identifiable goes near this add-in.

---

## The other capability: file creation in chat

Different product, same-looking outcome. You describe a sheet in the Claude chat and get a
real file back.

- **Plans:** Free, Pro, Max, Team and Enterprise. **Enabled by default**; Team and Enterprise owners can *disable* it in organisation settings.
- **Creates:** `.xlsx`, `.pptx`, `.docx` and PDF, plus Python scripts and PNG visualisations.
- **Where it lands:** download straight from the conversation, or save to Google Drive.
- **Limit:** 30MB per file, uploads and downloads.
- Carries its own prompt-injection warning: a bad actor can add instructions via external files or websites that trick Claude into reading sensitive data from a connected knowledge source and using the sandbox to make an external network request to leak it.

---

## What the doc check changed (2026-09-16)

| Previously believed | Actually |
|---|---|
| Add-in is "Pro plan and up", possibly beta | **GA on Pro, Max, Team and Enterprise.** The flagged tier conflict is resolved: the old module-2.8 script was wrong, and Day 12's PowerPoint finding extends to Excel |
| File creation needs an owner to **enable** it on Team | **Inverted** - it is on by default and owners can *disable* it |
| `Ctrl+Alt+C` opens the add-in | **Not in the docs at all.** Activation is Home → Add-ins (Windows) or Tools → Add-ins (Mac) |
| `support.claude.com/.../12650343-use-claude-for-excel` | **301s** to `claude.com/docs/office-agents/excel` |
| `claude.com/resources/tutorials/getting-started-with-claude-in-excel` | **301s** to `academy.claude.com/tutorials/...` |
| Board said Claude highlights what it changed | **Not documented.** What *is* documented is overwrite warnings and risky-operation confirmations - the board was changed to say that instead |

> **Flag for Day 12:** CLAUDE.md records that "both file creation and the add-in need an
> owner to enable them on a Team plan". For **Excel** the current docs say otherwise on both
> counts. Worth re-checking the Day 12 PowerPoint card against `claude.com/docs/office-agents/powerpoint`
> before that video is re-recorded - this card does not assume Day 12 is wrong, only that
> the two now disagree.

---

## Links (all checked 2026-09-16)

- **Use Claude for Excel** (primary): https://claude.com/docs/office-agents/excel
- Connectors and Skills: https://claude.com/docs/office-agents/connectors-and-skills
- Claude for Microsoft 365: https://claude.com/claude-for-microsoft-365
- Create and edit files with Claude: https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude
- *Advancing Claude for Excel and PowerPoint* (11 March 2026): https://claude.com/blog/claude-excel-powerpoint-updates
- Tutorial, ~7 min video: https://academy.claude.com/tutorials/getting-started-with-claude-in-excel
- Anthropic webinar, *Best Practices: Claude for Excel and Claude for PowerPoint*: https://www.anthropic.com/webinars/best-practices-for-claude-in-excel-and-powerpoint

**Do not link** `claude.com/blog/create-files` - Day 12's check (2026-09-14) established it is
a superseded September-2025 launch post.

---

## Related videos in the course

- **Day 3 - Prompting and CRISPE.** Beat 2 is the Context dial, pointed at a spreadsheet - and pushed past where Day 3 leaves it.
- **Day 7 - Skills.** "Test on a known input" is the same instinct as reconciling a second way - and beat 8's auditing Skill is a Day 7 artefact.
- **Day 10 - design work with Claude.** Where *an acceptable output is the dangerous one* is argued in full. This board is that argument with a number instead of a page.
- **Day 12 / Day 14 - Claude in PowerPoint, and in Word and PowerPoint.** The deck the £18.33 on beat 1 ends up in. Same Microsoft 365 add-in family, and context is shared across all of them in one conversation.

## Where this sits - and a decision somebody has to make

This board assumes fluency in both Excel and Claude. It uses modelling vocabulary without
glossing it, and its central beat only works on a room that will *try* to find the bug and
fail. **That makes it a poor fit for the mandatory all-staff course**, which is written for
clinical, ops, commercial and support colleagues as well as analysts.

If it goes into the mandatory track it needs either a general-audience sibling or an explicit
**advanced / optional** label on the Loom. That is a curriculum call, not something to fix by
softening the board - a version pitched at everyone would lose the only thing this one has.
