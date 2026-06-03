#!/usr/bin/env python3
"""Build phlo-2.2-claude-projects.excalidraw - ONE flowing, illustrated explainer
for the "Claude Projects" training video (Phlo AI training, module 2.2, ~7 min).

Style B (house style): a single hand-drawn journey, left-to-right, NO frames, NO
boxes, white canvas, everything in Excalifont (fontFamily 5), roughness 1, a lively
colour-coded Excalidraw palette, big colour-blocking, scribbled annotations,
charming primitive illustrations and a load-bearing connector spine. Self-contained,
embeds its own helpers + palette as the repo convention requires. Converted from the
old 10-frame editorial "Style A" deck of the same name.

Run:  python3 build_projects.py
      python3 ../3-artefacts/preview.py phlo-2.2-claude-projects.excalidraw out.png
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
GAP = 1800
WID = {1: 2500, 2: 2750, 3: 2550, 4: 3000, 5: 2200, 6: 2500, 7: 2350, 8: 2050, 9: 2550}
ACCENT = {1: RED, 2: VIOLET, 3: BLUE, 4: GREEN, 5: ORANGE, 6: TEAL, 7: INDIGO, 8: YELLOW, 9: VIOLET}
ABG = {1: RED_BG, 2: VIOLET_BG, 3: BLUE_BG, 4: GREEN_BG, 5: ORANGE_BG, 6: TEAL_BG,
       7: INDIGO_BG, 8: YELLOW_BG, 9: VIOLET_BG}
OX, _c = {}, 0
for _i in range(1, 10):
    OX[_i] = _c
    _c += WID[_i] + GAP
TOTAL_W = _c
HEAD_Y = 60
MY = 620

def beat_head(i, title, sub=None):
    ox = OX[i]; acc, abg = ACCENT[i], ABG[i]
    num_circle(ox, HEAD_Y, i, acc)
    tx = ox + 86
    tw = text_w(title, H1, HAND)
    highlighter(tx - 8, HEAD_Y + 2, tw + 50, H1 * LINE_H + 14, abg)
    text(tx, HEAD_Y + 6, title, size=H1, color=INK)
    scribble_underline(tx, HEAD_Y + 6 + H1 * LINE_H + 8, min(tw, 480), acc, sw=4)
    if sub:
        text(tx, HEAD_Y + 6 + H1 * LINE_H + 26, sub, size=BODY, color=GREYD)
    return ox

# ============================================================================
# BOARD TITLE
# ============================================================================
text(OX[1], -300, "Claude Projects", size=HERO, color=INK)
sparkles(OX[1] + text_w("Claude Projects", HERO) + 70, -230, VIOLET)
text(OX[1] + 6, -300 + HERO * LINE_H + 4, "the multiplier - set up once, use forever", size=H2, color=VIOLET)
text(OX[1] + 6, -300 + HERO * LINE_H + 4 + H2 * LINE_H + 10,
     "Phlo AI training  -  module 2.2  -  about 7 minutes", size=SMALL, color=GREY)

# ============================================================================
# BEAT 1 - THE TAX YOU PAY EVERY MORNING
# ============================================================================
ox = beat_head(1, "The tax you pay every morning")
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
dw, dgap, dy = 360, 40, 330
for k, d in enumerate(days):
    dx = ox + 40 + k * (dw + dgap)
    sticky(dx, dy, dw, 190, RED_BG, angle=jit(1.6))
    text(dx + 26, dy + 22, d, size=BODY, color=RED)
    text(dx + 26, dy + 70, "Who I am - my role -\nPhlo's tone - the\ndo-not-say list ...", size=SMALL, color=INK)
    arrow(dx + dw / 2, dy + 190, [[0, 0], [0, 36]], stroke=RED, sw=2, rough=1)
text(ox + 40, dy + 240, "the same brief, re-pasted every single morning", size=SMALL, color=GREYD)
clock(ox + 120, 660, 46, RED)
text(ox + 190, 636, "~10 min a day", size=H3, color=INK)
text(ox + 190, 686, "= about 1 hour a week. Every week.", size=H3, color=RED)
text(ox + 40, 780, "Re-explaining yourself is invisible work. It adds up.", size=BODY, color=GREYD)

# ============================================================================
# BEAT 2 - WHAT A PROJECT ACTUALLY IS
# ============================================================================
ox = beat_head(2, "What a Project actually is")
cont_x, cont_y, cont_w, cont_h = ox + 40, 300, WID[2] - 120, 430
rect(cont_x, cont_y, cont_w, cont_h, stroke=VIOLET, bg=VIOLET_BG, sw=3, rough=1, rounded=True,
     fill="solid", opacity=22, angle=jit(0.8))
text(cont_x + 28, cont_y + 18, "ONE PROJECT", size=H3, color=VIOLET)
parts = [("Custom instructions", "Your standing brief: role,\nPhlo's voice, what to avoid.", obj_doc, VIOLET, VIOLET_BG),
         ("Knowledge files", "Reference docs Claude reads\nbefore every reply.", obj_files, BLUE, BLUE_BG),
         ("Conversations", "Every chat here shares the\ntwo above - automatically.", None, GREEN, GREEN_BG)]
pw = (cont_w - 80) / 3
for k, (ttl, body, illus, acc, abg) in enumerate(parts):
    px = cont_x + 20 + k * (pw + 10)
    sticky(px, cont_y + 70, pw - 10, cont_h - 110, WHITE, angle=jit(0.8))
    rect(px, cont_y + 70, pw - 10, cont_h - 110, stroke=acc, bg="transparent", sw=2, rough=1, rounded=True)
    text(px + 26, cont_y + 92, ttl, size=H3, color=acc)
    if illus:
        illus(px + 30, cont_y + 150, acc, abg)
    else:
        for m in range(3):
            rect(px + 30, cont_y + 150 + m * 34, pw - 110, 24, stroke="transparent", bg=FAINT, sw=1, rounded=True, prefix="msg")
    text(px + 26, cont_y + 300, body, size=SMALL, color=INK)
text(cont_x + 20, cont_y + cont_h + 30, "One persistent space. Context lives here, not in your clipboard.", size=H3, color=VIOLET)

# ============================================================================
# BEAT 3 - THE SHIFT (before -> after)
# ============================================================================
ox = beat_head(3, "The shift")
# BEFORE
bx, by = ox + 40, 340
text(bx, by - 40, "BEFORE", size=H3, color=RED)
for k in range(3):
    sticky(bx + k * 26, by + k * 22, 300, 90, FAINT, angle=jit(2.0))
text(bx + 60, by + 28, "context ...\ncontext ...", size=SMALL, color=GREYD)
arrow(bx + 240, by + 150, [[0, 0], [40, 60]], stroke=RED, sw=3, rough=1)
claude_face(bx + 150, by + 320, r=42, color=RED)
text(bx + 40, by + 400, "paste it all, every time", size=SMALL, color=RED)
# arrow across
arrow(bx + 430, by + 180, [[0, 0], [220, 0]], stroke=BLUE, sw=6, rough=1)
text(bx + 470, by + 120, "write it once", size=BODY, color=BLUE)
# AFTER
ax = bx + 720
text(ax, by - 40, "AFTER", size=H3, color=BLUE)
rect(ax, by, 360, 300, stroke=BLUE, bg=BLUE_BG, sw=3, rough=1, rounded=True, fill="solid", opacity=30, angle=jit(-1.0))
text(ax + 110, by + 24, "Project", size=H2, color=BLUE)
text(ax + 40, by + 110, "the brief lives here\nand never moves", size=SMALL, color=INK)
sparkles(ax + 300, by + 40, BLUE)
claude_face(ax + 180, by + 400, r=42, color=BLUE)
text(ax + 70, by + 470, "context is permanent", size=SMALL, color=BLUE)
text(ox + 40, 868, "Write the brief once. Claude applies it every time.", size=H3, color=BLUE)

# ============================================================================
# BEAT 4 - THREE PROJECTS YOU COULD BUILD THIS WEEK
# ============================================================================
ox = beat_head(4, "Three Projects you could build this week")
projects = [
    ("A", "Patient comms drafting", "Patient Care + Pharmacy",
     "Phlo tone guide - examples of\ngreat replies - the do-not-say list", GREEN, GREEN_BG, True),
    ("B", "Engineering PR review", "Engineering",
     "coding standards - common review\npatterns - Phlo style guide", BLUE, BLUE_BG, False),
    ("C", "Weekly board prep", "Leadership",
     "board memo format - the last four\nmemos - the questions the board\ncares about", ORANGE, ORANGE_BG, False),
]
cw, cgap, cy0, ch = 860, 100, 320, 430
for k, (letter, ttl, who, files, acc, abg, gate) in enumerate(projects):
    cx = ox + 40 + k * (cw + cgap)
    sticky(cx, cy0, cw, ch, abg, angle=jit(1.2))
    ellipse(cx + 24, cy0 + 24, 52, 52, stroke=acc, bg=acc, sw=2)
    text_centered(cx + 50, cy0 + 36, letter, size=H2, color=WHITE)
    text(cx + 96, cy0 + 34, ttl, size=H3, color=acc)
    text(cx + 36, cy0 + 120, "Who: " + who, size=BODY, color=INK)
    text(cx + 36, cy0 + 180, "Knowledge:", size=SMALL, color=GREYD)
    text(cx + 36, cy0 + 214, files, size=SMALL, color=INK)
    if gate:
        rect(cx + 36, cy0 + ch - 96, cw - 72, 64, stroke=RED, bg=RED_BG, sw=2, rough=1, rounded=True, fill="solid", opacity=30)
        text(cx + 54, cy0 + ch - 82, "Drafts only - a person checks\nand sends. Never auto-sent.", size=SMALL, color=RED)

# ============================================================================
# BEAT 5 - THE MATHS
# ============================================================================
ox = beat_head(5, "The maths")
base = 760
line(ox + 60, base, [[0, 0], [560, 0]], stroke=INK, sw=2)
# setup bar (small) vs saving bar (big)
rect(ox + 120, base - 90, 150, 90, stroke=INK, bg=ORANGE, sw=2, rough=1, rounded=False)
text_centered(ox + 195, base + 14, "Setup", size=SMALL, color=GREYD)
text_centered(ox + 195, base - 130, "20 min\nonce", size=SMALL, color=ORANGE)
rect(ox + 360, base - 360, 150, 360, stroke=INK, bg=GREEN, sw=2, rough=1, rounded=False)
text_centered(ox + 435, base + 14, "Saving", size=SMALL, color=GREYD)
text_centered(ox + 435, base - 400, "hours\nevery week", size=SMALL, color=GREEN)
text(ox + 660, 360, "Setup:  20 minutes.  Once.", size=H3, color=ORANGE)
text(ox + 660, 430, "Saving:  hours every week -", size=H3, color=GREEN)
text(ox + 660, 470, "for as long as you do the job.", size=H3, color=GREEN)
highlighter(ox + 656, 560, 920, 60, ORANGE_BG, angle=0.0)
text(ox + 670, 572, "The best twenty minutes you'll spend this month.", size=BODY, color=INK)
sparkles(ox + 1620, 400, ORANGE)

# ============================================================================
# BEAT 6 - WHY IT'S A MULTIPLIER
# ============================================================================
ox = beat_head(6, "Why it's a multiplier")
sx, sy = ox + 80, 420
claude_face(sx, sy, r=48, color=TEAL)
text_centered(sx, sy + 80, "builds the\nProject once", size=SMALL, color=GREYD)
fan_x = sx + 420
for k in range(4):
    py = sy - 150 + k * 110
    arrow(sx + 70, sy, [[0, 0], [fan_x - sx - 110, py - sy + 30]], stroke=GREY, sw=2, rough=1)
    person(fan_x + 40, py + 30, TEAL)
text(fan_x + 110, sy - 130, "the whole team uses it", size=H3, color=TEAL)
text(ox + 40, 760, "One person builds Patient Comms. The clinical team drafts in Phlo's voice from day one.", size=BODY, color=INK)
text(ox + 40, 810, "Sharing is available on Team and Enterprise plans.", size=SMALL, color=GREY)

# ============================================================================
# BEAT 7 - LET'S BUILD ONE, LIVE
# ============================================================================
ox = beat_head(7, "Let's build one - live")
steps = ["Name it, and set who can see it",
         "Write the custom instructions",
         "Add two or three reference files, then chat"]
for k, s in enumerate(steps):
    sy = 330 + k * 130
    num_circle(ox + 50, sy, k + 1, INDIGO, d=64)
    sticky(ox + 140, sy, 1400, 96, INDIGO_BG, angle=jit(0.8))
    text(ox + 176, sy + 28, s, size=H3, color=INK)
demo_badge(ox + 140, 330 + 3 * 130 + 10, "live demo:  building a Patient Comms Project")

# ============================================================================
# BEAT 8 - PAUSE HERE, AND TRY IT
# ============================================================================
ox = beat_head(8, "Pause here, and try it")
pause_icon(ox + 40, 322, 80, color=YELLOW)
sparkles(ox + 90, 300, YELLOW)
lines8 = ["Think of one task you repeat.",
          "Open claude.ai/projects and create it now - even empty.",
          "Fill it as you watch the rest of this module."]
for k, s in enumerate(lines8):
    text(ox + 170, 332 + k * 70, s, size=H3, color=INK)
text(ox + 170, 332 + 3 * 70 + 16, "two minutes - then carry on.", size=BODY, color=GREYD)

# ============================================================================
# BEAT 9 - ONE PROJECT, TWENTY MINUTES (close)
# ============================================================================
ox = beat_head(9, "One Project. Twenty minutes.")
highlighter(ox + 36, 318, 1500, 70, VIOLET_BG, angle=0.0)
text(ox + 50, 330, "Use it once a day for a month.", size=H3, color=INK)
text(ox + 50, 396, "Then tell me Projects didn't change how you work.", size=H3, color=VIOLET)
text(ox + 40, 510, "Resources", size=H3, color=VIOLET)
sparkle(ox + 56, 580, 14, VIOLET)
text(ox + 90, 566, "Anthropic Help Centre - 'How can I create and manage projects' (support.claude.com)", size=SMALL, color=VIOLET)
sparkle(ox + 56, 624, 14, VIOLET)
text(ox + 90, 610, "AI Ops Learn - Prompt Library - Phlo's shared Projects", size=SMALL, color=VIOLET)
text(ox + 40, 720, "Phlo  -  AI Ops", size=SMALL, color=GREY)

# ============================================================================
# CONNECTOR SPINE
# ============================================================================
for i in range(1, 9):
    x0 = OX[i] + WID[i]; x1 = OX[i + 1]; acc = ACCENT[i + 1]
    arrow(x0 + 20, MY, [[0, 0], [(x1 - x0) * 0.4, -36], [(x1 - x0) * 0.6, 30], [x1 - x0 - 40, 0]],
          stroke=acc, sw=4, rough=1)
line(OX[1] + 40, MY + 340, [[0, 0], [TOTAL_W - 400, 0]], stroke=FAINT, sw=2, rough=1, dashed=True, opacity=60)

# ----------------------------------------------------------------------------
# WRITE + VALIDATE  (shared excalidraw_kit)
# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "phlo-2.2-claude-projects.excalidraw")
MAXW = max(WID.values()) + 200
finish(out, MAXW, TOTAL_W)
