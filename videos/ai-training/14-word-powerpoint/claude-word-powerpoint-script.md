# Day 14: Claude in Microsoft Word and PowerPoint - narration script (Loom)

Board: `videos/ai-training/14-word-powerpoint/claude-word-powerpoint.excalidraw` (11 beats,
one slot each, `GAP = 800`; beat 10 is the one wide slot at 1600). **Day 14** of the AI
training series.

> **Source note - read before recording.** `Phlo_Mandatory_AI_Course_Curriculum.docx` is
> the stated source of truth for script blocks and is **not in this repo**. There is **no
> Day 14 entry** - the module-2.9 entry describes the Word *product walkthrough* and the
> module-2.7 entry the PowerPoint one, and this video is neither. This narration was
> written from the brief in `claude-word-powerpoint-prompt.md`, with the user's explicit
> go-ahead, which is the same route Days 10, 11, 12 and 13 took. **Reconcile it against
> the curriculum when a Day 14 entry exists** - particularly the hook, the pause-and-try
> and the resource list.

> **What this is.** The Word video and the PowerPoint video, merged into one board and one
> Loom. **Nothing was retired to make room:** Day 12 (`12-powerpoint/`) and the older
> module-2.9 Word walkthrough (`videos/claude/9-claude-word/`) both stay exactly where
> they are. This is a new Day, not a move.

> **Runtime, measured not asserted.** 1,053 spoken words = **7:01 at 150 wpm**, plus
> the ~30 seconds across the two cut-aways where the doing takes longer than the saying:
> **~7:31**. Hard cap 8 minutes - this sits inside it with 29 seconds of headroom.
> Per-section word counts are in `claude-word-powerpoint-prompt.md`; **re-measure if you
> rewrite** - the command is there, and this repo's one recorded process lesson is that
> per-beat second budgets drift badly against written prose.

Cues:
- `[CAM]` - talking to camera, board not shared
- `[BOARD: beat N]` - share the Excalidraw board and pan to beat N
- `[CUT TO CLAUDE DESKTOP]` / `[BACK TO BOARD]` - the live cut-aways, marked on the board
  with orange demo badges on beats 6 and 11

Beat numbers match the build script's slot numbers and the sections below run in board
order, so you only ever pan **left to right**. Hold roughly 3 seconds of whitespace
between beats - the gap is the transition. **Beat 10 is wider than the rest**, so you will
zoom out one notch for it and back in for beat 11.

**If you need a shorter cut:** beats 8 and 9 are the droppable pair - nothing later depends
on either, and the argument still lands. That removes 44 measured seconds and takes the
video to **~6:48**.
**Beat 10 is the one to protect** - it is the reason these two videos are one video, it is
the longest section on purpose, and everything else was trimmed to pay for it.

**Loom chapters:** Hook (0:00) · Why this matters (0:09) · The document
(0:37) · The deck (3:02) · The catch (5:03) · Live (6:18) · Close
(7:05).

---

## 0:00 - 0:09 · Hook [CAM]

Nobody has ever sent back a document because the prose was too good. That is exactly the
problem we are here about.

## 0:09 - 0:37 · Why this one matters [CAM]

Word and PowerPoint are where most of us do the work other people read. Claude is excellent
in both, and it is best at the surface: fluent sentences, tidy slides.

Which is the problem, because the surface is what a reviewer checks. The substance - the
condition in the clause, the claim in the headline - is what it skips unless you ask. Both
apps in one video, because it is one habit.

## 0:37 - 1:15 · The document already exists [BOARD: beat 1]

Start with what makes this different from everything else you ask Claude for.

A draft starts from a blank page. Nothing to preserve, so nothing to lose. The thing open
on your screen is not a blank page. Somebody else's wording. A tracked change from last
week. A defined term you cannot quietly drop, because three other clauses point at it.

So you are not asking for a draft. **You are asking for a change.** That is the whole
video, and it covers the deck half too: a deck can look finished and say nothing.

## 1:15 - 1:39 · It lives in the sidebar [BOARD: beat 2]

Quickly, the mechanics. Most people do the copy-paste shuttle, rebuilding the context every
single time. Claude sits in a panel beside the file instead - same panel in Word, same
panel in PowerPoint. The file is the context, so you stop pasting it.

If you cannot see it, an owner has to switch it on. That is on the Resource Card.

## 1:39 - 2:14 · Review as a diff [BOARD: beat 3]

Here is the habit that makes this safe. Changes come back as tracked edits and you read
them one at a time.

"Shall be entitled to" becomes "may" - accept. "In the event that" becomes "if" - accept.
"Within five working days" becomes "promptly". Reject that one. "Promptly" is not a date,
it is a hope.

**Never accept a full rewrite.** One at a time is not slower. It is the only version of
this job where you can say what changed and why.

## 2:14 - 2:39 · Revise, do not rewrite [BOARD: beat 4]

Which means scoping the ask.

"Make this better" gets you a new document. Claude's voice, the thing you had gone, nothing
to compare it against.

"Tighten the second paragraph, keep the defined terms" gets you a change you can check. One
paragraph moved, the rest untouched, all of it in front of you as a diff. Name what has to
survive and it survives.

## 2:39 - 3:02 · It can read the whole thing [BOARD: beat 5]

A forty-page contract goes in whole. But its attention is not even across it - strong at
the ends, thinner through the middle.

So change what you ask for. "Summarise this contract" is exactly where the middle goes
missing. **"Quote the exact wording on notice periods, and tell me which page"** gives you
something you can check yourself.

## 3:02 - 3:53 · Structure first, slides second [BOARD: beat 6]

Now the deck. Same trap, one storey up.

Six slides. Titles, bullets, a chart on each. Nothing wrong with any of it, which is why it
sails through - and the slide saying why it matters was never asked for, so it is not
there.

So settle the argument in the chat first. Ask for an outline, not slides. Five lines, four
minutes, and the case is made before a slide exists.

`[CUT TO CLAUDE DESKTOP]` - agree the outline in chat, first. Steps are in the demo section
below. ~15 seconds of doing.

`[BACK TO BOARD]`

**If the outline is wrong, every minute of design after it is wasted.**

## 3:53 - 4:18 · One idea per slide, one line that carries it [BOARD: beat 7]

Then the bit that does most of the work.

"Q3 results" is a topic. It commits to nothing and there is no way to disagree with it.
"Margin fell because unit cost rose" - same slide, same chart - is a claim somebody can
push back on.

Do that to every headline. **If the headline could be a chapter title, it is not doing any
work.**

## 4:18 - 4:39 · Build it from a source [BOARD: beat 8]

And build it from a source, not a sentence.

Give it the supplier report and last quarter's costs, and the outline comes back grounded
in those two files, line by line. Ask for "a deck about supplier costs" and you get the
thing on the right: plausible, generic, and not about your numbers.

## 4:39 - 5:03 · Design is not its strength [BOARD: beat 9]

An honest one. It is good at the order of an argument and a first draft in minutes.

What stays with you is which template to use and what the brand actually is. It will follow
a template you hand it. It will not decide what your brand is. **Structure, not design** -
the brand pass is a person.

## 5:03 - 6:18 · Plausible passes review [BOARD: beat 10]

Here is the failure you will not catch, and it is the same failure in both apps.

On the left, the paragraph you asked it to tighten. Shorter, cleaner, better English than
the original - and the condition has gone. Written notice, at least thirty days before the
Renewal Date. That is not a style change, that is a different contract.

On the right, three decks. All well made, all different, all interchangeable. Read only the
headlines, in order: Q3 results, Background, Our options, Next steps. Four topics. That is
a table of contents, and not one line argues for re-tendering anything.

Both pass a review, because a reviewer checks whether it reads well and whether it looks
finished. Both do.

So here is the catch, and it goes *before* you look. **Name the test first.**

On a document, list what has to survive - the conditions, the dates, the defined terms -
then read the diff against that list. On a deck, write one sentence naming the decision you
want, then read only the headlines and ask whether they argue for it.

Name it first, and "it reads well" cannot be the verdict.

## 6:18 - 7:05 · Do it live, on real work [BOARD: beat 11]

So: one document, reviewed change by change - two accepted, one rejected, every one read as
a diff first.

`[CUT TO CLAUDE DESKTOP]` - three tracked changes, one rejected. Steps below. ~15 seconds
of doing.

`[BACK TO BOARD]`

And one deck, built from an outline you agreed first, every headline stating a position.

One rule before either leaves your hands. Nothing confidential goes into a document or a
deck you are sending out, and do not open a file, or build on a template, you do not trust
- a file from outside can carry instructions of its own.

## 7:05 - 7:32 · Pause and try, and close [CAM]

Pause here and do one of two things. Take a paragraph you wrote this week and ask for a
change rather than a rewrite. Or take your last deck and rewrite three slide titles so each
states a claim.

Accept nothing you have not read as a diff. The argument is the deliverable. And if you
keep one thing from today: name the test before you look.

---

## On-screen demo steps

Everything below is invented, generic data. No patient information, no Phlo specifics, at
any point. The board marks these cut-aways with orange demo badges on **beats 6 and 11**.

### Demo 1 - agree the outline in chat, first (~15s on camera, beat 6)

1. In a new chat in **Claude Desktop**, paste a short block of plain notes - invent them on
   the spot, e.g. a fictional packaging-supplier review: unit cost up 9%, two of three
   suppliers missed SLA twice, a re-tender takes eleven weeks. Then type:
   > Before any slides: propose a five-line outline for a deck arguing that we should
   > re-tender the packaging contract. One claim per line, no topics.
2. Read the outline back on camera. Push on one line so they see it is negotiable:
   > Line 3 is a topic, not a claim. Rewrite it as a position.

### Demo 2 - three tracked changes, one rejected (~15s on camera, beat 11)

1. Open a fictional wordy document - a one-page supplier agreement or remote-working
   guidelines draft will do. Open the **Claude** panel and turn on suggested edits.
2. Select one bloated paragraph and type:
   > Tighten this paragraph, keep the defined terms, and do not touch the heading.
3. Show the changes arriving as tracked revisions. **Accept two. Reject one**, out loud,
   and say why you rejected it. That rejection is the teaching point of the whole video -
   do not skip it to save time, and never bulk-accept on camera.

> Tip if a demo wobbles: say the problem out loud in plain English and ask again. Re-runs
> are cheap - keep talking.

## Recording notes

- Open the `.excalidraw` full-screen and frame **one beat at a time**; the whitespace
  between slots is the camera move. Pan strictly left to right.
- **Beat 10 is the wide one.** Zoom out a notch to frame all three columns, hold it, then
  zoom back in for beat 11. Do not rush the gap between the two failures and the catch -
  the pause is what makes it land.
- Beat 6 is the pivot from the document half to the deck half. Say "same trap, one storey
  up" and let the colour change do the rest.
- The red band on beat 11 is the only on-screen data rule in this video. Say it, do not
  skim it.
