#!/usr/bin/env python3
"""Build 3-artifacts.excalidraw - ONE flowing, illustrated explainer for the
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
GAP = 800
# every beat uses the SAME slot, shaped like the "Words left, a thing right" beat
# (~1120 wide x ~980 tall content, ~1.15 : 1) so framing is identical and it fits
# a 14" MacBook screen. Content fills the slot; it never spreads wider or taller.
WID = {i: 1200 for i in range(1, 10)}
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
    # QUIET heading: plain hand title in the beat's accent colour, no step circle,
    # no highlighter sweep, no scribble underline - the unpolished natural-flow look.
    ox = OX[i]
    heading(ox, HEAD_Y, title, color=ACCENT[i], sub=sub)
    return ox

# ----------------------------------------------------------------------------
# BOARD TITLE
# ----------------------------------------------------------------------------
text(OX[1], -300, "Artifacts", size=HERO, color=INK)
text(OX[1] + 6, -300 + HERO * LINE_H + 4, "when Claude makes things, not just text",
     size=H2, color=VIOLET)

# ============================================================================
# BEAT 1 - HOOK + CORE IDEA
# ============================================================================
ox = beat_head(1, "Ask, and Claude builds it",
               "the feature that turns Claude from advisor into maker")
# the hook: chat bubble -> arrow -> a real calculator with a burst
by = 360
bw, bh = 520, 130
sticky(ox + 40, by, bw, bh, GREY, angle=jit(1.5))
text(ox + 72, by + 30, "build me a tool to work\nout unit costs", size=BODY, color=WHITE)
line(ox + 90, by + bh, [[0, 0], [-18, 30], [22, -2]], stroke=GREY, sw=3)  # tail
arrow(ox + 40 + bw + 30, by + bh / 2, [[0, 0], [150, 0]], stroke=ORANGE, sw=5, rough=1)
# burst behind calc
calc_x = ox + 40 + bw + 240
ellipse(calc_x - 30, by - 20, 200, 200, stroke=ORANGE, bg=ORANGE_BG, sw=2, rough=1,
        fill="solid", opacity=55)
obj_calc(calc_x, by + 4)
text(calc_x - 10, by + 168, "the actual thing - not a\ndescription of it", size=SMALL, color=ORANGE)
# advisor -> maker motif
amy = 620
text(ox + 40, amy, "advisor", size=H3, color=GREY)
line(ox + 40, amy + 22, [[0, 0], [text_w('advisor', H3) + 6, 4]], stroke=RED, sw=3)  # strike
arrow(ox + 40 + text_w("advisor", H3) + 24, amy + 18, [[0, 0], [70, 0]], stroke=GREEN, sw=4)
text(ox + 40 + text_w("advisor", H3) + 110, amy, "maker", size=H3, color=GREEN)

# ============================================================================
# BEAT 2 - WORDS LEFT, THING RIGHT
# ============================================================================
ox = beat_head(2, "Words left, a thing right",
               "Normally Claude talks in the chat. An Artifact\nis a separate panel holding an actual thing.")
cw_x, cw_y, cw_w, cw_h = ox + 40, 330, 1080, 600
claude_window(cw_x, cw_y, cw_w, cw_h, tiny=obj_doc)
# annotation
text(cw_x, cw_y + cw_h + 24, "the chat, like always", size=SMALL, color=GREY)
arrow(cw_x + cw_w * 0.74, cw_y + cw_h + 56, [[0, 0], [70, -60]], stroke=VIOLET, sw=3, rough=1)
text(cw_x + cw_w * 0.56, cw_y + cw_h + 60,
     "a panel holding something\nyou can edit, run and reuse", size=SMALL, color=VIOLET)

# ============================================================================
# BEAT 3 - IT CAN BE ALMOST ANYTHING
# ============================================================================
ox = beat_head(3, "It can be almost anything",
               "Same feature, very different outputs.\nThe skill is knowing it's there and asking for it.")
# playful cluster - 2 columns x 3 rows (portrait, fits the screen), jittered
positions = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1)]
cellw, cellh = 360, 350
gx, gy = ox + 60, 330
for (fn, cap, acc, abg), (cxi, cyi) in zip(OBJS, positions):
    bx = gx + cxi * cellw + random.uniform(-20, 20)
    byy = gy + cyi * cellh + random.uniform(-14, 14)
    sticky(bx - 20, byy - 24, 210, 234, abg, angle=jit(2.2))
    fn(bx, byy)
    text_centered(bx + 65, byy + 168, cap, size=SMALL, color=acc, angle=jit(2.0))

# ============================================================================
# BEAT 4 - TWO WAYS YOU GET ONE
# ============================================================================
ox = beat_head(4, "Two ways you get one",
               "Claude makes one on its own - or you ask, on purpose.\nTwo phrasings do most of the work.")
note_y, note_w, note_h = 300, 1040, 320
# top: appears on its own
sticky(ox + 40, note_y, note_w, note_h, GREEN_BG, angle=jit(1.6))
text(ox + 80, note_y + 28, "Appears on its own", size=H3, color=GREEN)
for k, item in enumerate(["long documents", "code", "tables and structured output",
                          "anything you'll clearly reuse"]):
    text(ox + 96, note_y + 96 + k * 52, "- " + item, size=BODY, color=INK)
# bottom: ask on purpose
ny2 = note_y + note_h + 44
sticky(ox + 40, ny2, note_w, note_h, BLUE_BG, angle=jit(-1.4))
text(ox + 80, ny2 + 28, "Ask for one on purpose", size=H3, color=BLUE)
chip(ox + 56, ny2 + 108, "make me a one-page Artifact summarising X",
     fill=WHITE, text_color=BLUE, border=BLUE, size=SMALL)
chip(ox + 56, ny2 + 200, "build me a tool to calculate Y",
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
        arrow(fx + w + 8, fy + h / 2, [[0, 0], [40, 0]], stroke=TEAL, sw=4)
    fx += w + 44
# loop-back curved arrow under the flow
arrow(fx - 30, fy + 70, [[0, 0], [-(fx - ox - 90), 40], [-(fx - ox - 120), -20]],
      stroke=TEAL, sw=3, rough=1, dashed=True)
text(ox + 60, fy + 132, "roll back to any version - every one is kept", size=BODY, color=GREYD)
text(ox + 60, fy + 178, "edit on the canvas yourself, or just tell Claude in plain English", size=SMALL, color=GREYD)
# version chips
vy = fy + 248
vx = ox + 60
for k, lab in enumerate(["v1", "v2", "v3"]):
    last = (k == 2)
    w, h = chip(vx, vy, lab, fill=(TEAL if last else WHITE),
                text_color=(WHITE if last else INK), border=TEAL, size=BODY)
    vx += w
    if not last:
        arrow(vx + 8, vy + h / 2, [[0, 0], [36, 0]], stroke=GREY, sw=3)
        vx += 52
demo_badge(ox + 60, vy + 110, "show in Claude desktop app:  a meeting-prep one-pager")

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
cards = [("Support", "reply-template one-pager", GREEN, GREEN_BG),
         ("Anyone", "meeting-prep one-pager", BLUE, BLUE_BG),
         ("Ops", "a budget calculator", ORANGE, ORANGE_BG)]
for k, (who, what, acc, abg) in enumerate(cards):
    cy = src_y - 110 + k * 150
    arrow(src_x + 320, src_y + 60, [[0, 0], [fan_x - (src_x + 320) - 10, cy + 40 - (src_y + 60)]],
          stroke=GREY, sw=2, rough=1)
    sticky(fan_x, cy, 520, 116, abg, angle=jit(1.6))
    text(fan_x + 28, cy + 22, who, size=BODY, color=acc)
    text(fan_x + 28, cy + 60, what, size=SMALL, color=INK)
text(src_x, src_y + 300, "anyone with the link can use it - no Claude account needed to open it",
     size=BODY, color=GREYD)
demo_badge(src_x, src_y + 350, "show in Claude desktop app:  a budget calculator, then publish")

# ============================================================================
# BEAT 7 - SUPERPOWERS (new)
# ============================================================================
ox = beat_head(7, "The panel just got superpowers")
feats = [("AI inside the Artifact", "it can think, not just sit there"),
         ("Live data", "refreshes when you reopen it"),
         ("Remembers between visits", "saves what you put in"),
         ("Connects to your tools", "calendar, email, chat and more")]
fy0 = 310
for k, (head, cap) in enumerate(feats):
    cy = fy0 + k * 174
    sticky(ox + 40, cy, 1040, 150, INDIGO_BG, angle=jit(1.3))
    text(ox + 120, cy + 26, head, size=H3, color=INDIGO)
    text(ox + 120, cy + 82, cap, size=BODY, color=INK)

# ============================================================================
# BEAT 8 - ONE RULE, ONE REALITY CHECK
# ============================================================================
ox = beat_head(8, "One rule, one reality check")
cy0, cw, ch = 300, 1040, 300
# the rule (red caution) - top
rect(ox + 40, cy0, cw, ch, stroke=RED, bg=RED_BG, sw=3, rough=1, rounded=True,
     fill="solid", opacity=35, angle=jit(-1.2))
diamond(ox + 80, cy0 - 56, 56, 56, stroke=RED, bg=RED_BG, sw=3)  # caution
text_centered(ox + 108, cy0 - 44, "!", size=H2, color=RED)
text(ox + 80, cy0 + 24, "The rule", size=H3, color=RED)
text(ox + 80, cy0 + 90,
     "Publishing or connecting an Artifact\nchanges who can see it. Keep anything\n"
     "confidential, and any logins or keys,\nout of anything you share.", size=BODY, color=INK)
# when not to bother - below
ny2 = cy0 + ch + 44
sticky(ox + 40, ny2, cw, ch, FAINT, angle=jit(1.2))
text(ox + 80, ny2 + 24, "When not to bother", size=H3, color=GREYD)
text(ox + 80, ny2 + 90,
     "A quick one-off answer doesn't need an\nArtifact. Reach for one when you'll\n"
     "reuse it, edit it, or hand it on.", size=BODY, color=INK)

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
text(ox + 110, 798, "Docs: Anthropic - What are Artifacts and how do I use them",
     size=SMALL, color=VIOLET)

# No connector spine and no branding footer: beats read as one picture through
# layout + consistent rhythm (the ai-foundations natural-flow look), not arrows.

# ----------------------------------------------------------------------------
# WRITE + VALIDATE  (shared excalidraw_kit)
# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "3-artifacts.excalidraw")
MAXW = max(WID.values()) + 200
finish(out, MAXW, TOTAL_W)
