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
import json
import math
import os
import random

random.seed(22022)

# ----------------------------------------------------------------------------
# DESIGN SYSTEM - lively Excalidraw palette
# ----------------------------------------------------------------------------
WHITE = "#ffffff"
INK   = "#1e1e1e"
GREYD = "#495057"
GREY  = "#868e96"
FAINT = "#dee2e6"
VIOLET, VIOLET_BG = "#7048e8", "#d0bfff"
ORANGE, ORANGE_BG = "#e8590c", "#ffd8a8"
GREEN,  GREEN_BG  = "#2f9e44", "#b2f2bb"
BLUE,   BLUE_BG   = "#1971c2", "#a5d8ff"
RED,    RED_BG     = "#c92a2a", "#ffc9c9"
TEAL,   TEAL_BG    = "#0c8599", "#99e9f2"
YELLOW, YELLOW_BG = "#f08c00", "#ffec99"
INDIGO, INDIGO_BG = "#364fc7", "#bac8ff"
PALETTE = {WHITE, INK, GREYD, GREY, FAINT, "transparent",
           VIOLET, VIOLET_BG, ORANGE, ORANGE_BG, GREEN, GREEN_BG,
           BLUE, BLUE_BG, RED, RED_BG, TEAL, TEAL_BG, YELLOW, YELLOW_BG,
           INDIGO, INDIGO_BG}
HERO, H1, H2, H3, BODY, LABEL, SMALL = 96, 48, 34, 28, 22, 20, 17
HAND = 5
LINE_H = 1.25
WFAC = 0.56

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
    return random.uniform(-maxdeg, maxdeg) * math.pi / 180.0

def _base(eid, etype, x, y, w, h, angle=0.0, opacity=100):
    return {
        "id": eid, "type": etype,
        "x": float(x), "y": float(y), "width": float(w), "height": float(h),
        "angle": float(angle), "strokeColor": INK, "backgroundColor": "transparent",
        "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
        "roughness": 1, "opacity": opacity, "groupIds": [], "frameId": None, "roundness": None,
        "seed": random.randint(1, 2**31), "version": 1,
        "versionNonce": random.randint(1, 2**31), "isDeleted": False,
        "boundElements": None, "updated": 1717200000000, "link": None, "locked": False,
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

def line(x, y, points, stroke=INK, sw=2, rough=1, bg="transparent", fill="solid",
         opacity=100, prefix="line", dashed=False):
    xs = [p[0] for p in points]; ys = [p[1] for p in points]
    e = _base(_uid(prefix), "line", x, y, max(xs) - min(xs), max(ys) - min(ys), 0.0, opacity)
    e.update(strokeColor=stroke, backgroundColor=bg, strokeWidth=sw, roughness=rough,
             fillStyle=fill, strokeStyle=("dashed" if dashed else "solid"),
             points=[[float(px), float(py)] for px, py in points],
             startArrowhead=None, endArrowhead=None, lastCommittedPoint=None, roundness=None)
    E.append(e); return e

def arrow(x, y, points, stroke=INK, sw=2, rough=1, prefix="arr", dashed=False, head="arrow"):
    xs = [p[0] for p in points]; ys = [p[1] for p in points]
    e = _base(_uid(prefix), "arrow", x, y, max(xs) - min(xs), max(ys) - min(ys))
    e.update(strokeColor=stroke, backgroundColor="transparent", strokeWidth=sw, roughness=rough,
             strokeStyle=("dashed" if dashed else "solid"),
             points=[[float(px), float(py)] for px, py in points],
             startArrowhead=None, endArrowhead=head, lastCommittedPoint=None, roundness=None)
    E.append(e); return e

def text_w(s, size, font=HAND):
    return max((len(ln) for ln in s.split("\n")), default=0) * size * WFAC

def text_h(s, size):
    return len(s.split("\n")) * size * LINE_H

def text(x, y, s, size=BODY, font=HAND, color=INK, align="left", width=None, angle=0.0, opacity=100):
    w = width if width is not None else text_w(s, size, font)
    e = _base(_uid("txt"), "text", x, y, w, text_h(s, size), angle, opacity)
    e.update(strokeColor=color, backgroundColor="transparent", roughness=1, text=s,
             fontSize=size, fontFamily=font, textAlign=align, verticalAlign="top",
             containerId=None, originalText=s, lineHeight=LINE_H, roundness=None)
    E.append(e); e["_mw"] = text_w(s, size, font); return e

def text_centered(cx, y, s, size=BODY, font=HAND, color=INK, angle=0.0):
    w = text_w(s, size, font)
    return text(cx - w / 2, y, s, size=size, font=font, color=color, align="center", width=w, angle=angle)

# ----------------------------------------------------------------------------
# FUN PRIMITIVES
# ----------------------------------------------------------------------------
def highlighter(x, y, w, h, color, angle=None):
    rect(x, y, w, h, stroke="transparent", bg=color, sw=1, rough=1, rounded=True, fill="solid",
         opacity=26, angle=(jit(2.0) if angle is None else angle), prefix="hl")

def sticky(x, y, w, h, fill, angle=None, prefix="sticky"):
    return rect(x, y, w, h, stroke="transparent", bg=fill, sw=1, rough=1, rounded=True, fill="solid",
                angle=(jit(2.2) if angle is None else angle), prefix=prefix)

def chip(x, y, label, fill=WHITE, text_color=INK, border=GREYD, size=LABEL, angle=None, sw=2):
    tw = text_w(label, size, HAND)
    px, py = 22, 12
    w, h = tw + 2 * px, size * LINE_H + 2 * py
    a = jit(1.8) if angle is None else angle
    rect(x, y, w, h, stroke=border, bg=fill, sw=sw, rough=1, rounded=True, fill="solid", angle=a, prefix="chip")
    text(x + px, y + py, label, size=size, color=text_color, angle=a, width=tw)
    return w, h

def scribble_underline(x, y, w, color, sw=3):
    n = max(3, int(w / 80))
    line(x, y, [[i * w / n, math.sin(i) * 4] for i in range(n + 1)], stroke=color, sw=sw, rough=1, prefix="ul")

def circle_around(x, y, w, h, color, sw=3):
    ellipse(x, y, w, h, stroke=color, bg="transparent", sw=sw, rough=2, prefix="circ")

def sparkle(cx, cy, s, color, sw=2):
    p = [[0, -s], [0.28 * s, -0.28 * s], [s, 0], [0.28 * s, 0.28 * s], [0, s],
         [-0.28 * s, 0.28 * s], [-s, 0], [-0.28 * s, -0.28 * s], [0, -s]]
    line(cx, cy, p, stroke=color, sw=sw, rough=1, bg=color, fill="solid", prefix="spk")

def sparkles(cx, cy, color):
    sparkle(cx, cy, 22, color, 2); sparkle(cx + 38, cy - 30, 12, color, 2); sparkle(cx - 30, cy - 22, 9, color, 2)

def pause_icon(x, y, size, color=YELLOW):
    bw = size * 0.32
    rect(x, y, bw, size, stroke=color, bg=color, sw=2, rough=1, rounded=False, prefix="pause")
    rect(x + bw + size * 0.3, y, bw, size, stroke=color, bg=color, sw=2, rough=1, rounded=False, prefix="pause")

def demo_badge(x, y, label):
    tw = text_w(label, SMALL, HAND)
    w, h = tw + 96, 56
    a = jit(1.5)
    rect(x, y, w, h, stroke=ORANGE, bg=ORANGE_BG, sw=2, rough=1, rounded=True, fill="solid", opacity=70, prefix="demo")
    line(x + 24, y + 16, [[0, 0], [22, 11], [0, 22], [0, 0]], stroke=ORANGE, sw=2, rough=1, bg=ORANGE, fill="solid", prefix="play")
    text(x + 60, y + 16, label, size=SMALL, color=ORANGE, angle=a, width=tw)
    return w, h

def num_circle(x, y, n, accent, d=56):
    ellipse(x, y, d, d, stroke=accent, bg=WHITE, sw=3, rough=1)
    text_centered(x + d / 2, y + d / 2 - H2 * 0.5, str(n), size=H2, color=accent)

def clock(cx, cy, r, color):
    ellipse(cx - r, cy - r, 2 * r, 2 * r, stroke=color, bg=WHITE, sw=3, rough=1)
    line(cx, cy, [[0, 0], [0, -r * 0.6]], stroke=color, sw=3)
    line(cx, cy, [[0, 0], [r * 0.5, 0]], stroke=color, sw=3)

def claude_face(cx, cy, r=44, color=VIOLET):
    rect(cx - r, cy - r, 2 * r, 2 * r, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True)
    line(cx, cy - r, [[0, 0], [0, -18]], stroke=INK, sw=2)
    ellipse(cx - 3, cy - r - 26, 8, 8, stroke=color, bg=color, sw=2)
    ellipse(cx - r * 0.42, cy - 8, 9, 9, stroke=INK, bg=INK, sw=2)
    ellipse(cx + r * 0.42 - 9, cy - 8, 9, 9, stroke=INK, bg=INK, sw=2)
    line(cx - r * 0.4, cy + r * 0.42, [[0, 0], [r * 0.4, 14], [r * 0.8, 0]], stroke=color, sw=3)

def person(cx, cy, color):
    ellipse(cx - 16, cy - 38, 32, 32, stroke=color, bg=WHITE, sw=3, rough=1)
    line(cx, cy - 6, [[0, 0], [-22, 40], [44, 0], [-22, -40]], stroke=color, sw=3, rough=1)

def obj_doc(x, y, accent=BLUE, abg=BLUE_BG):
    rect(x + 18, y, 104, 150, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True)
    rect(x + 18, y, 104, 26, stroke="transparent", bg=abg, sw=1, rough=1, rounded=True)
    for k in range(4):
        line(x + 34, y + 50 + k * 24, [[0, 0], [72, 0]], stroke=GREY, sw=2)

def obj_files(x, y, accent=GREEN, abg=GREEN_BG):
    for k in range(3):
        off = (2 - k) * 12
        rect(x + 18 + off, y + off, 92, 120, stroke=INK, bg=(WHITE if k == 2 else abg), sw=2, rough=1, rounded=True)
    for k in range(3):
        line(x + 34, y + 40 + k * 22, [[0, 0], [60, 0]], stroke=GREY, sw=2)

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
# ACCEPTANCE CHECKS
# ----------------------------------------------------------------------------
for e in E:
    for key in ("strokeColor", "backgroundColor"):
        assert e.get(key) in PALETTE, f"{e['type']} {e['id']} off-palette {key}={e.get(key)}"
assert not any(e["type"] == "frame" for e in E), "this design has no frames"
MAXW = max(WID.values()) + 200
overflow = [e["id"] for e in E if e["type"] == "text" and e.get("_mw", 0) > MAXW]
assert not overflow, f"text too wide: {overflow}"
texts = [e for e in E if e["type"] == "text"]
def _box(e):
    return (e["x"], e["y"], e["x"] + e.get("_mw", e["width"]), e["y"] + e["height"])
collisions = []
for a in range(len(texts)):
    ax0, ay0, ax1, ay1 = _box(texts[a])
    for b in range(a + 1, len(texts)):
        bx0, by0, bx1, by1 = _box(texts[b])
        if min(ax1, bx1) - max(ax0, bx0) > 6 and min(ay1, by1) - max(ay0, by0) > 6:
            collisions.append((texts[a]["text"][:18], texts[b]["text"][:18]))
if collisions:
    print(f"[warn] {len(collisions)} text/text overlaps:")
    for c in collisions[:25]:
        print("   ", c)
for e in E:
    e.pop("_mw", None)

# ----------------------------------------------------------------------------
# WRITE + RELOAD
# ----------------------------------------------------------------------------
scene = {"type": "excalidraw", "version": 2, "source": "https://excalidraw.com", "elements": E,
         "appState": {"viewBackgroundColor": WHITE, "gridSize": None}, "files": {}}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "phlo-2.2-claude-projects.excalidraw")
with open(out, "w") as fh:
    json.dump(scene, fh, indent=2, ensure_ascii=False)
with open(out) as fh:
    reloaded = json.load(fh)
assert reloaded["type"] == "excalidraw" and reloaded["version"] == 2
ids = [e["id"] for e in reloaded["elements"]]
assert len(ids) == len(set(ids)), "duplicate ids"
print(f"frames: 0, elements: {len(reloaded['elements'])}, width: {TOTAL_W}px, collisions: {len(collisions)}")
