#!/usr/bin/env python3
"""Build prompting-crispe-framework.excalidraw - ONE flowing, illustrated
explainer for Day 3 - Prompting & CRISPE Framework (the AI Training series).

House Style B (see excalidraw_kit): one hand-drawn left-to-right journey, NO
frames, white canvas, the hand font (fontFamily 1), roughness 1, a lively
palette colour-coded per beat. Composition + the one-off illustrations (crumpled
note, dial, quill, phone, microphone, monitor) live here; the look lives in the
kit.

SIX BEATS, each in its own 1200-wide slot with GAP = 800 of whitespace between
them. Style B has no frames - a literal Excalidraw frame is a hard Style-B guard
failure - so the beat slots ARE the "frames": you pan to one at a time and the
whitespace keeps its neighbours off-screen.

  1 orange  vague in, vague out - the one-liner on a crumpled note
  2 green   the same ask rebuilt as three sticky notes  [demo]
  3 violet  CRISPE as six dials, 3 x 2
  4 blue    fault-finder - symptom -> the dial that fixes it
  5 teal    set once, never repeat - Styles + preferences  [demo]
  6 yellow  capture by voice, shape at your desk

Recording: there is no animation any more, the camera IS the reveal. Pan
left-to-right, one beat per frame, ~3s of narration each; cut away to the Claude
desktop app on the two demo badges and come back to the same beat.

Run:  python3 videos/ai-training/3-prompting-crispe-framework/build_excalidraw.py
      python3 preview.py videos/ai-training/3-prompting-crispe-framework/prompting-crispe-framework.excalidraw out.png
"""
import os
import sys

_d = os.path.dirname(os.path.abspath(__file__))
while _d != os.path.dirname(_d) and not os.path.exists(os.path.join(_d, "excalidraw_kit.py")):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)

import math
import random
from excalidraw_kit import *

random.seed(30330)  # deterministic - re-runs produce identical files

# ----------------------------------------------------------------------------
# BEAT SCAFFOLD
# ----------------------------------------------------------------------------
N = 6
GAP = 800
WID = {i: 1200 for i in range(1, N + 1)}
ACCENT = {1: ORANGE, 2: GREEN, 3: VIOLET, 4: BLUE, 5: TEAL, 6: YELLOW}
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
def crumpled_note(x, y, w, h, accent, abg):
    """A screwed-up, smoothed-out note: ragged outline, a folded corner, and a
    couple of short creases low down (kept clear of the text on the note)."""
    pts = [[0, 22], [w * 0.17, 2], [w * 0.52, 14], [w * 0.80, 0], [w, 26],
           [w - 12, h * 0.50], [w, h - 18], [w * 0.68, h], [w * 0.40, h - 14],
           [w * 0.14, h - 2], [2, h - 28], [12, h * 0.52], [0, 22]]
    line(x, y, pts, stroke=INK, sw=2, rough=1, bg=abg, fill="solid", prefix="crumple")
    line(x + w - 78, y + 18, [[0, 0], [62, 10], [10, 50], [0, 0]],
         stroke=accent, sw=2, rough=1, prefix="fold")
    line(x + w * 0.08, y + h - 28,
         [[0, 0], [w * 0.11, -h * 0.09], [w * 0.24, -h * 0.02], [w * 0.34, -h * 0.11]],
         stroke=accent, sw=2, rough=1, prefix="crease")
    line(x + w * 0.54, y + h - 24,
         [[0, 0], [w * 0.10, -h * 0.10], [w * 0.22, -h * 0.01], [w * 0.32, -h * 0.10]],
         stroke=accent, sw=2, rough=1, prefix="crease")


def dial(cx, cy, frac, color, abg, r=34):
    """A sketched dial: face, three ticks over the top, needle set to `frac`
    (0 = swung low / left, 1 = swung high / right)."""
    ellipse(cx - r, cy - r, 2 * r, 2 * r, stroke=color, bg=abg, sw=3, rough=1, prefix="dial")
    for t in (0.0, 0.5, 1.0):
        th = math.radians(215 - t * 250)
        dx, dy = math.cos(th), -math.sin(th)
        line(cx + dx * (r + 6), cy + dy * (r + 6),
             [[0, 0], [dx * r * 0.28, dy * r * 0.28]], stroke=color, sw=2, prefix="tick")
    th = math.radians(215 - frac * 250)
    line(cx, cy, [[0, 0], [math.cos(th) * r * 0.74, -math.sin(th) * r * 0.74]],
         stroke=INK, sw=3, prefix="needle")
    ellipse(cx - r * 0.12, cy - r * 0.12, r * 0.24, r * 0.24, stroke=INK, bg=INK, sw=2, prefix="hub")


def quill(cx, cy, s, color, abg):
    """A feather pen: leaf-shaped vane, a shaft through it, barbs and an ink nib."""
    line(cx - s * 0.16, cy + s * 0.24,
         [[0, 0], [-s * 0.10, -s * 0.32], [s * 0.06, -s * 0.62], [s * 0.36, -s * 0.88],
          [s * 0.42, -s * 0.60], [s * 0.30, -s * 0.28], [0, 0]],
         stroke=color, sw=3, rough=1, bg=abg, fill="solid", prefix="vane")
    line(cx - s * 0.30, cy + s * 0.44, [[0, 0], [s * 0.64, -s * 0.90]],
         stroke=color, sw=3, rough=1, prefix="shaft")
    for k in range(3):
        bx = cx - s * 0.10 + k * s * 0.14
        by = cy + s * 0.10 - k * s * 0.20
        line(bx, by, [[0, 0], [-s * 0.12, -s * 0.05]], stroke=color, sw=2, prefix="barb")
    line(cx - s * 0.30, cy + s * 0.44,
         [[0, 0], [s * 0.11, -s * 0.05], [s * 0.06, -s * 0.15]], stroke=INK, sw=3, prefix="nib")


def person_big(cx, cy, color, abg, s=1.5):
    """An avatar silhouette: a head plus rounded shoulders. The kit's person() is
    sized for a crowd of tiny figures; this one has to hold its own next to the
    quill, so it lives here rather than in the kit."""
    r = 28 * s
    ellipse(cx - r, cy - 68 * s, 2 * r, 2 * r, stroke=color, bg=WHITE, sw=3,
            rough=1, prefix="head")
    line(cx - 56 * s, cy + 52 * s,
         [[0, 0], [0, -26 * s], [20 * s, -58 * s], [92 * s, -58 * s],
          [112 * s, -26 * s], [112 * s, 0]],
         stroke=color, sw=3, rough=1, bg=abg, fill="solid", prefix="shoulders")


def phone(x, y, w, h, abg):
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=3, rough=1, rounded=True, prefix="phone")
    rect(x + 14, y + 34, w - 28, h - 72, stroke=GREY, bg=abg, sw=1, rough=1,
         rounded=True, fill="solid", opacity=30, prefix="phonescr")
    line(x + w / 2 - 30, y + 18, [[0, 0], [60, 0]], stroke=GREY, sw=3, prefix="earp")
    rect(x + w / 2 - 40, y + h - 26, 80, 8, stroke=GREY, bg=GREY, sw=1, rough=1,
         rounded=True, prefix="homebar")


def mic_icon(cx, cy, s, color):
    """A sketched microphone: capsule, cradle, stand and base."""
    rect(cx - s * 0.28, cy - s * 0.6, s * 0.56, s * 0.8, stroke=color, bg=WHITE,
         sw=3, rough=1, rounded=True, prefix="mic")
    line(cx - s * 0.5, cy + s * 0.06,
         [[0, 0], [0, s * 0.16], [s * 0.22, s * 0.34], [s * 0.78, s * 0.34],
          [s, s * 0.16], [s, 0]], stroke=color, sw=3, prefix="cradle")
    line(cx, cy + s * 0.44, [[0, 0], [0, s * 0.3]], stroke=color, sw=3, prefix="stand")
    line(cx - s * 0.3, cy + s * 0.76, [[0, 0], [s * 0.6, 0]], stroke=color, sw=3, prefix="base")


def squiggle(x, y, w, color, amp=18, waves=4.0, sw=3):
    """A hand-drawn voice squiggle."""
    steps = 44
    pts = [[t / steps * w, math.sin(t / steps * math.pi * waves) * amp] for t in range(steps + 1)]
    line(x, y, pts, stroke=color, sw=sw, rough=1, prefix="squig")


def monitor(x, y, w, h, abg):
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=3, rough=1, rounded=True, prefix="mon")
    rect(x + 12, y + 12, w - 24, h - 24, stroke=GREY, bg=abg, sw=1, rough=1,
         rounded=True, fill="solid", opacity=30, prefix="monscr")
    rect(x + w / 2 - 34, y + h, 68, 22, stroke=INK, bg=WHITE, sw=2, rough=1,
         rounded=False, prefix="monstand")
    rect(x + w / 2 - 84, y + h + 22, 168, 12, stroke=INK, bg=WHITE, sw=2, rough=1,
         rounded=True, prefix="monbase")


# ============================================================================
# BOARD TITLE
# ============================================================================
text(OX[1], -300, "Prompting", size=HERO, color=INK)
text(OX[1] + 6, -300 + HERO * LINE_H + 4, "and CRISPE, the framework for telling what's missing",
     size=H2, color=VIOLET)

# ============================================================================
# BEAT 1 - VAGUE IN, VAGUE OUT  (orange)
# ============================================================================
ox = beat_head(1, "Vague in, vague out",
               "One line, no context. Claude has to guess -\nand it guesses generically.")
crumpled_note(ox + 40, 300, 620, 230, ORANGE, ORANGE_T)
text(ox + 110, 366, "Can you help with this\ncustomer reply?", size=BODY, color=INK)
text(ox + 730, 320, "?", size=HERO, color=ORANGE)
text(ox + 40, 578, "Nothing here says who it's for, what \"help\" means,\nor what a good answer looks like.",
     size=BODY, color=GREYD)
text(ox + 40, 682, "So Claude fills the gaps itself - and you get a\ngeneric answer you have to rewrite anyway.",
     size=SMALL, color=ORANGE)

# ============================================================================
# BEAT 2 - THE SAME ASK, REBUILT  (green)
# ============================================================================
ox = beat_head(2, "The same ask, rebuilt",
               "Three sticky notes is usually enough.")
NOTES = [
    ("context",      "Our Support team answers refund requests all day."),
    ("the real ask", "Rewrite this reply so it's warm but firm,\nand under 120 words."),
    ("one example",  "Here's one that reads well: \"Thanks for\nflagging this...\""),
]
for k, (lab, body) in enumerate(NOTES):
    ny = 290 + k * 180
    sticky(ox + 40, ny, 760, 160, GREEN_BG, angle=jit(1.5))
    text(ox + 84, ny + 20, lab, size=H3, color=GREEN)
    text(ox + 84, ny + 72, body, size=BODY, color=INK)
highlighter(ox + 40, 842, 350, 46, GREEN_BG, angle=0.0)
text(ox + 56, 852, "the minimum viable prompt", size=BODY, color=GREEN)
demo_badge(ox + 40, 906, "show in Claude desktop app:  fix the prompt live")

# ============================================================================
# BEAT 3 - CRISPE  (violet)
# ============================================================================
ox = beat_head(3, "CRISPE", "Six dials, not six boxes to fill in.")
DIALS = [
    ("Context",      "what's going on",      0.80),
    ("Role",         "who Claude is",        0.35),
    ("Instructions", "what to do",           0.90),
    ("Style",        "how it should read",   0.50),
    ("Parameters",   "length, format, limits", 0.25),
    ("Example",      "one that looks right", 0.70),
]
for k, (lab, gloss, frac) in enumerate(DIALS):
    cx = ox + 230 + (k % 3) * 370
    cy = 420 + (k // 3) * 280
    dial(cx, cy, frac, VIOLET, VIOLET_T, r=48)
    text_centered(cx, cy + 64, lab, size=BODY, color=VIOLET, angle=jit(1.4))
    text_centered(cx, cy + 100, gloss, size=SMALL, color=GREYD)
highlighter(ox + 40, 862, 340, 46, VIOLET_BG, angle=0.0)
text(ox + 56, 872, "a diagnostic, not a form", size=BODY, color=VIOLET)
text(ox + 40, 930, "Nobody fills in all six. Check the dials this ask needs, skip the rest.",
     size=SMALL, color=GREYD)

# ============================================================================
# BEAT 4 - FAULT-FINDER  (blue)
# ============================================================================
ox = beat_head(4, "Fault-finder",
               "Something's off in the answer? The symptom tells you\nwhich dial you left unset.")
FAULTS = [
    ("wrong tone",   "Style",      "say how it should read",    0.30),
    ("wrong length", "Parameters", "say how long, what format", 0.25),
    ("wrong shape",  "Example",    "show one that looks right", 0.20),
]
for k, (symptom, fix, gloss, frac) in enumerate(FAULTS):
    ry = 330 + k * 140
    chip(ox + 60, ry, symptom, fill=WHITE, text_color=RED, border=RED, size=BODY)
    arrow(ox + 270, ry + 27, [[0, 0], [96, 0]], stroke=BLUE, sw=4, rough=1)
    dial(ox + 392, ry + 27, frac, BLUE, BLUE_T, r=20)
    chip(ox + 445, ry, fix, fill=WHITE, text_color=BLUE, border=BLUE, size=BODY)
    text(ox + 660, ry + 14, gloss, size=SMALL, color=GREYD)
text(ox + 60, 760, "The fault is almost never \"Claude got it wrong\".\nIt's a dial you didn't set.",
     size=BODY, color=BLUE)

# ============================================================================
# BEAT 5 - SET ONCE, NEVER REPEAT  (teal)
# ============================================================================
ox = beat_head(5, "Set once, never repeat",
               "Two settings that carry across every chat, so you\nstop retyping the same instructions.")
quill(ox + 300, 500, 200, TEAL, TEAL_T)
text_centered(ox + 300, 610, "Styles", size=H3, color=TEAL)
text_centered(ox + 300, 656, "how Claude writes back", size=SMALL, color=GREYD)
person_big(ox + 830, 480, TEAL, TEAL_T, s=1.5)
text_centered(ox + 830, 610, "preferences", size=H3, color=TEAL)
text_centered(ox + 830, 656, "standing notes for every chat", size=SMALL, color=GREYD)
highlighter(ox + 40, 712, 330, 46, TEAL_BG, angle=0.0)
text(ox + 56, 722, "set once, never repeat", size=BODY, color=TEAL)
demo_badge(ox + 40, 790, "show in Claude desktop app:  set a Style and preferences")

# ============================================================================
# BEAT 6 - CAPTURE BY VOICE  (yellow)
# ============================================================================
ox = beat_head(6, "Capture by voice",
               "Talking is faster than typing, and a rambling\nspoken prompt still beats a vague written one.")
phone(ox + 90, 320, 250, 460, YELLOW_T)
mic_icon(ox + 215, 540, 92, YELLOW)
squiggle(ox + 360, 550, 300, YELLOW, amp=20, waves=4.0)
monitor(ox + 700, 420, 380, 250, YELLOW_T)
text_centered(ox + 215, 806, "say it, roughly", size=SMALL, color=GREYD)
text_centered(ox + 890, 760, "tidy it up here", size=SMALL, color=GREYD)
highlighter(ox + 40, 862, 480, 46, YELLOW_BG, angle=0.0)
text(ox + 56, 872, "capture by voice, shape at your desk", size=BODY, color=YELLOW)
text(ox + 40, 930, "The fastest prompt is usually the one you said out loud.",
     size=SMALL, color=GREYD)

# No connector spine, no inter-beat arrows, no baseline: the beats read as one
# picture through consistent shape and rhythm, and the whitespace is the camera.

# ----------------------------------------------------------------------------
# WRITE + VALIDATE  (shared excalidraw_kit)
# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "prompting-crispe-framework.excalidraw")
MAXW = max(WID.values()) + 200
finish(out, MAXW, TOTAL_W)
