#!/usr/bin/env python3
"""Build claude-excel.excalidraw - ONE flowing, illustrated explainer for
DAY 15 of the Phlo AI training: "Claude in Microsoft Excel"
(~7 min board + ~30s live cut-away, hard cap 8).

WHO THIS IS FOR - and it is NOT the rest of the course
------------------------------------------------------
Retargeted on 2026-09-16 at the user's request: **advanced users, in Excel AND
with Claude.** That is a real change of audience, not a change of tone, and it
is why the board was rewritten rather than edited. The previous version taught
"ask for the formula", "describe the sheet", "check one row by hand" - correct
habits, and ones this audience already has. Teaching them to a modeller is
worse than useless: it signals the video has nothing for them, and they stop
watching before the beat that does.

READ THIS BEFORE EDITING: this board is NOT general-audience material, and the
rest of the AI Ops Learn series is. If it is being slotted into the mandatory
all-staff course, that is a mismatch somebody has to decide about - see the note
in CLAUDE.md. Do not "fix" it by softening it back to the middle; a board pitched
at everyone would lose the one thing this one has.

THE ESCALATION, BEAT BY BEAT
-----------------------------
  old: ask for the formula, not the answer   ->  ask for the ASSUMPTION the
       formula encodes. An advanced user reads formulas fluently, and that
       fluency is exactly what hides this failure - the syntax is never wrong.
  old: describe the sheet first              ->  state the model's CONTRACT:
       what is authoritative, what is derived, what must never be overwritten.
  old: check one row by hand                 ->  RECONCILE. A spot-check scales
       linearly and a model does not - and against a method error it fails
       completely, because every row really is right.
  new: the session drifts (non-determinism + auto-compaction).
  new: hunt the hardcodes - the exhaustive sweep, the one job where it is
       unambiguously better than a human.

THE ADVERSARIAL BEAT HAD TO GET HARDER, AND THIS IS THE WHOLE REWRITE
---------------------------------------------------------------------
The old beat 6 was a SUM range stopping one row short. Any competent Excel user
spots that in two seconds, so with this audience the ten-second silence dies on
camera and the day dies with it.

The new failure is an AVERAGE OF AVERAGES, and it is a different species:

    Claude is asked for the average cost per unit and writes =AVERAGE(D2:D13) -
    the unweighted mean of twelve monthly rates. The range is correct. The
    formula is valid. EVERY CELL IN D IS ARITHMETICALLY RIGHT. Spot-check any
    row and it checks out (Jul: 40,800 / 3,400 = 12.00 exactly).

    The answer is still wrong. The correct figure is total spend over total
    units - a WEIGHTED mean - because volume is not flat across the months.
    18.33 against 16.31: a 12.4% overstatement, on a number you would price off.

Why this one and not another subtle bug: it is the only shape that DEFEATS THE
OLD CATCH. "Check one row by hand" finds nothing here, because every row is
right. That forces beat 7 to teach reconciliation instead, which is the actual
advanced discipline, and it makes beats 6 and 7 a single argument rather than a
failure followed by a tip.

NOTHING ON BEAT 6's SHEET IS WRONG, AND THAT IS THE POINT. The old board drew a
marquee that visibly stopped short. This one draws a marquee over the WHOLE of
D2:D13 - correctly - so there is genuinely nothing to find by looking. Do not
"improve" this beat by introducing a visible flaw; the absence of one is the
lesson. Red appears on the heading, on the "take ten seconds" prompt and on the
catch strip, and NOWHERE on the sheet.

ONE WORKED EXAMPLE RUNS THE BOARD, pinned in MONTHS / UNITS / CPU / SPEND with
asserts so it cannot drift out of arithmetic: a generic twelve-month supplier
spend sheet where quiet months carry a high unit cost and busy months a low one.
GBP 18.33 is the wrong headline on beats 1, 3, 6 and 7; GBP 16.31 is the right
one, revealed only on beat 7. CHANGE IT AND BEATS 1, 2, 3, 6, 7 AND 9 ALL MOVE.

TWO COLOURS ARE HELD CONSTANT AND ARE NOT BEAT ACCENTS:
  * BLUE = a formula and the range it covers (beats 3 and 6). Beat 6's marquee
    is blue on a red beat on purpose: a blue range border is what a spreadsheet
    selection looks like, so it reads as neutral UI, not as a flag.
  * GREEN = the human pass, held from Days 10, 11, 13 and 14. Beat 7's gate is
    green although the beat's accent is yellow. Beat 8's accent is green by the
    scaffold; that is an accent, not the human-pass marker.

VERIFIED AGAINST ANTHROPIC'S LIVE DOCS on 2026-09-16
-----------------------------------------------------
Primary source: claude.com/docs/office-agents/excel. Full read on
`claude-excel-resource-card.md`. What the docs back directly:
  * Beat 2's "it edits the live workbook" and the contract's do-not-overwrite
    line - documented overwrite protection and risky-operation confirmations,
    plus the best practice "Start with a trusted copy of the workbook before
    asking Claude to edit widely".
  * Beat 2's persistent Instructions - Settings in the add-in sidebar, per app.
  * Beat 5's auto-compaction half: "longer conversations are automatically
    compacted into new conversations". The non-determinism half is a property of
    the model, NOT a documented Excel behaviour - the card says so.
  * Beat 8's exhaustive sweep - documented error tracing and root-cause finding,
    plus the preloaded model-auditing Skill.
  * Beats 6/7 wholesale: the docs' own limitations list says Claude for Excel is
    not recommended for "Audit-critical calculations without verification", and
    the best practices say "Verify that outputs match your organization's
    standards and your own judgment".
  * Beat 9's governance rule: Claude for Excel "does not inherit custom data
    retention settings" and "Activity is not included in Enterprise audit logs".
The board names NO plan and NO tier, so it does not date. Fix the card, not the
board.

PAN ORDER (left to right - the whitespace between slots IS the camera; frame one
beat at a time, and hold the silence on 6):

     1  ORANGE  the error that survives a spot-check
     2  VIOLET  give it the contract              <- not "describe the sheet"
     3  BLUE    ask for the assumption            <- not "ask for the formula"
     4  TEAL    where it actually beats you
     5  INDIGO  the session drifts                <- non-determinism + compaction
     6  RED     every row is right, and the answer is wrong   <- HERO. 1600 wide.
     7  YELLOW  reconcile, do not spot-check      <- the catch for 6
     8  GREEN   hunt the hardcodes
     9  ORANGE  do it live                        <- [CUT TO CLAUDE DESKTOP], close

BEAT 6 IS THE ONE WIDE SLOT (1600, not 1200): a four-column, twelve-row sheet at
a readable size, plus the formula, the result and the catch. Widened rather than
made taller on purpose - on a 16:10 laptop HEIGHT binds framing, so 1600x980
frames better than 1200x1230. Day 14's beat 10 records the identical decision.

RUNTIME: budget in seconds, then MEASURE the written prose (wc -w) - this repo's
recorded process lesson is that per-beat budgets drift by up to 2x, and it has
bitten on Day 10 and Day 14. At ~150 wpm the script must land near 1,050 words.
The command is in the script's header. MEASURE IT BEFORE CALLING IT DONE.

Run:  python3 videos/ai-training/15-excel/build_excel.py
      python3 preview.py videos/ai-training/15-excel/claude-excel.excalidraw out.png
"""
import os
import sys

_d = os.path.dirname(os.path.abspath(__file__))
while _d != os.path.dirname(_d) and not os.path.exists(os.path.join(_d, "excalidraw_kit.py")):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)

import random
from excalidraw_kit import *

random.seed(80810)

# ----------------------------------------------------------------------------
# THE ONE WORKED EXAMPLE - a generic twelve-month supplier spend sheet.
# Quiet months carry a high unit cost, busy months a low one, which is what
# makes the unweighted mean wrong. Beats 1, 2, 3, 6, 7 and 9 all read from here.
# ----------------------------------------------------------------------------
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
UNITS = [1200, 1100, 1400, 1300, 2600, 3100, 3400, 3200, 2900, 2700, 1500, 1250]
CPU = [24.00, 25.00, 22.00, 23.00, 15.00, 13.00, 12.00, 12.50, 14.00, 14.50, 21.00, 24.00]
SPEND = [int(round(u * c)) for u, c in zip(UNITS, CPU)]

WRONG_FORMULA = "=AVERAGE(D2:D13)"                 # the unweighted mean of the rates
RIGHT_FORMULA = "=SUM(B2:B13)/SUM(C2:C13)"         # total spend over total units
UNWEIGHTED = sum(CPU) / len(CPU)                   # 18.3333 -> 18.33
WEIGHTED = sum(SPEND) / sum(UNITS)                 # 16.3099 -> 16.31
OVERSTATED = (UNWEIGHTED - WEIGHTED) / WEIGHTED * 100

# EVERY row must spot-check exactly, because the narration says "pick any other
# row - also correct". That is the claim beat 6 cannot afford to be wrong about:
# if one row fails to divide cleanly, an advanced room finds THAT instead of the
# real lesson, and the beat is dead. Both directions are pinned.
assert all(u * c == s for u, c, s in zip(UNITS, CPU, SPEND)), \
    "SPEND must be whole pounds"
assert all(SPEND[i] / UNITS[i] == CPU[i] for i in range(len(MONTHS))), \
    "EVERY row must spot-check exactly - the narration says 'pick any other row'"
assert f"{UNWEIGHTED:.2f}" == "18.33" and f"{WEIGHTED:.2f}" == "16.31"
assert 12.0 < OVERSTATED < 13.0
SPOT = 6  # July - the row the narration works through live; 40,800 / 3,400 = 12.00


def money(n):
    return f"{n:,}"


def gbp(x):
    return f"£{x:,.2f}"


# ----------------------------------------------------------------------------
# BEAT SCAFFOLD  (9 beats, uniform 1200 slots except the wide adversarial 6)
# ----------------------------------------------------------------------------
N = 9
GAP = 800
WID = {i: 1200 for i in range(1, N + 1)}
WID[6] = 1600                                  # the one wide slot - see docstring
ACCENT = {1: ORANGE, 2: VIOLET, 3: BLUE, 4: TEAL, 5: INDIGO,
          6: RED, 7: YELLOW, 8: GREEN, 9: ORANGE}
OX = {}
_c = 0
for _i in range(1, N + 1):
    OX[_i] = _c
    _c += WID[_i] + GAP
TOTAL_W = _c
HEAD_Y = 60
MAX_TEXT_W = 1400                              # stricter than the widest slot


def beat_head(i, title, sub=None):
    ox = OX[i]
    heading(ox, HEAD_Y, title, color=ACCENT[i], sub=sub)
    return ox


# ----------------------------------------------------------------------------
# LOCAL ONE-OFF ILLUSTRATIONS
# ----------------------------------------------------------------------------
GUT = 54   # the row-number gutter

# accent -> its pastel fill, so a doodle takes the colour of the beat it sits on
# (the kit's TINT map is the ultra-light wash, which is too faint for a header strip)
ACC_BG = {VIOLET: VIOLET_BG, ORANGE: ORANGE_BG, GREEN: GREEN_BG, BLUE: BLUE_BG,
          RED: RED_BG, TEAL: TEAL_BG, YELLOW: YELLOW_BG, INDIGO: INDIGO_BG}


def grid(x, y, w, h, accent, abg, rows=5, cols=5, hi=None):
    """An anonymous spreadsheet grid - tinted header row and row-header column,
    faint gridlines, optional highlighted cell at hi=(col, row). Carried over
    from the previous build; beat 1 wants a sheet with no readable contents so
    the ONE figure in it is the only thing to look at."""
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="grid")
    cw, ch = w / cols, h / rows
    rect(x, y, w, ch, stroke="transparent", bg=abg, sw=1, rough=1, rounded=False, prefix="ghead")
    rect(x, y, cw, h, stroke="transparent", bg=abg, sw=1, rough=1, rounded=False, prefix="gcol")
    for c in range(1, cols):
        line(x + c * cw, y, [[0, 0], [0, h]], stroke=FAINT, sw=1)
    for r in range(1, rows):
        line(x, y + r * ch, [[0, 0], [w, 0]], stroke=FAINT, sw=1)
    if hi:
        cc, rr = hi
        rect(x + cc * cw, y + rr * ch, cw, ch, stroke=accent, bg=accent, sw=2, rough=1,
             rounded=False, fill="solid", opacity=45, prefix="ghi")


def ledger(x, y, w, rows, abg, headers, row_h=44, size=SMALL, letters=True):
    """A spreadsheet with REAL cell contents - the kit's grid() draws empty cells,
    and this board lives or dies on the audience being able to read B2:B13.

    Excel row 1 is the header, so the gutter numbers the data rows from 2 and a
    cell reference on the board matches the cell drawn under it. Returns the
    geometry so callers can place a selection marquee with cell_box()."""
    ncol = len(headers)
    colw = (w - GUT) / ncol
    lh = int(row_h * 0.68) if letters else 0
    h = lh + (len(rows) + 1) * row_h
    rect(x, y + lh, w, h - lh, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="sheet")
    if letters:
        rect(x, y, w, lh, stroke=FAINT, bg=abg, sw=1, rough=1, rounded=False, prefix="scols")
        for c in range(ncol):
            text_centered(x + GUT + (c + 0.5) * colw, y + (lh - size * LINE_H) / 2,
                          chr(ord("A") + c), size=size, color=GREYD)
    rect(x, y + lh, w, row_h, stroke="transparent", bg=abg, sw=1, rough=1,
         rounded=False, prefix="shead")
    rect(x, y + lh, GUT, h - lh, stroke="transparent", bg=abg, sw=1, rough=1,
         rounded=False, prefix="sgut")
    for c in range(ncol + 1):
        line(x + GUT + c * colw, y + lh, [[0, 0], [0, h - lh]], stroke=FAINT, sw=1)
    for r in range(1, len(rows) + 1):
        line(x, y + lh + r * row_h, [[0, 0], [w, 0]], stroke=FAINT, sw=1)
    ty = (row_h - size * LINE_H) / 2
    text(x + 14, y + lh + ty, "1", size=size, color=GREY)
    for c, hd in enumerate(headers):
        text(x + GUT + c * colw + 12, y + lh + ty, hd, size=size, color=GREYD)
    for r, cells in enumerate(rows):
        ry = y + lh + (r + 1) * row_h
        text(x + 14, ry + ty, str(r + 2), size=size, color=GREY)
        for c, cell in enumerate(cells):
            text(x + GUT + c * colw + 12, ry + ty, cell, size=size, color=INK)
    return {"x": x, "y": y, "w": w, "h": h, "lh": lh, "row_h": row_h, "colw": colw}


def cell_box(g, col, row):
    """col: 0-based data column (0 = A). row: the Excel row number (1 = header)."""
    return (g["x"] + GUT + col * g["colw"],
            g["y"] + g["lh"] + (row - 1) * g["row_h"],
            g["colw"], g["row_h"])


def marquee(g, col, row_from, row_to, color=BLUE, sw=3):
    """A spreadsheet SELECTION - border only, never a fill, so the cell values
    underneath stay readable. Blue because that is what a range border looks
    like in a spreadsheet; it must read as neutral UI, not as a flag."""
    cx, cy, cw, _ = cell_box(g, col, row_from)
    rect(cx + 2, cy + 2, cw - 4, (row_to - row_from + 1) * g["row_h"] - 4,
         stroke=color, bg="transparent", sw=sw, rough=1, rounded=False, prefix="marq")


def human_gate(cx, cy, color=GREEN):
    """A deliberately unmistakable human marker. The kit's person() is sized for
    a crowd of tiny figures; this one stands alone and is safety-bearing, so it
    is drawn big - the same reasoning Day 3 and Day 10 record."""
    ellipse(cx - 21, cy - 79, 42, 42, stroke=color, bg=WHITE, sw=4, rough=1)
    line(cx - 42, cy + 14, [[0, 0], [0, -14], [10, -30], [26, -38], [42, -40],
                            [58, -38], [74, -30], [84, -14], [84, 0]],
         stroke=color, sw=4, rough=1)


def mini_sheet(x, y, w, h, abg, rows=4, cols=3, ragged=False):
    """A small anonymous sheet - no cell contents. `ragged` draws uneven stubs
    instead of clean rows, for the messy-export doodle."""
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="msheet")
    rect(x, y, w, h / (rows + 1), stroke="transparent", bg=abg, sw=1, rough=1,
         rounded=False, prefix="mshead")
    rh = h / (rows + 1)
    for r in range(1, rows + 1):
        if ragged:
            line(x + 10, y + r * rh + rh / 2, [[0, 0], [w * random.uniform(0.3, 0.92), 0]],
                 stroke=GREY, sw=2)
        else:
            line(x + 10, y + r * rh + rh / 2, [[0, 0], [w - 20, 0]], stroke=GREY, sw=2)
    if not ragged:
        for c in range(1, cols):
            line(x + c * (w / cols), y, [[0, 0], [0, h]], stroke=FAINT, sw=1)


def doodle_error(x, y, accent):
    """Tracing a #REF! back to its cause. The "#REF!" literal stays RED whatever the
    beat accent - a spreadsheet error IS red - and that contrast is load-bearing:
    beat 4 shows the LOUD failures Claude is genuinely good at finding, which is
    exactly why beat 6 can be the beat with no red anywhere on the sheet."""
    mini_sheet(x, y, 284, 120, ACC_BG[accent], rows=4, cols=4)
    text(x + 196, y + 30, "#REF!", size=SMALL, color=RED)
    arrow(x + 192, y + 46, [[0, 0], [-92, 40]], stroke=accent, sw=3, rough=1)
    text(x + 40, y + 88, "the cause", size=SMALL, color=accent)


def doodle_hardcode(x, y, accent):
    """Constants buried inside formulas, ringed. The rings are the BEAT ACCENT, not
    red: a hardcode is a finding, not an error, and beat 6 needs red to stay scarce."""
    mini_sheet(x, y, 284, 120, ACC_BG[accent], rows=4, cols=4)
    text(x + 22, y + 32, "=B4*1.15", size=SMALL, color=GREYD)
    circle_around(x + 52, y + 20, 64, 46, accent, sw=3)
    text(x + 22, y + 80, "=C7+4200", size=SMALL, color=GREYD)
    circle_around(x + 52, y + 68, 68, 46, accent, sw=3)


def doodle_lookup(x, y, accent):
    mini_sheet(x, y + 18, 104, 104, ACC_BG[accent], rows=3, cols=2)
    mini_sheet(x + 180, y, 104, 104, ACC_BG[accent], rows=3, cols=2)
    link_icon(x + 108, y + 52, color=accent)


def doodle_explain(x, y, accent):
    rect(x, y + 40, 150, 46, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="fbox")
    text(x + 12, y + 52, "=XLOOKUP(...)", size=SMALL, color=GREYD)
    rect(x + 168, y, 116, 82, stroke=accent, bg=TINT[accent], sw=2, rough=1,
         rounded=True, prefix="bub")
    line(x + 188, y + 82, [[0, 0], [-14, 26], [22, -2]], stroke=accent, sw=2)
    for r in range(3):
        line(x + 184, y + 26 + r * 18, [[0, 0], [82, 0]], stroke=accent, sw=2)


def paper_stack(x, y, w, h, abg, n=3):
    for k in range(n):
        off = (n - 1 - k) * 14
        rect(x + off, y + off, w, h, stroke=INK, bg=(WHITE if k == n - 1 else abg),
             sw=2, rough=1, rounded=True, prefix="stk")


# ============================================================================
# BOARD TITLE
# ============================================================================
text(OX[1], -300, "Claude in Microsoft Excel", size=HERO, color=INK)
text(OX[1] + 6, -300 + HERO * LINE_H + 4,
     "advanced - the errors that survive a review", size=H2, color=ORANGE)

# ============================================================================
# BEAT 1 - ORANGE - the error that survives a spot-check
# ============================================================================
ox = beat_head(1, "the error that survives a spot-check",
               "you already check your work. this video is about\n"
               "the kind of error that checking does not catch")

grid(ox + 40, 350, 300, 190, accent=ORANGE, abg=ORANGE_BG, rows=5, cols=4, hi=(2, 2))
text(ox + 40 + 2 * 75 + 4, 350 + 2 * 38 + 9, gbp(UNWEIGHTED), size=SMALL, color=INK)
text(ox + 40, 562, "a cost per unit", size=SMALL, color=GREY)
arrow(ox + 358, 445, [[0, 0], [56, 0]], stroke=ORANGE, sw=4, rough=1)

rect(ox + 430, 360, 290, 170, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="pl")
text(ox + 452, 382, "the price list", size=SMALL, color=INK)
text(ox + 452, 424, gbp(UNWEIGHTED), size=H2, color=ORANGE)
text(ox + 452, 482, "+ the margin we want", size=SMALL, color=GREY)
text(ox + 430, 562, "a price", size=SMALL, color=GREY)
arrow(ox + 738, 445, [[0, 0], [56, 0]], stroke=ORANGE, sw=4, rough=1)

rect(ox + 820, 360, 300, 170, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="mg")
text(ox + 844, 386, "the margin\nwe quoted", size=H3, color=INK)
tick(ox + 844, 476, GREEN, s=28, sw=4)
text(ox + 896, 478, "signed off", size=SMALL, color=GREEN)
text(ox + 820, 562, "a commitment", size=SMALL, color=GREY)

text(ox + 40, 634, "every cell behind this number was correct", size=H2, color=ORANGE)
text(ox + 40, 714,
     "You are not the audience for “always double-check”. You already do that. The failure\n"
     "that costs you is the one where every input is right, every formula is valid, every\n"
     "range is correct - and the answer is still wrong, because the method was wrong.",
     size=BODY, color=GREYD)
text(ox + 40, 830,
     "Claude produces that failure fluently, and it produces it in a form that passes review.",
     size=BODY, color=GREYD)
chip(ox + 40, 890, "method errors, not typos", fill=ORANGE_T, text_color=ORANGE, border=ORANGE)

# ============================================================================
# BEAT 2 - VIOLET - give it the contract
# ============================================================================
ox = beat_head(2, "give it the contract",
               "what a row means is table stakes. tell it what is\n"
               "authoritative, what is derived, and what it must not touch")

CONTRACT = [("INPUTS", "columns B and C are entered. everything else is derived."),
            ("AUTHORITATIVE", "the units column is the source of truth for volume"),
            ("NEVER OVERWRITE", "column D is a formula. never replace it with its value."),
            ("CONVENTIONS", "spend is ex-VAT, in GBP, and always positive.")]
for k, (lab, body) in enumerate(CONTRACT):
    cy = 330 + k * 130
    sticky(ox + 40, cy, 1080, 110, VIOLET_T, angle=jit(0.7))
    text(ox + 72, cy + 34, lab, size=H3, color=VIOLET)
    text(ox + 400, cy + 38, body, size=BODY, color=INK)

text(ox + 40, 880,
     "It edits the live workbook. “Do not touch” is the protection undo does not give you.",
     size=BODY, color=GREYD)
chip(ox + 40, 940, "set the contract once, in the add-in’s Instructions",
     fill=VIOLET_T, text_color=VIOLET, border=VIOLET)

# ============================================================================
# BEAT 3 - BLUE - ask for the assumption
# ============================================================================
ox = beat_head(3, "ask for the assumption",
               "you can read a formula. you cannot read the\n"
               "assumption the formula encodes")

sticky(ox + 40, 330, 520, 360, FAINT, angle=jit(0.8))
text(ox + 72, 356, "you ask", size=SMALL, color=GREY)
text(ox + 72, 388, "“give me the formula”", size=BODY, color=INK)
text(ox + 72, 480, "you get", size=SMALL, color=GREY)
text(ox + 72, 512, WRONG_FORMULA, size=H3, color=INK)
text(ox + 72, 580, "valid. right range. and it tells\nyou nothing about whether that\n"
                   "is the right method.", size=SMALL, color=GREYD)

sticky(ox + 600, 330, 520, 360, BLUE_T, angle=jit(0.8))
text(ox + 632, 356, "you ask", size=SMALL, color=BLUE)
text(ox + 632, 388, "“give me the formula, and\nthe assumption it makes”", size=BODY, color=INK)
text(ox + 632, 480, "you get", size=SMALL, color=BLUE)
text(ox + 632, 512, WRONG_FORMULA, size=H3, color=BLUE)
text(ox + 632, 560, "“I assumed each month\nshould count equally.”", size=BODY, color=INK)
text(ox + 632, 636, "there it is. that sentence is\nthe whole error.", size=SMALL, color=BLUE)

chip(ox + 40, 730, "the bug is never in the syntax", fill=BLUE_T, text_color=BLUE, border=BLUE)
text(ox + 40, 820,
     "Put it in your Instructions: state the assumption behind any aggregate, in one\n"
     "sentence, every time. It costs nothing, and it is the only place the error is visible.",
     size=BODY, color=GREYD)
text(ox + 40, 930,
     "You read formulas fluently. That fluency is exactly what hides this failure -\n"
     "there is nothing wrong with the formula.", size=BODY, color=BLUE)

# ============================================================================
# BEAT 4 - TEAL - where it actually beats you
# ============================================================================
ox = beat_head(4, "where it actually beats you",
               "you are faster at deciding. it is faster at the\n"
               "exhaustive, boring sweep")

jobs = [(doodle_explain, "read a nested formula", "somebody else’s, three\nlevels deep"),
        (doodle_error, "trace precedents across tabs", "a #REF, a stale link,\na circular reference"),
        (doodle_lookup, "match two sets", "and list what did\nnot match"),
        (doodle_hardcode, "sweep for hardcodes", "every constant buried\nin a formula")]
for k, (doodle, head, cap) in enumerate(jobs):
    jx = ox + 40 + (k % 2) * 560
    jy = 330 + (k // 2) * 322
    doodle(jx + 8, jy, TEAL)
    text(jx, jy + 152, head, size=H3, color=TEAL)
    text(jx, jy + 202, cap, size=BODY, color=GREYD)

text(ox + 40, 966,
     "It is not faster than you at deciding what the model should do. Use it where\n"
     "thoroughness beats judgement.", size=BODY, color=TEAL)

# ============================================================================
# BEAT 5 - INDIGO - the session drifts
# ============================================================================
ox = beat_head(5, "the session drifts",
               "two reasons what was true at minute five is\n"
               "not true at minute forty")

sticky(ox + 40, 330, 1080, 250, INDIGO_T, angle=jit(0.6))
text(ox + 72, 356, "1 · it is not deterministic", size=H3, color=INDIGO)
text(ox + 72, 414,
     "The same prompt, on the same workbook, twice, does not give you the same\n"
     "model twice. Different formulas, different structure, same plausible output.",
     size=BODY, color=INK)
text(ox + 72, 504, "So “I checked it” is a claim about one run, not about the tool.",
     size=BODY, color=INDIGO)

sticky(ox + 40, 620, 1080, 250, INDIGO_T, angle=jit(0.6))
text(ox + 72, 646, "2 · long sessions compact", size=H3, color=INDIGO)
text(ox + 72, 704,
     "Long conversations are automatically compacted to avoid running out of\n"
     "context. The contract you set at the start is summarised, not preserved.",
     size=BODY, color=INK)
text(ox + 72, 794, "Re-state it. Minute forty does not still know what minute five was told.",
     size=BODY, color=INDIGO)

chip(ox + 40, 910, "verification is per-run, not per-tool",
     fill=INDIGO_T, text_color=INDIGO, border=INDIGO)

# ============================================================================
# BEAT 6 - RED - every row is right, and the answer is wrong
# *** THE ADVERSARIAL HERO. Nothing on this sheet is wrong. That is the point. ***
# ============================================================================
ox = beat_head(6, "every row is right, and the answer is wrong",
               "the range is correct. the formula is valid.\n"
               "spot-check any row you like - it will check out.")

rows6 = [(MONTHS[i], money(SPEND[i]), money(UNITS[i]), f"{CPU[i]:.2f}") for i in range(12)]
g6 = ledger(ox + 50, 310, 720, rows6, FAINT,
            ("Month", "Spend  £", "Units", "Cost/unit  £"), row_h=46)
marquee(g6, 3, 2, 13)                       # D2:D13 - the WHOLE column, correctly
_mx, _my, _mw, _mh = cell_box(g6, 3, 2)
text(ox + 780, _my + 5.5 * g6["row_h"], "D2:D13", size=SMALL, color=BLUE)

text(ox + 870, 330, "what Claude wrote", size=SMALL, color=GREY)
text(ox + 870, 368, WRONG_FORMULA, size=H1, color=BLUE)
text(ox + 870, 460, "what it returned", size=SMALL, color=GREY)
text(ox + 870, 498, gbp(UNWEIGHTED), size=H1, color=INK)

text(ox + 870, 594,
     f"{MONTHS[SPOT]}: {money(SPEND[SPOT])} over {money(UNITS[SPOT])} is\n"
     f"{CPU[SPOT]:.2f} exactly. Correct.\nSo is every other row on the sheet.",
     size=BODY, color=GREYD)
text(ox + 870, 718, "Take ten seconds.", size=H3, color=RED)

sticky(ox + 870, 790, 660, 180, RED_T, angle=jit(0.7))
text(ox + 902, 814, "the catch", size=SMALL, color=RED)
text(ox + 902, 850,
     "Compute it a second, independent way.\nIf the two do not tie, the method is\nwrong - not the cells.",
     size=BODY, color=INK)

# ============================================================================
# BEAT 7 - YELLOW - reconcile, do not spot-check   (the catch for beat 6)
# ============================================================================
ox = beat_head(7, "reconcile, do not spot-check",
               "a spot-check scales linearly and a model does not -\n"
               "and against a method error it fails completely")

sticky(ox + 40, 330, 520, 200, FAINT, angle=jit(0.8))
text(ox + 72, 356, "the mean of the monthly rates", size=SMALL, color=GREYD)
text(ox + 72, 392, WRONG_FORMULA, size=H3, color=INK)
text(ox + 72, 452, gbp(UNWEIGHTED), size=H2, color=INK)

sticky(ox + 600, 330, 520, 200, YELLOW_T, angle=jit(0.8))
text(ox + 632, 356, "total spend over total units", size=SMALL, color=YELLOW)
text(ox + 632, 392, RIGHT_FORMULA, size=H3, color=INK)
text(ox + 632, 452, gbp(WEIGHTED), size=H2, color=INK)

text(ox + 40, 560,
     f"They do not tie. {OVERSTATED:.0f}% apart, and the mean is the one that is wrong -\n"
     "it over-weights your quiet months, which are your expensive ones.",
     size=BODY, color=GREYD)
text(ox + 40, 648, f"{OVERSTATED:.0f}% on a unit cost is a pricing decision, not a rounding difference.",
     size=BODY, color=RED)

chip(ox + 40, 706, "if it does not tie, do not ship it",
     fill=YELLOW_T, text_color=YELLOW, border=YELLOW)
for k, s in enumerate(["tie it to a control total you already trust",
                       "cross-foot: rows and columns reach the same total",
                       "rebuild it a second way, from different cells"]):
    check_item(ox + 40, 790 + k * 48, s, accent=YELLOW)

human_gate(ox + 920, 880, GREEN)
text_centered(ox + 920, 906, "you own the tie-out", size=LABEL, color=GREEN)
text(ox + 40, 950,
     "Claude can run the second calculation. It cannot be the thing that agrees with itself.",
     size=BODY, color=GREYD)

# ============================================================================
# BEAT 8 - GREEN - hunt the hardcodes
# ============================================================================
ox = beat_head(8, "hunt the hardcodes",
               "the exhaustive sweep is the one job where it is\n"
               "genuinely better than you are")

paper_stack(ox + 40, 350, 330, 280, GREEN_BG, n=3)
mini_sheet(ox + 40, 350, 330, 280, GREEN_BG, rows=6, cols=4)
text(ox + 40, 680, "a model you inherited.\nin use every month.", size=SMALL, color=GREYD)

for k, q in enumerate(["every constant buried in a formula, with its cell",
                       "every range that will not grow with a new row",
                       "every lookup whose key is not unique",
                       "every input that is a formula somewhere else"]):
    qy = 340 + k * 98
    sticky(ox + 460, qy, 660, 86, GREEN_T, angle=jit(1.0))
    text(ox + 492, qy + 26, q, size=BODY, color=INK)

text(ox + 40, 762,
     "Ask for a list with cell references, not a narrative. Then check the list -\n"
     "which is quick - instead of the model, which is not.", size=BODY, color=GREYD)
chip(ox + 40, 862, "make it produce evidence you can check",
     fill=GREEN_T, text_color=GREEN, border=GREEN)
text(ox + 40, 950,
     "This is the one place it is unambiguously better than you: it does not get\n"
     "bored on row four thousand.", size=BODY, color=GREEN)

# ============================================================================
# BEAT 9 - ORANGE - do it live  (demo, pause-and-try, the red rule, the close)
# ============================================================================
ox = beat_head(9, "do it live",
               "one model, reconciled a second way -\n"
               "and the tie-out written down")

demo_badge(ox + 40, 320,
           "show in Claude desktop app: ask for the assumption, then reconcile a second way")

for k, s in enumerate(["ask for the number, the formula, and the assumption",
                       "reconcile it a second way, from different cells",
                       "if they do not tie, ask which assumption differs"]):
    sy = 408 + k * 68
    num_badge(ox + 40, sy, k + 1, ORANGE)
    text(ox + 104, sy + 6, s, size=BODY, color=INK)

pause_icon(ox + 44, 632, 32, ORANGE)
text(ox + 104, 624, "pause here, and try it", size=H3, color=ORANGE)
text(ox + 104, 672, "Take a model you own and reconcile its headline number a second way.",
     size=BODY, color=INK)

rect(ox + 40, 750, 1080, 230, stroke=RED, bg=RED_T, sw=2, rough=1, rounded=True, prefix="rule")
text(ox + 72, 772, "two rules, and the second one is ours", size=H3, color=RED)
text(ox + 72, 822,
     "A workbook from outside can carry instructions you did not write, and nothing\n"
     "confidential or personal goes into a sheet you will share.\n"
     "Claude for Excel is not in Enterprise audit logs and does not inherit your\n"
     "retention settings - so your reconciliation IS the audit trail. Write it down.",
     size=BODY, color=INK)

text(ox + 40, 996, "If it does not tie, it is not done.", size=H3, color=INK)

# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "claude-excel.excalidraw")
finish(out, MAX_TEXT_W, TOTAL_W)
