#!/usr/bin/env python3
"""Build claude-interface-properly.excalidraw - ONE flowing, illustrated explainer
for the "Claude interface, properly" training video (Phlo AI training, ~4 min).

Style B (house style): a single hand-drawn journey, left-to-right, NO frames, NO
boxes, white canvas, everything in Excalifont (fontFamily 5), roughness 1. A lively
Excalidraw palette colour-coded per beat, big colour-blocking, scribbled
annotations, charming primitive illustrations, and a load-bearing connector spine.
Modelled on videos/claude/3-artefacts/2-3-artifacts.excalidraw - self-contained,
embeds its own helpers + palette as the repo convention requires.

Run:  python3 build_claude_interface.py   # writes the file, reloads, asserts, prints counts
      python3 ../3-artefacts/preview.py claude-interface-properly.excalidraw out.png
"""
import json
import math
import os
import random

random.seed(40404)  # deterministic - re-runs produce identical files

# ----------------------------------------------------------------------------
# DESIGN SYSTEM - lively Excalidraw palette (matches the house style)
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
# FUN PRIMITIVES
# ----------------------------------------------------------------------------
def highlighter(x, y, w, h, color, angle=None):
    rect(x, y, w, h, stroke="transparent", bg=color, sw=1, rough=1, rounded=True,
         fill="solid", opacity=26, angle=(jit(2.0) if angle is None else angle), prefix="hl")

def sticky(x, y, w, h, fill, angle=None, prefix="sticky"):
    return rect(x, y, w, h, stroke="transparent", bg=fill, sw=1, rough=1, rounded=True,
                fill="solid", angle=(jit(2.2) if angle is None else angle), prefix=prefix)

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
    pts = [[i * w / n, math.sin(i) * 4] for i in range(n + 1)]
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

def pause_icon(x, y, size, color=YELLOW):
    bw = size * 0.32
    rect(x, y, bw, size, stroke=color, bg=color, sw=2, rough=1, rounded=False, prefix="pause")
    rect(x + bw + size * 0.3, y, bw, size, stroke=color, bg=color, sw=2, rough=1, rounded=False, prefix="pause")

def num_badge(x, y, n, accent, d=44):
    ellipse(x, y, d, d, stroke=accent, bg=accent, sw=2)
    text_centered(x + d / 2, y + d / 2 - H3 * 0.55, str(n), size=H3, color=WHITE)

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
    for k in range(5):
        rect(sb_x + 20, y + 78 + k * 54, sb_w - 40, 30, stroke="transparent", bg=WHITE,
             sw=1, rough=1, rounded=True, prefix="srow")
    # chat -> Conversations
    cx = sb_x + sb_w + 44
    cw = w * 0.42
    my = y + 78
    for f in (1.0, 0.7, 0.92, 0.6):
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
# BEAT SCAFFOLD - wide gaps so a single beat frames cleanly on a 14" laptop
# ----------------------------------------------------------------------------
GAP = 1800
WID = {1: 3120, 2: 2600, 3: 2000, 4: 2300}
ACCENT = {1: VIOLET, 2: BLUE, 3: YELLOW, 4: GREEN}
ABG = {1: VIOLET_BG, 2: BLUE_BG, 3: YELLOW_BG, 4: GREEN_BG}
OX, _c = {}, 0
for _i in range(1, 5):
    OX[_i] = _c
    _c += WID[_i] + GAP
TOTAL_W = _c

HEAD_Y = 60
MY = 620

def head(ox, title, accent, abg, sub=None):
    """Section heading: highlighter sweep + hand title + scribbled underline. No
    step-number circle here - in this video the five PARTS carry the numbers."""
    tw = text_w(title, H1, HAND)
    highlighter(ox - 8, HEAD_Y + 2, tw + 50, H1 * LINE_H + 14, abg)
    text(ox, HEAD_Y + 6, title, size=H1, color=INK)
    scribble_underline(ox, HEAD_Y + 6 + H1 * LINE_H + 8, min(tw, 520), accent, sw=4)
    if sub:
        text(ox, HEAD_Y + 6 + H1 * LINE_H + 26, sub, size=BODY, color=GREYD)

# ============================================================================
# BOARD TITLE
# ============================================================================
text(OX[1], -300, "The interface, properly", size=HERO, color=INK)
sparkles(OX[1] + text_w("The interface, properly", HERO) + 70, -230, VIOLET)
text(OX[1] + 6, -300 + HERO * LINE_H + 4,
     "five things on screen most people never touch", size=H2, color=VIOLET)
text(OX[1] + 6, -300 + HERO * LINE_H + 4 + H2 * LINE_H + 8,
     "- and they're where the productivity is", size=H3, color=GREYD)
text(OX[1] + 6, -300 + HERO * LINE_H + 4 + H2 * LINE_H + 8 + H3 * LINE_H + 10,
     "Phlo AI training  -  about 4 minutes", size=SMALL, color=GREY)

# ============================================================================
# BEAT 1 - ONE WINDOW, FIVE PARTS (the hero map)
# ============================================================================
ox = OX[1]
head(ox, "One window. Five parts.", ACCENT[1], ABG[1])
win_x, win_y, win_w, win_h = ox + 760, 320, 1500, 420
anch = claude_window_full(win_x, win_y, win_w, win_h)

def callout(sx, sy, w, h, n, accent, abg, title, body, target, frm):
    sticky(sx, sy, w, h, abg, angle=jit(1.3))
    num_badge(sx + 16, sy + 16, n, accent)
    text(sx + 78, sy + 26, title, size=H3, color=accent)
    text(sx + 30, sy + 88, body, size=SMALL, color=INK)
    fx0, fy0 = frm
    arrow(fx0, fy0, [[0, 0], [target[0] - fx0, target[1] - fy0]], stroke=accent, sw=3, rough=1)

# 2 Projects -> sidebar (top-left)
callout(ox + 40, 300, 660, 200, 2, VIOLET, VIOLET_BG, "Projects",
        "The multiplier. Persistent\ninstructions, files and memory\nacross every chat inside it.\n(Video 2.2)",
        anch["sidebar"], (ox + 700, 400))
# 1 Conversations -> chat (left, below Projects)
callout(ox + 40, 548, 660, 184, 1, ORANGE, ORANGE_BG, "Conversations",
        "Where most people live. Useful,\nbut volatile - context doesn't\ncarry between chats.",
        anch["chat"], (ox + 700, 612))
# 5 Model picker -> chip (top-right)
callout(ox + 2360, 300, 660, 156, 5, TEAL, TEAL_BG, "Model picker",
        "Match the model to the task.",
        anch["chip"], (ox + 2360, 372))
# 3 Artifacts -> panel (right, below)
callout(ox + 2360, 504, 660, 204, 3, BLUE, BLUE_BG, "Artifacts",
        "When Claude builds a document\nor tool, not just text. Opens a\nside panel - persistent, editable.",
        anch["panel"], (ox + 2360, 590))
# 4 File uploads -> paperclip (bottom-centre)
callout(ox + 1180, 804, 720, 150, 4, GREEN, GREEN_BG, "File uploads",
        "PDFs, images, spreadsheets, code.\nClaude reads them. The most\nunderused feature.",
        anch["clip"], (ox + 1300, 804))

# ============================================================================
# BEAT 2 - PICK THE MODEL DELIBERATELY
# ============================================================================
ox = OX[2]
head(ox, "Pick the model deliberately", ACCENT[2], ABG[2])

def opus_illus(cx, cy, accent):     # heavy: a stacked weight
    rect(cx - 70, cy + 56, 140, 30, stroke=INK, bg=accent, sw=2, rough=1, rounded=True)
    rect(cx - 48, cy + 28, 96, 30, stroke=INK, bg=accent, sw=2, rough=1, rounded=True)
    rect(cx - 28, cy, 56, 30, stroke=INK, bg=accent, sw=2, rough=1, rounded=True)

def sonnet_illus(cx, cy, accent):   # balanced: a bright star
    sparkle(cx, cy + 44, 38, accent, sw=3)

def haiku_illus(cx, cy, accent):    # light + fast: motion lines + a zippy dot
    for k, ln in enumerate((120, 92, 64)):
        line(cx - 60, cy + 20 + k * 24, [[0, 0], [ln, 0]], stroke=accent, sw=4, rough=1)
    ellipse(cx + 66, cy + 36, 16, 16, stroke=accent, bg=accent, sw=2)

cards = [
    ("Opus", "Claude Opus 4.8", "Deep reasoning, long-form\nwriting, complex analysis.\nSlowest, deepest.",
     INDIGO, INDIGO_BG, opus_illus, None),
    ("Sonnet", "Claude Sonnet 4.6", "Balanced speed and quality.\nMost day-to-day work.",
     GREEN, GREEN_BG, sonnet_illus, "DEFAULT"),
    ("Haiku", "Claude Haiku 4.5", "Fast and light.\nQuick lookups, simple drafts.",
     YELLOW, YELLOW_BG, haiku_illus, None),
]
cw, cgap, cy0, ch = 720, 120, 320, 430
for k, (name, sub, body, acc, abg, illus, tag) in enumerate(cards):
    cx = ox + 40 + k * (cw + cgap)
    sticky(cx, cy0, cw, ch, abg, angle=jit(1.1))
    text(cx + 40, cy0 + 28, name, size=H2, color=acc)
    text(cx + 40, cy0 + 84, sub, size=SMALL, color=GREYD)
    if tag:
        chip(cx + cw - 224, cy0 + 30, tag, fill=acc, text_color=WHITE, border=acc, size=SMALL)
    illus(cx + cw * 0.5, cy0 + 150, acc)
    text(cx + 40, cy0 + 300, body, size=BODY, color=INK)
# usage note + a faster->deeper gradient of chips
text(ox + 40, cy0 + ch + 60, "Heavier models think longer and use more of your allowance.  Lighter ones are faster.",
     size=BODY, color=GREYD)
gx = ox + 40
text(gx, cy0 + ch + 110, "faster", size=SMALL, color=GREY)
gx += 120
for lab, acc, abg in [("Haiku", YELLOW, YELLOW_BG), ("Sonnet", GREEN, GREEN_BG), ("Opus", INDIGO, INDIGO_BG)]:
    w, h = chip(gx, cy0 + ch + 100, lab, fill=abg, text_color=acc, border=acc, size=SMALL)
    gx += w
    arrow(gx + 6, cy0 + ch + 100 + h / 2, [[0, 0], [40, 0]], stroke=GREY, sw=3)
    gx += 52
text(gx + 6, cy0 + ch + 110, "deeper", size=SMALL, color=GREY)

# ============================================================================
# BEAT 3 - PAUSE HERE, AND TRY IT
# ============================================================================
ox = OX[3]
head(ox, "Pause here, and try it", ACCENT[3], ABG[3])
pause_icon(ox + 40, 322, 76, color=YELLOW)
highlighter(ox + 150, 318, 940, 130, YELLOW_BG, angle=0.0)
text(ox + 174, 336, "Open Claude. Switch to a model that\nisn't your default. Run one prompt.",
     size=H3, color=INK)
ex_x = ox + 60
for lab in ["try Opus", "or Haiku", "notice the difference"]:
    w, h = chip(ex_x, 510, lab, fill=WHITE, text_color=YELLOW, border=YELLOW, size=SMALL)
    ex_x += w + 40
sparkles(ox + 90, 300, YELLOW)
text(ox + 60, 610, "60 seconds - then carry on.", size=BODY, color=GREYD)

# ============================================================================
# BEAT 4 - FIVE FEATURES, FOUR MINUTES (close)
# ============================================================================
ox = OX[4]
head(ox, "Five features. Four minutes.", ACCENT[4], ABG[4])
recap = [("Conversations", ORANGE, ORANGE_BG), ("Projects", VIOLET, VIOLET_BG),
         ("Artifacts", BLUE, BLUE_BG), ("File uploads", GREEN, GREEN_BG),
         ("Model picker", TEAL, TEAL_BG)]
rx = ox + 40
for lab, acc, abg in recap:
    w, h = chip(rx, 320, lab, fill=abg, text_color=acc, border=acc, size=SMALL)
    rx += w + 32
nxt = "Next: Projects - the one that compounds for years."
text(ox + 40, 440, nxt, size=H3, color=INK)
circle_around(ox + 40 + text_w("Next: ", H3) - 6, 434, text_w("Projects", H3) + 24, H3 * LINE_H + 16, VIOLET, sw=3)
sparkles(ox + 80, 590, YELLOW)
text(ox + 130, 580, "Docs: Claude Help Centre - support.claude.com", size=SMALL, color=VIOLET)
text(ox + 40, 700, "Phlo AI training  -  the interface", size=SMALL, color=GREY)

# ============================================================================
# CONNECTOR SPINE - the through-line that makes it ONE picture
# ============================================================================
for i in range(1, 4):
    x0 = OX[i] + WID[i]
    x1 = OX[i + 1]
    acc = ACCENT[i + 1]
    arrow(x0 + 20, MY, [[0, 0], [(x1 - x0) * 0.4, -36], [(x1 - x0) * 0.6, 30], [x1 - x0 - 40, 0]],
          stroke=acc, sw=4, rough=1)
line(OX[1] + 40, MY + 340, [[0, 0], [TOTAL_W - 400, 0]], stroke=FAINT, sw=2, rough=1, dashed=True, opacity=60)

# ----------------------------------------------------------------------------
# ACCEPTANCE CHECKS (Style B): palette discipline, no frames, overflow, collisions
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
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "claude-interface-properly.excalidraw")
with open(out, "w") as fh:
    json.dump(scene, fh, indent=2, ensure_ascii=False)
with open(out) as fh:
    reloaded = json.load(fh)
assert reloaded["type"] == "excalidraw" and reloaded["version"] == 2
assert reloaded["appState"]["viewBackgroundColor"] == WHITE
ids = [e["id"] for e in reloaded["elements"]]
assert len(ids) == len(set(ids)), "duplicate ids"
print(f"frames: 0, elements: {len(reloaded['elements'])}, width: {TOTAL_W}px, collisions: {len(collisions)}")
