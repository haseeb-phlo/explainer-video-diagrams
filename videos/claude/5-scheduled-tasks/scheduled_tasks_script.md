Video script
Format notes for you: target run time 12-14 minutes. [BEAT n] tells you which Excalidraw board to be on. [DEMO] means switch to your live Claude Desktop screen. [CAM] means your face is the main shot. Spoken lines are written to be read aloud naturally. British English throughout.
Before you hit record - quick checklist: Claude Desktop open and logged in; Cowork visible in the sidebar; at least Slack and Outlook connected; one real channel you can demo against; close anything with patient data on screen.

0:00 - 0:40 | Hook
[CAM]
"Right, quick question. How much of your week is the same handful of jobs, over and over? The Monday status write-up. The morning scan of Slack and your inbox. The weekly numbers you pull together for a meeting nobody remembers scheduling.
What if those just happened, on their own, and the finished result was sitting there waiting for you each morning? That is what Claude Scheduled Tasks does. By the end of this video you will know exactly what they are, the one rule that trips everyone up, and you will have automated your first job. Let's get into it."

0:40 - 1:30 | What it actually is
[BEAT 2]
"So, plainly: a scheduled task is a job you describe to Claude once, that Claude then runs for you automatically on a schedule.
Normally, every time you want Claude to do something, you open it up, you type the prompt, you wait, you copy the result. A scheduled task flips that. You set it up one time, you tell Claude how often to run it, and from then on it runs itself and hands you the finished output. A daily briefing. A weekly report. A tidy-up of a folder. You write the instructions once and you stop thinking about it."
[PRESENTER NOTE: point at the Before/After cards as you say "flips that".]

1:30 - 2:30 | What you need first
[BEAT 3]
"Before anyone goes and tries this, here is what you need, because this is where people get stuck.
First, the Claude Desktop app. Not the website, not your phone - the desktop application, because scheduled tasks live inside a feature called Cowork, and Cowork is desktop only.
Second, a paid plan. Pro, Max, Team or Enterprise. The free tier does not have this.
Third, Cowork needs to be switched on. On our Team and Enterprise setup, that is controlled by an admin, so if you genuinely cannot see Cowork in your sidebar, that is the reason, and that is an AI Ops question, not a you problem.
And fourth, the more of your work tools you have connected - Slack, Outlook, Jira, Beacon, Xero - the more useful these tasks become, because a scheduled task can reach into all of them."

2:30 - 3:30 | How a task runs
[BEAT 4]
"Here is the mental model for how one of these actually runs.
You write the prompt once. You pick how often it should run. When the time comes, Claude opens its own fresh session, completely separate from whatever you are doing, and it carries out the instructions. While it works, it can use everything you have set up - your connected tools, any skills, any plugins. And then it delivers the result for you to review.
The key idea is that each run is independent and self-contained. It is like sending a very capable colleague off with a clear brief, who comes back with the work done."

3:30 - 4:30 | The one rule everyone forgets
[BEAT 5]
"Now, the single most important thing in this entire video, and the bit people miss.
A scheduled task only runs while your computer is awake and the Desktop app is open.
If your laptop is shut at the moment a task is due, the task does not run on time. It is skipped. The good news is it does not vanish - Claude runs it automatically the next time you wake your machine and open the app, and you get a notification telling you it caught up. Any skipped runs also show in the task's history, so nothing is hidden.
What this means in practice: if you want a genuine eight in the morning briefing, your machine needs to be on and the app open at eight in the morning. So pick cadences that match when you are actually at your desk. If you need something that runs come what may, even with your laptop shut, that is the cloud version, and that is a separate conversation - flag it in AI Ops and we will help."
[PRESENTER NOTE: slow down here. This is the line that saves support tickets.]

4:30 - 7:00 | Live demo: create a task from a chat
[DEMO]
"Let me show you the easy way to create one, straight from a chat.
I will start a new task in Cowork. In the prompt box, I just type a forward slash and the word schedule - /schedule - and that launches the scheduler.
Now I describe what I want in plain English. I will type:
'Every weekday at 8am, summarise yesterday's messages in our patient-care-ops Slack channel and any emails I have flagged in Outlook. Give me five bullet points, with anything urgent at the very top.'
I send that, and notice what happens - Claude asks me a couple of clarifying questions with buttons I can just tap, rather than making me type everything out. So it might confirm the channel, or the time.
Once it has what it needs, it shows me a summary: the name of the task, the schedule it will follow, and exactly what it is going to do. I read that back, and when I am happy, I click Schedule. Done. That task now exists, it is on my Scheduled list, and tomorrow morning the briefing will be waiting."
[PRESENTER NOTE: actually click Schedule on screen. Then open the Scheduled page so the new task is visible before you move on.]

7:00 - 8:15 | Live demo: the form, and what each field means
[DEMO] then [BEAT 7]
"There is a second way to create one, which gives you more control, and it is worth seeing because it shows you everything a task is made of.
I click Scheduled in the left sidebar, then New task in the top corner, and I get this form."
[BEAT 7]
"Six things. Task name - keep it short and recognisable, because your teammates may see it too. Description - one line on what it does. The prompt - this is the actual instruction, and here is a handy trick: type a forward slash inside the prompt and you can pull in plugins and skills. Frequency - hourly, daily, weekly, weekdays only, or manual if you only ever want to run it on demand. Then two optional ones: which model to use, and which folder Claude should work in if the job involves files.
Fill those in, hit Save, and it behaves exactly like the one we made from the chat."

8:15 - 9:15 | Managing your tasks
[BEAT 8]
"Everything you create lives under Scheduled in the sidebar, and you are fully in control.
You can run a task right now on demand, without waiting for its schedule - handy for testing. You can pause one if you are on leave and do not want a week of briefings piling up. You can resume it when you are back. You can edit the instructions or the timing at any point. You can look at the history of past runs. And you can delete anything you no longer need.
My one strong recommendation: when you build a new task, run it once manually first. Check the output is actually what you wanted before you trust it to run on its own."

9:15 - 11:15 | What to automate on your team
[BEAT 9]
"Let me make this real for wherever you sit in the business.
If you are in the support team or Ops, that morning briefing we just built is the obvious one - overnight Slack and flagged emails, urgent first, ready before you have made your coffee.
Delivery and logistics: a weekly summary of operational status pulled straight from Jira or Asana, so your Monday update writes itself.
Data and analytics: a weekly Beacon metrics digest, drafted and waiting for you to sense-check before it goes anywhere.
Finance: a start-of-month snapshot from Xero - spend, outstanding items, whatever you normally chase down by hand.
Marketing: a weekly tracker of what competitors are doing and what is moving in the sector.
And for absolutely everyone, the humble one - a Friday afternoon task that tidies up a shared project folder so Monday starts clean.
The pattern to look for is simple. Anything you do on a regular rhythm, that follows the same steps each time, is a candidate."

11:15 - 12:30 | Doing this safely
[BEAT 10]
"Quick but important, given where we work.
Keep confidential data out of your prompts unless you are in a properly approved, sanctioned workspace. For the kind of tasks we have talked about - briefings, ops summaries, sector news - you almost never need it, so do not put it in.
Always review the output before you act on it or pass it on. These tasks are a very capable assistant, not a replacement for your judgement.
Name your tasks clearly, so anyone glancing at what is running understands it. And pause or delete tasks you have stopped needing, so nothing is quietly running in the background that nobody owns.
If you are ever unsure whether something is appropriate to automate, ask first. That is genuinely the whole rule."
[PRESENTER NOTE: keep this section calm and brief. Do not lecture. One pass is enough.]

12:30 - 13:30 | Recap and your task this week
[BEAT 11] then [CAM]
"So, to land this.
A scheduled task means you set a job up once and Claude runs it for you on a schedule. The big rule: the Desktop app has to be open and your machine awake, or the task waits until it is. And always start small and check the result before you rely on it.
[CAM]
Here is your one action from this video. Between now and the end of the week, pick a single repetitive job - just one - and schedule it. The morning briefing is a great first one if you are not sure where to start.
If you get stuck, or you want a hand designing something cleverer, post in the AI Ops channel and we will sort it. Thanks for watching, and go get an hour of your week back."
