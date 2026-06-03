#!/usr/bin/env python3
"""Build 2-3-artifacts.excalidraw - ONE flowing, illustrated explainer for the
"Artifacts" training video (Phlo AI training, module 2.3).

Design: a single hand-drawn journey that reads left-to-right - NO frames, NO
boxes, white canvas, everything in Excalifont (fontFamily 5), roughness 1. A
lively Excalidraw palette, colour-coded per beat, with big colour blocking,
scribbled annotations, charming primitive illustrations and a load-bearing
connector spine that threads the nine beats into one picture.

This replaces the old boxed "Riso Workshop" 12-frame storyboard. The flowing
style mirrors llm_explainer.excalidraw, which the team preferred.

Run:  python3 build_excalidraw.py   # writes the file, reloads it, asserts, prints counts
      python3 preview.py            # rasterise an approximate PNG to eyeball
"""
import os
import sys

_d = os.path.dirname(os.path.abspath(__file__))
while _d != os.path.dirname(_d) and not os.path.exists(os.path.join(_d, "excalidraw_kit.py")):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)

import random
from excalidraw_kit import *

random.seed(20230)  # deterministic - re-runs produce identical files

OBJS = [
    (obj_doc, "one-pager", BLUE, BLUE_BG),
    (obj_calc, "calculator", GREEN, GREEN_BG),
    (obj_app, "mini-app", VIOLET, VIOLET_BG),
    (obj_chart, "chart", ORANGE, ORANGE_BG),
    (obj_diagram, "diagram", TEAL, TEAL_BG),
    (obj_file, "Word / PPT\nExcel / PDF", YELLOW, YELLOW_BG),
]

# ----------------------------------------------------------------------------
# BEAT SCAFFOLD
# ----------------------------------------------------------------------------
# Wide gaps so a single beat can be framed on a 14" laptop without neighbours
# peeking in - the empty space IS the zoom-to-one-beat affordance.
GAP = 1800
WID = {1: 2300, 2: 2050, 3: 2350, 4: 1950, 5: 2100, 6: 2500, 7: 2200, 8: 2000, 9: 1900}
ACCENT = {1: ORANGE, 2: VIOLET, 3: BLUE, 4: GREEN, 5: TEAL, 6: VIOLET, 7: INDIGO, 8: RED, 9: YELLOW}
ABG = {1: ORANGE_BG, 2: VIOLET_BG, 3: BLUE_BG, 4: GREEN_BG, 5: TEAL_BG, 6: VIOLET_BG,
       7: INDIGO_BG, 8: RED_BG, 9: YELLOW_BG}
OX = {}
_c = 0
for _i in range(1, 10):
    OX[_i] = _c
    _c += WID[_i] + GAP
TOTAL_W = _c

HEAD_Y = 60          # heading baseline band
MY = 620             # mid-height for the connector spine

def beat_head(i, title, sub=None):
    ox = OX[i]
    acc, abg = ACCENT[i], ABG[i]
    # step circle
    ellipse(ox, HEAD_Y, 60, 60, stroke=acc, bg=WHITE, sw=3, rough=1)
    text_centered(ox + 30, HEAD_Y + 12, str(i), size=H2, color=acc)
    tx = ox + 86
    tw = text_w(title, H1, HAND)
    highlighter(tx - 8, HEAD_Y + 2, tw + 50, H1 * LINE_H + 14, abg)
    text(tx, HEAD_Y + 6, title, size=H1, color=INK)
    scribble_underline(tx, HEAD_Y + 6 + H1 * LINE_H + 8, min(tw, 420), acc, sw=4)
    if sub:
        text(tx, HEAD_Y + 6 + H1 * LINE_H + 26, sub, size=BODY, color=GREYD)
    return ox

# ----------------------------------------------------------------------------
# BOARD TITLE
# ----------------------------------------------------------------------------
text(OX[1], -300, "Artifacts", size=HERO, color=INK)
sparkles(OX[1] + text_w("Artifacts", HERO) + 70, -230, ORANGE)
text(OX[1] + 6, -300 + HERO * LINE_H + 4, "when Claude makes things, not just text",
     size=H2, color=VIOLET)
text(OX[1] + 6, -300 + HERO * LINE_H + 4 + H2 * LINE_H + 10,
     "Phlo AI training  -  module 2.3  -  about 5 minutes", size=SMALL, color=GREY)

# ============================================================================
# BEAT 1 - HOOK + CORE IDEA
# ============================================================================
ox = beat_head(1, "Ask, and Claude builds it",
               "the feature that turns Claude from advisor into maker")
# the hook: chat bubble -> arrow -> a real calculator with a burst
by = 360
bw, bh = 520, 130
sticky(ox + 40, by, bw, bh, GREY, angle=jit(1.5))
text(ox + 72, by + 30, "build me a tool to work\nout days of supply", size=BODY, color=WHITE)
line(ox + 90, by + bh, [[0, 0], [-18, 30], [22, -2]], stroke=GREY, sw=3)  # tail
arrow(ox + 40 + bw + 30, by + bh / 2, [[0, 0], [150, 0]], stroke=ORANGE, sw=5, rough=1)
# burst behind calc
calc_x = ox + 40 + bw + 240
ellipse(calc_x - 30, by - 20, 200, 200, stroke=ORANGE, bg=ORANGE_BG, sw=2, rough=1,
        fill="solid", opacity=55)
sparkles(calc_x + 150, by - 10, ORANGE)
obj_calc(calc_x, by + 4)
text(calc_x - 10, by + 168, "the actual thing - not a\ndescription of it", size=SMALL, color=ORANGE)
# advisor -> maker motif
amy = 560
text(ox + 40, amy, "advisor", size=H3, color=GREY)
line(ox + 40, amy + 22, [[0, 0], [text_w('advisor', H3) + 6, 4]], stroke=RED, sw=3)  # strike
arrow(ox + 40 + text_w("advisor", H3) + 24, amy + 18, [[0, 0], [70, 0]], stroke=GREEN, sw=4)
text(ox + 40 + text_w("advisor", H3) + 110, amy, "maker", size=H3, color=GREEN)

# ============================================================================
# BEAT 2 - WORDS LEFT, THING RIGHT
# ============================================================================
ox = beat_head(2, "Words left, a thing right")
cw_x, cw_y, cw_w, cw_h = ox + 40, 300, WID[2] - 120, 460
claude_window(cw_x, cw_y, cw_w, cw_h, tiny=obj_doc)
# annotation arrows
text(cw_x - 20, cw_y + cw_h + 30, "the chat, like always", size=SMALL, color=GREY)
arrow(cw_x + cw_w * 0.72, cw_y + cw_h + 60, [[0, 0], [80, -70]], stroke=VIOLET, sw=3, rough=1)
text(cw_x + cw_w * 0.62, cw_y + cw_h + 64,
     "a panel holding something\nyou can edit, run and reuse", size=SMALL, color=VIOLET)
text(cw_x, cw_y - 56, "Words on the left.  A thing you can use on the right.",
     size=H3, color=VIOLET)

# ============================================================================
# BEAT 3 - IT CAN BE ALMOST ANYTHING
# ============================================================================
ox = beat_head(3, "It can be almost anything")
# playful cluster - two rows, jittered
positions = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1)]
cellw, cellh = 700, 250
gx, gy = ox + 60, 320
for (fn, cap, acc, abg), (cxi, cyi) in zip(OBJS, positions):
    bx = gx + cxi * cellw + random.uniform(-20, 20)
    byy = gy + cyi * cellh + random.uniform(-14, 14)
    sticky(bx - 20, byy - 24, 210, 234, abg, angle=jit(2.2))
    fn(bx, byy)
    text_centered(bx + 65, byy + 168, cap, size=SMALL, color=acc, angle=jit(2.0))

# ============================================================================
# BEAT 4 - TWO WAYS YOU GET ONE
# ============================================================================
ox = beat_head(4, "Two ways you get one")
note_y, note_w, note_h = 320, 820, 420
# left: appears on its own
sticky(ox + 40, note_y, note_w, note_h, GREEN_BG, angle=jit(1.6))
text(ox + 80, note_y + 36, "Appears on its own", size=H3, color=GREEN)
for k, item in enumerate(["long documents", "code", "tables and structured output",
                          "anything you'll clearly reuse"]):
    text(ox + 96, note_y + 120 + k * 64, "- " + item, size=BODY, color=INK)
# right: ask on purpose
rx = ox + 40 + note_w + 120
sticky(rx, note_y, note_w, note_h, BLUE_BG, angle=jit(-1.4))
text(rx + 40, note_y + 36, "Ask for one on purpose", size=H3, color=BLUE)
chip(rx + 56, note_y + 150, "make me a one-page Artifact summarising X",
     fill=WHITE, text_color=BLUE, border=BLUE, size=SMALL)
chip(rx + 56, note_y + 250, "build me a tool to calculate Y",
     fill=WHITE, text_color=BLUE, border=BLUE, size=SMALL)

# ============================================================================
# BEAT 5 - CLAY, NOT STONE
# ============================================================================
ox = beat_head(5, "It's clay, not stone")
flow = ["build", "edit on the spot", "ask Claude to refine"]
fx, fy = ox + 50, 340
for k, lab in enumerate(flow):
    w, h = chip(fx, fy, lab, fill=TEAL_BG, text_color=INK, border=TEAL, size=BODY)
    if k < len(flow) - 1:
        arrow(fx + w + 10, fy + h / 2, [[0, 0], [54, 0]], stroke=TEAL, sw=4)
    fx += w + 64
# loop-back curved arrow under the flow
arrow(fx - 30, fy + 70, [[0, 0], [-(fx - ox - 90), 40], [-(fx - ox - 120), -20]],
      stroke=TEAL, sw=3, rough=1, dashed=True)
text(ox + 60, fy + 120, "roll back to any version - every one is kept", size=BODY, color=GREYD)
# version chips
vy = fy + 200
vx = ox + 60
for k, lab in enumerate(["v1", "v2", "v3"]):
    last = (k == 2)
    w, h = chip(vx, vy, lab, fill=(TEAL if last else WHITE),
                text_color=(WHITE if last else INK), border=TEAL, size=BODY)
    vx += w
    if not last:
        arrow(vx + 8, vy + h / 2, [[0, 0], [36, 0]], stroke=GREY, sw=3)
        vx += 52
demo_badge(ox + 60, vy + 110, "live demo:  a meeting-prep one-pager")

# ============================================================================
# BEAT 6 - BUILD ONCE, SHARE (hero)
# ============================================================================
ox = beat_head(6, "Build once. Share with everyone.")
# central: a build -> publish -> link
src_x, src_y = ox + 60, 380
claude_face(src_x + 60, src_y + 60, r=46, color=VIOLET)
text_centered(src_x + 60, src_y + 130, "you build it", size=SMALL, color=GREYD)
arrow(src_x + 130, src_y + 60, [[0, 0], [110, 0]], stroke=VIOLET, sw=4)
link_icon(src_x + 250, src_y + 44, color=VIOLET)
text_centered(src_x + 290, src_y + 130, "publish -> link", size=SMALL, color=VIOLET)
# fan out to three team cards
fan_x = src_x + 420
cards = [("Patient Care", "reply-template one-pager", GREEN, GREEN_BG),
         ("Anyone", "meeting-prep one-pager", BLUE, BLUE_BG),
         ("Ops", "reorder-date calculator", ORANGE, ORANGE_BG)]
for k, (who, what, acc, abg) in enumerate(cards):
    cy = src_y - 110 + k * 150
    arrow(src_x + 320, src_y + 60, [[0, 0], [fan_x - (src_x + 320) - 10, cy + 40 - (src_y + 60)]],
          stroke=GREY, sw=2, rough=1)
    sticky(fan_x, cy, 520, 116, abg, angle=jit(1.6))
    text(fan_x + 28, cy + 22, who, size=BODY, color=acc)
    text(fan_x + 28, cy + 60, what, size=SMALL, color=INK)
text(src_x, src_y + 300, "anyone with the link can use it - no Claude account needed to open it",
     size=BODY, color=GREYD)
demo_badge(src_x, src_y + 350, "live demo:  a supply calculator, then publish")

# ============================================================================
# BEAT 7 - SUPERPOWERS (new)
# ============================================================================
ox = beat_head(7, "The panel just got superpowers")
sparkles(ox + text_w("The panel just got superpowers", H1) + 150, HEAD_Y + 30, INDIGO)
feats = [("AI inside the Artifact", "it can think, not just sit there"),
         ("Live data", "refreshes when you reopen it"),
         ("Remembers between visits", "saves what you put in"),
         ("Connects to your tools", "calendar, email, chat and more")]
fx0, fy0 = ox + 60, 340
for k, (head, cap) in enumerate(feats):
    cx = fx0 + (k % 2) * 1040
    cy = fy0 + (k // 2) * 200
    sticky(cx, cy, 960, 150, INDIGO_BG, angle=jit(1.3))
    sparkle(cx + 36, cy + 40, 14, INDIGO)
    text(cx + 70, cy + 26, head, size=H3, color=INDIGO)
    text(cx + 70, cy + 80, cap, size=BODY, color=INK)

# ============================================================================
# BEAT 8 - ONE RULE, ONE REALITY CHECK
# ============================================================================
ox = beat_head(8, "One rule, one reality check")
cy0, cw, ch = 330, 860, 380
# the rule (red caution)
rect(ox + 40, cy0, cw, ch, stroke=RED, bg=RED_BG, sw=3, rough=1, rounded=True,
     fill="solid", opacity=35, angle=jit(-1.2))
text(ox + 80, cy0 + 30, "The rule", size=H3, color=RED)
diamond(ox + 80, cy0 - 56, 56, 56, stroke=RED, bg=RED_BG, sw=3)  # caution
text_centered(ox + 108, cy0 - 44, "!", size=H2, color=RED)
text(ox + 80, cy0 + 110,
     "Publishing or connecting an\nArtifact changes who can see it.\n\n"
     "Keep anything patient-identifiable,\nand any logins or keys, out of\n"
     "anything you share.", size=BODY, color=INK)
# when not to bother
rx = ox + 40 + cw + 120
sticky(rx, cy0, cw, ch, FAINT, angle=jit(1.2))
text(rx + 40, cy0 + 30, "When not to bother", size=H3, color=GREYD)
text(rx + 40, cy0 + 110,
     "A quick one-off answer\ndoesn't need an Artifact.\n\n"
     "Reach for one when you'll\nreuse it, edit it, or hand it on.", size=BODY, color=INK)

# ============================================================================
# BEAT 9 - PAUSE & TRY / CLOSE
# ============================================================================
ox = beat_head(9, "Pause here, and try it")
pause_icon(ox + 40, 320, 70, color=YELLOW)
highlighter(ox + 130, 318, 760, 80, YELLOW_BG, angle=0.0)
text(ox + 150, 330, "make a one-page Artifact for\nsomething you do every week", size=H3, color=INK)
ex_x = ox + 60
for lab in ["a status update", "a meeting-prep sheet", "a checklist"]:
    w, h = chip(ex_x, 470, lab, fill=WHITE, text_color=YELLOW, border=YELLOW, size=SMALL)
    ex_x += w + 36
text(ox + 60, 570, "see what it gives you - then change one thing", size=BODY, color=GREYD)
# close line - a clean sentence, then echo beat 1's "advisor -> maker" motif.
# Each piece is its own element with motif spacing, so kerning is font-native and
# the gaps read as intentional (no fragile mid-sentence width maths).
text(ox + 40, 666, "Artifacts turn Claude from...", size=H3, color=INK)
my2 = 726
text(ox + 40, my2, "advisor", size=H3, color=GREY)
arrow(ox + 40 + text_w("advisor", H3) + 20, my2 + 18, [[0, 0], [70, 0]], stroke=GREEN, sw=4)
text(ox + 40 + text_w("advisor", H3) + 110, my2, "maker", size=H3, color=GREEN)
sparkles(ox + 60, 808, YELLOW)
text(ox + 110, 798, "Docs: Anthropic - What are Artifacts and how do I use them",
     size=SMALL, color=VIOLET)
text(ox + 40, 858, "Phlo AI training  -  module 2.3", size=SMALL, color=GREY)

# ============================================================================
# CONNECTOR SPINE - the load-bearing through-line that makes it ONE picture
# ============================================================================
for i in range(1, 9):
    x0 = OX[i] + WID[i]
    x1 = OX[i + 1]
    acc = ACCENT[i + 1]
    midx = (x0 + x1) / 2
    # a gentle wavy hand-drawn arrow across the gap
    arrow(x0 + 20, MY, [[0, 0], [(x1 - x0) * 0.4, -36], [(x1 - x0) * 0.6, 30],
                        [x1 - x0 - 40, 0]], stroke=acc, sw=4, rough=1)

# faint dotted journey baseline under everything (drawn last, low opacity)
line(OX[1] + 40, MY + 320, [[0, 0], [TOTAL_W - 400, 0]], stroke=FAINT, sw=2,
     rough=1, dashed=True, opacity=60)

# ----------------------------------------------------------------------------
# WRITE + VALIDATE  (shared excalidraw_kit)
# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "2-3-artifacts.excalidraw")
MAXW = max(WID.values()) + 200
finish(out, MAXW, TOTAL_W)
