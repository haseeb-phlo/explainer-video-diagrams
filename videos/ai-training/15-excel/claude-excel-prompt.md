# Day 15 - Claude in Microsoft Excel - the commissioning brief

The record of what this video was asked to be, and the decisions taken building it. It is
the source of record, because **there is no curriculum entry** - see *Provenance*.

---

## Slug and file

- **Folder:** `videos/ai-training/15-excel/` - **Day 15**
- **Build:** `build_excel.py` → **`claude-excel.excalidraw`** · 9 beats · ~6 min 56 board + ~30s cut-away

**Three commissions, in order:**

1. **2026-09-15** - rebuild module 2.8 (`videos/claude/8-claude-excel/`) from a product
   walkthrough into an argument. Scope confirmed with the user: Excel only, adapted in place,
   not merged with the Chrome-extension video.
2. **2026-09-16** - move it into the `ai-training` series. It became **Day 15**, leaving a
   sixth gap (at 8) in the `claude/` numbering. Nothing in `videos/claude/` was renumbered.
3. **2026-09-16** - **retarget at advanced users, in Excel and with Claude.** This is the
   commission that produced the current board, and it was a rewrite rather than an edit.

---

## Why the retarget was a rewrite

The general-audience version taught *ask for the formula*, *describe the sheet*, and
*check one row by hand*. Those are correct habits and this audience already has them.
Teaching them to a modeller is worse than useless: it signals the video has nothing for
them, and they stop watching before the beat that does.

| general-audience version | advanced version |
|---|---|
| ask for the formula, not the answer | **ask for the assumption the formula encodes** - an advanced user reads formulas fluently, and that fluency is exactly what hides this failure |
| describe the sheet first | **state the model's contract** - what is authoritative, what is derived, what must never be overwritten |
| check one row by hand | **reconcile** - a spot-check scales linearly and a model does not, and against a method error it fails completely |
| *(none)* | **the session drifts** - non-determinism and auto-compaction |
| audit, do not just build | **hunt the hardcodes** - the exhaustive sweep, framed as evidence you can check |

## The adversarial beat had to get harder, and that is the whole rewrite

The old beat 6 was a `SUM` range stopping one row short. Any competent Excel user spots that
in two seconds, so with this audience the ten-second silence dies on camera and the day dies
with it.

The new failure is an **average of averages**:

> Claude is asked for the average cost per unit and writes `=AVERAGE(D2:D13)` - the
> unweighted mean of twelve monthly rates. The range is correct. The formula is valid.
> **Every cell in column D is arithmetically right.** Spot-check any row and it checks out
> (Jul: 40,800 / 3,400 = 12.00 exactly). The answer is still wrong: the right figure is total
> spend over total units, a weighted mean. **£18.33 against £16.31 - a 12.4% overstatement**,
> on a number you would price off.

**Why this one and not another subtle bug: it is the only shape that defeats the old catch.**
"Check one row" finds nothing here, because every row is right. That forces beat 7 to teach
reconciliation, which is the real advanced discipline, and it makes beats 6 and 7 one
argument rather than a failure followed by a tip.

**Nothing on beat 6's sheet is wrong, and that is the point.** The old board drew a marquee
that visibly stopped short; this one draws a marquee over the whole of `D2:D13`, correctly,
so there is genuinely nothing to find by looking. **Do not "improve" this beat by introducing
a visible flaw** - the absence of one is the lesson. Red appears on the heading, the "take ten
seconds" prompt and the catch strip, and nowhere on the sheet.

---

## The board

| # | Accent | Heading | Carries |
|---|---|---|---|
| 1 | orange | the error that survives a spot-check | cell → price → margin, and the level-setting |
| 2 | violet | give it the contract | inputs / authoritative / never overwrite / conventions; live-edit and undo |
| 3 | blue | ask for the assumption | two replies; the assumption sentence is the error |
| 4 | teal | where it actually beats you | four jobs where thoroughness beats judgement |
| 5 | indigo | the session drifts | non-determinism + auto-compaction |
| 6 | **red** | every row is right, and the answer is wrong | **adversarial hero, 1600 wide** |
| 7 | yellow | reconcile, do not spot-check | the catch: tie out, cross-foot, rebuild a second way |
| 8 | green | hunt the hardcodes | the exhaustive sweep, as a checkable list |
| 9 | orange | do it live | demo badge, pause-and-try, the red rule, the close |

**Pan order:** left to right, 1 to 9, one slot at a time. In the build script's docstring.

**Ships:** one model, reconciled a second way, with the tie-out written down.
**Pause-and-try:** take a model you own and reconcile its headline number a second way.

---

## Decisions that are load-bearing

**One worked example runs the board.** A twelve-month supplier spend sheet where quiet months
carry a high unit cost and busy months a low one - which is what makes the unweighted mean
wrong. Pinned in `MONTHS` / `UNITS` / `CPU` / `SPEND` with asserts, including one that every
SPEND is whole pounds **so that every row spot-checks cleanly**. That assert is not cosmetic:
it is what makes beat 6 work. Change the example and beats 1, 2, 3, 6, 7 and 9 all move.

**Two colours are held constant and are not beat accents.** Blue = a formula and the range it
covers (beats 3 and 6); beat 6's marquee is blue on a red beat because a blue range border is
what a spreadsheet selection looks like, so it reads as neutral UI rather than a flag. Green =
the human pass, held from Days 10, 11, 13 and 14 - beat 7's gate is green although the beat is
yellow.

**The red data caution sits on beat 9**, the same call Days 7, 10, 12 and 14 each made, and it
now carries a second half that is specific to this video: Claude for Excel activity is not in
Enterprise audit logs and does not inherit retention settings, **so the reconciliation is the
only audit trail that exists.** That turns a governance footnote into a reason to write the
tie-out down.

**Beat 6 is the one wide slot** (1600, not 1200), widened rather than made taller - on a 16:10
laptop height binds framing. Day 14's beat 10 records the identical decision.

**Runtime discipline.** The first advanced draft measured **8:40 against a 7:00 budget** - the
third recorded instance of this repo's drift lesson, after Day 10 and Day 14, and on a script
whose own header warns about it. Trimmed twice to 1,042 words, ~6:56 + ~30s = **~7:26**.
Measure it, every time; the command is in the script header.

---

## Verification

**Verified against Anthropic's live documentation on 2026-09-16**, primarily
[Use Claude for Excel](https://claude.com/docs/office-agents/excel). Full read, and the table
of what the check corrected, on `claude-excel-resource-card.md`.

What the docs back directly: beat 2's live-edit and do-not-overwrite framing (documented
overwrite protection and risky-operation confirmations, plus the best practice *"Start with a
trusted copy of the workbook before asking Claude to edit widely"*); beat 2's persistent
per-app Instructions; beat 5's compaction half; beat 8's sweep and the preloaded auditing
Skill; beat 9's governance rule. And **beats 6 and 7 wholesale** - the docs' own limitations
list says Claude for Excel is not recommended for *"Audit-critical calculations without
verification"*.

**One board claim is not doc-backed and the card says so:** beat 5's non-determinism half is a
property of the model, not a documented Excel behaviour.

The board names **no plan and no tier**, so it does not date. Fix the card, not the board.

---

## Provenance, and one open question

**No curriculum entry.** `Phlo_Mandatory_AI_Course_Curriculum.docx` is the stated source of
truth for script blocks and is not in this repo. The user was asked and confirmed there is
none to hand; the module-2.8 entry that exists describes the product walkthrough this
replaces. Board and narration were written from this brief with the user's explicit go-ahead.
**Reconcile before recording.**

**Open question for whoever owns the curriculum:** this board is pitched at advanced users and
the rest of the AI Ops Learn series is not. It assumes fluency in both Excel and Claude, uses
modelling vocabulary without glossing it, and its central beat only works on a room that will
try to find the bug and fail. **That makes it a poor fit for the mandatory all-staff course.**
It needs either a general-audience sibling or an explicit *advanced / optional* label on the
Loom. Do not resolve this by softening the board - a version pitched at everyone would lose
the only thing this one has.
