# Brief - Day 12: Claude in Microsoft PowerPoint

**Folder:** `videos/ai-training/12-powerpoint/`
**File:** `build_powerpoint.py` -> `claude-powerpoint.excalidraw`
**Slug:** `claude-powerpoint` (so: `claude-powerpoint-script.md`,
`claude-powerpoint-prompt.md`, `claude-powerpoint-resource-card.md`)
**Style:** Style B, per `.claude/skills/SKILL.md` and the repo `CLAUDE.md`
**Length:** 7 beats. The recorded script measures **844 spoken words = 5 min 37 at 150
wpm**, plus ~15s where the cut-away takes longer to do than to say: **~5 min 52**. Hard
cap 8, target 4 to 6 - see Runtime budget.
**Curriculum ref:** **Day 12** of the AI training day-by-day series. **No Day 12 entry
exists in `Phlo_Mandatory_AI_Course_Curriculum.docx`** - the day series is newer than the
docx, and the entry that exists describes the module-2.7 Claude + PowerPoint product
walkthrough this board replaces. Board and narration were authored from this brief, with
the user's explicit go-ahead. **Reconcile both against the curriculum when a Day 12 entry
exists.**
**Action:** ADAPT, then MOVE. The brief said to adapt the folder holding
`build_powerpoint.py`, which was `videos/claude/7-claude-powerpoint/`; it was reframed
there and moved here as Day 12 when the day-by-day series was confirmed as the
destination. **The Day number appears in exactly two places** - the build script's
docstring header and this line - so a renumber is a two-line edit plus the folder name,
not a re-audit.

## Where it sits in the series

**Day 12 is the second half of the judgement arc.** Day 10 established that the advanced
failure in visual work is not a bad output but an *acceptable* one, and that generic
passes review. Day 11 made that habit permanent in a `design.md`. Day 12 is the same
failure wearing a suit: a deck is the one artefact where "it looks finished" and "it is
finished" come apart completely, because formatting is the part Claude is best at and
arguing is the part it will skip unless you make it.

It sits **after both design days on purpose**. A viewer who has done Day 10 already knows
the shape of the trap ("name the test before you look"); this board points that same
instinct at an audience-facing artefact, where the cost of a plausible-but-empty result
is a decision that never gets made.

Per the repo precedence rule, **a Day covers its topic in full**: this board does not
signpost the old module-2 walkthrough and must never be trimmed to a "see the other
video" pointer. **There is no other PowerPoint video - `claude/7-claude-powerpoint` *is*
this one, moved.** A future reader who sees the gap at 7 in `videos/claude/` should read
it as a gap, not as a second video to cross-reference.

## Why this video exists

**The failure here is not an ugly deck, it is a tidy one that makes no argument.** For an
audience that presents to executives weekly, that is the expensive failure, and it is the
one nobody catches in review - because a reviewer checks that the slides look right,
which they do. Everything on the board serves that one sentence.

**Ships:** one deck built from an agreed outline, with a headline on every slide that
states a position.
**Pause-and-try:** take your last deck and rewrite three slide titles so each states a
claim.

## Where it came from, and what changed

This board **moved here from `videos/claude/7-claude-powerpoint/`** (module 2.7), the
same move Day 4, Day 7, Day 8 and Day 10 each made out of `videos/claude/`. That series
now has a **fifth numbering gap, at 7** - a gap is not lost work, and **nothing remaining
in `videos/claude/` was renumbered**.

It was a **nine-beat product walkthrough**: ask and get a real `.pptx`, what the file
actually is, start from what you have, tell it the shape, the two places Claude lives
(the chat versus the Microsoft 365 add-in), edit by talking, four use cases, a safety
checklist, a try-it close. That board taught a **feature surface**, and almost every
interesting fact on it was a plan tier or a file-size limit.

It is now a **seven-beat board about argument construction**. The reframe is settled by
the fact that not one of the seven headings needs the word "PowerPoint" - the board
teaches how to build a case, and the deck is only where the case happens to live.

### The on-board / on-card line

**The board names the tool, never the tier.** "PowerPoint" appears in the board title and
in the demo badge and nowhere else. Plan tiers, the Microsoft 365 add-in, the 30MB limit,
web / desktop / mobile availability, `.pptx` and Google Drive export, and the four "decks
worth handing over" use cases are **all on `claude-powerpoint-resource-card.md`**. That
card is a **deliverable, not an afterthought** - do not re-inflate the board with it, and
**when a fact changes, fix the card, not the board.**

### Four judgement calls worth recording

**1. The data caution moved onto the board rather than onto the card.** The old beat 8
carried the only on-screen data-handling rule. The seven-beat brief has no slot for it,
so it now sits on **beat 7**, in red, beside the close - because this is a mandatory
course for a regulated pharmacy and that is the only data rule a viewer sees on screen.
This is the same call Day 7 made with its red Skill caution and Day 10 with its
confidential-designs rule. **Do not quietly drop it in a later edit.** The untrusted-file
line rides along with it because it is genuinely specific to this video: a deck template
is a file from outside, and this is the one board where people are told to feed outside
files in.

**2. Beat 5 is scoped to judgement, not mechanics.** "Design is not its strength" means
**it will not make brand decisions for you**. It *does* respect a template you hand it -
the docs (verified 2026-09-14) say Claude "reads the slide master, layouts, fonts, and
color scheme in your deck and uses them", aiming to "maintain template compliance without
introducing off-brand elements". So the narration says "it will follow a template you hand
it, it will not decide what your brand is". Phrased any other way, the board, the card and
the docs contradict each other. Watch for this if the script is ever ad-libbed.

**The doc check forced one board edit here.** The right-hand column originally read "the
template" and "brand colours and type", which - given documented template awareness - read
as *"Claude ignores your template"*, which is false. They are now worded as **decisions**:
"which template to use" and "what the brand actually is". The judgement claim itself is
squarely backed by the docs, which list **"replacing your judgment on design and narrative
flow"** among the things the add-in is not recommended for.

**3. Beat 6's catch is a headline test, and it deliberately reaches back to beat 3.** The
shared constraint is "how this capability fails silently **and how you would catch it**".
The failure is three well-made, interchangeable decks; the catch is: **name the decision
you want in one sentence before you build, then read only the headlines, in order, and
ask whether they argue for it.** All three then fail, having passed the eye test. The
catch only *works* if headlines state positions, which is beat 3 - so the adversarial
beat retroactively tests an earlier one, and beat 3 stops being a style tip and becomes
load-bearing. Failure without a catch is a diagnosis with no test, and this beat is the
Best Catch feeder.

**4. The three decks on beat 6 carry no jitter and one neutral grey.** This is a
deliberate exception to the house rule that notes and chips get rotation jitter. **The
sameness is the point** - a tilt or a colour each would read as three real options rather
than three interchangeable ones. Day 10's beat 6 records the identical exception; do not
"fix" either.

## The seven beats

| # | Accent | Heading | What is drawn |
|---|---|---|---|
| 1 | orange | it looks finished and says nothing | Eight tidy slides in a 4x2 grid, every one formatted, **none of them carrying any text** - then a dashed empty slot where the argument should be, marked *- missing -*. Chip: *formatted is not reasoned*. |
| 2 | violet | structure first, slides second | The outline agreed in a chat panel before anything is designed: five numbered claims, a tick, then the deck. Chip: *if the outline is wrong, the design is wasted*. |
| 3 | blue | one idea per slide, one line that carries it | Two slides, same chart: **"Q3 results" struck through** against *"margin fell because unit cost rose"*. Below, all three headlines rewritten from topic to claim. Chip: *the headline is the argument, not the topic*. |
| 4 | teal | build it from a source | A report and a chart flowing into **an outline, not a blank box**, against a bare prompt producing a generic grey deck. Chip: *feed it the source, not a description of the source*. |
| 5 | indigo | design is not its strength | Honest beat. What it is good at (order, one idea a slide, the carrying line) against what stays yours (template, brand colours, what good looks like). The brand pass drawn as a **person**. Chip: *structure, not design*. |
| 6 | red | the plausible deck | **Adversarial.** Three interchangeable grey decks, all "looks fine", then the headlines lifted out into one strip, then the named decision, then all three fail it. Chip: *it will happily produce something nobody can disagree with*. |
| 7 | green | outline to deck, live | The agreed outline, four headline slides each stating a position, the demo badge, the red data rule, the close chip: *the argument is the deliverable*. |

**Pan order:** left to right, beats 1 to 7, one slot at a time. Documented in the build
script docstring.

**Accent cycle:** orange / violet / blue / teal / indigo / red / green - no repeats at all
on a seven-beat board, so none adjacent.

**Demo badge:** beat 7 only - `show in Claude desktop app: agree the outline in chat, then
build the deck from it`, with `[CUT TO CLAUDE DESKTOP]` / `[BACK TO BOARD]` in the script.

**The badge deliberately sits on the chat path, not on the Microsoft 365 add-in.**
Originally this was justified on plan availability - and that justification turned out to
be wrong. The **2026-09-14 doc check** established that Claude for PowerPoint is
**generally available to Pro, Max, Team and Enterprise**, so a sidebar cut-away is *not*
blocked by Phlo's Team plan.

The badge stays on the chat path anyway, for two better reasons. **One:** the chat path is
what the seven beats actually teach - agree an outline, then build from it - and the
add-in is a different surface with its own install. **Two:** the add-in has to be installed
from the Microsoft add-in store before it exists at all, so it is not guaranteed to be live
on the day, and the chat path is the one with fewer moving parts on camera. (**Corrected
2026-09-16:** this used to say both paths needed an owner to switch something on for a Team
org. File creation is enabled by default on Team, and the add-in's gates are Microsoft's,
not Claude's.)

**If the add-in is enabled for Phlo, add a second badge on beat 5** rather than moving
this one - beat 5 is where template behaviour is discussed, and the sidebar demonstrates
it directly. Same shape as Day 8's note about adding a Dispatch badge if it reaches Team.

## Runtime budget

Budgeted in seconds first, beat count second - then **measured against the written script,
which is the step that matters.** Beats are not uniform: 3 and 6 are the hero beats; 1, 4
and 5 run short.

| section | words | on the clock |
|---|---|---|
| hook | 27 | 10s |
| why this matters | 81 | 32s |
| beat 1 · it looks finished and says nothing | 72 | 28s |
| beat 2 · structure first, slides second | 81 | 32s |
| beat 3 · one idea per slide, one line that carries it | 109 | 43s |
| beat 4 · build it from a source | 71 | 28s |
| beat 5 · design is not its strength | 69 | 27s |
| **beat 6 · the plausible deck** | **161** | **64s** |
| beat 7 · outline to deck, live (+ ~15s cut-away doing time) | 96 | 53s |
| pause-and-try | 42 | 16s |
| close | 35 | 14s |
| **total** | **844** | **~5 min 52** |

**Re-measure if you rewrite the narration.** The first draft measured **872 words / 5 min
48 spoken**, which put the total past the 4-to-6 target once the cut-away was counted; it
was trimmed to 844. To re-measure:

```bash
awk '/^## On-screen|^## Recording/{stop=1} stop{next}
     /^## [0-9]/{if(s)printf "%-46s %4d w ~%3ds\n",substr(s,4,42),w,int(w/2.5); s=$0; w=0; next}
     /^(>|`\[|\[|---|- |[0-9]\. )/{next} s{w+=NF; t+=NF}
     END{printf "%-46s %4d w ~%3ds\n",substr(s,4,42),w,int(w/2.5); \
         printf "\nTOTAL %d words = %d:%02d\n",t,int(t/2.5)/60,int(t/2.5)%60}' \
  videos/ai-training/12-powerpoint/claude-powerpoint-script.md
```

**If it needs a shorter cut: beats 4 and 5 are the droppable pair** - nothing later
depends on either, and the board still lands its argument (tidy but empty → outline first
→ headlines state positions → the plausible deck → build it live). That removes 55s and
takes it to **~4 min 57**. **Beat 6 is the one to protect** - it is the longest section on
purpose and everything else was trimmed to pay for it.

## The worked example

**One generic packaging-supplier re-tender** runs through beats 2, 3, 6 and 7 - the
outline agreed in chat, the headlines rewritten as positions, the decision the deck has to
win, and the deck that finally asks for it. Everyday business, never Phlo-specific, no
patient or clinical detail, invented numbers throughout.

Pinned at the top of the build script: `DECISION` (beat 6's catch), `TOPIC_TO_CLAIM` (beat
3's rewrites), `GENERIC_HEADLINES` (beat 6's strip) and `OUTLINE` / `OUTLINE_SHORT` (beats
2, 4 and 7). **Change the example and beats 2, 3, 6 and 7 all have to move together.**

## How it is built

One flowing hand-drawn board, generated by `build_powerpoint.py`, which imports the shared
engine (`from excalidraw_kit import *`) and holds only the composition: the beat scaffold
(`OX` / `WID` / `ACCENT` / `beat_head`), the worked-example constants and this board's
bespoke illustrations. Never hand-place elements in the `.excalidraw`; change the build
script and regenerate. Never edit `excalidraw_kit.py`.

```bash
python3 videos/ai-training/12-powerpoint/build_powerpoint.py     # rebuild this board
/usr/bin/python3 preview.py videos/ai-training/12-powerpoint/claude-powerpoint.excalidraw out.png
/usr/bin/python3 preview.py <scene> out.png XMIN XMAX        # close-up on one beat
python3 build_all.py                                         # rebuild all + Style-B guard
```

`preview.py` needs `/usr/bin/python3` - Pillow is on the system interpreter, not
Homebrew's. Beat *n* frames at `XMIN = (n-1)*2000 - 100`, `XMAX = (n-1)*2000 + 1300`.

`random.seed(240712)` keeps re-runs byte-identical.

### Bespoke illustrations (one-offs - they stay in the build, never in the kit)

- `slide()` - a tidy slide: title bar, bullet lines, a small bar chart, and **zero text
  elements**. That is what makes beat 1 work: eight of them in a grid look finished and
  contain nothing, which reads better unlabelled than it would with eight invented slide
  titles. Carried over from the 2.7 build, which had it right.
- `slide_deck()` - three offset slides, one crisp in front. Extent `x..x+268, y..y+186`.
- `headline_slide()` - the counterpart to `slide()`: same furniture, but the one text
  element on it is a **full sentence** doing the arguing. `strike=` draws the title struck
  through, which is how beat 3 shows a topic heading failing.
- `struck()` / `_strike()` - the kit has no strikethrough. Text plus a line across it at
  **0.44** of the line box: with `lineHeight 1.4` the glyphs sit high in their box, so a
  line at the geometric middle crosses the descenders and reads as an underline that
  slipped. Day 10 found this the hard way; the constant is copied deliberately.
- `dashed_box()` - the kit's `rect()` has no `strokeStyle`, so an empty dashed slot is
  four dashed `line()` calls. Beat 1's missing argument.
- `human_gate()` - the human marker on beat 5. It does **not** use the kit's `person()`,
  which is sized for a crowd of tiny figures and reads as a paper dart standing alone at
  hero size. Same reasoning as Day 10's `human_gate()` and Day 3's `person_big()`.
- `chat_panel()` / `outline_rows()` - beat 2's chat window and the numbered-claim outline,
  reused at three sizes on beats 2, 4 and 7 so the outline reads as the same object each
  time.

## Documentation check - 2026-09-14

The board and card were checked against Anthropic's live documentation. **The board needed
one edit; the card needed a substantial rewrite** - which is the "name the tool, never the
tier" design working exactly as intended.

Sources read:
- `https://claude.com/docs/office-agents/powerpoint` (the add-in)
- `https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude`
- `https://claude.com/blog/claude-excel-powerpoint-updates` (11 March 2026)
- `https://claude.com/blog/create-files` (September 2025 - **superseded**, see below)

**What was wrong and is now fixed:**

1. **The add-in's plan availability.** The 2.7 script said "Pro plan and up"; a draft of
   this card hedged that Team was unconfirmed. It is **generally available to Pro, Max,
   Team and Enterprise** - Team included, GA not beta. Card corrected; the badge rationale
   above was rebuilt on this.
2. **The add-in's doc URL 301s.** `support.claude.com/en/articles/13521390-use-claude-for-powerpoint`
   now redirects to `claude.com/docs/office-agents/powerpoint`. Card relinked.
3. **`claude.com/blog/create-files` must not be linked.** It is the September 2025 launch
   post: it calls file creation a *preview* limited to Max/Team/Enterprise and tells people
   to enable it under *Settings > Features > Experimental*. Both are now false and that
   settings path is gone. Dropped from the resource list, with a note so nobody re-adds it.

**What was confirmed:** file creation on **all plans** (Free through Enterprise), web /
desktop / mobile, **30MB per file**, download or save to Google Drive, and the
prompt-injection caution - which the add-in docs state far more strongly than the old
script did, naming **downloaded templates** explicitly. That is the documented basis for
beat 7's red rule, and it lands hardest on beat 4, the beat that tells people to feed
outside files in.

**What was newly found and added to the card:** ~~file creation and the add-in both need an
owner to enable them on a Team plan~~ - **WRONG, and corrected on 2026-09-16 when the Excel
doc check (Day 15) exposed it.** File creation is **enabled by default** for Team and for
new Enterprise organisations; an owner can only *disable* it. The add-in has **no
Claude-side org gate at all** - the *Organization settings > Office agents > "Let Claude
work across apps"* path is not in the documentation. The real gates are Microsoft's: the
Office Store setting and Integrated apps deployment. Also added: the
add-in's own **"not recommended for"** list, which independently backs beats 5, 6 and 7;
and the governance facts that add-in activity is **not in Enterprise audit logs** and
**does not inherit custom org data-retention settings**, with Compliance API coverage in
public beta.

**The one board edit** is recorded under judgement call 2 above.

## Validation record

`finish()` reported **0 text-overflow and 0 text/text collision warnings**, so there is
nothing to justify. `python3 build_all.py` runs **BUILD OK | GUARD PASS** across all
seventeen scenes in the repo.

Previewed whole-board plus a close-up x-window on all seven beats. The composition came
back clean on the first render - the beat-6 layout was changed **before** building, on the
advice that three decks each carrying readable headlines would mean 9 to 12 text elements
fighting the "interchangeable" read. The headlines are lifted out into **one** strip
instead: one artefact to read, three things that fail it.

**Note on the rasteriser:** `preview.py` ignores element `angle`, so the rotation jitter
on stickies and chips does not show in the PNGs. It is in the scene and will show in
Excalidraw. Beat 6's three decks are the deliberate exception - **no jitter, one neutral
grey** - for the reason recorded above.

## Constraints this board is held to

- No Excalidraw `frame` elements (a literal frame is a hard `build_all.py` guard failure),
  no boxes, no connector spine, no inter-beat arrows, no colour-band washes, white
  background. Beats are separated by whitespace only - **the whitespace is the camera**.
- Uniform slots, `WID = 1200`, content ~1120 x ~980, `GAP = 800`.
- All text hand-drawn (`fontFamily 1` / `HAND`), `roughness 1`, `lineHeight 1.4`. No typed
  sans or mono anywhere. Body and explanation text stays ink or grey; accents are for
  headings, labels, shapes and fills.
- Headings via the kit's `heading()`. No step-number circle, no highlighter sweep, no
  sparkles.
- Examples generic, not Phlo-specific. No Phlo branding or logo, no patient or clinical
  specifics. Phlo-native material appears only in the live cut-away at the demo badge.
- Fictional identifiers only. Any clinical or dispensing flow drawn anywhere shows the
  human verification gate: AI drafts, a human approves, the record updates. **This board
  draws no clinical flow**, so the gate does not appear as a regulatory marker - the
  person on beat 5 is a brand-approval step, not a clinical one, and should not be
  described as a verification gate in narration.
- Product proper nouns exact: Claude, Artifact, Project, Skill, MCP, Connector, Cowork,
  Claude Desktop, Claude Tag, Dispatch.
- British English, hyphens not em dashes, no Oxford commas.

## Source note - READ BEFORE RECORDING

`Phlo_Mandatory_AI_Course_Curriculum.docx` is the stated source of truth for script blocks
and is **not in this repo**. There is **no Day 12 entry**, and the module-2.7 entry that
exists describes the **Claude + PowerPoint product walkthrough this board replaces** rather
than the argument-construction video it now is.

The narration in `claude-powerpoint-script.md` was therefore written from this brief, on
an explicit go-ahead rather than by default. **Reconcile it against the curriculum before
recording** - particularly the hook, the pause-and-try and the resource list. The script
carries the same note at the top.
