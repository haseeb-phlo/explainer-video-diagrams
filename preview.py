#!/usr/bin/env python3
"""Approximate raster preview of an .excalidraw scene, for eyeballing layout.

Not a faithful renderer - it ignores hand-drawn roughness and uses macOS system
fonts as stand-ins - but it shows composition, colour, overlap and text overflow,
which is what we need to verify a "make it fun and visual" redesign without
Excalidraw itself.

Usage:  python3 preview.py [scene.excalidraw] [out.png]
"""
import json
import math
import os
import sys

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SCENE = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "videos/claude/3-artefacts/3-artifacts.excalidraw")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "preview.png")
# optional x-window for close-up inspection:  preview.py scene out XMIN XMAX
WIN_XMIN = float(sys.argv[3]) if len(sys.argv) > 3 else None
WIN_XMAX = float(sys.argv[4]) if len(sys.argv) > 4 else None

# Font stand-ins: hand-drawn for fontFamily 1/5, sans for 2, mono for 3.
HAND_FONT = "/System/Library/Fonts/Supplemental/Bradley Hand Bold.ttf"
SANS_FONT = "/System/Library/Fonts/Supplemental/Arial.ttf"
MONO_FONT = "/System/Library/Fonts/Menlo.ttc"
if not os.path.exists(MONO_FONT):
    MONO_FONT = SANS_FONT


def font_path(family):
    if family in (1, 5):
        return HAND_FONT
    if family == 3:
        return MONO_FONT
    return SANS_FONT


_FCACHE = {}
def get_font(family, size):
    key = (family, int(size))
    if key not in _FCACHE:
        try:
            _FCACHE[key] = ImageFont.truetype(font_path(family), int(size))
        except Exception:
            _FCACHE[key] = ImageFont.load_default()
    return _FCACHE[key]


def main():
    scene = json.load(open(SCENE))
    els = scene["elements"]
    bg = scene.get("appState", {}).get("viewBackgroundColor", "#ffffff")

    # bounds
    xs, ys = [], []
    for e in els:
        xs += [e["x"], e["x"] + e.get("width", 0)]
        ys += [e["y"], e["y"] + e.get("height", 0)]
    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)
    margin = 80
    minx -= margin; miny -= margin; maxx += margin; maxy += margin
    if WIN_XMIN is not None:
        minx = WIN_XMIN
    if WIN_XMAX is not None:
        maxx = WIN_XMAX
    w = maxx - minx; h = maxy - miny

    # scale to keep the long axis <= 6000px so text stays legible but file is sane
    scale = min(1.0, 6000.0 / max(w, h))
    W = int(w * scale); H = int(h * scale)
    img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img, "RGBA")

    def sx(x): return (x - minx) * scale
    def sy(y): return (y - miny) * scale

    def col(c, alpha=255):
        if c in (None, "transparent"):
            return None
        c = c.lstrip("#")
        if len(c) == 3:
            c = "".join(ch * 2 for ch in c)
        r, g, b = int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16)
        return (r, g, b, alpha)

    for e in els:
        t = e["type"]
        x, y = sx(e["x"]), sy(e["y"])
        ew, eh = e.get("width", 0) * scale, e.get("height", 0) * scale
        stroke = col(e.get("strokeColor"))
        sw = max(1, int(e.get("strokeWidth", 1) * scale))
        bgc = e.get("backgroundColor")
        fill_alpha = 110 if e.get("fillStyle") == "hachure" else 255
        fillc = col(bgc, fill_alpha)

        if t in ("rectangle", "frame"):
            r = 12 * scale if e.get("roundness") else 0
            d.rounded_rectangle([x, y, x + ew, y + eh], radius=r, fill=fillc, outline=stroke, width=sw)
        elif t == "ellipse":
            d.ellipse([x, y, x + ew, y + eh], fill=fillc, outline=stroke, width=sw)
        elif t == "diamond":
            cx, cy = x + ew / 2, y + eh / 2
            d.polygon([(cx, y), (x + ew, cy), (cx, y + eh), (x, cy)], fill=fillc, outline=stroke)
        elif t in ("line", "arrow"):
            pts = [(x + px * scale, y + py * scale) for px, py in e.get("points", [])]
            if len(pts) >= 2:
                d.line(pts, fill=stroke, width=sw, joint="curve")
                if t == "arrow" and e.get("endArrowhead"):
                    (x1, y1), (x2, y2) = pts[-2], pts[-1]
                    ang = math.atan2(y2 - y1, x2 - x1)
                    hl = 14 * scale
                    for da in (math.radians(150), math.radians(-150)):
                        d.line([(x2, y2), (x2 + hl * math.cos(ang + da), y2 + hl * math.sin(ang + da))],
                               fill=stroke, width=sw)
        elif t == "text":
            f = get_font(e.get("fontFamily", 1), e.get("fontSize", 16) * scale)
            color = stroke or (30, 30, 30, 255)
            align = e.get("textAlign", "left")
            lh = e.get("fontSize", 16) * e.get("lineHeight", 1.25) * scale
            for i, ln in enumerate(e.get("text", "").split("\n")):
                ly = y + i * lh
                lx = x
                if align in ("center", "right"):
                    tw = d.textlength(ln, font=f)
                    lx = x + (ew - tw) / (2 if align == "center" else 1)
                d.text((lx, ly), ln, font=f, fill=color)

    img.save(OUT)
    print(f"wrote {OUT}  ({W}x{H}, scale={scale:.3f}, {len(els)} elements)")


if __name__ == "__main__":
    main()
