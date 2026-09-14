#!/usr/bin/env python3
"""Build claude-chrome.excalidraw - ONE flowing, illustrated explainer for the
"Claude in Chrome" (the browser extension) training video (Phlo AI Ops Learn,
module 2.10).

House Style B (see excalidraw_kit): one hand-drawn left-to-right journey, no
frames, white canvas, the hand font, lively palette. Composition + a one-off
browser illustration live here.

Unlike the file-type videos (2.8-2.9, plus PowerPoint - now Day 12), this is
an AGENTIC tool: Claude in Chrome
navigates, clicks and fills forms in your browser, with your logins and context,
across tabs - and can record/repeat and schedule browser tasks. So the shape is
different: no "build a real file" beat; instead the PERMISSION MODEL and the
prompt-injection risk are front and centre (beats 4 and 8), because it acts on
your behalf. Beta, all paid plans, Chrome.

Run:  python3 videos/claude/10-claude-web-extension/build_web_extension.py
      python3 preview.py videos/claude/10-claude-web-extension/claude-chrome.excalidraw out.png
"""
import os
import sys

_d = os.path.dirname(os.path.abspath(__file__))
while _d != os.path.dirname(_d) and not os.path.exists(os.path.join(_d, "excalidraw_kit.py")):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)

import random
from excalidraw_kit import *

random.seed(101010)

N = 9
GAP = 800
WID = {i: 1200 for i in range(1, N + 1)}
ACCENT = {1: VIOLET, 2: BLUE, 3: ORANGE, 4: GREEN, 5: TEAL,
          6: INDIGO, 7: YELLOW, 8: RED, 9: VIOLET}
OX = {}
_c = 0
for _i in range(1, N + 1):
    OX[_i] = _c
    _c += WID[_i] + GAP
TOTAL_W = _c
HEAD_Y = 60


def beat_head(i, title, sub=None):
    ox = OX[i]
    heading(ox, HEAD_Y, title, color=ACCENT[i], sub=sub)
    return ox


# ----------------------------------------------------------------------------
# LOCAL ONE-OFF ILLUSTRATIONS
# ----------------------------------------------------------------------------
def browser(x, y, w, h, accent=VIOLET, abg=VIOLET_BG, panel=True, tabs=3, table=False,
            content=True):
    """A browser window: chrome bar with traffic dots + tabs + URL bar, a page
    area, and an optional Claude side panel. content=False leaves the page blank
    so the caller can place its own labelled page elements."""
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="brz")
    rect(x, y, w, 46, stroke="transparent", bg=FAINT, sw=1, rough=1, rounded=True, prefix="brzbar")
    for k in range(3):
        ellipse(x + 16 + k * 16, y + 16, 10, 10, stroke=GREY, bg=GREY, sw=1)
    for k in range(tabs):
        rect(x + 70 + k * 92, y + 10, 82, 28, stroke=GREY,
             bg=(WHITE if k == 0 else FAINT), sw=1, rough=1, rounded=True, prefix="tab")
    rect(x + 16, y + 54, w - 32, 26, stroke=FAINT, bg=WHITE, sw=1, rough=1, rounded=True, prefix="url")
    page_r = (x + w * 0.62) if panel else (x + w - 24)
    cx, cy = x + 24, y + 104
    if not content:
        pass
    elif table:
        tw = page_r - cx - 20
        rect(cx, cy, tw, 24, stroke="transparent", bg=abg, sw=1, rough=1, rounded=False, prefix="trh")
        rows = int((h - (cy - y) - 30) / 34)
        for r in range(rows):
            line(cx, cy + 24 + r * 30, [[0, 0], [tw, 0]], stroke=FAINT, sw=1)
        for c in range(1, 4):
            line(cx + c * tw / 4, cy, [[0, 0], [0, 24 + rows * 30]], stroke=FAINT, sw=1)
    else:
        for k in range(5):
            line(cx, cy + k * 34, [[0, 0], [page_r - cx - 30, 0]], stroke=GREY, sw=2)
    if panel:
        px = x + w * 0.64
        pw = x + w - 16 - px
        rect(px, y + 92, pw, h - 92 - 16, stroke=accent, bg=abg, sw=2, rough=1,
             rounded=True, fill="solid", opacity=45, prefix="brzpanel")
        rect(px, y + 92, 8, h - 92 - 16, stroke=accent, bg=accent, sw=1, rough=1,
             rounded=False, prefix="brzedge")
        text(px + 24, y + 104, "Claude", size=SMALL, color=accent)


def cursor(x, y, color=ORANGE):
    line(x, y, [[0, 0], [0, 28], [8, 20], [13, 32], [18, 30], [12, 18], [22, 18], [0, 0]],
         stroke=color, sw=2, rough=1, bg=color, fill="solid", prefix="cur")


def shield(x, y, w, h, color=RED, bg=RED_BG):
    pts = [[w / 2, 0], [w, h * 0.2], [w, h * 0.55], [w / 2, h], [0, h * 0.55], [0, h * 0.2], [w / 2, 0]]
    line(x, y, pts, stroke=color, sw=3, rough=1, bg=bg, fill="solid", prefix="shield")


# ============================================================================
# BOARD TITLE
# ============================================================================
text(OX[1], -300, "Claude in Chrome", size=HERO, color=INK)
text(OX[1] + 6, -300 + HERO * LINE_H + 4,
     "Claude that can actually use your browser", size=H2, color=VIOLET)

# ============================================================================
# BEAT 1 - HOOK
# ============================================================================
ox = beat_head(1, "Claude, inside your browser",
               "not a separate tab you copy things into - a helper\nthat works the sites you already use")
browser(ox + 60, 360, 720, 440, accent=VIOLET, abg=VIOLET_BG, panel=True)
text(ox + 90, 824, "it lives beside the page", size=SMALL, color=GREY)
text(ox + 820, 470, "ask a question -\nor ask it to do\nsomething", size=H3, color=VIOLET)
arrow(ox + 810, 540, [[0, 0], [-40, 0]], stroke=VIOLET, sw=4)

# ============================================================================
# BEAT 2 - IT SEES THE PAGE LIKE YOU DO
# ============================================================================
ox = beat_head(2, "It sees the page like you do",
               "Buttons, forms, menus, content - Claude reads the\npage the same way you read it, then works with it.")
browser(ox + 60, 340, 760, 460, accent=BLUE, abg=BLUE_BG, panel=True, content=False)
# label the PAGE (left ~60%), not the Claude panel - Claude reads the page itself.
# Real page elements sit on the page; short arrows point at them.
rect(ox + 100, 440, 310, 90, stroke=GREYD, bg=BLUE_BG, sw=2, rough=1, rounded=True)   # content block
text(ox + 440, 470, "content", size=BODY, color=BLUE)
arrow(ox + 436, 486, [[0, 0], [-30, 0]], stroke=BLUE, sw=3)
rect(ox + 100, 558, 310, 40, stroke=GREYD, bg=WHITE, sw=2, rough=1, rounded=True)      # form field
text(ox + 440, 566, "forms", size=BODY, color=BLUE)
arrow(ox + 436, 582, [[0, 0], [-30, 0]], stroke=BLUE, sw=3)
rect(ox + 100, 626, 150, 46, stroke=BLUE, bg=BLUE_BG, sw=2, rough=1, rounded=True)     # button
text(ox + 128, 636, "Sign up", size=SMALL, color=BLUE)
text(ox + 440, 636, "buttons", size=BODY, color=BLUE)
arrow(ox + 436, 652, [[0, 0], [-184, 0]], stroke=BLUE, sw=3)
chx = ox + 60
for lab in ["beta", "all paid plans", "Chrome browser"]:
    w, _ = chip(chx, 856, lab, fill=WHITE, text_color=BLUE, border=BLUE, size=SMALL)
    chx += w + 28

# ============================================================================
# BEAT 3 - IT CAN ACT, NOT JUST READ
# ============================================================================
ox = beat_head(3, "It can act, not just read",
               "It clicks, types and fills forms for you - and keeps\ngoing across every tab in the group.")
browser(ox + 60, 340, 700, 420, accent=ORANGE, abg=ORANGE_BG, panel=True)
# a click on a button
rect(ox + 220, 520, 120, 40, stroke=ORANGE, bg=ORANGE_BG, sw=2, rough=1, rounded=True)
text(ox + 240, 528, "Submit", size=SMALL, color=ORANGE)
cursor(ox + 330, 548, color=ORANGE)
acts = ["navigate and click", "fill in forms", "work across your open tabs",
        "carry on when you switch tabs"]
for k, a in enumerate(acts):
    chip(ox + 800, 360 + k * 90, a, fill=WHITE, text_color=ORANGE, border=ORANGE, size=SMALL)

# ============================================================================
# BEAT 4 - YOU'RE IN CONTROL  (permissions - signature)
# ============================================================================
ox = beat_head(4, "It works with your permission",
               "It uses your logins and your context - so it only\ngoes where you let it, and you approve what it does.")
# a layered permission stack
stack = [("you grant access, site by site", GREEN, GREEN_BG),
         ("you approve actions before they run", BLUE, BLUE_BG),
         ("you can stop or take over any time", VIOLET, VIOLET_BG)]
for k, (lab, acc, abg) in enumerate(stack):
    yy = 340 + k * 130
    rect(ox + 60, yy, 760, 100, stroke=acc, bg=abg, sw=2, rough=1, rounded=True,
         fill="solid", opacity=40, angle=jit(0.8))
    ellipse(ox + 86, yy + 28, 44, 44, stroke=acc, bg=WHITE, sw=3)
    text_centered(ox + 108, yy + 36, str(k + 1), size=H3, color=acc)
    text(ox + 156, yy + 30, lab, size=H3, color=INK)
text(ox + 60, 750, "a multi-layered permission system - control, not blind trust", size=BODY, color=GREYD)

# ============================================================================
# BEAT 5 - TEACH IT, SCHEDULE IT
# ============================================================================
ox = beat_head(5, "Teach it once, then schedule it",
               "Record a workflow and Claude repeats it - on demand,\nor on a schedule you set.")
half = 510
lx, ly = ox + 40, 340
sticky(lx, ly, half, 440, TEAL_BG, angle=jit(-1.0))
text(lx + 36, ly + 28, "Record a workflow", size=H3, color=TEAL)
text(lx + 36, ly + 86, "Do it once with Claude watching;\nit learns the steps to repeat.", size=BODY, color=INK)
for k, lab in enumerate(["1 - open the report", "2 - copy the figures", "3 - paste into the tracker"]):
    chip(lx + 40, ly + 180 + k * 78, lab, fill=WHITE, text_color=TEAL, border=TEAL, size=SMALL)
rx = ox + 40 + half + 60
sticky(rx, ly, half, 440, INDIGO_BG, angle=jit(1.0))
text(rx + 36, ly + 28, "Set it on a schedule", size=H3, color=INDIGO)
text(rx + 36, ly + 86, "Recurring browser tasks run on\ntheir own - daily, weekly, monthly.", size=BODY, color=INK)
clock(rx + 130, ly + 290, 70, INDIGO)
text(rx + 230, ly + 270, "“every Monday,\n9am”", size=BODY, color=INDIGO)

# ============================================================================
# BEAT 6 - STEER / EXAMPLES
# ============================================================================
ox = beat_head(6, "What you'd actually ask it",
               "Plain English - it works out the clicks.")
asks = ["pull these rows into a summary",
        "fill this form from my notes",
        "find this part across the three open tabs",
        "summarise this long page in five bullets"]
for k, a in enumerate(asks):
    chip(ox + 60, 350 + k * 96, a, fill=WHITE, text_color=INDIGO, border=INDIGO, size=BODY)
demo_badge(ox + 60, 350 + len(asks) * 96 + 6,
           "show in Chrome:  summarise a long page, then pull a table into a list")

# ============================================================================
# BEAT 7 - WHERE IT EARNS ITS KEEP  (a grid - the everyday browser chores)
# ============================================================================
ox = beat_head(7, "Everyday browser drudgery")
jobs = [("Pull data off a page", "rows from a dashboard into a list", ORANGE, ORANGE_BG),
        ("Fill repetitive forms", "the same fields, again and again", GREEN, GREEN_BG),
        ("Read a long page fast", "summarise an article or a PDF", BLUE, BLUE_BG),
        ("Gather across tabs", "one answer from several pages", VIOLET, VIOLET_BG)]
gx2, gy = ox + 40, 320
cw2, ch2 = 520, 150
for k, (head, cap, acc, abg) in enumerate(jobs):
    bx = gx2 + (k % 2) * (cw2 + 40)
    byy = gy + (k // 2) * (ch2 + 40)
    sticky(bx, byy, cw2, ch2, abg, angle=jit(1.2))
    text(bx + 32, byy + 24, head, size=H3, color=acc)
    text(bx + 32, byy + 84, cap, size=BODY, color=INK)

# ============================================================================
# BEAT 8 - SAFETY  (a shield + a 'never point it at' list, not a caution box)
# ============================================================================
ox = beat_head(8, "Powerful - so keep it on a short lead")
shield(ox + 90, 340, 220, 260, color=RED, bg=RED_BG)
text_centered(ox + 200, 430, "!", size=HERO, color=RED)
text(ox + 70, 624, "it's beta, and it acts on your behalf", size=SMALL, color=GREYD)
# prompt-injection callout
rect(ox + 380, 340, 700, 150, stroke=RED, bg=RED_T, sw=2, rough=1, rounded=True)
text(ox + 412, 362, "Watch for prompt injection", size=H3, color=RED)
text(ox + 412, 416, "a web page can hide instructions that try to hijack\nClaude - grant the least access that works", size=BODY, color=INK)
# never point it at
rect(ox + 380, 520, 700, 230, stroke=GREYD, bg=FAINT, sw=2, rough=1, rounded=True)
text(ox + 412, 542, "Never point it at", size=H3, color=GREYD)
for k, it in enumerate(["patient systems", "banking or payments", "anything regulated"]):
    yy = 606 + k * 46
    xmark(ox + 414, yy, color=RED, s=18)
    text(ox + 448, yy - 4, it, size=BODY, color=INK)

# ============================================================================
# BEAT 9 - TRY / CLOSE  (a browser with a green read-only badge, no pause band)
# ============================================================================
ox = beat_head(9, "Start with something it can't break")
browser(ox + 60, 340, 560, 320, accent=VIOLET, abg=VIOLET_BG, panel=True, content=False)
rect(ox + 110, 446, 230, 60, stroke=GREEN, bg=GREEN_BG, sw=2, rough=1, rounded=True)
text(ox + 134, 462, "read-only - safe", size=BODY, color=GREEN)
ex_x = ox + 60
for lab in ["summarise this page", "pull a table into a list", "compare two open tabs"]:
    w, h = chip(ex_x, 700, lab, fill=WHITE, text_color=VIOLET, border=VIOLET, size=SMALL)
    ex_x += w + 30
text(ox + 60, 772, "watch what it does - then decide what you'd trust it to click", size=BODY, color=GREYD)
text(ox + 40, 832, "Claude can use the browser for you - you decide what it's allowed to touch.",
     size=H3, color=INK)
text(ox + 60, 904, "Docs: Claude - Get started with Claude in Chrome, and Using Claude in Chrome safely",
     size=SMALL, color=VIOLET)

# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "claude-chrome.excalidraw")
finish(out, max(WID.values()) + 200, TOTAL_W)
