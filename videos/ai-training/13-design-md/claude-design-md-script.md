# Day 13: design.md - narration script (~7 min 10, Loom)

Board: `videos/ai-training/13-design-md/claude-design-md.excalidraw` (8 beats, one slot
each, `GAP = 800`). **Day 13** of the AI training series.

> **Source note.** There is **no Day 13 entry** in
> `Phlo_Mandatory_AI_Course_Curriculum.docx` - the day series is newer than the docx.
> Board and narration were written from `claude-design-md-prompt.md`, which was in turn
> distilled from a third-party tutorial transcript. **Reconcile against the curriculum
> when a Day 13 entry exists** - particularly the hook, the pause-and-try and the
> resource list.

> **One deliberate departure from the source, and do not undo it.** The tutorial this is
> based on downloads a real brand's `design.md` from a public repository, has another
> model strip out "the proprietary content", renames the file, and feeds that in -
> because Claude will not reproduce a real brand's guidelines. That is routing around a
> refusal, and it is off this board and out of this script. What survives is the
> mechanism: start from a *reference* `design.md` rather than a blank one, and take your
> rules from your own brand assets. Beat 3 says the refusal is correct behaviour. **Do
> not put the laundering step back in, on the board or on camera.**

Cues:
- `[CAM]` - talking to camera, board not shared
- `[BOARD: beat N]` - share the Excalidraw board and pan to beat N
- `[CUT TO CLAUDE DESIGN]` / `[BACK TO BOARD]` - the live cut-away, marked on the board
  with an orange demo badge on beat 6

Beat numbers match the build script's slot numbers and the sections below run in board
order, so you only ever pan **left to right**. Hold roughly 3 seconds of whitespace
between beats - the gap is the transition.

> **Runtime, measured not asserted.** 1,027 spoken words, **~7 min 10 at 150 wpm**,
> including ~20s where the beat-6 cut-away takes longer to *do* than to say. The hard cap
> is 8 minutes, so this has **50 seconds of headroom and no more** - this is the longest
> board in the series after Day 4, and it earns the length by carrying three files plus
> the compounding trap. **If you ad-lib, trim as you go.** A first draft ran 1,262 words
> and would have recorded at **8 min 45, past the cap**; the trims came out of every
> section except beat 7 and beat 3's red rule. Per-section word counts are in
> `claude-design-md-prompt.md`; re-measure if you rewrite.

**Loom chapters:** Hook (0:00) · Why this matters (0:14) · Content (0:33) · Pause and try
(6:24) · Close (6:44). Beats 6 and 7 are the long ones - 3:21 to 5:58.

**If you need a shorter cut:** beats 5 and 8 are the droppable pair (50 seconds, taking
it to ~6 min 20) - the template
distinction can be said in one line over beat 2, and the export list is on the Resource
Card. **Beat 7 is the one to protect**, then beat 3's red rule.

**What dates fastest on this board:** nothing, by design - no product name beyond Claude
Design itself, no plan tier, no model, no button names. The version-specific detail (the
model picker, the effort setting, the build time, where the files live in the project
tree, the export options) is deliberately on the Resource Card. **Re-check the card, not
the board, before each re-record.**

---

## 0:00 - 0:14 · Hook [CAM]

Most tutorials tell you to pick a template, give it a name and start prompting. Do that
and you get something generic, and then you spend longer rescuing it than preparing would
have taken.

## 0:14 - 0:33 · Why this one matters [CAM]

Day 10 was about judgement. This one is about making that judgement permanent: three
files, prepared before you prompt. Get them right and the first draft is already close,
every correction afterwards carries forward on its own, and you stop paying the same tax
on every deck.

## 0:33 - 1:00 · Start in the wrong place [BOARD: beat 1]

Here is the loop to avoid. Pick a template, name it, start prompting, and out comes
something generic that is not yours. So you go again. And again.

Three goes, still generic, and you paid for all three - because nothing you corrected in
run one was written down before run two. The preparation is cheaper than the rescue, and
unlike the rescue, **you only do it once.**

## 1:00 - 1:36 · Three files, before you prompt [BOARD: beat 2]

Three files, in this order, each built from the one before it.

One: a **design.md** - the rules. Colours, type, spacing. Two: a **design system** -
those same rules, turned into something Claude Design uses natively. Three: a
**template** - how a deck is actually laid out.

The line underneath is the one to hold on to: **the design system decides how everything
looks, the template decides how a deck is arranged.** Build them once and they apply to
everything after - and not only slides. Carousels, newsletter visuals, one-off graphics.

## 1:36 - 2:24 · design.md is the rulebook [BOARD: beat 3]

File one. A `design.md` is a plain text file that says how a design should look: colours
by name and hex, type, spacing, radius, how a button or a card is styled. It is plain
text, so it works in any AI tool - Claude Design is what turns it into something native.
And you start from a reference, not a blank page.

Now the red line, and this one matters. **Claude will not reproduce a real brand's
guidelines, and that refusal is correct.** Do not route around it by finding another
company's file and laundering the names out. Take your rules from your own brand assets:
if you cannot say where a colour came from, it is not yours.

## 2:24 - 2:57 · The design system makes it native [BOARD: beat 4]

File two. You hand it the design.md and it builds a working style guide - and generates
sample mockups, so you see the style before anything depends on it. Wrong? Say so in
plain English: *replace the dark background with this hex from our own palette.* No
settings panel, exactly as on Day 10.

And this is the step that pays you back: upload your logo, your icons and a
voice-and-tone file once, here, and every design after this has them without asking.

## 2:57 - 3:21 · The template is the layout [BOARD: beat 5]

File three - the one people conflate with file two.

Left, the design system: colours, type, logo. How it *looks*. Right, the template: title
slide, section divider, two columns, closing. Which slides exist and in what order. How
it is *arranged*.

Together, every new deck starts on brand and pre-structured. Give the template feedback
too - every future deck reads it.

## 3:21 - 5:02 · Two kinds of feedback [BOARD: beat 6]

Now the part that makes it compound. Two kinds of feedback, and you should know which
one you are giving.

Left, the kind that carries forward. *Make the eyebrow labels more prominent, put them in
a container* - and ask for it to be written down. It goes into a `CLAUDE.md` in the
project, read before every new design, so it applies to this deck and every deck after.

Right, the kind that does not, and should not. Edit one element. Annotate - draw on the
slide and say what you want. Or add a tweak: one switch for a decision that repeats on
every slide, like whether your logo shows.

And the three lines at the bottom matter, because people merge these constantly. Same
filename, three different jobs: Claude's memory is about *you*, across chats - Day 3. A
CLAUDE.md in Claude Code is how to work in a codebase - Day 4. A CLAUDE.md in a design
project is standing instructions for *these designs*.

`[CUT TO CLAUDE DESIGN]` - demo badge: *show in Claude Design: give feedback once, then
open the project's CLAUDE.md*

Let me do it live. Here is the feedback - and there, in the project files, is the
CLAUDE.md with my correction written into it. New chat, next deck, it still applies.

`[BACK TO BOARD]`

## 5:02 - 5:58 · Everything compounds, mistakes too [BOARD: beat 7]

This is the beat to stay awake for. Everything I have just sold you is compounding, and
**compounding runs both ways.**

One wrong rule saved into the system - eyebrow labels, eleven pixels, grey. Too small,
and now it is a rule. Every deck after inherits it, and so does every new chat, because
the CLAUDE.md is read before each one. And look at the three decks: they all look fine.
Nothing on screen says anything happened. That is the silent part.

So, the catch. **Keep one reference design, and re-render it after every change to the
system.** One design where you already know what it should look like. Before the change:
still right. After: wrong - caught in ten seconds instead of in ten decks.

That is Day 7's rule, test on a known input, pointed at a design system.

## 5:58 - 6:24 · Then it leaves the room [BOARD: beat 8]

Getting it out: PowerPoint, PDF, or one standalone HTML file - and that last one is worth
knowing, because it opens in any browser for anyone you send it to, with nothing to
install.

Then the bit that has not changed since Day 10: a person signs it off. Looking finished
and being right are still different things, and **nothing goes out without the human
pass.**

## 6:24 - 6:44 · Pause here, and try it [CAM]

Pause the video. Write the first ten lines of your own `design.md` - the colours you
already use, by hex, and the two type sizes you always reach for. You are not writing a
brand book. And if you do not know your own hex codes, that is the finding.

## 6:44 - 7:10 · Close [CAM]

What you are shipping today: a design.md, and a design system built from it.

The idea underneath: **prepare once, and every design after this one is cheaper.** But it
all compounds - so keep one reference design and re-render it whenever you change the
system, or you compound the mistakes just as efficiently.

Resources and the version-specific detail are on the Resource Card below.

---

## On-screen demo steps

Not read aloud - this is the performance behind the cut-away in beat 6. **Rehearse it
once and keep it to 30 seconds.** It is the only cut-away on the board, and it exists to
prove one thing: that feedback lands in a file you can open.

Everything below is invented, generic content: an internal workshop deck. No Phlo
branding, no patient, clinical or confidential material, and no other company's brand
assets, at any point.

1. In **Claude Design**, open an existing design project with a deck already in it.
2. Give it the beat-6 feedback, and ask for it to be written down:
   `make the eyebrow labels more prominent - put them in a container. Save this so it
   applies to every future deck in this project.`
3. When it finishes, open the project's file list and show the **`CLAUDE.md`**. Read the
   captured line out loud - that is the whole payload of the cut-away.
4. Optional, only if you are ahead of time: start a new chat in the same project and show
   that the rule still applies without re-typing it.
5. **Do not** demonstrate creating a design system from scratch on camera - it takes far
   longer than the video has, and the Resource Card carries the timing.

---

## Recording notes

- Voice: warm, plain, a colleague who has already paid the tax you are about to avoid.
  **Beat 7 is the one to slow down for** - "compounding runs both ways" is the sentence
  the whole board exists to deliver.
- Open `claude-design-md.excalidraw` full-screen and frame **one beat at a time**; the
  whitespace gaps are the camera moves. Beat *n* sits at `x = (n-1) * 2000`.
- End framed on beat 8 so the board can be paused on the human pass.
- Three object colours are constant and worth pointing at as you go: **blue is the
  design.md, green is the design system, teal is the template.** Green is also the human
  pass on beat 8, held from Day 10 on purpose.
- Do not say "Claude Design will copy your brand" - it builds a system from rules *you*
  supply. The distinction is the point of beat 3's red line.
