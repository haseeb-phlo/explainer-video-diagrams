#!/usr/bin/env python3
"""excalidraw_kit - the shared Style B engine for Phlo AI-training diagrams.

ONE flowing, illustrated, hand-drawn journey: no frames, white canvas, the hand
font (fontFamily 1, as in the canonical 3-artefacts build), roughness 1, a
lively colour-coded Excalidraw palette, colour
blocking, scribbled annotations, charming primitive illustrations and a connector
spine. This module is the single source of truth for the LOOK - the palette, the
element factory, the fun primitives, the reusable illustrations, and the
validate/finish tail.

Each video's `build.py` does:

    import random
    from excalidraw_kit import *
    random.seed(<n>)                 # deterministic - re-runs are identical
    # ... define the scene + its own beat scaffold (OX/WID/ACCENT, beat_head, spine)
    finish(out_path, max_w=<n>, total_w=<n>)

Scene-level layout (how many beats, their widths/accents, the heading style) lives
in each build.py, not here - that is composition, not vocabulary. Bespoke one-off
illustrations also stay in the build that needs them.

The element factory + primitives are lifted verbatim from the canonical
videos/claude/3-artefacts build, so migrating a self-contained script to this kit
reproduces byte-identical output (same seed -> same random sequence).
"""
import json
import math
import random

# ----------------------------------------------------------------------------
# DESIGN SYSTEM - lively Excalidraw palette
# ----------------------------------------------------------------------------
WHITE = "#ffffff"
INK   = "#1e1e1e"   # primary text / strokes
GREYD = "#495057"   # secondary text
GREY  = "#868e96"   # captions, faint lines
FAINT = "#dee2e6"   # very light guide lines

# accent stroke + pastel fill + ultra-light tint (the soft full-beat wash)
VIOLET, VIOLET_BG, VIOLET_T = "#7048e8", "#d0bfff", "#f3f0ff"
ORANGE, ORANGE_BG, ORANGE_T = "#e8590c", "#ffd8a8", "#fff4e6"
GREEN,  GREEN_BG,  GREEN_T  = "#2f9e44", "#b2f2bb", "#ebfbee"
BLUE,   BLUE_BG,   BLUE_T   = "#1971c2", "#a5d8ff", "#e7f5ff"
RED,    RED_BG,    RED_T     = "#c92a2a", "#ffc9c9", "#fff5f5"
TEAL,   TEAL_BG,   TEAL_T    = "#0c8599", "#99e9f2", "#e6fcf5"
YELLOW, YELLOW_BG, YELLOW_T = "#f08c00", "#ffec99", "#fff9db"
INDIGO, INDIGO_BG, INDIGO_T = "#364fc7", "#bac8ff", "#edf2ff"

PALETTE = {WHITE, INK, GREYD, GREY, FAINT, "transparent",
           VIOLET, VIOLET_BG, VIOLET_T, ORANGE, ORANGE_BG, ORANGE_T,
           GREEN, GREEN_BG, GREEN_T, BLUE, BLUE_BG, BLUE_T,
           RED, RED_BG, RED_T, TEAL, TEAL_BG, TEAL_T,
           YELLOW, YELLOW_BG, YELLOW_T, INDIGO, INDIGO_BG, INDIGO_T}

# Type scale
HERO, H1, H2, H3, BODY, LABEL, SMALL = 96, 48, 34, 28, 22, 20, 17
HAND = 1  # the canonical hand font (Virgil) - the ONLY font allowed (see 3-artefacts)
LINE_H = 1.4  # roomier line spacing between lines within a text block
WFAC = 0.56  # generous glyph-width factor (over-estimate is safe)

# ----------------------------------------------------------------------------
# ELEMENT FACTORY  (verbatim from the canonical build)
# ----------------------------------------------------------------------------
E = []          # the scene; build.py appends to this via the helpers below
_seq = 0

def reset():
    """Clear the scene. A fresh process starts empty, so this is only needed if a
    single process builds more than one scene."""
    global E, _seq
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

def play_icon(x, y, size, color=ORANGE):
    line(x, y, [[0, 0], [size, size / 2], [0, size], [0, 0]], stroke=color, sw=2,
         rough=1, bg=color, fill="solid", prefix="play")

def pause_icon(x, y, size, color=ORANGE):
    bw = size * 0.32
    rect(x, y, bw, size, stroke=color, bg=color, sw=2, rough=1, rounded=False, prefix="pause")
    rect(x + bw + size * 0.3, y, bw, size, stroke=color, bg=color, sw=2, rough=1, rounded=False, prefix="pause")

def demo_badge(x, y, label):
    """A 'live demo' pill with a play glyph - the [TO CLAUDE] cut-aways."""
    tw = text_w(label, SMALL, HAND)
    w, h = tw + 96, 56
    a = jit(1.5)
    rect(x, y, w, h, stroke=ORANGE, bg=ORANGE_BG, sw=2, rough=1, rounded=True,
         fill="solid", angle=a, opacity=70, prefix="demo")
    play_icon(x + 24, y + 16, 22, color=ORANGE)
    text(x + 60, y + 16, label, size=SMALL, color=ORANGE, angle=a, width=tw)
    return w, h

def num_circle(x, y, n, accent, d=56):
    """A numbered step circle: accent outline, accent numeral on white."""
    ellipse(x, y, d, d, stroke=accent, bg=WHITE, sw=3, rough=1)
    text_centered(x + d / 2, y + d / 2 - H2 * 0.5, str(n), size=H2, color=accent)

def num_badge(x, y, n, accent, d=44):
    """A filled numbered badge: white numeral on an accent disc."""
    ellipse(x, y, d, d, stroke=accent, bg=accent, sw=2)
    text_centered(x + d / 2, y + d / 2 - H3 * 0.55, str(n), size=H3, color=WHITE)

TINT = {VIOLET: VIOLET_T, ORANGE: ORANGE_T, GREEN: GREEN_T, BLUE: BLUE_T,
        RED: RED_T, TEAL: TEAL_T, YELLOW: YELLOW_T, INDIGO: INDIGO_T}

def heading(x, y, title, color=INK, sub=None, kicker=None):
    """A prominent-but-unpolished section heading: a big hand title in the beat's
    accent colour with a lively hand-drawn underline (no highlighter block, no
    number badge). Optional small grey kicker above and a sub line below."""
    yy = y
    if kicker:
        text(x, yy, kicker, size=SMALL, color=GREY)
        yy += SMALL * LINE_H + 6
    text(x, yy, title, size=H1, color=color)
    scribble_underline(x, yy + H1 * LINE_H + 4, min(text_w(title, H1), 520), color, sw=3)
    if sub:
        text(x, yy + H1 * LINE_H + 30, sub, size=BODY, color=GREYD)

def beat_band(x, y, w, h, accent, opacity=100):
    """A soft, borderless ultra-light colour wash behind a beat - 'more colour' +
    makes each beat read as an individual zone. Not a bordered box."""
    rect(x, y, w, h, stroke="transparent", bg=TINT.get(accent, VIOLET_T), sw=1,
         rough=1, rounded=True, fill="solid", opacity=opacity, prefix="band")

def clock(cx, cy, r, color):
    ellipse(cx - r, cy - r, 2 * r, 2 * r, stroke=color, bg=WHITE, sw=3, rough=1)
    line(cx, cy, [[0, 0], [0, -r * 0.6]], stroke=color, sw=3)
    line(cx, cy, [[0, 0], [r * 0.5, 0]], stroke=color, sw=3)

# ----------------------------------------------------------------------------
# REUSABLE ILLUSTRATIONS - charming, from primitives, colour-coded
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

def obj_files(x, y, accent=GREEN, abg=GREEN_BG):       # a stack of reference files
    for k in range(3):
        off = (2 - k) * 12
        rect(x + 18 + off, y + off, 92, 120, stroke=INK, bg=(WHITE if k == 2 else abg), sw=2, rough=1, rounded=True)
    for k in range(3):
        line(x + 34, y + 40 + k * 22, [[0, 0], [60, 0]], stroke=GREY, sw=2)

def claude_face(cx, cy, r=44, color=ORANGE):
    """A friendly sketch of Claude - rounded head, two eyes, a little smile."""
    rect(cx - r, cy - r, 2 * r, 2 * r, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True)
    line(cx, cy - r, [[0, 0], [0, -18]], stroke=INK, sw=2)
    ellipse(cx - 3, cy - r - 26, 8, 8, stroke=color, bg=color, sw=2)  # antenna dot
    ellipse(cx - r * 0.42, cy - 8, 9, 9, stroke=INK, bg=INK, sw=2)
    ellipse(cx + r * 0.42 - 9, cy - 8, 9, 9, stroke=INK, bg=INK, sw=2)
    line(cx - r * 0.4, cy + r * 0.42, [[0, 0], [r * 0.4, 14], [r * 0.8, 0]], stroke=color, sw=3)

def person(cx, cy, color):
    """A tiny stick person - head + torso triangle."""
    ellipse(cx - 16, cy - 38, 32, 32, stroke=color, bg=WHITE, sw=3, rough=1)
    line(cx, cy - 6, [[0, 0], [-22, 40], [44, 0], [-22, -40]], stroke=color, sw=3, rough=1)

def link_icon(x, y, color=VIOLET):
    """Two interlocking chain links."""
    rect(x, y + 10, 48, 26, stroke=color, bg="transparent", sw=4, rough=1, rounded=True)
    rect(x + 34, y, 48, 26, stroke=color, bg="transparent", sw=4, rough=1, rounded=True)

def claude_window(x, y, w, h, tiny=None):
    """Chat on the left, Artifact panel on the right."""
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="cwin")
    line(x, y + 40, [[0, 0], [w, 0]], stroke=GREY, sw=1)
    for k in range(3):
        ellipse(x + 18 + k * 18, y + 15, 10, 10, stroke=GREY, bg=GREY, sw=1)
    cx = x + 26
    cw = w * 0.5 - 50
    my = y + 64
    for f in (1.0, 0.78, 0.9, 0.6):
        rect(cx, my, cw * f, 26, stroke="transparent", bg=FAINT, sw=1, rough=1, rounded=True, prefix="msg")
        my += 42
    text(cx, my + 8, "you talk here", size=SMALL, color=GREY)
    px = x + w * 0.52
    pw = w - (w * 0.52) - 24
    py = y + 60
    ph = h - 60 - 24
    rect(px, py, pw, ph, stroke=VIOLET, bg=VIOLET_BG, sw=2, rough=1, rounded=True, fill="solid", opacity=40, prefix="panel")
    rect(px, py, 8, ph, stroke=VIOLET, bg=VIOLET, sw=1, rough=1, rounded=False, prefix="vedge")
    text(px + 24, py + 14, "Artifact", size=SMALL, color=VIOLET)
    if tiny is not None:
        tiny(px + pw / 2 - 65, py + ph / 2 - 75)

# ----------------------------------------------------------------------------
# VALIDATE + WRITE  (the acceptance checks + JSON tail, shared by every build)
# ----------------------------------------------------------------------------
def validate(max_w):
    """Style B acceptance checks: palette discipline, the hand font, no frames,
    text overflow, text/text collisions (printed as warnings). Off-palette colours
    and non-hand fonts are HARD asserts here, mirrored by build_all's guard so the
    same rules apply to kit-built scenes and to files on disk. Returns the
    collision count."""
    for e in E:
        for key in ("strokeColor", "backgroundColor"):
            assert e.get(key) in PALETTE, f"{e['type']} {e['id']} off-palette {key}={e.get(key)}"
        if e["type"] == "text":
            assert e.get("fontFamily") == HAND, \
                f"text {e['id']} non-hand fontFamily={e.get('fontFamily')} (must be {HAND})"
    assert not any(e["type"] == "frame" for e in E), "Style B has no frames"
    overflow = [e["id"] for e in E if e["type"] == "text" and e.get("_mw", 0) > max_w]
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
    return len(collisions)

def finish(out_path, max_w, total_w=None):
    """Validate, strip scratch fields, write the .excalidraw, reload + assert."""
    n_collisions = validate(max_w)
    for e in E:
        e.pop("_mw", None)
    scene = {
        "type": "excalidraw", "version": 2, "source": "https://excalidraw.com",
        "elements": E,
        "appState": {"viewBackgroundColor": WHITE, "gridSize": None},
        "files": {},
    }
    with open(out_path, "w") as fh:
        json.dump(scene, fh, indent=2, ensure_ascii=False)
    with open(out_path) as fh:
        reloaded = json.load(fh)
    assert reloaded["type"] == "excalidraw" and reloaded["version"] == 2
    assert reloaded["appState"]["viewBackgroundColor"] == WHITE
    ids = [e["id"] for e in reloaded["elements"]]
    assert len(ids) == len(set(ids)), "duplicate ids"
    width = f", width: {total_w}px" if total_w is not None else ""
    print(f"frames: 0, elements: {len(reloaded['elements'])}{width}, collisions: {n_collisions} -> {out_path}")
