#!/usr/bin/env python3
"""Build your-setup.excalidraw - the "Your setup" scene for Day 3
- Prompting & CRISPE Framework (the AI Training series).

House Style B (see excalidraw_kit): hand-drawn, no frames, white canvas, the
hand font, lively palette. Composition + the one-off dashboard, toggle, phone
and microphone illustrations live here.

ONE composed beat, exactly as briefed:

  * a dashboard mock holding five toggle cards - model choice, extended
    thinking, web search, writing style, preferences.
  * a phone with a microphone icon, labelled "capture by voice, shape at your
    desk", linked back to the desk setup with a dashed arrow.

"Revealed one by one": there is no animation any more - the camera IS the
reveal, so the reveal order is baked into the board as numbered badges 1-5.
Pan down the stack card by card, hold ~3s of narration on each, then pan right
to the phone to close. (Nothing is dropped from the brief; the reveal is a
camera move you perform live in Loom.)

Run:  python3 videos/ai-training/3-prompting-crispe-framework/build_your_setup.py
      python3 preview.py videos/ai-training/3-prompting-crispe-framework/your-setup.excalidraw out.png
"""
import os
import sys

_d = os.path.dirname(os.path.abspath(__file__))
while _d != os.path.dirname(_d) and not os.path.exists(os.path.join(_d, "excalidraw_kit.py")):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)

import random
from excalidraw_kit import *

random.seed(30320)

# ----------------------------------------------------------------------------
# BEAT SCAFFOLD - one composed beat (the brief is a single dashboard picture),
# so the usual GAP between slots never comes into play.
# ----------------------------------------------------------------------------
WID = {1: 1200}
ACCENT = {1: BLUE}
OX = {1: 0}
TOTAL_W = WID[1]
HEAD_Y = 60


def beat_head(i, title, sub=None):
    ox = OX[i]
    heading(ox, HEAD_Y, title, color=ACCENT[i], sub=sub)
    return ox


# ----------------------------------------------------------------------------
# LOCAL ONE-OFF ILLUSTRATIONS
# ----------------------------------------------------------------------------
def window(x, y, w, h, label):
    """A plain app window: chrome bar, three dots, a faint title."""
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="win")
    line(x, y + 46, [[0, 0], [w, 0]], stroke=GREY, sw=1, prefix="winbar")
    for k in range(3):
        ellipse(x + 20 + k * 20, y + 17, 11, 11, stroke=GREY, bg=GREY, sw=1, prefix="dot")
    text(x + w / 2 - text_w(label, SMALL) / 2, y + 12, label, size=SMALL, color=GREY)


def toggle(x, y, accent, abg, w=76, h=36):
    """An on-switch: accent pill with the knob swung right."""
    rect(x, y, w, h, stroke=accent, bg=abg, sw=2, rough=1, rounded=True, prefix="tog")
    ellipse(x + w - h + 4, y + 4, h - 8, h - 8, stroke=accent, bg=accent, sw=2, prefix="knob")


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


# ============================================================================
# BOARD TITLE
# ============================================================================
text(OX[1], -300, "Your setup", size=HERO, color=INK)
text(OX[1] + 6, -300 + HERO * LINE_H + 4, "five switches that change what you get back",
     size=H2, color=BLUE)

# ============================================================================
# THE BEAT
# ============================================================================
ox = beat_head(1, "Set it once",
               "These live in Claude's own settings. Change them\nwhen the job changes, not every chat.")

# ------------------------------------------------------- THE DASHBOARD MOCK ----
WX, WY, WW, WH = ox + 20, 262, 740, 640
window(WX, WY, WW, WH, "Settings")

CARDS = [
    ("Model choice",      "quick answers, or deeper thinking",     BLUE,   BLUE_T,   BLUE_BG),
    ("Extended thinking", "let it work longer on a hard problem",  VIOLET, VIOLET_T, VIOLET_BG),
    ("Web search",        "let it look things up, not guess",      TEAL,   TEAL_T,   TEAL_BG),
    ("Writing style",     "how it writes back: plain, formal, brief", ORANGE, ORANGE_T, ORANGE_BG),
    ("Preferences",       "standing notes it applies to every chat", GREEN,  GREEN_T,  GREEN_BG),
]
for k, (name, cap, acc, tint, pastel) in enumerate(CARDS):
    cy = 330 + k * 112
    rect(ox + 44, cy, 692, 96, stroke=acc, bg=tint, sw=2, rough=1, rounded=True, prefix="card")
    num_badge(ox + 64, cy + 26, k + 1, acc, d=44)
    text(ox + 128, cy + 18, name, size=BODY, color=acc)
    text(ox + 128, cy + 52, cap, size=SMALL, color=GREYD)
    toggle(ox + 626, cy + 30, acc, pastel)

# ------------------------------------------------------------- THE PHONE ----
PX, PY, PW, PH = ox + 820, 300, 250, 470
text_centered(ox + 945, 262, "on the move", size=SMALL, color=GREY)
phone(PX, PY, PW, PH, VIOLET_T)
mic_icon(ox + 945, 500, 90, VIOLET)
arrow(ox + 812, 520, [[0, 0], [-40, 0]], stroke=VIOLET, sw=3, rough=1, dashed=True)
text_centered(ox + 945, 800, "capture by voice,\nshape at your desk", size=BODY, color=VIOLET)

demo_badge(ox + 20, 940, "show in Claude desktop app:  the settings panel")

# ----------------------------------------------------------------------------
# WRITE + VALIDATE  (shared excalidraw_kit)
# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "your-setup.excalidraw")
MAXW = max(WID.values()) + 200
finish(out, MAXW, TOTAL_W)
