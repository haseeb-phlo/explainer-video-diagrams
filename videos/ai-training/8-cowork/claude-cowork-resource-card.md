# Resource Card - Day 8: Cowork

Paste this into the AI Ops Learn Resource Card for Day 8, alongside the Loom.

> **Three things to do before publishing this card.**
> 1. **There is no Day 8 entry in `Phlo_Mandatory_AI_Course_Curriculum.docx`**, so the
>    "Resources linked from this video" list could not be lifted from it. The links
>    below are named, not pasted - **paste the current URLs in and check each one
>    resolves** before the card goes live.
> 2. **Plan and availability figures date faster on this card than on any other in the
>    course.** Four features here have four different plan rules, and two of
>    them are betas. Re-check the whole "What you can actually get on a Team plan" table
>    against Claude before publishing, and again at each 90-day refresh.
> 3. Everything in "The detail that did not fit on the board" was on the previous
>    module-2 Cowork board and is **product surface**. Same warning applies.

---

## What you are shipping today

**One multi-step task handed to Cowork, with its checkpoints named before it runs.** Not
after. That is the whole assignment.

**Pause-and-try:** write the brief for one task you would actually hand over. Then read
it back and find the sentence doing no work - the one that sounds professional and tells
Claude nothing. Replace it with "when to stop and ask", because that is the one nobody
writes.

## The six things from the video

1. **Chat is a conversation, Cowork is a shift.** In chat you are the checkpoint on every
   turn. In a run, you stop watching at step three - and you should, otherwise you would
   have been quicker doing it yourself. So the supervision has to move somewhere else.
2. **The brief is the only steering you get.** There is no next turn to correct it on.
   A thin brief does not produce a smaller answer, it produces a drifted one, and you
   find out at the end.
3. **Four things a brief must name.** The inputs. The output shape. What a gap means.
   When to stop and ask. Four sentences.
4. **Three checkpoints, against real file handoffs.** Before the first write. At the
   join. Before it leaves the folder. Name them in the brief before the run starts.
5. **You review the join, not each branch.** Cowork splits work into sub-agents running
   in parallel. The branches are the fast part; the join is where the mistakes meet.
6. **Long runs hide their mistakes.** One wrong assumption at step two, and every step
   after it does perfectly correct work on a wrong input. What arrives reads well, adds
   up, and has been wrong since step two. A better model just makes it more convincing.
   The fix is a checkpoint, not a model.

## The safety rule, repeated

**Cowork takes real actions on real files, unattended.** That is a different risk shape
from a chat you are reading.

- **Scope it to one folder for one task.** Never point it at your whole machine, and
  never at a folder you have not looked inside recently.
- **Nothing confidential or patient-identifiable goes in the scoped folder** unless it
  has been approved for that use. Fictional placeholders only in anything you demo or
  share: `Patient_001`, `J. Doe`, `NHS_TEST_123`, `acme.pharmacy@example.com`.
- **Use Manual mode for anything that matters.** Manual pauses and asks. Auto keeps
  going. **Skip checks nothing at all** - do not use it on work you would have to defend.
- **Anything patient-facing keeps the human gate.** Any task touching prescriptions,
  dispensing or patient records: **Claude drafts, a person approves, then the record
  updates.** A long unattended run is exactly the wrong shape for a clinical decision.
  Cowork never writes to a patient record.
- **Read the output before it goes anywhere.** If you cannot verify it, you have not
  checked it - you have chosen not to look.
- **In the built-in browser:** do not sign Claude into anything you would not hand
  someone the keys to. What you sign in to stays available to it in later sessions. And
  a web page can carry instructions written at Claude rather than at you.
- Check the Phlo AI Use Policy before pointing Cowork at anything patient-facing.

---

## The detail that did not fit on the board

Nine beats carried the argument, not the feature surface. This is the rest of it.

### What Cowork actually is

Cowork uses the same agentic architecture that powers Claude Code, inside Claude Desktop
without a terminal. You describe an outcome and come back to finished work - documents,
organised files, synthesised research, spreadsheets with working formulas, decks.

Chat and Cowork share one home: you start both from the same message box and pick Cowork.

### What you can actually get on a Team plan

Phlo is on a Team plan. These four features have four different rules, and this is the
single most useful table on this card.

| Feature | Plans | On a Team plan? |
|---|---|---|
| **Cowork** itself | All paid plans - Pro, Max, Team, Enterprise | **Yes** |
| **Built-in browser** | Pro, Max, Team, Enterprise where enabled | **Yes**, on by default as it rolls out. An Owner controls it at Organization settings → Cowork → Built-in browser |
| **Computer use** (Claude clicking round your screen) | Beta, **Pro and Max only** | **No.** "Team and Enterprise plans don't have access to computer use at this time" |
| **Dispatch** (start it from your phone) | **Limited beta, some Pro and Max plans** | **Probably not yet** |

So: if you cannot find computer use or Dispatch, nothing is broken and there is no
setting to hunt for. They are not on your plan.

### Where you can run it

- **Claude Desktop** (macOS, Windows) - all paid plans. This is where the local-file work
  happens.
- **Web** (claude.ai) - Pro, Max, Team; Enterprise where an admin has enabled it.
- **Mobile** (iOS, Android) - Pro, Max, Team; Enterprise where enabled.
- **Chrome side panel** - Max, Team, rolling out to Pro; Enterprise where enabled.

### The three permission modes, in full

This is the setting behind beat 4's three checkpoints.

| Mode | What it does | Use it for |
|---|---|---|
| **Manual** | Claude pauses and asks for approval for actions | Anything that changes a file, anything that leaves the folder, anything you would have to defend |
| **Auto** | Claude keeps working without stopping to ask about every step, but reviews safety automatically | Read-only work, drafts in a scratch folder, second runs of something you have already checked |
| **Skip** | Claude does not pause, and nothing checks its actions automatically | Effectively nothing at Phlo |

You can also jump in mid-task to course-correct or add direction, and you can delete a
task at any point.

### Two ways to give it context

- **Folder instructions** - pick local folders on the desktop and add context specific to
  them. This is the scoping surface for a one-off task.
- **Projects** - separate workspaces with their own files, context, instructions and
  memory. This is Day 4's feature doing Day 8's job: if you hand the same kind of task
  over every month, the standing half of the brief belongs in a Project and only the
  varying half goes in the message.

Cowork also loads the Connectors, Skills and Plugins enabled for your claude.ai account,
synced at session start. You manage them from **Customize** in the sidebar.

### Sub-agents

Complex work gets divided into smaller tasks with parallel workstreams. Each sub-agent is
self-contained and works with its own context window, then reports back. You do not
configure this and you do not need to - the only thing it changes for you is where you
look. **Review the join.**

### The built-in browser, in more detail

When a task needs a website, a browser opens in the side panel and Claude navigates,
reads, clicks and types. No extension, no setup, and nothing shared from your own browser
unless you choose to.

Safeguards, all on by default: per-site permission prompts before Claude acts on a new
site, a blocklist for high-risk sites, and safety checks on every action.

Two risks worth naming plainly:

- **Prompt injection.** Instructions hidden in a web page can try to redirect Claude. The
  safety checks review Claude's actions against what you actually asked for, but no
  safeguard is perfect.
- **Persistent sign-ins.** Anything you sign in to inside the built-in browser is
  available to Claude in future Cowork sessions. Anthropic's own guidance is to avoid
  using it for sensitive information, and it names financial accounts and medical
  information specifically.

### Dispatch, in more detail

One conversation that syncs across your phone and your desktop - not two chats. You send
an instruction from the mobile app, it runs on your desktop with everything the desktop
has (local files, connectors, plugins, apps), and the result comes back to your phone.
You get a push notification when it finishes **or when it needs approval** - that is a
checkpoint arriving on your phone.

Requirements people miss: **your computer must be awake and the Claude Desktop app open
while Claude works.** It is not running in a cloud on your behalf. And it is a limited
beta on some Pro and Max plans.

The risk chain is worth stating out loud: instructions from your phone can trigger real
actions on your computer. Before enabling it, know what files and accounts it can reach.

### Who this is for

Not developers. Anyone whose work involves moving between files.

- **Ops and support** - the assembly work between the thinking.
- **Analysts and finance** - gather, reconcile, summarise.
- **Anyone with folders** - documents you have to read across rather than read.

No code, no setup, plain English.

### Where Cowork sits against the other features

| Feature | What it changes | Day |
|---|---|---|
| **A good prompt** | one answer | Day 3 |
| **Project** | what Claude knows before you ask | Day 4 |
| **Skill** | how Claude does a recurring procedure | Day 7 |
| **Cowork** | who does the steps, and who is watching | Day 8 |

They stack, and the order matters. **Most of what people bring to Cowork should have
been a Skill first.** If you are handing over a procedure you have described four times,
write the Skill and then hand the Skill to Cowork.

### The brief template, to copy

> Read every file in `<folder>`. Produce `<output shape - one page, a table with these
> columns, in this order>`. If `<a file is missing / two sources disagree>`, `<skip it
> and list it at the end / use this source>` - do not estimate. Stop and ask me before
> `<the first write / sending anything / changing any number>`.

Four sentences. If one of yours is doing no work, it is usually the last one, because it
is the one people leave out.

---

## Links

**Paste the current URL against each before publishing. Do not publish a broken card.**

- Claude help centre - *Get started with Claude Cowork*
- Claude help centre - *Use the built-in browser in Claude Cowork*
- Claude help centre - *Set up browser use in Claude Cowork for Team and Enterprise plans*
- Claude help centre - *Let Claude use your computer in Cowork*
- Claude help centre - *Assign tasks from anywhere in Claude Cowork* (Dispatch)
- Claude docs - *Cowork overview*
- Phlo AI Use Policy (AI Ops)
- Day 4 - Claude Projects (where the standing half of a brief lives)
- Day 7 - Skills (write the procedure before you hand over the shift)

## Refresh

Tool-specific videos refresh every 90 days. At each refresh re-check, in this order:
**the plan table** (four features, four rules, two betas - this is the one that breaks),
the permission-mode names, the built-in browser's default state and Owner toggle path,
and Dispatch's beta status. Those date fastest.

The six things from the video, and the safety rule, do not.
