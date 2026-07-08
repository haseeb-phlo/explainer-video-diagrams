#!/usr/bin/env python3
"""Build claude_intro.excalidraw - ONE flowing, illustrated explainer
for the "Claude interface, properly" training video (Phlo AI training, ~4 min).

Style B (house style): a single hand-drawn journey, left-to-right, NO frames, NO
boxes, white canvas, everything in the hand font (fontFamily 1), roughness 1. A
lively Excalidraw palette colour-coded per beat, big colour-blocking, scribbled
annotations and charming primitive illustrations. Modelled on the canonical
videos/claude/3-artefacts build; the look lives in the shared excalidraw_kit.

Run:  python3 build_claude_interface.py   # writes the file, reloads, asserts, prints counts
      python3 ../../../preview.py claude_intro.excalidraw out.png
"""
import os
import sys

_d = os.path.dirname(os.path.abspath(__file__))
while _d != os.path.dirname(_d) and not os.path.exists(os.path.join(_d, "excalidraw_kit.py")):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)

import random
from excalidraw_kit import *

random.seed(40404)  # deterministic - re-runs produce identical files

# ----------------------------------------------------------------------------
# THE HERO ILLUSTRATION - a Claude.ai window with all five parts drawn,
# so every callout arrow lands on a real element. Returns anchor points.
# ----------------------------------------------------------------------------
def claude_window_full(x, y, w, h):
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="cwin")
    line(x, y + 44, [[0, 0], [w, 0]], stroke=GREY, sw=1)
    for k in range(3):
        ellipse(x + 20 + k * 20, y + 16, 11, 11, stroke=GREY, bg=GREY, sw=1)
    # sidebar -> Projects
    sb_x, sb_w = x + 18, 248
    rect(sb_x, y + 56, sb_w, h - 74, stroke="transparent", bg=VIOLET_BG, sw=1, rough=1,
         rounded=True, fill="solid", opacity=45, prefix="side")
    for k in range(4):
        rect(sb_x + 20, y + 78 + k * 54, sb_w - 40, 30, stroke="transparent", bg=WHITE,
             sw=1, rough=1, rounded=True, prefix="srow")
    # chat -> Conversations
    cx = sb_x + sb_w + 44
    cw = w * 0.42
    my = y + 78
    for f in (1.0, 0.7, 0.92):
        rect(cx, my, cw * f, 32, stroke="transparent", bg=FAINT, sw=1, rough=1,
             rounded=True, prefix="msg")
        my += 50
    # model chip -> Model picker
    chip_w = 178
    chip_x = x + w - chip_w - 26
    rect(chip_x, y + 58, chip_w, 46, stroke=TEAL, bg=TEAL_BG, sw=2, rough=1, rounded=True, prefix="mchip")
    text(chip_x + 20, y + 70, "Sonnet  v", size=SMALL, color=TEAL)
    # artifact panel -> Artifacts
    pw = 210
    px = x + w - pw - 26
    py = y + 126
    ph = (y + h - 26) - py
    rect(px, py, pw, ph, stroke=BLUE, bg=BLUE_BG, sw=2, rough=1, rounded=True,
         fill="solid", opacity=45, prefix="panel")
    rect(px, py, 9, ph, stroke=BLUE, bg=BLUE, sw=1, rough=1, rounded=False, prefix="pedge")
    text(px + 24, py + 16, "Artifact", size=SMALL, color=BLUE)
    # input bar + paperclip -> File uploads
    ib_x = cx
    ib_y = y + h - 66
    ib_w = (px - 26) - ib_x
    rect(ib_x, ib_y, ib_w, 44, stroke=GREY, bg=WHITE, sw=2, rough=1, rounded=True, prefix="input")
    pc_x, pc_y = ib_x + 18, ib_y + 10
    line(pc_x, pc_y, [[0, 0], [0, 24], [15, 24], [15, 6], [7, 6], [7, 18]],
         stroke=GREEN, sw=3, rough=1, prefix="clip")
    return {
        "sidebar": (sb_x + sb_w * 0.5, y + 130),
        "chat":    (cx + cw * 0.45, y + 110),
        "chip":    (chip_x + 6, y + 80),
        "panel":   (px + 4, py + ph * 0.5),
        "clip":    (pc_x + 8, ib_y + 12),
    }

# ----------------------------------------------------------------------------
# BEAT SCAFFOLD - wide gaps so a single beat frames cleanly on a 14" laptop.
# Every beat uses the SAME ~1120-wide x ~980-tall slot (~1.15 : 1) so framing is
# identical and fits a 14" MacBook screen.
# ----------------------------------------------------------------------------
N = 4
GAP = 800
WID = dict.fromkeys(range(1, N + 1), 1200)
ACCENT = {1: VIOLET, 2: BLUE, 3: YELLOW, 4: GREEN}
OX, _c = {}, 0
for _i in range(1, N + 1):
    OX[_i] = _c
    _c += WID[_i] + GAP
TOTAL_W = _c

HEAD_Y = 60

def head(ox, title, accent, sub=None):
    """QUIET heading: kit heading() draws a prominent hand title in the beat's
    accent colour + a lively hand underline. No step circle, no highlighter sweep,
    no scribble of its own."""
    heading(ox, HEAD_Y, title, color=accent, sub=sub)

# ============================================================================
# BOARD TITLE
# ============================================================================
text(OX[1], -300, "The interface, properly", size=HERO, color=INK)
text(OX[1] + 6, -300 + HERO * LINE_H + 4,
     "five things on screen most people never touch", size=H2, color=VIOLET)
text(OX[1] + 6, -300 + HERO * LINE_H + 4 + H2 * LINE_H + 8,
     "- and they're where the productivity is", size=H3, color=GREYD)

# ============================================================================
# BEAT 1 - ONE WINDOW, FIVE PARTS (the hero map)
# ============================================================================
ox = OX[1]
head(ox, "One window. Five parts.", ACCENT[1])
# Compact hero: a wide-but-short Claude window across the top, with the five
# callouts stacked in a 2-column grid below, arrows pointing UP to real anchors.
win_x, win_y, win_w, win_h = ox + 30, 250, 1100, 300
anch = claude_window_full(win_x, win_y, win_w, win_h)

def callout(sx, sy, w, h, n, accent, abg, title, body, target):
    sticky(sx, sy, w, h, abg, angle=jit(1.3))
    num_badge(sx + 16, sy + 16, n, accent)
    text(sx + 78, sy + 24, title, size=H3, color=accent)
    text(sx + 30, sy + 80, body, size=SMALL, color=INK)
    # arrow from the top edge of the sticky up to its target anchor in the window
    fx0, fy0 = sx + w * 0.5, sy
    arrow(fx0, fy0, [[0, 0], [target[0] - fx0, target[1] - fy0]], stroke=accent, sw=3, rough=1)

col_l, col_r = ox + 30, ox + 600
row1, row2, row3 = 600, 800, 1000
cw, ch = 530, 180
# Callouts assigned by SIDE so arrows stay short + don't cross: left-column
# callouts point to left/centre anchors, right-column to right-side anchors.
# LEFT column: Projects -> sidebar | Conversations -> chat | File uploads -> clip
callout(col_l, row1, cw, ch, 2, VIOLET, VIOLET_BG, "Projects",
        "The multiplier. Persistent\ninstructions, files and memory\nacross every chat. (Video 2.2)",
        anch["sidebar"])
callout(col_l, row2, cw, ch, 1, ORANGE, ORANGE_BG, "Conversations",
        "Where most people live.\nUseful, but volatile - context\ndoesn't carry between chats.",
        anch["chat"])
callout(col_l, row3, cw, 120, 4, GREEN, GREEN_BG, "File uploads",
        "PDFs, images, spreadsheets, code -\nClaude reads them. Most underused.",
        anch["clip"])
# RIGHT column: Model picker -> chip (top-right) | Artifacts -> panel (right)
callout(col_r, row1, cw, 120, 5, TEAL, TEAL_BG, "Model picker",
        "Match the model to the task.",
        anch["chip"])
callout(col_r, row2, cw, ch, 3, BLUE, BLUE_BG, "Artifacts",
        "When Claude builds a document\nor tool, not just text. A side\npanel - persistent, editable.",
        anch["panel"])
# Safety caution on uploads (SKILL.md guardrail) - generic, no clinical wording.
warn_x, warn_y = col_r, row3 + 30
line(warn_x, warn_y + 34, [[0, 0], [18, -34], [36, 0], [0, 0]],
     stroke=RED, sw=3, rough=1, bg=RED_BG, fill="solid", prefix="warn")
text(warn_x + 13, warn_y + 4, "!", size=H3, color=RED)
chip(warn_x + 58, warn_y, "Never upload confidential data",
     fill=RED_BG, text_color=RED, border=RED, size=SMALL, angle=0.0)

# ============================================================================
# BEAT 2 - PICK THE MODEL DELIBERATELY
# ============================================================================
ox = OX[2]
head(ox, "Pick the model deliberately", ACCENT[2])

def opus_illus(cx, cy, accent):     # heavy: a stacked weight
    rect(cx - 60, cy + 40, 120, 24, stroke=INK, bg=accent, sw=2, rough=1, rounded=True)
    rect(cx - 42, cy + 18, 84, 24, stroke=INK, bg=accent, sw=2, rough=1, rounded=True)
    rect(cx - 24, cy - 4, 48, 24, stroke=INK, bg=accent, sw=2, rough=1, rounded=True)

def sonnet_illus(cx, cy, accent):   # balanced: a little balance scale (no sparkle)
    line(cx, cy - 8, [[0, 0], [0, 50]], stroke=accent, sw=3, rough=1)        # post
    line(cx - 44, cy, [[0, 0], [88, 0]], stroke=accent, sw=3, rough=1)       # beam
    line(cx, cy + 50, [[0, 0], [-24, 0], [24, 0]], stroke=accent, sw=3, rough=1)  # foot
    ellipse(cx - 58, cy + 6, 28, 16, stroke=accent, bg=accent, sw=2, rough=1)     # left pan
    ellipse(cx + 30, cy + 6, 28, 16, stroke=accent, bg=accent, sw=2, rough=1)     # right pan

def haiku_illus(cx, cy, accent):    # light + fast: motion lines + a zippy dot
    for k, ln in enumerate((100, 76, 52)):
        line(cx - 50, cy + 8 + k * 20, [[0, 0], [ln, 0]], stroke=accent, sw=4, rough=1)
    ellipse(cx + 56, cy + 20, 14, 14, stroke=accent, bg=accent, sw=2)

cards = [
    ("Opus", "Claude Opus 4.8", "Deep reasoning, long-form writing,\ncomplex analysis. Slowest, deepest.",
     INDIGO, INDIGO_BG, opus_illus, None),
    ("Sonnet", "Claude Sonnet 4.6", "Balanced speed and quality.\nMost day-to-day work.",
     GREEN, GREEN_BG, sonnet_illus, "DEFAULT"),
    ("Haiku", "Claude Haiku 4.5", "Fast and light.\nQuick lookups, simple drafts.",
     YELLOW, YELLOW_BG, haiku_illus, None),
]
cw, cy0, ch, cvg = 1100, 250, 200, 20
for k, (name, sub, body, acc, abg, illus, tag) in enumerate(cards):
    cy = cy0 + k * (ch + cvg)
    sticky(ox + 30, cy, cw, ch, abg, angle=jit(1.0))
    text(ox + 70, cy + 24, name, size=H2, color=acc)
    text(ox + 70, cy + 80, sub, size=SMALL, color=GREYD)
    if tag:
        chip(ox + 70, cy + 130, tag, fill=acc, text_color=WHITE, border=acc, size=SMALL)
    illus(ox + cw - 220, cy + 90, acc)
    text(ox + cw - 480, cy + 24, body, size=BODY, color=INK)
# usage note + a faster->deeper gradient of chips
fy = cy0 + 3 * (ch + cvg) + 12
text(ox + 30, fy, "Heavier models think longer and use more of your\nallowance.  Lighter ones are faster.",
     size=BODY, color=GREYD)
gy = fy + 96
gx = ox + 30
text(gx, gy + 10, "faster", size=SMALL, color=GREY)
gx += 120
for lab, acc, abg in [("Haiku", YELLOW, YELLOW_BG), ("Sonnet", GREEN, GREEN_BG), ("Opus", INDIGO, INDIGO_BG)]:
    w, h = chip(gx, gy, lab, fill=abg, text_color=acc, border=acc, size=SMALL)
    gx += w
    arrow(gx + 6, gy + h / 2, [[0, 0], [36, 0]], stroke=GREY, sw=3)
    gx += 48
text(gx + 6, gy + 10, "deeper", size=SMALL, color=GREY)
text(ox + 30, gy + 70, "Switch any time - even mid-conversation.", size=BODY, color=GREYD)

# ============================================================================
# BEAT 3 - PAUSE HERE, AND TRY IT
# ============================================================================
ox = OX[3]
head(ox, "Pause here, and try it", ACCENT[3])
pause_icon(ox + 40, 322, 76, color=YELLOW)
highlighter(ox + 150, 318, 960, 130, YELLOW_BG, angle=0.0)
text(ox + 174, 336, "Open Claude. Switch to a model that\nisn't your default. Run one prompt.",
     size=H3, color=INK)
ex_x = ox + 60
for lab in ["try Opus", "or Haiku", "notice the difference"]:
    w, h = chip(ex_x, 560, lab, fill=WHITE, text_color=YELLOW, border=YELLOW, size=SMALL)
    ex_x += w + 40
text(ox + 60, 700, "60 seconds - then carry on.", size=BODY, color=GREYD)
# hands-on beat -> cue the recorder to cut to the live app
demo_badge(ox + 60, 820, "show in Claude desktop app:  the model picker")

# ============================================================================
# BEAT 4 - FIVE FEATURES, FOUR MINUTES (close)
# ============================================================================
ox = OX[4]
head(ox, "Five features. Four minutes.", ACCENT[4])
recap = [("Conversations", ORANGE, ORANGE_BG), ("Projects", VIOLET, VIOLET_BG),
         ("Artifacts", BLUE, BLUE_BG), ("File uploads", GREEN, GREEN_BG),
         ("Model picker", TEAL, TEAL_BG)]
# the five features recapped as a vertical stack of chips
ry = 260
for lab, acc, abg in recap:
    w, h = chip(ox + 40, ry, lab, fill=abg, text_color=acc, border=acc, size=BODY)
    ry += h + 24
nxt = "Next: Projects - the one that compounds for years."
text(ox + 40, ry + 30, nxt, size=H3, color=INK)
circle_around(ox + 40 + text_w("Next: ", H3) - 6, ry + 24, text_w("Projects", H3) + 24,
              H3 * LINE_H + 16, VIOLET, sw=3)
# roadmap - the rest of the Claude module (planned, not yet shipped)
rdy = ry + 120
text(ox + 40, rdy, "Later in this module:", size=SMALL, color=GREY)
rmx = ox + 40
for lab in ["Skills", "Scheduled tasks", "Connectors (MCP)", "Cowork", "+ more"]:
    w, h = chip(rmx, rdy + 40, lab, fill=WHITE, text_color=GREYD, border=FAINT, size=SMALL)
    rmx += w + 22
text(ox + 40, rdy + 130, "Docs: Claude Help Centre - support.claude.com", size=SMALL, color=VIOLET)

# No connector spine and no branding footer: beats read as one picture through
# consistent layout + rhythm (the natural-flow look), not arrows in the gaps.

# ----------------------------------------------------------------------------
# WRITE + VALIDATE  (shared excalidraw_kit)
# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "claude_intro.excalidraw")
MAXW = max(WID.values()) + 200
finish(out, MAXW, TOTAL_W)
