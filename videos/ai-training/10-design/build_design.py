#!/usr/bin/env python3
"""Build claude-design.excalidraw - ONE flowing, illustrated explainer for
DAY 10 of the Phlo AI training: "design work with Claude" (~6 min, hard cap 8).

Day 10 is the advanced beat of the series: by here a person can prompt (Day 3),
hold context (Day 4), write a procedure (Day 7) and supervise a long run (Day 8).
What is left is judgement - and in visual work the failure mode is not a bad
output, it is an acceptable one. It sits after Cowork deliberately: the habit it
teaches (name the test before you look) is the one that catches a plausible
result, which is exactly what a long unsupervised run produces.

WHAT THIS BOARD IS NOW (it was adapted, not extended)
-----------------------------------------------------
This board MOVED HERE from videos/claude/12-design/ (module 2.12) when the
day-by-day training became the authoritative series - the same move Day 4, Day 7
and Day 8 each made out of videos/claude/. videos/claude/ now has a fourth
numbering gap, at 12. A gap is not lost work.

This used to be a NINE-beat product walkthrough of Claude Design (Anthropic
Labs research preview): what it is, the design-system onboarding, start-from-
anything, the export targets, three role flows, the preview caveat. That board
taught a feature surface.

It is now a SEVEN-beat board about the practice, because the advanced failure in
design work is not a bad output - it is an acceptable one. Generic passes review.
The demo badge cuts to the Claude desktop app, not to a separate product, so
nothing on the board depends on plan tier or on a preview that may be renamed.

Per the repo precedence rule, a Day covers its topic IN FULL: this board does not
signpost the old module-2 walkthrough and must never be trimmed to a "see the
other video" pointer. There is no other video - 12-design is this one.

Everything displaced by the reframe - Labs / research-preview status, the model
and plan it runs on, design-system onboarding from a codebase, start-from-
anything inputs, PPTX / Canva export, the designer / PM / founder flows - is on
`claude-design-resource-card.md`. That card is a deliverable, not an afterthought:
do not re-inflate the board with it.

ONE THING MOVED RATHER THAN WENT. The old beat 8 carried the only on-screen
data-handling rule ("confidential designs, patient-facing material, or a private
codebase"). The seven-beat brief has no slot for it, but this is a mandatory
course for a regulated pharmacy, so it sits on beat 7 next to the human pass
instead of going to the card - the same call Day 7 made with its red Skill
caution. Do not quietly drop it in a later edit.

THE ADVERSARIAL BEAT (6) CARRIES ITS OWN CATCH. The failure is three outputs
that are all presentable and all interchangeable; the catch is naming the one
thing the design must get right BEFORE looking at it, then holding each output
against that. Failure without the catch is a diagnosis with no test, and the
catch is the half that has to travel - this beat is the Best Catch feeder.

Style B (house style): a single hand-drawn journey, left-to-right, NO frames, NO
boxes, white canvas, everything in the hand font (fontFamily 1), roughness 1, a
lively colour-coded Excalidraw palette, big colour blocking, scribbled
annotations and charming primitive illustrations. The look lives in the shared
excalidraw_kit; this file holds only the composition and the bespoke one-offs.

PAN ORDER (left to right - the whitespace between slots IS the camera; frame one
beat at a time):

     1  ORANGE  blank page to worth-reacting-to
     2  VIOLET  reference beats adjectives        <- 'clean and modern', struck through
     3  BLUE    structure versus polish
     4  TEAL    iterate by talking to it
     5  INDIGO  in units, not wholesale          <- 'regenerate is not iterate'
     6  RED     presentable is not correct       <- adversarial: the failure AND the catch
     7  GREEN   human pass for brand-final       <- [CUT TO CLAUDE DESKTOP], then the close

Beat 2 carries a one-line pointer to DAY 13 (videos/ai-training/13-design-md/), which
is the depth pass on design.md - the three prepared files that make this beat's habit
permanent. A forward pointer to another Day's topic, not a signpost standing in for this
board's own subject, so the precedence rule is intact. Day 13 never points back.

RUNTIME (budgeted in seconds, then MEASURED against the written narration - the
measuring is the step that matters, and the first draft of the script blew the cap):
     beats are not uniform. Measured at 150 wpm, from claude-design-script.md:
        b1 28s   b2 41s   b3 31s   b4 28s   b5 32s   b6 67s   b7 52s (+18s cut-away)
        hook 12s   why 29s   pause-and-try 18s   close 20s
     909 spoken words = ~6 min 16. Hard cap 8 minutes, target 4 to 6.
     Beat 6 is the longest on purpose; everything else was trimmed to pay for it.
     Shorter cut: drop beats 3 and 4 (~5 min). Never drop beat 6.

Run:  python3 videos/ai-training/10-design/build_design.py
      /usr/bin/python3 preview.py videos/ai-training/10-design/claude-design.excalidraw out.png
      /usr/bin/python3 preview.py <scene> out.png XMIN XMAX   # close-up on one beat
      python3 build_all.py            # rebuild all + Style-B guard
"""
import os
import sys

_d = os.path.dirname(os.path.abspath(__file__))
while _d != os.path.dirname(_d) and not os.path.exists(os.path.join(_d, "excalidraw_kit.py")):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)

import random
from excalidraw_kit import *

random.seed(121207)  # deterministic - re-runs produce identical files

# ----------------------------------------------------------------------------
# BEAT SCAFFOLD - seven beats, wide gaps so one frames cleanly on a 14" laptop
# ----------------------------------------------------------------------------
N = 7
GAP = 800
# every beat uses the SAME slot, shaped ~1.15:1 (content ~1120 wide x ~980 tall,
# the heading at y60 counted in) so framing is identical on a 14" laptop.
WID = {i: 1200 for i in range(1, N + 1)}
ACCENT = {1: ORANGE, 2: VIOLET, 3: BLUE, 4: TEAL, 5: INDIGO, 6: RED, 7: GREEN}
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
# BESPOKE ILLUSTRATIONS for this board (one-offs stay here, never in the kit)
# ----------------------------------------------------------------------------
def mockup(x, y, w, h, accent=VIOLET, abg=VIOLET_BG, shuffled=False, cards=2):
    """A polished UI mockup: header bar, hero block, two cards, a button.

    `shuffled=True` puts the SAME polished blocks in the wrong order (the
    button first, the header last) - the "beautiful, wrong structure" half of
    beat 3 and the regenerate on beat 5. `cards=0` drops the card row, so beat 5
    can show that a regenerate lost the one element that was already working."""
    hdr, hero, crd, btn = ((0.07, 0.25, 0.57, 0.85) if not shuffled
                           else (0.86, 0.52, 0.22, 0.07))
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="mock")
    rect(x + 0.08 * w, y + hdr * h, 0.84 * w, 0.12 * h, stroke="transparent",
         bg=accent, sw=1, rough=1, rounded=True, prefix="mh")
    rect(x + 0.08 * w, y + hero * h, 0.84 * w, 0.26 * h, stroke=GREYD, bg=abg, sw=2,
         rough=1, rounded=True, prefix="mhero")
    for k in range(cards):
        rect(x + (0.08 + 0.46 * k) * w, y + crd * h, 0.38 * w, 0.22 * h, stroke=GREYD,
             bg=WHITE, sw=2, rough=1, rounded=True, prefix="mc")
    rect(x + 0.08 * w, y + btn * h, 0.30 * w, 0.09 * h, stroke=accent, bg=accent, sw=1,
         rough=1, rounded=True, prefix="mbtn")


def wireframe(x, y, w, h):
    """The same screen in grey boxes: structure only, no colour, no polish. Grey
    and faint on purpose - it must read as unfinished and still be arguable."""
    rect(x, y, w, h, stroke=GREYD, bg=WHITE, sw=2, rough=1, rounded=True, prefix="wf")
    rect(x + 0.07 * w, y + 0.06 * h, 0.86 * w, 0.10 * h, stroke=GREY, bg=FAINT, sw=2,
         rough=1, rounded=True, prefix="wfb")
    rect(x + 0.07 * w, y + 0.20 * h, 0.86 * w, 0.26 * h, stroke=GREY, bg=WHITE, sw=2,
         rough=1, rounded=True, prefix="wfb")
    line(x + 0.07 * w, y + 0.20 * h, [[0, 0], [0.86 * w, 0.26 * h]], stroke=FAINT, sw=2)
    line(x + 0.07 * w, y + 0.46 * h, [[0, 0], [0.86 * w, -0.26 * h]], stroke=FAINT, sw=2)
    for k in range(2):  # two cards, matching mockup() - beat 3 is the SAME content twice
        rect(x + (0.07 + 0.46 * k) * w, y + 0.52 * h, 0.38 * w, 0.22 * h, stroke=GREY,
             bg=WHITE, sw=2, rough=1, rounded=True, prefix="wfb")
    rect(x + 0.07 * w, y + 0.80 * h, 0.34 * w, 0.10 * h, stroke=GREYD, bg=FAINT, sw=2,
         rough=1, rounded=True, prefix="wfb")


def struck(x, y, s, size=H2, color=GREYD, strike=VIOLET, sw=4):
    """Hand-struck text - the words, with a line drawn through them. The kit has
    no strikethrough, so this is a one-off: a text element plus a line across its
    middle. Struck in an accent so the crossing-out reads as a deliberate mark.

    0.44 of the line box, not 0.5: with lineHeight 1.4 the glyphs sit high in
    their box, so a line at the geometric middle crosses the descenders and reads
    as an underline that slipped."""
    e = text(x, y, s, size=size, color=color)
    w = text_w(s, size)
    line(x - 8, y + size * LINE_H * 0.44, [[0, 0], [w + 16, 0]], stroke=strike, sw=sw,
         rough=1, prefix="strike")
    return e


def reference_frame(x, y, w, h, accent=VIOLET, abg=VIOLET_BG):
    """A pasted reference: a bordered picture holding a rough layout, taped at both
    top corners - 'the thing you like', stuck to the brief. Tape rather than a
    paperclip: a clip drawn at this scale reads as a stray rectangle."""
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=3, rough=1, rounded=True, prefix="ref")
    rect(x + 24, y + 34, w - 48, 0.24 * h, stroke=GREYD, bg=abg, sw=2, rough=1,
         rounded=True, prefix="refh")
    line(x + 24, y + 0.37 * h, [[0, 0], [(w - 48) * 0.55, 0]], stroke=FAINT, sw=3)
    for k in range(3):
        rect(x + 24 + k * (w - 48) / 3, y + 0.44 * h, (w - 48) / 3 - 20, 0.34 * h,
             stroke=GREYD, bg=WHITE, sw=2, rough=1, rounded=True, prefix="refc")
    for tx, ta in ((x + 16, -0.45), (x + w - 90, 0.45)):
        rect(tx, y - 14, 74, 28, stroke=accent, bg=abg, sw=2, rough=1, rounded=False,
             fill="solid", angle=ta, opacity=75, prefix="tape")


def settings_panel(x, y, w, h):
    """The reflex a design tool trains: rows of sliders, a dropdown and a hex
    field. Drawn grey on purpose - it is the thing you are NOT reaching for."""
    rect(x, y, w, h, stroke=GREYD, bg=WHITE, sw=2, rough=1, rounded=True, prefix="pnl")
    text(x + 24, y + 16, "Properties", size=SMALL, color=GREY)
    line(x, y + 54, [[0, 0], [w, 0]], stroke=FAINT, sw=2)
    for k in range(3):
        sy = y + 92 + k * 62
        line(x + 24, sy, [[0, 0], [w - 100, 0]], stroke=GREY, sw=3)
        ellipse(x + 24 + (w - 100) * (0.28 + 0.22 * k), sy - 10, 20, 20, stroke=GREYD,
                bg=WHITE, sw=2)
    rect(x + 24, y + 286, w - 48, 44, stroke=GREY, bg=WHITE, sw=2, rough=1, rounded=True,
         prefix="pnlf")
    line(x + w - 76, y + 301, [[0, 0], [14, 16], [28, 0]], stroke=GREYD, sw=3)
    rect(x + 24, y + 338, w - 48, 44, stroke=GREY, bg=WHITE, sw=2, rough=1, rounded=True,
         prefix="pnlf")
    text(x + 42, y + 348, "#1e1e1e", size=SMALL, color=GREY)


def human_gate(cx, cy, color=GREEN, abg=GREEN_BG, s=1.0):
    """The human-in-loop marker for beat 7: a head plus rounded shoulders, filled.

    This is safety-bearing - SKILL.md requires the human decision point to be
    unmistakable - so it does not use the kit's person(), which is sized for a
    crowd of tiny figures and reads as a paper dart when it has to stand alone.
    Same reason Day 3 keeps its own person_big()."""
    r = 26 * s
    ellipse(cx - r, cy - 62 * s, 2 * r, 2 * r, stroke=color, bg=WHITE, sw=3, rough=1,
            prefix="hghead")
    line(cx - 50 * s, cy + 46 * s,
         [[0, 0], [0, -22 * s], [18 * s, -50 * s], [82 * s, -50 * s],
          [100 * s, -22 * s], [100 * s, 0]],
         stroke=color, sw=3, rough=1, bg=abg, fill="solid", prefix="hgbody")


# ----------------------------------------------------------------------------
# THE WORKED EXAMPLE - one generic landing page, carried across beats 1, 4, 5
# and 7 so the board tells a single story: the first draft you can argue with,
# the correction said in plain words, that one correction applied to one
# element and the three named iterations you ship. Deliberately everyday
# business (an internal tool's landing page), never Phlo-specific.
# ----------------------------------------------------------------------------
HEADER_FIX = "the header is fighting the hero -\nmake the header quieter"
NAMED_CHANGES = ["'the header is fighting the hero - make it quieter'",
                 "'move the price above the fold'",
                 "'three cards, not four - drop the last one'"]
# The criterion on beat 6 is the catch. It is one sentence, falsifiable by
# looking at the output, and written BEFORE the output is judged.
CRITERION = "'a first-time reader can see the price without scrolling'"

# ============================================================================
# BOARD TITLE
# ============================================================================
text(OX[1], -300, "Design with Claude", size=HERO, color=INK)
text(OX[1] + 6, -300 + HERO * LINE_H + 4,
     "get to something worth arguing with - then earn the finish", size=H2, color=ORANGE)

# ============================================================================
# BEAT 1 - BLANK PAGE TO WORTH-REACTING-TO
# ============================================================================
ox = beat_head(1, "blank page to worth-reacting-to",
               "The win is not a design you can ship. It is a design you can\nargue with - and arguing is the fast part.")
# left: the blank page, with nothing on it but a cursor
rect(ox + 50, 330, 300, 390, stroke=GREY, bg=WHITE, sw=2, rough=1, rounded=True)
line(ox + 200, 480, [[0, 0], [0, 76]], stroke=GREY, sw=4)
text(ox + 50, 740, "hour three of\nthe blank page", size=SMALL, color=GREY)
arrow(ox + 378, 520, [[0, 0], [104, 0]], stroke=ORANGE, sw=5, rough=1)
# right: ninety seconds of Claude, and suddenly you have opinions
mockup(ox + 510, 330, 320, 390, accent=ORANGE, abg=ORANGE_BG)
text(ox + 510, 740, "ninety seconds later", size=SMALL, color=GREY)
text(ox + 862, 296, "and now you have opinions", size=SMALL, color=GREY)
for k, note in enumerate(["the hero says\nnothing", "price should be\nhigher up",
                          "three cards,\nnot four"]):
    ny = 340 + k * 130
    sticky(ox + 862, ny, 250, 100, ORANGE_BG, angle=jit(2.0))
    text(ox + 886, ny + 24, note, size=SMALL, color=INK)
    arrow(ox + 852, ny + 48, [[0, 0], [-18, 0]], stroke=ORANGE, sw=3, rough=1)
text(ox + 50, 812,
     "A draft you disagree with tells you what you actually wanted.\nA blank page tells you nothing at all.",
     size=BODY, color=GREYD)
chip(ox + 50, 918, "get to something worth reacting to", fill=ORANGE_BG,
     text_color=ORANGE, border=ORANGE, size=LABEL)

# ============================================================================
# BEAT 2 - REFERENCE BEATS ADJECTIVES
# ============================================================================
ox = beat_head(2, "reference beats adjectives",
               "'Clean and modern' is a phrase you both think you understand.\nShow it the thing you like instead.")
# left: the adjective brief, struck through
text(ox + 50, 292, "what you typed", size=SMALL, color=GREY)
sticky(ox + 50, 326, 500, 208, VIOLET_T, angle=jit(1.4))
text(ox + 86, 352, "make the landing page", size=BODY, color=GREYD)
struck(ox + 86, 400, "clean and modern", size=H2, color=GREYD, strike=VIOLET)
xmark(ox + 88, 472, GREY, s=22)
text(ox + 130, 466, "two words, a hundred readings", size=SMALL, color=GREYD)
# right: the reference you paste instead
arrow(ox + 566, 420, [[0, 0], [44, 0]], stroke=VIOLET, sw=5, rough=1)
text(ox + 620, 292, "what to paste instead", size=SMALL, color=GREY)
reference_frame(ox + 620, 326, 460, 290)
text(ox + 620, 636, "the page you already like", size=BODY, color=VIOLET)
# the swap, spelled out: words it guesses at, against things it can look at
text(ox + 50, 700, "words it has to guess at", size=SMALL, color=GREY)
_sx = ox + 50
for word in ["clean", "modern", "professional", "on-brand"]:
    struck(_sx, 736, word, size=H3, color=GREYD, strike=VIOLET)
    _sx += text_w(word, H3) + 56
text(ox + 50, 812, "things it can actually look at", size=SMALL, color=GREY)
_cx = ox + 50
for lab in ["a screenshot", "a link", "last year's deck", "a page you like"]:
    _w, _h = chip(_cx, 846, lab, fill=WHITE, text_color=VIOLET, border=VIOLET, size=SMALL)
    _cx += _w + 24
text_centered(ox + 560, 936, "show it the thing you like", size=H3, color=VIOLET)
# the hand-off to Day 13: a design.md is this beat made permanent. A forward
# pointer to another Day's topic, which the precedence rule allows - it is not a
# signpost standing in for this board's own subject.
chip(ox + 320, 1000, "write the reference down once: Day 13, design.md", fill=WHITE,
     text_color=VIOLET, border=VIOLET, size=SMALL)

# ============================================================================
# BEAT 3 - STRUCTURE VERSUS POLISH
# ============================================================================
ox = beat_head(3, "structure versus polish",
               "The same content, twice. Polish laid over the wrong structure is\nthe most expensive work you can do.")
# left: grey boxes, right order
text(ox + 50, 292, "grey boxes, right order", size=H3, color=BLUE)
wireframe(ox + 50, 344, 460, 396)
tick(ox + 52, 768, GREEN)
text(ox + 98, 762, "you can settle this in a ten-minute\nconversation", size=SMALL, color=GREYD)
# right: beautiful, wrong order - the same blocks, shuffled
text(ox + 610, 292, "beautiful, wrong order", size=H3, color=BLUE)
mockup(ox + 610, 344, 460, 396, accent=BLUE, abg=BLUE_BG, shuffled=True)
xmark(ox + 612, 766, RED, s=22)
text(ox + 656, 762, "every fix from here is a redraw", size=SMALL, color=GREYD)
text(ox + 50, 836,
     "Settle the order of things while they are still cheap to move.\nPolish is the last pass, never the first.",
     size=BODY, color=GREYD)
chip(ox + 50, 940, "polish on bad structure is a redraw", fill=BLUE_BG,
     text_color=BLUE, border=BLUE, size=LABEL)

# ============================================================================
# BEAT 4 - ITERATE BY TALKING TO IT
# ============================================================================
ox = beat_head(4, "iterate by talking to it",
               "You already know what is wrong with it. Say that - in the words\nyou would use to a colleague.")
# left: the settings-panel instinct
text(ox + 50, 292, "the old instinct", size=SMALL, color=GREY)
settings_panel(ox + 50, 330, 420, 400)
xmark(ox + 52, 762, GREY, s=22)
text(ox + 96, 756, "hunting for the control\nthat does the thing", size=SMALL, color=GREYD)
# right: the correction, in plain language
text(ox + 560, 292, "what you say instead", size=SMALL, color=GREY)
sticky(ox + 560, 330, 520, 188, TEAL_BG, angle=jit(1.4))
text(ox + 596, 360, HEADER_FIX + ",\nand give the hero room\nto breathe", size=BODY, color=INK)
tick(ox + 562, 566, GREEN)
text(ox + 608, 560, "no panel, no hex codes,\nnothing to hunt for", size=SMALL, color=GREYD)
text(ox + 50, 836,
     "It is a conversation, not a control surface. Describe the problem,\nnot the setting you imagine would fix it.",
     size=BODY, color=GREYD)
chip(ox + 50, 940, "say what is wrong, in words", fill=TEAL_BG, text_color=TEAL,
     border=TEAL, size=LABEL)

# ============================================================================
# BEAT 5 - IN UNITS, NOT WHOLESALE
# ============================================================================
ox = beat_head(5, "in units, not wholesale",
               "Change one element at a time. A full regenerate throws away the\nparts that were already working.")
# the design you have, with the one element that was already right
text(ox + 50, 330, "what you have", size=SMALL, color=GREY)
mockup(ox + 50, 370, 280, 240, accent=INDIGO, abg=INDIGO_BG)
circle_around(ox + 64, 498, 126, 72, GREEN)
text(ox + 50, 630, "the pricing card was\nalready right", size=SMALL, color=GREYD)
text(ox + 50, 730,
     "Name the element,\nthen name the change.\n\nA regenerate is a fresh\nroll of the dice. It can\nlose what you had\nalready won.",
     size=BODY, color=GREYD)
# the fork: one element, or the lot
arrow(ox + 344, 450, [[0, 0], [128, -66]], stroke=INDIGO, sw=4, rough=1)
arrow(ox + 344, 534, [[0, 0], [128, 186]], stroke=GREYD, sw=4, rough=1, dashed=True)
# top branch - one element, named
text(ox + 500, 330, "change one thing", size=H3, color=INDIGO)
chip(ox + 500, 386, "'make the header quieter'", fill=WHITE, text_color=INDIGO,
     border=INDIGO, size=SMALL)
mockup(ox + 500, 452, 250, 210, accent=INDIGO, abg=INDIGO_BG)
circle_around(ox + 512, 458, 228, 44, INDIGO)
tick(ox + 790, 472, GREEN)
text(ox + 836, 466, "the header changed.\nNothing else did.", size=SMALL, color=GREYD)
chip(ox + 790, 690, "regenerate is not iterate", fill=INDIGO_BG, text_color=INDIGO,
     border=INDIGO, size=LABEL)
# bottom branch - start again, and lose the card
text(ox + 500, 700, "start again", size=H3, color=GREYD)
chip(ox + 500, 756, "'try another version'", fill=WHITE, text_color=GREYD,
     border=GREYD, size=SMALL)
mockup(ox + 500, 820, 250, 210, accent=INDIGO, abg=INDIGO_BG, shuffled=True, cards=0)
xmark(ox + 792, 842, RED, s=22)
text(ox + 836, 836, "different everywhere -\nand the card is gone", size=SMALL, color=GREYD)

# ============================================================================
# BEAT 6 - PRESENTABLE IS NOT CORRECT   (adversarial: the failure AND the catch)
# ============================================================================
ox = beat_head(6, "presentable is not correct",
               "Three outputs. All acceptable, all interchangeable, not one of them\nright - and you cannot tell by looking.")
# three near-identical outputs. NO jitter and one neutral colour: the sameness IS
# the point, and a tilt or a colour each would read as three real options.
for k, lab in enumerate(["version A", "version B", "version C"]):
    bx = ox + 50 + k * 370
    text(bx, 300, lab, size=SMALL, color=GREY)
    mockup(bx, 334, 300, 200, accent=GREY, abg=FAINT)
    text(bx, 552, "looks fine", size=BODY, color=GREYD)
# the catch - named before you look, so "it looks fine" cannot be the verdict
text(ox + 50, 616, "the catch", size=SMALL, color=RED)
text(ox + 50, 650, "name what it has to get right - before you look at it", size=H3, color=RED)
sticky(ox + 50, 706, 1040, 78, RED_T, angle=jit(1.0))
text(ox + 86, 727, CRITERION, size=BODY, color=INK)
for k in range(3):
    bx = ox + 50 + k * 370
    xmark(bx + 2, 830, RED, s=22)
    text(bx + 46, 824, "fails it", size=BODY, color=RED)
text(ox + 50, 886,
     "All three passed the eye test. All three fail the one test that\nmattered - and the test is the only thing you added.",
     size=BODY, color=GREYD)
chip(ox + 50, 968, "you will accept this if you are in a hurry", fill=RED_BG,
     text_color=RED, border=RED, size=LABEL)

# ============================================================================
# BEAT 7 - HUMAN PASS FOR BRAND-FINAL   (the cut-away, then the close)
# ============================================================================
ox = beat_head(7, "human pass for brand-final",
               "Claude gets you a strong draft, fast. A person owns what actually\ngoes out of the door.")
text(ox + 50, 292, "three iterations, each one named", size=SMALL, color=GREY)
for k, change in enumerate(NAMED_CHANGES):
    ry = 326 + k * 86
    num_badge(ox + 50, ry, k + 1, GREEN)
    text(ox + 112, ry + 4, change, size=BODY, color=INK)
# the human gate: Claude drafts, a person passes it, then it is brand-final
mockup(ox + 50, 570, 230, 165, accent=GREEN, abg=GREEN_BG)
arrow(ox + 296, 652, [[0, 0], [86, 0]], stroke=GREEN, sw=5, rough=1)
human_gate(ox + 470, 676, GREEN, GREEN_BG)
arrow(ox + 556, 652, [[0, 0], [86, 0]], stroke=GREEN, sw=5, rough=1)
mockup(ox + 680, 570, 230, 165, accent=GREEN, abg=GREEN_BG)
tick(ox + 942, 620, GREEN)
text(ox + 50, 748, "Claude's draft", size=SMALL, color=GREYD)
text_centered(ox + 470, 748, "you: the last pass", size=SMALL, color=GREEN)
text(ox + 680, 748, "brand-final", size=SMALL, color=GREEN)
# the data rule - red, because it is the only on-screen data-handling rule here
highlighter(ox + 40, 800, 1080, 96, RED_BG, angle=0.0)
diamond(ox + 56, 816, 44, 44, stroke=RED, bg=RED_BG, sw=3)
text_centered(ox + 78, 820, "!", size=H3, color=RED)
text(ox + 124, 816,
     "Nothing confidential goes in: no unapproved designs, no private\ncodebase, nothing patient-facing.",
     size=BODY, color=RED)
demo_badge(ox + 50, 908,
           "show in Claude desktop app: one design, three targeted iterations")
chip(ox + 50, 984, "nothing goes out without the human pass", fill=GREEN_BG,
     text_color=GREEN, border=GREEN, size=LABEL)

# No connector spine, no inter-beat arrows and no footer: the seven beats read as
# one picture through consistent shape and rhythm, and the whitespace is the camera.

# ----------------------------------------------------------------------------
# WRITE + VALIDATE  (shared excalidraw_kit; hard-fails on frames / off-palette)
# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "claude-design.excalidraw")
MAXW = max(WID.values()) + 200
finish(out, MAXW, TOTAL_W)
