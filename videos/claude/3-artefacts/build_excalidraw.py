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
import json
import math
import os
import random

random.seed(20230)  # deterministic - re-runs produce identical files

# ----------------------------------------------------------------------------
# DESIGN SYSTEM - lively Excalidraw palette (matches llm_explainer.excalidraw)
# ----------------------------------------------------------------------------
WHITE = "#ffffff"
INK   = "#1e1e1e"   # primary text / strokes
GREYD = "#495057"   # secondary text
GREY  = "#868e96"   # captions, faint lines
FAINT = "#dee2e6"   # very light guide lines

# accent stroke + matching pastel fill, one pair per "colour"
VIOLET, VIOLET_BG = "#7048e8", "#d0bfff"
ORANGE, ORANGE_BG = "#e8590c", "#ffd8a8"
GREEN,  GREEN_BG  = "#2f9e44", "#b2f2bb"
BLUE,   BLUE_BG   = "#1971c2", "#a5d8ff"
RED,    RED_BG    = "#c92a2a", "#ffc9c9"
TEAL,   TEAL_BG   = "#0c8599", "#99e9f2"
YELLOW, YELLOW_BG = "#f08c00", "#ffec99"
INDIGO, INDIGO_BG = "#364fc7", "#bac8ff"

PALETTE = {WHITE, INK, GREYD, GREY, FAINT, "transparent",
           VIOLET, VIOLET_BG, ORANGE, ORANGE_BG, GREEN, GREEN_BG,
           BLUE, BLUE_BG, RED, RED_BG, TEAL, TEAL_BG, YELLOW, YELLOW_BG,
           INDIGO, INDIGO_BG}

# Type scale
HERO, H1, H2, H3, BODY, LABEL, SMALL = 96, 48, 34, 28, 22, 20, 17
HAND = 5  # Excalifont everywhere - the whole point is "not typed text"
LINE_H = 1.25
WFAC = 0.56  # generous glyph-width factor for Excalifont (over-estimate is safe)

# ----------------------------------------------------------------------------
# ELEMENT FACTORY
# ----------------------------------------------------------------------------
E = []
_seq = 0
def _uid(p):
    global _seq
    _seq += 1
    return f"{p}-{_seq:03d}"

def jit(maxdeg=2.5):
    """A small random rotation in radians - the hand-arranged wobble."""
    return random.uniform(-maxdeg, maxdeg) * math.pi / 180.0

def _base(eid, etype, x, y, w, h, angle=0.0, opacity=100):
    return {
        "id": eid, "type": etype,
        "x": float(x), "y": float(y), "width": float(w), "height": float(h),
        "angle": float(angle),
        "strokeColor": INK, "backgroundColor": "transparent",
        "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
        "roughness": 1, "opacity": opacity, "groupIds": [],
        "frameId": None, "roundness": None,
        "seed": random.randint(1, 2**31), "version": 1,
        "versionNonce": random.randint(1, 2**31), "isDeleted": False,
        "boundElements": None, "updated": 1717200000000,
        "link": None, "locked": False,
    }

def rect(x, y, w, h, stroke=INK, bg="transparent", sw=2, rough=1, rounded=True,
         fill="solid", angle=0.0, opacity=100, prefix="rect"):
    e = _base(_uid(prefix), "rectangle", x, y, w, h, angle, opacity)
    e.update(strokeColor=stroke, backgroundColor=bg, strokeWidth=sw, roughness=rough,
             fillStyle=fill, roundness=({"type": 3} if rounded else None))
    E.append(e); return e

def ellipse(x, y, w, h, stroke=INK, bg="transparent", sw=2, rough=1, fill="solid",
            angle=0.0, opacity=100, prefix="ell"):
    e = _base(_uid(prefix), "ellipse", x, y, w, h, angle, opacity)
    e.update(strokeColor=stroke, backgroundColor=bg, strokeWidth=sw, roughness=rough,
             fillStyle=fill, roundness=None)
    E.append(e); return e

def diamond(x, y, w, h, stroke=INK, bg="transparent", sw=2, rough=1, fill="solid", prefix="dia"):
    e = _base(_uid(prefix), "diamond", x, y, w, h)
    e.update(strokeColor=stroke, backgroundColor=bg, strokeWidth=sw, roughness=rough,
             fillStyle=fill, roundness=None)
    E.append(e); return e

def _bbox(pts):
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    return min(xs), min(ys), max(xs), max(ys)

def line(x, y, points, stroke=INK, sw=2, rough=1, bg="transparent", fill="solid",
         opacity=100, prefix="line", dashed=False):
    minx, miny, maxx, maxy = _bbox(points)
    e = _base(_uid(prefix), "line", x, y, maxx - minx, maxy - miny, 0.0, opacity)
    e.update(strokeColor=stroke, backgroundColor=bg, strokeWidth=sw, roughness=rough,
             fillStyle=fill, strokeStyle=("dashed" if dashed else "solid"),
             points=[[float(px), float(py)] for px, py in points],
             startArrowhead=None, endArrowhead=None, lastCommittedPoint=None, roundness=None)
    E.append(e); return e

def arrow(x, y, points, stroke=INK, sw=2, rough=1, prefix="arr", dashed=False, head="arrow"):
    minx, miny, maxx, maxy = _bbox(points)
    e = _base(_uid(prefix), "arrow", x, y, maxx - minx, maxy - miny)
    e.update(strokeColor=stroke, backgroundColor="transparent", strokeWidth=sw, roughness=rough,
             strokeStyle=("dashed" if dashed else "solid"),
             points=[[float(px), float(py)] for px, py in points],
             startArrowhead=None, endArrowhead=head, lastCommittedPoint=None, roundness=None)
    E.append(e); return e

def text_w(s, size, font=HAND):
    longest = max((len(ln) for ln in s.split("\n")), default=0)
    return longest * size * WFAC

def text_h(s, size):
    return len(s.split("\n")) * size * LINE_H

def text(x, y, s, size=BODY, font=HAND, color=INK, align="left", width=None,
         angle=0.0, opacity=100):
    w = width if width is not None else text_w(s, size, font)
    h = text_h(s, size)
    e = _base(_uid("txt"), "text", x, y, w, h, angle, opacity)
    e.update(strokeColor=color, backgroundColor="transparent", roughness=1,
             text=s, fontSize=size, fontFamily=font, textAlign=align,
             verticalAlign="top", containerId=None, originalText=s,
             lineHeight=LINE_H, roundness=None)
    E.append(e)
    e["_mw"] = text_w(s, size, font)
    return e

def text_centered(cx, y, s, size=BODY, font=HAND, color=INK, angle=0.0):
    w = text_w(s, size, font)
    return text(cx - w / 2, y, s, size=size, font=font, color=color, align="center",
                width=w, angle=angle)

# ----------------------------------------------------------------------------
# FUN PRIMITIVES - colour blocking, annotations, sketches
# ----------------------------------------------------------------------------
def highlighter(x, y, w, h, color, angle=None):
    """A marker sweep: saturated colour at low opacity, slight wobble."""
    rect(x, y, w, h, stroke="transparent", bg=color, sw=1, rough=1, rounded=True,
         fill="solid", opacity=26, angle=(jit(2.0) if angle is None else angle),
         prefix="hl")

def sticky(x, y, w, h, fill, angle=None, prefix="sticky"):
    """A filled note - no border, gentle rotation."""
    return rect(x, y, w, h, stroke="transparent", bg=fill, sw=1, rough=1,
                rounded=True, fill="solid",
                angle=(jit(2.2) if angle is None else angle), prefix=prefix)

def chip(x, y, label, fill=WHITE, text_color=INK, border=GREYD, size=LABEL,
         angle=None, sw=2):
    tw = text_w(label, size, HAND)
    px, py = 22, 12
    w, h = tw + 2 * px, size * LINE_H + 2 * py
    a = jit(1.8) if angle is None else angle
    rect(x, y, w, h, stroke=border, bg=fill, sw=sw, rough=1, rounded=True,
         fill="solid", angle=a, prefix="chip")
    text(x + px, y + py, label, size=size, color=text_color, angle=a, width=tw)
    return w, h

def scribble_underline(x, y, w, color, sw=3):
    """A wobbly hand underline."""
    n = max(3, int(w / 80))
    pts = [[i * w / n, math.sin(i) * 4 + (0 if i not in (0, n) else 0)] for i in range(n + 1)]
    line(x, y, pts, stroke=color, sw=sw, rough=1, prefix="ul")

def circle_around(x, y, w, h, color, sw=3):
    ellipse(x, y, w, h, stroke=color, bg="transparent", sw=sw, rough=2, prefix="circ")

def sparkle(cx, cy, s, color, sw=2):
    p = [[0, -s], [0.28 * s, -0.28 * s], [s, 0], [0.28 * s, 0.28 * s],
         [0, s], [-0.28 * s, 0.28 * s], [-s, 0], [-0.28 * s, -0.28 * s], [0, -s]]
    line(cx, cy, p, stroke=color, sw=sw, rough=1, bg=color, fill="solid", prefix="spk")

def sparkles(cx, cy, color):
    sparkle(cx, cy, 22, color, sw=2)
    sparkle(cx + 38, cy - 30, 12, color, sw=2)
    sparkle(cx - 30, cy - 22, 9, color, sw=2)

def play_icon(x, y, size, color=ORANGE):
    line(x, y, [[0, 0], [size, size / 2], [0, size], [0, 0]], stroke=color, sw=2,
         rough=1, bg=color, fill="solid", prefix="play")

def pause_icon(x, y, size, color=ORANGE):
    bw = size * 0.32
    rect(x, y, bw, size, stroke=color, bg=color, sw=2, rough=1, rounded=False, prefix="pause")
    rect(x + bw + size * 0.3, y, bw, size, stroke=color, bg=color, sw=2, rough=1,
         rounded=False, prefix="pause")

def demo_badge(x, y, label):
    """A dashed 'live demo' pill with a play glyph - the [TO CLAUDE] cut-aways."""
    tw = text_w(label, SMALL, HAND)
    w, h = tw + 96, 56
    a = jit(1.5)
    rect(x, y, w, h, stroke=ORANGE, bg=ORANGE_BG, sw=2, rough=1, rounded=True,
         fill="solid", angle=a, opacity=70, prefix="demo")
    play_icon(x + 24, y + 16, 22, color=ORANGE)
    text(x + 60, y + 16, label, size=SMALL, color=ORANGE, angle=a, width=tw)
    return w, h

# ----------------------------------------------------------------------------
# ILLUSTRATIONS (~140-180px) - charming, from primitives, colour-coded
# ----------------------------------------------------------------------------
def obj_doc(x, y, accent=BLUE, abg=BLUE_BG):           # one-pager
    rect(x + 18, y, 104, 150, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True)
    rect(x + 18, y, 104, 26, stroke="transparent", bg=abg, sw=1, rough=1, rounded=True)
    for k in range(4):
        line(x + 34, y + 50 + k * 24, [[0, 0], [72, 0]], stroke=GREY, sw=2)

def obj_calc(x, y, accent=GREEN, abg=GREEN_BG):        # calculator / tool
    rect(x + 8, y, 124, 150, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True)
    rect(x + 22, y + 14, 96, 28, stroke=GREYD, bg=abg, sw=1, rough=1, rounded=True)
    for r in range(3):
        for c in range(3):
            rect(x + 26 + c * 32, y + 56 + r * 28, 22, 20, stroke=GREYD,
                 bg=(accent if (r == 2 and c == 2) else WHITE), sw=1, rough=1, rounded=True)

def obj_app(x, y, accent=VIOLET, abg=VIOLET_BG):       # mini-app
    rect(x + 6, y, 128, 150, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True)
    rect(x + 6, y, 128, 28, stroke="transparent", bg=abg, sw=1, rough=1, rounded=True)
    for k in range(3):
        ellipse(x + 20 + k * 16, y + 9, 9, 9, stroke=GREYD, bg=GREYD, sw=1)
    rect(x + 40, y + 96, 60, 32, stroke=accent, bg=accent, sw=2, rough=1, rounded=True)

def obj_chart(x, y, accent=ORANGE, abg=ORANGE_BG):     # chart
    base = y + 134
    line(x + 14, base, [[0, 0], [118, 0]], stroke=INK, sw=2)
    line(x + 14, y + 16, [[0, 0], [0, base - (y + 16)]], stroke=INK, sw=2)
    for k, hgt in enumerate([54, 92, 70, 110]):
        rect(x + 26 + k * 28, base - hgt, 20, hgt, stroke=INK, bg=accent, sw=2, rough=1, rounded=False)

def obj_diagram(x, y, accent=TEAL, abg=TEAL_BG):       # diagram
    nodes = [(x + 16, y + 18), (x + 96, y + 36), (x + 44, y + 104)]
    line(x + 16 + 20, y + 18 + 20, [[0, 0], [60, 18]], stroke=GREYD, sw=2)
    line(x + 16 + 20, y + 18 + 20, [[0, 0], [28, 86]], stroke=GREYD, sw=2)
    for nx, ny in nodes:
        ellipse(nx, ny, 40, 40, stroke=INK, bg=abg, sw=2, rough=1)

def obj_file(x, y, accent=YELLOW, abg=YELLOW_BG):      # downloadable file + arrow
    for k in range(3):
        off = (2 - k) * 12
        rect(x + 26 + off, y + off, 92, 116, stroke=INK,
             bg=(WHITE if k == 2 else abg), sw=2, rough=1, rounded=True)
    arrow(x + 72, y + 118, [[0, 0], [0, 40]], stroke=accent, sw=3, rough=1)

OBJS = [
    (obj_doc, "one-pager", BLUE, BLUE_BG),
    (obj_calc, "calculator", GREEN, GREEN_BG),
    (obj_app, "mini-app", VIOLET, VIOLET_BG),
    (obj_chart, "chart", ORANGE, ORANGE_BG),
    (obj_diagram, "diagram", TEAL, TEAL_BG),
    (obj_file, "Word / PPT\nExcel / PDF", YELLOW, YELLOW_BG),
]

def claude_face(cx, cy, r=44, color=ORANGE):
    """A friendly sketch of Claude - rounded head, two eyes, a little smile."""
    rect(cx - r, cy - r, 2 * r, 2 * r, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True)
    line(cx, cy - r, [[0, 0], [0, -18]], stroke=INK, sw=2)
    ellipse(cx - 3, cy - r - 26, 8, 8, stroke=color, bg=color, sw=2)  # antenna dot
    ellipse(cx - r * 0.42, cy - 8, 9, 9, stroke=INK, bg=INK, sw=2)
    ellipse(cx + r * 0.42 - 9, cy - 8, 9, 9, stroke=INK, bg=INK, sw=2)
    line(cx - r * 0.4, cy + r * 0.42, [[0, 0], [r * 0.4, 14], [r * 0.8, 0]], stroke=color, sw=3)

def link_icon(x, y, color=VIOLET):
    """Two interlocking chain links."""
    rect(x, y + 10, 48, 26, stroke=color, bg="transparent", sw=4, rough=1, rounded=True)
    rect(x + 34, y, 48, 26, stroke=color, bg="transparent", sw=4, rough=1, rounded=True)

def claude_window(x, y, w, h, tiny=None):
    """The hero illustration: chat on the left, Artifact panel on the right."""
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="cwin")
    line(x, y + 40, [[0, 0], [w, 0]], stroke=GREY, sw=1)
    for k in range(3):
        ellipse(x + 18 + k * 18, y + 15, 10, 10, stroke=GREY, bg=GREY, sw=1)
    # left chat: message bars
    cx = x + 26
    cw = w * 0.5 - 50
    my = y + 64
    for f in (1.0, 0.78, 0.9, 0.6):
        rect(cx, my, cw * f, 26, stroke="transparent", bg=FAINT, sw=1, rough=1, rounded=True, prefix="msg")
        my += 42
    text(cx, my + 8, "you talk here", size=SMALL, color=GREY)
    # right artifact panel
    px = x + w * 0.52
    pw = w - (w * 0.52) - 24
    py = y + 60
    ph = h - 60 - 24
    rect(px, py, pw, ph, stroke=VIOLET, bg=VIOLET_BG, sw=2, rough=1, rounded=True,
         fill="solid", opacity=40, prefix="panel")
    rect(px, py, 8, ph, stroke=VIOLET, bg=VIOLET, sw=1, rough=1, rounded=False, prefix="vedge")
    text(px + 24, py + 14, "Artifact", size=SMALL, color=VIOLET)
    if tiny is not None:
        tiny(px + pw / 2 - 65, py + ph / 2 - 75)

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
# ACCEPTANCE CHECKS
# ----------------------------------------------------------------------------
# palette discipline
for e in E:
    for key in ("strokeColor", "backgroundColor"):
        c = e.get(key)
        assert c in PALETTE, f"{e['type']} {e['id']} off-palette {key}={c}"

# no frames
assert not any(e["type"] == "frame" for e in E), "this design has no frames"

# text width must not exceed a sane single-line bound (catch silent overflow)
MAXW = max(WID.values()) + 200
overflow = [e["id"] for e in E if e["type"] == "text" and e.get("_mw", 0) > MAXW]
assert not overflow, f"text too wide: {overflow}"

# text-vs-text collision check (rough AABB; ignores rotation jitter)
texts = [e for e in E if e["type"] == "text"]
def _box(e):
    return (e["x"], e["y"], e["x"] + e.get("_mw", e["width"]), e["y"] + e["height"])
collisions = []
for a in range(len(texts)):
    ax0, ay0, ax1, ay1 = _box(texts[a])
    for b in range(a + 1, len(texts)):
        bx0, by0, bx1, by1 = _box(texts[b])
        ox_ = min(ax1, bx1) - max(ax0, bx0)
        oy_ = min(ay1, by1) - max(ay0, by0)
        if ox_ > 6 and oy_ > 6:  # meaningful overlap
            collisions.append((texts[a]["text"][:18], texts[b]["text"][:18]))
if collisions:
    print(f"[warn] {len(collisions)} text/text overlaps (check these aren't bad):")
    for c in collisions[:20]:
        print("   ", c)

for e in E:
    e.pop("_mw", None)

# ----------------------------------------------------------------------------
# WRITE + RELOAD
# ----------------------------------------------------------------------------
scene = {
    "type": "excalidraw", "version": 2, "source": "https://excalidraw.com",
    "elements": E,
    "appState": {"viewBackgroundColor": WHITE, "gridSize": None},
    "files": {},
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "2-3-artifacts.excalidraw")
with open(out, "w") as fh:
    json.dump(scene, fh, indent=2, ensure_ascii=False)
with open(out) as fh:
    reloaded = json.load(fh)
assert reloaded["type"] == "excalidraw" and reloaded["version"] == 2
assert reloaded["appState"]["viewBackgroundColor"] == WHITE
print(f"frames: 0, elements: {len(reloaded['elements'])}, width: {TOTAL_W}px")
