#!/usr/bin/env python3
"""Build claude-training-recap.excalidraw - ONE flowing, illustrated explainer for
DAY 17 of the Phlo AI training: the course wrap-up (~6 min 30, hard cap 8).

WHAT THIS BOARD IS
------------------
The closing video for the day-by-day series. Commissioned 2026-09-18: recap
everything covered, congratulate people for finishing, and give next steps they
can actually implement. The "day 15" in the brief was about sequence, not the
slot, and the scope was confirmed with the user before authoring.

IT WAS BUILT AS DAY 16 AND RENUMBERED TO 17 MID-BUILD. Day 16 (Claude in
Microsoft Outlook) landed on main while this board was being drawn, so the recap
moved to the next free number AND - much more importantly - had to absorb the
day it had just been scooped by. A recap that omits a shipped video is wrong on
the day it is published. If another Day lands before this is recorded, CHECK
`videos/ai-training/` AGAINST `DAYS`, `CATCHES` AND `BUILT` BEFORE RECORDING.

It recaps the ELEVEN BUILT DAYS - 3, 4, 7, 8, 10, 11, 12, 13, 14, 15 and 16.
Days 1, 2, 5, 6 and 9 do not exist, and this board does NOT pretend they do or
paper over the gaps: it says "eleven videos", never "seventeen days". Beat 1's
badge row, beats 3 to 7, the script and the card all key off BUILT.

THE RECAP HAS A THESIS, AND IT IS NOT A LIST
---------------------------------------------
Reading the ten boards back to back, the adversarial beat is the same failure
every single time, wearing a different coat:

    Day 7  a Skill that omits the assumption you never said out loud
    Day 8  a long run whose small errors compound where you cannot see them
    Day 10 an acceptable design - generic passes review
    Day 11 a self-review that is not a second opinion
    Day 12 a tidy deck that argues nothing
    Day 13 a wrong rule saved into the design system, propagating silently
    Day 14 a fluent rewrite that drops the clause
    Day 15 an answer that is wrong although every row is right
    Day 16 a reply that is well written and commits you to something

THE DANGEROUS OUTPUT IS NEVER THE BAD ONE. IT IS THE ACCEPTABLE ONE. That is
beat 2, it is the red beat, and it is what makes this a wrap-up rather than a
contents page. Do not flatten it back into "here is what we covered".

Beat 2 also carries the single catch that is the PARENT of the other nine -
"name what it has to get right, before you look at it", which is Day 10's, and
which every later day is a specialisation of. Beat 7 then lists all eleven catches
as the take-away page.

EVERY CATCH ON BEAT 7 IS QUOTED OR NEAR-QUOTED FROM THE DAY'S OWN BOARD, not
paraphrased from memory. They were read back out of the .excalidraw files. If
you edit a day's catch, edit it here too - a recap that misquotes the course is
worse than no recap. The source line for each is in CATCHES below.

NO DEMO BADGE, DELIBERATELY. Every other Day has a live cut-away; this one has
nothing to demonstrate, because it teaches nothing new. The actionable beat is 8
("what to do this week"), and those are things the VIEWER does afterwards, not
things the presenter performs. Adding a cut-away here would pad a video whose
whole job is to be short.

BEAT 7 IS THE ONE WIDE SLOT (1600, not 1200): two columns of five catches is
inherently wide, and it is the page people will screenshot. Widened rather than
made taller, for the reason Day 14 and Day 15 both record - on a 16:10 laptop
height is what binds framing.

THE THREE OUTPUTS ON BEAT 2 CARRY NO JITTER AND ONE NEUTRAL GREY. The sameness
IS the point: a tilt or a colour each would read as three real options rather
than three interchangeable ones. Day 10's beat 6 and Day 12's beat 6 record the
identical exception to the house jitter rule - do not "fix" any of the three.

GREEN = the human pass, held from Days 10, 11, 13, 14 and 15. Beat 9's gate is
green, and so is the beat, which is the one place on the board where those
coincide.

THE RED RULE GETS THE LAST WORD (beat 9). Every day in the series carried an
on-screen data rule; this is a mandatory course for a regulated pharmacy, so the
closing board restates it rather than assuming ten previous mentions stuck.

PAN ORDER (left to right - the whitespace between slots IS the camera):

     1  GREEN   you got to the end            <- the congratulation
     2  RED     one failure, eleven times     <- the thesis, and the parent catch
     3  VIOLET  the foundations               <- Days 3, 4
     4  BLUE    making it repeatable          <- Days 7, 8
     5  TEAL    the design days               <- Days 10, 11, 13
     6  INDIGO  the documents you already have <- Days 12, 14, 15, 16
     7  ORANGE  your eleven catches           <- the take-away page. 1600 wide.
     8  YELLOW  what to do this week          <- next steps, pick one
     9  GREEN   and after that                <- ninety days, the red rule, close

RUNTIME: budget in seconds, then MEASURE the written prose (wc -w). This repo's
recorded lesson is that per-beat budgets drift by up to 2x, and it has bitten on
Day 10, Day 14 and Day 15. Target ~6 min 30 at ~150 wpm, which is ~975 words.
MEASURE IT BEFORE CALLING IT DONE - the command is in the script header.

Run:  python3 videos/ai-training/17-recap/build_recap.py
      python3 preview.py videos/ai-training/17-recap/claude-training-recap.excalidraw out.png
"""
import os
import sys

_d = os.path.dirname(os.path.abspath(__file__))
while _d != os.path.dirname(_d) and not os.path.exists(os.path.join(_d, "excalidraw_kit.py")):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)

import random
from excalidraw_kit import *

random.seed(160916)

# ----------------------------------------------------------------------------
# THE COURSE, AS BUILT. Ten days exist; 1, 2, 5, 6 and 9 do not.
# Each takeaway is the day's own argument, not a summary of its features.
# ----------------------------------------------------------------------------
DAYS = {
    3:  ("Prompting, and CRISPE",
         "Name the thing you want. Six dials: Context, Role,\nInstructions, Style, Parameters, Example."),
    4:  ("Claude Projects",
         "Write the brief once. Every chat after it starts\nbriefed, instead of you retyping the background."),
    7:  ("Skills",
         "Procedure, not context. Write the steps down once,\nthen test the Skill on a known input."),
    8:  ("Cowork",
         "The brief is the whole job. Name the checkpoints\nbefore the run starts, not after it surprises you."),
    10: ("Design work with Claude",
         "Generic passes review. Name what it has to get right\nbefore you look at it."),
    11: ("Claude Design, job by job",
         "One six-step loop - then make it draw the states it\nnever drew: empty, refused, far too many."),
    13: ("design.md",
         "Three files before you prompt. Everything compounds,\nincluding the rule you got wrong."),
    12: ("Claude in PowerPoint",
         "Structure first, slides second. One line per slide,\nand it has to state a position."),
    14: ("Claude in Word and PowerPoint",
         "Review as a diff. Revise, do not rewrite - a rewrite\nquietly drops the clause you needed."),
    15: ("Claude in Excel",
         "Every row can be right and the answer still wrong.\nReconcile it a second, independent way."),
    16: ("Claude in Outlook",
         "This one leaves the building. Read only the sentences\nthat commit you - a date, a number, an obligation."),
}

# The take-away page. EVERY LINE IS QUOTED OR NEAR-QUOTED FROM THAT DAY'S BOARD -
# they were read back out of the .excalidraw files, not written from memory.
CATCHES = [
    (3,  "name the thing you want"),                        # 3: "Name the thing you want."
    (4,  "write the brief once, in a Project"),             # 4: "every chat starts briefed"
    (7,  "test it on a known input"),                       # 7: "test on a known input"
    (8,  "name the checkpoints before the run"),            # 8: "Name them in the brief before the run starts"
    (10, "name what it has to get right, first"),           # 10: "name what it has to get right - before you look at it"
    (11, "make it draw the states it never drew"),          # 11: "make it draw the states it never drew"
    (12, "read only the headlines, in order"),              # 12: "read only the headlines, in order"
    (13, "re-render a reference design after each change"),  # 13: "keep one reference design - re-render it after every change"
    (14, "read the change as a diff"),                      # 14: "review as a diff"
    (15, "reconcile a second, independent way"),            # 15: "reconcile, do not spot-check"
    (16, "read only the sentences that commit you"),      # 16: "Read only the sentences that contain a commitment"
]
BUILT = [3, 4, 7, 8, 10, 11, 12, 13, 14, 15, 16]
assert sorted(DAYS) == BUILT and [d for d, _ in CATCHES] == BUILT
assert len(CATCHES) == 11

# ----------------------------------------------------------------------------
# BEAT SCAFFOLD  (9 beats, uniform 1200 slots except the wide take-away page)
# ----------------------------------------------------------------------------
N = 9
GAP = 800
WID = {i: 1200 for i in range(1, N + 1)}
WID[7] = 1600                                  # the take-away page - see docstring
ACCENT = {1: GREEN, 2: RED, 3: VIOLET, 4: BLUE, 5: TEAL,
          6: INDIGO, 7: ORANGE, 8: YELLOW, 9: GREEN}
OX = {}
_c = 0
for _i in range(1, N + 1):
    OX[_i] = _c
    _c += WID[_i] + GAP
TOTAL_W = _c
HEAD_Y = 60
MAX_TEXT_W = 1400


def beat_head(i, title, sub=None):
    ox = OX[i]
    heading(ox, HEAD_Y, title, color=ACCENT[i], sub=sub)
    return ox


# ----------------------------------------------------------------------------
# LOCAL ONE-OFF ILLUSTRATIONS
# ----------------------------------------------------------------------------
def day_card(x, y, w, n, accent, h=190):
    """One day of the course: numbered badge, its title, its argument in two lines."""
    title, takeaway = DAYS[n]
    sticky(x, y, w, h, TINT[accent], angle=jit(0.7))
    num_badge(x + 30, y + 28, n, accent, d=52)
    text(x + 108, y + 32, title, size=H3, color=accent)
    text(x + 108, y + 84, takeaway, size=BODY, color=INK)


def out_deck(x, y):
    """A tidy deck that argues nothing."""
    rect(x, y, 200, 130, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="od")
    line(x + 20, y + 30, [[0, 0], [110, 0]], stroke=GREY, sw=4)
    for k in range(3):
        line(x + 20, y + 62 + k * 22, [[0, 0], [160, 0]], stroke=FAINT, sw=3)


def out_layout(x, y):
    """A clean layout that says nothing."""
    rect(x, y, 200, 130, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="ol")
    rect(x, y, 200, 26, stroke="transparent", bg=FAINT, sw=1, rough=1, rounded=True, prefix="olh")
    for k in range(2):
        rect(x + 18 + k * 92, y + 44, 74, 62, stroke=GREY, bg=WHITE, sw=2, rough=1, rounded=True, prefix="olb")


def out_number(x, y):
    """A plausible figure that checks out."""
    rect(x, y, 200, 130, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="on")
    for c in range(1, 3):
        line(x + c * 66, y, [[0, 0], [0, 130]], stroke=FAINT, sw=1)
    for r in range(1, 4):
        line(x, y + r * 32, [[0, 0], [200, 0]], stroke=FAINT, sw=1)
    text(x + 78, y + 70, "18.33", size=SMALL, color=GREYD)


def human_gate(cx, cy, color=GREEN):
    """The human pass. Deliberately unmistakable - the kit's person() is sized for
    a crowd and reads as a paper dart standing alone (Day 10 and Day 15 record it)."""
    ellipse(cx - 21, cy - 79, 42, 42, stroke=color, bg=WHITE, sw=4, rough=1)
    line(cx - 42, cy + 14, [[0, 0], [0, -14], [10, -30], [26, -38], [42, -40],
                            [58, -38], [74, -30], [84, -14], [84, 0]],
         stroke=color, sw=4, rough=1)


# ============================================================================
# BOARD TITLE
# ============================================================================
text(OX[1], -300, "That's the course", size=HERO, color=INK)
text(OX[1] + 6, -300 + HERO * LINE_H + 4,
     "eleven days, one habit, and what to do on Monday", size=H2, color=GREEN)

# ============================================================================
# BEAT 1 - GREEN - you got to the end
# ============================================================================
ox = beat_head(1, "you got to the end",
               "eleven videos, one habit, and a team that now\n"
               "argues with its tools")

for k, n in enumerate(BUILT):
    num_badge(ox + 40 + k * 96, 340, n, GREEN, d=64)

text(ox + 40, 452, "Eleven videos. Every one of them finished.", size=H2, color=GREEN)
text(ox + 40, 532,
     "That is not nothing. This was a mandatory course about a tool that changes every few\n"
     "months, and you sat through the awkward part - the one where you change how you work\n"
     "rather than watch somebody else do it.",
     size=BODY, color=GREYD)
text(ox + 40, 668, "Well done. Genuinely.", size=H2, color=INK)
text(ox + 40, 748,
     "What follows is the whole thing in six minutes: what you covered, the one idea\n"
     "underneath all of it, and three things to do this week.",
     size=BODY, color=GREYD)
chip(ox + 40, 860, "eleven days, one habit", fill=GREEN_T, text_color=GREEN, border=GREEN)

# ============================================================================
# BEAT 2 - RED - one failure, ten times   *** the thesis, and the parent catch ***
# The three outputs carry NO jitter and one neutral grey. The sameness is the point.
# ============================================================================
ox = beat_head(2, "one failure, eleven times",
               "every day in this course was pointed at the same\n"
               "thing - and it is not a bad output")

outs = [(out_deck, "a tidy deck", "argues nothing"),
        (out_layout, "a clean layout", "says nothing"),
        (out_number, "a plausible figure", "every cell checks out")]
for k, (glyph, lab, cap) in enumerate(outs):
    gx = ox + 40 + k * 370
    rect(gx, 336, 340, 210, stroke=GREY, bg=WHITE, sw=2, rough=1, rounded=True,
         angle=0.0, prefix="outc")
    glyph(gx + 70, 376)
    text(gx, 572, lab, size=H3, color=GREYD)
    text(gx, 620, cap, size=SMALL, color=GREY)

text(ox + 40, 690, "not wrong enough to notice", size=H2, color=RED)
text(ox + 40, 762,
     "Nobody here was ever going to ship something obviously broken - you would have\n"
     "caught that. What gets through is the output that is well-made, plausible and\n"
     "empty. It gets through because a review checks whether it looks right.",
     size=BODY, color=GREYD)

sticky(ox + 40, 880, 1080, 130, RED_T, angle=jit(0.6))
text(ox + 72, 902, "one move, and the other ten are all versions of it", size=SMALL, color=RED)
text(ox + 72, 940, "Name what it has to get right - before you look at it.", size=H3, color=INK)

# ============================================================================
# BEAT 3 - VIOLET - the foundations  (Days 3, 4)
# ============================================================================
ox = beat_head(3, "the foundations",
               "days three and four - saying what you want,\n"
               "and only having to say it once")
day_card(ox + 40, 340, 1080, 3, VIOLET)
day_card(ox + 40, 570, 1080, 4, VIOLET)
text(ox + 40, 820,
     "Day 3 teaches one good prompt. Day 4 is how you stop typing it again tomorrow.",
     size=BODY, color=VIOLET)
text(ox + 40, 880,
     "If nothing else from this course survives, let it be these two. Everything after\n"
     "them assumes the context is already in the room.",
     size=BODY, color=GREYD)

# ============================================================================
# BEAT 4 - BLUE - making it repeatable  (Days 7, 8)
# ============================================================================
ox = beat_head(4, "making it repeatable",
               "days seven and eight - the procedure, and the\n"
               "run you are not watching")
day_card(ox + 40, 340, 1080, 7, BLUE)
day_card(ox + 40, 570, 1080, 8, BLUE)
text(ox + 40, 820,
     "A Skill is what you should have written before you handed the job to Cowork.",
     size=BODY, color=BLUE)
text(ox + 40, 880,
     "Most of what people bring to a long unsupervised run should have been six lines\n"
     "of procedure and a known input to test it against.",
     size=BODY, color=GREYD)

# ============================================================================
# BEAT 5 - TEAL - the design days  (Days 10, 11, 13)
# ============================================================================
ox = beat_head(5, "the design days",
               "ten, eleven and thirteen - the judgement, the jobs,\n"
               "and the file that makes both permanent")
for k, n in enumerate([10, 11, 13]):
    day_card(ox + 40, 330 + k * 186, 1080, n, TEAL, h=170)
text(ox + 40, 906,
     "Day 10 is the argument, Day 11 is the work, and Day 13 is the plumbing that stops\n"
     "the argument having to be made twice.",
     size=BODY, color=TEAL)

# ============================================================================
# BEAT 6 - INDIGO - the documents you already have  (Days 12, 14, 15)
# ============================================================================
ox = beat_head(6, "the documents you already have",
               "twelve, fourteen, fifteen and sixteen -\n"
               "where the work actually lives")
for k, n in enumerate([12, 14, 15, 16]):
    day_card(ox + 40, 330 + k * 160, 1080, n, INDIGO, h=150)
text(ox + 40, 980,
     "Same failure, four surfaces - and all four pass a review that looks at the surface.",
     size=BODY, color=INDIGO)

# ============================================================================
# BEAT 7 - ORANGE - your eleven catches  (the take-away page, 1600 wide)
# ============================================================================
ox = beat_head(7, "your eleven catches",
               "one sentence from each day. this is the page to\n"
               "screenshot and keep.")
for k, (n, catch) in enumerate(CATCHES):
    col, row = (0, k) if k < 6 else (1, k - 6)
    cx = ox + 50 + col * 790
    cy = 340 + row * 104
    num_badge(cx, cy, n, ORANGE, d=48)
    text(cx + 68, cy + 10, catch, size=LABEL, color=INK)

text(ox + 50, 950,
     "Eleven days, eleven catches, one shape: name the test before you look at the output.",
     size=BODY, color=ORANGE)

# ============================================================================
# BEAT 8 - YELLOW - what to do this week
# ============================================================================
ox = beat_head(8, "what to do this week",
               "three things. not all three at once -\n"
               "pick the one that matches your week.")

STEPS = [("Build one Project for the job you do most.",
          "Twenty minutes. Day 4 walks the whole thing."),
         ("Turn your most-repeated explanation into one Skill.",
          "Then test it on a known input, and see what it missed."),
         ("Take something you shipped and name the test it should have passed.",
          "Then run that test on it. That is the course, in five minutes.")]
for k, (head, sub) in enumerate(STEPS):
    sy = 340 + k * 160
    sticky(ox + 40, sy, 1080, 140, YELLOW_T, angle=jit(0.7))
    num_badge(ox + 72, sy + 28, k + 1, YELLOW, d=52)
    text(ox + 150, sy + 28, head, size=H3, color=INK)
    text(ox + 150, sy + 80, sub, size=BODY, color=GREYD)

chip(ox + 40, 840, "one of them. not all three.",
     fill=YELLOW_T, text_color=YELLOW, border=YELLOW)
text(ox + 40, 920,
     "If you only do one, do the first. Everything else here gets easier once the\n"
     "context stops being something you retype.",
     size=BODY, color=GREYD)

# ============================================================================
# BEAT 9 - GREEN - and after that  (ninety days, the red rule, the close)
# ============================================================================
ox = beat_head(9, "and after that",
               "what good looks like in ninety days")

for k, s in enumerate(["you stop retyping context, because it lives in a Project",
                       "you name the test before you look at the output",
                       "“it looks fine” stops counting as a review"]):
    check_item(ox + 40, 330 + k * 56, s, accent=GREEN)

human_gate(ox + 120, 660, GREEN)
text(ox + 230, 586, "and you still sign it off", size=H3, color=GREEN)
text(ox + 230, 636,
     "Claude drafts. A person approves. The record updates.\nThat did not change, and it is not going to.",
     size=BODY, color=GREYD)

rect(ox + 40, 750, 1080, 152, stroke=RED, bg=RED_T, sw=2, rough=1, rounded=True, prefix="rule")
text(ox + 72, 772, "the one rule that outlives the course", size=H3, color=RED)
text(ox + 72, 822,
     "No patient data, no confidential data, and nothing you would not put in an email\n"
     "to somebody outside Phlo. That holds whichever tool you are using.",
     size=BODY, color=INK)

text(ox + 40, 932, "Eleven days. One habit. Name the test before you look.", size=H2, color=INK)

# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "claude-training-recap.excalidraw")
finish(out, MAX_TEXT_W, TOTAL_W)
