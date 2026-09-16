# Day 15 - Claude in Microsoft Excel - narration script

**Board:** `videos/ai-training/15-excel/claude-excel.excalidraw` (built by `build_excel.py`) · **9 beats**
**Audience: advanced.** People fluent in Excel *and* fluent with Claude. Deliberately not general-audience material - see the note at the end.

**Measured: 1042 words = ~6 min 56 board + ~30s cut-away** (hard cap 8:00).

Re-measure after every edit. This repo's recorded process lesson is that per-beat second budgets drift by up to 2x against written prose, and it has bitten on Day 10, on Day 14, and again on the first draft of this script, which came in at 8:40 against a 7:00 budget:

```bash
awk '/^## Narrat/,/^## Demo/' claude-excel-script.md | grep -vE '^(#|>|\*\*|\[|-)' | wc -w
```

> **Reconcile before recording.** No curriculum entry exists for this video. Written from `claude-excel-prompt.md` with the user's explicit go-ahead. Product facts verified against Anthropic's live docs on 2026-09-16 - see `claude-excel-resource-card.md`.

---

## Narration

> **Voice:** peer to peer. You are not teaching them Excel and you are not teaching them Claude. You are handing them one failure mode they have probably already shipped, and the discipline that catches it. No hedging, no "always double-check".

### [BEAT 1] 0:00 - 0:50 · orange · *the error that survives a spot-check*

**Hook (0:00 - 0:12)**

"Eighteen pounds thirty-three. That is a cost per unit, it came out of a model, and it is wrong by twelve per cent. Every single cell behind it is correct."

**Why this matters (0:12 - 0:50)**

"It became a price, then a margin, then a signature. Nothing in that chain asked how it was computed, because there was nothing visibly wrong to ask about.

You are not the audience for 'always double-check your AI'. You already do. The failure that costs you is the one where every input is right, every formula is valid, every range is correct - and the answer is still wrong, because the method was wrong. Claude produces it fluently, in a form that passes review, because review looks at cells.

Nine beats. The middle one is the point."

### [BEAT 2] 0:50 - 1:30 · violet · *give it the contract*

"Context first, but not the version you have been told to give it. 'Each row is one month' is table stakes - it can infer that.

What it cannot infer is the contract. Which columns are entered and which are derived. Which one is the source of truth when two disagree - here, units, not the order log. What it must never touch: column D is a formula, and replacing a formula with its value is how a model quietly dies. And your conventions: ex-VAT, sterling, sign-positive.

It matters because the add-in edits the live workbook. 'Do not touch' is the protection undo does not give you - undo reaches the edit you just watched, not the version you already sent on.

Put the contract in the add-in's Instructions and you set it once, not every chat."

### [BEAT 3] 1:30 - 2:10 · blue · *ask for the assumption*

"Second habit, and this is where it diverges from the beginner version.

Everyone says ask for the formula, not the answer. But you read formulas fluently, and that fluency is what hides this failure. Look: equals AVERAGE, D2 to D13. Valid. Correct range. Nothing to object to.

So ask for the formula and the assumption it encodes. Same formula back, plus one sentence: 'I assumed each month should count equally.'

There it is. That sentence is the entire error, and it was never going to show up in the syntax. Make it permanent in your Instructions: state the assumption behind any aggregate, one sentence, every time."

### [BEAT 4] 2:10 - 2:40 · teal · *where it actually beats you*

"Quick and honest, because most demos aimed at you are insulting.

It is not faster than you at building a model. It is faster at reading somebody else's nested formula three levels deep, tracing precedents across tabs, matching two data sets and listing what did not match, and sweeping a workbook for every buried constant without getting bored on row four thousand.

The pattern: use it where thoroughness beats judgement. Not the reverse."

### [BEAT 5] 2:40 - 3:10 · indigo · *the session drifts*

"Two things that catch experienced people out.

One: it is not deterministic. Same prompt, same workbook, twice, and you get a different model - different formulas, different structure, same plausible output. So 'I checked it' is a claim about one run. Re-run it and you have not checked the new one.

Two: long conversations get compacted automatically to avoid running out of context, so the contract you set at minute five is summarised, not preserved. Re-state it.

Verification is per-run, not per-tool."

### [BEAT 6] 3:10 - 4:20 · red · *every row is right, and the answer is wrong* — the beat the day is built on

"Right. Here is the one.

Twelve months of supplier spend. B is spend, C is units, D is cost per unit. I asked for the average cost per unit for the year. It wrote equals AVERAGE of D2 to D13, and returned eighteen pounds thirty-three.

Check the range: all twelve months, nothing missed. Check the function: AVERAGE is right for an average. Check a row - July, forty thousand eight hundred over three thousand four hundred is twelve pounds exactly. Correct. Pick any other row. Also correct. Every cell on this sheet is right.

The answer is still wrong by twelve per cent.

Take ten seconds."

> ⏸ **HOLD THE SILENCE. Count to ten on camera.** Do not narrate, do not point, do not move the mouse. There is genuinely nothing on the sheet to find - the marquee covers the whole column, correctly - and that is the lesson. An advanced room will hunt for a bad cell and fail, and *that failure is the payload*. Talk through this and the beat is gone, and so is the video.

"You cannot find it by looking, and neither could I. There is nothing on screen to catch."

### [BEAT 7] 4:20 - 5:15 · yellow · *reconcile, do not spot-check*

"Here is the catch, and notice what it is not. It is not 'check a row'. Checking rows finds nothing here, because every row is right. A spot-check scales linearly while a model does not, and against a method error it fails completely.

Compute the number a second, independent way. Total spend over total units: sixteen pounds thirty-one.

They do not tie. Twelve per cent apart, and the mean is the wrong one - an unweighted average over-weights your quiet months, which are your expensive ones. Twelve per cent on a unit cost is a pricing decision, not a rounding difference.

So: tie the headline to a control total you already trust. Cross-foot. Rebuild it a second way from different cells. Any of the three catches this in under a minute.

The second calculation can be Claude's. The agreement cannot."

### [BEAT 8] 5:15 - 5:50 · green · *hunt the hardcodes*

"The highest-value thing to point it at is not a blank sheet. It is a model somebody else built that is still in use every month.

Every constant buried inside a formula, with its cell. Every range that will not grow when a row is added. Every lookup whose key is not unique - that one is worth the price of admission on its own. Every cell that is an input on one tab and a formula on another.

Ask for a list with cell references, not a narrative. Then you check the list, which is quick, instead of the model, which is not. Evidence you can verify, not a reassurance you cannot.

This is the one place it is unambiguously better than you."

### [BEAT 9] 5:50 - 6:40 · orange · *do it live*

"Let me do the whole loop in thirty seconds."

**[CUT TO CLAUDE DESKTOP]** — see Demo steps below (~30s)

**[BACK TO BOARD]**

"Two rules, and the second is ours rather than Anthropic's.

Theirs: a workbook from outside can carry instructions you did not write, so treat a vendor template like any untrusted file - and nothing confidential or personal goes into a sheet you will share.

Ours: Claude for Excel is not in Enterprise audit logs and does not inherit your retention settings. Nothing records that anyone checked this, so your reconciliation is the only audit trail there is. Write it down.

Pause and try it: take a model you own and reconcile its headline number a second way. If it ties, you lost four minutes. If it does not, you just found something.

If it does not tie, it is not done."

---

## Demo steps

Invented, generic data throughout. No patient information and no Phlo specifics, at any point.

**Demo — the reconciliation loop (~30s)**

1. Open Claude Desktop on a fictional workbook: months, spend, units, a derived cost-per-unit column. Say out loud that every figure is made up.
2. Ask: `What was our average cost per unit last year? Give me the formula and the assumption it encodes.`
3. Read the assumption sentence back on camera. This is beat 3, live, and it is the fastest win in the video.
4. Ask: `Now compute the same figure a second, independent way, using different cells.`
5. Put the two numbers side by side. If they tie, say so and say why that is still worth the forty seconds. If they do not, ask: `Which assumption differs between the two?`

> If it wobbles, describe the problem plainly and keep talking — re-runs are cheap. Invented numbers only, and never a real workbook on camera.

---

## Ships

One model, reconciled a second way, with the tie-out written down.

## Pause-and-try

Take a model you own and reconcile its headline number a second way.

---

## A note on where this sits

This board is pitched at advanced users and it does not behave like the rest of the AI Ops Learn series. It assumes fluency in both Excel and Claude, it uses modelling vocabulary without glossing it, and its central beat only works on a room that will try to find the bug and fail.

**That makes it a poor fit for the mandatory all-staff course**, which is written for clinical, ops, commercial and support colleagues as well as analysts. If it is going into the mandatory track it needs either a general-audience sibling or an explicit "advanced / optional" label on the Loom. That is a call for whoever owns the curriculum, not one to fix by softening the board — a version pitched at everyone would lose the only thing this one has.
