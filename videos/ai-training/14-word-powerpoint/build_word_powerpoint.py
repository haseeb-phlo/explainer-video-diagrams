#!/usr/bin/env python3
"""Build claude-word-powerpoint.excalidraw - ONE flowing, illustrated explainer for
DAY 14 of the Phlo AI training: "Claude in Microsoft Word and PowerPoint"
(~7 min 30, hard cap 8).

WHAT THIS BOARD IS - a MERGE, not a compilation
-----------------------------------------------
This is the Word video and the PowerPoint video combined into ONE board and ONE
Loom, at the user's request (2026-09-14). It is a NEW DAY 14. Nothing was
retired to make room: Day 12 (videos/ai-training/12-powerpoint/) and the older
module-2.9 Word walkthrough (videos/claude/9-claude-word/) both stay exactly
where they are and keep building. That was an explicit decision - "leave
everything as it is and just create a new day video" - so a future reader should
NOT read this board as a move, and should not delete either predecessor on the
strength of it.

The two briefs are 7 beats each, which is ~10 minutes of narration and cannot be
one video. The merge is what makes 11 beats work, and it rests on one
observation: BOTH briefs have the same adversarial beat. "The rewrite that drops
a clause" and "the plausible deck" are the same failure - a fluent, well-made
output that passes review because review checks the surface. Fusing them into
ONE red beat (10) is what buys the room, and it honours the shared constraint
that exactly one beat per board is adversarial.

Three other things merged rather than duplicated:
  * Word beat 1 is DESIGNATED shared framing ("taught once"), so it carries the
    thesis for both halves and absorbs PowerPoint's "it looks finished and says
    nothing" - as the closing strip here, and as the setup on beat 6, where the
    deck with the missing argument is the reason to do structure first.
  * Word beat 2, the sidebar, is the SAME Microsoft 365 add-in family for both
    apps. Taught once, on both windows, in 20 seconds.
  * Both briefs close on a green demo beat. One green beat (11) carries both
    cut-aways' payload; the deck cut-away moved up to beat 6, where agreeing an
    outline in chat is the thing being taught.

ONE WORKED EXAMPLE RUNS THE WHOLE BOARD. A generic packaging-supplier contract
that becomes a re-tender deck: the agreement is the document you edit (beats 1,
3, 4, 5), and the case for re-tendering is the deck you build (beats 6, 7, 8,
11). Beat 10 breaks both halves of it - the tightened clause quietly loses its
notice condition, and three decks never ask for the decision. This is what makes
the video ONE video rather than two halves sharing a canvas.
CHANGE THE EXAMPLE AND BEATS 1, 3, 4, 5, 6, 7, 8, 10 AND 11 ALL MOVE TOGETHER.

THE BOARD NAMES THE TOOLS, NEVER THE TIER. "Word" and "PowerPoint" appear in
the board title, on beat 2's two windows and in the demo badges, and nowhere
else - not one of the eleven headings needs either word. Plan tiers, the
Microsoft 365 add-in, the 30MB limit, file creation, template awareness,
governance and the prompt-injection warning are all on
`claude-word-powerpoint-resource-card.md`. That card is a deliverable, not an
afterthought: do not re-inflate the board with it, and WHEN A FACT MOVES, FIX
THE CARD, NOT THE BOARD. This is the same on-board / on-card line Day 12 drew,
and it is why the two halves' conflicting tier claims (the old Word script says
the add-in is "Pro and up"; the Day 12 card, verified 2026-09-14, says GA on
Pro, Max, Team AND Enterprise, re-verified 2026-09-16) are a card problem
here and not a board problem.

BEAT 5 IS THE FASTEST-DATING LINE ON THE BOARD. "Strong at the ends, thinner
through the middle" is a claim about model behaviour on long inputs, and it will
move. It earns board space because it changes what a person TYPES - ask for the
quote and the page, not the summary - which is the same filter Day 3 and Day 4
apply to their sources. Re-check it before re-recording, the same treatment Day
3's beat 15 and Day 11's beat 7 carry.

BEAT 9 IS SCOPED TO JUDGEMENT, NOT MECHANICS, and this is inherited from Day 12
where it was a documented correction. "Design is not its strength" means it will
not make BRAND DECISIONS for you. It demonstrably DOES respect a template you
hand it - the docs say it reads the slide master, layouts, fonts and colour
scheme and aims to maintain template compliance. So the right-hand column is
worded as DECISIONS ("which template to use", "what the brand actually is"),
never as objects ("the template"), and the narration must not drift into
claiming it ignores your template. That would contradict both the card and the
docs.

BEAT 3 AND BEAT 10 DELIBERATELY BREAK DIFFERENT CONDITIONS. Beat 3 rejects a
response time collapsing into "promptly"; beat 10 loses the renewal deadline. An
earlier draft used the SAME condition on both, which quietly wrecked beat 10: a
viewer who has just been shown catching that exact edit as a single tracked
change is then told it is the thing they would never catch. Keep them distinct.
Note also that LOST_CONDITION must restate the DEADLINE ("at least 30 days
before the Renewal Date"), never a duration ("30 days' notice") - paraphrasing it
loosely commits, ON THE ADVERSARIAL BEAT, the very error beat 3 teaches.

THE HUMAN GATE ON BEAT 9 IS GREEN, not the beat's teal and not Day 12's indigo.
Green = the human pass is held constant across Day 10, Day 11 and Day 13, and
that marker is safety-bearing in a mandatory course for a regulated pharmacy, so
it reads as the same rule here as it does there. It uses a bespoke human_gate()
rather than the kit's person(), which is sized for a crowd of tiny figures and
reads as a paper dart standing alone - the same call Day 10 and Day 12 made.

ACCENTS. The prose half runs orange / violet / blue / teal / indigo. The deck
half deliberately does NOT re-run that sequence - it opens on YELLOW, a colour
the prose half never uses, so the pivot at beat 6 is visible from the colour
alone before a word is read. No accent repeats on adjacent beats.

Style B (house style): a single hand-drawn journey, left-to-right, NO frames, NO
boxes, white canvas, everything in the hand font (fontFamily 1), roughness 1, a
lively colour-coded Excalidraw palette, big colour blocking, scribbled
annotations and charming primitive illustrations. The look lives in the shared
excalidraw_kit; this file holds only the composition and the bespoke one-offs.
(Scene template: videos/claude/3-artefacts/build_excalidraw.py, by way of Day
12's build_powerpoint.py, which is the closest existing board - its slide,
slide_deck, headline_slide, chat_panel and outline_rows one-offs are re-declared
here, because bespoke illustrations belong to the build that needs them and
never to the kit.)

PAN ORDER (left to right - the whitespace between slots IS the camera; frame one
beat at a time):

   -- the document half -------------------------------------------------
     1  ORANGE  the document already exists   <- shared framing, taught once
     2  VIOLET  it lives in the sidebar       <- orientation, both apps, 20s
     3  BLUE    review as a diff
     4  TEAL    revise, do not rewrite
     5  INDIGO  it can read the whole thing   <- fastest-dating line on the board
   -- the deck half -----------------------------------------------------
     6  YELLOW  structure first, slides second    <- the pivot [CUT TO CLAUDE]
     7  VIOLET  one idea per slide, one line that carries it
     8  BLUE    build it from a source
     9  TEAL    design is not its strength        <- honest beat; the pass is human
   -- both --------------------------------------------------------------
    10  RED     plausible passes review   <- adversarial: BOTH failures, ONE catch
    11  GREEN   do it live, on real work  <- [CUT TO CLAUDE DESKTOP], then close

RUNTIME (budgeted in seconds, then MEASURED against the written narration - the
measuring is the step that matters; this repo's one recorded process lesson is
that per-beat second budgets drift by 2x against written prose):
     beats are not uniform. MEASURED at 150 wpm from claude-word-powerpoint-
     script.md, not budgeted - the first draft measured 8 min 17 against a
     6 min 42 budget, which is this repo's recorded 2x drift happening again:
        b1 38s  b2 24s  b3 33s  b4 26s  b5 23s  b6 36s  b7 26s
        b8 21s  b9 23s  b10 76s  b11 32s
        hook 9s   why 28s   pause-and-try + close 27s
     1,086 spoken words = 7 min 14, plus ~30s across the two cut-aways where
     the doing takes longer than the saying = ~7 min 44.
     Hard cap 8 minutes - 16 seconds of headroom. RE-MEASURE IF YOU REWRITE.
     (Was 1,053 / ~7 min 31. On 2026-09-17 the Outlook add-in Loom was attached
     to this Day and the pause-and-try was widened from two strands to three -
     document, deck, reply - which cost ~8s. THE BOARD WAS NOT CHANGED: it is
     still Word and PowerPoint, and the Outlook board is Day 16. The measuring
     command now lives in the script header.)
     Beat 10 is the longest on purpose; everything else was trimmed to pay for
     it. Shorter cut: beats 8 and 9 are the droppable pair (-44s, ~6 min 48) -
     nothing later depends on either. NEVER drop beat 10.

Run:  python3 videos/ai-training/14-word-powerpoint/build_word_powerpoint.py
      /usr/bin/python3 preview.py videos/ai-training/14-word-powerpoint/claude-word-powerpoint.excalidraw out.png
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

random.seed(141214)  # deterministic - re-runs produce identical files

# ----------------------------------------------------------------------------
# BEAT SCAFFOLD - eleven beats, wide gaps so one frames cleanly on a 14" laptop
# ----------------------------------------------------------------------------
N = 11
GAP = 800
# every beat uses the SAME slot, shaped ~1.15:1 (content ~1120 wide x ~980 tall,
# the heading at y60 counted in) so framing is identical on a 14" laptop.
WID = {i: 1200 for i in range(1, N + 1)}
# Beat 10 is the ONE exception the house rule allows ("an inherently wide beat
# may run a little wider, within reason"). It carries two failures AND the catch
# that covers both, which is three columns' worth. Widening it keeps its HEIGHT
# at the standard ~980 - and height is what actually binds framing on a 16:10
# laptop, so a 1600 x 980 beat frames MORE comfortably than a 1200-wide one that
# runs 250px tall past its slot. Do not solve this by making it taller.
WID[10] = 1600
ACCENT = {1: ORANGE, 2: VIOLET, 3: BLUE, 4: TEAL, 5: INDIGO,
          6: YELLOW, 7: VIOLET, 8: BLUE, 9: TEAL,
          10: RED, 11: GREEN}
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
# THE WORKED EXAMPLE - one generic packaging-supplier contract, carried across
# nine of the eleven beats so the board tells a single story: the agreement you
# edit, the clause that must survive being tightened, and the deck that argues
# for re-tendering it. Deliberately everyday business, never Phlo-specific, no
# patient or clinical detail, invented numbers and fictional wording throughout.
#
# CHANGE THE EXAMPLE AND BEATS 1, 3, 4, 5, 6, 7, 8, 10 AND 11 ALL MOVE TOGETHER.
# ----------------------------------------------------------------------------
# The document half. CLAUSE_AFTER is genuinely better prose and genuinely wrong:
# it has dropped the condition that made the clause mean anything. That gap is
# the whole of beat 10's left-hand side.
CLAUSE_BEFORE = ("Either party may terminate this agreement,\n"
                 "provided that written notice is given at\n"
                 "least 30 days before the Renewal Date.")
CLAUSE_AFTER = ("Either party may terminate this\n"
                "agreement at any time.")
# Must read as a DEADLINE, not a duration, and must fit column A (ends before
# column B at ox+560): at SMALL this is ~453px wide including the chip padding.
LOST_CONDITION = "30 days before the Renewal Date, in writing"
DEFINED_TERMS = ["Renewal Date", "Notice Period"]

# The deck half. The decision is the catch on beat 10: one sentence, named
# before you build, and falsifiable by reading the headlines alone.
DECISION = "'approve the re-tender of the packaging contract'"

# Beat 7's rewrites: the topic you would have typed, and the claim that works.
TOPIC_TO_CLAIM = [
    ("Q3 results", "margin fell because unit cost rose"),
    ("Supplier review", "two of three suppliers missed SLA twice"),
    ("Next steps", "re-tender now, or absorb it again"),
]

# Beat 10's headline strip - the generic deck, read in order. No argument in it.
GENERIC_HEADLINES = "Q3 results   -   Background   -   Our options   -   Next steps"

# The outline agreed in chat on beat 6, and its short forms on beats 8 and 11.
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
def doc_page(x, y, w, h, accent=BLUE, abg=BLUE_BG, lines=7, tracked=False,
             cite=None, blank=False, weighted=False):
    """A document page: title bar + paragraph lines.

    tracked=True adds a struck deletion, a coloured insertion and a margin
    change-bar. cite=row highlights a line as a citation target. blank=True
    draws the page empty - the thing generation starts from. weighted=True
    inks the top and bottom rows and fades the middle ones to FAINT, which is
    beat 5's attention picture drawn in palette colours rather than opacity."""
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="doc")
    if not blank:
        rect(x + 0.10 * w, y + 0.08 * h, 0.5 * w, 0.045 * h, stroke="transparent",
             bg=accent, sw=1, rough=1, rounded=True, prefix="dttl")
    for k in range(lines):
        ly = y + 0.22 * h + k * (0.62 * h / lines)
        ln_w = (0.78 if k % 3 else 0.58) * w
        col = GREY
        if weighted:
            edge = max(1, int(lines * 0.22))
            col = INK if (k < edge or k >= lines - edge) else FAINT
        line(x + 0.10 * w, ly, [[0, 0], [ln_w, 0]], stroke=col, sw=2)
    if cite is not None:
        ly = y + 0.22 * h + cite * (0.62 * h / lines)
        rect(x + 0.08 * w, ly - 8, 0.84 * w, 18, stroke="transparent", bg=abg,
             sw=1, rough=1, rounded=True, fill="solid", opacity=70, prefix="dcite")
    if tracked:
        ly = y + 0.22 * h + 2 * (0.62 * h / lines)
        line(x + 0.10 * w, ly, [[0, 0], [0.38 * w, 0]], stroke=RED, sw=3)
        line(x + 0.50 * w, ly, [[0, 0], [0.26 * w, 0]], stroke=GREEN, sw=3)
        rect(x + 0.93 * w, y + 0.2 * h, 0.03 * w, 0.3 * h, stroke=accent, bg=abg,
             sw=1, rough=1, rounded=True, prefix="dmar")


def app_window(x, y, w, h, label, accent=VIOLET, abg=VIOLET_BG, kind="doc"):
    """An Office window with a Claude sidebar down its right-hand edge.

    Beat 2's whole point: the panel sits BESIDE the file, so the file is already
    the context. kind='doc' fills it with paragraph rules, kind='slides' with a
    row of slide thumbnails - the same illustration serving both apps, which is
    the merge this board is built on."""
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="app")
    line(x, y + 36, [[0, 0], [w, 0]], stroke=GREY, sw=1)
    for k in range(3):
        ellipse(x + 16 + k * 16, y + 13, 9, 9, stroke=GREY, bg=GREY, sw=1)
    text(x + 74, y + 6, label, size=SMALL, color=GREYD)
    sb_w = 0.30 * w
    body_w = w - sb_w
    if kind == "doc":
        for k in range(7):
            ln = (0.72 if k % 3 else 0.5) * body_w
            line(x + 0.08 * body_w, y + 76 + k * 26, [[0, 0], [ln, 0]], stroke=GREY, sw=2)
    else:
        for k in range(4):
            sx = x + 0.07 * body_w + (k % 2) * 0.47 * body_w
            sy = y + 72 + (k // 2) * 88
            rect(sx, sy, 0.40 * body_w, 74, stroke=INK, bg=WHITE, sw=2, rough=1,
                 rounded=True, prefix="thumb")
            rect(sx + 10, sy + 10, 0.22 * body_w, 9, stroke="transparent", bg=accent,
                 sw=1, rough=1, rounded=True, prefix="thumbt")
    rect(x + body_w, y + 36, sb_w, h - 36, stroke=accent, bg=abg, sw=2, rough=1,
         rounded=True, fill="solid", opacity=45, prefix="sbar")
    rect(x + body_w, y + 36, 8, h - 36, stroke=accent, bg=accent, sw=1, rough=1,
         rounded=False, prefix="sedge")
    text(x + body_w + 24, y + 54, "Claude", size=SMALL, color=accent)
    for k in range(3):
        rect(x + body_w + 24, y + 94 + k * 40, sb_w * 0.62, 24, stroke="transparent",
             bg=WHITE, sw=1, rough=1, rounded=True, fill="solid", prefix="sbmsg")


def review_row(x, y, w, old, new, accepted, accent=BLUE):
    """One row of the reviewing pane: the old wording struck, the new wording
    beside it, and the decision you made about it."""
    rect(x, y, w, 76, stroke=GREYD, bg=WHITE, sw=2, rough=1, rounded=True, prefix="rrow")
    text(x + 22, y + 24, old, size=SMALL, color=GREYD)
    _strike(x + 22, y + 24, old, SMALL, RED, sw=3)
    ax = x + 22 + text_w(old, SMALL) + 26
    arrow(ax, y + 36, [[0, 0], [38, 0]], stroke=accent, sw=3, rough=1)
    text(ax + 56, y + 24, new, size=SMALL, color=accent)
    if accepted:
        tick(x + w - 62, y + 24, GREEN, s=24)
    else:
        xmark(x + w - 58, y + 26, RED, s=22)


def slide(x, y, w, h, accent=ORANGE, abg=ORANGE_BG, bullets=3, chart=True):
    """A single tidy slide: title bar, a few bullet lines, a small bar chart.

    Deliberately carries ZERO text elements - six of these with the argument
    slide missing is beat 6's setup, and that reads better unlabelled than it
    would with six invented slide titles."""
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


def slide_deck(x, y, accent=ORANGE, abg=ORANGE_BG, s=1.0):
    """A stack of slides - two offset behind, one crisp slide in front.
    Extent is x..x+268*s, y..y+186*s."""
    for k in range(2):
        off = (2 - k) * 18 * s
        rect(x + off, y + off, 232 * s, 150 * s, stroke=INK, bg=abg, sw=2, rough=1,
             rounded=True, prefix="deck")
    slide(x + 36 * s, y + 36 * s, 232 * s, 150 * s, accent=accent, abg=abg,
          bullets=3, chart=True)


def _strike(x, y, s, size, color, sw=4):
    """A hand line through text. The kit has no strikethrough, so this is a
    one-off - and it sits at 0.44 of the line box, not 0.5: with lineHeight 1.4
    the glyphs sit high in their box, so a line at the geometric middle crosses
    the descenders and reads as an underline that slipped. (Day 10 and Day 12
    both record this finding; rediscovering it cost a preview round there.)"""
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
    through, which is how beat 7 shows a topic heading failing."""
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


def human_gate(cx, cy, color=GREEN, abg=GREEN_BG, s=1.0):
    """The human marker on beat 9: a head plus rounded shoulders, filled.

    GREEN, not the beat's accent - green = the human pass is held constant
    across Day 10, Day 11 and Day 13, and this marker is safety-bearing. It does
    not use the kit's person(), which is sized for a crowd of tiny figures and
    reads as a paper dart when it has to stand alone at hero size."""
    r = 26 * s
    ellipse(cx - r, cy - 62 * s, 2 * r, 2 * r, stroke=color, bg=WHITE, sw=3, rough=1,
            prefix="hghead")
    line(cx - 50 * s, cy + 46 * s,
         [[0, 0], [0, -22 * s], [18 * s, -50 * s], [82 * s, -50 * s],
          [100 * s, -22 * s], [100 * s, 0]],
         stroke=color, sw=3, rough=1, bg=abg, fill="solid", prefix="hgbody")


def chat_panel(x, y, w, h, stroke=INK):
    """A plain chat window: title strip and three dots. Everything else is placed
    by the caller, so beat 6 can put the outline inside it."""
    rect(x, y, w, h, stroke=stroke, bg=WHITE, sw=2, rough=1, rounded=True, prefix="chat")
    line(x, y + 40, [[0, 0], [w, 0]], stroke=GREY, sw=1)
    for k in range(3):
        ellipse(x + 18 + k * 18, y + 15, 10, 10, stroke=GREY, bg=GREY, sw=1)


def outline_rows(x, y, items, accent, step=58, d=34, size=SMALL, gap=48):
    """A numbered outline - one claim to a line. The shape the argument lives in
    before any of it is designed. This is the ONLY numbered process on the
    board."""
    for k, item in enumerate(items):
        ry = y + k * step
        num_badge(x, ry, k + 1, accent, d=d)
        text(x + gap, ry + 3, item, size=size, color=INK)


# ============================================================================
# BOARD TITLE
# ============================================================================
text(OX[1], -400, "Claude in Word\nand PowerPoint", size=HERO, color=INK)
text(OX[1] + 6, -400 + 2 * HERO * LINE_H + 10,
     "it is best at the surface - the substance is the part you ask for",
     size=H2, color=ORANGE)

# ============================================================================
# BEAT 1 - THE DOCUMENT ALREADY EXISTS   (shared framing, taught once)
# ============================================================================
ox = beat_head(1, "the document already exists",
               "Generation starts from a blank page. This does not. There is history in\n"
               "it, other people's wording, and a shape it has to keep.")
text(ox + 50, 292, "what a blank page gets you", size=SMALL, color=GREY)
doc_page(ox + 50, 330, 300, 300, accent=GREY, abg=FAINT, lines=0, blank=True)
sticky(ox + 50, 654, 300, 84, FAINT, angle=jit(1.4))
text(ox + 78, 676, "\"write me a draft\"", size=BODY, color=GREYD)
xmark(ox + 52, 762, GREY, s=20)
text(ox + 96, 756, "nothing to preserve,\nso nothing to lose", size=SMALL, color=GREYD)

text(ox + 470, 292, "what is actually open on your screen", size=SMALL, color=GREY)
doc_page(ox + 470, 330, 300, 300, accent=ORANGE, abg=ORANGE_BG, lines=9, tracked=True)
for k, (lab, ly) in enumerate([("someone else's wording", 352),
                               ("a tracked change from\nlast week", 448),
                               ("a defined term you\ncannot quietly drop", 568)]):
    arrow(ox + 786, ly + 14, [[0, 0], [-32, 0]], stroke=ORANGE, sw=3, rough=1)
    text(ox + 828, ly, lab, size=SMALL, color=ORANGE)
xmark(ox + 472, 662, RED, s=20)
text(ox + 516, 656, "a draft would throw all of that away", size=SMALL, color=GREYD)
chip(ox + 50, 828, "you are not asking for a draft, you are asking for a change",
     fill=ORANGE_BG, text_color=ORANGE, border=ORANGE, size=LABEL)

# the thesis for BOTH halves, and the plant for the deck half - PowerPoint's
# "it looks finished and says nothing" lives here and again on beat 6.
sticky(ox + 40, 906, 760, 130, ORANGE_T, angle=jit(0.8))
text(ox + 76, 928, "Word and PowerPoint, one trap: Claude is best at the\n"
                   "surface - and the surface is what a reviewer checks.",
     size=BODY, color=INK)
slide_deck(ox + 840, 900, accent=GREY, abg=FAINT, s=0.72)
text(ox + 828, 1046, "a deck can look finished\nand say nothing", size=SMALL, color=GREY)

# ============================================================================
# BEAT 2 - IT LIVES IN THE SIDEBAR   (orientation, both apps, kept short)
# ============================================================================
ox = beat_head(2, "it lives in the sidebar",
               "A panel beside the file you already have open - not a separate\n"
               "window you paste things into.")
text(ox + 50, 292, "the copy-paste shuttle", size=SMALL, color=GREY)
doc_page(ox + 50, 330, 190, 190, accent=GREY, abg=FAINT, lines=6)
arrow(ox + 258, 400, [[0, 0], [96, 0]], stroke=GREY, sw=3, rough=1)
arrow(ox + 354, 456, [[0, 0], [-96, 0]], stroke=GREY, sw=3, rough=1)
chat_panel(ox + 372, 330, 190, 190)
for k in range(3):
    rect(ox + 392, 388 + k * 36, 150 - k * 30, 22, stroke="transparent", bg=FAINT,
         sw=1, rough=1, rounded=True, fill="solid", prefix="cmsg")
xmark(ox + 52, 548, RED, s=20)
text(ox + 96, 542, "you rebuild the context every single time", size=SMALL, color=GREYD)

text(ox + 50, 622, "the sidebar", size=H3, color=VIOLET)
app_window(ox + 50, 678, 510, 300, "a document", accent=VIOLET, abg=VIOLET_BG, kind="doc")
app_window(ox + 610, 678, 510, 300, "a deck", accent=VIOLET, abg=VIOLET_BG, kind="slides")
chip(ox + 50, 1000, "the file is the context - so you stop pasting it",
     fill=VIOLET_BG, text_color=VIOLET, border=VIOLET, size=LABEL)

# ============================================================================
# BEAT 3 - REVIEW AS A DIFF
# ============================================================================
ox = beat_head(3, "review as a diff",
               "Changes arrive as tracked edits. You read them one at a time and\n"
               "decide each one on its own.")
text(ox + 50, 292, "the agreement, marked up", size=SMALL, color=GREY)
doc_page(ox + 50, 330, 300, 340, accent=BLUE, abg=BLUE_BG, lines=10, tracked=True)
text(ox + 50, 692, "changes land in the document you already had", size=SMALL, color=GREYD)

text(ox + 420, 292, "the reviewing pane", size=SMALL, color=BLUE)
review_row(ox + 420, 330, 700, "shall be entitled to", "may", True, accent=BLUE)
review_row(ox + 420, 426, 700, "in the event that", "if", True, accent=BLUE)
review_row(ox + 420, 522, 700, "within 5 working days", "promptly", False, accent=BLUE)
tick(ox + 422, 630, GREEN, s=22)
text(ox + 466, 624, "two accepted - shorter, and they mean the same thing",
     size=SMALL, color=GREYD)
xmark(ox + 422, 676, RED, s=20)
text(ox + 466, 670, "one rejected - \"promptly\" is not a date",
     size=SMALL, color=GREYD)
chip(ox + 50, 782, "never accept a full rewrite", fill=BLUE_BG, text_color=BLUE,
     border=BLUE, size=LABEL)
text(ox + 50, 872, "One at a time is not slower. It is the only version of this\n"
                   "job where you can say what changed and why.",
     size=BODY, color=GREYD)

# ============================================================================
# BEAT 4 - REVISE, DO NOT REWRITE   (the pair is stacked, not spread)
# ============================================================================
ox = beat_head(4, "revise, do not rewrite",
               "The same document, two asks. One gives you a new problem,\n"
               "the other gives you a change you can check.")
sticky(ox + 40, 306, 1080, 290, FAINT, angle=jit(-0.7))
text(ox + 76, 330, "\"make this better\"", size=H3, color=GREYD)
arrow(ox + 440, 380, [[0, 0], [86, 0]], stroke=GREY, sw=4, rough=1)
doc_page(ox + 566, 326, 180, 200, accent=GREY, abg=FAINT, lines=8)
text(ox + 776, 340, "a new document", size=BODY, color=GREYD)
xmark(ox + 778, 396, RED, s=20)
text(ox + 822, 390, "nothing to compare it to - you\nhave to re-read all of it, and\n"
                    "hope you notice what went missing",
     size=SMALL, color=GREYD)
text(ox + 76, 400, "it rewrites the lot, in its\nown voice, and the thing\n"
                   "you had is gone",
     size=SMALL, color=GREYD)

sticky(ox + 40, 626, 1080, 300, TEAL_T, angle=jit(0.7))
text(ox + 76, 650, "\"tighten the second paragraph,\nkeep the defined terms\"",
     size=H3, color=TEAL)
arrow(ox + 440, 740, [[0, 0], [86, 0]], stroke=TEAL, sw=4, rough=1)
doc_page(ox + 566, 668, 180, 200, accent=TEAL, abg=TEAL_BG, lines=8, tracked=True)
text(ox + 776, 672, "a change you can check", size=BODY, color=TEAL)
tick(ox + 778, 726, GREEN, s=22)
text(ox + 822, 720, "one paragraph moved, the rest\nuntouched, and every word of it\n"
                    "is in front of you as a diff",
     size=SMALL, color=GREYD)
tx = ox + 76
for term in DEFINED_TERMS:
    w, _ = chip(tx, 800, term, fill=WHITE, text_color=TEAL, border=TEAL, size=SMALL)
    tx += w + 24
text(ox + 76, 876, "name what must survive, and it survives", size=SMALL, color=TEAL)
chip(ox + 40, 956, "scope the ask and you scope the risk", fill=TEAL_BG,
     text_color=TEAL, border=TEAL, size=LABEL)

# ============================================================================
# BEAT 5 - IT CAN READ THE WHOLE THING
# ============================================================================
ox = beat_head(5, "it can read the whole thing",
               "A forty-page contract goes in whole. Its attention is not even\n"
               "across it - strong at the ends, thinner through the middle.")
text(ox + 50, 292, "forty pages, all of it in front of Claude", size=SMALL, color=GREY)
doc_page(ox + 50, 330, 300, 520, accent=INDIGO, abg=INDIGO_BG, lines=18, weighted=True)
arrow(ox + 392, 372, [[0, 0], [-32, 0]], stroke=INDIGO, sw=3, rough=1)
text(ox + 432, 356, "strong here", size=SMALL, color=INDIGO)
arrow(ox + 392, 592, [[0, 0], [-32, 0]], stroke=GREY, sw=3, rough=1)
text(ox + 432, 562, "thinner through\nthe middle", size=SMALL, color=GREYD)
arrow(ox + 392, 800, [[0, 0], [-32, 0]], stroke=INDIGO, sw=3, rough=1)
text(ox + 432, 784, "strong here", size=SMALL, color=INDIGO)

text(ox + 640, 292, "so change what you ask for", size=SMALL, color=INDIGO)
sticky(ox + 640, 330, 480, 190, FAINT, angle=jit(-1.2))
text(ox + 672, 354, "\"summarise this contract\"", size=BODY, color=GREYD)
xmark(ox + 674, 422, RED, s=20)
text(ox + 718, 416, "a summary is exactly where\nthe middle goes missing",
     size=SMALL, color=GREYD)
sticky(ox + 640, 552, 480, 230, INDIGO_T, angle=jit(1.2))
text(ox + 672, 576, "\"quote the exact wording on\nnotice periods, and tell me\n"
                    "which page it is on\"",
     size=BODY, color=INK)
tick(ox + 674, 690, GREEN, s=22)
text(ox + 718, 684, "now you can check it against\nthe page yourself",
     size=SMALL, color=GREYD)
chip(ox + 640, 822, "ask for the quote, not the summary", fill=INDIGO_BG,
     text_color=INDIGO, border=INDIGO, size=LABEL)
text(ox + 50, 902, "This is the line on this board most likely to go out of date - model\n"
                   "behaviour on long documents moves. The habit it teaches does not.",
     size=SMALL, color=GREYD)

# ============================================================================
# BEAT 6 - STRUCTURE FIRST, SLIDES SECOND   (the pivot into the deck half)
# ============================================================================
ox = beat_head(6, "structure first, slides second",
               "A deck has the same trap, one storey up. Agree the argument in the\n"
               "chat before anything gets designed.")
text(ox + 50, 292, "six tidy slides - and the one that says why any of it matters",
     size=SMALL, color=GREY)
for k in range(6):
    sx = ox + 50 + (k % 3) * 200
    sy = 330 + (k // 3) * 132
    slide(sx, sy, 186, 120, accent=YELLOW, abg=YELLOW_BG, bullets=2, chart=True)
dashed_box(ox + 50, 598, 586, 90, GREY, sw=3)
text_centered(ox + 343, 626, "- missing -", size=H3, color=GREY)
text(ox + 50, 708, "nothing on there is wrong, which is why it will sail through",
     size=SMALL, color=GREYD)

text(ox + 690, 292, "so settle it here, first", size=SMALL, color=YELLOW)
chat_panel(ox + 690, 330, 430, 480)
sticky(ox + 718, 388, 320, 72, YELLOW_T, angle=jit(1.2))
text(ox + 742, 406, "propose an outline first", size=SMALL, color=INK)
text(ox + 718, 480, "Claude:", size=SMALL, color=GREY)
outline_rows(ox + 718, 512, OUTLINE_SHORT, YELLOW, step=56, d=32, size=SMALL, gap=44)
tick(ox + 692, 832, GREEN, s=22)
text(ox + 736, 826, "four minutes of chat, and the argument is settled",
     size=SMALL, color=GREYD)
demo_badge(ox + 50, 860,
           "show in Claude desktop app: agree the outline in chat first")
chip(ox + 50, 950, "if the outline is wrong, the design is wasted", fill=YELLOW_BG,
     text_color=YELLOW, border=YELLOW, size=LABEL)

# ============================================================================
# BEAT 7 - ONE IDEA PER SLIDE, ONE LINE THAT CARRIES IT
# ============================================================================
ox = beat_head(7, "one idea per slide, one line that carries it",
               "The headline is the argument, not the topic. If it could be a\n"
               "chapter title, it is not doing any work.")
text(ox + 50, 292, "a topic", size=SMALL, color=GREY)
headline_slide(ox + 50, 326, 480, 270, "Q3 results", accent=GREY, abg=FAINT,
               tsize=H3, lines=3, strike=VIOLET, chart=True)
xmark(ox + 52, 618, RED, s=22)
text(ox + 96, 612, "a chapter heading - it commits to nothing", size=SMALL, color=GREYD)
text(ox + 610, 292, "a position", size=SMALL, color=GREY)
headline_slide(ox + 610, 326, 480, 270, "margin fell because\nunit cost rose",
               accent=VIOLET, abg=VIOLET_BG, tsize=H3, lines=3, chart=True)
tick(ox + 612, 616, GREEN, s=22)
text(ox + 658, 612, "a claim - you can agree or disagree with it", size=SMALL, color=GREYD)
text(ox + 50, 676, "every headline on the deck, rewritten the same way", size=SMALL, color=GREY)
for k, (topic, claim) in enumerate(TOPIC_TO_CLAIM):
    ry = 716 + k * 66
    struck(ox + 50, ry, topic, size=H3, color=GREYD, strike=VIOLET)
    arrow(ox + 330, ry + 18, [[0, 0], [50, 0]], stroke=VIOLET, sw=3, rough=1)
    text(ox + 400, ry, claim, size=H3, color=VIOLET)
chip(ox + 50, 924, "the headline is the argument, not the topic", fill=VIOLET_BG,
     text_color=VIOLET, border=VIOLET, size=LABEL)

# ============================================================================
# BEAT 8 - BUILD IT FROM A SOURCE
# ============================================================================
ox = beat_head(8, "build it from a source",
               "Point it at the report and the numbers you already have.\n"
               "A deck built from a prompt is built from nothing.")
text(ox + 50, 292, "what you already have", size=SMALL, color=GREY)
obj_doc(ox + 50, 336, BLUE, BLUE_BG)
text(ox + 50, 502, "the supplier report", size=SMALL, color=GREYD)
obj_chart(ox + 50, 556, BLUE, BLUE_BG)
text(ox + 50, 706, "last quarter's costs", size=SMALL, color=GREYD)
arrow(ox + 196, 420, [[0, 0], [120, 60]], stroke=BLUE, sw=3, rough=1)
arrow(ox + 196, 640, [[0, 0], [120, -60]], stroke=BLUE, sw=3, rough=1)
text(ox + 340, 292, "the outline it proposes", size=SMALL, color=GREY)
rect(ox + 340, 336, 380, 400, stroke=BLUE, bg=BLUE_T, sw=2, rough=1, rounded=True)
outline_rows(ox + 370, 380, OUTLINE_SHORT, BLUE, step=68, d=32, size=SMALL, gap=46)
text(ox + 340, 752, "grounded in those two files, line by line", size=SMALL, color=GREYD)
text(ox + 770, 292, "what a prompt on its own gives you", size=SMALL, color=GREY)
sticky(ox + 770, 336, 340, 100, FAINT, angle=jit(1.4))
text(ox + 796, 358, "\"make me a deck about\nsupplier costs\"", size=SMALL, color=GREYD)
arrow(ox + 940, 448, [[0, 0], [0, 44]], stroke=GREY, sw=3, rough=1)
slide_deck(ox + 800, 508, accent=GREY, abg=FAINT)
xmark(ox + 772, 722, RED, s=22)
text(ox + 816, 716, "plausible, generic, and not\nabout your numbers",
     size=SMALL, color=GREYD)
chip(ox + 50, 866, "feed it the source, not a description of the source",
     fill=BLUE_BG, text_color=BLUE, border=BLUE, size=LABEL)

# ============================================================================
# BEAT 9 - DESIGN IS NOT ITS STRENGTH   (the honest beat)
# ============================================================================
ox = beat_head(9, "design is not its strength",
               "It is good at the order of an argument. It will not decide what\n"
               "your brand looks like.")
text(ox + 50, 292, "genuinely good at this", size=H3, color=TEAL)
sticky(ox + 50, 344, 510, 300, TEAL_T, angle=jit(1.2))
for k, item in enumerate(["the order things go in", "one idea to a slide",
                          "the line that carries each one", "a first draft in minutes"]):
    check_item(ox + 86, 384 + k * 64, item, color=INK, accent=TEAL, size=BODY)
text(ox + 610, 292, "still yours to decide", size=H3, color=GREYD)
sticky(ox + 610, 344, 500, 300, FAINT, angle=jit(-1.2))
# Worded as DECISIONS, never as objects. Claude demonstrably DOES read the slide
# master, layouts, fonts and colour scheme and generate against them - "the
# template" on its own would read as "Claude ignores your template", which is
# false and would contradict the Resource Card. See the docstring.
for k, item in enumerate(["which template to use", "what the brand actually is",
                          "what good looks like here", "the final look"]):
    yy = 384 + k * 64
    xmark(ox + 646, yy + 2, GREY, s=20)
    text(ox + 692, yy, item, size=BODY, color=GREYD)
slide_deck(ox + 60, 700, accent=TEAL, abg=TEAL_BG)
arrow(ox + 348, 790, [[0, 0], [76, 0]], stroke=TEAL, sw=5, rough=1)
human_gate(ox + 510, 822, GREEN, GREEN_BG)
arrow(ox + 592, 790, [[0, 0], [76, 0]], stroke=TEAL, sw=5, rough=1)
slide_deck(ox + 700, 700, accent=TEAL, abg=TEAL_BG)
text(ox + 60, 902, "Claude's structure", size=SMALL, color=GREYD)
text_centered(ox + 510, 902, "you: the brand pass", size=SMALL, color=GREEN)
text(ox + 790, 902, "ready to send", size=SMALL, color=GREYD)
chip(ox + 50, 956, "structure, not design", fill=TEAL_BG, text_color=TEAL,
     border=TEAL, size=LABEL)

# ============================================================================
# BEAT 10 - PLAUSIBLE PASSES REVIEW   (adversarial: BOTH failures, ONE catch)
# ============================================================================
# The fused adversarial beat, and the reason this is one video rather than two.
# Left: the document failure. Middle: the deck failure. Right: the single catch
# that covers both, in the shape Day 10's beat 6 established - name the test
# BEFORE you look, so "it reads well" and "it looks fine" cannot be the verdict.
# A failure with no catch is a diagnosis with no test; this beat is the Best
# Catch feeder. Three columns is why this slot is 1600 rather than 1200.
ox = beat_head(10, "plausible passes review",
               "Both of these would sail through a review. One has quietly lost a\n"
               "condition. The other never made a case.")

# --- column A: the document fails by losing something ------------------------
text(ox + 50, 292, "the paragraph you asked it to tighten", size=SMALL, color=RED)
rect(ox + 50, 330, 470, 150, stroke=GREYD, bg=WHITE, sw=2, rough=1, rounded=True)
text(ox + 76, 352, CLAUSE_BEFORE, size=SMALL, color=GREYD)
arrow(ox + 285, 494, [[0, 0], [0, 40]], stroke=RED, sw=4, rough=1)
rect(ox + 50, 546, 470, 100, stroke=RED, bg=RED_T, sw=2, rough=1, rounded=True)
text(ox + 76, 570, CLAUSE_AFTER, size=SMALL, color=INK)
tick(ox + 52, 674, GREEN, s=22)
text(ox + 96, 668, "shorter, cleaner, better English", size=SMALL, color=GREYD)
xmark(ox + 52, 714, RED, s=20)
text(ox + 96, 708, "and the condition is gone:", size=SMALL, color=RED)
chip(ox + 50, 748, LOST_CONDITION, fill=RED_BG, text_color=RED, border=RED, size=SMALL)
chip(ox + 50, 824, "fluent is not faithful", fill=RED_BG, text_color=RED,
     border=RED, size=LABEL)

# --- column B: the deck fails by never saying anything -----------------------
text(ox + 560, 292, "three decks, all well-made", size=SMALL, color=RED)
# ONE neutral grey and NO jitter: the sameness IS the point, and a tilt or a
# colour each would read as three real options rather than three interchangeable
# ones. Day 10's beat 6 and Day 12's beat 6 both record this same exception.
for k in range(3):
    slide_deck(ox + 560 + k * 157, 330, accent=GREY, abg=FAINT, s=0.55)
text(ox + 560, 452, "all well-made, all different, all interchangeable",
     size=SMALL, color=GREYD)
text(ox + 560, 496, "read only the headlines, in order", size=SMALL, color=RED)
rect(ox + 560, 530, 470, 96, stroke=GREYD, bg=WHITE, sw=2, rough=1, rounded=True)
text(ox + 586, 552, "Q3 results  -  Background\nOur options  -  Next steps",
     size=SMALL, color=GREYD)
xmark(ox + 562, 652, RED, s=20)
text(ox + 606, 646, "four topics. That is a table of\ncontents, not an argument",
     size=SMALL, color=GREYD)
text(ox + 560, 716, "and not one of them argues for:", size=SMALL, color=RED)
chip(ox + 560, 748, DECISION, fill=RED_BG, text_color=RED, border=RED, size=SMALL)
chip(ox + 560, 824, "nothing here to disagree with", fill=RED_BG, text_color=RED,
     border=RED, size=LABEL)

# --- column C: one catch, two shapes -----------------------------------------
text(ox + 1110, 292, "the catch - and it goes BEFORE you look", size=SMALL, color=RED)
text(ox + 1110, 330, "name the test first,\nso \"it reads well\"\ncannot be the verdict",
     size=H3, color=RED)
sticky(ox + 1100, 500, 460, 186, RED_T, angle=jit(0.8))
text(ox + 1130, 522, "on a document", size=SMALL, color=RED)
text(ox + 1130, 554, "list what has to survive -\nthe conditions, the dates,\n"
                     "the defined terms - then\nread the diff against it",
     size=SMALL, color=INK)
sticky(ox + 1100, 712, 460, 186, RED_T, angle=jit(-0.8))
text(ox + 1130, 734, "on a deck", size=SMALL, color=RED)
text(ox + 1130, 766, "name the decision you want\nin one sentence - then read\n"
                     "only the headlines, in order,\nand ask if they argue for it",
     size=SMALL, color=INK)

# ============================================================================
# BEAT 11 - DO IT LIVE, ON REAL WORK   (the cut-away, then the close)
# ============================================================================
ox = beat_head(11, "do it live, on real work",
               "One document, reviewed change by change. One deck, built from an\n"
               "outline you agreed first.")
text(ox + 50, 292, "the document", size=SMALL, color=GREEN)
doc_page(ox + 50, 330, 260, 300, accent=GREEN, abg=GREEN_BG, lines=9, tracked=True)
for k, (lab, acc) in enumerate([("accepted", GREEN), ("accepted", GREEN),
                                ("rejected", RED)]):
    yy = 656 + k * 48
    if acc is GREEN:
        tick(ox + 52, yy, GREEN, s=20)
    else:
        xmark(ox + 54, yy + 2, RED, s=18)
    text(ox + 96, yy - 4, lab, size=SMALL, color=acc)
text(ox + 50, 812, "every one read as a diff first", size=SMALL, color=GREYD)

text(ox + 400, 292, "the deck", size=SMALL, color=GREEN)
for k, hl in enumerate(["margin fell\nbecause unit\ncost rose",
                        "two suppliers\nmissed SLA\ntwice",
                        "absorbing it\ncosts more\nby Q2",
                        "re-tender now -\nhere is the\nask"]):
    headline_slide(ox + 400 + (k % 2) * 250, 330 + (k // 2) * 170, 226, 152, hl,
                   accent=GREEN, abg=GREEN_BG, tsize=SMALL, lines=2)
text(ox + 400, 680, "every headline states a position", size=SMALL, color=GREEN)
demo_badge(ox + 400, 730,
           "show in Claude desktop app: three tracked changes, one rejected")

# the data rule - red, because it is the only on-screen data-handling rule here
highlighter(ox + 40, 856, 1080, 104, RED_BG, angle=0.0)
diamond(ox + 56, 876, 44, 44, stroke=RED, bg=RED_BG, sw=3)
text_centered(ox + 78, 880, "!", size=H3, color=RED)
text(ox + 124, 872,
     "Nothing confidential goes into a document or a deck you will send out - and\n"
     "do not open a file, or build on a template, that you do not trust.",
     size=SMALL, color=RED)
chip(ox + 50, 992, "accept nothing you have not read as a diff", fill=GREEN_BG,
     text_color=GREEN, border=GREEN, size=LABEL)
chip(ox + 640, 992, "the argument is the deliverable", fill=GREEN_BG,
     text_color=GREEN, border=GREEN, size=LABEL)

# No connector spine, no inter-beat arrows and no footer: the eleven beats read
# as one picture through consistent shape and rhythm, and the whitespace is the
# camera.

# ----------------------------------------------------------------------------
# WRITE + VALIDATE  (shared excalidraw_kit; hard-fails on frames / off-palette)
# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "claude-word-powerpoint.excalidraw")
# The NARROW slot plus 200, not the wide one: beat 10 is wider only because it
# holds three columns, and no single line of text should ever be wider than a
# standard slot. Using max() here would quietly slacken the check for all eleven.
MAXW = 1400
finish(out, MAXW, TOTAL_W)
