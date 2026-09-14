# Resource Card - Day 12: design.md

Paste this into the AI Ops Learn Resource Card for Day 12, alongside the Loom.

> **Three things to do before publishing this card.**
> 1. **There is no Day 12 entry in `Phlo_Mandatory_AI_Course_Curriculum.docx`**, so the
>    "Resources linked from this video" list could not be lifted from it. The links below
>    are **named, not pasted** - put the current URLs in and check each one resolves
>    before the card goes live.
> 2. Everything under "The version-specific detail" is **product surface that dates
>    fast**, and it came from a third-party tutorial rather than from Anthropic
>    documentation. **Re-check all of it against Claude Design before publishing**, and
>    again at each 90-day refresh.
> 3. **The board itself names no plan, model or button**, deliberately, which is why it
>    will still be true when this card has gone stale. Keep it that way: if something
>    here changes, fix the card, not the board.

---

## What you are shipping today

**A design.md, and a design system built from it.** Not a finished deck - the two files
that make every future deck cheaper.

**Pause-and-try:** write the first ten lines of your own `design.md`. The colours you
already use, by hex, and the two type sizes you always reach for. You are not writing a
brand book. And if you do not know your own hex codes, that is the finding.

## The one idea

**Prepare once, and every design after this one is cheaper.** Three files, in order,
before you prompt. Every correction you make afterwards carries forward on its own -
which is the whole point, and also the trap (see the catch, below).

## The three files

| | What it is | What it decides |
|---|---|---|
| **1. design.md** | A plain text file of rules: colours by name and hex, type, spacing, radius, how a button or a card is styled. Works in any AI tool. | The raw rules |
| **2. design system** | Those same rules, turned into something Claude Design uses natively, with sample mockups generated for you to review. | **How it looks** |
| **3. template** | A pre-built deck in your style: title slide, section dividers, two-column, closing. | **How it is arranged** |

Build all three once and they apply to everything you make afterwards - **and not only
slides**: social carousels, newsletter and email visuals, one-off graphics.

## The eight things from the video

1. **Start in the wrong place and you pay three times.** Pick a template, name it, start
   prompting, and you get something generic. Three goes later it is still generic, and
   you paid for every run - because nothing you corrected in run one was written down
   before run two.
2. **Three files, in order.** Each is built from the one before it.
3. **design.md is the rulebook.** Plain text, so it works anywhere. Start from a
   reference, not a blank page.
4. **The design system makes it native** - and generates mockups so you can see the style
   before anything depends on it. Correct it in plain English; no settings panel.
5. **The template is the layout, not the look.** This is the distinction people conflate.
6. **Two kinds of feedback.** One carries forward, one does not, and you should know which
   you are giving.
7. **Everything compounds, including the mistakes.** The catch is below. This is the one
   to remember.
8. **A person still signs it off.** Looking finished and being right are different things.

## The catch, written out

Beat 7 is the beat to practise, because it is the failure you will not notice.

A wrong rule saved into the design system - or bad feedback captured into the project's
`CLAUDE.md` - propagates to **every future design and every new chat in that project**,
and nothing on the screen tells you it happened. The outputs all look fine. That is what
makes it silent.

**Keep one reference design, and re-render it after every change to the system.**

- Pick one design where you already know exactly what it should look like.
- Render it *before* the change and *after*. Same input, both times.
- A difference you did not ask for is the bug - caught in ten seconds instead of in ten
  decks.

That is **Day 7's rule - test on a known input - pointed at a design system** instead of
at a Skill. Same discipline, different object.

## Three things share these names. Do not merge them.

This is the single easiest thing on the day to get wrong, so it is on the board and it is
here too.

| | What it is | Where it is taught |
|---|---|---|
| **Claude's memory** | What Claude remembers about **you**, across chats. Off by default on Team and Enterprise. | Day 3, beats 11-12 |
| **`CLAUDE.md` in Claude Code** | Standing instructions for how to work in **a codebase**. | Day 4, beat 8 (the instruction-writing discipline only) |
| **`CLAUDE.md` in a design project** | Standing instructions for **these designs** - written when you ask for feedback to be saved, and read before every new design in that project. | **Day 12, beat 6** |

Same filename in two of the three. Three completely different jobs.

## The two kinds of feedback

**Carries forward** - ask for it to be written down, and it goes into the project's
`CLAUDE.md`:

> make the eyebrow labels more prominent - put them in a container. Save this so it
> applies to every future deck in this project.

**This deck only** - and it should be:

- **edit** - change one element yourself.
- **annotate** - draw on the slide and say what you want.
- **tweaks** - one switch for a decision that repeats on every slide, such as whether
  your logo appears or slide numbers show. Flip it to compare before you commit, then
  save the setting you want as the default.

Rule of thumb: **edit and annotate to fix one thing in one place. A tweak when one
decision touches every slide. The CLAUDE.md when the correction should outlive this
deck.**

## The safety rules, repeated

**1. Take your rules from your own brand assets.** Claude will not reproduce a real
brand's guidelines, and **that refusal is correct behaviour, not an obstacle.** Do not
route around it by taking another company's design file and stripping the names out of
it. If you cannot say where a colour came from, it is not yours.

**2. Nothing confidential goes in.** A design.md, a design system and a template are
shared files that other people can open.

- No unapproved designs, no private codebase, nothing patient-facing.
- Fictional placeholders only in any example: `Patient_001`, `J. Doe`, `NHS_TEST_123`,
  `acme.pharmacy@example.com`.
- Anything that touches prescriptions, dispensing or patient records keeps the human
  gate: **Claude drafts, a person approves, then the record is updated.**
- Check the Phlo AI Use Policy before anything made this way goes in front of a patient.

**3. A design is never brand-final because Claude Design produced it.** A person does the
last pass and owns what ships. Carried over from Day 10 unchanged.

---

## The version-specific detail

Kept off the board on purpose - **all of it dates faster than anything on the board, and
all of it came from a third-party tutorial rather than from Anthropic documentation.
Verify before you rely on it.**

### Building the design system

- Start a **new chat in Claude Design** and use the **create design system** option.
- Give it a short description of the style you are after, then **upload your design.md**.
  Most of the other fields on that form can be left alone.
- **It takes a while** - on the order of **10 to 20 minutes** - because it is reading the
  file, extracting every colour, font and spacing rule, then generating sample slides and
  components for you to review.
- **Model and effort:** the tutorial picked the latest Opus model with effort set to
  maximum, on the grounds that it does the job without the heavier token cost of the
  largest option. **Both the model list and that setting move - check what is current.**
  (Note this is Claude Design's own effort control, not the API parameter of the same
  name, which Day 3 deliberately leaves out.)
- There is a **team checkbox** on the review screen you can ignore if you are working
  alone.
- Use the **feedback** control on any generated mockup to correct it in plain English.
- You can **upload more than the design.md**: a voice-and-tone or voice-principles file
  so the copywriting sounds like you, your logo, and any icons you use repeatedly. Do
  this once and every future design has them.

### Building the template

- Once the design system looks right, ask for a template directly: *go ahead and build a
  slide deck template for workshops and trainings - you pick the number of slides.*
- **Give the template feedback before you rely on it**, because every future deck
  references it. Useful things to check: does the background treatment apply to all
  slides or only the covers, is any colour being used that you would not choose, does the
  text scale to fill the space, is your logo in the footer.

### Generating a deck

- On the Claude Design home page, select **the design system**, then **the matching
  template**, then attach your talking points - **plain markdown is fine**.
- Ask it to *turn the attached talking points into a workshop deck, and ask me anything
  you need before you build.*
- It will **pause and ask clarifying questions** before building. **Answer them
  properly** - a few minutes here saves a lot later. There is usually a **decide for me**
  option if you genuinely do not know.
- **Rename the project** to something descriptive, because you will come back to it. The
  point of the CLAUDE.md is that your **next** deck starts as a new chat in the *same*
  project rather than in a new one.

### Finding things in a project

Navigation is not obvious. The design system button returns you to the home page, and a
project's files sit under an **all project files** drop-down - templates and decks are
folders inside it, and opening the HTML file brings the slides back up.

### Getting it out

- **PowerPoint** and **PDF** are direct exports.
- **More formats** includes a **standalone HTML file**, which is the most versatile
  option: download it, double-click it, and it runs in any browser. Anyone you send the
  file to can open it the same way, with nothing to install and no account.
- HTML export has **advanced options** worth exploring - the tutorial had asked for a
  **presenter view** button that opens interactive speaker notes during the talk.

---

## Resources to link under the video

Paste the current URLs and check each resolves.

- Claude Design - the current getting-started documentation
- The Phlo AI Use Policy (internal)
- Phlo's own brand assets: the colours, type and logo files staff should actually be
  building a `design.md` from. **If this does not exist as a single findable thing, that
  is worth fixing before this video ships** - the whole day assumes people can answer
  "where did this colour come from?"
- The board itself: `videos/ai-training/12-design-md/claude-design-md.excalidraw` - open
  it full-screen and pan beat to beat if you want the argument without the narration

## Related videos in the course

- **Day 10 - design work with Claude** - the judgement half. Reference beats adjectives,
  one element at a time, presentable is not correct. **Watch it first**; Day 12 makes its
  habits permanent.
- **Day 11 - Claude Design, job by job** - sits between Day 10 and this one in the running
  order: the six-step loop, wireframes, the handoff, motion graphics, and the review that
  only looks like a review. **Watch it before this one.**
- **Day 7 - Skills** - where "test on a known input" comes from. Day 12's catch is the
  same rule pointed at a design system.
- **Day 4 - Claude Projects** - where the instruction-writing discipline comes from, and
  one of the three things called `CLAUDE.md`.
- **Day 3 - Prompting and CRISPE** - Claude's memory, the third thing in that table.
