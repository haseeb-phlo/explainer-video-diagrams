# Day 15 - Claude in Microsoft Excel - the commissioning brief

This file carries the brief this board and script were built from, verbatim, plus the
decisions taken while building. It is the source of record for the video, because
**there is no curriculum entry** - see *Provenance* at the bottom.

---

## Slug and file

- **Folder:** `videos/ai-training/15-excel/` - **Day 15.** Rebuilt in place at
  `videos/claude/8-claude-excel/` (module 2.8) on 2026-09-15, then **moved here as Day 15 on
  2026-09-16 at the user's request**, leaving a sixth gap (at 8) in the `claude/` numbering.
  Nothing in `videos/claude/` was renumbered.
- **Build:** `build_excel.py` → **`claude-excel.excalidraw`**
- **Action:** ADAPT and widen. The highest-risk board in the block and the one that earns the most beats.

**Scope was confirmed with the user before authoring (2026-09-15).** The commissioning
message opened "Create one visual set for both Claude in Excel extension", and the beat
table immediately above the Excel brief was **Day 12's PowerPoint board verbatim**
(beats 2-7; the missing beat 1 is orange *it looks finished and says nothing*), which
`videos/ai-training/12-powerpoint/` already ships. The user confirmed: **Excel only,
adapted in place** - not merged with the Chrome extension video, and not moved to
`ai-training/` as a new Day. The brief named no Day number, and every previous move out
of `videos/claude/` was separately commissioned.

---

## Why this day exists

> Every other surface in the programme fails visibly. A spreadsheet fails as a plausible
> number sitting in a cell that nobody queries, and it then flows into a decision. **This is
> the board where the adversarial beat is the point of the day rather than a beat in it.**

## Beats and runtime

**9 beats, roughly 6 to 7 minutes.** Delivered at ~6 min 42 board + ~30s cut-away.

| # | Accent | Heading on the board | What is drawn |
|---|---|---|---|
| 1 | orange | a number nobody checked | A figure moving from a cell into a slide into a decision, drawn as a short chain. Caption: "nothing in this chain asks where it came from". |
| 2 | violet | it edits the live sheet | Changes landing as highlighted cells in the real workbook, not in a copy. Where undo sits and what undo will not reach. Chip: "work on a duplicate the first few times". |
| 3 | blue | ask for the formula, not the answer | Two responses side by side: a number you must trust, against a formula you can read. Chip: "a formula is inspectable, an answer is not". |
| 4 | teal | describe the sheet first | What it needs before it can help: what a row represents, which range is the data, which columns are derived. Drawn as three short labels pinned to a sheet doodle. |
| 5 | indigo | what it is genuinely good at | The honest list: cleaning messy exports, reshaping, lookups across sheets, explaining a formula someone else wrote. Drawn as four small doodles, no hype. |
| 6 | red | a formula that looks right | Adversarial hero beat, and the sharpest in the programme. A range off by one row, a total that is plausible, nothing flagged anywhere. Draw the wrong range visibly so the audience can find it themselves. |
| 7 | yellow | check one row by hand | The discipline that catches beat 6. One row recomputed manually against the formula's output. Chip: "one row, every time, before it leaves the sheet". |
| 8 | green | audit, do not just build | The advanced move. Point it at a model someone else built and ask what breaks, what is hard-coded and what assumes the sheet never grows. Higher value than asking it to build a new one. |
| 9 | orange | do it live | Demo badge: "show in Claude desktop app: ask for the formula, then break the range on purpose and see whether the check catches it". |

**Pan order:** left to right, beats 1 to 9, one slot at a time. Documented in the build script docstring.

**Ships:** one workbook either built or audited, with one row verified by hand.

**Pause-and-try:** open a sheet an AI touched this month and recompute a single row yourself.

> **Watch out:** Do not soften beat 6 into a general caution. It only works if the wrong
> range is drawn on the board and the room is given a moment to spot it. The whole day is
> built on that moment.

---

## Shared constraints applied

Build: thin `build*.py` doing `from excalidraw_kit import *`, scene + scaffold
(`OX` / `WID` / `ACCENT` / `beat_head`), `finish(out, max_w, total_w)`. Never hand-place
elements, never edit the kit. Copied `videos/claude/3-artefacts/build_excalidraw.py` as the
scene template. `random.seed(80810)` (carried from the previous build). Pan order in the
module docstring.

Style B: no frame elements, no boxes, no connector spine, no inter-beat arrows, no
colour-band washes, white background, whitespace as the camera. Uniform ~1120x980 slots,
`GAP = 800`. All text `fontFamily 1` / `HAND`, roughness 1, lineHeight 1.4. Headings via
`heading()`. Body and explanation text ink or grey; accents for headings, labels, shapes
and fills. Light jitter on notes and chips. Hand-drawn icons, no emoji. Accents never
repeat on adjacent beats (1 and 9 are both orange and are seven slots apart).

Content: generic examples, fictional identifiers, British English, hyphens not em dashes,
no Oxford commas, product proper nouns exact. Demo marked with `demo_badge()` and
`[CUT TO CLAUDE DESKTOP]` / `[BACK TO BOARD]` in the script.

**One beat is adversarial and always red.** Here that is beat 6, and on this board it is
the hero rather than a checkpoint.

---

## Decisions taken while building

**The one worked example.** A generic twelve-month supplier spend sheet, pinned in
`MONTHS` / `SPEND` / `WRONG_FORMULA` / `WRONG_TOTAL` / `TRUE_TOTAL` at the top of the
build, with `assert`s so it cannot drift out of arithmetic. £376,600 (Jan-Nov) is the
number travelling through beat 1's chain, the number the broken range produces on beat 6
and the number the hand-check contradicts on beat 7; the true total is £411,900 and the
missing row is December at £35,300. **Every value in `SPEND` is distinct on purpose** -
two equal figures either side of the marquee's bottom edge would make it ambiguous which
row the range stops at, which is the one thing beat 6 cannot afford.
**Change the example and beats 1, 2, 3, 4, 6, 7 and 9
all move together.**

**Beat 3 plants the range that beat 6 breaks.** Beat 3's good reply is
`=AVERAGE(B2:B13)` and it closes on "Twelve months of data live in B2:B13. Worth
remembering." Beat 6 then shows `=SUM(B2:B12)`. A viewer who was listening on beat 3 can
find the error unaided, which is the experience the brief asks for. **Beat 3 uses AVERAGE,
not SUM, on purpose** - a SUM there would reveal the annual total and hand the reveal to
beat 3, leaving beat 6 with nothing to find. Keep them different functions.

**Beat 7's discipline was made honest.** "Recompute one row by hand" catches a wrong
*per-row* formula, but not by itself a wrong aggregate *range*, which is what beat 6
breaks. So the board states the pair that actually works: recompute one row by hand **and
check that the row you picked is inside the range - pick the last one.** That is still one
row, still by hand, and it genuinely catches beat 6. Weakening it back to "spot-check a
row" breaks the beat 6 / beat 7 join.

**Nothing on beat 6's sheet is flagged, and the build enforces it.** The sheet's header
tint is neutral `FAINT`, not `RED_BG`; the selection marquee is **blue, border-only** (a
fill would dim the cell values, and red would flag the error). Red appears on beat 6's
heading, on "Take ten seconds. Where is it wrong?" and on the catch strip, and nowhere on
the sheet. The script carries an explicit **HOLD THE SILENCE** direction for the recording.

**Beat 6 is the one wide slot** - 1600, not 1200. It carries the twelve-row sheet at a
readable size, the formula, the total and the catch. It was widened rather than made
taller: on a 16:10 laptop height binds framing, so 1600x980 frames better than 1200x1230.
Day 14's beat 10 records the identical decision.

**Two colours are held constant and are not beat accents.** **Blue = a formula and the
range it covers** (beat 3's reply, beat 6's marquee and formula). **Green = the human
pass**, held from Day 10, Day 11, Day 13 and Day 14 - beat 7's gate is green although the
beat's accent is yellow. Beat 8's accent is green by the brief; that is an accent, not the
human-pass marker. Beat 7's gate uses a bespoke `human_gate()` rather than the kit's
`person()`, which is sized for a crowd and reads as a paper dart standing alone.

**The red data caution sits on beat 9, not on the Resource Card.** The nine-beat brief has
no slot for it, but it is the only on-screen data-handling rule in a mandatory course for a
regulated pharmacy - the same call Day 7 (beat 3), Day 10 (beat 7), Day 12 (beat 7) and
Day 14 (beat 11) each made. The untrusted-workbook half rides with it because beat 4 is the
beat that tells people to feed outside sheets in.

**The board names the tool, never the tier.** "Excel" appears in the board title and the
demo badge and nowhere else. Everything displaced is on
`claude-excel-resource-card.md` - **fix the card, not the board.**

---

## What came off the old board

The previous nine beats were a product walkthrough: it works inside your spreadsheet · a
real .xlsx · start from the mess you inherited · it keeps the formulas alive · two front
doors (chat vs the Home-ribbon add-in) · it finds what's broken · the jobs it's best at ·
trust the model check the numbers · try it. Its most interesting facts were a plan tier and
a keyboard shortcut. Everything displaced - the two capabilities kept distinct, plan tiers,
the ribbon location and shortcut, dependent recompute, `#REF!` tracing and the doc links -
is on the Resource Card. **That card is a deliverable, not an afterthought; do not
re-inflate the board with it.**

The old `excel_script.md` was **replaced**, not left beside the new board: its thesis
("a spreadsheet helper that keeps your formulas alive") is the argument this rebuild
retired, and leaving it in place would have left a script the board contradicts.

---

## Provenance

**No curriculum entry.** `Phlo_Mandatory_AI_Course_Curriculum.docx` is the stated source of
truth for script blocks and is **not in this repo**. The user was asked for the relevant
entry before narration was authored, per the brief, and confirmed there is none to hand -
the module-2.8 entry that exists describes the product walkthrough this video replaces.
Board and narration were therefore written from this brief with the user's explicit
go-ahead (2026-09-15), the same route Days 10, 11, 12, 13 and 14 took.
**RECONCILE BEFORE RECORDING.**

**The board was verified against Anthropic's live documentation on 2026-09-16**, at the
user's request, primarily against [Use Claude for Excel](https://claude.com/docs/office-agents/excel).
The full read is on `claude-excel-resource-card.md`, including a table of what the check
changed. Four board edits came out of it (beats 2, 4, 5 and 8) and they are recorded in the
build script's docstring. The board still names no plan and no tier, so it does not date.

Two documented findings **validate the day rather than change it**: Anthropic's own
limitations list says Claude for Excel is not recommended for *"Audit-critical calculations
without verification"*, and its best practices say *"Start with a trusted copy of the
workbook before asking Claude to edit widely"* and *"Verify that outputs match your
organization's standards and your own judgment"*. Beats 2, 6 and 7 were written before that
page was read and land on the same three points.
