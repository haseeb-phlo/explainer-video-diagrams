# Claude in Microsoft Excel - narration script

**Board:** `videos/ai-training/15-excel/claude-excel.excalidraw` (built by `build_excel.py`) · **9 beats** · **~7 min 00 board + ~30s live cut-away = ~7 min 30** (hard cap 8:00)
**Format:** one flowing Excalidraw board you pan across left to right, full-screen, framing one beat at a time. The whitespace between slots is the camera. British English, generic examples, no Phlo branding and no patient or clinical specifics.

**Measured:** 1050 words in the narration blocks below (`[BEAT n]` / `[BACK TO BOARD]` prose only), ~150 wpm.
**Re-measure after every edit** - this repo's one recorded process lesson is that per-beat second budgets drift by up to 2x against the written prose, and it has bitten twice already:

```bash
sed -n '/^## Narration/,/^## Demo steps/p' claude-excel-script.md | grep -v '^\[' | grep -v '^\*\*' | wc -w
```

> **Reconcile before recording.** `Phlo_Mandatory_AI_Course_Curriculum.docx` is not in this repo, and the module-2.8 entry that exists describes the *product walkthrough* this video replaces. This script was written from `claude-excel-prompt.md` with the user's explicit go-ahead (2026-09-15) - the same route Days 10, 11, 12, 13 and 14 took.

---

## Narration

Voice: warm, plain, a colleague showing you something that will save you an embarrassment.

### [BEAT 1] 0:00 - 0:55 · orange · *a number nobody checked*

**Hook (0:00 - 0:10)**

"Here is a number: three hundred and seventy-six thousand, six hundred pounds. It is wrong. Nobody in this chain is going to notice."

**Why this matters (0:10 - 0:55)**

"That figure started life in a cell. It got pasted onto a slide. The slide said spend is under control, and on the strength of it somebody renewed a contract. Nothing in that chain asked where it came from.

Every other tool in this course fails where you can see it. A deck that says nothing looks like a deck that says nothing. A rewrite that drops a clause is at least a sentence you can read. A spreadsheet is different. It fails as a plausible number sitting in a cell that nobody queries, and then it travels. So this whole video is really one habit: check one row."

### [BEAT 2] 0:55 - 1:40 · violet · *it edits the live sheet*

"First, the thing that surprises people. When Claude works on a spreadsheet it edits the sheet you have open. Not a copy, not a draft to review later. It warns you before it overwrites something, and asks you to confirm anything risky.

Useful guardrails - and still the reason Anthropic's own guidance says to start on a copy of the workbook.

Because undo is smaller than people think. It reaches the edit you just watched land, and this workbook while it is still open. It does not reach the version you already saved and sent, the figure already pasted into a deck, or the decision somebody made on it. Undo is a safety net for the file. That chain on the last beat is not in the file."

### [BEAT 3] 1:40 - 2:25 · blue · *ask for the formula, not the answer*

"Second habit, and this one costs you nothing. Ask for the formula, not the answer.

Ask what our average monthly spend is and you get a sentence: your average monthly spend is thirty-four thousand, four hundred and eight pounds. You can agree with that or disagree with it. That is the whole menu.

Ask for the formula and the range it covers, and you get equals AVERAGE, B2 to B13. Column B, rows two to thirteen, all twelve months. Now you can read it. Now you can check it.

A formula is inspectable. An answer is not. So ask for both, every time. And remember that range: twelve months of data live in B2 to B13."

### [BEAT 4] 2:25 - 3:05 · teal · *describe the sheet first*

"Third: describe the sheet before you ask it anything. Claude can see your cells. It cannot see what you know about them.

Three sentences will do it. What a row represents. Which range is the actual data. Which columns are worked out rather than typed, so it does not overwrite them.

Type that once at the start and everything after it is better. Better still, set it once in the add-in's own Instructions and it applies to every conversation in Excel, so you stop retyping it. Skip it and Claude will guess. It guesses well, which is exactly the problem."

### [BEAT 5] 3:05 - 3:35 · indigo · *what it is genuinely good at*

"A quick, honest list of what it is genuinely good at. Cleaning a messy export: splitting the columns, fixing the dates, stripping the blank rows. Finding what is broken: tracing a hash-REF back to the cell that actually caused it, across tabs. Looking up across sheets, and asking which rows did not match. And explaining a formula somebody else wrote.

Notice what is not on that list: deciding whether the answer is right."

### [BEAT 6] 3:35 - 4:50 · red · *a formula that looks right* — **the beat the day is built on**

"Right. This is the beat that matters.

Here is a sheet. Twelve months of supplier spend, January to December, down column B. Claude wrote the total. Equals SUM, B2 to B12. It returned three hundred and seventy-six thousand, six hundred pounds.

It ran without an error. It is a valid formula. It is formatted correctly. Nobody flagged it, because there is nothing to flag.

It is also wrong.

Take ten seconds. Look at the blue box, and look at where it stops."

> **HOLD THE SILENCE. Count to ten on camera. Do not talk over it, do not point at the sheet, and do not move the mouse.** The board deliberately flags nothing, so the room can find it unaided. If you narrate through this pause the beat is gone and so is the video.

"The data runs to row thirteen. The formula stops at row twelve. December is sitting right there, thirty-five thousand three hundred pounds, outside the range. The total is short by a whole month, and it is short in a way that looks completely normal. That is what makes this different from every other failure in this programme: there is nothing on screen to catch."

### [BEAT 7] 4:50 - 5:45 · yellow · *check one row by hand*

"So here is the catch, and it is small enough that you will actually do it.

Recompute one row by hand, and check that the row you picked is inside the range. Pick the last one.

December, thirty-five thousand three hundred. Add it back. Three hundred and seventy-six thousand six hundred, plus thirty-five thousand three hundred, is four hundred and eleven thousand nine hundred. The sheet says three hundred and seventy-six thousand six hundred. Caught, in about fifteen seconds.

And it has to be you. Claude wrote the formula, so it cannot also be the thing that checks it.

You are not auditing the whole sheet. You are checking that the row you picked is inside the range, which is exactly why you pick the last one. One row, every time, before it leaves the sheet."

### [BEAT 8] 5:45 - 6:25 · green · *audit, do not just build*

"One more move, and it is the higher-value one. Most people ask Claude to build them a sheet. Point it at a sheet somebody else built instead.

Ask what breaks if this number doubles. Ask what is hard-coded that should be a reference. Ask what assumes this sheet never gets another row. And you do not have to write that from scratch - a ready-made auditing Skill ships with it. Type a forward slash in the sidebar to find it.

Building a new sheet is the obvious ask. Auditing an old one is worth more, because the old one is already making decisions."

### [BEAT 9] 6:25 - 7:10 · orange · *do it live*

"Let me show you the whole thing in about thirty seconds."

**[CUT TO CLAUDE DESKTOP]** — see Demo steps below (~30s)

**[BACK TO BOARD]**

"Two things before you go. A workbook from outside is a file from outside, and it can carry instructions you did not write, so treat one like any other attachment. And never put confidential or personal data into a sheet you are going to share.

Then pause here and try it: open a sheet an AI touched this month, and recompute a single row yourself. That is the whole exercise.

One row, every time, before it leaves the sheet. See you in the next one."

---

## Demo steps

Everything below is invented, generic data. No patient information and no Phlo specifics, at any point.

**Demo - break the range on purpose (~30s)**

1. Open Claude Desktop on a fictional workbook: one column of twelve monthly figures, nothing else. Say out loud that every number here is made up.
2. Ask: `Give me the total spend, and the formula you used, and the range it covers.`
3. Read the range back on camera. This is beat 3, live.
4. Now break it, the same way the board does: **edit the formula yourself so it stops one row short** - change the range to end at the second-to-last row. (Or ask Claude to total "January to November", then treat that as the annual figure.) Do not announce which row you dropped.
5. Recompute the **last** row by hand against the total, out loud. It will not add up, and that is the point: this is the same failure the room spent ten seconds finding on beat 6, caught on camera in about fifteen seconds.

> If it wobbles, describe the problem plainly ("the total has not moved") and keep talking - re-runs are cheap. Invented numbers only.

---

## Ships

One workbook, either built or audited, with **one row verified by hand**.

## Pause-and-try

Open a sheet an AI touched this month and recompute a single row yourself.
