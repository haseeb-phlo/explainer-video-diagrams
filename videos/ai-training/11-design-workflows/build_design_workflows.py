#!/usr/bin/env python3
"""Build claude-design-workflows.excalidraw - ONE flowing, illustrated explainer
for DAY 11 of the Phlo AI training: "Claude Design, workflow by workflow"
(~6 min 42, hard cap 8).

WHAT THIS BOARD IS
------------------
Topic coverage, not an argument. Day 10 is the argument about judgement and
Day 13 is the plumbing (design.md, design system, template). This Day walks the
actual jobs people bring to Claude Design, in the order the sources cover them,
built on ONE repeatable six-step loop.

NUMBERING. This board is new work and took slot 11. The design.md board moved
TWICE: 11 -> 12 to free slot 11, then 12 -> 13 when Claude PowerPoint landed on
Day 12 from another branch while this board was in progress. Day 10's beat 2
pointer chip was regenerated to read "Day 13, design.md".

BEAT 1 IS A DELIBERATE RE-RUN, AND IT IS DELIBERATELY SHORT. The brief was
"ignore anything already covered in the Day 10 / design.md boards, cover those
as a brief reminder, then everything new from wireframing onwards". Beat 1 is
that reminder - four Day 10 chips, a forward chip to Day 13, and a chip sending
full on-brand decks to Day 12, Claude PowerPoint. ~20 seconds.
It is NOT a re-teach and must never grow into one; this board's subject starts at
beat 2. Day 10's own beat 2 -> Day 13 chip is the precedent for a forward chip.

SOURCES - TWO THIRD-PARTY, ONE FIRST-PARTY, AND THEY ARE NOT EQUAL
-------------------------------------------------------------------
  1. a third-party video transcript supplied with the brief;
  2. a third-party published playbook of workflows and prompts;
  3. Anthropic's own documentation - the Claude Design announcement, Get started
     with Claude Design, Set up your design system, the Team and Enterprise admin
     guide, the product page, and the Claude Academy prototypes/UX and
     presentations tutorials.
(3) outranks (1) and (2). Where the third-party sources assert product surface
that the docs do not carry, it goes on the Resource Card, attributed, never on
the board. `claude-design-workflows-prompt.md` records the mapping line by line.

ONE NUMBERED PROCESS PER BOARD. The six-step loop is beat 2 and it is the only
numbered thing here. Beat 5's exploration habit is a SEQUENCE in the source but
is drawn UNNUMBERED on purpose - two competing "the steps are" claims on one
board is a legibility failure, and the habit is what travels, not the count.

THE FASTEST-DATING LINE ON THIS BOARD is beat 7's "it plays in the browser - you
capture it off the screen". It is phrased as a mechanism rather than as the
absence of a button, precisely so it survives an export button shipping; but if
one does ship, this is the line to revisit. Same treatment Day 3's beat 15
(per-model habits) gets - the board carries it AND says it dates.

ONE SOURCE CLAIM WAS CHANGED ON SAFETY GROUNDS. The video's answer to "it cannot
generate images" is "go to Gemini or ChatGPT". For a regulated pharmacy that
routing decision belongs to the AI Use Policy, not to a training board, so beat 6
says "a real one, or one from a tool you are allowed to use" and names no
third-party model.

THE PLAN FACT IS STATED POSITIVELY, unlike Day 3's memory beat and Day 8's Cowork
beats. Those hedge ("you may not see this") because the feature is OFF by default
on Team. Claude Design is DEFAULT ON for Team and default off for Enterprise, and
Phlo is on Team - so the honest line is "on unless an admin turned it off". That
fact is on the card, not the board.

THE ADVERSARIAL BEAT (8) CARRIES ITS OWN CATCH. Step 5 of the loop tells you to
ask Claude to review its own work, and it does that well - readability, hierarchy,
contrast, accessibility. The failure is that this is the same pair of eyes on
content it invented, and it reads exactly like diligence. The catch is to make it
render the states it never drew - empty, refused, real volume - which is
Anthropic's own design-review guidance written as one falsifiable sentence, in the
shape Day 10's beat 6 established. This beat is the Best Catch feeder, and the
demo badge sits here because this is the payload.

ONE COLOUR IS HELD CONSTANT ACROSS THREE BOARDS: GREEN = the human pass. Day 10
closes on it, Day 13 closes on it, beat 9 here closes on it. Deliberately no
second object-colour system - Day 13 already owns blue = design.md,
green = design system, teal = template, and beat 1 draws those three as neutral
chips rather than re-using the semantics out of context.

Style B (house style): a single hand-drawn journey, left-to-right, NO frames, NO
boxes, white canvas, everything in the hand font (fontFamily 1), roughness 1, a
lively colour-coded Excalidraw palette, big colour blocking, scribbled
annotations and charming primitive illustrations. The look lives in the shared
excalidraw_kit; this file holds only the composition and the bespoke one-offs.

PAN ORDER (left to right - the whitespace between slots IS the camera; frame one
beat at a time):

     1  ORANGE  you already have the habits   <- the brief reminder. Keep it short
     2  VIOLET  the loop, six steps           <- the spine. The ONLY numbered thing
     3  BLUE    a spec in, wireframes out     <- + prototype inside the meeting
     4  TEAL    hand it to whoever builds it  <- the package, and who can do what
     5  INDIGO  explore before you commit     <- three directions, then the best bits
     6  ORANGE  one input, many outputs       <- one-pagers, roadmaps, templates
     7  YELLOW  motion graphics for video     <- + the fastest-dating line here
     8  RED     it checks its own work        <- adversarial + [CUT TO CLAUDE DESKTOP]
     9  GREEN   where it stops, and who owns it

RUNTIME (budgeted in WORDS first, because budgeting in seconds is how Day 10 and
the first draft of this board both overran, then MEASURED against the script):
     beats are not uniform. Measured at 150 wpm, from the script:
        b1 20s  b2 46s  b3 40s  b4 29s  b5 38s  b6 25s  b7 34s
        b8 58s (+15s cut-away)  b9 36s
        hook 11s  why 25s  pause-and-try 13s  close 14s
     See the script header for the measured total. Hard cap 8, target 4 to 6.
     Beat 8 is the longest on purpose; everything else was trimmed to pay for it.
     Shorter cut: drop beats 4 and 6. Never drop 8.

Run:  python3 videos/ai-training/11-design-workflows/build_design_workflows.py
      /usr/bin/python3 preview.py videos/ai-training/11-design-workflows/claude-design-workflows.excalidraw out.png
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

random.seed(110911)  # deterministic - re-runs produce identical files

# ----------------------------------------------------------------------------
# BEAT SCAFFOLD - nine beats, wide gaps so one frames cleanly on a 14" laptop
# ----------------------------------------------------------------------------
N = 9
GAP = 800
# every beat uses the SAME slot, shaped ~1.15:1 (content ~1120 wide x ~980 tall,
# the heading at y60 counted in) so framing is identical on a 14" laptop.
WID = {i: 1200 for i in range(1, N + 1)}
ACCENT = {1: ORANGE, 2: VIOLET, 3: BLUE, 4: TEAL, 5: INDIGO, 6: ORANGE,
          7: YELLOW, 8: RED, 9: GREEN}
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
def doc_page(x, y, w, h, accent=BLUE, abg=BLUE_BG, lines=6, title=True):
    """A page of prose - the input you prepared before you opened anything."""
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="doc")
    if title:
        rect(x + 0.10 * w, y + 0.09 * h, 0.52 * w, 0.09 * h, stroke="transparent",
             bg=abg, sw=1, rough=1, rounded=True, prefix="doch")
    for k in range(lines):
        f = 0.80 if k % 3 else 0.56
        line(x + 0.10 * w, y + (0.28 + k * 0.10) * h, [[0, 0], [f * w, 0]],
             stroke=GREY, sw=2)


def wire_screen(x, y, w, h, kind="list", accent=GREY, abg=FAINT):
    """One wireframe screen: grey boxes, no styling, arguable in ten minutes.

    `kind` picks the layout so a row of screens reads as a flow rather than three
    copies. Grey on purpose - a wireframe that looks finished is not a wireframe."""
    rect(x, y, w, h, stroke=GREYD, bg=WHITE, sw=2, rough=1, rounded=True, prefix="wsc")
    rect(x + 0.08 * w, y + 0.07 * h, 0.60 * w, 0.09 * h, stroke="transparent", bg=abg,
         sw=1, rough=1, rounded=True, prefix="wsb")
    if kind == "list":
        for k in range(3):
            rect(x + 0.08 * w, y + (0.26 + k * 0.20) * h, 0.84 * w, 0.15 * h,
                 stroke=GREY, bg=WHITE, sw=2, rough=1, rounded=True, prefix="wsb")
    elif kind == "form":
        for k in range(3):
            rect(x + 0.08 * w, y + (0.26 + k * 0.18) * h, 0.84 * w, 0.12 * h,
                 stroke=GREY, bg=WHITE, sw=2, rough=1, rounded=True, prefix="wsb")
        rect(x + 0.08 * w, y + 0.82 * h, 0.34 * w, 0.11 * h, stroke=GREYD, bg=abg,
             sw=2, rough=1, rounded=True, prefix="wsb")
    else:  # confirm
        ellipse(x + 0.40 * w, y + 0.30 * h, 0.20 * w, 0.20 * w, stroke=GREY, bg=WHITE,
                sw=2, rough=1, prefix="wsb")
        line(x + 0.20 * w, y + 0.66 * h, [[0, 0], [0.60 * w, 0]], stroke=FAINT, sw=3)
        line(x + 0.28 * w, y + 0.78 * h, [[0, 0], [0.44 * w, 0]], stroke=FAINT, sw=3)


def bundle(x, y, w, h, accent=TEAL, abg=TEAL_BG, items=()):
    """The handoff parcel: one package holding the designs, the conversation and a
    written brief. Drawn as a taped box rather than a folder - a folder reads as a
    Project, and violet folders mean something else in this repo."""
    rect(x, y, w, h, stroke=accent, bg=WHITE, sw=3, rough=1, rounded=True, prefix="bnd")
    line(x, y + 52, [[0, 0], [w, 0]], stroke=accent, sw=2)
    rect(x + w / 2 - 46, y - 12, 92, 30, stroke=accent, bg=abg, sw=2, rough=1,
         rounded=False, fill="solid", angle=jit(1.6), opacity=80, prefix="tape")
    for k, it in enumerate(items):
        iy = y + 82 + k * 62
        rect(x + 26, iy, 34, 42, stroke=INK, bg=abg, sw=2, rough=1, rounded=True,
             prefix="bit")
        text(x + 78, iy + 6, it, size=SMALL, color=INK)


def image_slot(x, y, w, h, accent=ORANGE, abg=ORANGE_BG, label="1200 x 628"):
    """The gap a code-drawn design leaves where a photograph should be: a crossed
    box with the size marked on it. The beat-6 limit drawn rather than asserted -
    it can draw the space, it cannot fill it."""
    rect(x, y, w, h, stroke=GREYD, bg=WHITE, sw=2, rough=1, rounded=True, prefix="ims")
    line(x, y, [[0, 0], [w, h]], stroke=FAINT, sw=2)
    line(x, y + h, [[0, 0], [w, -h]], stroke=FAINT, sw=2)
    rect(x + w / 2 - 72, y + h / 2 - 24, 144, 48, stroke=accent, bg=abg, sw=2, rough=1,
         rounded=True, prefix="imsl")
    text_centered(x + w / 2, y + h / 2 - 12, label, size=SMALL, color=accent)


def ref_card(x, y, w, h, accent=INDIGO, abg=INDIGO_BG):
    """A pasted reference - the thing you already like, taped to the brief. Tape
    rather than a paperclip: a clip drawn at this scale reads as a stray rectangle."""
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=3, rough=1, rounded=True, prefix="ref")
    rect(x + 20, y + 30, w - 40, 0.26 * h, stroke=GREYD, bg=abg, sw=2, rough=1,
         rounded=True, prefix="refh")
    line(x + 20, y + 0.42 * h, [[0, 0], [(w - 40) * 0.58, 0]], stroke=FAINT, sw=3)
    for k in range(3):
        rect(x + 20 + k * (w - 40) / 3, y + 0.52 * h, (w - 40) / 3 - 16, 0.3 * h,
             stroke=GREYD, bg=WHITE, sw=2, rough=1, rounded=True, prefix="refc")
    for tx, ta in ((x + 14, -0.45), (x + w - 82, 0.45)):
        rect(tx, y - 12, 68, 26, stroke=accent, bg=abg, sw=2, rough=1, rounded=False,
             fill="solid", angle=ta, opacity=75, prefix="tape")


def direction(x, y, w, h, accent, abg, variant=0, chosen=False):
    """One exploration. `variant` moves the blocks around so three of them read as
    three real alternatives rather than three copies; `chosen` rings it."""
    layouts = [(0.10, 0.34, 0.66), (0.62, 0.12, 0.36), (0.34, 0.62, 0.10)]
    a, b, c = layouts[variant % 3]
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="dir")
    rect(x + 0.09 * w, y + a * h, 0.82 * w, 0.16 * h, stroke="transparent", bg=accent,
         sw=1, rough=1, rounded=True, prefix="dirb")
    rect(x + 0.09 * w, y + b * h, 0.82 * w, 0.22 * h, stroke=GREYD, bg=abg, sw=2,
         rough=1, rounded=True, prefix="dirb")
    for k in range(2):
        rect(x + (0.09 + 0.44 * k) * w, y + c * h, 0.36 * w, 0.20 * h, stroke=GREYD,
             bg=WHITE, sw=2, rough=1, rounded=True, prefix="dirb")
    if chosen:
        circle_around(x - 16, y - 16, w + 32, h + 32, accent)


def frames_strip(x, y, w, h, n=4, accent=YELLOW, abg=YELLOW_BG):
    """A row of animation frames with a play head under it - the same graphic at
    four moments, which is the only honest way to draw motion on a static board."""
    fw = (w - (n - 1) * 16) / n
    for k in range(n):
        fx = x + k * (fw + 16)
        rect(fx, y, fw, h, stroke=GREYD, bg=WHITE, sw=2, rough=1, rounded=True,
             prefix="frm")
        grow = 0.20 + 0.22 * k
        rect(fx + 0.14 * fw, y + h * (0.74 - grow * 0.6), 0.30 * fw, grow * h * 0.6,
             stroke="transparent", bg=accent, sw=1, rough=1, rounded=True, prefix="frb")
        rect(fx + 0.54 * fw, y + h * 0.52, 0.32 * fw, 0.10 * h, stroke="transparent",
             bg=abg, sw=1, rough=1, rounded=True, prefix="frb")
        line(fx + 0.14 * fw, y + h * 0.86, [[0, 0], [fw * 0.62, 0]], stroke=FAINT, sw=3)
    line(x, y + h + 30, [[0, 0], [w, 0]], stroke=GREY, sw=3)
    for k in range(n):
        fx = x + k * (fw + 16) + fw / 2
        ellipse(fx - 7, y + h + 23, 14, 14, stroke=accent, bg=accent, sw=2, prefix="pip")


def talking_head(cx, cy, r=34, color=GREYD):
    """A presenter: head and shoulders in a frame corner - the thing the motion
    graphic sits next to, so beat 7 reads as 'over video', not 'a video'."""
    ellipse(cx - r, cy - r, 2 * r, 2 * r, stroke=color, bg=WHITE, sw=3, rough=1,
            prefix="thhead")
    # shoulders start below the head, not through it - at this scale a 34px head
    # and a -38 shoulder rise cross each other and read as a collar, not a person
    line(cx - 42, cy + 78, [[0, 0], [0, -16], [16, -36], [68, -36], [84, -16], [84, 0]],
         stroke=color, sw=3, rough=1, prefix="thbody")


def comment_pin(cx, cy, color=INDIGO, abg=INDIGO_BG, s=1.0):
    """A dropped comment: a small rounded bubble with a tail, pinned to one spot."""
    rect(cx - 34 * s, cy - 30 * s, 68 * s, 44 * s, stroke=color, bg=abg, sw=2, rough=1,
         rounded=True, fill="solid", prefix="cmt")
    line(cx - 10 * s, cy + 14 * s, [[0, 0], [6 * s, 18 * s], [20 * s, 0]], stroke=color,
         sw=2, rough=1, bg=abg, fill="solid", prefix="cmtt")
    for k in range(2):
        line(cx - 20 * s, cy - 16 * s + k * 14 * s, [[0, 0], [40 * s, 0]], stroke=color,
             sw=2)


def data_rows(x, y, w, n=3, accent=GREY, short=True):
    """Rows of invented sample content - three tidy names that always fit."""
    for k in range(n):
        ry = y + k * 40
        rect(x, ry, w, 30, stroke=GREY, bg=WHITE, sw=2, rough=1, rounded=True,
             prefix="row")
        line(x + 14, ry + 15, [[0, 0], [(0.34 if short else 0.92) * w, 0]],
             stroke=accent, sw=3)


def human_gate(cx, cy, color=GREEN, abg=GREEN_BG, s=1.0):
    """The human-in-loop marker - head plus rounded shoulders, filled.

    Safety-bearing, so it does not use the kit's person(), which is sized for a
    crowd of tiny figures and reads as a paper dart standing alone. Same helper
    and same green as Day 10's and Day 13's closing beats, on purpose."""
    r = 26 * s
    ellipse(cx - r, cy - 62 * s, 2 * r, 2 * r, stroke=color, bg=WHITE, sw=3, rough=1,
            prefix="hghead")
    line(cx - 50 * s, cy + 46 * s,
         [[0, 0], [0, -22 * s], [18 * s, -50 * s], [82 * s, -50 * s],
          [100 * s, -22 * s], [100 * s, 0]],
         stroke=color, sw=3, rough=1, bg=abg, fill="solid", prefix="hgbody")


# ----------------------------------------------------------------------------
# THE WORKED EXAMPLE - one internal holiday-request tool, carried across beats
# 2, 3, 4 and 8. Everyday business, never Phlo-specific, no patient or clinical
# detail. Beat 8's three states are exactly the states beat 3's wireframe never
# drew, so the two beats are one story: the shape you agreed, and the shape you
# never checked. Change the tool and all four beats move together.
# ----------------------------------------------------------------------------
TOOL = "a holiday-request tool"
# The six steps. This is the ONLY numbered process on the board.
LOOP = [("prep the input", "the spec, the notes, the\nscreenshots - gathered first"),
        ("start simple", "two or three sentences.\nNot a specification"),
        ("read the first draft", "all of it, before you\ntouch anything"),
        ("refine wide, then narrow", "one whole-page pass, then\none element, then one more"),
        ("ask it to review", "it audits its own work.\nSee beat 8 before you trust it"),
        ("get it out", "export it, or hand the\nwhole package over")]
# The catch on beat 8. One sentence, falsifiable by looking, naming the three
# things Claude cannot invent for itself: no data, a refusal, and real volume.
CATCH = "'show me this with no requests at all, one that was\nrefused and forty rows - one name sixty characters long'"

# ============================================================================
# BOARD TITLE
# ============================================================================
text(OX[1], -300, "Claude Design, job by job", size=HERO, color=INK)
text(OX[1] + 6, -300 + HERO * LINE_H + 4,
     "one loop, seven jobs, and the review that only looks like a review",
     size=H2, color=ORANGE)

# ============================================================================
# BEAT 1 - YOU ALREADY HAVE THE HABITS   (the brief reminder - keep it SHORT)
# ============================================================================
ox = beat_head(1, "you already have the habits",
               "Day 10 gave you the judgement. Day 13 gives you the files that make it\nstick. One minute on both, and then today is the jobs themselves.")
text(ox + 50, 300, "from Day 10, in four lines", size=SMALL, color=GREY)
for k, hab in enumerate(["reference beats adjectives",
                         "structure before polish",
                         "one element at a time",
                         "presentable is not correct"]):
    chip(ox + 50, 342 + k * 78, hab, fill=WHITE, text_color=ORANGE, border=ORANGE,
         size=LABEL)
text(ox + 620, 300, "and Day 13 goes deep on these", size=SMALL, color=GREY)
for k, (nm, cap) in enumerate([("design.md", "the rules, written down"),
                               ("design system", "those rules, built in"),
                               ("template", "how a deck is laid out")]):
    ry = 346 + k * 98
    rect(ox + 620, ry, 56, 68, stroke=GREYD, bg=WHITE, sw=2, rough=1, rounded=True,
         prefix="rem")
    rect(ox + 620, ry, 56, 15, stroke="transparent", bg=ORANGE_BG, sw=1, rough=1,
         rounded=True, prefix="remh")
    text(ox + 700, ry + 4, nm, size=BODY, color=INK)
    text(ox + 700, ry + 38, cap, size=SMALL, color=GREY)
chip(ox + 620, 650, "prepare once, inherit forever - Day 13", fill=WHITE,
     text_color=ORANGE, border=ORANGE, size=SMALL)
chip(ox + 620, 718, "a full on-brand deck - Day 12, Claude PowerPoint",
     fill=WHITE, text_color=ORANGE, border=ORANGE, size=SMALL)
text(ox + 50, 792, "today is the jobs themselves", size=H3, color=ORANGE)
text(ox + 50, 846,
     "Wireframes, a landing page, one-pagers, roadmaps, motion graphics - and one\nsix-step loop that runs underneath every single one of them.",
     size=BODY, color=GREYD)
chip(ox + 50, 946, "a reminder, not a re-run", fill=ORANGE_BG, text_color=ORANGE,
     border=ORANGE, size=LABEL)

# ============================================================================
# BEAT 2 - THE LOOP, SIX STEPS   (the spine - the ONLY numbered thing on the board)
# ============================================================================
ox = beat_head(2, "the loop, six steps",
               "Every job below runs this same loop. Most people do one, two and six,\nthen wonder why the middle took all afternoon.")
for k, (nm, cap) in enumerate(LOOP):
    bx = ox + 40 + (k % 3) * 368
    by = 292 + (k // 3) * 208
    rect(bx, by, 330, 168, stroke=VIOLET, bg=WHITE, sw=3, rough=1, rounded=True,
         prefix="stp")
    rect(bx, by, 330, 52, stroke="transparent", bg=VIOLET_BG, sw=1, rough=1,
         rounded=True, prefix="stph")
    num_badge(bx + 14, by + 6, k + 1, VIOLET, d=38)
    text(bx + 62, by + 12, nm, size=LABEL, color=VIOLET)
    text(bx + 24, by + 84, cap, size=SMALL, color=INK)
text(ox + 40, 706, "inside step four, match the channel to the size of the change",
     size=SMALL, color=GREY)
_cx = ox + 40
for lab in ["comment on the element - one thing, in one place",
            "chat - structure, or the whole page"]:
    _w, _h = chip(_cx, 740, lab, fill=WHITE, text_color=VIOLET, border=VIOLET, size=SMALL)
    _cx += _w + 24
text(ox + 40, 812,
     "Steps three and four are the job. The first draft is not the output, it is\nthe thing you are about to argue with.",
     size=BODY, color=GREYD)
chip(ox + 40, 908, "typing the same three corrections every week? that is a Skill - Day 7",
     fill=WHITE, text_color=VIOLET, border=VIOLET, size=SMALL)
chip(ox + 40, 976, "wide, then narrow, then wide", fill=VIOLET_BG, text_color=VIOLET,
     border=VIOLET, size=LABEL)

# ============================================================================
# BEAT 3 - A SPEC IN, WIREFRAMES OUT
# ============================================================================
ox = beat_head(3, "a spec in, wireframes out",
               "The document nobody can picture becomes screens people can click through.\nGrey boxes, on purpose.")
text(ox + 40, 292, "what you hand it", size=SMALL, color=GREY)
doc_page(ox + 40, 330, 210, 262, accent=BLUE, abg=BLUE_BG)
text(ox + 40, 610, "the spec for\n" + TOOL, size=SMALL, color=GREYD)
arrow(ox + 272, 448, [[0, 0], [58, 0]], stroke=BLUE, sw=5, rough=1)
text(ox + 356, 292, "it asks before it builds", size=SMALL, color=GREY)
sticky(ox + 356, 330, 430, 262, BLUE_T, angle=jit(1.2))
for k, q in enumerate(["who approves - one manager, or two?",
                       "can a request be withdrawn?",
                       "does anyone else need to see it?"]):
    text(ox + 386, 362 + k * 74, q, size=SMALL, color=INK)
text(ox + 356, 610, "answer these properly - it is the cheapest\nfive minutes in the whole job",
     size=SMALL, color=GREYD)
text(ox + 830, 292, "what comes back", size=SMALL, color=GREY)
for k, kind in enumerate(["list", "form", "confirm"]):
    wy = 330 + k * 186
    wire_screen(ox + 830, wy, 230, 156, kind=kind)
    if k < 2:
        arrow(ox + 944, wy + 162, [[0, 0], [0, 18]], stroke=BLUE, sw=3, rough=1)
text(ox + 830, 892, "clickable, not pretty", size=SMALL, color=BLUE)
text(ox + 40, 700,
     "Nobody argues with grey boxes for long, which is exactly why you want them.\nSettle what the screens are and in what order, while that is still free.",
     size=BODY, color=GREYD)
chip(ox + 40, 806, "settle the shape before anything is styled", fill=BLUE_BG,
     text_color=BLUE, border=BLUE, size=LABEL)
chip(ox + 40, 884, "same move inside a meeting: leave with the prototype, not the notes",
     fill=WHITE, text_color=BLUE, border=BLUE, size=SMALL)

# ============================================================================
# BEAT 4 - HAND IT TO WHOEVER BUILDS IT
# ============================================================================
ox = beat_head(4, "hand it to whoever builds it",
               "A prototype is not a build. What travels is a package: the designs, the\nconversation that produced them and a written brief.")
text(ox + 40, 296, "one package", size=SMALL, color=GREY)
bundle(ox + 40, 336, 420, 300, items=["the designs themselves",
                                      "the conversation behind them",
                                      "a written brief for whoever picks it up"])
arrow(ox + 484, 476, [[0, 0], [72, 0]], stroke=TEAL, sw=5, rough=1)
text(ox + 596, 296, "goes to", size=SMALL, color=GREY)
for k, (who, what) in enumerate([("Claude Code", "builds it, with the package as the brief"),
                                 ("a developer", "reads the same three things you did"),
                                 ("a designer", "picks it up and takes it further")]):
    ry = 340 + k * 96
    rect(ox + 596, ry, 46, 46, stroke=TEAL, bg=TEAL_BG, sw=2, rough=1, rounded=True,
         prefix="dst")
    text(ox + 668, ry + 2, who, size=BODY, color=TEAL)
    text(ox + 668, ry + 38, what, size=SMALL, color=GREYD)
text(ox + 40, 690, "and if you are only sharing it", size=SMALL, color=GREY)
for k, (lvl, what) in enumerate([("view", "they can look"),
                                 ("comment", "they can mark it up - you still hold the pen"),
                                 ("edit", "they can change it. Give this one on purpose")]):
    ry = 730 + k * 58
    chip(ox + 40, ry, lvl, fill=WHITE, text_color=TEAL, border=TEAL, size=SMALL)
    text(ox + 216, ry + 10, what, size=SMALL, color=GREYD)
chip(ox + 40, 924, "a prototype is a brief, not a build", fill=TEAL_BG,
     text_color=TEAL, border=TEAL, size=LABEL)

# ============================================================================
# BEAT 5 - EXPLORE BEFORE YOU COMMIT   (deliberately UNNUMBERED - see docstring)
# ============================================================================
ox = beat_head(5, "explore before you commit",
               "Ask for one thing and you get the house style - the layout this tool\nreaches for by default. Ask for three and you get a choice.")
text(ox + 40, 292, "start from what you like", size=SMALL, color=GREY)
ref_card(ox + 40, 334, 240, 196)
text(ox + 40, 548, "two or three references,\nnot two or three adjectives", size=SMALL,
     color=GREYD)
arrow(ox + 300, 424, [[0, 0], [50, 0]], stroke=INDIGO, sw=5, rough=1)
text(ox + 380, 292, "ask for three directions, not one", size=SMALL, color=GREY)
for k in range(3):
    direction(ox + 380 + k * 245, 334, 215, 196, INDIGO, INDIGO_BG, variant=k)
    text_centered(ox + 380 + k * 245 + 107, 548, "ABC"[k], size=H3, color=INDIGO)
text(ox + 40, 626, "then say what worked in each - and only then build one",
     size=H3, color=INDIGO)
_cx = ox + 40
for lab in ["A: the layout", "B: the colour", "C: the way type is used"]:
    _w, _h = chip(_cx, 684, lab, fill=WHITE, text_color=INDIGO, border=INDIGO, size=SMALL)
    _cx += _w + 22
direction(ox + 40, 764, 250, 190, INDIGO, INDIGO_BG, variant=1, chosen=True)
tick(ox + 322, 836, GREEN)
text(ox + 380, 772,
     "One direction, assembled out of the parts that earned their place. It costs\nyou one extra round and it is the difference between something that is\nyours and something that looks like everything else this tool makes.",
     size=BODY, color=GREYD)
chip(ox + 380, 906, "comparing beats guessing", fill=INDIGO_BG, text_color=INDIGO,
     border=INDIGO, size=LABEL)

# ============================================================================
# BEAT 6 - ONE INPUT, MANY OUTPUTS   (short chip beat + the one durable limit)
# ============================================================================
ox = beat_head(6, "one input, many outputs",
               "The same notes you already have go to four different jobs. You are not\nstarting again each time - you are re-pointing one input.")
text(ox + 40, 300, "one set of notes", size=SMALL, color=GREY)
doc_page(ox + 40, 340, 200, 250, accent=ORANGE, abg=ORANGE_BG)
for k in range(4):
    arrow(ox + 262, 430 + k * 12, [[0, 0], [86, (k - 1.5) * 96]], stroke=ORANGE, sw=3,
          rough=1)
for k, (lab, cap) in enumerate([("a one-pager", "the leave-behind for sales"),
                                ("a roadmap", "the same plan, drawn"),
                                ("a landing page", "the draft you argue with"),
                                ("social templates", "sized once, reused")]):
    ry = 316 + k * 92
    rect(ox + 380, ry, 44, 44, stroke=ORANGE, bg=ORANGE_BG, sw=2, rough=1,
         rounded=True, prefix="out")
    text(ox + 448, ry - 2, lab, size=BODY, color=INK)
    text(ox + 448, ry + 32, cap, size=SMALL, color=GREY)
text(ox + 820, 300, "where a picture should be", size=SMALL, color=GREY)
image_slot(ox + 820, 340, 260, 180)
text(ox + 820, 552, "it leaves the space, sized\nand marked. You bring the\npicture.", size=SMALL, color=GREYD)
text(ox + 40, 700, "the one thing it cannot do", size=SMALL, color=ORANGE)
sticky(ox + 40, 738, 1060, 140, ORANGE_T, angle=jit(0.8))
text(ox + 76, 764,
     "It draws everything with code - shapes, type, layout, motion. It does not\ntake photographs. Where a picture is needed it leaves you a space the right\nsize, and you bring a real one, or one from a tool you are allowed to use.",
     size=BODY, color=INK)
chip(ox + 40, 916, "it can draw anything and photograph nothing", fill=ORANGE_BG,
     text_color=ORANGE, border=ORANGE, size=LABEL)

# ============================================================================
# BEAT 7 - MOTION GRAPHICS FOR VIDEO   (carries the fastest-dating line here)
# ============================================================================
ox = beat_head(7, "motion graphics for video",
               "Hand it the transcript of a video you have already recorded, and it draws\nthe graphics that go over the top of you talking.")
text(ox + 40, 292, "your transcript", size=SMALL, color=GREY)
doc_page(ox + 40, 332, 200, 240, accent=YELLOW, abg=YELLOW_BG)
text(ox + 40, 590, "what you actually said,\nwith the timings", size=SMALL, color=GREYD)
talking_head(ox + 140, 700, 34, GREYD)
text_centered(ox + 140, 782, "you, on camera", size=SMALL, color=GREY)
arrow(ox + 262, 452, [[0, 0], [58, 0]], stroke=YELLOW, sw=5, rough=1)
text(ox + 350, 292, "the graphic, at four moments", size=SMALL, color=GREY)
frames_strip(ox + 350, 332, 730, 240, n=4)
text(ox + 350, 634, "the animation lands on the word you say it on - that is the whole trick",
     size=BODY, color=GREYD)
text(ox + 350, 700, "then you edit it in plain English: slower, hold that number longer,\ndrop the third one entirely.",
     size=BODY, color=GREYD)
# the caveat, and it is the fastest-dating line on this board
highlighter(ox + 40, 828, 1080, 96, YELLOW_T, angle=0.0)
diamond(ox + 58, 852, 44, 44, stroke=YELLOW, bg=YELLOW_BG, sw=3)
text_centered(ox + 80, 856, "!", size=H3, color=YELLOW)
text(ox + 126, 844,
     "Getting it out is the rough edge: it plays in the browser, so you capture it\noff the screen and drop that into your editor.",
     size=BODY, color=GREYD)
chip(ox + 40, 946, "it follows the words, not a timeline", fill=YELLOW_BG,
     text_color=YELLOW, border=YELLOW, size=LABEL)

# ============================================================================
# BEAT 8 - IT CHECKS ITS OWN WORK   (adversarial: the failure AND the catch)
# ============================================================================
ox = beat_head(8, "it checks its own work",
               "Step five said ask it to review. It does that well - and it is still the\nsame pair of eyes, on content it invented.")
for k, (ttl, cap) in enumerate([
        ("the check you never see", "it holds its output against your design\nsystem and fixes it before you look"),
        ("the check you ask for", "readability, hierarchy, contrast, whether\nit is accessible - a real audit")]):
    bx = ox + 40 + k * 548
    text(bx, 288, ttl, size=H3, color=RED)
    text(bx, 340, cap, size=SMALL, color=GREYD)
tick(ox + 40, 416, GREEN)
text(ox + 86, 410, "both of these are real, and both of them are worth having", size=SMALL,
     color=GREYD)
text(ox + 40, 472, "what neither one can see", size=SMALL, color=RED)
text(ox + 40, 506, "it reviewed the screen it drew, with the data it invented", size=H3,
     color=RED)
data_rows(ox + 40, 560, 420, n=3)
text(ox + 490, 562, "three requests. Three short names.\nEverything fits, because it chose\nwhat had to fit.", size=SMALL, color=GREYD)
xmark(ox + 492, 648, RED, s=22)
text(ox + 536, 642, "nobody has ever had zero holidays booked", size=SMALL, color=RED)
text(ox + 40, 706, "the catch", size=SMALL, color=RED)
text(ox + 40, 740, "make it draw the states it never drew", size=H3, color=RED)
sticky(ox + 40, 796, 1060, 96, RED_T, angle=jit(1.0))
text(ox + 76, 818, CATCH, size=BODY, color=INK)
text(ox + 40, 912,
     "Empty, refused and far too many. Ask for those three by name - they are the\nones it will not think of, and the only ones your team will actually hit.",
     size=BODY, color=GREYD)
demo_badge(ox + 40, 1000,
           "show in Claude desktop app: Design - ask it to review, then ask for the empty state")

# ============================================================================
# BEAT 9 - WHERE IT STOPS, AND WHO OWNS IT   (the close)
# ============================================================================
ox = beat_head(9, "where it stops, and who owns it",
               "It is an exploration tool and a very good first draft. Four jobs belong\nsomewhere else, and one of them belongs to a person.")
text(ox + 40, 292, "hand these on", size=SMALL, color=GREY)
for k, (job, where) in enumerate([
        ("production-ready code", "the handoff bundle, into Claude Code"),
        ("pixel-perfect production design", "your design tool - this is a draft, not a spec"),
        ("final polish and publishing", "your brand tool, where the sizing lives"),
        ("a full animated explainer video", "a video editor. This is graphics, not films")]):
    ry = 332 + k * 78
    rect(ox + 40, ry, 34, 34, stroke=GREEN, bg=GREEN_BG, sw=2, rough=1, rounded=True,
         prefix="stop")
    text(ox + 96, ry - 2, job, size=BODY, color=INK)
    text(ox + 96, ry + 30, where, size=SMALL, color=GREY)
text(ox + 40, 664,
     "Fast drafts mean more drafts, which means more things arriving that look\nfinished. The last pass matters more as the tool gets better, not less.",
     size=BODY, color=GREYD)
wire_screen(ox + 700, 322, 170, 130, kind="form")
arrow(ox + 886, 384, [[0, 0], [46, 0]], stroke=GREEN, sw=5, rough=1)
human_gate(ox + 1010, 408, GREEN, GREEN_BG, s=0.9)
tick(ox + 700, 500, GREEN)
text(ox + 746, 494, "a person signs it off,\nthen it goes out", size=SMALL, color=GREEN)
# the data rule - red, because it is the only on-screen data-handling rule here
highlighter(ox + 40, 770, 1080, 132, RED_BG, angle=0.0)
diamond(ox + 58, 800, 44, 44, stroke=RED, bg=RED_BG, sw=3)
text_centered(ox + 80, 804, "!", size=H3, color=RED)
text(ox + 126, 788,
     "A shared design is a shared file. Nothing confidential goes in - no private\ncodebase, no unapproved work, nothing patient-facing - and anything that\ntouches records keeps the gate: Claude drafts, a person approves.",
     size=BODY, color=RED)
chip(ox + 40, 928, "nothing goes out without the human pass", fill=GREEN_BG,
     text_color=GREEN, border=GREEN, size=LABEL)
chip(ox + 40, 1000, "a strong first draft is the product, not the finished thing",
     fill=WHITE, text_color=GREEN, border=GREEN, size=LABEL)

# No connector spine, no inter-beat arrows and no footer: the nine beats read as
# one picture through consistent shape and rhythm, and the whitespace is the camera.

# ----------------------------------------------------------------------------
# WRITE + VALIDATE  (shared excalidraw_kit; hard-fails on frames / off-palette)
# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "claude-design-workflows.excalidraw")
MAXW = max(WID.values()) + 200
finish(out, MAXW, TOTAL_W)
