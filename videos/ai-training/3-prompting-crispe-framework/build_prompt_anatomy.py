#!/usr/bin/env python3
"""Build prompt-anatomy.excalidraw - the "Prompt anatomy" scene for Day 3
- Prompting & CRISPE Framework (the AI Training series).

House Style B (see excalidraw_kit): hand-drawn, no frames, white canvas, the
hand font, lively palette. Composition + the one-off dial illustration live here.

ONE composed beat, exactly as briefed:

  * left column, stacked vertically (the design system's "stack side-by-side
    pairs vertically" rule): the BEFORE - a one-line vague prompt with a big
    question mark - and below it the AFTER, the same ask rewritten, with three
    callout tags pointing into it: "context", "the real ask", "example".
  * right SIDE PANEL, across a dashed divider: six small labelled dials titled
    CRISPE (Context, Role, Instructions, Style, Parameters, Example) with the
    caption "a diagnostic, not a form".

The callout colours match their dials on purpose - context/BLUE -> Context,
the real ask/GREEN -> Instructions, example/YELLOW -> Example - so the panel
reads as the general form of the annotated prompt.

Recording: there is no animation any more, the camera is the reveal. Pan the
BEFORE first, then the AFTER (holding on each callout tag as you name it), then
zoom right to the CRISPE panel and land on the caption.

Run:  python3 videos/ai-training/3-prompting-crispe-framework/build_prompt_anatomy.py
      python3 preview.py videos/ai-training/3-prompting-crispe-framework/prompt-anatomy.excalidraw out.png
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

random.seed(30310)

# ----------------------------------------------------------------------------
# BEAT SCAFFOLD - one composed beat (the brief is a single picture), so the
# usual GAP between slots never comes into play. Same slot shape as every other
# video: ~1160 wide of content, framed whole on a 14" MacBook.
# ----------------------------------------------------------------------------
WID = {1: 1200}
ACCENT = {1: VIOLET}
OX = {1: 0}
TOTAL_W = WID[1]
HEAD_Y = 60


def beat_head(i, title, sub=None):
    ox = OX[i]
    heading(ox, HEAD_Y, title, color=ACCENT[i], sub=sub)
    return ox


# ----------------------------------------------------------------------------
# LOCAL ONE-OFF ILLUSTRATION - a little hand-drawn dial
# ----------------------------------------------------------------------------
def dial(cx, cy, frac, color, abg, r=34):
    """A sketched dial: face, three tick marks over the top, and a needle set to
    `frac` (0 = swung left / low, 1 = swung right / high)."""
    ellipse(cx - r, cy - r, 2 * r, 2 * r, stroke=color, bg=abg, sw=3, rough=1, prefix="dial")
    for t in (0.0, 0.5, 1.0):
        th = math.radians(215 - t * 250)
        dx, dy = math.cos(th), -math.sin(th)
        line(cx + dx * (r + 5), cy + dy * (r + 5),
             [[0, 0], [dx * 9, dy * 9]], stroke=color, sw=2, prefix="tick")
    th = math.radians(215 - frac * 250)
    line(cx, cy, [[0, 0], [math.cos(th) * r * 0.74, -math.sin(th) * r * 0.74]],
         stroke=INK, sw=3, prefix="needle")
    ellipse(cx - 4, cy - 4, 8, 8, stroke=INK, bg=INK, sw=2, prefix="hub")


# ============================================================================
# BOARD TITLE
# ============================================================================
text(OX[1], -300, "Prompt anatomy", size=HERO, color=INK)
text(OX[1] + 6, -300 + HERO * LINE_H + 4, "the same ask twice - one vague, one that works",
     size=H2, color=VIOLET)

# ============================================================================
# THE BEAT
# ============================================================================
ox = beat_head(1, "Same ask, twice",
               "A prompt has parts. Once you can see them,\nyou can see what a weak one is missing.")

# ---------------------------------------------------------------- BEFORE ----
text(ox + 20, 246, "before", size=SMALL, color=GREY)
sticky(ox + 20, 276, 560, 92, FAINT, angle=jit(1.4))
text(ox + 48, 306, "Can you help with this customer reply?", size=BODY, color=INK)
text(ox + 610, 268, "?", size=HERO, color=RED)
text(ox + 20, 388, "one line, no context - Claude has to guess the rest",
     size=SMALL, color=RED)

# ----------------------------------------------------------------- AFTER ----
text(ox + 20, 462, "after", size=SMALL, color=GREY)
rect(ox + 20, 492, 470, 318, stroke=GREYD, bg=WHITE, sw=2, rough=1, rounded=True,
     angle=jit(1.1), prefix="after")

PARTS = [
    (BLUE,   "context",      "Our Support team answers refund\nrequests all day."),
    (GREEN,  "the real ask", "Rewrite this reply so it's warm\nbut firm, and under 120 words."),
    (YELLOW, "example",      "Here's one that reads well:\n\"Thanks for flagging this...\""),
]
for k, (acc, tag, body) in enumerate(PARTS):
    py = 518 + k * 96
    rect(ox + 36, py, 6, 66, stroke=acc, bg=acc, sw=1, rough=1, rounded=False, prefix="bar")
    text(ox + 52, py + 2, body, size=BODY, color=INK)
    chip(ox + 530, py + 8, tag, fill=WHITE, text_color=acc, border=acc, size=SMALL)
    arrow(ox + 524, py + 32, [[0, 0], [-30, 0]], stroke=acc, sw=3, rough=1)

# ------------------------------------------------------ SIDE PANEL: CRISPE ----
line(ox + 730, 250, [[0, 0], [0, 580]], stroke=FAINT, sw=2, dashed=True, prefix="div")

text(ox + 770, 250, "CRISPE", size=H2, color=VIOLET)
scribble_underline(ox + 770, 250 + H2 * LINE_H + 4, 130, VIOLET, sw=3)

DIALS = [
    ("Context",      0.80, BLUE,   BLUE_T),
    ("Role",         0.35, ORANGE, ORANGE_T),
    ("Instructions", 0.90, GREEN,  GREEN_T),
    ("Style",        0.50, TEAL,   TEAL_T),
    ("Parameters",   0.25, INDIGO, INDIGO_T),
    ("Example",      0.70, YELLOW, YELLOW_T),
]
for k, (lab, frac, acc, tint) in enumerate(DIALS):
    cx = ox + 867 + (k % 2) * 195
    cy = 400 + (k // 2) * 152
    dial(cx, cy, frac, acc, tint)
    text_centered(cx, cy + 46, lab, size=SMALL, color=acc, angle=jit(1.6))

highlighter(ox + 770, 796, 330, 46, VIOLET_BG, angle=0.0)
text(ox + 786, 806, "a diagnostic, not a form", size=BODY, color=VIOLET)
text(ox + 770, 862, "check the dials this ask needs -\nskip the rest", size=SMALL, color=GREYD)

# ----------------------------------------------------------------------------
# WRITE + VALIDATE  (shared excalidraw_kit)
# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompt-anatomy.excalidraw")
MAXW = max(WID.values()) + 200
finish(out, MAXW, TOTAL_W)
