# Brief - Day 13: design.md

**Folder:** `videos/ai-training/13-design-md/`
**File:** `build_design_md.py` -> `claude-design-md.excalidraw`
**Slug:** `claude-design-md` (so: `claude-design-md-script.md`,
`claude-design-md-prompt.md`, `claude-design-md-resource-card.md`)
**Style:** Style B, per `.claude/skills/SKILL.md` and the repo `CLAUDE.md`
**Length:** 8 beats. The recorded script measures **~7 min 10** (1,027 spoken words at
150 wpm, plus ~20s where the cut-away takes longer to do than to say). Hard cap 8, target
4 to 6 - see Runtime below.
**Curriculum ref:** **Day 13**. **No Day 13 entry exists in
`Phlo_Mandatory_AI_Course_Curriculum.docx`** - the day series is newer than the docx.
**Reconcile board and narration against the curriculum when a Day 13 entry exists.**

## Where it sits, and why it is separate from Day 10

**Day 10 teaches the judgement. Day 13 teaches the plumbing that makes that judgement
permanent.** Day 10's beat 2 says "reference beats adjectives" and a `design.md` is the
industrial-strength version of exactly that - so Day 10 *mentions* design.md on beat 2
with a one-line chip and hands off here.

That split was a deliberate instruction, not a convenience: design.md is a big enough
topic to need its own day, and Day 10 would have lost its argument if it had to carry the
three-file workflow too.

Per the repo precedence rule, **Day 13 covers its topic in full** and never points back
at Day 10 for substance. The Day 10 dependencies it *does* lean on are stated as
callbacks, not prerequisites: "no settings panel, exactly as on Day 10" (beat 4) and
"looking finished and being right are different things" (beat 8).

**Ships:** a design.md, and a design system built from it.
**Pause-and-try:** write the first ten lines of your own design.md - the colours you
already use, by hex, and the two type sizes you always reach for.

## Source, and the one departure from it

Distilled from a **third-party tutorial transcript** supplied with the brief. There is no
other source; nothing here came from Anthropic documentation, so **everything
product-specific dates fast and is on the Resource Card rather than the board.**

### What was taken

| From the source | Where it landed |
|---|---|
| "most tutorials say pick a template and start prompting" → generic output, wasted runs | beat 1 |
| three inputs: design.md → design system → template | beat 2, then beats 3, 4, 5 |
| what a design.md is: colours, fonts, spacing, how buttons and cards are styled; plain text, works in any AI tool | beat 3 |
| design system = the same rules, native to Claude Design; generated mockups to review; plain-English feedback; upload logo, icons and a voice-principles file once | beat 4 |
| design system = how it looks, template = how it is laid out; title slide, section dividers, two-column | beat 5 |
| two kinds of feedback; project-wide feedback captured into a `CLAUDE.md` read before every design; edit / annotate / tweaks; a tweak is a switch for a decision that repeats across the deck | beat 6 |
| export to PowerPoint, PDF, standalone HTML; the HTML opens in any browser | beat 8 |
| the workflow applies beyond slides - carousels, newsletter visuals | beat 2 chip row |
| model picker, effort setting, the 10-20 minute build, the "create design system" button, project-tree navigation, presenter view, the clarifying questions and "decide for me" | **Resource Card only** - version-specific |

### What was deliberately left out

- **The brand-laundering step, and this is not negotiable.** The source downloads a real
  brand's `design.md` from a public repository, has another model "remove the proprietary
  content and replace them using your own judgment", renames the file, and feeds that in -
  explicitly because Claude will not reproduce a real brand's guidelines. **That is
  routing around a refusal.** It cannot go into mandatory training for a regulated
  pharmacy, and it is off the board, out of the script and out of the demo steps. What
  survives is the mechanism (start from a *reference* design.md, not a blank page) plus
  the red rule on beat 3, stated positively: **the refusal is correct behaviour, take
  your rules from your own brand assets, and if you cannot say where a colour came from
  it is not yours.** Do not put the laundering step back.
- **The source's plug for its author's own product.** Dropped.
- **Named third-party brands** as worked examples. The board's worked example is a
  generic internal workshop deck.

## The eight beats

| # | Accent | Heading | What is drawn |
|---|---|---|---|
| 1 | orange | start in the wrong place | Prompt → a grey generic deck, then three struck attempts. You paid for all three. |
| 2 | violet | three files, before you prompt | The map of the whole day: three numbered cards feeding each other, then every deck after. Chip row for non-slide uses. |
| 3 | blue | design.md is the rulebook | The file itself with real token rows, a checklist of what goes in it, and **the red sourcing rule**. |
| 4 | green | the design system makes it native | design.md → a system panel with swatches, type and a component; the mockups it generates; plain-English feedback. |
| 5 | teal | the template is the layout | Looks versus arranged, side by side: a system panel against four named slide layouts. |
| 6 | indigo | two kinds of feedback | Carries-forward (→ `CLAUDE.md`) against this-deck-only (edit / annotate / tweak toggles), plus **the three-way name collision**. Demo badge. |
| 7 | red | everything compounds, mistakes too | **Adversarial.** One wrong rule fanning out to three fine-looking decks, then the catch: a reference design re-rendered before and after. |
| 8 | yellow | then it leaves the room | Export routes, then the human pass in Day 10's green. |

**Pan order:** left to right, beats 1 to 8, one slot at a time. In the build docstring.

**Accent cycle:** orange / violet / blue / green / teal / indigo / red / yellow - eight
beats, eight accents, no repeats at all.

**Demo badge:** beat 6 only - `show in Claude Design: give feedback once, then open the
project's CLAUDE.md`. **The badge says Claude Design, not "Claude desktop app"**, because
the payload (a CLAUDE.md inside a design project) only exists there; the board this
replaced used the same form.

### Three decisions that are load-bearing

**1. The adversarial beat is 7, and it is deliberately NOT the brand question.** Brand
laundering fails *loudly* - Claude refuses. The silent failure of this capability is that
a wrong rule saved into the design system, or bad feedback captured into the project's
`CLAUDE.md`, propagates to every future design with nothing on screen to say so. The
catch is a regression check: **keep one reference design and re-render it after every
change to the system** - which is Day 7's "test on a known input" pointed at a design
system. Failure without a catch is a diagnosis with no test, and this beat is the Best
Catch feeder.

**2. The three-way `CLAUDE.md` collision is on beat 6 and must stay there.** The repo
already warns that Day 3 (the Claude app remembering you) and Day 4 (Claude Code's
`CLAUDE.md` instruction-writing discipline) must not merge. Day 13 adds a third: a
`CLAUDE.md` that Claude Design writes inside a design project. All three are named on the
board with their Day numbers, in one row each. **Do not remove that row to save space** -
it is the only place a viewer sees the three side by side.

**3. Four colours are held constant and are not free for reuse.**

| Colour | Means | Introduced |
|---|---|---|
| blue | the design.md file | beat 3 |
| green | the design system | beat 4 |
| teal | the template | beat 5 |
| green | **also** the human pass | beat 8, held from Day 10's closing beat |

Green doing double duty is intentional: the design system and the human pass are the two
things the board says you own. The Day 10 carry-over matters more - the two boards share
that one colour so the rule reads as the same rule.

## Runtime

Budgeted in seconds, then **measured against the written narration.**

| section | words | on the clock |
|---|---|---|
| hook | 34 | 14s |
| why this matters | 47 | 19s |
| beat 1 · start in the wrong place | 68 | 27s |
| beat 2 · three files, before you prompt | 91 | 36s |
| beat 3 · design.md is the rulebook | 120 | 48s |
| beat 4 · the design system makes it native | 83 | 33s |
| beat 5 · the template is the layout | 61 | 24s |
| **beat 6 · two kinds of feedback** (incl. ~20s cut-away doing time) | **202** | **101s** |
| **beat 7 · everything compounds, mistakes too** | **141** | **56s** |
| beat 8 · then it leaves the room | 66 | 26s |
| pause-and-try | 50 | 20s |
| close | 64 | 26s |
| **total** | **1,027** | **~7 min 10** |

**A first draft ran 1,262 words - 8 min 45, past the 8-minute hard cap.** Trims came out
of every section except beat 7 and beat 3's red rule. Re-measure if you rewrite:

```bash
awk '/^## On-screen|^## Recording/{stop=1} stop{next}
     /^## [0-9]/{if(s)printf "%-44s %4d w ~%3ds\n",substr(s,4,40),w,int(w/2.5); s=$0; w=0; next}
     /^(>|`\[|\[|---|- |[0-9]\. )/{next} s{w+=NF; t+=NF}
     END{printf "%-44s %4d w ~%3ds\n",substr(s,4,40),w,int(w/2.5); \
         printf "\nTOTAL %d words = %d:%02d\n",t,int(t/2.5)/60,int(t/2.5)%60}' \
  videos/ai-training/13-design-md/claude-design-md-script.md
```

This is over the 4-to-6 target and 50 seconds inside the cap. **If it needs to come
down: beats 5 and 8 are the droppable pair** (the looks-versus-layout distinction can be
said in a line over beat 2, and the export list is on the card), taking it to ~6 min 20.
**Beat 7 is the one to protect**, then beat 3's red rule.

## The worked example

One generic internal workshop deck runs through beats 1, 6, 7 and 8. The same element -
the eyebrow label - is the good correction on beat 6 (`GOOD_FEEDBACK`) and the wrong rule
on beat 7 (`BAD_RULE`), so the two beats tell one story: the correction that compounds,
and the correction that compounds wrongly. `REFERENCE` names the regression check.
All three are pinned at the top of the build script - **change one and all three beats
have to move together.** Never Phlo-specific, no patient or clinical detail, no real
brand's assets.

## How it is built

```bash
python3 videos/ai-training/13-design-md/build_design_md.py     # rebuild this board
/usr/bin/python3 preview.py videos/ai-training/13-design-md/claude-design-md.excalidraw out.png
/usr/bin/python3 preview.py <scene> out.png XMIN XMAX          # close-up on one beat
python3 build_all.py                                           # rebuild all + Style-B guard
```

`preview.py` needs `/usr/bin/python3` - Pillow is on the system interpreter, not
Homebrew's. Beat *n* frames at `XMIN = (n-1)*2000 - 100`, `XMAX = (n-1)*2000 + 1300`.
`random.seed(111108)` keeps re-runs byte-identical.

Thin build over the shared engine (`from excalidraw_kit import *`): it holds only the
composition, the beat scaffold and the bespoke illustrations. Never hand-place elements
in the `.excalidraw`; never edit `excalidraw_kit.py`.

### Bespoke illustrations (one-offs - they stay in the build, never in the kit)

- `md_file()` - the rulebook card: titled header plus swatch-and-text rule rows. Used for
  both the design.md (blue) and the project's CLAUDE.md (indigo).
- `slide_thumb(kind=, generic=)` - one slide. `kind` picks the layout (`title`,
  `section`, `two-col`, `content`) so beat 5's template row reads as a *sequence* rather
  than four copies; `generic=True` drains the colour to grey, which is how beat 1's
  unprepared output and beat 7's interchangeable decks read.
- `deck()` - a stack of slides rather than a single one.
- `swatch_strip()` - a palette row; returns its right edge so what follows can be laid
  out against it.
- `toggle()` - a tweaks switch, on and off.
- `human_gate()` - the human-in-loop marker. **Not** the kit's `person()`, which is sized
  for a crowd of tiny figures and reads as a paper dart standing alone; this marker is
  safety-bearing so it has to be unmistakable. Same helper and same green as Day 10.

## Validation record

`finish()` reported **0 text-overflow and 0 text/text collision warnings**, so there is
nothing to justify. `python3 build_all.py` runs **BUILD OK | GUARD PASS** across every
scene in the repo. Previewed whole-board plus a close-up x-window on all eight beats.

Two things the rasteriser caught and the build now fixes:

1. The beat 2 step cards had their coloured header strip empty with the number and name
   floating below it, so each card read as an untitled panel. The badge and the name now
   sit **inside** the strip and the card is shorter.
2. The docstring's pan-order label for beat 1 had drifted from the heading actually on
   the board.

**Note on the rasteriser:** `preview.py` ignores element `angle`, so the rotation jitter
on notes and chips does not show in the PNGs. It is in the scene and shows in Excalidraw.
Beat 1's three attempts and beat 7's three decks are deliberately drawn `generic=True`
with no colour - the sameness is the point in both places.

## Constraints this board is held to

- No Excalidraw `frame` elements (a literal frame is a hard `build_all.py` guard
  failure), no boxes, no connector spine, no inter-beat arrows, no colour-band washes,
  white background. Beats are separated by whitespace only - **the whitespace is the
  camera**.
- Uniform slots, `WID = 1200`, content ~1120 x ~980, `GAP = 800`.
- All text hand-drawn (`fontFamily 1` / `HAND`), `roughness 1`, `lineHeight 1.4`. No
  typed sans or mono anywhere. Body and explanation text stays ink or grey.
- Headings via the kit's `heading()`. No step-number circle, no highlighter sweep, no
  sparkles.
- Examples generic, not Phlo-specific. No Phlo branding or logo, no patient or clinical
  specifics, **and no other company's brand assets**. Phlo-native material appears only
  in the live cut-away at the demo badge.
- Fictional identifiers only. Any clinical or dispensing flow drawn anywhere shows the
  human verification gate: AI drafts, a human approves, the record updates.
- Product proper nouns exact: Claude, Artifact, Project, Skill, MCP, Connector, Cowork,
  Claude Desktop, Claude Tag, Dispatch, Claude Design.
- British English, hyphens not em dashes, no Oxford commas.
