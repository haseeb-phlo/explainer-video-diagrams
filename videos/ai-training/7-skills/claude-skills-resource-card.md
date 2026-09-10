# Resource Card - Day 7: Skills

Paste this into the AI Ops Learn Resource Card for Day 7, alongside the Loom.

> **Two things to do before publishing this card.**
> 1. **There is no Day 7 entry in `Phlo_Mandatory_AI_Course_Curriculum.docx`**, so the
>    "Resources linked from this video" list could not be lifted from it. The links
>    below are named, not pasted - **paste the current URLs in and check each one
>    resolves** before the card goes live.
> 2. Everything in "The detail that did not fit on the board" was on the previous
>    eleven-beat Skills board and is **product surface that dates fast**. Re-check it
>    against Claude before publishing, and again at each 90-day refresh.

---

## What you are shipping today

**One Skill, published to the gallery, tested on a known input.** That is the whole
assignment. Twenty minutes.

**Pause-and-try:** find the correction you have typed most often this month. Not the most
important one - the most repeated one. That is your first Skill.

## The five things from the video

1. **The fourth time is the signal.** The first time you type a correction it is a
   conversation. The fourth time it is a Skill you have not written yet.
2. **Context is what it knows, a Skill is what it does.** Pasting a document means you
   want a Project. Re-explaining the order things happen in means you want a Skill. They
   stack - the Project holds the background, the Skill runs the procedure.
3. **Search the gallery first.** A Skill you enable in ten seconds beats a Skill you
   spend an hour writing.
4. **Name the hidden assumption.** The step you never wrote down is the one that breaks
   it. Write for someone who has never done the job.
5. **Test on a known input.** One input where you already know the right answer, run
   before the edit and after. It is the only way you know the edit worked.

## The safety rule, repeated

**A Skill is a shared file.** It can be published, pushed to a whole organisation, and
opened by somebody who is not you.

- Never put confidential or sensitive data inside a Skill. No real names, no account
  numbers, no patient or clinical detail, nothing you would not put in a shared folder.
- Write the **procedure**, not the **particulars**. If a Skill needs sensitive input, the
  input goes into the chat at the time, not into the file.
- Fictional placeholders only in any example inside a Skill: `Patient_001`, `J. Doe`,
  `NHS_TEST_123`, `acme.pharmacy@example.com`.
- A Skill must never be written so that it makes a clinical or dispensing decision
  unsupervised. Any procedure touching prescriptions, dispensing or patient records keeps
  the human gate: **Claude drafts, a person approves, then the record is updated.**
- Check the Phlo AI Use Policy before you publish a Skill that touches anything
  patient-facing.

---

## The detail that did not fit on the board

Six beats could not carry the whole feature surface. This is the rest of it.

### What is inside a Skill

A Skill is a folder. The only required file is `SKILL.md`, plain Markdown:

- `name:` - a short identifier, e.g. `team-report-format`
- `description:` - **when to use it.** This is the trigger. It is how Claude decides
  whether to open the Skill at all, so make it specific. A vague description is the most
  common reason a Skill never fires.
- Everything under that is the instructions, in plain English.

Optional extras for more advanced Skills:

- `scripts/` - code the Skill can run
- `resources/` - reference files the Skill can read

### How Claude decides to use one

1. **You ask.** You give Claude a task, in normal language. You do not name the Skill.
2. **Claude scans.** It reads the *descriptions* of the Skills available to you and picks
   the relevant one, or none.
3. **Claude applies.** It loads those instructions and follows them.

Only relevant Skills load, which is why having a lot of them enabled does not slow Claude
down or eat your context window. It also means the `description` is doing almost all of
the work.

### The four kinds of Skill

| Kind | Where it comes from |
|---|---|
| **Built in** | Anthropic's own - Word, Excel, PowerPoint and PDF creation |
| **Custom** | Written by you or your team, for your own workflows |
| **Organisation** | Pushed to everyone by admins; they appear without you doing anything |
| **Partner** | From the Skills gallery - Notion, Figma, Atlassian and others |

### Finding and switching one on

1. Open **Customize** in your account
2. **Skills** → **+** → browse
3. Enable what you need. Organisation Skills appear on their own.

**Prerequisite:** code execution has to be enabled in settings. If the Skills section is
missing or a Skill will not run, check that first.

> **Wording check before publishing.** The video calls this shelf of ready-made Skills
> **the gallery**; the steps above came from the previous board and say **browse**. The
> in-product wording may be different again. Open Claude, confirm what the surface is
> actually called, and make the video, this card and the enable steps agree - all three
> together, not one at a time. A viewer follows this card straight out of the video.

### Skills against the other Claude features

| Feature | What it gives Claude | When it applies |
|---|---|---|
| **Skill** | how to do a task | only when the task matches its description |
| **Project** | background knowledge and files | always, inside that Project |
| **MCP / Connector** | access to tools and live data | when the tool is called |
| **Instructions for Claude** | your general preferences | always, everywhere |

They stack. A Skill can tell Claude how to use a Connector well, and a Skill can run
inside a Project and use what the Project knows.

### Do this, avoid this

**Do**
- Keep the `description` specific - it is the trigger
- One Skill, one job
- Reuse approved Skills rather than forking your own copy
- Write for someone who has never done the job
- Test on a known input before and after every edit

**Avoid**
- Vague descriptions ("helps with reports")
- Cramming several jobs into one Skill
- Anything confidential or sensitive inside the file
- Asking Claude to write the Skill for you from scratch - you bring the procedure, Claude
  critiques it

### The prompt from beat 5, to copy

> Here is a Skill I wrote. Read it as if you had never done this job. Which step is
> ambiguous? What would a new starter get wrong?

Then fix what it flags and run your known input again. You are asking Claude to critique
what you wrote, not to write it for you.

### One shortcut

Claude has a **skill-creator** Skill. Ask it to help you turn a procedure you describe
into a properly structured Skill. You still bring the procedure - and you still test it
on a known input.

---

## Links

**Paste the current URL against each before publishing. Do not publish a broken card.**

- Anthropic docs - Agent Skills overview
- Anthropic docs - authoring a `SKILL.md`
- Claude help centre - using Skills in the Claude apps
- The Skills gallery, for browsing what already exists
- Phlo AI Use Policy (AI Ops)
- Day 4 - Claude Projects (the "context, not procedure" other half)
- Day 8 - Cowork (watch after this one, deliberately)

## Refresh

Tool-specific videos refresh every 90 days. At each refresh re-check, in this order:
the gallery contents and its name, the enable path and the code-execution prerequisite,
the four kinds of Skill, and the plan availability. Those date fastest. The five things
from the video, and the safety rule, do not.
