#!/usr/bin/env python3
"""Build claude-design.excalidraw - ONE flowing, illustrated explainer for the
"Claude Design" training video (Phlo AI Ops Learn, module 2.12).

House Style B (see excalidraw_kit): one hand-drawn left-to-right journey, no
frames, white canvas, the hand font, lively palette. Composition + one-off
illustrations (a UI mockup, a design-system swatch strip) live here.

Claude Design (Anthropic Labs, research preview, powered by Claude Opus 4.7,
Pro+) is a design partner: you collaborate to make polished visual work -
designs, interactive prototypes, on-brand decks, one-pagers. Its signature is
that it BUILDS A DESIGN SYSTEM from your codebase + design files during
onboarding, then every project uses your colours, type and components
automatically (beat 3). You start from a prompt, uploaded images/docs, or your
codebase, and export to PPTX or Canva. Because it's a research preview, beat 8
flags rough edges + not uploading confidential material.

Run:  python3 videos/claude/12-design/build_design.py
      python3 preview.py videos/claude/12-design/claude-design.excalidraw out.png
"""
import os
import sys

_d = os.path.dirname(os.path.abspath(__file__))
while _d != os.path.dirname(_d) and not os.path.exists(os.path.join(_d, "excalidraw_kit.py")):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)

import random
from excalidraw_kit import *

random.seed(121210)

N = 9
GAP = 800
WID = dict.fromkeys(range(1, N + 1), 1200)
ACCENT = {1: VIOLET, 2: BLUE, 3: GREEN, 4: ORANGE, 5: TEAL,
          6: INDIGO, 7: YELLOW, 8: ORANGE, 9: VIOLET}
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
def mockup(x, y, w, h, accent=VIOLET, abg=VIOLET_BG):
    """A polished UI mockup: header bar, hero block, two cards, a button."""
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="mock")
    rect(x + 0.08 * w, y + 0.07 * h, 0.84 * w, 0.12 * h, stroke="transparent",
         bg=accent, sw=1, rough=1, rounded=True, prefix="mh")
    rect(x + 0.08 * w, y + 0.25 * h, 0.84 * w, 0.26 * h, stroke=GREYD, bg=abg, sw=2,
         rough=1, rounded=True, prefix="mhero")
    rect(x + 0.08 * w, y + 0.57 * h, 0.38 * w, 0.22 * h, stroke=GREYD, bg=WHITE, sw=2,
         rough=1, rounded=True, prefix="mc")
    rect(x + 0.54 * w, y + 0.57 * h, 0.38 * w, 0.22 * h, stroke=GREYD, bg=WHITE, sw=2,
         rough=1, rounded=True, prefix="mc")
    rect(x + 0.08 * w, y + 0.85 * h, 0.30 * w, 0.09 * h, stroke=accent, bg=accent, sw=1,
         rough=1, rounded=True, prefix="mbtn")


def swatch_strip(x, y, cols):
    """A design-system strip: colour swatches + a type sample + a component chip."""
    sw_ = 52
    for k, (c, cbg) in enumerate(cols):
        rect(x + k * (sw_ + 14), y, sw_, sw_, stroke=c, bg=cbg, sw=2, rough=1, rounded=True, prefix="swt")
    tx = x + len(cols) * (sw_ + 14) + 20
    text(tx, y - 2, "Aa", size=H2, color=INK)
    bx = tx + 90
    rect(bx, y + 6, 120, 40, stroke=VIOLET, bg=VIOLET, sw=1, rough=1, rounded=True, prefix="swbtn")
    text(bx + 22, y + 14, "Button", size=SMALL, color=WHITE)


# ============================================================================
# BOARD TITLE
# ============================================================================
text(OX[1], -300, "Claude Design", size=HERO, color=INK)
text(OX[1] + 6, -300 + HERO * LINE_H + 4,
     "describe it - and watch it get designed, on-brand", size=H2, color=VIOLET)

# ============================================================================
# BEAT 1 - HOOK
# ============================================================================
ox = beat_head(1, "Describe it, see it designed",
               "not a wall of text describing a screen - an actual,\npolished design you can look at")
by = 360
bw, bh = 500, 130
sticky(ox + 40, by, bw, bh, GREY, angle=jit(1.5))
text(ox + 72, by + 30, "design a clean landing\npage for the new tool", size=BODY, color=WHITE)
line(ox + 90, by + bh, [[0, 0], [-18, 30], [22, -2]], stroke=GREY, sw=3)
arrow(ox + 40 + bw + 30, by + bh / 2, [[0, 0], [140, 0]], stroke=VIOLET, sw=5, rough=1)
mx = ox + 40 + bw + 210
ellipse(mx - 30, by - 40, 300, 320, stroke=VIOLET, bg=VIOLET_BG, sw=2, rough=1, fill="solid", opacity=45)
mockup(mx, by - 20, 240, 280, accent=VIOLET, abg=VIOLET_BG)
text(mx - 10, by + 274, "a real design, not a\ndescription of one", size=SMALL, color=VIOLET)

# ============================================================================
# BEAT 2 - WHAT IT IS
# ============================================================================
ox = beat_head(2, "A design partner from Anthropic Labs",
               "Work with Claude to make polished visual things -\ndesigns, prototypes, decks, one-pagers.")
mockup(ox + 120, 340, 380, 420, accent=BLUE, abg=BLUE_BG)
outs = [("interactive prototypes", 60), ("on-brand decks", 180), ("one-pagers", 300)]
for lab, yy in outs:
    text(ox + 560, 340 + yy, lab, size=BODY, color=BLUE)
    arrow(ox + 555, 360 + yy, [[0, 0], [-50, 0]], stroke=BLUE, sw=3)
chx = ox + 120
for lab in ["research preview", "powered by Claude Opus", "Pro and up"]:
    w, _ = chip(chx, 784, lab, fill=WHITE, text_color=BLUE, border=BLUE, size=SMALL)
    chx += w + 26

# ============================================================================
# BEAT 3 - IT LEARNS YOUR STYLE  (signature)
# ============================================================================
ox = beat_head(3, "It learns your house style",
               "Onboarding, once: Claude reads your codebase and\ndesign files and builds your design system.")
file_icon(ox + 70, 360, abg=GREEN_BG)
file_icon(ox + 140, 380, abg=BLUE_BG)
text(ox + 60, 470, "your codebase\n+ design files", size=SMALL, color=GREYD)
arrow(ox + 230, 400, [[0, 0], [110, 0]], stroke=GREEN, sw=4)
# the learned design system
sticky(ox + 360, 330, 720, 200, GREEN_BG, angle=jit(-0.8))
text(ox + 390, 352, "your design system", size=H3, color=GREEN)
swatch_strip(ox + 392, 420, [(VIOLET, VIOLET_BG), (BLUE, BLUE_BG), (GREEN, GREEN_BG),
                             (ORANGE, ORANGE_BG)])
text(ox + 60, 580, "then every project after that uses your colours, type and components - automatically",
     size=BODY, color=GREYD)
chip(ox + 60, 650, "on-brand by default, not by copy-paste", fill=WHITE, text_color=GREEN, border=GREEN, size=SMALL)

# ============================================================================
# BEAT 4 - START FROM ANYTHING
# ============================================================================
ox = beat_head(4, "Start from almost anything",
               "A prompt, a pile of files, or your live site -\nClaude meets you where your idea already is.")
starts = [("a text prompt", VIOLET, VIOLET_BG),
          ("images & docs (DOCX, PPTX, XLSX)", BLUE, BLUE_BG),
          ("your codebase", GREEN, GREEN_BG),
          ("grab elements off your live site", ORANGE, ORANGE_BG)]
sy = 340
for k, (lab, acc, abg) in enumerate(starts):
    yy = sy + k * 110
    sticky(ox + 60, yy, 760, 86, abg, angle=jit(1.0))
    ellipse(ox + 84, yy + 22, 40, 40, stroke=acc, bg=WHITE, sw=3)
    text_centered(ox + 104, yy + 28, str(k + 1), size=H3, color=acc)
    text(ox + 150, yy + 24, lab, size=H3, color=INK)
text(ox + 60, sy + 4 * 110 + 16, "the web-capture tool grabs real elements, so prototypes look like the real product",
     size=SMALL, color=GREYD)

# ============================================================================
# BEAT 5 - WHAT YOU GET OUT
# ============================================================================
ox = beat_head(5, "What you get out",
               "Things you can share, test and ship - not just pictures.")
outs = [("Interactive prototypes", "shareable and user-testable -\nno code review, no PRs", TEAL, TEAL_BG),
        ("Feature flows", "sketch it, hand it to\nClaude Code to build", INDIGO, INDIGO_BG),
        ("On-brand decks", "export to PPTX, or\nsend straight to Canva", VIOLET, VIOLET_BG)]
gx2, gy = ox + 50, 340
cw2 = 340
for k, (head, cap, acc, abg) in enumerate(outs):
    bx = gx2 + k * (cw2 + 30)
    sticky(bx, gy, cw2, 380, abg, angle=jit(1.0))
    text(bx + 28, gy + 26, head, size=H3, color=acc)
    text(bx + 28, gy + 96, cap, size=BODY, color=INK)
    mockup(bx + 60, gy + 190, 220, 160, accent=acc, abg=abg)

# ============================================================================
# BEAT 6 - WHO IT'S FOR
# ============================================================================
ox = beat_head(6, "Three handy flows",
               "One per job - designer, PM, founder.")
flows = [("Designers", "static mockup -> interactive prototype to user-test", VIOLET),
         ("Product managers", "sketch a feature flow -> hand to Claude Code", BLUE),
         ("Founders & AEs", "rough outline -> a complete, on-brand deck", ORANGE)]
fy = 350
for k, (who, what, acc) in enumerate(flows):
    yy = fy + k * 130
    text(ox + 60, yy, who, size=H3, color=acc)
    chip(ox + 60, yy + 50, what, fill=WHITE, text_color=acc, border=acc, size=SMALL)
demo_badge(ox + 60, fy + 3 * 130 + 10,
           "show in Claude Design:  a prompt -> an on-brand mockup, then export")

# ============================================================================
# BEAT 7 - WHERE IT SHINES  (a gallery of mockups)
# ============================================================================
ox = beat_head(7, "What to make first")
jobs = [("A quick prototype", "clickable, to test today", TEAL, TEAL_BG),
        ("An on-brand deck", "a pitch, in your style", VIOLET, VIOLET_BG),
        ("A tidy one-pager", "made to look finished", ORANGE, ORANGE_BG),
        ("A feature flow", "agree the shape first", BLUE, BLUE_BG)]
fx0, fy0, step = ox + 50, 360, 285
for k, (head, cap, acc, abg) in enumerate(jobs):
    bx = fx0 + k * step
    mockup(bx, fy0, 232, 180, accent=acc, abg=abg)
    text(bx, fy0 + 202, head, size=BODY, color=acc, width=250)
    text(bx, fy0 + 244, cap, size=SMALL, color=GREYD, width=250)

# ============================================================================
# BEAT 8 - SAFETY  (draft -> refine -> final, not a caution box)
# ============================================================================
ox = beat_head(8, "A preview - so treat the output as a draft")
mw, mh = 240, 190
xs = [ox + 60, ox + 440, ox + 820]
accs = [(ORANGE, ORANGE_BG), (BLUE, BLUE_BG), (GREEN, GREEN_BG)]
labs = ["first draft", "you refine it", "your final"]
for k, (mxx, (acc, abg), lab) in enumerate(zip(xs, accs, labs, strict=True)):
    mockup(mxx, 380, mw, mh, accent=acc, abg=abg)
    text_centered(mxx + mw / 2, 590, lab, size=BODY, color=acc)
    if k < 2:
        arrow(mxx + mw + 10, 470, [[0, 0], [80, 0]], stroke=VIOLET, sw=4)
chip(ox + 60, 330, "research preview - rough edges, and it changes", fill=WHITE,
     text_color=ORANGE, border=ORANGE, size=SMALL)
rect(ox + 60, 650, 1020, 120, stroke=ORANGE, bg=ORANGE_T, sw=2, rough=1, rounded=True)
text(ox + 92, 672, "Keep out unless it's been approved", size=H3, color=ORANGE)
text(ox + 92, 726, "confidential designs, patient-facing material, or a private codebase", size=BODY, color=INK)

# ============================================================================
# BEAT 9 - TRY / CLOSE  (a prompt -> a mockup, and the module wrap)
# ============================================================================
ox = beat_head(9, "Describe one screen you wish existed")
sticky(ox + 60, 340, 540, 160, VIOLET_BG, angle=jit(1.3))
text(ox + 96, 366, "Try this", size=H3, color=VIOLET)
text(ox + 96, 426, "describe one screen or deck\nyou wish already existed", size=BODY, color=INK)
arrow(ox + 620, 420, [[0, 0], [70, 0]], stroke=VIOLET, sw=4)
mockup(ox + 720, 350, 240, 200, accent=VIOLET, abg=VIOLET_BG)
ex_x = ox + 60
for lab in ["a landing page", "a pitch deck", "a settings screen"]:
    w, _ = chip(ex_x, 560, lab, fill=WHITE, text_color=VIOLET, border=VIOLET, size=SMALL)
    ex_x += w + 32
text(ox + 60, 648, "see the first design, then refine it in plain English", size=BODY, color=GREYD)
text(ox + 40, 708, "Claude gets you a polished start - you shape it into the finished thing.",
     size=H3, color=INK)
text(ox + 40, 770, "That's the Claude module - nice work getting through it.", size=BODY, color=GREEN)
text(ox + 60, 836, "Docs: Anthropic - Introducing Claude Design, and Get started with Claude Design",
     size=SMALL, color=VIOLET)

# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "claude-design.excalidraw")
finish(out, max(WID.values()) + 200, TOTAL_W)
