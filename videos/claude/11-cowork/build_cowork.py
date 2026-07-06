#!/usr/bin/env python3
"""Build claude-cowork.excalidraw - ONE flowing, illustrated explainer for the
"Claude Cowork" training video (Phlo AI Ops Learn, module 2.11).

House Style B (see excalidraw_kit): one hand-drawn left-to-right journey, no
frames, white canvas, the hand font, lively palette. Composition + a few one-off
illustrations (a monitor, folders, file icons, a finished deliverable) live here.

Cowork is agentic KNOWLEDGE WORK on the desktop: you give a goal, Claude works
across your local files, folders and apps, and returns a FINISHED deliverable -
it's not a chat assistant. Human oversight is the spine: consequential decisions
stay with you. All paid plans, in the Claude desktop app. So, like the Chrome
video, the shape is "power then control": beat 3 is goal->deliverable, beat 5 is
the oversight model, beat 8 is the scoped-access safety beat.

Run:  python3 videos/claude/11-cowork/build_cowork.py
      python3 preview.py videos/claude/11-cowork/claude-cowork.excalidraw out.png
"""
import os
import sys

_d = os.path.dirname(os.path.abspath(__file__))
while _d != os.path.dirname(_d) and not os.path.exists(os.path.join(_d, "excalidraw_kit.py")):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)

import random
from excalidraw_kit import *

random.seed(111110)

N = 9
GAP = 800
WID = {i: 1200 for i in range(1, N + 1)}
ACCENT = {1: VIOLET, 2: BLUE, 3: ORANGE, 4: GREEN, 5: TEAL,
          6: INDIGO, 7: YELLOW, 8: GREEN, 9: VIOLET}
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
def folder(x, y, w=96, h=70, accent=YELLOW, abg=YELLOW_BG):
    rect(x, y + 14, w, h, stroke=INK, bg=abg, sw=2, rough=1, rounded=True, prefix="fold")
    rect(x, y, w * 0.5, 22, stroke=INK, bg=abg, sw=2, rough=1, rounded=True, prefix="foldtab")


def deliverable(x, y, accent=GREEN, abg=GREEN_BG):
    """A finished one-pager with a green tick badge."""
    rect(x, y, 150, 196, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="del")
    rect(x + 18, y + 22, 90, 14, stroke="transparent", bg=accent, sw=1, rough=1, rounded=True, prefix="deltt")
    for k in range(5):
        line(x + 18, y + 58 + k * 22, [[0, 0], [(96 if k % 2 else 70), 0]], stroke=GREY, sw=2)
    ellipse(x + 108, y + 150, 54, 54, stroke=GREEN, bg=WHITE, sw=3)
    tick(x + 122, y + 164, color=GREEN, s=26, sw=5)


def monitor(x, y, w, h, accent=BLUE, abg=BLUE_BG):
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="mon")
    rect(x + 10, y + 10, w - 20, h - 20, stroke=GREY, bg=abg, sw=1, rough=1,
         rounded=True, fill="solid", opacity=30, prefix="monscr")
    rect(x + w / 2 - 34, y + h, 68, 20, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=False, prefix="monstand")
    rect(x + w / 2 - 80, y + h + 20, 160, 12, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="monbase")


# ============================================================================
# BOARD TITLE
# ============================================================================
text(OX[1], -300, "Claude Cowork", size=HERO, color=INK)
text(OX[1] + 6, -300 + HERO * LINE_H + 4,
     "hand over the whole task, not one question", size=H2, color=VIOLET)

# ============================================================================
# BEAT 1 - HOOK
# ============================================================================
ox = beat_head(1, "Give it the whole job",
               "not a chatbot you ask one thing at a time - a worker\nthat takes a task away and brings it back done")
by = 400
sticky(ox + 40, by, 360, 150, GREY, angle=jit(1.4))
text(ox + 70, by + 28, "“pull these five reports\ninto one summary”", size=BODY, color=WHITE)
arrow(ox + 420, by + 70, [[0, 0], [110, 0]], stroke=VIOLET, sw=5, rough=1)
claude_face(ox + 600, by + 60, r=50, color=VIOLET)
text_centered(ox + 600, by + 130, "Claude works", size=SMALL, color=GREYD)
arrow(ox + 670, by + 60, [[0, 0], [110, 0]], stroke=VIOLET, sw=5, rough=1)
deliverable(ox + 800, by - 30, accent=VIOLET, abg=VIOLET_BG)
text(ox + 790, by + 196, "a finished deliverable,\nnot a to-do list", size=SMALL, color=VIOLET)

# ============================================================================
# BEAT 2 - IT WORKS ON YOUR COMPUTER
# ============================================================================
ox = beat_head(2, "It works on your computer",
               "Cowork runs in the Claude desktop app, where the\nwork already is - your files, folders and apps.")
monitor(ox + 200, 340, 760, 420, accent=BLUE, abg=BLUE_BG)
folder(ox + 250, 400, accent=YELLOW, abg=YELLOW_BG)
folder(ox + 380, 400, accent=ORANGE, abg=ORANGE_BG)
file_icon(ox + 520, 396)
file_icon(ox + 600, 396, abg=GREEN_BG)
claude_face(ox + 800, 470, r=44, color=BLUE)
text(ox + 250, 600, "Claude moves between them, the way you would", size=BODY, color=GREYD)
chx = ox + 250
for lab in ["all paid plans", "Claude desktop app"]:
    w, _ = chip(chx, 660, lab, fill=WHITE, text_color=BLUE, border=BLUE, size=SMALL)
    chx += w + 28

# ============================================================================
# BEAT 3 - GOAL IN, DELIVERABLE OUT  (how it works)
# ============================================================================
ox = beat_head(3, "Goal in, deliverable out",
               "You set the goal once. Claude plans the steps and\nworks through them - you don't drive each one.")
steps = [("you set a goal", VIOLET, VIOLET_BG),
         ("Claude plans the steps", ORANGE, ORANGE_BG),
         ("works across files & apps", BLUE, BLUE_BG),
         ("hands back the result", GREEN, GREEN_BG)]
sx, sy = ox + 50, 380
for k, (lab, acc, abg) in enumerate(steps):
    w, h = chip(sx, sy, lab, fill=abg, text_color=INK, border=acc, size=BODY)
    if k < len(steps) - 1:
        arrow(sx + w + 8, sy + h / 2, [[0, 0], [44, 0]], stroke=acc, sw=4)
    sx += w + 56
text(ox + 50, sy + 130, "multi-step work, synthesised across several sources -", size=BODY, color=GREYD)
text(ox + 50, sy + 176, "you spend your time on the judgement, not the assembly", size=BODY, color=GREYD)

# ============================================================================
# BEAT 4 - IT USES YOUR REAL STUFF
# ============================================================================
ox = beat_head(4, "It uses your real material",
               "Local files, whole folders, the apps you use - Cowork\nreads across them and pulls one answer together.")
items = [("a folder of reports", folder, YELLOW, YELLOW_BG),
         ("loose files", file_icon, BLUE, BLUE_BG),
         ("the apps you use", None, VIOLET, VIOLET_BG)]
sx, sy = ox + 60, 360
for k, (lab, fn, acc, abg) in enumerate(items):
    yy = sy + k * 130
    sticky(sx, yy, 300, 104, abg, angle=jit(1.4))
    if fn is folder:
        folder(sx + 20, yy + 24, accent=acc, abg=abg)
    elif fn is file_icon:
        file_icon(sx + 28, yy + 18, abg=abg)
    else:
        rect(sx + 22, yy + 22, 80, 60, stroke=acc, bg=WHITE, sw=2, rough=1, rounded=True)
        ellipse(sx + 36, yy + 36, 12, 12, stroke=acc, bg=acc, sw=1)
    text(sx + 130, yy + 38, lab, size=SMALL, color=acc, width=160)
    # all three converge cleanly on Claude (no crossing X)
    arrow(sx + 310, yy + 52, [[0, 0], [130, (sy + 200) - (yy + 52)]],
          stroke=GREY, sw=2, rough=1)
claude_face(ox + 540, sy + 200, r=46, color=GREEN)
arrow(ox + 600, sy + 200, [[0, 0], [110, 0]], stroke=GREEN, sw=4)
deliverable(ox + 730, sy + 100, accent=GREEN, abg=GREEN_BG)
text(ox + 60, sy + 410, "synthesised into one finished thing - 'let Claude use your computer'", size=SMALL, color=GREYD)

# ============================================================================
# BEAT 5 - YOU STAY IN CHARGE  (oversight - signature)
# ============================================================================
ox = beat_head(5, "You stay in charge",
               "Cowork is built around human oversight - the\nconsequential decisions stay with you.")
stack = [("it completes the task...", BLUE, BLUE_BG),
         ("...but checks in on the big calls", TEAL, TEAL_BG),
         ("you review the deliverable", GREEN, GREEN_BG),
         ("steer or stop at any point", VIOLET, VIOLET_BG)]
for k, (lab, acc, abg) in enumerate(stack):
    yy = 330 + k * 110
    rect(ox + 60, yy, 760, 86, stroke=acc, bg=abg, sw=2, rough=1, rounded=True,
         fill="solid", opacity=40, angle=jit(0.7))
    ellipse(ox + 84, yy + 22, 40, 40, stroke=acc, bg=WHITE, sw=3)
    text_centered(ox + 104, yy + 28, str(k + 1), size=H3, color=acc)
    text(ox + 150, yy + 24, lab, size=H3, color=INK)

# ============================================================================
# BEAT 6 - WHAT YOU'D HAND IT
# ============================================================================
ox = beat_head(6, "Whole tasks you'd hand over",
               "Plain English in - a finished thing out.")
text(ox + 60, 320, "you say", size=H3, color=INDIGO)
text(ox + 800, 320, "you get back", size=H3, color=GREEN)
asks = ["pull these five reports into one summary",
        "tidy this folder and rename files by date",
        "draft the monthly update from these notes",
        "reconcile these two lists and flag the gaps"]
for k, a in enumerate(asks):
    yy = 384 + k * 96
    chip(ox + 60, yy, a, fill=WHITE, text_color=INDIGO, border=INDIGO, size=SMALL)
    arrow(ox + 700, yy + 22, [[0, 0], [80, 0]], stroke=GREEN, sw=3)
    rect(ox + 800, yy - 6, 58, 74, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="done")
    for i in range(3):
        line(ox + 812, yy + 14 + i * 12, [[0, 0], [34, 0]], stroke=GREY, sw=2)
    ellipse(ox + 842, yy + 44, 30, 30, stroke=GREEN, bg=WHITE, sw=2)
    tick(ox + 850, yy + 50, color=GREEN, s=16, sw=5)
demo_badge(ox + 60, 384 + len(asks) * 96 + 6,
           "show in Claude desktop:  Cowork turning a folder of notes into one summary")

# ============================================================================
# BEAT 7 - WHO IT'S FOR  (three people, not a grid)
# ============================================================================
ox = beat_head(7, "Who it's really for")
roles = [("Ops & support", "the assembly work\nbetween the thinking", ORANGE),
         ("Analysts & finance", "gather, reconcile\nand summarise", GREEN),
         ("Anyone with files", "documents and folders,\nevery day", BLUE)]
for k, (who, cap, acc) in enumerate(roles):
    cx = ox + 220 + k * 330
    person(cx, 450, acc)
    text_centered(cx, 500, who, size=H3, color=acc)
    text_centered(cx, 560, cap, size=BODY, color=GREYD)
text(ox + 60, 700, "not just developers - no code, no setup, just plain English", size=BODY, color=GREYD)

# ============================================================================
# BEAT 8 - SAFETY  (scope it to one folder; sign off - not a caution box)
# ============================================================================
ox = beat_head(8, "Scope it tight, then sign it off")
rect(ox + 60, 360, 520, 250, stroke=GREYD, bg=WHITE, sw=2, rough=1, rounded=True)
text(ox + 84, 374, "your whole computer", size=SMALL, color=GREY)
folder(ox + 96, 456, accent=GREY, abg=FAINT)
folder(ox + 220, 456, accent=GREY, abg=FAINT)
folder(ox + 420, 456, accent=GREY, abg=FAINT)
folder(ox + 340, 456, accent=GREEN, abg=GREEN_BG)
line(ox + 326, 446, [[0, 0], [128, 0], [128, 104], [0, 104], [0, 0]],
     stroke=GREEN, sw=3, rough=1, dashed=True, prefix="scope")
text(ox + 300, 566, "just this folder, for this task", size=SMALL, color=GREEN)
nx = ox + 620
rect(nx, 360, 460, 120, stroke=GREEN, bg=GREEN_T, sw=2, rough=1, rounded=True)
text(nx + 28, 380, "Scope it", size=H3, color=GREEN)
text(nx + 28, 432, "one folder for the task, not the whole machine", size=BODY, color=INK)
rect(nx, 500, 460, 120, stroke=GREYD, bg=FAINT, sw=2, rough=1, rounded=True)
text(nx + 28, 520, "Keep it clean", size=H3, color=GREYD)
text(nx + 28, 572, "confidential or patient data stays out unless approved", size=BODY, color=INK)
tick(nx + 28, 660, color=GREEN, s=28, sw=5)
text(nx + 72, 656, "and read the deliverable before it goes anywhere", size=BODY, color=INK)

# ============================================================================
# BEAT 9 - TRY / CLOSE  (a goal note -> a finished deliverable)
# ============================================================================
ox = beat_head(9, "Hand over one whole task")
sticky(ox + 60, 340, 560, 160, VIOLET_BG, angle=jit(1.3))
text(ox + 96, 366, "Try this", size=H3, color=VIOLET)
text(ox + 96, 426, "give it one whole task you'd\nnormally dread assembling", size=BODY, color=INK)
arrow(ox + 640, 420, [[0, 0], [70, 0]], stroke=VIOLET, sw=4)
deliverable(ox + 740, 350, accent=VIOLET, abg=VIOLET_BG)
ex_x = ox + 60
for lab in ["merge a few documents", "tidy a messy folder", "draft a recurring update"]:
    w, h = chip(ex_x, 560, lab, fill=WHITE, text_color=VIOLET, border=VIOLET, size=SMALL)
    ex_x += w + 30
text(ox + 60, 648, "point it at one folder, watch it work, then check the result", size=BODY, color=GREYD)
text(ox + 40, 708, "Cowork does the legwork - you keep the judgement calls.", size=H3, color=INK)
text(ox + 60, 800, "Docs: Claude - Get started with Claude Cowork, and Let Claude use your computer",
     size=SMALL, color=VIOLET)

# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "claude-cowork.excalidraw")
finish(out, max(WID.values()) + 200, TOTAL_W)
