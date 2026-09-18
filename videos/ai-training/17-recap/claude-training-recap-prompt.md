# Day 17 - That's the course - the commissioning brief

The record of what this video was asked to be and the decisions taken building it.

---

## Slug and file

- **Folder:** `videos/ai-training/17-recap/` - **Day 17**, the closing video
- **Build:** `build_recap.py` → **`claude-training-recap.excalidraw`** · 9 beats · ~6 min 32, no cut-away

## The brief, as given (2026-09-18)

> "Create a summary video presentation for day 15 on everything that is being covered,
> congratulating everyone, and recapping some of the main points and any next steps which
> they should implement. This should be in the AI training folder."

**Scope was confirmed before authoring.** "Day 15" was about sequence, not the slot - Day 15
is the Excel video, shipped two days earlier. "Congratulating everyone", "everything that is
being covered" and "next steps" all point at a **programme wrap-up**, and the user confirmed:
build it as the wrap-up, recapping the whole series.

## It was built as Day 16 and renumbered to 17 mid-build

**Day 16 (Claude in Microsoft Outlook) landed on main while this board was being drawn.**
That cost two things, and the second matters far more than the first: the recap took the next
free number, **and it had to absorb the day it had just been scooped by.** A recap that omits
a shipped video is wrong on the day it is published.

**Before recording, check `videos/ai-training/` against `DAYS`, `CATCHES` and `BUILT` in the
build script.** If another Day has landed, it belongs on beats 3 to 7, in the script, and on
the card - and the count changes everywhere.

## What it covers

The **eleven built days**: 3, 4, 7, 8, 10, 11, 12, 13, 14, 15, 16. Days 1, 2, 5, 6 and 9 do
not exist. **The board does not paper over that** - it says "eleven videos", never "seventeen
days". Beat 1's badge row, beats 3 to 7, the script and the card all key off `BUILT`.

---

## The recap has a thesis, and that is the whole design

A wrap-up that lists ten topics is a contents page. Reading the ten boards back to back,
something better was already there: **the adversarial beat is the same failure every time.**

| Day | The failure it named |
|---|---|
| 7 | a Skill that omits the assumption you never said out loud |
| 8 | a long run whose small errors compound out of sight |
| 10 | an acceptable design - generic passes review |
| 11 | a self-review that is not a second opinion |
| 12 | a tidy deck that argues nothing |
| 13 | a wrong rule saved into the design system, propagating silently |
| 14 | a fluent rewrite that drops the clause |
| 15 | an answer that is wrong although every row is right |
| 16 | a reply that is well written and commits you to something |

**The dangerous output is never the bad one. It is the acceptable one.** That is beat 2, it
is the red beat, and it is what makes this a wrap-up rather than an index. Beat 2 also carries
the catch that is the **parent of the other ten** - *"name what it has to get right, before
you look at it"*, which is Day 10's, and which every later day specialises.

**Do not flatten beat 2 back into "here is what we covered."**

---

## Decisions that are load-bearing

**Every catch on beat 7 is quoted or near-quoted from that day's own board.** They were read
back out of the `.excalidraw` files, not written from memory, and the source line for each is
in a comment beside `CATCHES` in the build. **A recap that misquotes the course is worse than
no recap** - if a day's catch changes, change it here too.

**No demo badge, deliberately.** Every other Day has a live cut-away. This one teaches nothing
new, so there is nothing to demonstrate; the actionable beat is 8, and those are things the
viewer does afterwards, not things the presenter performs. Adding one would pad a video whose
whole job is to be short.

**Beat 7 is the one wide slot** (1600, not 1200). Two columns of five is inherently wide, and
it is the page people will screenshot. Widened rather than made taller, for the reason Day 14
and Day 15 both record: on a 16:10 laptop, height binds framing.

**The three outputs on beat 2 carry no jitter and one neutral grey.** The sameness *is* the
point - a tilt or a colour each would read as three real options rather than three
interchangeable ones. Day 10's beat 6 and Day 12's beat 6 record the identical exception to
the house jitter rule. Do not "fix" any of the three.

**Green = the human pass**, held from Days 10, 11, 13, 14 and 15. Beat 9's gate is green, and
so is the beat - the one place on the board where those coincide.

**The red rule gets the last word** (beat 9). Every day in the series carried an on-screen
data rule; this is a mandatory course for a regulated pharmacy, so the closing board restates
it rather than assuming ten previous mentions stuck.

**Audience: everyone.** This is deliberately the general-audience register again, after Day
15 went specialist. It names CRISPE, Projects, Skills and Cowork as proper nouns but glosses
each in the same breath, and the one advanced day is flagged as such on beat 6 ("for the
modellers") rather than assumed.

---

## Runtime

Budgeted ~5 min 50. First draft measured **7 min 00** - the fourth recorded instance of this
repo's drift lesson, after Days 10, 14 and 15. Trimmed across eight beats to 926 words, then
Day 16 was folded in, landing at **981 words, ~6 min 32**. That is over the 4-6 target and
comfortably inside the 8:00 cap. An eleven-day recap genuinely has more ground than a
single-topic board, and 6:32 was judged the right trade rather than dropping a day.

Beat 1 and beat 9 were **not** trimmed on the same pass. Beat 1 is the congratulation and
beat 9 is the close, and both are the wrong places to save fifteen seconds.

## Provenance

No curriculum entry, like Days 10 to 15. Written from this brief and from the ten shipped
boards, which are the authoritative source for what the course actually says. **Reconcile
before recording.**
