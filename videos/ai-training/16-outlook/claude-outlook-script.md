# Day 16 - Claude in Microsoft Outlook - narration script

**Board:** `videos/ai-training/16-outlook/claude-outlook.excalidraw` (built by `build_outlook.py`) · **7 beats**
**This is the CLOSE of the Microsoft block** - Word, Excel, PowerPoint, then this. Beat 7 is the block's payoff, not this video's, and it assumes the other three have been watched.

> **The recording for this board is filed under Day 14.** The Outlook add-in Loom (<https://www.loom.com/share/10e4eaa90c0c4cf584c1fc562b3ed912>)
> was attached to `videos/ai-training/14-word-powerpoint/` on 2026-09-17 at the user's
> request. **Day 16 carries the board and the product detail; Day 14 carries the video.**
> Day 14's pause-and-try was widened to three strands so its task covers the reply too.

**Measured: 776 spoken words = ~5 min 10 board, + a 10s hold on beat 6 and a ~30s cut-away on beat 7 = ~5 min 50** (hard cap 8:00).
The first draft measured 822 against a 756-word budget - this repo's 2x-drift lesson landing for the fourth time, on a script whose own header warns about it. Trimmed twice.

Re-measure after every edit. This repo's recorded process lesson is that per-beat second budgets drift by up to 2x against written prose, and it has bitten on Day 10, Day 14 and Day 15:

```bash
# the '*' class drops BOTH bold labels and italic stage directions -
# an earlier version excluded only '**' and counted the beat-6 hold as prose
awk '/^## Narrat/,/^## Demo/' claude-outlook-script.md | grep -vE '^(#|>|\*|\[|-)' | wc -w
```

> **Reconcile before recording.** No curriculum entry exists for this video - confirmed with the user on 2026-09-17, who gave explicit go-ahead to write from `claude-outlook-prompt.md`. Product facts verified against Anthropic's live docs on the same date - see `claude-outlook-resource-card.md`.

---

## Narration

> **Voice:** peer to peer, and slightly more serious than the other three. This is the only surface in the block that produces outbound communication. No hedging, no "always double-check" - give them one failure and one catch.

### [BEAT 1] 0:00 - 0:34 · orange · *the inbox is not a document*

**Hook (0:00 - 0:10)**

"Every other tool in this block fails inwards. A clumsy clause, a wrong average, a deck that argues nothing. This one fails outwards."

**Why this matters (0:10 - 0:34)**

"Your inbox holds two different jobs, and from the outside they look like one. Triage is deciding: what needs you, what can be handled, what is noise. Drafting is only wording.

Most people open this and ask for the second. Then they wonder why it only saved them ten minutes. The deciding is the expensive half, and the one you can hand over first."

### [BEAT 2] 0:34 - 0:58 · violet · *it drafts, you send*

"One status line before we go on. Claude for Outlook is in beta, and it drafts only. It has no permission to send.

Every reply it writes lands unsent in the compose pane, and you press Send. That is not a setting somebody can switch off - it is the shape of the thing. Nothing leaves without you."

### [BEAT 3] 0:58 - 1:42 · blue · *the thread is the brief*

"Here is the habit that changes the output most, and it costs nothing: stop explaining the background.

Look at what is already above the reply box. The schedule changed, you checked it against the agreement, procurement signed off the price review in June, and now they want to move the cutover. It has read all of it.

So do not retype it. Ask what you actually want: what has been decided, what is still open. Every answer cites the email it came from, and clicking it lands you on the original. That is your check - not whether the summary sounds right, but whether the email it points at says so."

### [BEAT 4] 1:42 - 2:20 · teal · *tone is most of the job*

"Four replies to one message. They want to push the cutover two weeks.

The answer is no in all four. Warm: really sorry, the 26th does not work our end. Neutral: we are not able to move it. Firm: the date is fixed. On the record: we are unable to agree a change.

The content is identical. What changes is the register - and the register is the decision. It picks your register up from your sent folder, and that genuinely works. What it cannot know is which relationship you are in today."

### [BEAT 5] 2:20 - 2:59 · indigo · *know what it can see*

"Scope, quickly - and it matters more here than anywhere else in the block.

A mailbox is not your filing cabinet. Most of what is in it was written by somebody else: other people's words, attachments you did not write, things sent to you in confidence. It reads the email you have open, and when you ask, it reaches the rest - search, other threads, the calendar.

So check what your organisation's data agreement covers before you point it at a mailbox. And one more: email from outside is untrusted input. Treat it as data, never as instructions."

### [BEAT 6] 2:59 - 4:27 · red · *the reply that commits you*  ← THE BEAT. Hold the silence.

"Now the one that costs you something.

You asked for a friendly reply, agree where we can, keep it short. This came back. Read it.

*[hold, ten seconds, say nothing. The silence is the beat - it is counted in the runtime above.]*

Nothing in it is badly written. It is short, it is warm, and it sounds like you. And it agreed to three things.

It agreed to hold the current volumes to the 26th. That is a date. It agreed to absorb the four pence uplift this quarter. That is a price. And anything that slips beyond that sits with us. That is a liability.

Three sentences, and not one of them was yours to give.

Notice what changed since the last beat. There, you decided the answer and chose only the register. Here the draft decided for you, and it decided so well that review never stopped on it - because review reads for tone, and the tone was perfect.

So the catch. Read only the sentences that contain a commitment: a date, a number, an obligation. For each one, name who authorised it. If you cannot name them, it does not go.

Tone is not the review. Tone is what gets a draft past one."

### [BEAT 7] 4:27 - 4:56 · green · *one conversation, four apps*  (+ ~30s cut-away)

"This is the payoff for all four videos, and it only lands if you have the other three.

One conversation: unit cost is four pence higher than the model says - update it, redo the cost slide, then draft the note to the supplier."

**[CUT TO CLAUDE DESKTOP]** - *see Demo steps below. Recording note: the doing happens in the Office add-ins with Claude Desktop open alongside, not in the chat window on its own.*

**[BACK TO BOARD]**

"Change the figure once. The slide follows. The email that reports it follows too. Nothing copied between them, because it is one conversation standing across four apps."

### Pause and try (5:26 - 5:42)

"Pause here. Find a reply you sent this week and read it for what it promises rather than how it reads. Look for a date, a number or an obligation you agreed to without noticing you had agreed.

Most people find one."

### Close (5:42 - 5:52)

"One conversation. Four files. And one rule that outlasts all four: nothing leaves the building until you have read it.

That is the block."

---

## Demo steps - beat 7 cut-away (~30 seconds)

Badge on the board: *"show in Claude desktop app: change a figure in Excel, rebuild the slide, then draft the email that reports it"*.

1. Open the generic supplier workbook. Change the unit cost by 4p, in one cell.
2. In the same conversation, ask for the cost slide to be rebuilt off the new figure. Show the slide updating.
3. Still the same conversation: ask for the note to the supplier reporting the change.
4. **Stop on the unsent draft.** Do not press Send on camera - the whole board argues that pressing Send is the human's move, and sending a demo email undoes beat 2 and beat 6 in one gesture.

Use fictional identifiers and a generic business example throughout. No Phlo branding, no real supplier, no customer or clinical detail.

---

## Ships

One drafted reply, read for what it commits to before sending.

## What to watch

**Outlook is in beta.** If that changes before this is recorded, **beat 2 is the only beat that needs rebuilding** - the fact lives in one constant (`BETA_LINE`) in `build_outlook.py` and appears nowhere else on the board. Keep the replacement the same length or shorter and nothing reflows. The narration change is the second paragraph of beat 2 and nothing else.
