## Intelligence Scale type

I'll follow the evaluation skill and rate only the product in the Gemini spec.

The skill file is large, so I’ll read it in sections and follow it exactly.

I’ll check the skill’s remaining rules and the Spark, schedule, and research sources that decide Type II.

Web fetch was blocked, so I’ll pull the cited Help pages directly and check how this repo structures evaluations.

**Intelligence Scale capability: 1.6 / 3.0**

Type I with early Type II capabilities. Evaluated 2026-09-29 from the Gemini Apps brief (reviewed 2026-09-28). Strongest supported configuration: Google AI Ultra, including experimental Spark where offered. Chassis only, not the Gemini models, the API, or Workspace side panels.

Gemini Apps is a chat assistant on the web, mobile, Chrome, and Messages. People still own the work. Connected Apps, Deep Research, Gems, and scheduled prompts are native assistance. Spark can run a described task on a timer or an email, with a remote browser and computer, but that unit stays a task. It is not a persistent actor that owns a business process.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| I.1 | 1.00 | Signed-in chat on gemini.google.com, mobile, Chrome, Messages, and other surfaces; drafts, summaries, and files in ordinary work. | https://support.google.com/gemini/answer/13275745?hl=en |
| I.2 | 1.00 | Files, Search, notebooks, and Connected Apps including Workspace (read and create events, notes, and tasks). User can @ an app or let Gemini pick. | https://support.google.com/gemini/answer/13695044?hl=en |
| I.3 | 1.00 | Deep Research plans then writes a report. Chrome can complete multi-step actions and auto-browse. Canvas builds a doc, app, slides, or code. | https://support.google.com/gemini/answer/15719111?hl=en |
| I.4 | 1.00 | People edit and regenerate prompts, edit Canvas, confirm custom-app writes, pause Spark, and take over browser steps. | https://support.google.com/gemini/answer/13275745?hl=en |
| I.5 | 1.00 | Gems, notebooks, memory, scheduled actions, and work or school admin controls support repeatable use, not a one-off demo. | https://support.google.com/gemini/answer/15146780?hl=en |
| II.1 | 0.25 | Scheduled actions are recurring prompts. Spark runs a task a person describes; a time or an email can start that task. No actor takes each case from a queue to an outcome across runs. | https://support.google.com/gemini/answer/17094507?hl=en |
| II.2 | 0.75 | Deep Research and Chrome progress through a multi-step run. Spark can continue a task, but it is experimental, supervision is required, and the user may have to take over browser steps. | https://support.google.com/gemini/answer/17094507?hl=en |
| II.3 | 1.00 | In a run, Gemini uses granted Connected Apps, Search, files, and Workspace actions without the person coordinating each call. Setup grants do not lower this. | https://support.google.com/gemini/answer/15229592?hl=en |
| II.4 | 0.75 | Spark is a durable experimental personal agent with schedules, skills, and a remote browser and computer. It has no principal, permissions, or credentials of its own; it uses the person's access. | https://support.google.com/gemini/answer/17094507?hl=en |
| II.5 | 0.75 | Spark has a work panel, pause and resume, takeover, and activity history. That supervision is experimental, personal Pro or Ultra only, and not a full exception and audit loop. | https://support.google.com/gemini/answer/17094710?hl=en |
| II.6 | 0.75 | GA scheduled actions start recurring prompts in the background. Email-event starts exist only on experimental Spark. No webhooks. One GA trigger kind. | https://support.google.com/gemini/answer/16316416?hl=en |
| III.1 | 0.25 | Unattended runs are scheduled or described tasks. Routine organizational operations still require people. Spark requires supervision. | https://support.google.com/gemini/answer/17094507?hl=en |
| III.2 | 0.00 | Daily Brief suggests items for the person to complete or dismiss. No actor determines and allocates operational work. | https://support.google.com/gemini/answer/17077455?hl=en |
| III.3 | 0.00 | Skills combine inside one Spark task. No persistent actors coordinate or delegate to each other. | https://support.google.com/gemini/answer/17094296?hl=en |
| III.4 | 0.00 | Memory personalizes later chats. No detect, decide, execute, observe, and evaluate loop that changes later operations. | https://support.google.com/gemini/answer/13594961?hl=en |
| III.5 | 0.00 | No native ability to change how work is organized, reallocate actors, or create operational paths. | https://support.google.com/gemini/answer/17094507?hl=en |
| III.6 | 0.00 | Activity and admin controls govern an assistant. The product cannot make routine human intervention exceptional. | https://support.google.com/gemini/answer/14620100?hl=en |

- **Completed floor:** 1
- **Next Type raw progress:** 0.71 (4.25/6)
- **Weakest criterion:** 0.25 (II.1)
- **Weakest-link penalty:** 0.13
- **Adjusted progress:** 0.58
- **Final score:** **1.6**

### What prevents the next Type?

Type II is incomplete, so the score stays below 2.0. II.1: no persistent actor owns a process and takes each case from a channel or queue to an outcome across runs. II.2: unattended progression through process steps, branches, and retries is not GA; the background agent is experimental and can require browser takeover. II.4: no actor principal, permissions, or credentials; Spark is experimental and uses the person's access. II.5: in-run supervision is experimental and personal-plan only, without a complete approval, exception, and audit loop. II.6: GA initiation is recurring prompts only; event triggers are experimental, and webhooks are absent.

## Execution coverage

I'll follow the evaluation skill and rate only the product in `specs/gemini.md`.

The brief is Gemini Apps. I’ll verify the cited Help pages that decide span, sharing, reach, catalog, surfaces, adoption, and ready-made jobs.

**Execution coverage: 0.62 / 1.00**

Gemini Apps, as of 2026-09-29, is Google’s hosted chat assistant (web, mobile, Chrome, Mac), not the Gemini API. The strongest supported setup is Google AI Ultra or Workspace AI Ultra Access. People across functions can draft, research, and make files on it today. Work stays single-player, and almost every company job is still designed in chat.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| E.1 | 1.00 | Signed-in personal, work, and school users draft mail and posts, research, and create Docs, Sheets, slides, and code. Not one craft or one suite. | https://support.google.com/gemini/answer/13275745?hl=en |
| E.2 | 0.50 | Workspace is an org account with admin controls. Chats stay single-player. Canvas sharing is a public link the recipient copies. Work mobile users cannot create public chat links. Shared notebooks open in separate Gemini Notebook, not this product. | https://support.google.com/gemini/answer/14620100?hl=en |
| E.3 | 0.75 | Connected Apps read and act in several systems: summarize Gmail, create Calendar events in Google or third-party apps, export Docs, Sheets, and Drive files. Workspace writes called out are events, Keep notes, and Tasks. Comments, images, and Drive folders are excluded. A connector name is not write-back. | https://support.google.com/gemini/answer/13695044?hl=en |
| E.4 | 0.75 | A first-party Connected Apps directory spans many vendors, not one craft. It is mostly connectors. Custom MCP is a private server URL, not org publishing into a marketplace. | https://support.google.com/gemini/answer/13695044?hl=en |
| E.5 | 0.75 | Work happens on the web app, mobile app, Mac app, and Gemini in Chrome. Messages is personal-only. No workplace mail or chat surface, and no Gemini Apps API or embed. Chrome is a gradual rollout. | https://support.google.com/gemini/answer/14554984 |
| E.6 | 1.00 | Personal sign-in is immediate. Work and school need a qualifying Workspace edition and admin enablement, with documented licenses, history, and data controls. No platform assembly. | https://support.google.com/gemini/answer/13278668 |
| E.7 | 0.50 | Deep Research and a few premade Gems (Storybook, Learning coach) are ready. Other jobs are prompts, hand-written Gems, or scheduled prompts. Spark’s describe-a-task path is experimental and personal-only. | https://support.google.com/gemini/answer/15719111?hl=en |

* **Raw mean:** 0.75
* **Weakest criterion:** 0.50
* **Weakest-link penalty:** 0.125
* **Uncapped score:** 0.625
* **Span cap:** none
* **Final score:** **0.62**

### What most limits coverage?

E.2 and E.7. There is no shared run where several people and an operator see the same state. Ready-made jobs do not cover several business functions, so a team still designs each job by hand.
