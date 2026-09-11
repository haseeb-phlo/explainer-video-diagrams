#!/usr/bin/env python3
"""Build claude-design-md.excalidraw - ONE flowing, illustrated explainer for
DAY 11 of the Phlo AI training: "design.md" (~7 min, hard cap 8).

Day 11 is the depth pass on the three files Day 10 only points at. Day 10 teaches
the judgement (reference beats adjectives, presentable is not correct, the human
pass). Day 11 teaches the plumbing that makes that judgement permanent: a
design.md, the design system built from it, and the template built from that -
prepared BEFORE you prompt, so the first output is already close and every
correction afterwards compounds.

Day 10 mentions design.md on its beat 2 and hands off here. This board covers the
topic in full per the repo precedence rule and never points back.

THREE OBJECT COLOURS ARE HELD CONSTANT across beats 2-7 - each is the accent of
the beat that introduces it, which makes them mnemonic rather than decorative:
  BLUE  = the design.md file       (introduced on beat 3)
  GREEN = the design system        (introduced on beat 4)
  TEAL  = the template             (introduced on beat 5)
GREEN doubles as the human pass on beat 8, held deliberately from Day 10's
closing beat - the two boards share that one colour so the rule reads as the same
rule. Don't re-map any of the four.

SOURCED FROM a third-party tutorial transcript; `claude-design-md-prompt.md`
records what was taken and what was deliberately left out. ONE DEPARTURE FROM THE
SOURCE, and it is not negotiable: the source downloads a real brand's design.md
from a public repository, has another model "remove the proprietary content and
replace it using your own judgment", renames it, and feeds that in - explicitly
because Claude will not reproduce a real brand's guidelines. That is routing
around a refusal and it is off this board. What survives is the mechanism (start
from a reference design.md, not a blank one) plus the red rule on beat 3: the
refusal is correct behaviour, and if you cannot say where a colour came from it
is not yours. Do not put the laundering step back.

THE ADVERSARIAL BEAT IS 7, and it is NOT the brand question - that failure is
loud, because Claude refuses. The silent failure of this capability is that a
wrong rule saved into the design system, or bad feedback captured into the
project's CLAUDE.md, propagates to every future design with nothing on screen to
say so. The catch is a regression check: keep one reference design and re-render
it after every change to the system. That is Day 7's "test on a known input",
applied to a design system.

Style B (house style): a single hand-drawn journey, left-to-right, NO frames, NO
boxes, white canvas, everything in the hand font (fontFamily 1), roughness 1, a
lively colour-coded Excalidraw palette, big colour blocking, scribbled
annotations and charming primitive illustrations. The look lives in the shared
excalidraw_kit; this file holds only the composition and the bespoke one-offs.

PAN ORDER (left to right - the whitespace between slots IS the camera; frame one
beat at a time):

     1  ORANGE  start in the wrong place
     2  VIOLET  three files, before you prompt          <- the map of the whole day
     3  BLUE    design.md is the rulebook               <- input 1, + the red rule
     4  GREEN   the design system makes it native       <- input 2
     5  TEAL    the template is the layout              <- input 3
     6  INDIGO  two kinds of feedback                   <- [CUT TO CLAUDE DESIGN]
     7  RED     everything compounds, mistakes too      <- adversarial: failure AND catch
     8  YELLOW  then it leaves the room                 <- export, then the human pass

Run:  python3 videos/ai-training/11-design-md/build_design_md.py
      /usr/bin/python3 preview.py videos/ai-training/11-design-md/claude-design-md.excalidraw out.png
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

random.seed(111108)  # deterministic - re-runs produce identical files

# ----------------------------------------------------------------------------
# BEAT SCAFFOLD - eight beats, wide gaps so one frames cleanly on a 14" laptop
# ----------------------------------------------------------------------------
N = 8
GAP = 800
WID = {i: 1200 for i in range(1, N + 1)}
ACCENT = {1: ORANGE, 2: VIOLET, 3: BLUE, 4: GREEN, 5: TEAL,
          6: INDIGO, 7: RED, 8: YELLOW}
OX = {}
_c = 0
for _i in range(1, N + 1):
    OX[_i] = _c
    _c += WID[_i] + GAP
TOTAL_W = _c

HEAD_Y = 60

# the three prepared files, held constant wherever they appear
MD, SYS, TPL = BLUE, GREEN, TEAL
MD_BG, SYS_BG, TPL_BG = BLUE_BG, GREEN_BG, TEAL_BG
MD_T, SYS_T, TPL_T = BLUE_T, GREEN_T, TEAL_T


def beat_head(i, title, sub=None):
    ox = OX[i]
    heading(ox, HEAD_Y, title, color=ACCENT[i], sub=sub)
    return ox


# ----------------------------------------------------------------------------
# BESPOKE ILLUSTRATIONS for this board (one-offs stay here, never in the kit)
# ----------------------------------------------------------------------------
def md_file(x, y, w, h, accent=MD, abg=MD_BG, label="design.md", rules=None):
    """A markdown rulebook: titled card, then the rules as swatch + text rows.
    This is the design.md object, so it is always drawn in MD (blue)."""
    rect(x, y, w, h, stroke=accent, bg=WHITE, sw=3, rough=1, rounded=True, prefix="mdf")
    rect(x, y, w, 46, stroke="transparent", bg=abg, sw=1, rough=1, rounded=True, prefix="mdfh")
    text(x + 22, y + 10, label, size=LABEL, color=accent)
    for k, (swatch, txt) in enumerate(rules or []):
        ry = y + 74 + k * 52
        if swatch is not None:
            rect(x + 22, ry, 30, 30, stroke=swatch, bg=swatch, sw=2, rough=1, rounded=True,
                 prefix="mdsw")
            text(x + 66, ry + 2, txt, size=SMALL, color=INK)
        else:
            text(x + 22, ry + 2, txt, size=SMALL, color=GREYD)


def swatch_strip(x, y, cols, sw_=44, gap=14):
    """A row of palette swatches - the visible half of a design system."""
    for k, (c, cbg) in enumerate(cols):
        rect(x + k * (sw_ + gap), y, sw_, sw_, stroke=c, bg=cbg, sw=2, rough=1,
             rounded=True, prefix="swt")
    return x + len(cols) * (sw_ + gap)


def slide_thumb(x, y, w, h, accent, abg, kind="content", generic=False):
    """One slide. `kind` picks the layout so a template row reads as a sequence
    rather than four copies; `generic=True` drains the colour, which is how the
    unprepared output on beat 1 and the interchangeable decks on beat 7 read."""
    st, bg = (GREY, FAINT) if generic else (accent, abg)
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="sld")
    if kind == "title":
        rect(x + 0.10 * w, y + 0.30 * h, 0.62 * w, 0.16 * h, stroke="transparent", bg=st,
             sw=1, rough=1, rounded=True, prefix="sb")
        rect(x + 0.10 * w, y + 0.54 * h, 0.40 * w, 0.09 * h, stroke="transparent", bg=bg,
             sw=1, rough=1, rounded=True, prefix="sb")
    elif kind == "section":
        rect(x + 0.10 * w, y + 0.12 * h, 0.80 * w, 0.76 * h, stroke=GREYD, bg=bg, sw=2,
             rough=1, rounded=True, prefix="sb")
        rect(x + 0.22 * w, y + 0.42 * h, 0.40 * w, 0.14 * h, stroke="transparent", bg=st,
             sw=1, rough=1, rounded=True, prefix="sb")
    elif kind == "two-col":
        rect(x + 0.08 * w, y + 0.12 * h, 0.84 * w, 0.12 * h, stroke="transparent", bg=st,
             sw=1, rough=1, rounded=True, prefix="sb")
        for c in range(2):
            rect(x + (0.08 + 0.46 * c) * w, y + 0.32 * h, 0.38 * w, 0.52 * h, stroke=GREYD,
                 bg=WHITE, sw=2, rough=1, rounded=True, prefix="sb")
    else:  # content
        rect(x + 0.08 * w, y + 0.12 * h, 0.60 * w, 0.12 * h, stroke="transparent", bg=st,
             sw=1, rough=1, rounded=True, prefix="sb")
        rect(x + 0.08 * w, y + 0.32 * h, 0.84 * w, 0.30 * h, stroke=GREYD, bg=bg, sw=2,
             rough=1, rounded=True, prefix="sb")
        for k in range(2):
            line(x + 0.08 * w, y + (0.72 + 0.10 * k) * h, [[0, 0], [0.66 * w, 0]],
                 stroke=FAINT, sw=2)


def deck(x, y, w, h, accent, abg, generic=False, n=3):
    """A stack of slides - a deck rather than a single slide."""
    for k in range(n - 1, 0, -1):
        rect(x + k * 14, y + k * 12, w, h, stroke=GREY, bg=WHITE, sw=2, rough=1,
             rounded=True, prefix="dk")
    slide_thumb(x, y, w, h, accent, abg, kind="content", generic=generic)


def toggle(x, y, label, on, accent=INDIGO):
    """A tweaks switch: the track, the knob, the label."""
    rect(x, y, 74, 34, stroke=accent, bg=(accent if on else WHITE), sw=2, rough=1,
         rounded=True, prefix="tgl")
    ellipse(x + (44 if on else 4), y + 4, 26, 26, stroke=accent, bg=WHITE, sw=2, rough=1,
            prefix="tglk")
    text(x + 90, y + 4, label, size=SMALL, color=INK)


def human_gate(cx, cy, color=GREEN, abg=GREEN_BG, s=1.0):
    """The human-in-loop marker - head plus rounded shoulders, filled. Not the
    kit's person(), which is sized for a crowd and reads as a paper dart alone;
    this marker is safety-bearing so it has to be unmistakable. Same helper and
    same green as Day 10's closing beat, on purpose."""
    r = 26 * s
    ellipse(cx - r, cy - 62 * s, 2 * r, 2 * r, stroke=color, bg=WHITE, sw=3, rough=1,
            prefix="hghead")
    line(cx - 50 * s, cy + 46 * s,
         [[0, 0], [0, -22 * s], [18 * s, -50 * s], [82 * s, -50 * s],
          [100 * s, -22 * s], [100 * s, 0]],
         stroke=color, sw=3, rough=1, bg=abg, fill="solid", prefix="hgbody")


# ----------------------------------------------------------------------------
# THE WORKED EXAMPLE - one generic internal workshop deck, carried across beats
# 1, 6, 7 and 8. Everyday business, never Phlo-specific, no patient or clinical
# detail. The one rule that goes wrong on beat 7 (tiny grey eyebrow labels) is
# the same element the good feedback fixes on beat 6, so the two beats are one
# story: the correction that compounds, and the correction that compounds wrongly.
# ----------------------------------------------------------------------------
GOOD_FEEDBACK = "make the eyebrow labels more prominent -\nput them in a container"
BAD_RULE = "eyebrow labels: 11px, grey"
REFERENCE = "'the workshop cover slide' - you already know what it should look like"

# ============================================================================
# BOARD TITLE
# ============================================================================
text(OX[1], -300, "design.md", size=HERO, color=INK)
text(OX[1] + 6, -300 + HERO * LINE_H + 4,
     "three files before you prompt - then every fix you make carries forward",
     size=H2, color=ORANGE)

# ============================================================================
# BEAT 1 - MOST TUTORIALS START YOU IN THE WRONG PLACE
# ============================================================================
ox = beat_head(1, "start in the wrong place",
               "Pick a template, name it, start prompting. You get something generic -\nand then you spend longer rescuing it than preparing would have taken.")
text(ox + 50, 296, "the usual advice", size=SMALL, color=GREY)
sticky(ox + 50, 330, 460, 120, ORANGE_BG, angle=jit(1.4))
text(ox + 82, 358, "pick a template, name it,\nstart prompting", size=BODY, color=INK)
arrow(ox + 528, 384, [[0, 0], [78, 0]], stroke=ORANGE, sw=5, rough=1)
deck(ox + 640, 320, 270, 210, ORANGE, ORANGE_BG, generic=True)
text(ox + 640, 570, "generic, and not yours", size=SMALL, color=GREYD)
# so you try again, and again, and pay for each one
text(ox + 50, 620, "so you try again", size=SMALL, color=GREY)
for k, ver in enumerate(["v1", "v2", "v3"]):
    bx = ox + 50 + k * 232
    slide_thumb(bx, 656, 200, 150, ORANGE, ORANGE_BG, kind="content", generic=True)
    xmark(bx + 4, 818, RED, s=20)
    text(bx + 40, 812, ver, size=SMALL, color=GREYD)
text(ox + 760, 664, "and every rescue\ncosts another run", size=SMALL, color=GREYD)
text(ox + 50, 866,
     "Three goes, still generic, and you paid for all three. The preparation is\ncheaper than the rescue - and you only do it once.",
     size=BODY, color=GREYD)
chip(ox + 50, 966, "prepare, then prompt", fill=ORANGE_BG, text_color=ORANGE,
     border=ORANGE, size=LABEL)

# ============================================================================
# BEAT 2 - THREE FILES, BEFORE YOU PROMPT   (the map of the whole day)
# ============================================================================
ox = beat_head(2, "three files, before you prompt",
               "Each one is built from the one before it. Get these three right and the\nfourth step - the actual deck - stops being the hard part.")
STEPS = [("design.md", "the rules: colours,\ntype, spacing", MD, MD_BG),
         ("design system", "those rules, native\nto Claude Design", SYS, SYS_BG),
         ("template", "how a deck is\nlaid out", TPL, TPL_BG)]
for k, (name, cap, acc, abg) in enumerate(STEPS):
    bx = ox + 40 + k * 290
    rect(bx, 356, 230, 200, stroke=acc, bg=WHITE, sw=3, rough=1, rounded=True, prefix="stp")
    rect(bx, 356, 230, 46, stroke="transparent", bg=abg, sw=1, rough=1, rounded=True,
         prefix="stph")
    num_badge(bx + 14, 360, k + 1, acc, d=38)
    text(bx + 62, 366, name, size=LABEL, color=acc)
    text(bx + 22, 442, cap, size=SMALL, color=INK)
    if k < 2:
        arrow(bx + 240, 446, [[0, 0], [38, 0]], stroke=GREYD, sw=4, rough=1)
arrow(ox + 880, 446, [[0, 0], [34, 0]], stroke=GREYD, sw=4, rough=1)
deck(ox + 930, 380, 160, 180, VIOLET, VIOLET_BG)
text(ox + 926, 600, "every deck\nafter this", size=SMALL, color=VIOLET)
text(ox + 40, 668,
     "The design system decides how everything LOOKS. The template decides how a\ndeck is ARRANGED. Built once, they apply to everything you make after.",
     size=BODY, color=GREYD)
text(ox + 40, 786, "and it is not only slides", size=SMALL, color=GREY)
_cx = ox + 40
for lab in ["slide decks", "social carousels", "newsletter visuals", "one-off graphics"]:
    _w, _h = chip(_cx, 820, lab, fill=WHITE, text_color=VIOLET, border=VIOLET, size=SMALL)
    _cx += _w + 22
chip(ox + 40, 916, "in order - each one feeds the next", fill=VIOLET_BG,
     text_color=VIOLET, border=VIOLET, size=LABEL)

# ============================================================================
# BEAT 3 - DESIGN.MD IS THE RULEBOOK   (input 1, + the red sourcing rule)
# ============================================================================
ox = beat_head(3, "design.md is the rulebook",
               "A plain text file that says how a design should look: the exact colours,\nthe fonts, the spacing, how a button or a card is styled.")
md_file(ox + 50, 316, 440, 430, rules=[
    (BLUE, "brand.primary   #1971c2"),
    (GREEN, "brand.accent    #2f9e44"),
    (None, "type: Inter / 16-48 / 600 weight"),
    (None, "spacing: 8 / 16 / 24 / 48"),
    (None, "radius: 8. Cards: 1px border, no shadow"),
    (None, "buttons: solid fill, white label"),
])
text(ox + 540, 316, "what goes in it", size=SMALL, color=GREY)
for k, item in enumerate(["colours, by name and by hex",
                          "type: family, sizes, weights",
                          "spacing, radius, borders",
                          "how a button or a card looks"]):
    check_item(ox + 540, 356 + k * 62, item, color=INK, accent=BLUE, size=BODY)
text(ox + 540, 618,
     "It is plain text, so it works in any\nAI tool. Claude Design is what turns\nit into something it can use natively.",
     size=BODY, color=GREYD)
chip(ox + 540, 742, "start from a reference, not a blank page", fill=WHITE,
     text_color=BLUE, border=BLUE, size=SMALL)
# the red rule - sourcing. This is the only on-screen rule on this board, and it
# is the one the source transcript got wrong, so it is stated positively here.
highlighter(ox + 40, 812, 1080, 140, RED_BG, angle=0.0)
diamond(ox + 58, 838, 44, 44, stroke=RED, bg=RED_BG, sw=3)
text_centered(ox + 80, 842, "!", size=H3, color=RED)
text(ox + 126, 830,
     "Claude will not reproduce a real brand's guidelines, and that refusal is\ncorrect - do not route around it. Take your rules from your own brand\nassets: if you cannot say where a colour came from, it is not yours.",
     size=BODY, color=RED)

# ============================================================================
# BEAT 4 - THE DESIGN SYSTEM MAKES IT NATIVE   (input 2)
# ============================================================================
ox = beat_head(4, "the design system makes it native",
               "Claude Design reads the design.md and builds a working style guide from it,\nwith sample mockups for you to check before anything depends on them.")
md_file(ox + 40, 340, 190, 220, label="design.md", rules=[
    (BLUE, "colours"), (None, "type"), (None, "spacing")])
arrow(ox + 244, 436, [[0, 0], [84, 0]], stroke=SYS, sw=5, rough=1)
rect(ox + 352, 330, 728, 240, stroke=SYS, bg=WHITE, sw=3, rough=1, rounded=True,
     prefix="sysp")
rect(ox + 352, 330, 728, 46, stroke="transparent", bg=SYS_BG, sw=1, rough=1,
     rounded=True, prefix="sysph")
text(ox + 376, 340, "your design system", size=LABEL, color=SYS)
_ex = swatch_strip(ox + 378, 404, [(VIOLET, VIOLET_BG), (BLUE, BLUE_BG),
                                   (GREEN, GREEN_BG), (ORANGE, ORANGE_BG)])
text(_ex + 16, 398, "Aa", size=H2, color=INK)
button(_ex + 108, 404, "Button", SYS, w=150, h=44)
text(ox + 378, 478, "your logo, your icons and a voice-and-tone file - uploaded once", size=SMALL, color=GREYD)
text(ox + 378, 516, "then every design after this one has them, without asking", size=SMALL, color=GREYD)
# the mockups it generates for review
text(ox + 40, 606, "it builds sample mockups so you can see the style before you rely on it",
     size=SMALL, color=GREY)
for k, kind in enumerate(["title", "content", "two-col", "section"]):
    slide_thumb(ox + 40 + k * 268, 644, 240, 150, SYS, SYS_BG, kind=kind)
# feedback in plain English
text(ox + 40, 824, "not right? say so in plain English", size=SMALL, color=GREY)
sticky(ox + 40, 858, 660, 84, SYS_BG, angle=jit(1.2))
text(ox + 70, 878, "replace the dark background with this hex from our own palette",
     size=SMALL, color=INK)
chip(ox + 740, 866, "build it once, inherit it forever", fill=WHITE, text_color=SYS,
     border=SYS, size=SMALL)

# ============================================================================
# BEAT 5 - THE TEMPLATE IS THE LAYOUT   (input 3)
# ============================================================================
ox = beat_head(5, "the template is the layout",
               "The design system says how it looks. The template says how a deck is\narranged - which slides exist, and in what order.")
line(ox + 545, 350, [[0, 0], [0, 430]], stroke=GREY, sw=2, dashed=True)
# left: how it LOOKS
text(ox + 40, 300, "how it looks", size=H2, color=SYS)
text(ox + 40, 348, "the design system", size=SMALL, color=GREY)
rect(ox + 40, 388, 460, 320, stroke=SYS, bg=SYS_T, sw=3, rough=1, rounded=True,
     prefix="lks")
_ex = swatch_strip(ox + 70, 428, [(VIOLET, VIOLET_BG), (BLUE, BLUE_BG),
                                  (GREEN, GREEN_BG), (ORANGE, ORANGE_BG)])
text(ox + 70, 508, "Aa  Inter  16 / 24 / 48", size=H3, color=INK)
text(ox + 70, 570, "spacing 8 / 16 / 24", size=BODY, color=GREYD)
text(ox + 70, 618, "your logo, your icons", size=BODY, color=GREYD)
text(ox + 40, 736, "colours, type, logo - unchanged everywhere", size=SMALL, color=GREYD)
# right: how it is ARRANGED
text(ox + 600, 300, "how it is arranged", size=H2, color=TPL)
text(ox + 600, 348, "the template", size=SMALL, color=GREY)
for k, (kind, lab) in enumerate([("title", "title"), ("section", "section divider"),
                                 ("two-col", "two columns"), ("content", "closing")]):
    bx = ox + 600 + (k % 2) * 262
    by = 388 + (k // 2) * 172
    slide_thumb(bx, by, 240, 140, TPL, TPL_BG, kind=kind)
    text(bx, by + 148, lab, size=SMALL, color=TPL)
text(ox + 600, 736, "which slides, in which order", size=SMALL, color=GREYD)
text(ox + 40, 806,
     "Together, every new deck starts on brand AND pre-structured, instead of from\na blank canvas. Give the template feedback too - every future deck reads it.",
     size=BODY, color=GREYD)
chip(ox + 40, 918, "looks and layout are two different jobs", fill=TPL_BG,
     text_color=TPL, border=TPL, size=LABEL)

# ============================================================================
# BEAT 6 - TWO KINDS OF FEEDBACK   (+ the three-way CLAUDE.md distinction)
# ============================================================================
ox = beat_head(6, "two kinds of feedback",
               "One kind changes this deck. The other changes every deck you make after\nit - and you should know which one you are giving.")
line(ox + 566, 330, [[0, 0], [0, 380]], stroke=GREY, sw=2, dashed=True)
# left: the kind that carries forward
text(ox + 40, 296, "carries forward", size=H2, color=INDIGO)
sticky(ox + 40, 356, 490, 104, INDIGO_BG, angle=jit(1.2))
text(ox + 68, 378, GOOD_FEEDBACK, size=SMALL, color=INK)
arrow(ox + 150, 476, [[0, 0], [0, 48]], stroke=INDIGO, sw=4, rough=1)
md_file(ox + 40, 538, 490, 172, accent=INDIGO, abg=INDIGO_BG, label="CLAUDE.md", rules=[
    (None, "labels sit in a container"),
    (None, "icons have transparent backgrounds")])
text(ox + 40, 724, "written into the project, and read before every new design", size=SMALL, color=GREYD)
# right: the kind that does not
text(ox + 620, 296, "this deck only", size=H2, color=GREYD)
_cx = ox + 620
for lab in ["edit", "annotate", "tweaks"]:
    _w, _h = chip(_cx, 362, lab, fill=WHITE, text_color=GREYD, border=GREYD, size=SMALL)
    _cx += _w + 20
text(ox + 620, 436, "edit one element. Draw on a slide and\nsay what you want. Or add a switch:", size=SMALL, color=GREYD)
toggle(ox + 620, 520, "show logo", True)
toggle(ox + 620, 572, "slide numbers", False)
text(ox + 620, 636, "a tweak is one switch for a decision that\nrepeats on every slide - flip it before\nyou commit to it", size=SMALL, color=GREYD)
# the three-way name collision - the thing this board must not let merge
text(ox + 40, 764, "three different things share these names. Do not let them merge:",
     size=SMALL, color=GREY)
for k, (acc, nm, gloss) in enumerate([
        (VIOLET, "Claude's memory", "what Claude remembers about YOU, across chats  (Day 3)"),
        (ORANGE, "CLAUDE.md in Claude Code", "how to work in a codebase  (Day 4)"),
        (INDIGO, "CLAUDE.md in a design project", "standing instructions for THESE designs  (here)")]):
    ry = 800 + k * 48
    rect(ox + 44, ry + 4, 22, 22, stroke=acc, bg=acc, sw=2, rough=1, rounded=True, prefix="dot")
    text(ox + 82, ry, nm + " - " + gloss, size=SMALL, color=INK)
demo_badge(ox + 40, 952,
           "show in Claude Design: give feedback once, then open the project's CLAUDE.md")

# ============================================================================
# BEAT 7 - EVERYTHING COMPOUNDS, MISTAKES TOO  (adversarial: failure AND catch)
# ============================================================================
ox = beat_head(7, "everything compounds, mistakes too",
               "The whole point is that every fix carries forward. So does every wrong\nrule - and nothing on the screen tells you it happened.")
text(ox + 40, 292, "one wrong rule, saved into the system", size=SMALL, color=RED)
rect(ox + 40, 326, 440, 170, stroke=RED, bg=RED_T, sw=3, rough=1, rounded=True, prefix="badsys")
for k, rule in enumerate(["cards: 1px border, no shadow", BAD_RULE,
                          "buttons: solid fill"]):
    text(ox + 68, 348 + k * 44, rule, size=SMALL,
         color=(RED if rule == BAD_RULE else GREYD))
circle_around(ox + 58, 386, 330, 46, RED)
for k in range(3):
    arrow(ox + 490, 380 + k * 34, [[0, 0], [56, k * 26 - 26]], stroke=RED, sw=3, rough=1,
          dashed=True)
for k in range(3):
    bx = ox + 570 + k * 186
    slide_thumb(bx, 326, 170, 130, GREY, FAINT, kind="content", generic=True)
    text(bx + 14, 468, "looks fine", size=SMALL, color=GREYD)
text(ox + 40, 540,
     "Every deck after that change inherits it, and so does every new chat in the\nproject - because the CLAUDE.md is read before each one. Nothing says so.",
     size=BODY, color=GREYD)
# the catch
text(ox + 40, 646, "the catch", size=SMALL, color=RED)
text(ox + 40, 680, "keep one reference design - re-render it after every change",
     size=H3, color=RED)
sticky(ox + 40, 736, 1060, 76, RED_T, angle=jit(1.0))
text(ox + 74, 756, REFERENCE, size=BODY, color=INK)
slide_thumb(ox + 40, 838, 150, 110, SYS, SYS_BG, kind="title")
tick(ox + 208, 872, GREEN)
text(ox + 254, 866, "before the change:\nstill right", size=SMALL, color=GREYD)
slide_thumb(ox + 500, 838, 150, 110, GREY, FAINT, kind="title", generic=True)
xmark(ox + 670, 876, RED, s=22)
text(ox + 714, 866, "after: caught in ten seconds,\nnot in ten decks", size=SMALL, color=GREYD)
chip(ox + 40, 972, "a system can teach itself your mistakes", fill=RED_BG,
     text_color=RED, border=RED, size=LABEL)

# ============================================================================
# BEAT 8 - THEN IT LEAVES THE ROOM   (export, then the human pass)
# ============================================================================
ox = beat_head(8, "then it leaves the room",
               "Out to PowerPoint, to PDF, or to a single HTML file that opens in any\nbrowser. And a person still signs it off.")
text(ox + 50, 296, "the finished deck", size=SMALL, color=GREY)
deck(ox + 50, 334, 250, 200, YELLOW, YELLOW_BG)
arrow(ox + 326, 424, [[0, 0], [72, 0]], stroke=YELLOW, sw=5, rough=1)
for k, lab in enumerate(["PowerPoint", "PDF", "one standalone HTML file"]):
    chip(ox + 430, 336 + k * 70, lab, fill=WHITE, text_color=YELLOW, border=YELLOW,
         size=SMALL)
text(ox + 430, 552,
     "the HTML one opens in any browser and works for\nanyone you send it to - nothing to install, no account",
     size=SMALL, color=GREYD)
# the human pass, in the same green Day 10 closes on
human_gate(ox + 160, 760, GREEN, GREEN_BG)
arrow(ox + 250, 720, [[0, 0], [90, 0]], stroke=GREEN, sw=5, rough=1)
slide_thumb(ox + 380, 650, 190, 140, GREEN, GREEN_BG, kind="title")
tick(ox + 610, 690, GREEN)
text_centered(ox + 160, 826, "a person signs it off", size=SMALL, color=GREEN)
text(ox + 380, 806, "then it goes out", size=SMALL, color=GREEN)
text(ox + 700, 660,
     "Claude Design gets you a deck that\nlooks finished. Day 10's rule has not\nchanged: looking finished and being\nright are different things.",
     size=BODY, color=GREYD)
chip(ox + 40, 900, "nothing goes out without the human pass", fill=GREEN_BG,
     text_color=GREEN, border=GREEN, size=LABEL)
chip(ox + 40, 972, "prepare once, and every deck after this is cheaper", fill=YELLOW_BG,
     text_color=YELLOW, border=YELLOW, size=LABEL)

# No connector spine, no inter-beat arrows and no footer: the eight beats read as
# one picture through consistent shape and rhythm, and the whitespace is the camera.

# ----------------------------------------------------------------------------
# WRITE + VALIDATE  (shared excalidraw_kit; hard-fails on frames / off-palette)
# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "claude-design-md.excalidraw")
MAXW = max(WID.values()) + 200
finish(out, MAXW, TOTAL_W)
