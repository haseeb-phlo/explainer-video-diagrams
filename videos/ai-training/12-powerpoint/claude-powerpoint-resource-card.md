# Resource Card - Day 12: Claude in Microsoft PowerPoint

Paste this into the AI Ops Learn Resource Card for Day 12, alongside the Loom.

> **Verified against Anthropic's documentation on 2026-09-14.** Everything under "The
> product detail" below was checked against the live docs on that date, not carried over
> from the older module-2.7 script. Three things that changed since that script was
> written are flagged inline as **CORRECTED**.
>
> 1. Re-check the product detail at each 90-day refresh. The plan rules and the add-in
>    surface move faster than anything else on this card.
> 2. The board deliberately names **no plan, no add-in and no limit** - "PowerPoint"
>    appears in its title and its demo badge and nowhere else. That is why the 2026-09-14
>    doc check changed this card substantially and the board barely at all. Keep it that
>    way: **if something here changes, fix the card, not the board.**
> 3. **There is no Day 12 entry in `Phlo_Mandatory_AI_Course_Curriculum.docx`**, and the
>    module-2.7 entry that exists describes the older *product walkthrough* rather than
>    the argument-construction video this now is - so the resource list below was rebuilt
>    from the docs rather than lifted from the curriculum.

---

## What you are shipping today

**One deck built from an agreed outline, with a headline on every slide that states a
position.** That is the whole assignment. Not a beautiful deck - a deck that argues for
something specific.

**Pause-and-try:** take your last deck and rewrite three slide titles so each states a
claim. Three, not the whole deck.

## The one sentence to take away

**The failure here is not an ugly deck. It is a tidy one that makes no argument.**
Formatted is not reasoned, and formatted is what passes review.

## The seven things from the video

1. **It looks finished and says nothing.** Eight slides with titles, bullets and a chart
   each will sail through review and still not tell anyone what to do. Go looking for the
   slide that says why any of it matters - usually it was never asked for.
2. **Structure first, slides second.** Agree the outline in the chat before anything gets
   designed. **If the outline is wrong, every minute of design after it is wasted.**
3. **One idea per slide, one line that carries it.** "Q3 results" is a topic and commits
   to nothing. "Margin fell because unit cost rose" is a claim someone can push back on.
   **If the headline could be a chapter title, it is not doing any work.**
4. **Build it from a source.** Give it the report and the numbers, not a sentence. A deck
   built from a prompt is built from nothing: plausible, generic, and not about your
   figures.
5. **Design is not its strength.** It is good at the order of an argument. It will follow
   a template you hand it, but it will not decide what your brand is. **Structure, not
   design** - the brand pass stays with a person.
6. **The plausible deck.** Three decks can all be well made, completely interchangeable
   and none of them capable of changing a decision. See the catch below.
7. **Outline to deck, live.** Outline agreed first, deck built from it, every headline
   stating a position. **The argument is the deliverable.**

## The catch, written out

Beat 6 is the one to practise, because it is the failure you will not notice.

**Before** you build anything, write one sentence naming the **decision you want**. Then
read **only the headlines**, in order, and ask whether they argue for it.

- Good: *"approve the re-tender of the packaging contract"*
- Good: *"move the Q1 budget from paid search to retention"*
- Useless: *"give an update on Q3"*, *"align the team"*, *"share what we found"*

A deck whose headlines read "Q3 results / Background / Our options / Next steps" is a
**table of contents**, not a case. Four topics, no position, nothing to disagree with. If
you cannot find the sentence your headlines are arguing for, the deck does not have one -
and no amount of design will add it.

Three decks that all fail the same sentence are telling you **the brief was wrong**, not
that you need a fourth.

## The safety rule, repeated

**Nothing confidential goes in a deck you are going to send out.**

- Everything you paste into a prompt or upload as a source is content you are handing to a
  tool. Treat it the way you would treat a shared folder.
- Fictional placeholders only in any example: `Patient_001`, `J. Doe`, `NHS_TEST_123`,
  `acme.pharmacy@example.com`.
- **Do not build on a template or a file you do not trust.** A document or deck from
  outside can carry instructions of its own, which is a real risk whenever you feed
  outside files in - and feeding outside files in is exactly what beat 4 asks you to do.
- A deck is never finished because Claude produced it. **You own what goes out**, and for
  anything patient-facing or regulated that review is not optional.

---

## The product detail that did not fit on the board

The board is about building an argument and names no plan or feature on purpose. This is
the mechanical surface, kept here so the board does not date. **Verified 2026-09-14.**

### Two different things, often confused

**1. Creating and editing files in the Claude chat.** You describe the deck and Claude
writes a genuine PowerPoint file by running code, then hands it to you. It comes out as a
real `.pptx` and opens in PowerPoint, Google Slides or Keynote like any file a colleague
would send.

- **Available to all Claude users - Free, Pro, Max, Team and Enterprise** - on the web,
  Claude Desktop and Claude Mobile.
- **Maximum 30MB per file**, for both uploads and downloads.
- Creates `.xlsx`, `.pptx`, `.docx` and `.pdf`, plus Python scripts and PNG
  visualisations. **Download the file, or save it straight to Google Drive.**
- **It has to be switched on, and on a Team plan that is not your switch.** Free, Pro and
  Max users enable it themselves under **Settings > Capabilities**. On **Team and
  Enterprise an owner enables it organisation-wide** under **Organization settings >
  Capabilities**, with optional network-access restrictions. **Phlo is on a Team plan**,
  so if you cannot find it, that is why - ask an owner rather than assuming it is gone.

**2. Claude for PowerPoint - the add-in.** A Claude sidebar inside PowerPoint that builds
and edits the deck you have open.

- **CORRECTED: generally available to Pro, Max, Team and Enterprise plans.** The older
  2.7 script said "Pro plan and up" and an earlier draft of this card hedged that Team was
  unconfirmed. **Team is explicitly included, and it is GA rather than beta.**
- **CORRECTED: it is now part of "Claude for Microsoft 365"**, alongside Claude for Excel,
  Word and Outlook, and it **shares context across those apps** - one conversation can
  span your open deck, workbook, document and inbox.
- **Team and Enterprise gate:** an organisation owner must turn on **Organization settings
  > Office agents > "Let Claude work across apps"** before an individual can enable it.
  Same pattern as file creation above, and the same answer if you cannot see it.
- **Install:** the "Claude for Microsoft 365" listing on Microsoft AppSource, then sign in
  from PowerPoint. Admins can deploy org-wide through the Microsoft 365 Admin Center
  (Settings > Integrated apps), or via a custom manifest XML if the Office Store is
  disabled.
- **Supported:** PowerPoint on the web; Windows with a Microsoft 365 subscription, build
  16.0.13127.20296 or later; Mac 16.46 or later. **Not supported:** PowerPoint 2016 and
  2019 perpetual or volume licence, PowerPoint on iPad, PowerPoint on Android.
- **Template awareness - this is the fact beat 5 is scoped against.** Claude "reads the
  slide master, layouts, fonts, and color scheme in your deck and uses them when
  generating or editing slides. It aims to maintain template compliance without
  introducing off-brand elements." So it **does** follow a template you hand it. What it
  does not do is decide what your brand *is* - which is exactly what beat 5 says, and the
  docs back it (see limitations below).
- **Persistent instructions:** the add-in's Settings sidebar has an Instructions field
  that applies to every PowerPoint conversation. **It is per-app** - instructions set in
  PowerPoint do not apply in Excel or Word.
- Supports **Connectors** (pulling external context into a deck) and **Skills** (reusable
  task recipes - Day 7). Long conversations auto-compact. Usage counts against your normal
  Claude account limits.

### Anthropic's own limitations list - worth reading aloud

The docs say Claude for PowerPoint is **not recommended for**:

1. **"Final client deliverables without human review."**
2. **"Presentations containing highly sensitive or regulated data without proper
   controls."**
3. **"Replacing your judgment on design and narrative flow."**

All three are on the board already: (1) and (3) are beats 5 and 6, and (2) is the red rule
on beat 7. If anyone pushes back on the caution in this video, that list is Anthropic's,
not ours.

### The prompt-injection warning, verbatim

> "Only use Claude for PowerPoint with trusted files. Files from external sources can
> contain hidden instructions that manipulate the add-in into extracting data, modifying
> records, or performing destructive actions."

The docs name **downloaded templates, vendor files, collaborative documents and data
imports** specifically, and say testing has identified real scenarios where the add-in can
be manipulated this way. When Claude proposes a risky operation you are asked to confirm -
**read those confirmations, especially for files from outside.** This is the documented
basis for beat 7's "do not build on a template or a file you do not trust", and it matters
most on beat 4, which is the beat that tells you to feed outside files in.

### Governance facts a regulated pharmacy should know

From the add-in's data-handling section, and **not obvious**:

- Inputs and outputs are deleted on the backend **within 30 days**; data is cached for
  some hours after deletion.
- **Chat history is stored locally in your browser (IndexedDB)** - not on Anthropic's
  servers, not synced across devices, clearable from Settings.
- **It does not inherit custom data-retention settings your organisation may have set**,
  and **add-in activity is not included in Enterprise audit logs.** For Enterprise orgs
  with the Compliance API enabled, sessions *are* covered, but that coverage is in public
  beta.
- Model choice in the add-in is a **curated subset** of Claude models and is also governed
  by your organisation's model-access settings.

### Steering a deck once it exists

You do not redo it, you steer it. Asks that work, from the docs and the old 2.7 board:

- *"Simplify the text on slide 3, it's too dense."*
- *"Combine slides 5 and 6 into a single summary."*
- *"Turn these bullets into a process flow diagram."*
- *"Restructure the storyline across slides 4 to 7."*
- *"Reorder slides to lead with recommendations first."*
- *"Make slide four's headline state the position, not the topic."* (ours, not theirs -
  this is beat 3 applied)

### Four decks genuinely worth handing over

1. **A report into slides** - paste the document, get a deck.
2. **A recurring team update** - on a template it already knows.
3. **A training deck** - a process, step by step.
4. **A first draft to react to** - far faster to fix a draft than to face a blank file.

Every one still needs beat 3 applying afterwards. A report turned into slides arrives with
the report's *topics* as headlines, which is exactly the failure this video is about.

## Resources linked from this video

**All three checked on 2026-09-14.**

- **Claude for PowerPoint** (the add-in):
  `https://claude.com/docs/office-agents/powerpoint`
  **CORRECTED:** the old support-centre URL used by the 2.7 script
  (`support.claude.com/en/articles/13521390-use-claude-for-powerpoint`) now **301s** here.
  Link the new one.
- **Create and edit files with Claude** (the chat path, which is what the demo shows):
  `https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude`
  Live and current.
- **Claude for Excel and PowerPoint updates** (11 March 2026):
  `https://claude.com/blog/claude-excel-powerpoint-updates`
  Cross-file context sharing, Skills inside the add-ins, and deployment via Amazon
  Bedrock, Google Cloud Vertex AI and Microsoft Foundry.

**Do not link** `claude.com/blog/create-files`. The 2.7 script had it, but it is the
**September 2025 launch announcement**: it describes file creation as a *preview* limited
to Max, Team and Enterprise, and tells people to enable it under *Settings > Features >
Experimental*. Both statements are now wrong, and the settings path no longer exists. Kept
here only so nobody re-adds it.

## Where this sits in the series

- **Day 10 - design work with Claude** established the parent idea: the advanced failure
  is not a bad output, it is an acceptable one. Generic passes review.
- **Day 11 - design.md** made that judgement permanent in a file.
- **Day 12 - this one** points the same instinct at a deck, where an acceptable-but-empty
  result costs you a decision that never gets made.

If you only did one of the three, do this one - but Day 10's catch and this one's are the
same move: **name the test before you look.**
