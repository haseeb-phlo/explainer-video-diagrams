#!/usr/bin/env python3
"""Build claude-skills.excalidraw - ONE flowing, illustrated explainer for
DAY 7 of the Phlo AI training: "Skills" (~4-5 min, hard cap 8).

Day 7 is the cheapest rung on the ladder and the first real artefact a person
ships. It sits before Cowork deliberately: most of what people bring to Cowork
should have been a Skill. It also absorbs the prompt-repair half of the retired
reverse-prompting day - beat 5.

This board was the eleven-beat module-2 Skills walkthrough at
videos/claude/4-skills/build_skills_training.py. It moved here and was cut to six
beats when the day-by-day training became the authoritative series - the same
move Day 4 made out of videos/claude/2-projects/. What came off the board (the
SKILL.md anatomy, the four types, the enable-a-Skill flow, progressive
disclosure, the recap) lives on the Resource Card, claude-skills-resource-card.md.

Style B (house style): a single hand-drawn journey, left-to-right, NO frames, NO
boxes, white canvas, everything in the hand font (fontFamily 1), roughness 1, a
lively colour-coded Excalidraw palette, big colour-blocking, scribbled annotations
and charming primitive illustrations. The look lives in the shared excalidraw_kit;
this file holds only the composition and this board's bespoke illustrations.

Two colours are held constant across the board and are not beat accents:
  INDIGO = a Skill (the object itself, wherever it appears)
  VIOLET = a Project folder (the repo-wide convention, as on the Day 4 board)

PAN ORDER (left to right - the whitespace between slots IS the camera; frame one
beat at a time, ~45s each):

     1  ORANGE  you have explained this four times
     2  VIOLET  procedure, not context             <- Project vs Skill, side by side
     3  BLUE    search the gallery first           <- the gallery shelf + the data caution
     4  TEAL    the hidden assumption
     5  RED     make it critique its own steps     <- [CUT TO CLAUDE DESKTOP]
     6  GREEN   test on a known input              <- closing chip

Run:  python3 videos/ai-training/7-skills/build_skills.py
      python3 preview.py videos/ai-training/7-skills/claude-skills.excalidraw out.png
      python3 build_all.py            # rebuild all + Style-B guard
"""
import math
import os
import sys

_d = os.path.dirname(os.path.abspath(__file__))
while _d != os.path.dirname(_d) and not os.path.exists(os.path.join(_d, "excalidraw_kit.py")):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)

import random
from excalidraw_kit import *

random.seed(70714)  # deterministic - re-runs produce identical files

# ----------------------------------------------------------------------------
# BEAT SCAFFOLD - six beats, wide gaps so one frames cleanly on a 14" laptop
# ----------------------------------------------------------------------------
GAP = 800
# every beat uses the SAME slot, shaped ~1.15:1 (content ~1120 wide x ~980 tall,
# heading at y60 counted in) so framing is identical on a 14" laptop. Content
# fills the slot; it never spreads wider than ox+1120 or below y~1050.
WID = {i: 1200 for i in range(1, 7)}
ACCENT = {1: ORANGE, 2: VIOLET, 3: BLUE, 4: TEAL, 5: RED, 6: GREEN}
OX = {}
_c = 0
for _i in range(1, 7):
    OX[_i] = _c
    _c += WID[_i] + GAP
TOTAL_W = _c

HEAD_Y = 60

def beat_head(i, title, sub=None):
    ox = OX[i]
    heading(ox, HEAD_Y, title, color=ACCENT[i], sub=sub)
    return ox

# ----------------------------------------------------------------------------
# BESPOKE ILLUSTRATIONS for this board (one-offs stay here, never in the kit)
# ----------------------------------------------------------------------------
def jit_min(lo=1.2, hi=2.8):
    """Rotation jitter with a guaranteed-visible magnitude - the kit's jit() can
    land near zero, which reads as 'forgot to tilt this one' when four copies of
    the same doodle sit next to each other."""
    return random.choice((-1, 1)) * random.uniform(lo, hi) * math.pi / 180.0


def rotate_group(els, cx, cy, a):
    """Tilt already-placed elements as one group about (cx, cy) - the hand-placed
    wobble applied to a whole doodle rather than to each piece separately. Safe for
    rectangles, ellipses, text and horizontal lines, whose x/y/width/height give
    their true centre; don't feed it lines with negative points."""
    ca, sa = math.cos(a), math.sin(a)
    for e in els:
        dx = e["x"] + e["width"] / 2 - cx
        dy = e["y"] + e["height"] / 2 - cy
        e["x"] = cx + dx * ca - dy * sa - e["width"] / 2
        e["y"] = cy + dx * sa + dy * ca - e["height"] / 2
        e["angle"] = a


def mini_chat(x, y, w, h, day, correction, abg):
    """A small chat-window doodle holding one pasted correction, tilted as a group."""
    i0 = len(E)
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="mc")
    line(x, y + 40, [[0, 0], [w, 0]], stroke=FAINT, sw=2)
    for k in range(3):
        ellipse(x + 16 + k * 17, y + 15, 10, 10, stroke=GREY, bg=GREY, sw=1)
    text(x + w - 96, y + 9, day, size=SMALL, color=GREY)
    for k, f in enumerate((0.62, 0.44)):
        rect(x + 22, y + 58 + k * 32, (w - 44) * f, 20, stroke="transparent",
             bg=FAINT, sw=1, rough=1, rounded=True, prefix="mcb")
    sticky(x + 22, y + 132, w - 44, h - 154, abg, angle=0.0)
    text(x + 48, y + 152, correction, size=BODY, color=INK)
    rotate_group(E[i0:], x + w / 2, y + h / 2, jit_min(1.2, 2.6))


def shelf_card(x, y, w, h, label, accent, abg):
    """A face-out card standing on the gallery shelf - coloured header, hand label."""
    i0 = len(E)
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="shc")
    rect(x, y, w, 30, stroke="transparent", bg=abg, sw=1, rough=1, rounded=True, prefix="shch")
    for k in range(3):
        line(x + 22, y + 52 + k * 15, [[0, 0], [w - 66 - k * 24, 0]], stroke=FAINT, sw=2)
    text_centered(x + w / 2, y + h - 42, label, size=SMALL, color=accent)
    rotate_group(E[i0:], x + w / 2, y + h / 2, jit_min(0.9, 2.0))


def _rp(a, x, y):
    ca, sa = math.cos(a), math.sin(a)
    return x * ca - y * sa, x * sa + y * ca


def falling_person(cx, cy, color, tilt=0.7):
    """A colleague mid-tumble - a stick figure with arms up and legs kicking, the
    whole body pre-rotated. Drawn from pre-rotated points rather than element
    angles, because the kit's line elements anchor at their start point, not at
    their bounding box, so an angle would slide them sideways."""
    hx, hy = _rp(tilt, 0, -48)
    ellipse(cx + hx - 18, cy + hy - 18, 36, 36, stroke=color, bg=WHITE, sw=3, rough=1)
    sx, sy = _rp(tilt, 0, -28)
    px, py = _rp(tilt, 0, 26)
    line(cx + sx, cy + sy, [[0, 0], [px - sx, py - sy]], stroke=color, sw=3, rough=1)
    for joint, limb in [((0, -18), (-36, -32)), ((0, -18), (38, -24)),
                        ((0, 26), (-30, 56)), ((0, 26), (34, 50))]:
        jx, jy = _rp(tilt, *joint)
        lx, ly = _rp(tilt, *limb)
        line(cx + jx, cy + jy, [[0, 0], [lx - jx, ly - jy]], stroke=color, sw=3, rough=1)


def dashed_box(x, y, w, h, color, sw=3):
    """A dashed outline drawn as a closed polyline - the kit's rect() has no
    strokeStyle, and this reads as a hole rather than as a panel."""
    line(x, y, [[0, 0], [w, 0], [w, h], [0, h], [0, 0]], stroke=color, sw=sw,
         rough=1, dashed=True, prefix="hole")


def skill_card(x, y, w, h, title, body, title_size=H3, body_size=BODY, head_h=55):
    """The Skill object: white card, indigo rule, indigo header strip. Indigo is
    this board's constant for 'a Skill', so it never doubles as a beat accent."""
    rect(x, y, w, h, stroke=INDIGO, bg=WHITE, sw=3, rough=1, rounded=True, prefix="skc")
    rect(x, y, w, head_h, stroke="transparent", bg=INDIGO_BG, sw=1, rough=1,
         rounded=True, prefix="skch")
    text(x + 30, y + (head_h - title_size * LINE_H) / 2, title, size=title_size, color=INDIGO)
    if body:
        text(x + 30, y + head_h + 34, body, size=body_size, color=INK)

# ----------------------------------------------------------------------------
# THE WORKED EXAMPLE - one generic Skill, carried across beats 2, 4, 5 and 6 so
# the four beats tell one story: the procedure, the hole in it, Claude finding
# the hole, and the test that proves the fix. Deliberately everyday business
# (a monthly report), never Phlo-specific, with fictional figures.
# ----------------------------------------------------------------------------
SKILL_STEPS = ["pull last month's figures", "check the figures",
               "write it up in the house format", "flag anything over 10%"]

# ============================================================================
# BOARD TITLE
# ============================================================================
text(OX[1], -300, "Skills", size=HERO, color=INK)
text(OX[1] + 6, -300 + HERO * LINE_H + 4,
     "write the procedure down once, and stop retyping it", size=H2, color=ORANGE)

# ============================================================================
# BEAT 1 - YOU HAVE EXPLAINED THIS FOUR TIMES
# ============================================================================
ox = beat_head(1, "you have explained this four times",
               "The same correction, typed again, into a chat that has never heard it.")
CORRECTION = "no, British English -\nand no bullet points"
for k, day in enumerate(["Monday", "Tuesday", "Thursday", "Friday"]):
    mini_chat(ox + 40 + (k % 2) * 540, 310 + (k // 2) * 330, 500, 290, day,
              CORRECTION, ORANGE_BG)
chip(ox + 40, 960, "the fourth time is the signal",
     fill=ORANGE_BG, text_color=ORANGE, border=ORANGE, size=LABEL)

# ============================================================================
# BEAT 2 - PROCEDURE, NOT CONTEXT
# ============================================================================
ox = beat_head(2, "procedure, not context",
               "Two different jobs. People reach for the wrong one constantly.")
line(ox + 570, 360, [[0, 0], [0, 440]], stroke=GREY, sw=2, dashed=True)
# left: a Project folder holding background (violet - the repo-wide folder colour).
# Kept pale on purpose: reference material is passive, the Skill card is not.
text(ox + 60, 296, "A Project", size=H2, color=VIOLET)
rect(ox + 60, 360, 150, 30, stroke=VIOLET, bg=VIOLET_BG, sw=2, rough=1, rounded=True)
rect(ox + 60, 388, 460, 400, stroke=VIOLET, bg=VIOLET_T, sw=3, rough=1, rounded=True)
for k, lab in enumerate(["the tone guide", "last quarter's numbers", "the team glossary"]):
    ry = 430 + k * 115
    file_icon(ox + 95, ry, 58, 74, abg=VIOLET_BG)
    text(ox + 180, ry + 22, lab, size=SMALL, color=INK)
text(ox + 60, 806, "background it can look at", size=SMALL, color=GREY)
# right: a Skill holding numbered steps (indigo - this board's constant). This is
# THE example Skill; beats 4, 5 and 6 all work on these same four steps.
text(ox + 620, 296, "A Skill", size=H2, color=INDIGO)
skill_card(ox + 620, 360, 460, 428, "SKILL", None)
for k, step in enumerate(SKILL_STEPS):
    sy = 450 + k * 80
    text(ox + 650, sy, f"{k + 1}.", size=BODY, color=INDIGO)
    text(ox + 695, sy, step, size=BODY, color=INK)
text(ox + 620, 806, "a procedure it follows", size=SMALL, color=GREY)
# the caption on the divide
text_centered(ox + 560, 870, "context is what it knows, a Skill is what it does",
              size=H3, color=INK)
text(ox + 40, 940, "They stack: the Project holds the background, the Skill runs the procedure.",
     size=BODY, color=GREYD)

# ============================================================================
# BEAT 3 - SEARCH THE GALLERY FIRST  (+ the data caution)
# ============================================================================
ox = beat_head(3, "search the gallery first",
               "Before you write one, check whether somebody already has.")
SHELVES = [
    (292, 330, "already built in - just switch them on",
     [("Word", BLUE, BLUE_BG), ("Excel", GREEN, GREEN_BG),
      ("PowerPoint", ORANGE, ORANGE_BG), ("PDF", TEAL, TEAL_BG)]),
    (512, 550, "published by other teams, by your admins, and by partners",
     [("built by your team", INDIGO, INDIGO_BG), ("pushed by your org", INDIGO, INDIGO_BG),
      ("partner Skills", INDIGO, INDIGO_BG), ("+ many more", GREY, FAINT)]),
]
for lab_y, card_y, shelf_label, cards in SHELVES:
    text(ox + 40, lab_y, shelf_label, size=SMALL, color=GREY)
    for k, (label, accent, abg) in enumerate(cards):
        shelf_card(ox + 40 + k * 267, card_y, 220, 130, label, accent, abg)
    line(ox + 30, card_y + 138, [[0, 0], [1090, 0]], stroke=GREYD, sw=5)
    line(ox + 40, card_y + 150, [[0, 0], [1070, 0]], stroke=FAINT, sw=3)
chip(ox + 40, 730, "someone has already built this",
     fill=BLUE_BG, text_color=BLUE, border=BLUE, size=LABEL)
# the data caution - red, because a Skill is a shared file (safety-bearing: this
# is the only on-screen data-handling rule on the board)
highlighter(ox + 30, 816, 1090, 104, RED_BG, angle=0.0)
diamond(ox + 50, 832, 44, 44, stroke=RED, bg=RED_BG, sw=3)
text_centered(ox + 72, 836, "!", size=H3, color=RED)
text(ox + 120, 832, "A Skill is a shared file. Never put confidential or\nsensitive data inside one.",
     size=BODY, color=RED)

# ============================================================================
# BEAT 4 - THE HIDDEN ASSUMPTION
# ============================================================================
ox = beat_head(4, "the hidden assumption",
               "The step you know so well that you never wrote it down.")
text(ox + 40, 310, "1.", size=BODY, color=TEAL)
text(ox + 90, 310, SKILL_STEPS[0], size=BODY, color=INK)
# the gap where the unwritten step should be - a hole in the list, not a panel
dashed_box(ox + 40, 380, 620, 170, TEAL)
arrow(ox + 120, 352, [[0, 0], [28, 48], [74, 86]], stroke=GREY, sw=2, rough=1, dashed=True)
falling_person(ox + 230, 465, TEAL, tilt=0.7)
text(ox + 330, 468, "your colleague,\non their first go", size=SMALL, color=GREYD)
arrow(ox + 666, 462, [[0, 0], [26, -22]], stroke=TEAL, sw=2, rough=1, dashed=True)
text(ox + 700, 388, "the step you know\nand never wrote down", size=H3, color=TEAL)
sticky(ox + 700, 482, 380, 96, TEAL_BG, angle=jit_min(1.0, 2.2))
text(ox + 726, 502, "'and we always exclude\nthe trial accounts'", size=BODY, color=INK)
for k, step in enumerate(SKILL_STEPS[1:]):
    sy = 590 + k * 70
    text(ox + 40, sy, f"{k + 2}.", size=BODY, color=TEAL)
    text(ox + 90, sy, step, size=BODY, color=INK)
text(ox + 40, 810,
     "Write it for someone who has never done the job. If a step\nassumes something, say the something.",
     size=BODY, color=GREYD)
chip(ox + 40, 900, "read it back as if you were new",
     fill=TEAL_BG, text_color=TEAL, border=TEAL, size=LABEL)

# ============================================================================
# BEAT 5 - MAKE IT CRITIQUE ITS OWN STEPS  (absorbed prompt repair)
# ============================================================================
ox = beat_head(5, "make it critique its own steps",
               "Paste the Skill you wrote back to Claude and ask it to find the holes.")
text(ox + 40, 296, "you type this", size=SMALL, color=GREY)
sticky(ox + 40, 330, 1040, 170, RED_BG, angle=jit_min(0.8, 1.6))
text(ox + 80, 358,
     "Here is a Skill I wrote. Read it as if you had never\ndone this job. Which step is ambiguous? What would\na new starter get wrong?",
     size=BODY, color=INK)
arrow(ox + 130, 516, [[0, 0], [0, 88]], stroke=RED, sw=5, rough=1)
claude_face(ox + 130, 700, r=48, color=RED)
text_centered(ox + 130, 762, "Claude reads it back", size=SMALL, color=GREY)
arrow(ox + 195, 700, [[0, 0], [100, 0]], stroke=RED, sw=4, rough=1)
text(ox + 330, 570, "what comes back", size=SMALL, color=GREY)
for k, finding in enumerate(["step 1 says 'pull the figures' - all of them?",
                             "step 3 assumes I know what 'house format' means",
                             "there is no example of a finished report"]):
    fy = 616 + k * 84
    ellipse(ox + 330, fy + 4, 22, 22, stroke=RED, bg=RED_BG, sw=2)
    text(ox + 372, fy, finding, size=BODY, color=INK)
text(ox + 40, 862, "You are asking it to critique what you wrote - not to write it for you.",
     size=SMALL, color=GREYD)
demo_badge(ox + 40, 906,
           "show in Claude desktop app: ask Claude to find the ambiguous step in your own Skill")

# ============================================================================
# BEAT 6 - TEST ON A KNOWN INPUT
# ============================================================================
ox = beat_head(6, "test on a known input",
               "One input where you already know the right answer. Run it before the edit, and after.")

def test_row(ry, ver, step_txt, out_big, out_small, out_bg, out_accent, passed):
    sticky(ox + 40, ry, 240, 180, FAINT, angle=jit_min(0.8, 1.8))
    text(ox + 62, ry + 34, "the March report", size=SMALL, color=GREYD)
    text(ox + 62, ry + 66, "you already know:", size=SMALL, color=GREYD)
    text(ox + 62, ry + 100, "£4,180", size=H3, color=INK)
    arrow(ox + 292, ry + 90, [[0, 0], [40, 0]], stroke=GREY, sw=4, rough=1)
    skill_card(ox + 340, ry, 360, 180, ver, step_txt, title_size=LABEL, head_h=40)
    arrow(ox + 708, ry + 90, [[0, 0], [42, 0]], stroke=GREY, sw=4, rough=1)
    sticky(ox + 760, ry, 330, 180, out_bg, angle=jit_min(0.8, 1.8))
    text(ox + 786, ry + 34, out_big, size=H2, color=out_accent)
    text(ox + 786, ry + 96, out_small, size=BODY, color=INK)
    if passed:
        tick(ox + 1030, ry + 38, GREEN)
    else:
        xmark(ox + 1034, ry + 42, RED)

text(ox + 40, 292, "before the edit", size=SMALL, color=GREYD)
test_row(330, "SKILL  v1", "step 1: pull last\nmonth's figures",
         "£5,020", "it counted the trial\naccounts in", RED_BG, RED, passed=False)
text(ox + 40, 544, "after the edit", size=SMALL, color=GREEN)
test_row(582, "SKILL  v2", "step 1: pull last\nmonth's figures,\nexcluding trials",
         "£4,180", "right, first time -\nand every time", GREEN_BG, GREEN, passed=True)
text(ox + 40, 806,
     "Same input, both times. That is the whole test - and the only way\nyou know the edit actually worked.",
     size=BODY, color=GREYD)
chip(ox + 40, 898, "a Skill nobody else can run is a note to self",
     fill=GREEN_BG, text_color=GREEN, border=GREEN, size=LABEL)

# No connector spine, no inter-beat arrows and no footer: the six beats read as
# one picture through consistent shape and rhythm, and the whitespace is the camera.

# ----------------------------------------------------------------------------
# WRITE + VALIDATE  (shared excalidraw_kit; hard-fails on frames / off-palette)
# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "claude-skills.excalidraw")
MAXW = max(WID.values()) + 200
finish(out, MAXW, TOTAL_W)
