#!/usr/bin/env python3
"""Build connectors-mcp-training.excalidraw - ONE flowing, illustrated explainer
for the "Claude Connectors & MCP" training video (Phlo AI Ops Learn, module 2.6).

This is a conversion of an externally-supplied brief that asked for a 10-frame,
teal/lime/cream, mixed-font deck. The CONTENT (the ten scenes, the literal copy)
is preserved verbatim; the STYLING is dropped in favour of the project's house
Style B: a single hand-drawn journey that reads left-to-right - NO frames, NO
boxed slides, white canvas, everything in Excalifont, roughness 1, a lively
colour-coded Excalidraw palette, colour blocking, scribbled annotations and
charming primitive illustrations. The "look here" accent and "caution" colour
the brief reserved for lime/coral map onto each beat's own accent and onto RED
respectively. The look lives in the shared excalidraw_kit; this file holds only
the composition.

Run:  python3 videos/claude/6-connectors-mcp/build_connectors_mcp.py
      python3 preview.py videos/claude/6-connectors-mcp/connectors-mcp-training.excalidraw out.png
"""
import os
import sys

_d = os.path.dirname(os.path.abspath(__file__))
while _d != os.path.dirname(_d) and not os.path.exists(os.path.join(_d, "excalidraw_kit.py")):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)

import random
from excalidraw_kit import *

random.seed(60610)  # deterministic - re-runs produce identical files

# ----------------------------------------------------------------------------
# BEAT SCAFFOLD  (10 beats, wide gaps so one frames cleanly on a 14" laptop)
# ----------------------------------------------------------------------------
# Every beat uses the SAME slot, shaped like the reference's "Words left, a thing
# right" beat (~1120 wide x ~980 tall content, ~1.15 : 1) so framing is identical
# and it fits a 14" MacBook screen. Wide gaps so a single beat frames cleanly with
# no neighbours peeking in - the empty space IS the zoom-to-one-beat affordance.
N = 10
GAP = 800
WID = {i: 1200 for i in range(1, N + 1)}
ACCENT = {1: VIOLET, 2: ORANGE, 3: BLUE, 4: GREEN, 5: TEAL,
          6: INDIGO, 7: VIOLET, 8: RED, 9: GREEN, 10: ORANGE}
ABG = {1: VIOLET_BG, 2: ORANGE_BG, 3: BLUE_BG, 4: GREEN_BG, 5: TEAL_BG,
       6: INDIGO_BG, 7: VIOLET_BG, 8: RED_BG, 9: GREEN_BG, 10: ORANGE_BG}
OX = {}
_c = 0
for _i in range(1, N + 1):
    OX[_i] = _c
    _c += WID[_i] + GAP
TOTAL_W = _c

HEAD_Y = 60


def beat_head(i, title, sub=None):
    # QUIET heading: plain hand title in the beat's accent colour, no step circle,
    # no highlighter sweep behind it - the unpolished natural-flow look.
    ox = OX[i]
    heading(ox, HEAD_Y, title, color=ACCENT[i], sub=sub)
    return ox


BEATS = []
def mark(label):
    prev = BEATS[-1][2] if BEATS else 0
    BEATS.append((label, len(E) - prev, len(E)))


# ----------------------------------------------------------------------------
# LOCAL ONE-OFF ILLUSTRATIONS  (bespoke to this video, kept out of the kit)
# ----------------------------------------------------------------------------
def tick(x, y, color=GREEN, s=26):
    line(x, y, [[0, s * 0.5], [s * 0.42, s], [s, 0]], stroke=color, sw=4, rough=1, prefix="tick")


def check_item(x, y, s, color=INK, accent=GREEN, size=BODY):
    tick(x, y + 2, accent)
    text(x + 46, y, s, size=size, color=color)


def button(x, y, label, accent, w=300, h=66, filled=True):
    """A control button: filled accent + white label, or an outline + ink label."""
    if filled:
        rect(x, y, w, h, stroke=accent, bg=accent, sw=2, rough=1, rounded=True, prefix="btn")
        text_centered(x + w / 2, y + h / 2 - LABEL * 0.6, label, size=LABEL, color=WHITE)
    else:
        rect(x, y, w, h, stroke=accent, bg=WHITE, sw=2, rough=1, rounded=True, prefix="btn")
        text_centered(x + w / 2, y + h / 2 - LABEL * 0.6, label, size=LABEL, color=accent)


def tool_box(x, y, label, accent, abg, w=170, h=96):
    """A small generic 'a tool you use' tile."""
    rect(x, y, w, h, stroke=accent, bg=abg, sw=2, rough=1, rounded=True, prefix="tool")
    text_centered(x + w / 2, y + h / 2 - LABEL * 0.6, label, size=LABEL, color=INK)


# ============================================================================
# BEAT 1 - TITLE
# ============================================================================
ox = OX[1]
text(ox + 70, 300, "Claude", size=H1, color=VIOLET)
text(ox + 70, 300 + H1 * LINE_H, "Connectors", size=HERO, color=INK)
text(ox + 70, 300 + H1 * LINE_H + HERO * LINE_H, "& MCP", size=HERO, color=INK)
text(ox + 76, 300 + H1 * LINE_H + 2 * HERO * LINE_H + 30,
     "What they are, how they work, and\nhow the team uses them safely", size=H2, color=GREYD)
chip(ox + 76, 300 + H1 * LINE_H + 2 * HERO * LINE_H + 30 + 2 * H2 * LINE_H + 40,
     "Internal training - AI Ops Learn",
     fill=WHITE, text_color=GREY, border=GREY, size=SMALL)
mark("1. Title")

# ============================================================================
# BEAT 2 - CLAUDE ON ITS OWN  (the problem we're about to solve)
# ============================================================================
ox = beat_head(2, "Claude, straight out of the box")
# Claude in a closed box, top-left
bx, by, bw, bh = ox + 60, 250, 360, 380
rect(bx, by, bw, bh, stroke=GREYD, bg=WHITE, sw=2, rough=1, rounded=True, prefix="closed")
claude_face(bx + bw / 2, by + bh / 2, r=72, color=ORANGE)
text_centered(bx + bw / 2, by + bh - 70, "(on its own)", size=SMALL, color=GREY)
# three caption cards on the right of the box, stacked vertically
cards = [
    "It only knows what it learned up\nto a cut-off date.",
    "It cannot see your tools, files,\nor live data.",
    "So you end up copying and pasting\ncontext in by hand.",
]
cx, cy, cw, ch = bx + bw + 80, 250, 620, 110
for k, s in enumerate(cards):
    yy = cy + k * (ch + 28)
    rect(cx, yy, cw, ch, stroke=GREYD, bg=WHITE, sw=2, rough=1, rounded=True, prefix="cap")
    text(cx + 30, yy + 22, s, size=BODY, color=INK)
mark("2. Claude on its own")

# ============================================================================
# BEAT 3 - WHAT IS A CONNECTOR  (the bridge)
# ============================================================================
ox = beat_head(3, "A Connector is a secure bridge")
row_y = 350
# Claude
claude_face(ox + 150, row_y + 70, r=64, color=BLUE)
text_centered(ox + 150, row_y + 160, "Claude", size=LABEL, color=INK)
# Connector - the focal element (filled accent, the brief's "lime / look here")
nx, nw, nh = ox + 360, 360, 130
rect(nx, row_y, nw, nh, stroke=BLUE, bg=BLUE, sw=3, rough=1, rounded=True, prefix="conn")
text_centered(nx + nw / 2, row_y + nh / 2 - H3 * 0.6, "Connector", size=H3, color=WHITE)
# a tool you already use (a real connector, not an abstract box)
tx, tw, th = ox + 800, 300, 130
rect(tx, row_y, tw, th, stroke=GREEN, bg=GREEN_BG, sw=2, rough=1, rounded=True, prefix="usetool")
text_centered(tx + tw / 2, row_y + nh / 2 - LABEL * 0.6, "Slack / Granola /\nBeacon ...", size=LABEL, color=INK)
arrow(ox + 280, row_y + nh / 2, [[0, 0], [70, 0]], stroke=GREYD, sw=4)
arrow(nx + nw + 10, row_y + nh / 2, [[0, 0], [60, 0]], stroke=GREYD, sw=4)
# definition + caption
text(ox + 60, row_y + 230,
     "It lets Claude securely reach a specific tool to find things, fetch\n"
     "information, and - with your say-so - take an action.", size=H3, color=INK)
text(ox + 60, row_y + 230 + 2 * H3 * LINE_H + 30,
     "Think: a visitor pass to one room, with a key you can take back at any time.",
     size=SMALL, color=GREY)
mark("3. What is a Connector")

# ============================================================================
# BEAT 4 - WHAT IS MCP  (one universal plug)
# ============================================================================
ox = beat_head(4, "MCP - the standard that makes it possible",
                sub="Model Context Protocol. An open standard created by\n"
                    "Anthropic, now used widely across the industry.")
# TOP HALF: a messy tangle - a custom integration for every tool
lx = ox + 60
top_y = 270
text(lx, top_y, "Before: a custom integration for every tool", size=LABEL, color=GREYD)
claude_face(lx + 70, top_y + 130, r=44, color=GREEN)
tangle = [(lx + 320, top_y + 50, ORANGE, ORANGE_BG),
          (lx + 560, top_y + 110, VIOLET, VIOLET_BG),
          (lx + 800, top_y + 50, BLUE, BLUE_BG)]
for k, (ttx, tty, acc, abg) in enumerate(tangle):
    tool_box(ttx, tty, f"Tool {k + 1}", acc, abg, w=150, h=80)
    # each on its own crooked, differently-shaped wire
    line(lx + 110, top_y + 130, [[0, 0], [(ttx - (lx + 110)) * 0.5, -50 + k * 40],
         [ttx - (lx + 110), tty + 40 - (top_y + 130)]],
         stroke=acc, sw=3, rough=2, prefix="wire")
# BOTTOM HALF: one common port - several tools all plugging into one identical port
bot_y = 620
text(lx, bot_y, "With MCP: one common way to connect", size=LABEL, color=GREEN)
claude_face(lx + 70, bot_y + 150, r=44, color=GREEN)
# the single common port - the focal accent element
px, pw, ph = lx + 280, 150, 240
rect(px, bot_y + 50, pw, ph, stroke=GREEN, bg=GREEN, sw=3, rough=1, rounded=True, prefix="port")
text_centered(px + pw / 2, bot_y + 50 + ph / 2 - H2 * 0.6, "MCP", size=H2, color=WHITE)
arrow(lx + 120, bot_y + 150, [[0, 0], [150, 0]], stroke=GREEN, sw=3, rough=1)
rtools = ["Tool 1", "Tool 2", "Tool 3"]
for k, lab in enumerate(rtools):
    tty = bot_y + 60 + k * 80
    tool_box(px + pw + 130, tty, lab, GREYD, WHITE, w=150, h=64)
    arrow(px + pw + 120, tty + 32, [[0, 0], [-100, (bot_y + 50 + ph / 2) - (tty + 32)]],
          stroke=GREEN, sw=3, rough=1, head=None)
text(lx, bot_y + ph + 110,
     "Like a single standard socket for AI - over 9,000 connectable services already exist.",
     size=SMALL, color=GREY)
mark("4. What is MCP")

# ============================================================================
# BEAT 5 - HOW IT WORKS  (4-step pipeline, step 4 is the accent)
# ============================================================================
ox = beat_head(5, "How a Connector actually works")
steps = [
    "The tool runs a small 'server' that lists what\nClaude is allowed to do.",
    "Claude connects to it over a secure link.",
    "Claude discovers the available actions\n(for example: search, fetch, create).",
    "Before doing anything that changes data, Claude asks\nyour permission - then acts and brings back the result.",
]
nx, nw = ox + 130, 960
ny = 290
for k, s in enumerate(steps):
    h = 150 if "\n" in s else 120
    accent_step = (k == len(steps) - 1)
    if accent_step:
        rect(nx, ny, nw, h, stroke=TEAL, bg=TEAL, sw=3, rough=1, rounded=True, prefix="step")
        num_badge(nx - 70, ny + h / 2 - 22, k + 1, TEAL)
        text(nx + 30, ny + (h - text_h(s, BODY)) / 2, s, size=BODY, color=WHITE)
    else:
        rect(nx, ny, nw, h, stroke=TEAL, bg=TEAL_T, sw=2, rough=1, rounded=True, prefix="step")
        num_badge(nx - 70, ny + h / 2 - 22, k + 1, TEAL)
        text(nx + 30, ny + (h - text_h(s, BODY)) / 2, s, size=BODY, color=INK)
    if k < len(steps) - 1:
        arrow(nx + nw / 2, ny + h, [[0, 0], [0, 40]], stroke=TEAL, sw=4)
    ny += h + 40
mark("5. How it works")

# ============================================================================
# BEAT 6 - TWO TYPES  (directory vs custom)
# ============================================================================
ox = beat_head(6, "Two ways to add one")
pw, ph = 510, 480
ptop = 290
panels = [
    ("Directory connectors", ["Pre-checked by Anthropic", "Added in one click",
                              "Available on every plan"]),
    ("Custom connectors", ["You point Claude at a tool's own\nsecure address",
                          "For tools not in the directory,\nincluding internal ones",
                          "On paid plans"]),
]
for k, (title, bullets) in enumerate(panels):
    px = ox + 60 + k * (pw + 40)
    rect(px, ptop, pw, ph, stroke=INDIGO, bg=WHITE, sw=2, rough=1, rounded=True, prefix="panel")
    rect(px, ptop, pw, 70, stroke="transparent", bg=INDIGO_BG, sw=1, rough=1, rounded=True, prefix="phead")
    text(px + 30, ptop + 20, title, size=H3, color=INDIGO)
    yy = ptop + 120
    for b in bullets:
        text(px + 40, yy, "- " + b, size=BODY, color=INK)
        yy += 70 + (40 if "\n" in b else 0)
# slim caption strip beneath both
sy = ptop + ph + 40
highlighter(ox + 60, sy, 2 * pw + 40, 70, INDIGO_T, angle=0.0)
text(ox + 84, sy + 20,
     "Some are 'interactive' - they show cards, tables or\nforms right inside the chat, instead of plain text.",
     size=SMALL, color=INK)
mark("6. Two types")

# ============================================================================
# BEAT 7 - WHAT YOU'LL SEE  (settings mock + permission dialog)
# ============================================================================
ox = beat_head(7, "What it looks like on screen")
# settings panel mock - on top, full width
sx, sy, sw_, sh = ox + 60, 250, 1060, 360
rect(sx, sy, sw_, sh, stroke=VIOLET, bg=WHITE, sw=2, rough=1, rounded=True, prefix="settings")
text(sx + 30, sy + 24, "Connectors", size=H3, color=VIOLET)
button(sx + sw_ - 280, sy + 22, "+ Add connector", VIOLET, w=250, h=56)
ry = sy + 110
for k in range(2):
    rect(sx + 30, ry, sw_ - 60, 80, stroke=GREYD, bg=WHITE, sw=2, rough=1, rounded=True, prefix="srow")
    text(sx + 56, ry + 26, f"Example tool {k + 1}", size=BODY, color=INK)
    button(sx + sw_ - 200, ry + 12, "Connect", VIOLET, w=140, h=56, filled=False)
    ry += 104
# permission dialog mock - below, on the left
dx, dy, dw, dh = ox + 60, sy + sh + 50, 640, 320
rect(dx, dy, dw, dh, stroke=VIOLET, bg=VIOLET_T, sw=2, rough=1, rounded=True, prefix="dialog")
text(dx + 36, dy + 36, "Claude wants to read your files", size=H3, color=INK)
text(dx + 36, dy + 110, "Allow Claude to access this tool?", size=BODY, color=GREYD)
button(dx + 36, dy + dh - 100, "Allow", VIOLET, w=250, h=64)
button(dx + 36 + 280, dy + dh - 100, "Don't allow", GREYD, w=250, h=64, filled=False)
# caption to the right of the dialog; desktop-app demo cue below
text(dx + dw + 60, dy + 40,
     "You stay in control -\naccess is asked for, and\ncan be switched off\nwhenever you like.",
     size=BODY, color=GREY)
demo_badge(dx, dy + dh + 6, "show in Claude desktop app:  turn on a connector")
mark("7. What you'll see")

# ============================================================================
# BEAT 8 - USING IT SAFELY  (the ONLY beat that uses red / caution)
# ============================================================================
ox = beat_head(8, "Using Connectors safely")
diamond(ox + 60, 230, 56, 56, stroke=RED, bg=RED_BG, sw=3)
text_centered(ox + 88, 242, "!", size=H2, color=RED)
highlighter(ox + 140, 236, 980, 80, RED_BG, angle=0.0)
text(ox + 164, 250, "Connectors reach your real tools and\ndata - treat them with care.",
     size=H3, color=INK)
rules = [
    "Least access: connect only what\nthe task needs.",
    "Read-only where possible; approve\neach action that changes things.",
    "Read the permission prompts - do\nnot click through on autopilot.",
    "Be wary of hidden instructions\nburied in fetched content or data.",
    "On managed plans, an admin enables\nconnectors before anyone can use them.",
    "Handle personal and sensitive info\nin line with your data policy.",
]
cw, chh = 510, 150
gx, gy = ox + 60, 380
for k, s in enumerate(rules):
    cxk = gx + (k % 2) * (cw + 40)
    cyk = gy + (k // 2) * (chh + 30)
    sticky(cxk, cyk, cw, chh, RED_T, angle=jit(1.2))
    text(cxk + 30, cyk + 30, s, size=BODY, color=INK)
mark("8. Using it safely")

# ============================================================================
# BEAT 9 - GOOD HABITS  (vertical checklist, green ticks)
# ============================================================================
ox = beat_head(9, "What good looks like")
habits = [
    "Connect only the tools you actually need.",
    "Before allowing, check what a connector can do.",
    "Pause on every permission prompt and read it.",
    "If something looks off, stop and report it.",
    "Disconnect access you no longer use.",
]
py = 290
for s in habits:
    check_item(ox + 60, py, s, color=INK, accent=GREEN, size=H3)
    py += 150
mark("9. Good habits")

# ============================================================================
# BEAT 10 - RECAP & CLOSE
# ============================================================================
ox = beat_head(10, "In a nutshell")
takeaways = [
    "A Connector is a secure bridge from Claude to a tool you use.",
    "MCP is the common standard that makes those bridges possible.",
    "You stay in control - permission first, access revocable.",
]
cw, ch = WID[10] - 160, 110
cy = 300
for k, s in enumerate(takeaways):
    yy = cy + k * (ch + 40)
    rect(ox + 60, yy, cw, ch, stroke=ORANGE, bg=WHITE, sw=2, rough=1, rounded=True, prefix="recap")
    text(ox + 30 + 60, yy + 34, s, size=BODY, color=INK)
band_y = cy + 3 * (ch + 40) + 30
rect(ox + 60, band_y, cw, 110, stroke=ORANGE, bg=ORANGE, sw=2, rough=1, rounded=True, prefix="cta")
text_centered(ox + 60 + cw / 2, band_y + 34, "Questions? [owner / channel placeholder]", size=H3, color=WHITE)
mark("10. Recap & close")

# ----------------------------------------------------------------------------
# WRITE + VALIDATE  (shared excalidraw_kit; hard-fails on frames / off-palette)
# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "connectors-mcp-training.excalidraw")
MAXW = max(WID.values()) + 200
finish(out, MAXW, TOTAL_W)

print("\nbeats (the Style-B analogue of frames) and their element counts:")
for label, count, _total in BEATS:
    print(f"  {label:<28} {count:>4} elements")
print(f"  {'TOTAL':<28} {len(E):>4} elements")
