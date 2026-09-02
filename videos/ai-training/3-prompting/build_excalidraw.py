#!/usr/bin/env python3
"""Build prompting-crispe-framework.excalidraw - ONE flowing, illustrated
explainer for Day 3 - Prompting & CRISPE Framework (the AI Training series).

House Style B (see excalidraw_kit): one hand-drawn left-to-right journey, NO
frames, white canvas, the hand font (fontFamily 1), roughness 1, a lively
palette colour-coded per beat. Composition + the one-off illustrations (crumpled
note, dial, quill, phone, microphone, monitor) live here; the look lives in the
kit.

THIRTEEN BEATS, each in its own 1200-wide slot with GAP = 800 of whitespace
between them. Style B has no frames - a literal Excalidraw frame is a hard
Style-B guard failure - so the beat slots ARE the "frames": you pan to one at a
time and the whitespace keeps its neighbours off-screen.

   1 orange  vague in, vague out - the one-liner on a crumpled note
   2 green   the same ask rebuilt as three sticky notes  [demo]
   3 violet  CRISPE as six dials, 3 x 2
   4 blue    fault-finder - symptom -> the dial that fixes it
   5 indigo  tell it why - the reason travels further than the rule
   6 green   three examples beat a paragraph
   7 red     say what to do, not what not to do
   8 blue    paste first, ask last - and ask for the quotes
   9 teal    set once, never repeat - Styles + preferences  [demo]
  10 indigo  it remembers you now - memory, chat search, project memory
  11 red     you stay in charge of it - the controls, and the rule  [demo]
  12 violet  different models, different habits
  13 yellow  capture by voice, shape at your desk

Beats 5-8 and 10 come from Anthropic's "Prompting best practices" page
(platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
and its per-model sub-pages. Only the parts that change what a person TYPES are
on the board: the API-only material (effort, adaptive thinking, budget_tokens,
prefill migration, computer-use toolsets, code-review harnesses, subagent caps)
is deliberately left off, because this audience uses the Claude app, not the API.
Beat 12's model habits date faster than anything else here - the beat says so on
the board.

Beats 10-11 come from Anthropic's support article on chat search and memory
(support.claude.com/en/articles/11817273). They deliberately go past what video
1.1 (claude-intro) already signposts - chat search, per-Project memory spaces,
Topics, pause vs reset, incognito - and they run power-then-control, because on
a regulated pharmacy's Team plan the control half is the half that matters. Note
what beat 10 does NOT say: memory is off by default on Team and Enterprise
plans (an owner switches it on), so the board tells people why they might not
see it rather than promising it is already there.

Recording: there is no animation any more, the camera IS the reveal. Pan
left-to-right, one beat per frame, ~3s of narration each; cut away to the Claude
desktop app on the two demo badges and come back to the same beat.

Run:  python3 videos/ai-training/3-prompting/build_excalidraw.py
      python3 preview.py videos/ai-training/3-prompting/prompting-crispe-framework.excalidraw out.png
"""
import os
import sys

_d = os.path.dirname(os.path.abspath(__file__))
while _d != os.path.dirname(_d) and not os.path.exists(os.path.join(_d, "excalidraw_kit.py")):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)

import math
import random
from excalidraw_kit import *

random.seed(30330)  # deterministic - re-runs produce identical files

# ----------------------------------------------------------------------------
# BEAT SCAFFOLD
# ----------------------------------------------------------------------------
N = 13
GAP = 800
WID = {i: 1200 for i in range(1, N + 1)}
ACCENT = {1: ORANGE, 2: GREEN, 3: VIOLET, 4: BLUE, 5: INDIGO, 6: GREEN,
          7: RED, 8: BLUE, 9: TEAL, 10: INDIGO, 11: RED, 12: VIOLET,
          13: YELLOW}
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
def crumpled_note(x, y, w, h, accent, abg):
    """A screwed-up, smoothed-out note: ragged outline, a folded corner, and a
    couple of short creases low down (kept clear of the text on the note)."""
    pts = [[0, 22], [w * 0.17, 2], [w * 0.52, 14], [w * 0.80, 0], [w, 26],
           [w - 12, h * 0.50], [w, h - 18], [w * 0.68, h], [w * 0.40, h - 14],
           [w * 0.14, h - 2], [2, h - 28], [12, h * 0.52], [0, 22]]
    line(x, y, pts, stroke=INK, sw=2, rough=1, bg=abg, fill="solid", prefix="crumple")
    line(x + w - 78, y + 18, [[0, 0], [62, 10], [10, 50], [0, 0]],
         stroke=accent, sw=2, rough=1, prefix="fold")
    line(x + w * 0.08, y + h - 28,
         [[0, 0], [w * 0.11, -h * 0.09], [w * 0.24, -h * 0.02], [w * 0.34, -h * 0.11]],
         stroke=accent, sw=2, rough=1, prefix="crease")
    line(x + w * 0.54, y + h - 24,
         [[0, 0], [w * 0.10, -h * 0.10], [w * 0.22, -h * 0.01], [w * 0.32, -h * 0.10]],
         stroke=accent, sw=2, rough=1, prefix="crease")


def dial(cx, cy, frac, color, abg, r=34):
    """A sketched dial: face, three ticks over the top, needle set to `frac`
    (0 = swung low / left, 1 = swung high / right)."""
    ellipse(cx - r, cy - r, 2 * r, 2 * r, stroke=color, bg=abg, sw=3, rough=1, prefix="dial")
    for t in (0.0, 0.5, 1.0):
        th = math.radians(215 - t * 250)
        dx, dy = math.cos(th), -math.sin(th)
        line(cx + dx * (r + 6), cy + dy * (r + 6),
             [[0, 0], [dx * r * 0.28, dy * r * 0.28]], stroke=color, sw=2, prefix="tick")
    th = math.radians(215 - frac * 250)
    line(cx, cy, [[0, 0], [math.cos(th) * r * 0.74, -math.sin(th) * r * 0.74]],
         stroke=INK, sw=3, prefix="needle")
    ellipse(cx - r * 0.12, cy - r * 0.12, r * 0.24, r * 0.24, stroke=INK, bg=INK, sw=2, prefix="hub")


def quill(cx, cy, s, color, abg):
    """A feather pen: leaf-shaped vane, a shaft through it, barbs and an ink nib."""
    line(cx - s * 0.16, cy + s * 0.24,
         [[0, 0], [-s * 0.10, -s * 0.32], [s * 0.06, -s * 0.62], [s * 0.36, -s * 0.88],
          [s * 0.42, -s * 0.60], [s * 0.30, -s * 0.28], [0, 0]],
         stroke=color, sw=3, rough=1, bg=abg, fill="solid", prefix="vane")
    line(cx - s * 0.30, cy + s * 0.44, [[0, 0], [s * 0.64, -s * 0.90]],
         stroke=color, sw=3, rough=1, prefix="shaft")
    for k in range(3):
        bx = cx - s * 0.10 + k * s * 0.14
        by = cy + s * 0.10 - k * s * 0.20
        line(bx, by, [[0, 0], [-s * 0.12, -s * 0.05]], stroke=color, sw=2, prefix="barb")
    line(cx - s * 0.30, cy + s * 0.44,
         [[0, 0], [s * 0.11, -s * 0.05], [s * 0.06, -s * 0.15]], stroke=INK, sw=3, prefix="nib")


def person_big(cx, cy, color, abg, s=1.5):
    """An avatar silhouette: a head plus rounded shoulders. The kit's person() is
    sized for a crowd of tiny figures; this one has to hold its own next to the
    quill, so it lives here rather than in the kit."""
    r = 28 * s
    ellipse(cx - r, cy - 68 * s, 2 * r, 2 * r, stroke=color, bg=WHITE, sw=3,
            rough=1, prefix="head")
    line(cx - 56 * s, cy + 52 * s,
         [[0, 0], [0, -26 * s], [20 * s, -58 * s], [92 * s, -58 * s],
          [112 * s, -26 * s], [112 * s, 0]],
         stroke=color, sw=3, rough=1, bg=abg, fill="solid", prefix="shoulders")


def notebook(x, y, w=104, h=124, accent=INDIGO, abg=INDIGO_T):
    """A little notebook: cover, spine rings, and written lines."""
    rect(x, y, w, h, stroke=INK, bg=abg, sw=2, rough=1, rounded=True, prefix="nb")
    line(x + 22, y, [[0, 0], [0, h]], stroke=accent, sw=2, prefix="nbspine")
    for k in range(3):
        ellipse(x + 15, y + 22 + k * 34, 14, 14, stroke=accent, bg=WHITE, sw=2, prefix="nbring")
    for k in range(4):
        line(x + 38, y + 28 + k * 24, [[0, 0], [(w - 62 if k % 2 else w - 78), 0]],
             stroke=GREY, sw=2, prefix="nbline")


def magnifier(cx, cy, r=34, color=INDIGO):
    """A search magnifier."""
    ellipse(cx - r, cy - r, 2 * r, 2 * r, stroke=color, bg=WHITE, sw=3, rough=1, prefix="mag")
    line(cx + r * 0.72, cy + r * 0.72, [[0, 0], [r * 0.86, r * 0.86]], stroke=color, sw=4, prefix="maghandle")


def ghost(cx, cy, w=76, h=92, color=GREYD):
    """The incognito ghost: a domed head, straight sides, a wavy hem, two eyes.
    (cx, cy) is the centre of the body, so the eyes sit inside it."""
    x0, y0 = cx - w / 2, cy - h / 2
    pts = [[0, h * 0.95], [0, h * 0.42], [w * 0.06, h * 0.20], [w * 0.28, h * 0.02],
           [w * 0.72, h * 0.02], [w * 0.94, h * 0.20], [w, h * 0.42], [w, h * 0.95],
           [w * 0.80, h * 0.78], [w * 0.60, h * 0.95], [w * 0.40, h * 0.78],
           [w * 0.20, h * 0.95], [0, h * 0.95]]
    line(x0, y0, pts, stroke=color, sw=3, rough=1, bg=WHITE, fill="solid", prefix="ghost")
    for dx in (-w * 0.22, w * 0.08):
        ellipse(cx + dx, cy - h * 0.16, 11, 11, stroke=color, bg=color, sw=2, prefix="geye")


def folder_tab(x, y, w=96, h=72, accent=INDIGO, abg=INDIGO_T):
    rect(x, y + 14, w, h, stroke=INK, bg=abg, sw=2, rough=1, rounded=True, prefix="fold")
    rect(x, y, w * 0.5, 22, stroke=INK, bg=abg, sw=2, rough=1, rounded=True, prefix="foldtab")


def phone(x, y, w, h, abg):
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=3, rough=1, rounded=True, prefix="phone")
    rect(x + 14, y + 34, w - 28, h - 72, stroke=GREY, bg=abg, sw=1, rough=1,
         rounded=True, fill="solid", opacity=30, prefix="phonescr")
    line(x + w / 2 - 30, y + 18, [[0, 0], [60, 0]], stroke=GREY, sw=3, prefix="earp")
    rect(x + w / 2 - 40, y + h - 26, 80, 8, stroke=GREY, bg=GREY, sw=1, rough=1,
         rounded=True, prefix="homebar")


def mic_icon(cx, cy, s, color):
    """A sketched microphone: capsule, cradle, stand and base."""
    rect(cx - s * 0.28, cy - s * 0.6, s * 0.56, s * 0.8, stroke=color, bg=WHITE,
         sw=3, rough=1, rounded=True, prefix="mic")
    line(cx - s * 0.5, cy + s * 0.06,
         [[0, 0], [0, s * 0.16], [s * 0.22, s * 0.34], [s * 0.78, s * 0.34],
          [s, s * 0.16], [s, 0]], stroke=color, sw=3, prefix="cradle")
    line(cx, cy + s * 0.44, [[0, 0], [0, s * 0.3]], stroke=color, sw=3, prefix="stand")
    line(cx - s * 0.3, cy + s * 0.76, [[0, 0], [s * 0.6, 0]], stroke=color, sw=3, prefix="base")


def squiggle(x, y, w, color, amp=18, waves=4.0, sw=3):
    """A hand-drawn voice squiggle."""
    steps = 44
    pts = [[t / steps * w, math.sin(t / steps * math.pi * waves) * amp] for t in range(steps + 1)]
    line(x, y, pts, stroke=color, sw=sw, rough=1, prefix="squig")


def monitor(x, y, w, h, abg):
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=3, rough=1, rounded=True, prefix="mon")
    rect(x + 12, y + 12, w - 24, h - 24, stroke=GREY, bg=abg, sw=1, rough=1,
         rounded=True, fill="solid", opacity=30, prefix="monscr")
    rect(x + w / 2 - 34, y + h, 68, 22, stroke=INK, bg=WHITE, sw=2, rough=1,
         rounded=False, prefix="monstand")
    rect(x + w / 2 - 84, y + h + 22, 168, 12, stroke=INK, bg=WHITE, sw=2, rough=1,
         rounded=True, prefix="monbase")


# ============================================================================
# BOARD TITLE
# ============================================================================
text(OX[1], -300, "Prompting", size=HERO, color=INK)
text(OX[1] + 6, -300 + HERO * LINE_H + 4, "and CRISPE, the framework for telling what's missing",
     size=H2, color=VIOLET)

# ============================================================================
# BEAT 1 - VAGUE IN, VAGUE OUT  (orange)
# ============================================================================
ox = beat_head(1, "Vague in, vague out",
               "One line, no context. Claude has to guess -\nand it guesses generically.")
crumpled_note(ox + 40, 300, 620, 230, ORANGE, ORANGE_T)
text(ox + 110, 366, "Can you help with this\ncustomer reply?", size=BODY, color=INK)
text(ox + 730, 320, "?", size=HERO, color=ORANGE)
text(ox + 40, 578, "Nothing here says who it's for, what \"help\" means,\nor what a good answer looks like.",
     size=BODY, color=GREYD)
text(ox + 40, 682, "So Claude fills the gaps itself - and you get a\ngeneric answer you have to rewrite anyway.",
     size=SMALL, color=ORANGE)

# ============================================================================
# BEAT 2 - THE SAME ASK, REBUILT  (green)
# ============================================================================
ox = beat_head(2, "The same ask, rebuilt",
               "Three sticky notes is usually enough.")
NOTES = [
    ("context",      "Our Support team answers refund requests all day."),
    ("the real ask", "Rewrite this reply so it's warm but firm,\nand under 120 words."),
    ("one example",  "Here's one that reads well: \"Thanks for\nflagging this...\""),
]
for k, (lab, body) in enumerate(NOTES):
    ny = 290 + k * 180
    sticky(ox + 40, ny, 760, 160, GREEN_BG, angle=jit(1.5))
    text(ox + 84, ny + 20, lab, size=H3, color=GREEN)
    text(ox + 84, ny + 72, body, size=BODY, color=INK)
highlighter(ox + 40, 842, 350, 46, GREEN_BG, angle=0.0)
text(ox + 56, 852, "the minimum viable prompt", size=BODY, color=GREEN)
demo_badge(ox + 40, 906, "show in Claude desktop app:  fix the prompt live")

# ============================================================================
# BEAT 3 - CRISPE  (violet)
# ============================================================================
ox = beat_head(3, "CRISPE", "Six dials, not six boxes to fill in.")
DIALS = [
    ("Context",      "what's going on",      0.80),
    ("Role",         "who Claude is",        0.35),
    ("Instructions", "what to do",           0.90),
    ("Style",        "how it should read",   0.50),
    ("Parameters",   "length, format, limits", 0.25),
    ("Example",      "one that looks right", 0.70),
]
for k, (lab, gloss, frac) in enumerate(DIALS):
    cx = ox + 230 + (k % 3) * 370
    cy = 420 + (k // 3) * 280
    dial(cx, cy, frac, VIOLET, VIOLET_T, r=48)
    text_centered(cx, cy + 64, lab, size=BODY, color=VIOLET, angle=jit(1.4))
    text_centered(cx, cy + 100, gloss, size=SMALL, color=GREYD)
highlighter(ox + 40, 862, 340, 46, VIOLET_BG, angle=0.0)
text(ox + 56, 872, "a diagnostic, not a form", size=BODY, color=VIOLET)
text(ox + 40, 930, "Nobody fills in all six. Check the dials this ask needs, skip the rest.",
     size=SMALL, color=GREYD)

# ============================================================================
# BEAT 4 - FAULT-FINDER  (blue)
# ============================================================================
ox = beat_head(4, "Fault-finder",
               "Something's off in the answer? The symptom tells you\nwhich dial you left unset.")
FAULTS = [
    ("wrong tone",   "Style",      "say how it should read",    0.30),
    ("wrong length", "Parameters", "say how long, what format", 0.25),
    ("wrong shape",  "Example",    "show one that looks right", 0.20),
]
for k, (symptom, fix, gloss, frac) in enumerate(FAULTS):
    ry = 330 + k * 140
    chip(ox + 60, ry, symptom, fill=WHITE, text_color=RED, border=RED, size=BODY)
    arrow(ox + 270, ry + 27, [[0, 0], [96, 0]], stroke=BLUE, sw=4, rough=1)
    dial(ox + 392, ry + 27, frac, BLUE, BLUE_T, r=20)
    chip(ox + 445, ry, fix, fill=WHITE, text_color=BLUE, border=BLUE, size=BODY)
    text(ox + 660, ry + 14, gloss, size=SMALL, color=GREYD)
text(ox + 60, 760, "The fault is almost never \"Claude got it wrong\".\nIt's a dial you didn't set.",
     size=BODY, color=BLUE)

# ============================================================================
# BEAT 5 - TELL IT WHY  (indigo)
# ============================================================================
ox = beat_head(5, "Tell it why",
               "Claude is a brilliant new colleague on their first day.\nGive the reason and it works out the rest itself.")
text(ox + 40, 250, "the rule on its own", size=SMALL, color=GREY)
sticky(ox + 40, 280, 560, 92, FAINT, angle=jit(1.3))
text(ox + 72, 310, "NEVER use ellipses", size=BODY, color=GREYD)
text(ox + 40, 400, "the rule plus the reason", size=SMALL, color=GREY)
sticky(ox + 40, 430, 760, 172, INDIGO_BG, angle=jit(-1.2))
text(ox + 72, 458, "This will be read aloud by a text-to-speech\nengine, so never use ellipses - it won't\nknow how to pronounce them.", size=BODY, color=INK)
text(ox + 40, 626, "Same rule. Only the second one lets Claude work out the cases you\ndidn't think to list.", size=SMALL, color=INDIGO)
sticky(ox + 40, 730, 1040, 156, INDIGO_T, angle=jit(1.1))
text(ox + 76, 754, "Golden rule", size=H3, color=INDIGO)
text(ox + 76, 806, "Show your prompt to a colleague with no context. If they'd\nbe confused, Claude will be too.", size=BODY, color=INK)

# ============================================================================
# BEAT 6 - THREE EXAMPLES BEAT A PARAGRAPH  (green)
# ============================================================================
ox = beat_head(6, "Show, don't just tell",
               "Examples are the most reliable way to steer format,\ntone and structure. Three to five is the sweet spot.")
for k in range(3):
    cx0 = ox + 60 + k * 360
    sticky(cx0, 296, 300, 216, GREEN_BG, angle=jit(1.8))
    rect(cx0 + 24, 320, 252, 168, stroke=GREEN, bg=WHITE, sw=2, rough=1, rounded=True, prefix="excard")
    text(cx0 + 44, 336, "<example>", size=SMALL, color=GREEN)
    for r in range(4):
        line(cx0 + 44, 384 + r * 24, [[0, 0], [(200 if r % 2 else 152), 0]], stroke=GREY, sw=2)
check_item(ox + 60, 570, "Relevant - mirror the job you actually do", accent=GREEN)
check_item(ox + 60, 632, "Diverse - vary them, or Claude copies a quirk", accent=GREEN)
check_item(ox + 60, 694, "Structured - wrap each one in <example> tags", accent=GREEN)
text(ox + 60, 780, "Stuck for examples? Paste your best one and ask Claude to write\nthree more like it, then keep the ones that fit.", size=BODY, color=GREYD)

# ============================================================================
# BEAT 7 - SAY WHAT TO DO  (red)
# ============================================================================
ox = beat_head(7, "Say what to do",
               "\"Don't do X\" leaves Claude guessing at what you\nwanted instead. Name the thing you want.")
PAIRS = [
    ("Do not use markdown",
     "Write in smoothly flowing prose paragraphs."),
    ("Don't write so much",
     "Give me a high-level summary unless I ask\nfor the detail."),
    ("Create a dashboard",
     "Create a dashboard. Include as many relevant\nfeatures and interactions as possible. Go\nbeyond the basics."),
]
for k, (bad, good) in enumerate(PAIRS):
    ry = 290 + k * 186
    xmark(ox + 60, ry + 6, RED, s=20, sw=4)
    text(ox + 106, ry, bad, size=BODY, color=GREYD)
    tick(ox + 58, ry + 54, GREEN)
    text(ox + 106, ry + 50, good, size=BODY, color=INK)
text(ox + 60, 848, "Your prompt's style rubs off too: drop the markdown out of the prompt\nand you get less of it back.", size=SMALL, color=RED)

# ============================================================================
# BEAT 8 - PASTE FIRST, ASK LAST  (blue)
# ============================================================================
ox = beat_head(8, "Paste first, ask last",
               "On a long or multi-document paste, put the documents\nat the top and your question at the very end.")
rect(ox + 60, 300, 440, 400, stroke=BLUE, bg=WHITE, sw=3, rough=1, rounded=True, prefix="prompt")
text(ox + 60, 264, "one prompt, in this order", size=SMALL, color=GREY)
arrow(ox + 30, 312, [[0, 0], [0, 376]], stroke=BLUE, sw=3, rough=1)
rect(ox + 88, 330, 384, 104, stroke=GREYD, bg=BLUE_T, sw=2, rough=1, rounded=True, prefix="doc")
text(ox + 112, 368, "the document", size=BODY, color=INK)
rect(ox + 88, 452, 384, 104, stroke=GREYD, bg=BLUE_T, sw=2, rough=1, rounded=True, prefix="doc")
text(ox + 112, 490, "the other document", size=BODY, color=INK)
rect(ox + 88, 578, 384, 96, stroke=BLUE, bg=BLUE_BG, sw=3, rough=1, rounded=True, prefix="q")
text(ox + 112, 612, "your question", size=BODY, color=BLUE)
sticky(ox + 560, 330, 580, 300, BLUE_BG, angle=jit(-1.2))
text(ox + 596, 356, "Then ask for the quotes", size=H3, color=BLUE)
text(ox + 596, 416, "\"Quote the lines that answer\nthis, then answer using only\nthose quotes.\"", size=BODY, color=INK)
text(ox + 596, 556, "an answer you can check, not one\nyou have to take on trust", size=SMALL, color=GREYD)
text(ox + 60, 748, "Question-at-the-end matters most on long, multi-document pastes.\nOn a one-line ask it makes no difference - don't overthink it.", size=SMALL, color=GREYD)

# ============================================================================
# BEAT 9 - SET ONCE, NEVER REPEAT  (teal)
# ============================================================================
ox = beat_head(9, "Set once, never repeat",
               "Two settings that carry across every chat, so you\nstop retyping the same instructions.")
quill(ox + 300, 500, 200, TEAL, TEAL_T)
text_centered(ox + 300, 610, "Styles", size=H3, color=TEAL)
text_centered(ox + 300, 656, "how Claude writes back", size=SMALL, color=GREYD)
person_big(ox + 830, 480, TEAL, TEAL_T, s=1.5)
text_centered(ox + 830, 610, "preferences", size=H3, color=TEAL)
text_centered(ox + 830, 656, "standing notes for every chat", size=SMALL, color=GREYD)
highlighter(ox + 40, 712, 330, 46, TEAL_BG, angle=0.0)
text(ox + 56, 722, "set once, never repeat", size=BODY, color=TEAL)
demo_badge(ox + 40, 790, "show in Claude desktop app:  set a Style and preferences")

# ============================================================================
# BEAT 10 - IT REMEMBERS YOU NOW  (indigo)
# ============================================================================
ox = beat_head(10, "It remembers you now",
               "Claude can carry context between chats. Two features,\nand one thing to know about Projects.")
sticky(ox + 40, 290, 1040, 170, INDIGO_BG, angle=jit(1.2))
notebook(ox + 80, 306, accent=INDIGO, abg=WHITE)
text(ox + 230, 314, "Memory", size=H3, color=INDIGO)
text(ox + 230, 366, "Holds your role, how you like replies and what you're\nworking on, and brings it to new chats. Say \"remember\nthis\" to save something on purpose.", size=SMALL, color=INK)
sticky(ox + 40, 480, 1040, 170, INDIGO_T, angle=jit(-1.1))
magnifier(ox + 132, 566, r=36, color=INDIGO)
text(ox + 230, 504, "Chat search", size=H3, color=INDIGO)
text(ox + 230, 556, "\"What did we discuss about the refund wording?\" - it goes\nand finds the conversation instead of you scrolling for it.", size=SMALL, color=INK)
sticky(ox + 40, 670, 1040, 130, INDIGO_T, angle=jit(1.0))
folder_tab(ox + 92, 700, accent=INDIGO, abg=WHITE)
text(ox + 230, 694, "Every Project keeps its own memory", size=H3, color=INDIGO)
text(ox + 230, 744, "Project context stays in that Project. It doesn't leak into your other chats.", size=SMALL, color=INK)
text(ox + 40, 830, "This is CRISPE's Context dial, filled in for you - so spend the prompt on\nthe ask, not the background.", size=BODY, color=INDIGO)
text(ox + 40, 916, "On a Team plan an owner switches memory on. If it isn't in your Settings, that's why.",
     size=SMALL, color=GREYD)

# ============================================================================
# BEAT 11 - YOU STAY IN CHARGE OF IT  (red)
# ============================================================================
ox = beat_head(11, "You stay in charge of it",
               "Everything it remembers is visible, editable and deletable -\nand some things must never go in.")
bx = ox + 60
for k, lab in enumerate(["Settings", "Memory", "Topics"]):
    w, h = chip(bx, 268, lab, fill=WHITE, text_color=RED, border=RED, size=BODY)
    bx += w
    if k < 2:
        arrow(bx + 10, 268 + h / 2, [[0, 0], [40, 0]], stroke=RED, sw=3)
        bx += 56
check_item(ox + 60, 352, "Read any topic, edit it, or delete it", accent=RED)
check_item(ox + 60, 408, "Pause memory - keeps what's there, stops adding more", accent=RED)
check_item(ox + 60, 464, "Reset memory - deletes the lot, and that one is permanent", accent=RED)
text(ox + 60, 512, "Deleting a chat does not delete the memories it made - delete those here.",
     size=SMALL, color=RED)
ghost(ox + 128, 600, w=76, h=88, color=GREYD)
text(ox + 220, 560, "Incognito", size=H3, color=GREYD)
text(ox + 220, 606, "the ghost icon, top right: a chat that isn't saved to history\nand isn't remembered.", size=SMALL, color=INK)
rect(ox + 40, 730, 1040, 196, stroke=RED, bg=RED_BG, sw=3, rough=1, rounded=True,
     fill="solid", opacity=35, angle=jit(-1.0), prefix="rule")
diamond(ox + 80, 692, 52, 52, stroke=RED, bg=RED_BG, sw=3)
text_centered(ox + 106, 702, "!", size=H2, color=RED)
text(ox + 80, 752, "The rule", size=H3, color=RED)
text(ox + 80, 802, "Health and the other sensitive topics are left out of memory by default.\nLeave that setting alone. No patient details and nothing confidential goes\ninto a chat that memory can keep.", size=BODY, color=INK)
demo_badge(ox + 40, 946, "show in Claude desktop app:  Settings > Memory > Topics")

# ============================================================================
# BEAT 12 - DIFFERENT MODELS, DIFFERENT HABITS  (violet)
# ============================================================================
ox = beat_head(12, "Different models, different habits",
               "The model you pick changes what comes back. These\nhabits move with every new model - check the docs.")
MODELS = [
    ("Claude Opus 5",
     "answers run long, and it already checks its own work",
     "ask for brief - and don't tell it to double-check itself"),
    ("Claude Sonnet 5",
     "length tracks the task, and it reads you very literally",
     "spell out the scope: \"every section, not just the first\""),
    ("Claude Fable 5 / Mythos 5",
     "built to run on its own for a long time",
     "ask it to back progress claims with evidence"),
    ("Claude Opus 4.8",
     "reasons rather than reaching for tools, and has a strong house look",
     "say when to search, and describe the look you want"),
]
for k, (name, habit, todo) in enumerate(MODELS):
    ry = 300 + k * 150
    sticky(ox + 40, ry, 1080, 140, VIOLET_T, angle=jit(1.0))
    text(ox + 76, ry + 18, name, size=H3, color=VIOLET)
    text(ox + 76, ry + 64, habit, size=SMALL, color=GREYD)
    text(ox + 76, ry + 96, todo, size=BODY, color=INK)
text(ox + 40, 918, "Docs: Anthropic - Prompting best practices, platform.claude.com",
     size=SMALL, color=VIOLET)

# ============================================================================
# BEAT 13 - CAPTURE BY VOICE  (yellow)
# ============================================================================
ox = beat_head(13, "Capture by voice",
               "Talking is faster than typing, and a rambling\nspoken prompt still beats a vague written one.")
phone(ox + 90, 320, 250, 460, YELLOW_T)
mic_icon(ox + 215, 540, 92, YELLOW)
squiggle(ox + 360, 550, 300, YELLOW, amp=20, waves=4.0)
monitor(ox + 700, 420, 380, 250, YELLOW_T)
text_centered(ox + 215, 806, "say it, roughly", size=SMALL, color=GREYD)
text_centered(ox + 890, 760, "tidy it up here", size=SMALL, color=GREYD)
highlighter(ox + 40, 862, 480, 46, YELLOW_BG, angle=0.0)
text(ox + 56, 872, "capture by voice, shape at your desk", size=BODY, color=YELLOW)
text(ox + 40, 930, "The fastest prompt is usually the one you said out loud.",
     size=SMALL, color=GREYD)

# No connector spine, no inter-beat arrows, no baseline: the beats read as one
# picture through consistent shape and rhythm, and the whitespace is the camera.

# ----------------------------------------------------------------------------
# WRITE + VALIDATE  (shared excalidraw_kit)
# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "prompting-crispe-framework.excalidraw")
MAXW = max(WID.values()) + 200
finish(out, MAXW, TOTAL_W)
