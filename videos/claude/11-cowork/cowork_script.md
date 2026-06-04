# Video 2.11 - Claude Cowork: hand over the whole task, not one question
### Production pack: Excalidraw board + narration script + demo steps

**Format:** one flowing Excalidraw board (`claude-cowork.excalidraw`) you pan across left-to-right and talk over, cutting to the live Claude desktop app between beats · ~4:30 Loom · British English · invented, generic examples (no Phlo branding, no patient or clinical data) · current to today.

**How to use this pack**
- Open `claude-cowork.excalidraw` full-screen and frame **one beat at a time** - the whitespace gaps are the camera moves. Pan left-to-right, ~3s of narration per beat.
- `[BEAT n]` maps **1:1** to board beat *n*. `[CUT TO CLAUDE DESKTOP]` / `[BACK TO BOARD]` mark the cut-away inside the beat it belongs to.

> Cowork is **agentic** - it works across your files and apps and returns a finished deliverable. As with the Chrome video, the oversight beat (5) and the safety beat (8) carry real weight. Don't rush them.

---

## Section 2 - Narration script (~4:30)

Voice: warm, plain, a colleague showing you something useful - honest about scope.

**[BEAT 1] 0:00 - 0:18 (Hook)**
"Most of what we've shown is Claude answering one question at a time. Cowork is different: you hand over a *whole task* - 'pull these five reports into one summary' - and Claude takes it away, does the steps, and brings back a finished thing. It's a worker, not a chatbot. Four and a half minutes."

**[BEAT 2] 0:18 - 0:44 (It works on your computer)**
"And it works where the work actually lives - on your computer. Cowork runs in the Claude desktop app and moves between your files, your folders and the apps you already use, the way you would. It's on all the paid plans. So this isn't a sandbox you upload things to; it's Claude working in your real environment, with your permission."

**[BEAT 3] 0:44 - 1:10 (Goal in, deliverable out)**
"The shape of it is simple: goal in, deliverable out. You set the goal once. Claude plans the steps, works across the files and apps to do them, and hands back the result - you're not driving each click. It's multi-step work, synthesised across several sources, so you spend your time on the judgement, not the assembly."

**[BEAT 4] 1:10 - 1:35 (It uses your real material)**
"What does it pull from? Your real material - a folder of reports, loose files scattered about, the apps you work in - and it reads across all of them to pull one answer together. Anthropic's own phrase for it is 'let Claude use your computer'. That's the unlock, and it's also exactly why the next bit matters."

**[BEAT 5] 1:35 - 2:05 (You stay in charge)**
"Cowork is built around human oversight. It completes the task - but it checks in on the big calls rather than just barrelling on. You review the deliverable before it counts. And you can steer it or stop it at any point. The principle is simple: Claude does the work, the consequential decisions stay with you. That's not a limitation bolted on; it's how it's designed."

**[BEAT 6] 2:05 - 2:32 (Whole tasks you'd hand over) → [CUT TO CLAUDE DESKTOP]**
"So what would you actually hand it? Whole tasks, in plain English. 'Pull these five reports into one summary.' 'Tidy this folder and rename the files by date.' 'Draft the monthly update from these notes.' 'Reconcile these two lists and flag the gaps.' Let me show one."

**[CUT TO CLAUDE DESKTOP] 2:32 - 3:10 (Demo - see Section 3)**
In the desktop app, point Cowork at a scoped folder of invented notes and ask for one summary. Show it working across the files and returning a deliverable.

**[BACK TO BOARD] [BEAT 7] 3:10 - 3:30 (Who it's really for)**
"And who's it for? Honestly, not developers - anyone with files. Ops and support, for the assembly work between the thinking. Analysts and finance, gathering, reconciling, summarising. Anyone who lives in documents and folders. No code, no setup - you ask in plain English."

**[BEAT 8] 3:30 - 4:00 (Scope it tight, then sign it off)**
"Now the important bit for us - scope it tight, then sign it off. Scope it: Cowork can reach your files and apps, so point it at a *specific folder* for the task, not your whole machine. Keep it clean: confidential or patient data stays out unless that's been approved. And sign it off: Claude does the assembly, you make the call - so read the deliverable before it goes anywhere, and watch the consequential steps. Scoped access, human sign-off - same as any capable new colleague."

**[BEAT 9] 4:00 - 4:18 (Hand over one whole task)**
"So try it: hand it one whole task you'd normally dread assembling - merge a few documents, tidy a messy folder, draft a recurring update. Point it at one folder, watch it work, then check the result. Cowork does the legwork - you keep the judgement calls. Docs below, including how to scope what it can touch. See you in the next one."

---

## Section 3 - On-screen demo steps

Everything below is invented, generic data in a **dedicated demo folder**. No patient information, no Phlo systems, no real confidential files, at any point.

### Demo - a folder of notes into one summary (~35s)

1. Beforehand: create a throwaway folder (e.g. `~/cowork-demo`) with 3-4 short invented text files - fictional "weekly notes" from different teams.
2. In the **Claude desktop app**, open **Cowork** and grant access to **just that folder** (narrate: "scoped to one folder, nothing else").
3. Ask: `Read the notes in this folder and write me one combined weekly summary - themes, decisions, and open questions.`
4. Show it working across the files, then producing the summary deliverable. Point out any **check-in / approval** moment if one appears.
5. **Review** the result on camera: "I read it before it goes anywhere." Switch back to the board.

> Keep it to the scoped demo folder with invented content - the scoping *is* the safety message. Never grant whole-disk or sensitive-app access on camera.

---

## Section 4 - Design rationale

- **House Style B**, built by `build_cowork.py` (imports the shared `excalidraw_kit`); re-run to regenerate.
- **Agentic shape, like the Chrome video**: power first (beats 1-4: whole task, on your computer, goal-to-deliverable, your real files), then control (beat 5 oversight, beat 8 scoped-access safety). No "build one file" beat - the deliverable *is* the point, whatever its format.
- **Verified behaviour**: multi-step knowledge work across local files/folders/apps, returns a finished deliverable, runs in the Claude desktop app on all paid plans, human keeps consequential decisions - all from the current Claude/Anthropic docs.
- **Safety is load-bearing**: "scope it to one folder, keep patient/confidential data out unless approved, read the deliverable" maps directly onto Phlo's regulated-pharmacy guardrails (human owns the final; AI never writes to records unsupervised). The demo is deliberately confined to a throwaway folder.

## Resources to link under the video
- Claude - *Get started with Claude Cowork*: https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
- Claude - *Let Claude use your computer in Cowork*: https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork
- Anthropic - *Claude Cowork* (product overview): https://www.anthropic.com/product/claude-cowork
