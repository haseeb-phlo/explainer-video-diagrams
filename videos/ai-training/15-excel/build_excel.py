#!/usr/bin/env python3
"""Build claude-excel.excalidraw - ONE flowing, illustrated explainer for
DAY 15 of the Phlo AI training: "Claude in Microsoft Excel"
(~7 min 00 board + ~30s live cut-away = ~7 min 30, hard cap 8).

WHAT THIS BOARD IS NOW (it was ADAPTED and widened, then MOVED)
---------------------------------------------------------------
It was rebuilt in place at videos/claude/8-claude-excel/ (module 2.8) on
2026-09-15, then MOVED here as DAY 15 on 2026-09-16 at the user's request - the
same move Days 4, 7, 8, 10 and 12 each made out of videos/claude/. That series
now has a SIXTH numbering gap, at 8. A gap is not lost work, and NOTHING in
videos/claude/ was renumbered.

Per the repo precedence rule, a Day covers its topic IN FULL. There is no other
Excel video to signpost - module 2.8 IS this video, moved - so this board must
never be trimmed to a "see the other video" pointer.

It used to be a NINE-beat product walkthrough whose angle was "live formula
relationships": it works inside your spreadsheet, a real .xlsx, start from the
mess you inherited, it keeps the formulas alive, two front doors (chat vs the
Home-ribbon add-in), it finds what's broken, the jobs it's best at, trust the
model check the numbers, try it. That board taught a FEATURE SURFACE, and its
most interesting facts were a plan tier and a keyboard shortcut.

It is now a NINE-beat board about ONE HABIT, because of one observation:

    Every other surface in this programme fails VISIBLY. A deck that says
    nothing looks like a deck that says nothing; a rewrite that drops a clause
    is at least a sentence you can read. A spreadsheet fails as a PLAUSIBLE
    NUMBER SITTING IN A CELL that nobody queries - and it then flows into a
    decision.

THIS IS THE BOARD WHERE THE ADVERSARIAL BEAT IS THE POINT OF THE DAY RATHER
THAN A BEAT IN IT. Beat 6 is the hero and beat 7 is its catch; beats 1-5 exist
to make beat 6 land and beats 8-9 exist to make beat 7 stick. Everything else is
negotiable. Beat 6 is not.

BEAT 6 MUST NEVER BE SOFTENED INTO A GENERAL CAUTION. The commissioning brief
says so in as many words, and it is a DRAWING instruction, not a tone one:

  * The wrong range is drawn on the board, visibly. The sheet carries twelve
    real monthly figures in B2:B13; the selection marquee covers B2:B12; the
    December row sits BELOW the marquee with its value showing.
  * The total is PLAUSIBLE. GBP 376,600 against a true GBP 411,900 - both are
    six-figure numbers a reader would accept. The build ASSERTS both against
    SPEND so the worked example can never drift out of arithmetic. EVERY VALUE IN
    SPEND IS DISTINCT, deliberately: two equal figures next to the marquee's bottom
    edge make it ambiguous which row the range stops at, which is the one thing
    this beat cannot afford. Keep them distinct if you ever edit the example.
  * NOTHING ON THE SHEET IS FLAGGED. No cross, no red arrow, no "wrong range"
    chip pointing at December, no annotation on the missing row. The beat accent
    RED appears on the heading, on the "where is it wrong?" prompt and on the
    catch strip - and NOWHERE on the sheet itself. Annotating the error destroys
    the ten seconds of silence the whole day is built on.

If a future edit makes beat 6 read as "always double-check spreadsheets", the
day has been deleted and only its title remains.

ONE WORKED EXAMPLE RUNS THE BOARD: a generic twelve-month supplier spend sheet,
pinned in MONTHS / SPEND / WRONG_FORMULA / WRONG_TOTAL / TRUE_TOTAL at the top.
GBP 376,600 is the number travelling through beat 1's chain, the number the
broken range produces on beat 6, and the number the hand-check contradicts on
beat 7. CHANGE THE EXAMPLE AND BEATS 1, 2, 3, 4, 6, 7 AND 9 ALL MOVE TOGETHER.

BEAT 3 PLANTS THE RANGE THAT BEAT 6 BREAKS, AND THAT IS LOAD-BEARING. Beat 3's
good reply is "=AVERAGE(B2:B13) - column B, rows 2 to 13, all twelve months",
and it closes on "Twelve months of data live in B2:B13. Worth remembering."
Beat 6 then shows =SUM(B2:B12). A viewer who was listening on beat 3 can find
the error on beat 6 unaided, which is exactly the experience the brief asks for.
Beat 3 deliberately uses AVERAGE, not SUM, so it plants the RANGE without
revealing the annual TOTAL - using SUM there would hand the reveal to beat 3 and
leave beat 6 with nothing to find. Keep them different functions.

BEAT 7 IS THE CATCH, AND IT HAD TO BE MADE HONEST. "Recompute one row by hand"
catches a wrong per-row formula on its own, but it does NOT by itself catch a
wrong aggregate RANGE, which is what beat 6 breaks. So the discipline on this
board is stated as the pair that actually works: recompute one row by hand AND
check that the row you picked is inside the range - which is why you pick the
LAST one. That is one row, done by hand, and it genuinely catches beat 6.
Weakening it back to a bare "spot-check a row" breaks the beat 6 / beat 7 join.

TWO COLOURS ARE HELD CONSTANT AND ARE NOT BEAT ACCENTS:
  * BLUE = a formula and the range it covers. Beat 3's good reply, and beat 6's
    selection marquee and formula text. The marquee is blue ON A RED BEAT on
    purpose: a blue range border is what a spreadsheet's own selection looks
    like, so it reads as neutral UI rather than as a flag. Drawing it red would
    flag the error and gut the beat. (It is also border-only, never a fill, so
    it cannot dim the cell values underneath.)
  * GREEN = the human pass, held from Day 10, Day 11, Day 13 and Day 14. Beat 7's
    gate is green even though beat 7's accent is yellow. Beat 8's accent is
    green by the brief; that is an accent, not the human-pass marker.

THE BOARD NAMES THE TOOL, NEVER THE TIER. "Excel" appears in the board title and
in the demo badge and nowhere else - not one of the nine headings needs it. Plan
tiers, the two distinct capabilities the old board spent a beat separating (chat
builds a genuine .xlsx on every plan vs the Home-ribbon add-in editing the open
workbook), Ctrl+Alt+C, the Microsoft 365 add-in family and the doc links are all
on `claude-excel-resource-card.md`. That card is a deliverable, not an
afterthought: do not re-inflate the board with it, and WHEN A FACT MOVES, FIX
THE CARD, NOT THE BOARD. Same line Day 12 and Day 14 drew.

THE RED DATA CAUTION SITS ON BEAT 9, not on the card - the nine-beat brief has
no slot for it, but it is the only on-screen data-handling rule in a mandatory
course for a regulated pharmacy. The same call Day 7 (beat 3), Day 10 (beat 7),
Day 12 (beat 7) and Day 14 (beat 11) each made. The untrusted-workbook half
rides with it because beat 4 is the beat that tells people to feed outside
sheets in. Do not quietly drop it.

NO CURRICULUM ENTRY. Phlo_Mandatory_AI_Course_Curriculum.docx is not in the
repo and has no entry for this reframe (the module-2.8 entry that exists
describes the product walkthrough this replaces). Board and narration were
written from `claude-excel-prompt.md` with the user's explicit go-ahead on
2026-09-15 - the same route Days 10, 11, 12, 13 and 14 took. RECONCILE BEFORE
RECORDING.

Style B (house style): a single hand-drawn journey, left-to-right, NO frames, NO
boxes, white canvas, everything in the hand font (fontFamily 1), roughness 1, a
lively colour-coded Excalidraw palette, colour blocking, scribbled annotations
and charming primitive illustrations. The look lives in the shared
excalidraw_kit; this file holds only the composition and the bespoke one-offs
(`ledger`, the beat-5 doodles, `human_gate`).

PAN ORDER (left to right - the whitespace between slots IS the camera; frame one
beat at a time, and hold the silence on 6):

     1  ORANGE  a number nobody checked        <- cell -> slide -> decision
     2  VIOLET  it edits the live sheet        <- what undo does not reach
     3  BLUE    ask for the formula, not the answer   <- plants B2:B13
     4  TEAL    describe the sheet first
     5  INDIGO  what it is genuinely good at   <- honest beat, four jobs
     6  RED     a formula that looks right     <- ADVERSARIAL HERO. 1600 wide.
     7  YELLOW  check one row by hand          <- the catch for 6
     8  GREEN   audit, do not just build
     9  ORANGE  do it live                     <- [CUT TO CLAUDE DESKTOP], close

BEAT 6 IS THE ONE WIDE SLOT (1600, not 1200). It carries the twelve-row sheet at
a readable size, the formula, the total and the catch - three columns' worth. It
is widened rather than made TALLER on purpose: on a 16:10 laptop HEIGHT is what
binds framing, so 1600x980 frames more comfortably than 1200x1230. Day 14's beat
10 records the identical decision. Do not solve a space problem here by growing
downwards; every slot stays within ~980 tall.

RUNTIME (budgeted in seconds, then MEASURED against the written narration - the
measuring is the step that matters; this repo's recorded process lesson is that
per-beat second budgets drift by up to 2x against the written prose, and it has
bitten twice, on Day 10 and again on Day 14):

     1  :55   |  2  :40   |  3  :45   |  4  :45   |  5  :30
     6  1:15  |  7  :55   |  8  :50   |  9  :45  (+ ~:30 live cut-away)
     ------------------------------------------------------------------
     MEASURED at 1,051 words = ~7:00 board, plus the cut-away = ~7:30. Cap 8:00.
     The 2026-09-16 doc pass ADDED to beats 2, 4 and 8 and pushed this to 7:30,
     so the headroom is now ~30s. Anything further added must be traded against
     something removed. MEASURE IT (wc -w) BEFORE CALLING IT DONE - the command
     is in the script's header.

VERIFIED AGAINST ANTHROPIC'S LIVE DOCS on 2026-09-16
-----------------------------------------------------
Primary source: claude.com/docs/office-agents/excel (the old support-centre URL
301s to it, exactly the rot Day 12's check found for PowerPoint). The full read
is on `claude-excel-resource-card.md`; four things changed ON THIS BOARD:

  * BEAT 2 no longer claims Claude highlights what it changed - that is NOT in
    the docs. What IS documented is overwrite protection ("Claude warns you
    before overwriting existing data") and risky-operation confirmations, so the
    beat says that instead. The "work on a duplicate" chip is now DOC-BACKED:
    "Start with a trusted copy of the workbook before asking Claude to edit
    widely" is Anthropic's own best practice.
  * BEAT 4 gained the persistent Instructions field in the add-in's Settings -
    set once per app rather than retyped every chat. It earns board space under
    the same filter Day 3 and Day 4 apply: it changes what a person TYPES.
  * BEAT 5 swapped "reshape it" for "find what is broken". Debugging errors is
    one of Anthropic's headline documented strengths and it was missing, while
    reshaping is not documented at all. The swap also SETS UP BEAT 6: beat 5
    shows the LOUD errors it is genuinely good at finding, which is why beat 6
    can be the beat with no red anywhere on the sheet.
  * BEAT 8 gained the preloaded auditing Skill, invoked with "/" in the sidebar.

TWO DOCUMENTED FACTS VALIDATE THE WHOLE DAY, and they are worth knowing before
anyone waters beat 6 down. Anthropic's own "Current limitations" list says
Claude for Excel is not recommended for "Audit-critical calculations without
verification", and its best practices say "Verify that outputs match your
organization's standards and your own judgment". Beat 6 and beat 7 are not a
cautious Phlo gloss - they are the vendor's own limitation, dramatised.

The board still names NO plan and NO tier, so it does not date. The one
resolved conflict: the add-in is GA on Pro, Max, Team AND Enterprise (the old
2.8 script's "Pro plan and up" was wrong), and there is no documented
Ctrl+Alt+C. Both live on the card.

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
# Beats 1, 2, 3, 4, 6, 7 and 9 all read from these. Change one, move them all.
# ----------------------------------------------------------------------------
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
SPEND = [34200, 31800, 36500, 33100, 35900, 32400,
         30700, 29900, 37200, 38600, 36300, 35300]

WRONG_FORMULA = "=SUM(B2:B12)"      # stops one row short - Jan to Nov
GOOD_RANGE = "B2:B13"               # all twelve months - planted on beat 3
WRONG_TOTAL = sum(SPEND[:11])       # 376,600 - the number that travels
TRUE_TOTAL = sum(SPEND)             # 411,900
MISSED = SPEND[-1]                  # 35,300 - December, the row outside the range

# the worked example must stay arithmetically true if anyone edits SPEND
assert WRONG_TOTAL == 376600 and TRUE_TOTAL == 411900 and MISSED == 35300
assert WRONG_TOTAL + MISSED == TRUE_TOTAL


def money(n):
    return f"{n:,}"


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


def doodle_clean(x, y, accent):
    mini_sheet(x, y, 110, 120, INDIGO_BG, rows=4, ragged=True)
    arrow(x + 122, y + 60, [[0, 0], [40, 0]], stroke=accent, sw=3, rough=1)
    mini_sheet(x + 174, y, 110, 120, INDIGO_BG, rows=4, cols=3)


def doodle_error(x, y, accent):
    """Tracing a #REF! back to its cause. The "#REF!" literal is RED on an indigo
    beat on purpose - a spreadsheet error IS red, and the contrast is load-bearing:
    beat 5 shows the LOUD errors Claude is genuinely good at finding, so that beat 6
    can be the one with no red anywhere on the sheet."""
    mini_sheet(x, y, 284, 120, INDIGO_BG, rows=4, cols=4)
    text(x + 196, y + 30, "#REF!", size=SMALL, color=RED)
    arrow(x + 192, y + 46, [[0, 0], [-92, 40]], stroke=accent, sw=3, rough=1)
    text(x + 40, y + 88, "the cause", size=SMALL, color=accent)


def doodle_reshape(x, y, accent):
    rect(x, y + 34, 160, 52, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="wide")
    for c in range(1, 5):
        line(x + c * 32, y + 34, [[0, 0], [0, 52]], stroke=FAINT, sw=1)
    arrow(x + 172, y + 60, [[0, 0], [40, 0]], stroke=accent, sw=3, rough=1)
    rect(x + 224, y, 60, 120, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="tall")
    for r in range(1, 5):
        line(x + 224, y + r * 24, [[0, 0], [60, 0]], stroke=FAINT, sw=1)


def doodle_lookup(x, y, accent):
    mini_sheet(x, y + 18, 104, 104, INDIGO_BG, rows=3, cols=2)
    mini_sheet(x + 180, y, 104, 104, INDIGO_BG, rows=3, cols=2)
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
     "the failure here is a number nobody checked", size=H2, color=ORANGE)

# ============================================================================
# BEAT 1 - ORANGE - a number nobody checked
# ============================================================================
ox = beat_head(1, "a number nobody checked",
               "one figure leaves a spreadsheet, lands on a slide,\n"
               "and becomes a decision - unquestioned")

# station A - a cell
grid(ox + 40, 350, 320, 200, accent=ORANGE, abg=ORANGE_BG, rows=5, cols=4, hi=(2, 2))
text(ox + 40 + 2 * 80 + 7, 350 + 2 * 40 + 9, money(WRONG_TOTAL), size=SMALL, color=INK)
text(ox + 40, 572, "a cell in a sheet", size=SMALL, color=GREY)
arrow(ox + 378, 450, [[0, 0], [58, 0]], stroke=ORANGE, sw=4, rough=1)

# station B - a slide
rect(ox + 452, 360, 296, 180, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="slide")
text(ox + 472, 380, "Spend is under control", size=SMALL, color=INK)
text(ox + 472, 428, f"£{money(WRONG_TOTAL)}", size=H2, color=ORANGE)
text(ox + 472, 492, "- finance pack, slide 4", size=SMALL, color=GREY)
text(ox + 452, 572, "a line on a slide", size=SMALL, color=GREY)
arrow(ox + 766, 450, [[0, 0], [58, 0]], stroke=ORANGE, sw=4, rough=1)

# station C - a decision
rect(ox + 840, 360, 280, 180, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="dec")
text(ox + 864, 386, "renew the\ncontract", size=H3, color=INK)
tick(ox + 864, 476, GREEN, s=28, sw=4)
text(ox + 916, 478, "approved", size=SMALL, color=GREEN)
text(ox + 840, 572, "a decision, made", size=SMALL, color=GREY)

text(ox + 40, 644, "nothing in this chain asks where it came from", size=H2, color=ORANGE)
text(ox + 40, 726,
     "Every other tool in this course fails where you can see it. A deck that says nothing\n"
     "looks like a deck that says nothing. A spreadsheet fails differently: a plausible\n"
     "number, sitting in a cell, that nobody queries - and then it travels.",
     size=BODY, color=GREYD)
chip(ox + 40, 856, "the whole day is one habit: check one row",
     fill=ORANGE_T, text_color=ORANGE, border=ORANGE)

# ============================================================================
# BEAT 2 - VIOLET - it edits the live sheet
# ============================================================================
ox = beat_head(2, "it edits the live sheet",
               "the changes land in the workbook you have open -\n"
               "not in a copy it made for you")

q4 = [("Sep", money(SPEND[8])), ("Oct", money(SPEND[9])), ("Nov", money(SPEND[10])),
      ("Dec", money(SPEND[11])), ("Q4 total", money(sum(SPEND[9:])))]
g2 = ledger(ox + 40, 330, 520, q4, VIOLET_BG, ("Month", "Spend  £"))
for _r in (3, 5, 6):
    _cx, _cy, _cw, _ch = cell_box(g2, 1, _r)
    rect(_cx + 3, _cy + 3, _cw - 6, _ch - 6, stroke=VIOLET, bg="transparent",
         sw=3, rough=1, rounded=False, prefix="chg")
text(ox + 40, 648, "three cells changed, in the file you already had open",
     size=SMALL, color=VIOLET)

text(ox + 604, 336, "the same file you had open.\nit warns you before it overwrites,\n"
                    "and asks you to confirm anything risky.", size=BODY, color=GREYD)
chip(ox + 604, 452, "work on a duplicate the first few times",
     fill=VIOLET_T, text_color=VIOLET, border=VIOLET)

text(ox + 40, 706, "undo reaches", size=H3, color=VIOLET)
check_item(ox + 40, 762, "the edit you just watched land", accent=VIOLET)
check_item(ox + 40, 812, "this workbook, while it is still open", accent=VIOLET)

text(ox + 604, 706, "undo does not reach", size=H3, color=GREYD)
for _k, _s in enumerate(["the version you already saved and sent",
                         "the figure already pasted into a deck",
                         "the decision someone made on it"]):
    xmark(ox + 604, 766 + _k * 50, GREY, s=20, sw=4)
    text(ox + 650, 762 + _k * 50, _s, size=BODY, color=GREYD)

text(ox + 40, 930, "Undo is a safety net for the file. The chain on the last beat is not in the file.",
     size=BODY, color=GREYD)

# ============================================================================
# BEAT 3 - BLUE - ask for the formula, not the answer
# ============================================================================
ox = beat_head(3, "ask for the formula, not the answer",
               "the same question, asked two ways -\n"
               "only one of the replies can be checked")

sticky(ox + 40, 330, 520, 330, FAINT, angle=jit(0.8))
text(ox + 72, 356, "you ask", size=SMALL, color=GREY)
text(ox + 72, 388, "“what’s our average\nmonthly spend?”", size=BODY, color=INK)
text(ox + 72, 480, "you get", size=SMALL, color=GREY)
text(ox + 72, 512, f"“Your average monthly\nspend is £{money(round(TRUE_TOTAL / 12))}.”",
     size=H3, color=INK)
text(ox + 72, 602, "you can agree with it, or disagree\nwith it. that is the whole menu.",
     size=SMALL, color=GREYD)

sticky(ox + 600, 330, 520, 330, BLUE_T, angle=jit(0.8))
text(ox + 632, 356, "you ask", size=SMALL, color=BLUE)
text(ox + 632, 388, "“give me the formula, and\nthe range it covers”", size=BODY, color=INK)
text(ox + 632, 480, "you get", size=SMALL, color=BLUE)
text(ox + 632, 512, f"=AVERAGE({GOOD_RANGE})", size=H3, color=BLUE)
text(ox + 632, 556, "column B, rows 2 to 13 -\nall twelve months", size=BODY, color=INK)
text(ox + 632, 630, "you can read it. you can check it.", size=SMALL, color=BLUE)

chip(ox + 40, 706, "a formula is inspectable, an answer is not",
     fill=BLUE_T, text_color=BLUE, border=BLUE)
text(ox + 40, 800,
     "This costs you nothing. Ask for both - the number, and the formula that made it -\n"
     "and you have turned a claim into something you can audit in ten seconds.",
     size=BODY, color=GREYD)
text(ox + 40, 906, f"Twelve months of data live in {GOOD_RANGE}. Worth remembering.",
     size=BODY, color=BLUE)

# ============================================================================
# BEAT 4 - TEAL - describe the sheet first
# ============================================================================
ox = beat_head(4, "describe the sheet first",
               "three sentences before you ask it anything -\n"
               "it cannot see what you already know")

BUDGET = 33000
h1 = [(MONTHS[i], money(SPEND[i]), money(BUDGET),
       ("+" if SPEND[i] >= BUDGET else "-") + money(abs(SPEND[i] - BUDGET)))
      for i in range(6)]
g4 = ledger(ox + 40, 330, 600, h1, TEAL_BG, ("Month", "Spend", "Budget", "Over/under"))

text(ox + 700, 352, "a row is one month", size=BODY, color=TEAL)
arrow(ox + 692, 364, [[0, 0], [-58, 44]], stroke=TEAL, sw=2, rough=1)
text(ox + 700, 472, f"the data runs {GOOD_RANGE}", size=BODY, color=TEAL)
arrow(ox + 692, 484, [[0, 0], [-402, 16]], stroke=TEAL, sw=2, rough=1)
text(ox + 700, 592, "“Over/under” is worked out,\nnot typed", size=BODY, color=TEAL)
text(ox + 40, 676, "(rows 8 to 13 carry on below - Jul to Dec)", size=SMALL, color=GREY)
arrow(ox + 692, 604, [[0, 0], [-72, 30]], stroke=TEAL, sw=2, rough=1)

sticky(ox + 40, 720, 1080, 200, TEAL_T, angle=jit(0.8))
text(ox + 72, 744, "what to type before your first question:", size=SMALL, color=TEAL)
text(ox + 72, 784,
     "“Each row is one month. The spend figures are column B, rows 2 to 13.\n"
     "The last column is worked out from the two before it - do not overwrite it.”",
     size=BODY, color=INK)
chip(ox + 40, 930, "set it once in the add-in\u2019s Instructions, not every chat",
     fill=TEAL_T, text_color=TEAL, border=TEAL)
text(ox + 40, 996, "It will guess if you do not tell it. It guesses well, which is the problem.",
     size=BODY, color=GREYD)

# ============================================================================
# BEAT 5 - INDIGO - what it is genuinely good at
# ============================================================================
ox = beat_head(5, "what it is genuinely good at",
               "no hype - four jobs where it reliably beats\n"
               "doing it by hand")

jobs = [(doodle_clean, "clean a messy export",
         "split the columns, fix the dates,\nstrip the blank rows"),
        (doodle_error, "find what is broken",
         "trace a #REF! back to the cell\nthat caused it, across tabs"),
        (doodle_lookup, "look up across sheets",
         "match on a key - and tell you which\nrows did not match"),
        (doodle_explain, "explain a formula",
         "read back what someone else’s\nnested formula actually does")]
for k, (doodle, head, cap) in enumerate(jobs):
    jx = ox + 40 + (k % 2) * 560
    jy = 330 + (k // 2) * 322
    doodle(jx + 8, jy, INDIGO)
    text(jx, jy + 152, head, size=H3, color=INDIGO)
    text(jx, jy + 202, cap, size=BODY, color=GREYD)

text(ox + 40, 986, "Notice what is not on this list: deciding whether the answer is right.",
     size=BODY, color=INDIGO)

# ============================================================================
# BEAT 6 - RED - a formula that looks right   *** THE ADVERSARIAL HERO ***
# Nothing on the sheet is flagged. The marquee is a SELECTION, not a warning.
# ============================================================================
ox = beat_head(6, "a formula that looks right",
               "everything on this sheet is well-formed. nothing is flagged.\n"
               "one number on it is wrong.")

rows6 = [(MONTHS[i], money(SPEND[i])) for i in range(12)]
g6 = ledger(ox + 50, 310, 560, rows6, FAINT, ("Month", "Spend  £"), row_h=46)
marquee(g6, 1, 2, 12)                      # B2:B12 - eleven of the twelve rows
_mx, _my, _mw, _mh = cell_box(g6, 1, 2)
text(ox + 620, _my + 5.5 * g6["row_h"], "B2:B12", size=SMALL, color=BLUE)

text(ox + 700, 330, "what Claude wrote", size=SMALL, color=GREY)
text(ox + 700, 368, WRONG_FORMULA, size=H1, color=BLUE)
text(ox + 700, 460, "what it returned", size=SMALL, color=GREY)
text(ox + 700, 498, f"£{money(WRONG_TOTAL)}", size=H1, color=INK)

text(ox + 700, 594,
     "It ran without an error. It is a valid formula.\n"
     "It is formatted correctly. Nobody flagged it.\n"
     "It is also wrong, and the sheet will never say so.",
     size=BODY, color=GREYD)
text(ox + 700, 718, "Take ten seconds. Where is it wrong?", size=H3, color=RED)

sticky(ox + 700, 790, 840, 170, RED_T, angle=jit(0.7))
text(ox + 732, 814, "the catch", size=SMALL, color=RED)
text(ox + 732, 850,
     "Recompute one row by hand - and check the row you\n"
     "picked is inside the range. Pick the last one.",
     size=BODY, color=INK)

# ============================================================================
# BEAT 7 - YELLOW - check one row by hand   (the catch for beat 6)
# ============================================================================
ox = beat_head(7, "check one row by hand",
               "the entire discipline is one row, on paper,\n"
               "before the number leaves the sheet")

rect(ox + 40, 340, 420, 72, stroke=YELLOW, bg=YELLOW_T, sw=3, rough=1,
     rounded=True, prefix="lifted")
text(ox + 62, 358, "13", size=SMALL, color=GREY)
text(ox + 116, 356, MONTHS[-1], size=BODY, color=INK)
text(ox + 290, 356, money(MISSED), size=BODY, color=INK)
text(ox + 40, 434, "the row you picked -\nthe last one", size=SMALL, color=GREYD)

sticky(ox + 520, 330, 600, 250, YELLOW_T, angle=jit(0.8))
text(ox + 552, 352, "on paper: is your row in the total?", size=SMALL, color=YELLOW)
text(ox + 552, 388, f"{money(WRONG_TOTAL)}  +  {money(MISSED)}", size=H2, color=INK)
line(ox + 552, 444, [[0, 0], [300, 0]], stroke=GREYD, sw=2)
text(ox + 552, 456, f"= {money(TRUE_TOTAL)}", size=H2, color=INK)
text(ox + 552, 516, f"what the sheet says:  £{money(WRONG_TOTAL)}", size=BODY, color=RED)

human_gate(ox + 100, 700, GREEN)
text(ox + 180, 646, "you", size=H3, color=GREEN)
text(ox + 180, 694, "not Claude. Claude wrote the formula -\n"
                    "it cannot also be the thing that checks it.", size=BODY, color=GREYD)

chip(ox + 40, 810, "one row, every time, before it leaves the sheet",
     fill=YELLOW_T, text_color=YELLOW, border=YELLOW)
text(ox + 40, 906,
     "You are not auditing the sheet. You are checking that the row you picked is\n"
     "inside the range - which is exactly why you pick the last one.",
     size=BODY, color=GREYD)

# ============================================================================
# BEAT 8 - GREEN - audit, do not just build
# ============================================================================
ox = beat_head(8, "audit, do not just build",
               "the higher-value ask: point it at a model\n"
               "someone else built, and ask what breaks")

paper_stack(ox + 40, 350, 330, 280, GREEN_BG, n=3)
mini_sheet(ox + 40, 350, 330, 280, GREEN_BG, rows=6, cols=4)
text(ox + 40, 680, "built by someone who has left.\nstill used every week.", size=SMALL, color=GREYD)

for k, q in enumerate(["what breaks if this number doubles?",
                       "what is hard-coded that should be a reference?",
                       "what assumes this sheet never gets another row?"]):
    qy = 344 + k * 116
    sticky(ox + 460, qy, 660, 96, GREEN_T, angle=jit(1.2))
    text(ox + 492, qy + 30, q, size=BODY, color=INK)

text(ox + 40, 762, "A ready-made auditing Skill ships with it - type / in the sidebar.",
     size=BODY, color=GREEN)
text(ox + 40, 830,
     "Building a new sheet is the obvious ask. Auditing an old one is worth more,\n"
     "because the old one is already making decisions.",
     size=BODY, color=GREYD)
chip(ox + 40, 926, "the sheets already in use are the ones worth checking",
     fill=GREEN_T, text_color=GREEN, border=GREEN)

# ============================================================================
# BEAT 9 - ORANGE - do it live   (demo, pause-and-try, the red rule, the close)
# ============================================================================
ox = beat_head(9, "do it live",
               "one workbook, built or audited -\n"
               "and one row verified by hand")

demo_badge(ox + 40, 326,
           "show in Claude desktop app: ask for the formula, then break the range on purpose")
text(ox + 40, 404, "- and see whether the check catches it.", size=BODY, color=ORANGE)

for k, s in enumerate(["ask for the total, and the formula that made it",
                       "add a row below the range, without saying so",
                       "recompute that row by hand, and compare"]):
    sy = 466 + k * 70
    num_badge(ox + 40, sy, k + 1, ORANGE)
    text(ox + 104, sy + 6, s, size=BODY, color=INK)

pause_icon(ox + 44, 706, 32, ORANGE)
text(ox + 104, 698, "pause here, and try it", size=H3, color=ORANGE)
text(ox + 104, 746, "Open a sheet an AI touched this month, and recompute a single row yourself.",
     size=BODY, color=INK)

rect(ox + 40, 820, 1080, 152, stroke=RED, bg=RED_T, sw=2, rough=1, rounded=True, prefix="rule")
text(ox + 72, 842, "before you paste anything in", size=H3, color=RED)
text(ox + 72, 892,
     "A workbook from outside is a file from outside - it can carry instructions.\n"
     "Never put confidential or personal data into a sheet you are going to share.",
     size=BODY, color=INK)

text(ox + 40, 1000, "One row, every time, before it leaves the sheet.", size=H3, color=INK)

# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "claude-excel.excalidraw")
finish(out, MAX_TEXT_W, TOTAL_W)
