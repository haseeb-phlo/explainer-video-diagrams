#!/usr/bin/env python3
"""Build phlo-2.2-claude-projects.excalidraw - ONE flowing, illustrated explainer
for the "Claude Projects" training video (Phlo AI training, module 2.2, ~7 min).

Style B (house style): a single hand-drawn journey, left-to-right, NO frames, NO
boxes, white canvas, everything in the hand font (fontFamily 1), roughness 1, a
lively colour-coded Excalidraw palette, big colour-blocking, scribbled annotations
and charming primitive illustrations. The look lives in the shared excalidraw_kit;
this file holds only the composition. Converted from the old 10-frame editorial
"Style A" deck of the same name.

Run:  python3 build_projects.py
      python3 ../../../preview.py phlo-2.2-claude-projects.excalidraw out.png
"""
import os
import sys

_d = os.path.dirname(os.path.abspath(__file__))
while _d != os.path.dirname(_d) and not os.path.exists(os.path.join(_d, "excalidraw_kit.py")):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)

import random
from excalidraw_kit import *

random.seed(22022)

# ----------------------------------------------------------------------------
# BEAT SCAFFOLD
# ----------------------------------------------------------------------------
# Wide gaps so a single beat can be framed on a 14" laptop without neighbours
# peeking in - the empty space IS the zoom-to-one-beat affordance. Every beat
# uses the SAME slot (~1120 wide x ~980 tall content, ~1.15 : 1) so framing is
# identical and fits a 14" MacBook screen.
GAP = 800
WID = dict.fromkeys(range(1, 10), 1200)
ACCENT = {1: RED, 2: VIOLET, 3: BLUE, 4: GREEN, 5: ORANGE, 6: TEAL, 7: INDIGO, 8: YELLOW, 9: VIOLET}
OX, _c = {}, 0
for _i in range(1, 10):
    OX[_i] = _c
    _c += WID[_i] + GAP
TOTAL_W = _c
HEAD_Y = 60

def beat_head(i, title, sub=None):
    # QUIET heading: kit heading() draws a prominent hand title in the beat's
    # accent colour + a hand underline. No step circle, no highlighter sweep.
    heading(OX[i], HEAD_Y, title, color=ACCENT[i], sub=sub)
    return OX[i]

# ============================================================================
# BOARD TITLE
# ============================================================================
text(OX[1], -300, "Claude Projects", size=HERO, color=INK)
text(OX[1] + 6, -300 + HERO * LINE_H + 4, "the multiplier - set up once, use forever", size=H2, color=VIOLET)

# ============================================================================
# BEAT 1 - THE TAX YOU PAY EVERY MORNING
# ============================================================================
ox = beat_head(1, "The tax you pay every morning")
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
dw, dgap, dy = 192, 26, 320
for k, d in enumerate(days):
    dx = ox + 40 + k * (dw + dgap)
    sticky(dx, dy, dw, 200, RED_BG, angle=jit(1.6))
    text(dx + 22, dy + 18, d, size=BODY, color=RED)
    text(dx + 22, dy + 64, "Who I am -\nmy role -\nhouse tone -\ndo-not-say\nlist ...", size=SMALL, color=INK)
    arrow(dx + dw / 2, dy + 200, [[0, 0], [0, 32]], stroke=RED, sw=2, rough=1)
text(ox + 40, dy + 248, "the same brief, re-pasted every single morning", size=SMALL, color=GREYD)
clock(ox + 110, 700, 46, RED)
text(ox + 180, 676, "~10 min a day", size=H3, color=INK)
text(ox + 180, 726, "= about 1 hour a week. Every week.", size=H3, color=RED)
text(ox + 40, 830, "Re-explaining yourself is invisible work. It adds up.", size=BODY, color=GREYD)

# ============================================================================
# BEAT 2 - WHAT A PROJECT ACTUALLY IS
# ============================================================================
ox = beat_head(2, "What a Project actually is")
cont_x, cont_y, cont_w, cont_h = ox + 40, 300, 1080, 560
rect(cont_x, cont_y, cont_w, cont_h, stroke=VIOLET, bg=VIOLET_BG, sw=3, rough=1, rounded=True,
     fill="solid", opacity=22, angle=jit(0.8))
text(cont_x + 28, cont_y + 18, "ONE PROJECT", size=H3, color=VIOLET)
parts = [("Custom instructions", "Your standing brief: role,\nyour house voice, what to avoid.", obj_doc, VIOLET, VIOLET_BG),
         ("Knowledge files", "Reference docs Claude reads\nbefore every reply.", obj_files, BLUE, BLUE_BG),
         ("Conversations", "Every chat here shares the\ntwo above - automatically.", None, GREEN, GREEN_BG)]
pw = (cont_w - 80) / 3
for k, (ttl, body, illus, acc, abg) in enumerate(parts):
    px = cont_x + 20 + k * (pw + 10)
    sticky(px, cont_y + 70, pw - 10, cont_h - 200, WHITE, angle=jit(0.8))
    rect(px, cont_y + 70, pw - 10, cont_h - 200, stroke=acc, bg="transparent", sw=2, rough=1, rounded=True)
    text(px + 22, cont_y + 92, ttl, size=LABEL, color=acc)
    if illus:
        illus(px + 24, cont_y + 150, acc, abg)
    else:
        for m in range(3):
            rect(px + 24, cont_y + 150 + m * 34, pw - 90, 24, stroke="transparent", bg=FAINT, sw=1, rounded=True, prefix="msg")
    text(px + 22, cont_y + 304, body, size=SMALL, color=INK)
text(cont_x + 20, cont_y + cont_h + 24, "One persistent space. Context lives here,\nnot in your clipboard.", size=H3, color=VIOLET)

# ============================================================================
# BEAT 3 - THE SHIFT (before -> after)
# ============================================================================
ox = beat_head(3, "The shift")
# BEFORE - top
bx, by = ox + 60, 300
text(bx, by - 36, "BEFORE", size=H3, color=RED)
for k in range(3):
    sticky(bx + k * 26, by + k * 22, 300, 86, FAINT, angle=jit(2.0))
text(bx + 56, by + 26, "context ...\ncontext ...", size=SMALL, color=GREYD)
arrow(bx + 360, by + 50, [[0, 0], [260, 0]], stroke=RED, sw=3, rough=1)
claude_face(bx + 700, by + 56, r=42, color=RED)
text(bx + 666, by + 130, "paste it all, every time", size=SMALL, color=RED)
# arrow down to AFTER
arrow(bx + 180, by + 200, [[0, 0], [0, 120]], stroke=BLUE, sw=6, rough=1)
text(bx + 220, by + 240, "write it once", size=BODY, color=BLUE)
# AFTER - below
ay = by + 340
text(bx, ay - 36, "AFTER", size=H3, color=BLUE)
rect(bx, ay, 360, 260, stroke=BLUE, bg=BLUE_BG, sw=3, rough=1, rounded=True, fill="solid", opacity=30, angle=jit(-1.0))
text(bx + 110, ay + 22, "Project", size=H2, color=BLUE)
text(bx + 40, ay + 100, "the brief lives here\nand never moves", size=SMALL, color=INK)
claude_face(bx + 700, ay + 90, r=42, color=BLUE)
text(bx + 660, ay + 170, "context is permanent", size=SMALL, color=BLUE)
text(ox + 40, ay + 290, "Write the brief once.\nClaude applies it every time.", size=H3, color=BLUE)

# ============================================================================
# BEAT 4 - THREE PROJECTS YOU COULD BUILD THIS WEEK
# ============================================================================
ox = beat_head(4, "Three Projects you could build this week")
projects = [
    ("A", "Customer reply drafting", "Support and Ops",
     "your tone guide - examples of\ngreat replies - the do-not-say list", GREEN, GREEN_BG, True),
    ("B", "Engineering PR review", "Engineering",
     "coding standards - common review\npatterns - the team style guide", BLUE, BLUE_BG, False),
    ("C", "Weekly board prep", "Leadership",
     "board memo format - the last four\nmemos - what the board cares about", ORANGE, ORANGE_BG, False),
]
cw, ch, cgap, cy0 = 1070, 235, 16, 285
for k, (letter, ttl, who, files, acc, abg, gate) in enumerate(projects):
    cy = cy0 + k * (ch + cgap)
    sticky(ox + 40, cy, cw, ch, abg, angle=jit(0.8))
    ellipse(ox + 64, cy + 24, 50, 50, stroke=acc, bg=acc, sw=2)
    text_centered(ox + 89, cy + 35, letter, size=H2, color=WHITE)
    text(ox + 132, cy + 32, ttl, size=H3, color=acc)
    text(ox + 132, cy + 92, "Who: " + who, size=BODY, color=INK)
    # right half: knowledge files
    text(ox + 600, cy + 28, "Knowledge:", size=SMALL, color=GREYD)
    text(ox + 600, cy + 64, files, size=SMALL, color=INK)
    if gate:
        rect(ox + 132, cy + 150, 420, 64, stroke=RED, bg=RED_BG, sw=2, rough=1, rounded=True, fill="solid", opacity=30)
        text(ox + 150, cy + 164, "Drafts only - a person checks\nand sends. Never auto-sent.", size=SMALL, color=RED)

# ============================================================================
# BEAT 5 - THE MATHS
# ============================================================================
ox = beat_head(5, "The maths")
base = 700
line(ox + 60, base, [[0, 0], [560, 0]], stroke=INK, sw=2)
# setup bar (small) vs saving bar (big)
rect(ox + 120, base - 90, 150, 90, stroke=INK, bg=ORANGE, sw=2, rough=1, rounded=False)
text_centered(ox + 195, base + 14, "Setup", size=SMALL, color=GREYD)
text_centered(ox + 195, base - 130, "20 min\nonce", size=SMALL, color=ORANGE)
rect(ox + 360, base - 360, 150, 360, stroke=INK, bg=GREEN, sw=2, rough=1, rounded=False)
text_centered(ox + 435, base + 14, "Saving", size=SMALL, color=GREYD)
text_centered(ox + 435, base - 400, "hours\nevery week", size=SMALL, color=GREEN)
text(ox + 700, base - 320, "Setup:  20 minutes.\nOnce.", size=H3, color=ORANGE)
text(ox + 700, base - 180, "Saving:  hours every\nweek - for as long as\nyou do the job.", size=H3, color=GREEN)
# under the bars
highlighter(ox + 56, base + 70, 940, 60, ORANGE_BG, angle=0.0)
text(ox + 70, base + 82, "The best twenty minutes you'll spend this month.", size=BODY, color=INK)

# ============================================================================
# BEAT 6 - WHY IT'S A MULTIPLIER
# ============================================================================
ox = beat_head(6, "Why it's a multiplier")
sx, sy = ox + 120, 460
claude_face(sx, sy, r=48, color=TEAL)
text_centered(sx, sy + 80, "builds the\nProject once", size=SMALL, color=GREYD)
fan_x = sx + 460
for k in range(4):
    py = sy - 150 + k * 110
    arrow(sx + 70, sy, [[0, 0], [fan_x - sx - 110, py - sy + 30]], stroke=GREY, sw=2, rough=1)
    person(fan_x + 40, py + 30, TEAL)
text(fan_x + 110, sy - 130, "the whole\nteam uses it", size=H3, color=TEAL)
text(ox + 40, 800, "One person builds Customer Replies. The support team\ndrafts in the house voice from day one.", size=BODY, color=INK)
text(ox + 40, 900, "Sharing is available on Team and Enterprise plans.", size=SMALL, color=GREY)

# ============================================================================
# BEAT 7 - LET'S BUILD ONE, LIVE
# ============================================================================
ox = beat_head(7, "Let's build one - live")
steps = ["Name it, and set who can see it",
         "Write the custom instructions",
         "Add two or three reference files, then chat"]
for k, s in enumerate(steps):
    sy = 320 + k * 150
    num_circle(ox + 50, sy, k + 1, INDIGO, d=64)
    sticky(ox + 140, sy, 940, 96, INDIGO_BG, angle=jit(0.8))
    text(ox + 176, sy + 28, s, size=H3, color=INK)
demo_badge(ox + 140, 320 + 3 * 150 + 10, "show in Claude desktop app:  building a Customer Replies Project")

# ============================================================================
# BEAT 8 - PAUSE HERE, AND TRY IT
# ============================================================================
ox = beat_head(8, "Pause here, and try it")
pause_icon(ox + 40, 322, 80, color=YELLOW)
lines8 = ["Think of one task you repeat.",
          "Open claude.ai/projects and create it\nnow - even empty.",
          "Fill it as you watch the rest of\nthis module."]
yy = 332
for s in lines8:
    text(ox + 170, yy, s, size=H3, color=INK)
    yy += text_h(s, H3) + 28
text(ox + 170, yy + 8, "two minutes - then carry on.", size=BODY, color=GREYD)

# ============================================================================
# BEAT 9 - ONE PROJECT, TWENTY MINUTES (close)
# ============================================================================
ox = beat_head(9, "One Project. Twenty minutes.")
highlighter(ox + 36, 318, 620, 64, VIOLET_BG, angle=0.0)
text(ox + 50, 330, "Use it once a day for a month.", size=H3, color=INK)
text(ox + 50, 410, "Then tell me Projects didn't\nchange how you work.", size=H3, color=VIOLET)
text(ox + 40, 540, "Resources", size=H3, color=VIOLET)
text(ox + 60, 606, "Anthropic Help Centre - 'How can I create and\nmanage projects' (support.claude.com)", size=SMALL, color=VIOLET)
text(ox + 60, 700, "AI Ops Learn - Prompt Library - the team's\nshared Projects", size=SMALL, color=VIOLET)

# No connector spine and no branding footer: beats read as one picture through
# layout + consistent rhythm (the ai-foundations natural-flow look), not arrows.

# ----------------------------------------------------------------------------
# WRITE + VALIDATE  (shared excalidraw_kit)
# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "phlo-2.2-claude-projects.excalidraw")
MAXW = max(WID.values()) + 200
finish(out, MAXW, TOTAL_W)
