#!/usr/bin/env python3
"""Build claude-cowork.excalidraw - ONE flowing, illustrated explainer for
DAY 8 of the Phlo AI training: "Cowork" (~7 min, hard cap 10).

Day 8 is the expensive rung. Chat is a conversation you supervise turn by turn;
Cowork is a shift you hand over, and the supervision model has to change with
it. Every beat is bent towards that one idea: the brief carries the whole job,
the checkpoints are where you get back in, and a long run hides its mistakes.

This board was the nine-beat module-2 Cowork walkthrough at
videos/claude/11-cowork/build_cowork.py. It moved here and was rewritten when
the day-by-day training became the authoritative series - the same move Day 4
made out of videos/claude/2-projects/ and Day 7 out of videos/claude/4-skills/.
videos/claude/ now has a numbering gap at 11; a gap is not lost work. It also
ABSORBS DISPATCH from the retired day 13 - beat 8. What came off the old board
(who it is for, plan and platform matrix, the scoped-folder mechanics, the
permission modes in full, the old demo steps) lives on the Resource Card,
claude-cowork-resource-card.md.

Style B (house style): a single hand-drawn journey, left-to-right, NO frames, NO
boxes round beats, white canvas, everything in the hand font (fontFamily 1),
roughness 1, a lively colour-coded Excalidraw palette, big colour-blocking,
scribbled annotations and charming primitive illustrations. The look lives in
the shared excalidraw_kit; this file holds only the composition and this board's
bespoke illustrations.

Three colours are held constant across the board and are never beat accents:
  RED   = a mistake, or a thing you must not hand over (beats 2, 6, 7, 9)
  GREEN = a checked, finished output (beats 2, 5, 6, 9)  - except beat 8, whose
          accent is green because Dispatch is the good-news beat
  GREY  = the part of the run you are no longer watching (beats 1, 2)

STOPS (beat 4) is the one place this board guesses. It is a callback to the
three checkpoints on the day 6 autonomy-ladder board, which does not exist yet;
the three labels below are derived from this day's brief ("placed against real
file handoffs"). They are pinned in ONE constant so reconciling with day 6 later
is a one-line edit, not a re-layout. See claude-cowork-prompt.md.

PAN ORDER (left to right - the whitespace between slots IS the camera; frame one
beat at a time, ~40s each):

     1  ORANGE  a conversation versus a shift
     2  VIOLET  the brief is the whole job
     3  BLUE    what a brief must name
     4  TEAL    checkpoints, applied           <- [CUT TO CLAUDE DESKTOP]
     5  INDIGO  it splits the work             <- sub-agents
     6  RED     long runs hide their mistakes  <- the adversarial beat
     7  YELLOW  it has its own browser
     8  GREEN   start it from your phone       <- Dispatch, from the old day 13
     9  ORANGE  what belongs here              <- ships + pause-and-try

Run:  python3 videos/ai-training/8-cowork/build_cowork.py
      /usr/bin/python3 preview.py videos/ai-training/8-cowork/claude-cowork.excalidraw out.png
      /usr/bin/python3 preview.py <scene> out.png XMIN XMAX   # one beat close up
      python3 build_all.py            # rebuild all + Style-B guard

Beat n frames at XMIN = (n-1)*2000 - 100, XMAX = (n-1)*2000 + 1250.
"""
import os
import sys

_d = os.path.dirname(os.path.abspath(__file__))
while _d != os.path.dirname(_d) and not os.path.exists(os.path.join(_d, "excalidraw_kit.py")):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)

import random
from excalidraw_kit import *

random.seed(80811)  # deterministic - re-runs produce identical files

# ----------------------------------------------------------------------------
# BEAT SCAFFOLD - nine beats, wide gaps so one frames cleanly on a 14" laptop
# ----------------------------------------------------------------------------
N = 9
GAP = 800
# every beat uses the SAME slot, shaped ~1.15:1 (content ~1120 wide x ~980 tall,
# heading at y60 counted in) so framing is identical on a 14" laptop. Content
# fills the slot; it never spreads wider than ox+1120 or below y~980.
WID = {i: 1200 for i in range(1, N + 1)}
ACCENT = {1: ORANGE, 2: VIOLET, 3: BLUE, 4: TEAL, 5: INDIGO,
          6: RED, 7: YELLOW, 8: GREEN, 9: ORANGE}
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
# THE ONE PLACE THIS BOARD GUESSES - the day 6 callback (beat 4).
# Three stops, each a real file handoff. Change these three tuples and beat 4
# re-lays itself out; nothing else on the board depends on the wording.
# ----------------------------------------------------------------------------
STOPS = [
    ("before the\nfirst write", "it has read everything and is\nabout to change a file"),
    ("at the join", "the branches come back together\nand become one answer"),
    ("before it leaves\nthe folder", "the output goes to a person,\na channel, or a system"),
]

# ----------------------------------------------------------------------------
# BESPOKE ILLUSTRATIONS for this board (one-offs stay here, never in the kit)
# ----------------------------------------------------------------------------
def folder(x, y, w=96, h=70, accent=YELLOW, abg=YELLOW_BG):
    rect(x, y + 14, w, h, stroke=INK, bg=abg, sw=2, rough=1, rounded=True, prefix="fold")
    rect(x, y, w * 0.5, 22, stroke=INK, bg=abg, sw=2, rough=1, rounded=True, prefix="foldtab")


def deliverable(x, y, accent=GREEN, abg=GREEN_BG):
    """A finished one-pager with a green tick badge."""
    rect(x, y, 150, 196, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="del")
    rect(x + 18, y + 22, 90, 14, stroke="transparent", bg=accent, sw=1, rough=1, rounded=True, prefix="deltt")
    for k in range(5):
        line(x + 18, y + 58 + k * 22, [[0, 0], [(96 if k % 2 else 70), 0]], stroke=GREY, sw=2)
    ellipse(x + 108, y + 150, 54, 54, stroke=GREEN, bg=WHITE, sw=3)
    tick(x + 122, y + 164, color=GREEN, s=26, sw=5)


def monitor(x, y, w, h, abg=BLUE_BG):
    """A desktop machine - screen, stand, base."""
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="mon")
    rect(x + 10, y + 10, w - 20, h - 20, stroke=GREY, bg=abg, sw=1, rough=1,
         rounded=True, fill="solid", opacity=30, prefix="monscr")
    rect(x + w / 2 - 34, y + h, 68, 20, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=False, prefix="monstand")
    rect(x + w / 2 - 80, y + h + 20, 160, 12, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="monbase")


def step_box(x, y, n, accent, abg, w=95, h=80, angle=0.0, num_color=None):
    """One numbered step in a long run."""
    rect(x, y, w, h, stroke=accent, bg=abg, sw=2, rough=1, rounded=True,
         fill="solid", angle=angle, prefix="stp")
    text_centered(x + w / 2, y + h / 2 - H3 * 0.7, str(n), size=H3,
                  color=(num_color or accent), angle=angle)


def phone(x, y, w=200, h=380):
    """A hand-drawn phone - speaker slot, screen, home dot."""
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=3, rough=1, rounded=True, prefix="ph")
    line(x + w / 2 - 24, y + 18, [[0, 0], [48, 0]], stroke=GREY, sw=3)
    rect(x + 12, y + 36, w - 24, h - 74, stroke=GREY, bg=WHITE, sw=1, rough=1,
         rounded=True, prefix="phscr")
    ellipse(x + w / 2 - 11, y + h - 30, 22, 22, stroke=GREY, bg=WHITE, sw=2)


def browser(x, y, w, h, accent=YELLOW, abg=YELLOW_BG):
    """A browser window - chrome bar, URL pill, a page with a form and a button."""
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=3, rough=1, rounded=True, prefix="brw")
    line(x, y + 48, [[0, 0], [w, 0]], stroke=GREY, sw=2)
    for k in range(3):
        ellipse(x + 20 + k * 22, y + 17, 12, 12, stroke=GREY, bg=GREY, sw=1)
    rect(x + 110, y + 12, w - 150, 26, stroke=GREY, bg=abg, sw=1, rough=1,
         rounded=True, fill="solid", opacity=60, prefix="url")
    for k in range(3):
        line(x + 34, y + 92 + k * 30, [[0, 0], [(w * 0.5 if k % 2 else w * 0.62), 0]],
             stroke=GREY, sw=3)
    rect(x + 34, y + 206, w * 0.46, 44, stroke=GREYD, bg=WHITE, sw=2, rough=1,
         rounded=True, prefix="field")
    rect(x + 34, y + 274, 168, 50, stroke=accent, bg=accent, sw=2, rough=1,
         rounded=True, prefix="brbtn")
    # Claude's pointer, mid-click
    line(x + w - 172, y + 250, [[0, 0], [0, 34], [11, 25], [19, 41], [27, 37], [19, 21], [32, 20], [0, 0]],
         stroke=INK, sw=3, prefix="ptr")


def bubble(x, y, w, h, fill, tail_left=True):
    """A speech bubble - rounded body plus a small tail."""
    rect(x, y, w, h, stroke="transparent", bg=fill, sw=1, rough=1, rounded=True,
         fill="solid", prefix="bub")
    tx = x + 26 if tail_left else x + w - 26
    d = 22 if tail_left else -22
    line(tx, y + h - 2, [[0, 0], [d, 22], [d * 0.1, 0]], stroke="transparent",
         bg=fill, fill="solid", sw=1, prefix="bubtail")


# ============================================================================
# BOARD TITLE
# ============================================================================
text(OX[1], -300, "Day 8 - Cowork", size=HERO, color=INK)
text(OX[1] + 6, -300 + HERO * LINE_H + 4,
     "a shift you hand over, not a conversation you steer", size=H2, color=ORANGE)

# ============================================================================
# BEAT 1 - A CONVERSATION VERSUS A SHIFT
# ============================================================================
ox = beat_head(1, "A conversation versus a shift",
               "Chat is a turn you supervise. Cowork is a run that keeps\ngoing while you are doing something else.")

text(ox + 20, 292, "chat", size=H3, color=GREYD)
turns = [("“reword this reply”", FAINT, 20),
         ("a draft comes back", ORANGE_BG, 90),
         ("“shorter, warmer”", FAINT, 20),
         ("a better draft", ORANGE_BG, 90)]
for k, (msg, fill, dx) in enumerate(turns):
    yy = 352 + k * 92
    bubble(ox + dx, yy, 370, 74, fill, tail_left=(k % 2 == 0))
    text(ox + dx + 26, yy + 24, msg, size=SMALL, color=INK)
    tick(ox + 480, yy + 22, color=GREEN, s=20, sw=4)
text(ox + 20, 740, "you read every turn", size=BODY, color=GREYD)

text(ox + 600, 292, "Cowork", size=H3, color=ORANGE)
sticky(ox + 600, 340, 480, 116, ORANGE_BG, angle=jit(1.2))
text(ox + 626, 360, "one brief:", size=SMALL, color=ORANGE)
text(ox + 626, 392, "“reconcile these two lists\nand write up the gaps”", size=SMALL, color=INK)
arrow(ox + 840, 462, [[0, 0], [0, 40]], stroke=ORANGE, sw=4)
for k in range(9):
    col, row = k % 3, k // 3
    sx, sy = ox + 640 + col * 130, 520 + row * 96
    watched = k < 3
    step_box(sx, sy, k + 1, ORANGE if watched else GREY,
             ORANGE_BG if watched else WHITE, w=84, h=72, angle=jit(1.6),
             num_color=ORANGE if watched else GREY)
    if col < 2:
        arrow(sx + 88, sy + 36, [[0, 0], [34, 0]], stroke=GREY, sw=2)
text(ox + 1000, 536, "watching", size=SMALL, color=ORANGE)
text(ox + 1000, 640, "not watching", size=SMALL, color=GREY)
text(ox + 600, 800, "you stop watching at step three", size=BODY, color=GREYD)

# ============================================================================
# BEAT 2 - THE BRIEF IS THE WHOLE JOB
# ============================================================================
ox = beat_head(2, "The brief is the whole job",
               "In chat you correct it on the next turn. In a run there is\nno next turn - the brief is the only steering you get.")

text(ox + 20, 292, "a thin brief", size=H3, color=GREYD)
rect(ox + 20, 344, 300, 96, stroke=GREY, bg=WHITE, sw=2, rough=1, rounded=True)
text(ox + 44, 374, "“tidy up the reports”", size=SMALL, color=INK)
line(ox + 360, 384, [[0, 0], [520, 0]], stroke=FAINT, sw=2, dashed=True, prefix="guide")
for k, drop in enumerate([0, 6, 18, 36, 60, 88]):
    step_box(ox + 366 + k * 88, 350 + drop, k + 1, GREY, WHITE, w=60, h=58,
             angle=jit(2.0 + k * 1.6), num_color=GREY)
rect(ox + 930, 400, 108, 132, stroke=GREY, bg=WHITE, sw=2, rough=1, rounded=True, prefix="baddoc")
for k in range(4):
    line(ox + 948, 428 + k * 22, [[0, 0], [64, 0]], stroke=FAINT, sw=2)
xmark(ox + 1052, 402, color=RED, s=26, sw=5)
text(ox + 800, 552, "drifted - you find out at the end", size=SMALL, color=GREYD)

text(ox + 20, 620, "a specified brief", size=H3, color=VIOLET)
rect(ox + 20, 672, 300, 200, stroke=VIOLET, bg=VIOLET_T, sw=2, rough=1, rounded=True)
text(ox + 44, 696, "the folder, the columns,\nwhat to skip, when to\nstop and ask me", size=SMALL, color=INK)
text(ox + 44, 812, "four sentences", size=SMALL, color=VIOLET)
line(ox + 360, 740, [[0, 0], [520, 0]], stroke=VIOLET_BG, sw=3, prefix="guide")
for k in range(6):
    step_box(ox + 366 + k * 88, 706, k + 1, VIOLET, VIOLET_BG, w=60, h=58,
             angle=jit(0.8), num_color=VIOLET)
rect(ox + 930, 674, 108, 132, stroke=VIOLET, bg=WHITE, sw=2, rough=1, rounded=True, prefix="gooddoc")
for k in range(4):
    line(ox + 948, 702 + k * 22, [[0, 0], [64, 0]], stroke=GREY, sw=2)
tick(ox + 1046, 676, color=GREEN, s=26, sw=5)
text(ox + 800, 826, "the same work - and checkable", size=SMALL, color=GREYD)

# ============================================================================
# BEAT 3 - WHAT A BRIEF MUST NAME
# ============================================================================
ox = beat_head(3, "What a brief must name",
               "Name these, or Claude guesses them - nine times over,\non its own, while you are not looking.")
must = [("the inputs", "which folder, which files,\nwhich list wins when they clash"),
        ("the output shape", "one page, a table with these\nfour columns, in this order"),
        ("what a gap means", "skip a missing file and list it\nat the end - never guess a number"),
        ("when to stop and ask", "anything that changes a number,\nor anything that leaves the folder")]
for k, (ttl, egs) in enumerate(must):
    cx = ox + 30 + (k % 2) * 550
    cy = 316 + (k // 2) * 240
    rect(cx, cy, 500, 210, stroke=BLUE, bg=WHITE, sw=2, rough=1, rounded=True, angle=jit(0.5))
    num_badge(cx + 26, cy + 24, k + 1, BLUE)
    text(cx + 88, cy + 30, ttl, size=H3, color=BLUE)
    text(cx + 30, cy + 108, egs, size=SMALL, color=INK)
text(ox + 30, 806, "Four sentences - the difference between a run you can check\nand a run you have to do again yourself.",
     size=BODY, color=GREYD)

# ============================================================================
# BEAT 4 - CHECKPOINTS, APPLIED
# ============================================================================
ox = beat_head(4, "Checkpoints, applied",
               "You met these three on the autonomy ladder. Here they\nare against real files, in a real run.")
for k, (ttl, cap) in enumerate(STOPS):
    cx = ox + 190 + k * 370
    num_badge(cx - 22, 300, k + 1, TEAL)
    # every panel reads source -> [pause] -> target, so the stop sits ON the handoff
    if k == 0:
        claude_face(cx - 118, 424, r=36, color=TEAL)
        arrow(cx - 76, 424, [[0, 0], [36, 0]], stroke=TEAL, sw=4)
        pause_icon(cx - 26, 404, 40, color=TEAL)
        arrow(cx + 24, 424, [[0, 0], [28, 0]], stroke=TEAL, sw=4)
        file_icon(cx + 58, 388, 58, 74, abg=TEAL_BG)
    elif k == 1:
        for dy in (-58, 0, 58):
            arrow(cx - 152, 424 + dy, [[0, 0], [82, -dy]], stroke=TEAL, sw=3)
        pause_icon(cx - 48, 404, 40, color=TEAL)
        arrow(cx + 2, 424, [[0, 0], [28, 0]], stroke=TEAL, sw=4)
        file_icon(cx + 36, 388, 58, 74, abg=TEAL_BG)
    else:
        file_icon(cx - 142, 388, 58, 74, abg=TEAL_BG)
        arrow(cx - 74, 424, [[0, 0], [28, 0]], stroke=TEAL, sw=4)
        pause_icon(cx - 32, 404, 40, color=TEAL)
        arrow(cx + 18, 424, [[0, 0], [30, 0]], stroke=TEAL, sw=4)
        person(cx + 96, 446, TEAL)
    text_centered(cx, 512, ttl, size=H3, color=TEAL)
    text_centered(cx, 618, cap, size=SMALL, color=GREYD)
text(ox + 20, 706, "Name them in the brief before the run starts, not after it surprises you.",
     size=BODY, color=GREYD)
chip(ox + 20, 762, "Cowork calls the asking mode Manual", fill=WHITE, text_color=TEAL, border=TEAL)
text(ox + 500, 776, "Auto keeps going. Skip checks nothing at all.", size=SMALL, color=GREYD)
demo_badge(ox + 20, 856,
           "show in Claude desktop app:  run a real multi-file task in Manual, stop it at the first checkpoint")

# ============================================================================
# BEAT 5 - IT SPLITS THE WORK
# ============================================================================
ox = beat_head(5, "It splits the work",
               "One brief becomes several workers running at once -\nsub-agents, each with its own context.")
rect(ox + 20, 435, 260, 150, stroke=INDIGO, bg=INDIGO_T, sw=2, rough=1, rounded=True)
text(ox + 44, 462, "one brief", size=H3, color=INDIGO)
text(ox + 44, 514, "“reconcile these,\nthen write it up”", size=SMALL, color=INK)
branches = ["reads the folder", "checks the numbers", "drafts the write-up", "finds what is missing"]
for k, lab in enumerate(branches):
    yy = 300 + k * 110
    rect(ox + 360, yy, 300, 90, stroke=INDIGO, bg=WHITE, sw=2, rough=1, rounded=True, angle=jit(0.8))
    ellipse(ox + 384, yy + 38, 16, 16, stroke=INDIGO, bg=INDIGO, sw=2)
    text(ox + 414, yy + 34, lab, size=SMALL, color=INK)
    arrow(ox + 290, 510, [[0, 0], [62, (yy + 45) - 510]], stroke=INDIGO, sw=2)
    arrow(ox + 668, yy + 45, [[0, 0], [86, 510 - (yy + 45)]], stroke=INDIGO, sw=2)
ellipse(ox + 760, 475, 70, 70, stroke=INDIGO, bg=WHITE, sw=3)
text_centered(ox + 795, 498, "join", size=SMALL, color=INDIGO)
arrow(ox + 836, 510, [[0, 0], [52, 0]], stroke=INDIGO, sw=4)
deliverable(ox + 900, 412, accent=INDIGO, abg=INDIGO_BG)
text(ox + 898, 632, "one answer", size=SMALL, color=INDIGO)
chip(ox + 20, 762, "you review the join, not each branch", fill=INDIGO_BG, text_color=INK, border=INDIGO)
text(ox + 20, 856, "The branches are the fast part. The join is where the mistakes meet,\nso that is the part you read.",
     size=BODY, color=GREYD)

# ============================================================================
# BEAT 6 - LONG RUNS HIDE THEIR MISTAKES
# ============================================================================
ox = beat_head(6, "Long runs hide their mistakes",
               "Nothing crashes. The run finishes, on time, and hands\nyou something that reads exactly right.")
text(ox + 132, 288, "one wrong assumption, here", size=SMALL, color=RED)
arrow(ox + 196, 320, [[0, 0], [0, 28]], stroke=RED, sw=3)
for k in range(9):
    sx = ox + 30 + k * 118
    if k == 0:
        step_box(sx, 356, 1, GREY, WHITE, w=98, h=82, angle=jit(1.2), num_color=GREY)
    elif k == 1:
        step_box(sx, 356, 2, RED, RED_BG, w=98, h=82, angle=jit(1.2), num_color=RED)
    else:
        step_box(sx, 356, k + 1, RED, RED_T, w=98, h=82, angle=jit(1.2), num_color=RED)
    if k < 8:
        arrow(sx + 102, 397, [[0, 0], [12, 0]], stroke=GREY, sw=2)
line(ox + 178, 452, [[0, 0], [0, 44], [844, 44], [844, 0]], stroke=RED, sw=3, dashed=True, prefix="carry")
text(ox + 330, 516, "each step is right, given the one before it", size=BODY, color=GREYD)

text(ox + 30, 594, "what arrives", size=H3, color=RED)
for k, (glyph, lab) in enumerate([("tick", "reads well"), ("tick", "adds up"),
                                  ("x", "wrong since step two")]):
    yy = 662 + k * 62
    if glyph == "tick":
        tick(ox + 30, yy + 2, color=GREEN, s=22, sw=4)
    else:
        xmark(ox + 30, yy + 2, color=RED, s=22, sw=4)
    text(ox + 76, yy, lab, size=BODY, color=INK)
arrow(ox + 1036, 452, [[0, 0], [-32, 132]], stroke=GREY, sw=2)
rect(ox + 860, 594, 180, 224, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="outdoc")
rect(ox + 884, 620, 110, 16, stroke="transparent", bg=RED_BG, sw=1, rough=1, rounded=True, prefix="outtt")
for k in range(6):
    line(ox + 884, 660 + k * 24, [[0, 0], [(126 if k % 2 else 96), 0]], stroke=GREY, sw=2)
text(ox + 836, 834, "looks finished", size=SMALL, color=GREYD)
chip(ox + 30, 862, "the fix is a checkpoint at step two, not a better model",
     fill=RED_T, text_color=INK, border=RED)

# ============================================================================
# BEAT 7 - IT HAS ITS OWN BROWSER
# ============================================================================
ox = beat_head(7, "It has its own browser",
               "When a step needs a website, a browser opens in the side\npanel and Claude works the page itself.")
text(ox + 20, 300, "a step in the run", size=SMALL, color=GREYD)
for k in range(3):
    hot = k == 2
    step_box(ox + 20 + k * 118, 470, k + 4, YELLOW if hot else GREY,
             YELLOW_BG if hot else WHITE, w=98, h=82, angle=jit(1.2),
             num_color=YELLOW if hot else GREY)
arrow(ox + 362, 511, [[0, 0], [26, 0]], stroke=YELLOW, sw=4)
text(ox + 400, 300, "no extension, no setup", size=SMALL, color=YELLOW)
browser(ox + 400, 344, 680, 356, accent=YELLOW, abg=YELLOW_BG)
chip(ox + 400, 726, "it asks before a new site", fill=WHITE, text_color=YELLOW, border=YELLOW)
chip(ox + 760, 726, "nothing shared from your own browser", fill=WHITE, text_color=YELLOW, border=YELLOW)
xmark(ox + 20, 818, color=RED, s=20, sw=4)
text(ox + 56, 810, "a page can carry instructions written at Claude, not at you", size=BODY, color=INK)
xmark(ox + 20, 866, color=RED, s=20, sw=4)
text(ox + 56, 858, "anything you sign it into stays available to it in later runs", size=BODY, color=INK)
text(ox + 20, 924, "Computer use - Claude clicking round your actual screen - is a wider, separate thing:\nbeta, Pro and Max only, not on Team or Enterprise. Different feature, not today's lesson.",
     size=SMALL, color=GREYD)

# ============================================================================
# BEAT 8 - START IT FROM YOUR PHONE  (Dispatch, absorbed from the old day 13)
# ============================================================================
ox = beat_head(8, "Start it from your phone",
               "Dispatch: send the brief from the train, the run happens\non your desktop, and the answer finds you.")
text_centered(ox + 140, 292, "your phone", size=SMALL, color=GREEN)
phone(ox + 40, 336, 200, 372)
bubble(ox + 60, 384, 160, 96, GREEN_BG, tail_left=True)
text(ox + 76, 402, "“sort the\ninvoices folder”", size=SMALL, color=INK)
arrow(ox + 258, 500, [[0, 0], [116, 0]], stroke=GREEN, sw=4)
text(ox + 262, 452, "the brief", size=SMALL, color=GREEN)

text_centered(ox + 650, 292, "your desktop, awake", size=SMALL, color=GREEN)
monitor(ox + 390, 348, 520, 300, abg=GREEN_BG)
folder(ox + 434, 412, accent=GREEN, abg=GREEN_BG)
file_icon(ox + 566, 408, 58, 74, abg=GREEN_BG)
claude_face(ox + 782, 470, r=40, color=GREEN)
text(ox + 434, 546, "working through the folder", size=SMALL, color=GREYD)
arrow(ox + 926, 500, [[0, 0], [56, 0]], stroke=GREEN, sw=4)

text_centered(ox + 1030, 292, "back to you", size=SMALL, color=GREEN)
phone(ox + 990, 336, 140, 260)
bubble(ox + 1002, 376, 116, 76, GREEN_BG, tail_left=False)
text(ox + 1014, 392, "done -\n3 flagged", size=SMALL, color=INK)

chip(ox + 40, 736, "one conversation, synced across both", fill=GREEN_BG, text_color=INK, border=GREEN)
text(ox + 40, 824, "It runs on your own desktop, not in a cloud - your machine stays awake\nwith Claude Desktop open, and it pings you when it wants a yes.",
     size=BODY, color=GREYD)
text(ox + 40, 932, "Limited beta, Pro and Max only - so you may not see it on a Team plan yet.",
     size=SMALL, color=GREYD)

# ============================================================================
# BEAT 9 - WHAT BELONGS HERE
# ============================================================================
ox = beat_head(9, "What belongs here",
               "Not everything deserves a shift. Three tests for handing\nit over, and two that send it back to chat.")
text(ox + 20, 292, "hand it over", size=H3, color=ORANGE)
for k, (lab, gloss) in enumerate([("many files", "the work is the moving between them"),
                                  ("repeatable", "you will run this again next month"),
                                  ("survives a second pass", "run it twice, get the same answer")]):
    yy = 356 + k * 124
    tick(ox + 20, yy + 12, color=GREEN, s=22, sw=4)
    chip(ox + 62, yy, lab, fill=ORANGE_BG, text_color=INK, border=ORANGE)
    text(ox + 66, yy + 66, gloss, size=SMALL, color=GREYD)

text(ox + 600, 292, "keep it in chat", size=H3, color=RED)
for k, (lab, gloss) in enumerate([("anything you cannot check", "if you cannot verify it,\nyou cannot hand it over"),
                                  ("anything patient-facing without a gate", "Claude drafts, a person approves,\nthen the record updates")]):
    yy = 356 + k * 186
    xmark(ox + 600, yy + 12, color=RED, s=22, sw=4)
    chip(ox + 642, yy, lab, fill=RED_T, text_color=INK, border=RED)
    text(ox + 646, yy + 84, gloss, size=SMALL, color=GREYD)

text(ox + 20, 742, "The test is not “can Claude do it” - it is “can I check it when it comes back”.",
     size=BODY, color=INK)
sticky(ox + 20, 800, 1080, 168, ORANGE_BG, angle=jit(0.9))
text(ox + 52, 820, "Ships today", size=H3, color=ORANGE)
text(ox + 52, 872, "one multi-step task handed to Cowork, with its checkpoints named before it runs",
     size=BODY, color=INK)
text(ox + 52, 916, "Pause and try", size=BODY, color=ORANGE)
text(ox + 226, 916, "write the brief, then find the sentence doing no work", size=BODY, color=INK)

# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "claude-cowork.excalidraw")
finish(out, max(WID.values()) + 200, TOTAL_W)
