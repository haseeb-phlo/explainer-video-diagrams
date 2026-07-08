#!/usr/bin/env python3
"""Build claude-powerpoint.excalidraw - ONE flowing, illustrated explainer for the
"Claude + PowerPoint" training video (Phlo AI Ops Learn, module 2.7).

House Style B: a single hand-drawn journey that reads left-to-right - NO frames,
NO boxed slides, white canvas, everything in the hand font (fontFamily 1),
roughness 1, a lively colour-coded Excalidraw palette, colour blocking, scribbled
annotations and charming primitive illustrations. The LOOK lives in the shared
excalidraw_kit; this file holds only the composition (scene + beat scaffold) and
the few one-off illustrations this video needs (a slide + a slide deck).

Content is two real, current capabilities, kept distinct from the Artifacts video
(2.3, which only name-checks "Word / PPT / Excel / PDF" as one output): (1) "Create
and edit files with Claude" - natural language to a genuine downloadable .pptx, on
all plans, web / desktop / mobile; and (2) "Claude for PowerPoint" - the Microsoft
365 add-in that puts Claude in a sidebar INSIDE PowerPoint. The angle for this
file-type video is decks: structure, templates/branding, and turning bullets into
native charts and diagrams (Excel = formulas/data, Word = long-form - kept separate
so the three don't read as copy-paste).

Run:  python3 videos/claude/7-claude-powerpoint/build_powerpoint.py
      python3 preview.py videos/claude/7-claude-powerpoint/claude-powerpoint.excalidraw out.png
"""
import os
import sys

_d = os.path.dirname(os.path.abspath(__file__))
while _d != os.path.dirname(_d) and not os.path.exists(os.path.join(_d, "excalidraw_kit.py")):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)

import random
from excalidraw_kit import *

random.seed(70710)  # deterministic - re-runs produce identical files

# ----------------------------------------------------------------------------
# BEAT SCAFFOLD  (9 beats, wide gaps so one frames cleanly on a 14" laptop)
# ----------------------------------------------------------------------------
# Every beat uses the SAME slot (~1120 wide x ~980 tall content, ~1.15 : 1) so
# framing is identical and fits a 14" MacBook screen. Wide gaps so a single beat
# frames cleanly with no neighbours peeking in - the whitespace IS the camera.
N = 9
GAP = 800
WID = dict.fromkeys(range(1, N + 1), 1200)
ACCENT = {1: ORANGE, 2: VIOLET, 3: BLUE, 4: GREEN, 5: TEAL,
          6: INDIGO, 7: ORANGE, 8: GREEN, 9: ORANGE}
OX = {}
_c = 0
for _i in range(1, N + 1):
    OX[_i] = _c
    _c += WID[_i] + GAP
TOTAL_W = _c

HEAD_Y = 60


def beat_head(i, title, sub=None):
    # QUIET heading: plain hand title in the beat's accent colour, lively underline,
    # no step circle, no highlighter sweep - the unpolished natural-flow look.
    ox = OX[i]
    heading(ox, HEAD_Y, title, color=ACCENT[i], sub=sub)
    return ox


# ----------------------------------------------------------------------------
# LOCAL ONE-OFF ILLUSTRATIONS  (bespoke to this video, kept out of the kit)
# ----------------------------------------------------------------------------
def slide(x, y, w, h, accent=ORANGE, abg=ORANGE_BG, bullets=3, chart=True):
    """A single PowerPoint slide: title bar, a few bullet lines, a tiny bar chart."""
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="slide")
    rect(x + 0.10 * w, y + 0.12 * h, 0.45 * w, 0.10 * h, stroke="transparent",
         bg=accent, sw=1, rough=1, rounded=True, prefix="sttl")
    for k in range(bullets):
        ly = y + 0.34 * h + k * 0.14 * h
        ellipse(x + 0.10 * w, ly + 2, 7, 7, stroke=accent, bg=accent, sw=1)
        line(x + 0.10 * w + 18, ly + 5, [[0, 0], [0.34 * w, 0]], stroke=GREY, sw=2)
    if chart:
        base = y + h - 0.16 * h
        for k, hh in enumerate([0.22, 0.40, 0.30, 0.5]):
            bh = hh * h
            rect(x + 0.62 * w + k * 0.085 * w, base - bh, 0.05 * w, bh,
                 stroke=INK, bg=abg, sw=1, rough=1, rounded=False, prefix="sbar")


def slide_deck(x, y, accent=ORANGE, abg=ORANGE_BG):
    """A stack of slides - two offset behind, one crisp slide in front."""
    for k in range(2):
        off = (2 - k) * 18
        rect(x + off, y + off, 232, 150, stroke=INK, bg=abg, sw=2, rough=1,
             rounded=True, prefix="deck")
    slide(x + 36, y + 36, 232, 150, accent=accent, abg=abg, bullets=3, chart=True)


def tiny_slide(x, y):
    slide(x, y, 170, 116, accent=ORANGE, abg=ORANGE_BG, bullets=3, chart=True)


def src_card(x, y, label, accent, abg):
    """A small labelled source the deck is built from."""
    w, h = 250, 96
    sticky(x, y, w, h, abg, angle=jit(1.6))
    rect(x + 18, y + 22, 40, 52, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True)
    for k in range(3):
        line(x + 26, y + 34 + k * 12, [[0, 0], [24, 0]], stroke=GREY, sw=2)
    text(x + 78, y + 36, label, size=SMALL, color=accent, width=w - 96)
    return w, h


# ============================================================================
# BOARD TITLE
# ============================================================================
text(OX[1], -300, "Claude + PowerPoint", size=HERO, color=INK)
text(OX[1] + 6, -300 + HERO * LINE_H + 4,
     "from a pile of notes to a finished deck", size=H2, color=ORANGE)

# ============================================================================
# BEAT 1 - HOOK
# ============================================================================
ox = beat_head(1, "Ask for a deck, get a real one",
               "not an outline of a deck - an actual PowerPoint file")
by = 360
bw, bh = 520, 130
sticky(ox + 40, by, bw, bh, GREY, angle=jit(1.5))
text(ox + 72, by + 30, "turn these notes into a\n10-slide deck", size=BODY, color=WHITE)
line(ox + 90, by + bh, [[0, 0], [-18, 30], [22, -2]], stroke=GREY, sw=3)  # tail
arrow(ox + 40 + bw + 30, by + bh / 2, [[0, 0], [150, 0]], stroke=ORANGE, sw=5, rough=1)
deck_x = ox + 40 + bw + 230
ellipse(deck_x - 40, by - 30, 260, 240, stroke=ORANGE, bg=ORANGE_BG, sw=2, rough=1,
        fill="solid", opacity=50)
slide_deck(deck_x, by)
arrow(deck_x + 130, by + 210, [[0, 0], [0, 44]], stroke=ORANGE, sw=3, rough=1)
text(deck_x + 12, by + 262, "a real .pptx you can\nopen and present", size=SMALL, color=ORANGE)

# ============================================================================
# BEAT 2 - WHAT IT IS
# ============================================================================
ox = beat_head(2, "A real file, not a picture of one",
               "Claude writes the file by running code, then hands\nit to you - to download or save straight to Drive.")
cw_x, cw_y, cw_w, cw_h = ox + 40, 330, 1080, 560
claude_window(cw_x, cw_y, cw_w, cw_h, tiny=tiny_slide)
text(cw_x, cw_y + cw_h + 24, "you ask in the chat, like always", size=SMALL, color=GREY)
arrow(cw_x + cw_w * 0.74, cw_y + cw_h + 56, [[0, 0], [70, -60]], stroke=VIOLET, sw=3, rough=1)
text(cw_x + cw_w * 0.55, cw_y + cw_h + 60,
     "downloads as .pptx - opens in PowerPoint,\nGoogle Slides or Keynote", size=SMALL, color=VIOLET)
# reassurance chips: who/where
chx = cw_x
for lab in ["every plan", "web, desktop & mobile", "up to 30MB a file"]:
    w, _ = chip(chx, cw_y + cw_h + 110, lab, fill=WHITE, text_color=VIOLET, border=VIOLET, size=SMALL)
    chx += w + 30

# ============================================================================
# BEAT 3 - START FROM WHAT YOU HAVE
# ============================================================================
ox = beat_head(3, "Start from what you already have",
               "Point Claude at your raw material and it does\nthe shaping. You rarely start from a blank slide.")
# sources on the left fan into Claude -> a deck on the right
sx, sy = ox + 40, 340
srcs = [("rough notes", BLUE, BLUE_BG), ("a Word report", INDIGO, INDIGO_BG),
        ("a sheet of numbers", GREEN, GREEN_BG), ("a meeting summary", ORANGE, ORANGE_BG)]
for k, (lab, acc, abg) in enumerate(srcs):
    src_card(sx, sy + k * 120, lab, acc, abg)
face_x, face_y = sx + 360, sy + 220
claude_face(face_x, face_y, r=46, color=BLUE)
text_centered(face_x, face_y + 86, "Claude", size=SMALL, color=GREYD)
for k in range(4):
    arrow(sx + 256, sy + 48 + k * 120, [[0, 0], [face_x - 46 - (sx + 256), face_y - (sy + 48 + k * 120)]],
          stroke=GREY, sw=2, rough=1)
arrow(face_x + 56, face_y, [[0, 0], [120, 0]], stroke=BLUE, sw=4)
slide_deck(face_x + 190, face_y - 90, accent=BLUE, abg=BLUE_BG)

# ============================================================================
# BEAT 4 - TELL IT THE SHAPE
# ============================================================================
ox = beat_head(4, "Tell it the shape you want",
               "The more you say up front, the less you fix later.")
note_y, note_w, note_h = 320, 1040, 290
sticky(ox + 40, note_y, note_w, note_h, GREEN_BG, angle=jit(1.4))
text(ox + 80, note_y + 26, "Worth saying", size=H3, color=GREEN)
for k, item in enumerate(["how many slides, and who it's for",
                          "the tone - board-level, or a team catch-up",
                          "a summary slide and speaker notes",
                          "charts built from your numbers"]):
    text(ox + 96, note_y + 92 + k * 46, "- " + item, size=BODY, color=INK)
ny2 = note_y + note_h + 40
chip(ox + 56, ny2, "build a 10-slide deck for the leadership review", fill=WHITE,
     text_color=GREEN, border=GREEN, size=SMALL)
chip(ox + 56, ny2 + 84, "make it match our template, and add speaker notes", fill=WHITE,
     text_color=GREEN, border=GREEN, size=SMALL)
demo_badge(ox + 56, ny2 + 168, "show in Claude desktop:  notes -> a 10-slide deck")

# ============================================================================
# BEAT 5 - TWO PLACES IT LIVES
# ============================================================================
ox = beat_head(5, "Build from chat, or edit in PowerPoint",
               "Make the whole deck in the chat - or open the\nClaude sidebar on a deck you already have.")
half = 510
# left: in the chat
lx, ly = ox + 40, 340
sticky(lx, ly, half, 470, TEAL_BG, angle=jit(-1.0))
text(lx + 36, ly + 28, "In the Claude chat", size=H3, color=TEAL)
text(lx + 36, ly + 86, "Describe it, Claude builds the\nwhole .pptx from scratch.", size=BODY, color=INK)
slide_deck(lx + 120, ly + 200, accent=TEAL, abg=TEAL_BG)
# right: the add-in inside PowerPoint
rx = ox + 40 + half + 60
sticky(rx, ly, half, 470, INDIGO_BG, angle=jit(1.0))
text(rx + 36, ly + 28, "Inside PowerPoint", size=H3, color=INDIGO)
text(rx + 36, ly + 86, "The Claude sidebar (a Microsoft\n365 add-in) edits your open deck.", size=BODY, color=INK)
# a deck with a sidebar
rect(rx + 36, ly + 200, 300, 200, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True)
slide(rx + 52, ly + 220, 190, 130, accent=INDIGO, abg=INDIGO_BG)
rect(rx + 256, ly + 210, 70, 180, stroke=INDIGO, bg=INDIGO_BG, sw=2, rough=1,
     rounded=True, fill="solid", opacity=55)
text(rx + 262, ly + 220, "Claude", size=SMALL, color=INDIGO)
text(rx + 36, ly + 416, "Pro plan and up", size=SMALL, color=GREYD)

# ============================================================================
# BEAT 6 - EDIT BY TALKING
# ============================================================================
ox = beat_head(6, "It's a draft you steer",
               "First pass is rarely the last. You change it by asking -\n"
               "Claude keeps your template and branding.")
flow = ["first draft", "ask for a change", "new version"]
fx, fy = ox + 50, 350
for k, lab in enumerate(flow):
    w, h = chip(fx, fy, lab, fill=INDIGO_BG, text_color=INK, border=INDIGO, size=BODY)
    if k < len(flow) - 1:
        arrow(fx + w + 8, fy + h / 2, [[0, 0], [40, 0]], stroke=INDIGO, sw=4)
    fx += w + 52
# loop-back
arrow(fx - 40, fy + 70, [[0, 0], [-(fx - ox - 110), 44], [-(fx - ox - 150), -18]],
      stroke=INDIGO, sw=3, rough=1, dashed=True)
asks = ["simplify the text on slide 3",
        "add a market-sizing section",
        "turn these bullets into a process diagram",
        "combine slides 5 and 6"]
for k, a in enumerate(asks):
    chip(ox + 60, fy + 150 + k * 84, a, fill=WHITE, text_color=INDIGO, border=INDIGO, size=SMALL)
demo_badge(ox + 60, fy + 150 + len(asks) * 84 + 6,
           "show in PowerPoint:  the Claude sidebar editing one slide")

# ============================================================================
# BEAT 7 - WHERE IT SHINES  (a filmstrip of four decks)
# ============================================================================
ox = beat_head(7, "Decks worth handing over")
jobs = [("A report -> slides", "paste the doc, get a deck", ORANGE, ORANGE_BG),
        ("A team update", "on a recurring template", BLUE, BLUE_BG),
        ("A training deck", "a process, step by step", GREEN, GREEN_BG),
        ("A first draft", "faster to fix than to start", VIOLET, VIOLET_BG)]
fx0, fy0, step = ox + 50, 360, 285
for k, (head, cap, acc, abg) in enumerate(jobs):
    bx = fx0 + k * step
    slide_deck(bx, fy0, accent=acc, abg=abg)
    text(bx, fy0 + 216, head, size=BODY, color=acc, width=250)
    text(bx, fy0 + 256, cap, size=SMALL, color=GREYD, width=250)

# ============================================================================
# BEAT 8 - SAFETY  (a pre-flight checklist, not a caution box)
# ============================================================================
ox = beat_head(8, "Before the deck leaves your hands")
cardx, cardy, cardw = ox + 60, 330, 980
rect(cardx, cardy, cardw, 300, stroke=GREEN, bg=GREEN_T, sw=2, rough=1, rounded=True)
text(cardx + 40, cardy + 26, "Quick check before you share", size=H3, color=GREEN)
for k, it in enumerate(["the facts and numbers are right",
                        "nothing confidential is in a deck you'll send",
                        "you've read it - you own the final"]):
    yy = cardy + 96 + k * 64
    tick(cardx + 48, yy, color=GREEN, s=28, sw=5)
    text(cardx + 96, yy - 4, it, size=BODY, color=INK)
warny = cardy + 340
rect(cardx, warny, cardw, 120, stroke=ORANGE, bg=ORANGE_T, sw=2, rough=1, rounded=True)
text(cardx + 40, warny + 22, "One thing to avoid", size=SMALL, color=ORANGE)
text(cardx + 40, warny + 56,
     "don't open templates or decks you don't trust - a booby-trapped\nfile can quietly hijack the request.",
     size=BODY, color=INK)

# ============================================================================
# BEAT 9 - TRY / CLOSE  (a 'your turn' homework note, no pause band)
# ============================================================================
ox = beat_head(9, "Your turn - notes into a deck")
sticky(ox + 60, 330, 620, 250, ORANGE_BG, angle=jit(1.3))
text(ox + 96, 356, "Try this week", size=H3, color=ORANGE)
text(ox + 96, 422, "take something you already wrote\nand ask Claude for a 5-slide version", size=BODY, color=INK)
slide_deck(ox + 770, 356, accent=ORANGE, abg=ORANGE_BG)
ex_x = ox + 60
for lab in ["a project update", "a process you explain", "last month's numbers"]:
    w, _ = chip(ex_x, 624, lab, fill=WHITE, text_color=ORANGE, border=ORANGE, size=SMALL)
    ex_x += w + 30
text(ox + 60, 716, "open it in PowerPoint and change one thing - it's yours now", size=BODY, color=GREYD)
text(ox + 40, 776, "Claude turns raw material into a finished deck - you still hold the pen.",
     size=H3, color=INK)
text(ox + 60, 868, "Docs: Claude - Create and edit files, and Use Claude for PowerPoint",
     size=SMALL, color=VIOLET)

# ----------------------------------------------------------------------------
# WRITE + VALIDATE  (shared excalidraw_kit)
# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "claude-powerpoint.excalidraw")
MAXW = max(WID.values()) + 200
finish(out, MAXW, TOTAL_W)
