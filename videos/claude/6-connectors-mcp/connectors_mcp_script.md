# Video script - "Claude Connectors & MCP"
### Internal training | Target run time: 13 to 15 minutes

**How to read this script**
- Plain text is what you say to camera, word for word. Read it as you, not as a presenter - warm and unhurried.
- `[ON SCREEN]` tells you which Excalidraw scene to be showing.
- `[CAMERA]` / `[SCREEN]` tells you whether you are on your webcam or sharing your screen.
- `[DEMO]` blocks are a live walkthrough - the talking points are scripted, but you are clicking in real time, so adapt naturally. Use a clean, signed-out-of-anything-sensitive account and no real patient or clinical data on screen.
- British English throughout. No jargon goes unexplained.

---

## 0. Cold open  (0:00 - 0:35)
`[CAMERA - you, full screen]`

Imagine you hire a brilliant new colleague. They have read almost everything ever written, they are quick, and they never get tired. But there is a catch. They have been sitting in a sealed room since the day they started. They cannot see your inbox, your calendar, your shared drive, or any of the systems you use every day. And anything that happened after they walked into that room, they simply have not heard about.

That, more or less, is Claude on its own. Today I want to show you the thing that opens the door to that room - safely, and on your terms. It is called a Connector, and the standard behind it is called MCP.

---

## 1. What you'll get from this  (0:35 - 1:05)
`[CAMERA]`

By the end of this video you will know three things. What a Connector actually is, in plain terms. What MCP is and why it matters. And, most importantly for us, how to use them safely and sensibly in your day to day work. No technical background needed. If you can use a web browser, you can follow this.

Let me start with the problem, because it makes everything else click into place.

---

## 2. The problem: Claude on its own  (1:05 - 2:25)
`[ON SCREEN - Scene 02: Claude, straight out of the box]`

On its own, Claude is a reasoning engine with a very large general knowledge. That is genuinely useful, but it has three limits worth understanding.

First, its knowledge has a cut-off date. It learned from a huge amount of text up to a certain point in time, and it does not automatically know what happened after that. Ask it about something from last week and, without help, it is guessing.

Second, it cannot see your tools or your data. It has no view of your files, your messages, your records, or anything behind a login. It only knows what you type into the chat.

Third, and this is the one that quietly eats your time - because of the first two, you end up being the courier. You copy information out of one system, paste it into Claude, read the answer, then copy that back somewhere else. Useful, but slow, and easy to get wrong.

Connectors exist to remove that courier job. So let us define one properly.

---

## 3. What a Connector is  (2:25 - 3:55)
`[ON SCREEN - Scene 03: A Connector is a secure bridge]`

A Connector is a secure bridge between Claude and one specific tool that you already use.

That is the whole idea. With a Connector in place, instead of you copying and pasting, Claude can reach the tool directly - to find things, to fetch information, and, only when you allow it, to take an action like drafting or creating something.

Here is the analogy I find most helpful. A Connector is like giving that new colleague a visitor pass to one particular room. Not the whole building - one room. The pass only works for that room, it only lets them do certain things in there, and you can take the pass back the moment you want to. Nothing about a Connector gives Claude a free run of everything. It is deliberately narrow, and it is reversible.

`[CAMERA]`

So that is the "what". The natural next question is "how do all these different tools connect in the same way?" And that is where MCP comes in.

---

## 4. What MCP is  (3:55 - 5:40)
`[ON SCREEN - Scene 04: MCP - the standard that makes it possible]`

MCP stands for Model Context Protocol. Do not let the name put you off. A protocol is just an agreed way of doing something so that different things can work together. The metric system is a protocol. A plug socket is a protocol.

And the plug socket is the analogy that fits best. Think about how, not so long ago, every device had its own charger, its own cable, its own awkward shape. Then a common standard came along, and suddenly one type of cable could charge almost anything.

MCP is that common standard, but for connecting AI to tools. Before it, every single tool would have needed its own bespoke, hand-built integration with Claude. Slow to build, expensive to maintain. With MCP, any tool that follows the standard can connect to Claude the same way - one common shape of plug.

A few things worth knowing. MCP is an open standard, which means it is published for anyone to use, not locked to one company. It was created by Anthropic, the company behind Claude. And it has caught on quickly across the industry, to the point where there are now well over nine thousand tools and services you can connect this way.

`[CAMERA]`

Right - we know what a Connector is, and we know MCP is the standard underneath it. Now let us look at what actually happens when Claude uses one, because understanding the steps is what makes you comfortable using it.

---

## 5. How it works under the bonnet  (5:40 - 7:20)
`[ON SCREEN - Scene 05: How a Connector actually works]`

There are four steps, and none of them are complicated.

Step one. The tool runs a small piece of software - think of it as a reception desk - whose only job is to list what Claude is allowed to do with that tool. Not everything; just a defined set of actions.

Step two. Claude connects to that reception desk over a secure link.

Step three. Claude reads the list and discovers what is on offer. For example: it might see that it can search records, fetch a document, or create a draft. It only ever knows about the actions on that list.

Step four, and this is the important one. When Claude wants to do something that simply reads information, it can usually go ahead. But when it wants to do something that changes things - sending, creating, editing - it asks your permission first. You approve it, Claude does it, and brings the result back into the conversation.

`[CAMERA]`

That fourth step is your safety net, and it is built in. Claude is designed to check with you before it acts, the same way a good colleague would say "shall I send this?" rather than just sending it. Keep that in mind, because we will come back to it.

---

## 6. The two types you'll meet  (7:20 - 8:35)
`[ON SCREEN - Scene 06: Two ways to add one]`

When you go to add a Connector, you will meet two types.

The first is a directory connector. These are the ready-made ones. They have been checked by Anthropic, they appear in a built-in list, and you add them in a single click. Most of the common, well-known tools live here. These are available on every plan.

The second is a custom connector. This is for when a tool is not in that ready-made list - for example, an internal system a company has built for itself. Instead of picking from the list, you point Claude at that tool's own secure address. These are available on the paid plans.

`[CAMERA]`

One small extra thing you will notice. Some connectors are what is called "interactive". Rather than just giving Claude plain text back, they can display proper cards, tables, or little forms right inside the chat. So the experience can feel quite rich. Either way, the safety model underneath is the same.

Now, enough theory. Let me actually show you one.

---

## 7. Live demo  (8:35 - 11:20)
`[SCREEN - share your screen. Reminder: clean account, no sensitive or clinical data visible.]`

`[DEMO - talking points; click live and narrate what you do]`

- "I am in Claude now. To manage Connectors, I go into Settings, and then the Connectors section. Notice these are managed in one place."
- `[Open Settings > Connectors.]` "Here is the directory - this is that ready-made list I mentioned. Each of these is a tool I could connect with a single click."
- "I am going to add a generic example one now. Watch what happens when I do." `[Click to add / connect a directory connector.]`
- "It does not just silently switch on. It takes me to a sign-in for that tool, and it tells me exactly what access it is asking for. This is the consent step - read this screen, do not just click through." `[Point to the scopes / permission text on the auth screen.]`
- "I will approve it for this demo." `[Approve.]` "And now it is connected. Importantly, see this control here - I can disconnect it again at any time. The pass is always returnable."
- `[Go to a normal chat.]` "Now, in an actual conversation, I turn a connector on for that chat using this button by the message box." `[Open the + / connector toggle in the composer.]` "I will enable our example tool."
- "Now I will ask Claude something that needs it." `[Type a harmless, generic prompt, for example: "Find the most recent item in the example tool and summarise it."]`
- "Here is the moment that matters. The first time Claude wants to actually reach into that tool, it asks me." `[Point to the permission prompt.]` "It is telling me what it wants to do. I read it, and only then do I allow it."
- `[Allow, let it run.]` "And there is the result, pulled straight in - no copying, no pasting. Notice it only did the thing I allowed, and nothing more."

`[CAMERA]`

So in under a minute we went from a sealed room to Claude working directly with a tool - and at no point did it act without me knowing. That control is the whole point, and it leads us neatly to the most important part of this video.

---

## 8. Using Connectors safely  (11:20 - 13:05)
`[ON SCREEN - Scene 08: Using Connectors safely]`

`[CAMERA, then hold on the scene]`

Connectors are powerful, and powerful tools deserve a bit of care. Six simple principles cover almost everything.

One. Least access. Connect only the tool the task actually needs. There is no prize for connecting everything.

Two. Prefer read-only, and approve each action that changes something. If Claude only needs to look things up, it does not need permission to edit or send.

Three. Read the permission prompts. They appear for a reason. Clicking "allow" on autopilot defeats the safety net we just talked about.

Four. Be aware of hidden instructions. This one is less obvious, so stick with me. When Claude fetches content - a document, a web page, a record - that content is just data. But occasionally something malicious can be written into that data trying to trick the AI into doing something you did not ask for. Claude is built to resist this, but the human rule is simple: if Claude suddenly suggests doing something odd or out of scope, stop and question it.

Five. On our managed plans, connectors are switched on by an administrator first. You will not see a tool until it has been approved for the organisation. That is a feature, not a fault.

And six. Whatever you connect, handle personal and sensitive information in line with our data policy. The usual rules about who can see what do not go away just because there is an AI in the middle.

---

## 9. What good looks like  (13:05 - 14:00)
`[ON SCREEN - Scene 09: What good looks like]`

If you remember nothing else, remember this short checklist.

Connect only the tools you actually need. Before you allow a connector, have a quick look at what it can do. Pause on every permission prompt and read it. If something looks off, stop and report it. And disconnect any access you are no longer using - tidy as you go.

None of that is hard. It just needs to be a habit.

---

## 10. Recap and close  (14:00 - 14:45)
`[ON SCREEN - Scene 10: In a nutshell]`

So, in a nutshell. A Connector is a secure bridge from Claude to a tool you already use, so you stop being the courier. MCP is the common standard that makes those bridges possible, the same way one cable came to charge everything. And throughout, you stay in control - Claude asks before it acts, and any access you grant can be taken back.

`[CAMERA]`

That is everything you need to get started confidently. If you have a question, or you are not sure whether something is safe to connect, do ask - the details are on screen. Thanks for watching.

`[ON SCREEN - hold on Scene 10 with the "Questions?" line]`

---

### Production notes
- **Length:** trimming the demo or the "how it works" detail brings this comfortably to 13 minutes; reading at a relaxed pace lands nearer 15. Both are fine.
- **Pace:** pause for half a beat each time you switch scene - it gives viewers time to read the visual.
- **Demo safety:** rehearse the click path once beforehand so the live take is smooth, and double-check nothing sensitive is on screen or in your notifications.
- **Currency:** the wording reflects how Connectors and MCP work as of mid-2026. If Anthropic changes the settings layout or plan rules, only Scene 06, Scene 07 and the demo steps need a quick refresh - the concepts stay the same.