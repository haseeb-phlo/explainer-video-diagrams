#!/usr/bin/env python3
"""Build claude-powerpoint.excalidraw - ONE flowing, illustrated explainer for
DAY 12 of the Phlo AI training: "Claude in Microsoft PowerPoint" (~5 min 52,
hard cap 8).

Day 12 sits after the two design days on purpose. Day 10 taught that the
advanced failure in visual work is not a bad output but an acceptable one;
this board is that same failure wearing a suit. A deck is the one artefact
where "it looks finished" and "it is finished" come apart completely, because
formatting is the part Claude is best at and arguing is the part it will skip
unless you make it.

WHAT THIS BOARD IS NOW (it was adapted, not extended)
-----------------------------------------------------
This board MOVED HERE from videos/claude/7-claude-powerpoint/ (module 2.7) when
the day-by-day training became the authoritative series - the same move Day 4,
Day 7, Day 8 and Day 10 each made out of videos/claude/. That series now has a
fifth numbering gap, at 7. A gap is not lost work, and NOTHING in videos/claude/
was renumbered.

Per the repo precedence rule, a Day covers its topic IN FULL. There is no other
PowerPoint video to signpost - claude/7-claude-powerpoint IS this video, moved -
so this board must never be trimmed to a "see the other video" pointer.

This used to be a NINE-beat product walkthrough: ask and get a real .pptx, what
the file is, start from what you have, tell it the shape, the two places Claude
lives (chat vs the Microsoft 365 add-in), edit by talking, four use cases, a
safety checklist, a try-it close. That board taught a FEATURE SURFACE, and every
interesting fact on it was a plan tier or a file-size limit.

It is now a SEVEN-beat board about ARGUMENT CONSTRUCTION, because the failure
here is not an ugly deck - it is a tidy one that makes no argument. For an
audience that presents to executives weekly, that is the expensive failure, and
it is the one nobody catches in review: a reviewer checks that the slides look
right, which they do.

THE BOARD NAMES THE TOOL, NEVER THE TIER. "PowerPoint" appears in the board
title and in the demo badge and nowhere else - not one of the seven headings
needs it. Plan tiers, the Microsoft 365 add-in, the 30MB limit, web/desktop/
mobile, .pptx and Drive export are all on `claude-powerpoint-resource-card.md`.
That card is a deliverable, not an afterthought: do not re-inflate the board
with it, and when a fact moves, FIX THE CARD, NOT THE BOARD.

ONE THING MOVED RATHER THAN WENT. The old beat 8 carried the only on-screen
data-handling rule. The seven-beat brief has no slot for it, but this is a
mandatory course for a regulated pharmacy, so it sits on beat 7 beside the
close instead of going to the card - the same call Day 7 made with its red Skill
caution and Day 10 with its confidential-designs rule. Do not quietly drop it.

BEAT 5 IS SCOPED TO JUDGEMENT, NOT MECHANICS. "Design is not its strength"
means it will not make BRAND DECISIONS for you. It emphatically DOES respect a
template you give it: the docs (verified 2026-09-14) say Claude reads the slide
master, layouts, fonts and colour scheme and generates against them, aiming to
"maintain template compliance without introducing off-brand elements". So the
right-hand column is worded as DECISIONS ("which template to use", "what the
brand actually is"), never as objects ("the template"), and the narration must
not drift into claiming it ignores your template - that would contradict both
the Resource Card and the docs. What the docs DO back is the judgement claim:
they list "replacing your judgment on design and narrative flow" as something
the add-in is not recommended for.

THE ADVERSARIAL BEAT (6) CARRIES ITS OWN CATCH. The failure is three decks that
are all well-made, all different and all interchangeable, because not one of
them would change a decision. The catch is: name the decision you are asking
for BEFORE you build, then read ONLY the headlines, in order, and ask whether
they argue for it. The catch retroactively tests beat 3, which is the point -
a headline that states a position is the thing that makes the test passable.
Failure without a catch is a diagnosis with no test, and this beat is the Best
Catch feeder.

Style B (house style): a single hand-drawn journey, left-to-right, NO frames, NO
boxes, white canvas, everything in the hand font (fontFamily 1), roughness 1, a
lively colour-coded Excalidraw palette, big colour blocking, scribbled
annotations and charming primitive illustrations. The look lives in the shared
excalidraw_kit; this file holds only the composition and the bespoke one-offs.

PAN ORDER (left to right - the whitespace between slots IS the camera; frame one
beat at a time):

     1  ORANGE  it looks finished and says nothing   <- eight tidy slides, no argument
     2  VIOLET  structure first, slides second
     3  BLUE    one idea per slide, one line that carries it
     4  TEAL    build it from a source
     5  INDIGO  design is not its strength           <- honest beat; the brand pass is human
     6  RED     the plausible deck                   <- adversarial: the failure AND the catch
     7  GREEN   outline to deck, live                <- [CUT TO CLAUDE DESKTOP], then the close

RUNTIME (budgeted in seconds, then MEASURED against the written narration - the
measuring is the step that matters; this repo's one recorded process lesson is
that per-beat second budgets drift by 2x against the written prose):
     beats are not uniform. Measured at 150 wpm, from claude-powerpoint-script.md:
        b1 28s   b2 32s   b3 43s   b4 28s   b5 27s   b6 64s   b7 38s (+15s cut-away)
        hook 10s   why 32s   pause-and-try 16s   close 14s
     844 spoken words = 5 min 37, plus the cut-away doing time = ~5 min 52.
     Hard cap 8 minutes, target 4 to 6 - inside target, 2 min 08 of headroom.
     Beat 6 is the longest on purpose; everything else was trimmed to pay for it.
     Shorter cut: drop beats 4 and 5 (~4 min 57). Never drop beat 6.

Run:  python3 videos/ai-training/12-powerpoint/build_powerpoint.py
      /usr/bin/python3 preview.py videos/ai-training/12-powerpoint/claude-powerpoint.excalidraw out.png
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

random.seed(240712)  # deterministic - re-runs produce identical files

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
# THE WORKED EXAMPLE - one generic supplier re-tender, carried across beats 2, 3,
# 6 and 7 so the board tells a single story: the outline agreed in chat, the
# headlines rewritten as positions, the decision the deck has to win, and the
# deck that finally asks for it. Deliberately everyday business, never
# Phlo-specific, no patient or clinical detail, invented numbers throughout.
#
# CHANGE THE EXAMPLE AND BEATS 2, 3, 6 AND 7 ALL HAVE TO MOVE TOGETHER.
# ----------------------------------------------------------------------------
# The decision is the catch on beat 6: one sentence, named before you build, and
# falsifiable by reading the headlines alone.
DECISION = "'approve the re-tender of the packaging contract'"

# Beat 3's rewrites: the topic you would have typed, and the claim that does work.
TOPIC_TO_CLAIM = [
    ("Q3 results",      "margin fell because unit cost rose"),
    ("Supplier review", "two of three suppliers missed SLA twice"),
    ("Next steps",      "re-tender now, or absorb it again"),
]

# Beat 6's headline strip - the generic deck, read in order. No argument in it.
GENERIC_HEADLINES = "Q3 results   -   Background   -   Our options   -   Next steps"

# The outline agreed in chat on beat 2, and its short form on beats 4 and 7.
OUTLINE = ["unit cost rose 9% in Q3",
           "two of three suppliers missed SLA twice",
           "absorbing it costs more by Q2",
           "a re-tender takes eleven weeks",
           "the ask: approve the re-tender"]
OUTLINE_SHORT = ["cost up 9%", "SLA missed twice", "absorb = worse by Q2",
                 "re-tender: 11 weeks", "the ask"]


# ----------------------------------------------------------------------------
# BESPOKE ILLUSTRATIONS for this board (one-offs stay here, never in the kit)
# ----------------------------------------------------------------------------
def slide(x, y, w, h, accent=ORANGE, abg=ORANGE_BG, bullets=3, chart=True):
    """A single tidy slide: title bar, a few bullet lines, a small bar chart.

    Deliberately carries ZERO text elements. Eight of these in a grid is the
    whole of beat 1 - it looks finished and contains nothing, and that reads
    better unlabelled than it would with eight invented slide titles."""
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="slide")
    rect(x + 0.10 * w, y + 0.12 * h, 0.45 * w, 0.10 * h, stroke="transparent",
         bg=accent, sw=1, rough=1, rounded=True, prefix="sttl")
    for k in range(bullets):
        ly = y + 0.34 * h + k * 0.14 * h
        ellipse(x + 0.10 * w, ly + 2, 7, 7, stroke=accent, bg=accent, sw=1)
        line(x + 0.10 * w + 18, ly + 5, [[0, 0], [0.34 * w, 0]], stroke=GREY, sw=2)
    if chart:
        base = y + h - 0.16 * h
        for k, hh in enumerate([0.22, 0.40, 0.30, 0.5]):
            bh = hh * h
            rect(x + 0.62 * w + k * 0.085 * w, base - bh, 0.05 * w, bh,
                 stroke=INK, bg=abg, sw=1, rough=1, rounded=False, prefix="sbar")


def slide_deck(x, y, accent=ORANGE, abg=ORANGE_BG):
    """A stack of slides - two offset behind, one crisp slide in front.
    Extent is x..x+268, y..y+186."""
    for k in range(2):
        off = (2 - k) * 18
        rect(x + off, y + off, 232, 150, stroke=INK, bg=abg, sw=2, rough=1,
             rounded=True, prefix="deck")
    slide(x + 36, y + 36, 232, 150, accent=accent, abg=abg, bullets=3, chart=True)


def _strike(x, y, s, size, color, sw=4):
    """A hand line through text. The kit has no strikethrough, so this is a
    one-off - and it sits at 0.44 of the line box, not 0.5: with lineHeight 1.4
    the glyphs sit high in their box, so a line at the geometric middle crosses
    the descenders and reads as an underline that slipped. (Same finding as
    Day 10's struck(); rediscovering it cost a preview round there.)"""
    w = text_w(s, size)
    line(x - 8, y + size * LINE_H * 0.44, [[0, 0], [w + 16, 0]], stroke=color,
         sw=sw, rough=1, prefix="strike")


def struck(x, y, s, size=H3, color=GREYD, strike=BLUE, sw=4):
    """Struck-through text: the words, with a deliberate mark drawn across them."""
    text(x, y, s, size=size, color=color)
    _strike(x, y, s, size, strike, sw)


def headline_slide(x, y, w, h, title, accent=GREEN, abg=GREEN_BG, tsize=SMALL,
                   lines=2, strike=None, chart=False):
    """A slide whose TITLE is a full sentence - the headline doing the arguing.

    The counterpart to slide(): same tidy furniture, but the one text element on
    it is the thing that carries the idea. `strike` draws the title as struck
    through, which is how beat 3 shows a topic heading failing."""
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="hsl")
    rect(x, y, w, 10, stroke="transparent", bg=accent, sw=1, rough=1, rounded=True,
         prefix="hsb")
    tx, ty = x + 0.07 * w, y + 0.10 * h
    text(tx, ty, title, size=tsize, color=(GREYD if strike else INK))
    if strike is not None:
        _strike(tx, ty, title, tsize, strike)
    ly = ty + len(title.split("\n")) * tsize * LINE_H + 22
    for k in range(lines):
        line(tx, ly + k * 20, [[0, 0], [w * 0.5, 0]], stroke=GREY, sw=2)
    if chart:
        base = y + h - 0.12 * h
        for k, hh in enumerate([0.16, 0.30, 0.22, 0.36]):
            bh = hh * h
            rect(x + 0.60 * w + k * 0.085 * w, base - bh, 0.05 * w, bh,
                 stroke=INK, bg=abg, sw=1, rough=1, rounded=False, prefix="hsbar")


def dashed_box(x, y, w, h, color=GREY, sw=3):
    """An empty dashed outline - a slot with nothing in it. The kit's rect() has
    no strokeStyle, so this is four dashed lines."""
    for pts, ox_, oy_ in (([[0, 0], [w, 0]], 0, 0), ([[0, 0], [w, 0]], 0, h),
                          ([[0, 0], [0, h]], 0, 0), ([[0, 0], [0, h]], w, 0)):
        line(x + ox_, y + oy_, pts, stroke=color, sw=sw, rough=1, dashed=True, prefix="dbx")


def human_gate(cx, cy, color=INDIGO, abg=INDIGO_BG, s=1.0):
    """The human marker on beat 5: a head plus rounded shoulders, filled.

    It does not use the kit's person(), which is sized for a crowd of tiny
    figures and reads as a paper dart when it has to stand alone at hero size.
    Same reasoning as Day 10's human_gate() and Day 3's person_big()."""
    r = 26 * s
    ellipse(cx - r, cy - 62 * s, 2 * r, 2 * r, stroke=color, bg=WHITE, sw=3, rough=1,
            prefix="hghead")
    line(cx - 50 * s, cy + 46 * s,
         [[0, 0], [0, -22 * s], [18 * s, -50 * s], [82 * s, -50 * s],
          [100 * s, -22 * s], [100 * s, 0]],
         stroke=color, sw=3, rough=1, bg=abg, fill="solid", prefix="hgbody")


def chat_panel(x, y, w, h, stroke=INK):
    """A plain chat window: title strip and three dots. Everything else is placed
    by the caller, so beat 2 can put the outline inside it."""
    rect(x, y, w, h, stroke=stroke, bg=WHITE, sw=2, rough=1, rounded=True, prefix="chat")
    line(x, y + 40, [[0, 0], [w, 0]], stroke=GREY, sw=1)
    for k in range(3):
        ellipse(x + 18 + k * 18, y + 15, 10, 10, stroke=GREY, bg=GREY, sw=1)


def outline_rows(x, y, items, accent, step=58, d=34, size=SMALL, gap=48):
    """A numbered outline - one claim to a line. The shape the argument lives in
    before any of it is designed."""
    for k, item in enumerate(items):
        ry = y + k * step
        num_badge(x, ry, k + 1, accent, d=d)
        text(x + gap, ry + 3, item, size=size, color=INK)


# ============================================================================
# BOARD TITLE
# ============================================================================
text(OX[1], -300, "Claude in PowerPoint", size=HERO, color=INK)
text(OX[1] + 6, -300 + HERO * LINE_H + 4,
     "a deck is an argument - the slides are just where it lives", size=H2, color=ORANGE)

# ============================================================================
# BEAT 1 - IT LOOKS FINISHED AND SAYS NOTHING
# ============================================================================
ox = beat_head(1, "it looks finished and says nothing",
               "Eight tidy slides. Every one formatted, not one of them\narguing for anything.")
text(ox + 50, 292, "what landed in your inbox at nine at night", size=SMALL, color=GREY)
# eight neat slides, 4 x 2. No text on any of them - that IS the point.
for k in range(8):
    sx = ox + 50 + (k % 4) * 268
    sy = 330 + (k // 4) * 186
    slide(sx, sy, 250, 165, accent=ORANGE, abg=ORANGE_BG, bullets=3, chart=True)
text(ox + 50, 706, "titles, bullets, a chart on every one - nothing to fix", size=SMALL, color=GREY)
text(ox + 50, 752, "and the slide that says why any of it matters:", size=H3, color=ORANGE)
dashed_box(ox + 50, 806, 1040, 116, GREY, sw=3)
text_centered(ox + 570, 846, "- missing -", size=H3, color=GREY)
chip(ox + 50, 950, "formatted is not reasoned", fill=ORANGE_BG, text_color=ORANGE,
     border=ORANGE, size=LABEL)

# ============================================================================
# BEAT 2 - STRUCTURE FIRST, SLIDES SECOND
# ============================================================================
ox = beat_head(2, "structure first, slides second",
               "Agree the argument in the chat. Only then let it build the\nthing you would have to redraw.")
text(ox + 50, 292, "in the chat, before any design exists", size=SMALL, color=GREY)
chat_panel(ox + 50, 330, 560, 500)
sticky(ox + 86, 392, 400, 84, VIOLET_T, angle=jit(1.2))
text(ox + 112, 414, "propose an outline first", size=BODY, color=INK)
text(ox + 86, 498, "Claude:", size=SMALL, color=GREY)
outline_rows(ox + 86, 532, OUTLINE, VIOLET, step=58, d=34, size=SMALL, gap=48)
tick(ox + 52, 866, GREEN)
text(ox + 96, 860, "four minutes of chat, and the argument is settled", size=SMALL, color=GREYD)
# then, and only then, the design
arrow(ox + 634, 560, [[0, 0], [66, 0]], stroke=VIOLET, sw=5, rough=1)
text(ox + 726, 292, "then, and only then", size=SMALL, color=GREY)
slide_deck(ox + 760, 440, accent=VIOLET, abg=VIOLET_BG)
text(ox + 760, 654, "the design goes last -\nand it is the cheap part", size=BODY, color=GREYD)
chip(ox + 50, 940, "if the outline is wrong, the design is wasted", fill=VIOLET_BG,
     text_color=VIOLET, border=VIOLET, size=LABEL)

# ============================================================================
# BEAT 3 - ONE IDEA PER SLIDE, ONE LINE THAT CARRIES IT
# ============================================================================
ox = beat_head(3, "one idea per slide, one line that carries it",
               "The headline is the argument, not the topic. If it could be\na chapter title, it is not doing any work.")
text(ox + 50, 292, "a topic", size=SMALL, color=GREY)
headline_slide(ox + 50, 326, 480, 280, "Q3 results", accent=GREY, abg=FAINT,
               tsize=H3, lines=3, strike=BLUE, chart=True)
xmark(ox + 52, 628, RED, s=22)
text(ox + 96, 622, "a chapter heading - it commits to nothing", size=SMALL, color=GREYD)
text(ox + 610, 292, "a position", size=SMALL, color=GREY)
headline_slide(ox + 610, 326, 480, 280, "margin fell because\nunit cost rose",
               accent=BLUE, abg=BLUE_BG, tsize=H3, lines=3, chart=True)
tick(ox + 612, 626, GREEN)
text(ox + 658, 622, "a claim - you can agree or disagree", size=SMALL, color=GREYD)
# every headline on the deck, rewritten the same way
text(ox + 50, 686, "every headline, rewritten as a position", size=SMALL, color=GREY)
for k, (topic, claim) in enumerate(TOPIC_TO_CLAIM):
    ry = 726 + k * 66
    struck(ox + 50, ry, topic, size=H3, color=GREYD, strike=BLUE)
    arrow(ox + 330, ry + 18, [[0, 0], [50, 0]], stroke=BLUE, sw=3, rough=1)
    text(ox + 400, ry, claim, size=H3, color=BLUE)
chip(ox + 50, 934, "the headline is the argument, not the topic", fill=BLUE_BG,
     text_color=BLUE, border=BLUE, size=LABEL)

# ============================================================================
# BEAT 4 - BUILD IT FROM A SOURCE
# ============================================================================
ox = beat_head(4, "build it from a source",
               "Point it at the report and the numbers you already have.\nA deck built from a prompt is built from nothing.")
text(ox + 50, 292, "what you already have", size=SMALL, color=GREY)
obj_doc(ox + 50, 336, BLUE, BLUE_BG)
text(ox + 50, 502, "the supplier report", size=SMALL, color=GREYD)
obj_chart(ox + 50, 556, TEAL, TEAL_BG)
text(ox + 50, 706, "last quarter's costs", size=SMALL, color=GREYD)
arrow(ox + 196, 420, [[0, 0], [120, 60]], stroke=TEAL, sw=3, rough=1)
arrow(ox + 196, 640, [[0, 0], [120, -60]], stroke=TEAL, sw=3, rough=1)
# the sources flow into an OUTLINE, not into a blank box
text(ox + 340, 292, "the outline it proposes", size=SMALL, color=GREY)
rect(ox + 340, 336, 380, 400, stroke=TEAL, bg=TEAL_T, sw=2, rough=1, rounded=True)
outline_rows(ox + 370, 380, OUTLINE_SHORT, TEAL, step=68, d=32, size=SMALL, gap=46)
text(ox + 340, 752, "grounded in those two files, line by line", size=SMALL, color=GREYD)
# against a prompt on its own
text(ox + 770, 292, "what a prompt on its own gives you", size=SMALL, color=GREY)
sticky(ox + 770, 336, 340, 100, FAINT, angle=jit(1.4))
text(ox + 796, 358, "'make me a deck about\nsupplier costs'", size=SMALL, color=GREYD)
arrow(ox + 940, 448, [[0, 0], [0, 44]], stroke=GREY, sw=3, rough=1)
slide_deck(ox + 800, 508, accent=GREY, abg=FAINT)
xmark(ox + 772, 722, RED, s=22)
text(ox + 816, 716, "plausible, generic, and not\nabout your numbers", size=SMALL, color=GREYD)
chip(ox + 50, 866, "feed it the source, not a description of the source",
     fill=TEAL_BG, text_color=TEAL, border=TEAL, size=LABEL)

# ============================================================================
# BEAT 5 - DESIGN IS NOT ITS STRENGTH   (the honest beat)
# ============================================================================
ox = beat_head(5, "design is not its strength",
               "It is good at the order of an argument. It will not decide\nwhat your brand looks like.")
text(ox + 50, 292, "genuinely good at this", size=H3, color=INDIGO)
sticky(ox + 50, 344, 510, 300, INDIGO_T, angle=jit(1.2))
for k, item in enumerate(["the order things go in", "one idea to a slide",
                          "the line that carries each one", "a first draft in minutes"]):
    check_item(ox + 86, 384 + k * 64, item, color=INK, accent=INDIGO, size=BODY)
text(ox + 610, 292, "still yours to decide", size=H3, color=GREYD)
sticky(ox + 610, 344, 500, 300, FAINT, angle=jit(-1.2))
# the four things that stay with a person. Worded as DECISIONS ("which template",
# "what the brand actually is") rather than as objects ("the template"), because
# Claude for PowerPoint demonstrably DOES read the slide master, layouts, fonts
# and colour scheme and generate against them (verified against the docs on
# 2026-09-14). What it will not do is decide what your brand IS. "the template"
# on its own read as "Claude ignores your template", which is wrong and would
# contradict the Resource Card.
for k, item in enumerate(["which template to use", "what the brand actually is",
                          "what good looks like here", "the final look"]):
    yy = 384 + k * 64
    xmark(ox + 646, yy + 2, GREY, s=20)
    text(ox + 692, yy, item, size=BODY, color=GREYD)
# Claude's structure -> the brand pass, which is a person -> ready to send
slide_deck(ox + 60, 700, accent=INDIGO, abg=INDIGO_BG)
arrow(ox + 348, 790, [[0, 0], [76, 0]], stroke=INDIGO, sw=5, rough=1)
human_gate(ox + 510, 822, INDIGO, INDIGO_BG)
arrow(ox + 592, 790, [[0, 0], [76, 0]], stroke=INDIGO, sw=5, rough=1)
slide_deck(ox + 700, 700, accent=INDIGO, abg=INDIGO_BG)
text(ox + 60, 902, "Claude's structure", size=SMALL, color=GREYD)
text_centered(ox + 510, 902, "you: the brand pass", size=SMALL, color=INDIGO)
text(ox + 790, 902, "ready to send", size=SMALL, color=GREYD)
chip(ox + 50, 956, "structure, not design", fill=INDIGO_BG, text_color=INDIGO,
     border=INDIGO, size=LABEL)

# ============================================================================
# BEAT 6 - THE PLAUSIBLE DECK   (adversarial: the failure AND the catch)
# ============================================================================
ox = beat_head(6, "the plausible deck",
               "Three decks. All well-made, all different, and not one of them\nwould change anybody's mind.")
# three decks, ONE neutral grey and NO jitter: the sameness IS the point, and a
# tilt or a colour each would read as three real options rather than three
# interchangeable ones. (Day 10's beat 6 records the same deliberate exception.)
for k, lab in enumerate(["deck A", "deck B", "deck C"]):
    bx = ox + 50 + k * 370
    text(bx, 300, lab, size=SMALL, color=GREY)
    slide_deck(bx, 334, accent=GREY, abg=FAINT)
    text(bx, 540, "looks fine", size=BODY, color=GREYD)
# the headlines lifted OUT of the decks - one artefact to read, in order
text(ox + 50, 596, "read only the headlines, in order", size=SMALL, color=RED)
rect(ox + 50, 630, 1040, 86, stroke=GREYD, bg=WHITE, sw=2, rough=1, rounded=True)
text(ox + 78, 658, GENERIC_HEADLINES, size=BODY, color=GREYD)
# the catch - named before you look, so "it looks fine" cannot be the verdict
text(ox + 50, 748, "the catch", size=SMALL, color=RED)
text(ox + 50, 782, "name the decision you want, before you build", size=H3, color=RED)
sticky(ox + 50, 838, 1040, 78, RED_T, angle=jit(1.0))
text(ox + 86, 859, DECISION, size=BODY, color=INK)
xmark(ox + 52, 940, RED, s=22)
text(ox + 96, 934, "not one of those headlines argues for that. All three fail the same test.",
     size=BODY, color=GREYD)
chip(ox + 50, 990, "it will happily produce something nobody can disagree with",
     fill=RED_BG, text_color=RED, border=RED, size=LABEL)

# ============================================================================
# BEAT 7 - OUTLINE TO DECK, LIVE   (the cut-away, then the close)
# ============================================================================
ox = beat_head(7, "outline to deck, live",
               "Agree the outline in the chat. Then build the deck from it -\nand make every headline state a position.")
text(ox + 50, 292, "what you are shipping", size=SMALL, color=GREY)
rect(ox + 50, 330, 420, 340, stroke=GREEN, bg=GREEN_T, sw=2, rough=1, rounded=True)
text(ox + 80, 352, "the agreed outline", size=SMALL, color=GREEN)
outline_rows(ox + 80, 400, ["cost rose 9% in Q3", "two suppliers missed SLA",
                            "absorbing costs more", "the ask: re-tender"],
             GREEN, step=62, d=32, size=SMALL, gap=46)
tick(ox + 52, 692, GREEN)
text(ox + 96, 686, "agreed before a single slide existed", size=SMALL, color=GREYD)
arrow(ox + 492, 480, [[0, 0], [80, 0]], stroke=GREEN, sw=5, rough=1)
for k, hl in enumerate(["margin fell\nbecause unit\ncost rose",
                        "two suppliers\nmissed SLA\ntwice",
                        "absorbing it\ncosts more\nby Q2",
                        "re-tender now -\nhere is the\nask"]):
    headline_slide(ox + 600 + (k % 2) * 270, 330 + (k // 2) * 180, 240, 160, hl,
                   accent=GREEN, abg=GREEN_BG, tsize=SMALL, lines=2)
text(ox + 600, 690, "every headline states a position", size=BODY, color=GREEN)
demo_badge(ox + 50, 746,
           "show in Claude desktop app: agree the outline in chat, then build the deck from it")
# the data rule - red, because it is the only on-screen data-handling rule here
highlighter(ox + 40, 820, 1080, 100, RED_BG, angle=0.0)
diamond(ox + 56, 838, 44, 44, stroke=RED, bg=RED_BG, sw=3)
text_centered(ox + 78, 842, "!", size=H3, color=RED)
text(ox + 124, 836,
     "Nothing confidential goes in a deck you will send out - and do not\nbuild on a template or a file you do not trust.",
     size=BODY, color=RED)
chip(ox + 50, 946, "the argument is the deliverable", fill=GREEN_BG, text_color=GREEN,
     border=GREEN, size=LABEL)

# No connector spine, no inter-beat arrows and no footer: the seven beats read as
# one picture through consistent shape and rhythm, and the whitespace is the camera.

# ----------------------------------------------------------------------------
# WRITE + VALIDATE  (shared excalidraw_kit; hard-fails on frames / off-palette)
# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "claude-powerpoint.excalidraw")
MAXW = max(WID.values()) + 200
finish(out, MAXW, TOTAL_W)
