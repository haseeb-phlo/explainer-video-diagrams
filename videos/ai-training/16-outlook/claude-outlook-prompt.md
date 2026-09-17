# Claude in Microsoft Outlook - the commissioning brief

The record of what this video was asked to be, and the decisions taken building it. It is the
source of record, because **there is no curriculum entry** - see *Provenance*.

---

## Slug and file

- **Folder:** `videos/ai-training/16-outlook/`
- **Build:** `build_outlook.py` → **`claude-outlook.excalidraw`** · 7 beats · ~5 min 10 board + ~40s of hold and cut-away
- **Commissioned:** 2026-09-17, as the fourth and last board of the Microsoft block. Moved into the training series as **Day 16** the same day, before first commit.

**The brief carried a tension in its own header, and the user resolved it.** It called this
board the close of "all four days" while writing the path into `videos/claude/<NN-outlook>/` -
the older per-feature series rather than the authoritative day-by-day one. It was first authored
at `videos/claude/14-claude-outlook/`, following the written path, and the user then directed it
into the training series. **The "days" half of the brief turned out to be the accurate one.**

**This is NOT a move in the sense Days 4, 7, 8, 10, 12 and 15 are**, and it should not be
recorded as one. The relocation happened the same day, **before anything was committed**. No
`claude/` folder was retired, nothing was left behind, and **the `claude/` numbering is
untouched - 14 is still free there.** The only trace of the first location is one historical
line in the build script's docstring.

**File names follow the destination series, not the brief.** The brief specified
`build_outlook.py` → `outlook.excalidraw`. Inside `ai-training/` every board uses a
`claude-<topic>` prefix for its scene and its three documents (Day 15 is `build_excel.py` →
`claude-excel.excalidraw`), so the scene and documents were renamed to match and the build
script kept its briefed name. Consistency within the series beat the literal filename, because
the series convention is what a future reader navigates by.

---

## The brief, as given

> **Claude in Microsoft Outlook**
>
> File: `videos/claude/<NN-outlook>/build_outlook.py` → `claude-outlook.excalidraw` - NEW folder, slug to be agreed.
>
> Action: NEW board. Copy the adapted `build_word.py` as the scene template so the block stays
> visually consistent. This board also carries the closing beat for all four days.
>
> Beats and runtime: 7 beats, roughly 5 minutes.
>
> Why this day exists: The only one of the four where the output leaves the building, and the
> only one still in beta. It closes the block because the cross-app payoff is most legible once
> the other three exist.
>
> | Beat | Accent | Heading on the board | What is drawn |
> |---|---|---|---|
> | 1 | orange | the inbox is not a document | Two different jobs drawn side by side: triage, which is about deciding, and drafting, which is about wording. Most people ask for the second when they need the first. |
> | 2 | violet | it drafts, you send | Status beat, kept short and stated in ink: beta, drafts only. Chip: "nothing leaves without you". |
> | 3 | blue | the thread is the brief | The conversation above the reply drawn as the context. Chip: "stop explaining the background that is already in the thread". |
> | 4 | teal | tone is most of the job | Four replies to the same message at four registers, with the change marked. The point is that register is the decision, not the content. |
> | 5 | indigo | know what it can see | Scope. A mailbox holds other people's words, attachments and things sent in confidence. Generic chip: "check what your organisation's data agreement covers before you point it at a mailbox". Keep this generic on the board; the specifics go in the narration and the Resource Card. |
> | 6 | red | the reply that commits you | Adversarial beat. A helpful, well-judged draft that agrees to a date, a price or a liability nobody authorised. Chip: "read it for what it promises, not for how it reads". |
> | 7 | green | one conversation, four apps | The payoff for the whole block, landing once, here. One thread touching the document, the sheet, the deck and the reply: change the figure in the sheet, the deck follows, the email that reports it follows too. Demo badge: "show in Claude desktop app: change a figure in Excel, rebuild the slide, then draft the email that reports it". |
>
> Pan order: Left to right, beats 1 to 7, one slot at a time. Document it in the build script docstring.
>
> Ships: One drafted reply, read for what it commits to before sending.
>
> Pause-and-try: Find a reply you sent this week that agreed to something without you noticing you had agreed.
>
> Watch out: Outlook is beta and the only surface here that produces outbound communication. If
> the beta status changes before recording, beat 2 is the only beat that needs rebuilding - keep
> it visually self-contained so the board can be patched rather than re-recorded.

The shared constraints (Style B, no frames, uniform slots, hand font, one adversarial beat,
generic examples, British English, demo cut-away conventions) were applied verbatim and are not
restated here - they live in `CLAUDE.md` and `.claude/skills/SKILL.md`.

---

## The scene template: what was actually copied, and why

**The brief says "copy the adapted `build_word.py`". No adapted Word build exists.** The only
`build_word.py` in the repo is `videos/claude/9-claude-word/build_word.py`, the original
module-2.9 product walkthrough, and a search of every local and remote branch turns up no
adapted version. Rather than block, this board was built from
**`videos/ai-training/14-word-powerpoint/build_word_powerpoint.py`** (Day 14), which is:

- the most recent Microsoft-apps board in the repo,
- the one that already absorbed the Word walkthrough, so "visually consistent with the block"
  means consistent with it, and
- the source of the one-offs this board needed - `human_gate`, `_strike` and the compose/window
  furniture.

If an adapted `build_word.py` lands later and diverges visually, this board should be
reconciled against it rather than the other way round.

---

## Decisions that are load-bearing

### 1. Beat 2 is built to be patched, not re-recorded

The brief's "watch out" only holds if the beta fact is structurally isolated, so it is:

- it lives in **one module-level constant, `BETA_LINE`**, and appears nowhere else on the board;
- **no other beat names beta, a plan or a tier** - all tier facts are card-only, which is the
  "name the tool, never the tier" line Day 12, Day 14 and Day 15 all draw;
- the replacement string must be **same length or shorter** so nothing reflows. That is the
  `ai-foundations/1-what-is-ai` fix and the Day 10 beat-2 regeneration, both of which held their
  layout by holding their string length.

The matching narration change is the second paragraph of beat 2 and nothing else.

### 2. One worked example runs the board, and it is deliberately Day 14's

The same generic packaging-supplier re-tender. By the time a viewer reaches beat 7 they have
already seen this contract edited in Word and argued in PowerPoint, so "one conversation, four
apps" lands as a fact about a job they recognise rather than as a diagram.
**Change it and beats 3, 4, 6 and 7 all move together.**

**The continuity is the SCENARIO, not the figures.** Day 14 pins a 9% Q3 unit-cost rise and a
renewal-notice clause; this board pins a 4p unit-cost rise and a cutover date. They are different
facts in the same story, so do not "reconcile" the numbers across the two boards - matching them
would assert a relationship that does not exist.

**There is exactly one number on this board, 4p, said twice in the same unit** (beat 6's draft
absorbs it, beat 7's ask reports it). An earlier draft also carried a "4% uplift" in beat 3's
thread, so a viewer heard *four per cent* and then *four pence* two beats apart and took one for
a misstatement of the other - **on the adversarial beat, whose entire instruction is to read the
numbers rather than the tone.** Beat 3's thread item is now figure-free and must stay that way.
Day 14's docstring records the same failure class.

### 3. The beat 4 / beat 6 flip is intentional

On beat 4 the answer is **no** - the date holds - and you choose only the register. On beat 6 a
draft quietly says **yes** to the same request. That is not a contradiction and the narration
names it: beat 4 is you making a decision, beat 6 is a draft making one for you. It is what
turns the adversarial beat from a warning into a reversal of something the viewer just did.

### 4. The adversarial beat is about commitment, not quality

Word, Excel and PowerPoint all fail inwards - a clumsy clause, a wrong average, a deck that
argues nothing. Those cost a rewrite. This one fails outwards, so the failure drawn is a
**well-written** draft that agreed to a date, a price and a liability. **Nothing on the draft is
badly written, and nothing on it is red.** Do not "improve" the beat by adding a clumsy sentence
or a wrong fact - the absence of one is the lesson, the same rule Day 15's beat 6 states about
its sheet. The catch is a falsifiable instruction in the shape Day 10's beat 6 established:
read only the sentences containing a commitment, and name who authorised each.

### 5. The red data caution sits on beat 5, not the closing beat

Days 7, 10, 12, 14 and 15 all park it on the last beat. Here **beat 5 is the data beat**, so the
rule belongs where the subject is. It is drawn in **red on an indigo beat** so it still reads as
the regulated-course caution rather than as more scope material, and it carries a second line
the docs back: email from outside is untrusted input, to be treated as data and never as
instructions.

### 6. Green = the human pass, and on this board it is beat 2

Held constant from Days 10, 11, 13, 14 and 15. It sits inside a **violet** beat on purpose: this
is the first gate in the repo where the thing being gated leaves the organisation, so it is
drawn at hero size in green rather than tinted to its beat. **Beat 7's green is the scaffold
accent, not the marker** - there is no second gate drawn on it.

### 7. Beat 6 is the one wide slot (1600, not 1200)

Three columns' worth - the artefact, the commitments lifted out of it, and the catch. Widened
rather than made taller, because height binds framing on a 16:10 laptop. Day 14's beat 10 and
Day 15's beat 6 record the identical call.

### 8. The demo badge text and the recording reality differ - flagged, not fixed

The badge reads *"show in Claude desktop app: …"* because the shared constraints mandate that
prefix and the brief spells the string out. The demo itself happens in the Office add-ins with
Claude Desktop open alongside. The string is used verbatim and the recording note sits beside
the `[CUT TO CLAUDE DESKTOP]` cue in the script so the presenter is not caught out on the day.

---

## Provenance

**There is no curriculum entry for this video.** `Phlo_Mandatory_AI_Course_Curriculum.docx` is
the course's stated source of truth for script blocks and is not in the repo. The user was
asked on 2026-09-17 and confirmed that no entry exists, giving explicit go-ahead to write board
and narration from this brief - the same route Days 10 to 15 all took. **Reconcile before
recording.**

**Product facts were verified against Anthropic's live documentation on 2026-09-17.** Primary
source: `claude.com/docs/office-agents/outlook`. The full read, and everything displaced from
the board, is on `claude-outlook-resource-card.md`. **When a fact moves, fix the card, not the board** -
the only board string that dates is `BETA_LINE`.

---

## If it needs a shorter cut

**Beats 4 and 5 are the droppable pair** (-1 min 17, taking it to ~3 min 53 + cut-away). Nothing
later depends on either: beat 6 reaches back to beat 4 in one sentence of narration, which can
be cut with it. **Beat 6 is the one to protect**, and beat 7 cannot be dropped at all - it is
the block's close and no other board carries it.
