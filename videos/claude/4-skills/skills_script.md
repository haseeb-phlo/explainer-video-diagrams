Video script (≈13 min)
Recording setup (Loom): Screen + camera bubble, bubble bottom-right. Sit slightly off-centre so the camera bubble never covers frame content. Zoom Excalidraw to each frame as you reach it (fit-to-frame). Speak to camera for intro and recap; narrate over the board for the middle sections.
Pace target: ~145 words/min. British English throughout.

[FRAME 01 - Title] · [ON CAMERA] · ~0:45
Hi everyone. This short training is on something called Claude Skills. By the end you'll know what a Skill is, why we're rolling them out, and how to use and even create one yourself - no technical background needed.
Quick framing before we start. Most of us already use Claude for one-off tasks: drafting an email, summarising a document, tidying a spreadsheet. Skills are the next step up. They're how we stop re-explaining ourselves every time and start getting the same high-quality result, automatically. Let's get into it.

[FRAME 02 - What is a Skill?] · [SCREEN] · ~1:15
So, what actually is a Skill?
A Skill is a folder of instructions that teaches Claude how to do a specific task the way we want it done. Officially: a folder of instructions, scripts and resources that Claude loads only when a task needs it.
The simplest way to picture it is a recipe card. [Point to the folder shape.] Imagine you've got a card that says exactly how Phlo likes a report formatted - the headings, the order, the tone. Once that card exists, you don't have to explain it again. You just ask for a report, and Claude reaches for the card.
Inside that folder there are usually three things: the instructions themselves, some examples of what good looks like, and - only for more advanced Skills - optional scripts. For most Skills you'll ever need, it's really just the instructions written in plain English.
That's the whole idea. A Skill is reusable know-how, packaged up so Claude can use it consistently.

[FRAME 03 - The problem Skills solve] · [SCREEN] · ~1:00
Why bother? Look at the two sides here.
Without Skills [point left], you re-explain the same thing every single time you open a new chat. Results vary depending on how you phrased it that day. And a lot of "how we do things" lives only in people's heads, so when someone's off or leaves, that knowledge walks out the door.
With Skills [point right], you write it down once. You get the same result every time, no matter who's asking. And because Skills can be shared, the whole team benefits from one person's good thinking.
That's the shift: from explaining over and over, to defining once and reusing forever.

[FRAME 04 - How Skills work] · [SCREEN] · ~1:30
Here's the clever bit, and it has a slightly technical name: progressive disclosure. Don't worry about the term - the idea is simple.
Three steps. [Follow the arrows.] One: you give Claude a task, just like normal. Two: behind the scenes, Claude scans the Skills available to it and picks only the ones relevant to what you've asked. Three: it loads just those instructions and follows them.
The key word is "only". Claude doesn't cram every Skill into its head at once. It reaches for the right one at the right moment, a bit like you pulling one folder off a shelf rather than tipping the whole filing cabinet onto your desk.
Why does that matter to you? Two reasons. It stays fast, and it stays accurate, because Claude isn't distracted by instructions that have nothing to do with your task. You don't have to tell it which Skill to use - if the Skill's description is good, it just knows.

[FRAME 05 - Anatomy of a Skill] · [SCREEN] · ~1:30
Let's open the bonnet for a moment. This won't get technical, I promise.
A Skill is built around one file, conventionally called SKILL dot M-D. [Point to the card.] It has three parts.
A name - just a label. A description - and this one matters most. The description tells Claude when to use the Skill. And then the instructions, written in ordinary Markdown, which is just plain text with a bit of light formatting. Bullet points, headings, that sort of thing. If you can write a clear set of notes, you can write this.
[Point to the optional bracket.] For more advanced Skills you can bundle extra scripts or resources, but most Skills never need them.
The one thing to take away from this frame [point to the highlighted line]: the description is how Claude decides whether to use the Skill at all. A vague description means it might never fire. A specific one - "use this when formatting a monthly performance report" - means it activates exactly when it should. We'll come back to that in best practice.

[FRAME 06 - The four types] · [SCREEN] · ~1:30
There are four types of Skill, and you'll come across all of them.
First, Anthropic Skills [point top-left]. These are built into Claude already - things like creating proper Word documents, Excel spreadsheets, PowerPoint decks and PDFs. They switch on automatically when relevant. You're probably already using these without realising.
Second, Custom Skills [top-right]. These are ones you or your team create for our specific workflows.
Third, Organisation Skills [bottom-left]. These are provisioned by our admins and pushed out to everyone automatically. So if Phlo approves a standard way of doing something, it can appear in your Skills list without you lifting a finger.
And fourth, Partner Skills [bottom-right]. These come from the Skills Directory and are built by companies like Notion, Figma and Atlassian to work neatly with their tools.
So: built-in, custom, organisation-wide, and partner. Four flavours, same underlying idea.

[FRAME 07 - Skills vs other features] · [SCREEN] · ~1:30
Now, Claude has a few features that sound similar, so let's clear up the difference. This table is worth a screenshot.
Skills are about how to do a task, and they load only when relevant.
Projects hold background knowledge that's always loaded while you're working inside that project. Think reference material that's always on.
MCP, or connectors, give Claude access to external tools and data - they kick in when you actually call the tool.
And custom instructions are your general preferences, applied everywhere, all the time.
Here's the part people miss [point to caption]: these aren't competing, they stack. A connector might give Claude access to one of our systems, and a Skill can teach Claude how to use that connection the way Phlo wants. Different jobs, working together.

[FRAME 08 - Using a Skill] · [SCREEN: switch to claude.ai] · ~1:15
Let's see where these actually live. [Switch from Excalidraw to your Claude account.]
Three steps. Open Customize in your account. Go to Skills, then click the plus, then Browse skills - that opens the directory where you can see what's available. Then simply enable the ones you want.
[Demonstrate on screen as you talk.] Organisation Skills that Phlo has set up will already be here without you adding anything.
One practical note: Skills rely on code execution being switched on in your settings, so if a Skill doesn't seem to be working, check that first. [Show the setting briefly if comfortable, then return to the storyboard.]

[FRAME 09 - Creating your own] · [SCREEN] · ~1:30
Here's the bit I want you to actually try. You can create your own Skill, and you do not need to code.
The flow is straightforward. [Follow the boxes.] Spot a task you do repeatedly - the same report, the same kind of summary, the same checklist. Write the steps out in plain English. Add a clear description so Claude knows when to use it. Then save it, and share it if it's useful to others.
And here's a shortcut [point to the tip]: Claude has a built-in skill-creator Skill whose entire job is to help you build other Skills. You can literally describe the task in a chat and ask it to help you write the Skill. So even step one is supported.
If you take one action after this video, make it this: think of one thing you explain to Claude again and again, and turn it into a Skill.

[FRAME 10 - Best practice & governance] · [SCREEN] · ~1:15
Quickly, how to do this well - and one thing to be careful about.
On the "do" side: keep your descriptions specific, because that's the trigger. Keep one Skill to one job - it's far more reliable than a sprawling everything-Skill. And reuse approved Skills rather than reinventing them.
On the "avoid" side: vague descriptions that never fire, and cramming several unrelated jobs into a single Skill.
And one that matters for us specifically: don't put confidential or patient-identifiable information inside a Skill file. Skills are designed to be shared and provisioned across the team, so treat them like a document that could be seen widely. Keep them about the method, not the data.

[FRAME 11 - Recap & next steps] · [ON CAMERA] · ~1:00
Let's recap. Skills are reusable how-to knowledge for Claude. They load only when they're needed, which keeps things fast and accurate. There are four types - built-in, custom, organisation, and partner. And anyone, including you, can make one without writing code.
Your next step: this week, open the Skills directory, enable one Skill, and have a go at sketching your own from a task you repeat.
That's Claude Skills. Thanks for watching, and I'll see you in the next one.
[END]
