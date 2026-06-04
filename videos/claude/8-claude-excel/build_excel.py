#!/usr/bin/env python3
"""Build claude-excel.excalidraw - ONE flowing, illustrated explainer for the
"Claude + Excel" training video (Phlo AI Ops Learn, module 2.8).

House Style B (see excalidraw_kit): one hand-drawn left-to-right journey, no
frames, white canvas, the hand font, lively colour-coded palette. This file holds
only the composition + a couple of one-off illustrations (a spreadsheet grid).

Sibling to the PowerPoint (2.7) and Word (2.9) file-type videos. To stop the three
reading as copy-paste, THIS one's angle is what's unique to spreadsheets: live
FORMULA relationships - Claude answers about your actual cells with citations,
changes an assumption and every dependent cell recomputes, and traces broken
references across tabs. Two real capabilities, kept distinct: (1) "Create and edit
files with Claude" - the chat builds a genuine downloadable .xlsx, all plans;
(2) "Claude for Excel" - the add-in that lives in Excel's Home ribbon (Pro+).

Run:  python3 videos/claude/8-claude-excel/build_excel.py
      python3 preview.py videos/claude/8-claude-excel/claude-excel.excalidraw out.png
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
# BEAT SCAFFOLD  (9 beats, uniform slots, wide gaps - the whitespace is the camera)
# ----------------------------------------------------------------------------
N = 9
GAP = 800
WID = {i: 1200 for i in range(1, N + 1)}
ACCENT = {1: GREEN, 2: BLUE, 3: ORANGE, 4: GREEN, 5: TEAL,
          6: INDIGO, 7: VIOLET, 8: ORANGE, 9: GREEN}
OX = {}
_c = 0
for _i in range(1, N + 1):
    OX[_i] = _c
    _c += WID[_i] + GAP
TOTAL_W = _c
HEAD_Y = 60


def beat_head(i, title, sub=None):
    ox = OX[i]
    heading(ox, HEAD_Y, title, color=ACCENT[i], sub=sub)
    return ox


# ----------------------------------------------------------------------------
# LOCAL ONE-OFF ILLUSTRATIONS
# ----------------------------------------------------------------------------
def grid(x, y, w, h, accent=GREEN, abg=GREEN_BG, rows=5, cols=5, hi=None):
    """A spreadsheet grid: tinted header row + row-header column, faint gridlines,
    optional highlighted cell at hi=(col,row)."""
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


def tiny_sheet(x, y):
    grid(x, y, 180, 120, accent=GREEN, abg=GREEN_BG, rows=4, cols=4, hi=(2, 2))


def src_card(x, y, label, accent, abg):
    w, h = 250, 96
    sticky(x, y, w, h, abg, angle=jit(1.6))
    grid(x + 16, y + 22, 48, 52, accent=accent, abg=abg, rows=3, cols=3)
    text(x + 82, y + 36, label, size=SMALL, color=accent, width=w - 98)
    return w, h


def magnifier(cx, cy, r=34, color=ORANGE):
    ellipse(cx - r, cy - r, 2 * r, 2 * r, stroke=color, bg="transparent", sw=4, rough=1, prefix="mag")
    line(cx + r * 0.7, cy + r * 0.7, [[0, 0], [26, 26]], stroke=color, sw=5, rough=1, prefix="maghdl")


# ============================================================================
# BOARD TITLE
# ============================================================================
text(OX[1], -300, "Claude + Excel", size=HERO, color=INK)
text(OX[1] + 6, -300 + HERO * LINE_H + 4,
     "a spreadsheet helper that keeps your formulas alive", size=H2, color=GREEN)

# ============================================================================
# BEAT 1 - HOOK
# ============================================================================
ox = beat_head(1, "It works inside your spreadsheet",
               "not a chatbot you copy numbers into - a helper that\nreads the actual cells")
by = 360
bw, bh = 520, 130
sticky(ox + 40, by, bw, bh, GREY, angle=jit(1.5))
text(ox + 72, by + 34, "walk me through this\nworkbook", size=BODY, color=WHITE)
line(ox + 90, by + bh, [[0, 0], [-18, 30], [22, -2]], stroke=GREY, sw=3)
arrow(ox + 40 + bw + 30, by + bh / 2, [[0, 0], [150, 0]], stroke=GREEN, sw=5, rough=1)
gx = ox + 40 + bw + 230
ellipse(gx - 40, by - 30, 320, 240, stroke=GREEN, bg=GREEN_BG, sw=2, rough=1, fill="solid", opacity=45)
grid(gx, by, 260, 180, accent=GREEN, abg=GREEN_BG, rows=5, cols=5, hi=(3, 2))
text(gx + 10, by + 196, "it answers about your real\ncells - and cites them", size=SMALL, color=GREEN)

# ============================================================================
# BEAT 2 - A REAL SPREADSHEET
# ============================================================================
ox = beat_head(2, "A real spreadsheet, not a screenshot",
               "Ask in the chat and Claude builds a genuine .xlsx -\n"
               "to download or save to Drive, formulas and all.")
cw_x, cw_y, cw_w, cw_h = ox + 40, 330, 1080, 560
claude_window(cw_x, cw_y, cw_w, cw_h, tiny=tiny_sheet)
text(cw_x, cw_y + cw_h + 24, "you ask in the chat", size=SMALL, color=GREY)
arrow(cw_x + cw_w * 0.74, cw_y + cw_h + 56, [[0, 0], [70, -60]], stroke=BLUE, sw=3, rough=1)
text(cw_x + cw_w * 0.55, cw_y + cw_h + 60,
     "opens in Excel or Google Sheets -\nworking formulas, not flat values", size=SMALL, color=BLUE)
chx = cw_x
for lab in ["every plan", "web, desktop & mobile"]:
    w, _ = chip(chx, cw_y + cw_h + 110, lab, fill=WHITE, text_color=BLUE, border=BLUE, size=SMALL)
    chx += w + 30

# ============================================================================
# BEAT 3 - START FROM A WORKBOOK YOU INHERITED
# ============================================================================
ox = beat_head(3, "Start from the mess you inherited",
               "Point Claude at a workbook nobody understands\nand ask it to explain itself.")
sx, sy = ox + 40, 340
srcs = [("a model you inherited", INDIGO, INDIGO_BG),
        ("a raw CSV export", BLUE, BLUE_BG),
        ("a template to fill", GREEN, GREEN_BG)]
for k, (lab, acc, abg) in enumerate(srcs):
    src_card(sx, sy + k * 120, lab, acc, abg)
face_x, face_y = sx + 360, sy + 180
claude_face(face_x, face_y, r=46, color=ORANGE)
text_centered(face_x, face_y + 86, "Claude", size=SMALL, color=GREYD)
for k in range(3):
    arrow(sx + 256, sy + 48 + k * 120, [[0, 0], [face_x - 46 - (sx + 256), face_y - (sy + 48 + k * 120)]],
          stroke=GREY, sw=2, rough=1)
arrow(face_x + 56, face_y, [[0, 0], [120, 0]], stroke=ORANGE, sw=4)
sticky(face_x + 190, face_y - 70, 360, 150, ORANGE_BG, angle=jit(1.2))
text(face_x + 214, face_y - 44, "“this tab is the\nrevenue model; B7 feeds\nevery quarter total”", size=SMALL, color=INK)

# ============================================================================
# BEAT 4 - IT KEEPS THE FORMULAS ALIVE  (the distinctive bit)
# ============================================================================
ox = beat_head(4, "It keeps the formulas alive",
               "Change one assumption and every dependent cell\nrecomputes - it edits the model, not just the number.")
grid(ox + 60, 340, 360, 240, accent=GREEN, abg=GREEN_BG, rows=6, cols=4, hi=(1, 1))
text(ox + 70, 588, "change an input here...", size=SMALL, color=GREEN)
arrow(ox + 440, 460, [[0, 0], [120, 0]], stroke=GREEN, sw=4)
grid(ox + 580, 340, 360, 240, accent=GREEN, abg=GREEN_BG, rows=6, cols=4, hi=(3, 5))
text(ox + 590, 588, "...the totals down here\nupdate themselves", size=SMALL, color=GREEN)
# the point chips
for k, lab in enumerate(["formulas reference the right cells, not frozen numbers",
                         "every change is highlighted and explained",
                         "answers cite the exact cell, across tabs"]):
    chip(ox + 60, 660 + k * 84, lab, fill=WHITE, text_color=GREEN, border=GREEN, size=SMALL)

# ============================================================================
# BEAT 5 - TWO PLACES IT WORKS
# ============================================================================
ox = beat_head(5, "From the chat, or in the ribbon",
               "Build a fresh sheet by asking - or open the add-in\non the workbook you've already got open.")
# left: build a fresh .xlsx from the chat
sticky(ox + 40, 340, 440, 360, TEAL_BG, angle=jit(-1.0))
text(ox + 78, 366, "From the chat", size=H3, color=TEAL)
text(ox + 78, 424, "describe it, get a fresh\n.xlsx built from scratch", size=BODY, color=INK)
grid(ox + 130, 524, 270, 150, accent=TEAL, abg=TEAL_BG, rows=4, cols=5, hi=(2, 2))
# right: the add-in in the Home ribbon, on the open sheet
rx = ox + 540
text(rx, 346, "In the Home ribbon", size=H3, color=INDIGO)
rect(rx, 404, 560, 56, stroke=INDIGO, bg=INDIGO_T, sw=2, rough=1, rounded=True, prefix="ribbon")
for k in range(6):
    rect(rx + 16 + k * 70, 416, 56, 32, stroke=GREYD, bg=WHITE, sw=1, rough=1, rounded=True, prefix="rbtn")
rect(rx + 16 + 6 * 70, 414, 96, 36, stroke=INDIGO, bg=INDIGO, sw=2, rough=1, rounded=True, prefix="rclaude")
text(rx + 16 + 6 * 70 + 14, 420, "Claude", size=SMALL, color=WHITE)
grid(rx, 480, 560, 220, accent=INDIGO, abg=INDIGO_BG, rows=6, cols=6, hi=(3, 2))
text(rx, 716, "Pro and up · Ctrl+Alt+C to open", size=SMALL, color=GREYD)

# ============================================================================
# BEAT 6 - IT FINDS WHAT'S BROKEN
# ============================================================================
ox = beat_head(6, "It finds what's broken",
               "A broken reference cascades. Claude traces it and\nshows every cell it touched - you choose the fix.")
grid(ox + 60, 340, 420, 280, accent=RED, abg=RED_BG, rows=6, cols=5, hi=(2, 1))
# the error spreads - mark a few cells
for cc, rr in [(2, 1), (3, 3), (1, 4)]:
    cwc, chc = 420 / 5, 280 / 6
    text(ox + 60 + cc * cwc + 8, 340 + rr * chc + 6, "#REF!", size=SMALL, color=RED)
text(ox + 60, 636, "one broken cell, three knock-on errors", size=SMALL, color=RED)
asks = ["where does this #REF come from?",
        "trace what the Q4 total depends on",
        "build a headcount model from these assumptions",
        "populate this template with the new data"]
for k, a in enumerate(asks):
    chip(ox + 560, 350 + k * 84, a, fill=WHITE, text_color=INDIGO, border=INDIGO, size=SMALL)
demo_badge(ox + 60, 700, "show in Excel:  'walk me through this workbook', then fix a #REF")

# ============================================================================
# BEAT 7 - WHERE IT EARNS ITS KEEP  (a vertical list with grid icons)
# ============================================================================
ox = beat_head(7, "The jobs it's best at")
jobs = [("Understand a handover", "explain a sheet you didn't build", ORANGE, ORANGE_BG),
        ("Build a quick model", "headcount, a budget, a forecast", GREEN, GREEN_BG),
        ("Sanity-check the maths", "find the broken or wrong cells", BLUE, BLUE_BG),
        ("Clean a data dump", "tidy a CSV, then summarise it", VIOLET, VIOLET_BG)]
for k, (head, cap, acc, abg) in enumerate(jobs):
    yy = 340 + k * 124
    grid(ox + 60, yy, 92, 92, accent=acc, abg=abg, rows=3, cols=3, hi=(1, 1))
    text(ox + 184, yy + 12, head, size=H3, color=acc)
    text(ox + 184, yy + 62, cap, size=BODY, color=INK)

# ============================================================================
# BEAT 8 - SAFETY  (a 'check the numbers' magnifier, not a caution box)
# ============================================================================
ox = beat_head(8, "Trust the model, check the numbers")
grid(ox + 60, 340, 420, 300, accent=ORANGE, abg=ORANGE_BG, rows=6, cols=5, hi=(2, 3))
magnifier(ox + 60 + 2.5 * (420 / 5), 340 + 3.5 * (300 / 6), r=40, color=ORANGE)
text(ox + 60, 668, "check the figures before they drive a decision", size=SMALL, color=ORANGE)
# two notes on the right - no red diamond
nx = ox + 560
rect(nx, 340, 520, 150, stroke=ORANGE, bg=ORANGE_T, sw=2, rough=1, rounded=True)
text(nx + 32, 362, "Where it can bite", size=H3, color=ORANGE)
text(nx + 32, 416, "an untrusted workbook can hijack the\nrequest - don't open files you don't trust", size=BODY, color=INK)
rect(nx, 510, 520, 150, stroke=GREEN, bg=GREEN_T, sw=2, rough=1, rounded=True)
text(nx + 32, 532, "What you still own", size=H3, color=GREEN)
text(nx + 32, 586, "Claude does the legwork; you own the\nnumbers - especially finance or regulated", size=BODY, color=INK)

# ============================================================================
# BEAT 9 - TRY / CLOSE  (a workbook + 'walk me through this' bubble)
# ============================================================================
ox = beat_head(9, "Try it on a sheet you didn't build")
grid(ox + 60, 340, 380, 250, accent=GREEN, abg=GREEN_BG, rows=5, cols=5, hi=(2, 2))
sticky(ox + 480, 380, 460, 150, GREEN_BG, angle=jit(1.4))
text(ox + 512, 410, "“walk me through\nthis workbook”", size=H3, color=INK)
line(ox + 480, 470, [[0, 0], [-34, 14], [0, 26]], stroke=GREEN, sw=3)  # bubble tail
ex_x = ox + 60
for lab in ["a budget tracker", "a forecast model", "a messy data export"]:
    w, h = chip(ex_x, 636, lab, fill=WHITE, text_color=GREEN, border=GREEN, size=SMALL)
    ex_x += w + 32
text(ox + 60, 724, "let it explain the sheet - then change one assumption and watch it update", size=BODY, color=GREYD)
text(ox + 40, 784, "Claude keeps your formulas alive - you keep the final say on the numbers.",
     size=H3, color=INK)
text(ox + 60, 876, "Docs: Claude - Create and edit files, and Use Claude for Excel", size=SMALL, color=VIOLET)

# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "claude-excel.excalidraw")
finish(out, max(WID.values()) + 200, TOTAL_W)
