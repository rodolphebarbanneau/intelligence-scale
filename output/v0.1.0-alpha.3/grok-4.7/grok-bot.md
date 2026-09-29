## Intelligence Scale type

I'll follow the evaluation skill and rate only the product in the spec.

The skill and spec are large, so I’ll read them in sections and follow the skill exactly.

I’ll finish the skill rubric and the rest of the Grok Bot brief before scoring.

The brief is in. I’ll check the cited docs and how prior evaluations were written so the grades stay conservative.

I’ll check how scores are parsed so the final JSON matches the expected schema.

**Intelligence Scale capability: 1.9 / 3.0**

Approaching Type II. Evaluated 2026-09-29 from the Grok Bot brief and its docs. Strongest supported configuration: Cursor Enterprise with Grok Bot on, routines, Marketplace connectors, Auto Review, and Action Recording. This is the Grok Bot chassis, not grok.com or Grok Build.

Grok Bot natively embeds named Bots in everyday work. A Bot runs multi-step tasks on a persistent cloud computer, uses connectors and computer use, and can repeat that work from a schedule or a Slack or GitHub event while the laptop is closed. People still set the mandate, remain the account principal, and finish the documented outcomes: review lists and email or Slack drafts they must send. That is assisted, repeatable execution, not full process ownership.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| I.1 | 1.00 | Desktop, mobile, and team clients for named Bots doing research, operations, documents, and automations, included on paid Cursor plans. | https://docs.x.ai/grok-bot/overview |
| I.2 | 1.00 | Connectors, browser, files, terminal, attachments, per-Bot memory, and optional local execution and Cloud Agent delegation. | https://docs.x.ai/grok-bot/computer-and-apps |
| I.3 | 1.00 | A Bot takes multi-step work across apps and websites; background turns continue with the app closed. | https://docs.x.ai/grok-bot/overview |
| I.4 | 1.00 | People message, redirect, stop, approve or deny, take over the computer, and review transcripts and drafts. | https://docs.x.ai/grok-bot/approvals-security-and-privacy |
| I.5 | 1.00 | Skills, routines, memory, shared templates, SSO, SCIM, and team rules support repeatable org use. | https://docs.x.ai/grok-bot/skills-routines-and-automations |
| II.1 | 0.75 | A named Bot can own routines across runs, including Slack or GitHub events, but documented roles stop at a review list, and email or Slack sends are cards a person must send. | https://docs.x.ai/grok-bot/use-cases |
| II.2 | 1.00 | Once a routine starts, the Bot moves through steps, tools, and failure reporting in the background. Approvals are the org's choice or limited to exceptions such as login, CAPTCHA, and payment. | https://docs.x.ai/grok-bot/skills-routines-and-automations |
| II.3 | 1.00 | During a run the Bot selects granted connectors, browser, shell, files, and Cloud Agent delegation. Binding those tools at setup does not lower this grade. | https://docs.x.ai/grok-bot/computer-and-apps |
| II.4 | 0.75 | A durable Bot has a job, memory, routines, and a persistent computer, but no principal of its own. It acts only as the member; the computer and logins are shared by every Bot on the account. | https://docs.x.ai/grok-bot/security |
| II.5 | 1.00 | On Enterprise, people can watch the computer, get approval and exception prompts, stop a run, and audit via Action Recording, OpenTelemetry, and control-plane audit logs. | https://docs.x.ai/grok-bot/security |
| II.6 | 1.00 | Schedules and Slack or GitHub event triggers start runs with no person starting each one. Work continues in the cloud when the app is closed. | https://docs.x.ai/grok-bot/skills-routines-and-automations |
| III.1 | 0.25 | Recurring work is a member's designed routines, not organization-wide operations that proceed without that person. | https://docs.x.ai/grok-bot/teams-and-enterprises |
| III.2 | 0.25 | Bots can pick a respondent in a group or hand off a task. They do not determine the organization's next work. | https://docs.x.ai/grok-bot/chat-and-collaboration |
| III.3 | 0.75 | Bots message each other asynchronously, share a group, and can delegate coding to Cloud Agents. Coordination is limited to one member's bounded roster. | https://docs.x.ai/grok-bot/chat-and-collaboration |
| III.4 | 0.50 | Memory keeps summaries of prior work for later runs. Outcome evaluation does not itself change later operating decisions. | https://docs.x.ai/grok-bot/overview |
| III.5 | 0.25 | Branches live in human-authored skills. There is no native rewrite of processes or reallocation of standing work. | https://docs.x.ai/grok-bot/skills-routines-and-automations |
| III.6 | 0.25 | Enterprise policy, network, and audit controls exist, but routine review and the member principal remain structurally required. | https://docs.x.ai/grok-bot/teams-and-enterprises |

* **Completed floor:** 1
* **Next Type raw progress:** 0.92
* **Weakest criterion:** 0.75
* **Weakest-link penalty:** 0.06
* **Adjusted progress:** 0.86
* **Final score:** **1.9**

Mean of II.1–II.6 is 5.50/6 = 0.9167. Penalty is 0.25 × (1 − 0.75) × 0.9167 = 0.0573. Adjusted progress is 0.8594. That rounds to 1.9 and stays below 2.0 because Type II is incomplete.

### What prevents the next Type?

Two gaps block 2.0. **II.1:** a Bot does not own each case from a channel or queue through to a closed outcome. Routines are person-defined workflows whose documented finish is a draft or review list, and email or Slack sends require the person to send. **II.4:** a Bot has no principal, permissions, or credentials of its own; it acts only as the signed-in member on a shared computer.

## Execution coverage

I'll follow the evaluation skill and rate only the product in the spec.

The spec is large, so I’ll read it in sections and use only that brief.

I’ll open the cited docs that decide span, sharing, reach, catalog, and ready-made jobs.

I’ll check the plans page and how this repo treats multi-device chat when scoring surfaces.

**Execution coverage: 0.49 / 1.00**

Grok Bot, evaluated 2026-09-29, is xAI’s named-teammate product on paid Cursor plans (strongest supported config: Enterprise). People in sales, talent, finance, marketing, product, support, and operations can put their own jobs on a persistent cloud computer. Work stays in one person’s chat client. Others get a template copy or a finish notification, not the same run.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| E.1 | 1.00 | Shipped guidance covers sales outbound, talent, paid media, expenses, product performance, bug reproduction, account health, and chief of staff. Any other job is created by describing it; the surface is not one craft or one vendor suite. | https://docs.x.ai/grok-bot/use-cases ; https://docs.x.ai/grok-bot/overview |
| E.2 | 0.25 | Each person has a dedicated computer another user cannot reach. Group chats are that person’s Bots. Share copies a template link. Alerts are device notifications that a Bot finished or needs input. | https://docs.x.ai/grok-bot/teams-and-enterprises ; https://docs.x.ai/grok-bot/bots ; https://docs.x.ai/grok-bot/settings-and-notifications |
| E.3 | 0.75 | A persistent computer operates signed-in company apps; Marketplace connectors add structured access; email and Slack drafts can be sent. Documented starter jobs stop at review and do not ship read/write jobs for named systems of record. | https://docs.x.ai/grok-bot/computer-and-apps ; https://docs.x.ai/grok-bot/chat-and-collaboration ; https://docs.x.ai/grok-bot/use-cases |
| E.4 | 0.75 | Marketplace installs supported connectors and packaged skills across jobs. Third-party or customer publishing into that catalog is not documented. Bot sharing is a link; private skills stay in one person’s library. | https://docs.x.ai/grok-bot/skills-routines-and-automations ; https://docs.x.ai/grok-bot/computer-and-apps ; https://docs.x.ai/grok-bot/bots |
| E.5 | 0.25 | Desktop and mobile are thin clients for the same chat, review, and approvals. Slack and GitHub events only start routines. No workplace-chat, mail, customer-channel, or work API surface is documented. | https://docs.x.ai/grok-bot/teams-and-enterprises ; https://docs.x.ai/grok-bot/skills-routines-and-automations ; https://docs.x.ai/grok-bot/overview |
| E.6 | 1.00 | Install, Cursor sign-in, first-run onboarding, and a usage-credit trial are documented. Teams includes every member. Enterprise adds enablement, group access, SSO/SCIM, and permissions. | https://docs.x.ai/grok-bot/get-started ; https://cursor.com/help/grok-bot/plans ; https://docs.x.ai/grok-bot/teams-and-enterprises |
| E.7 | 0.75 | Several functions have starter prompts, suggested teammates, and a describe-the-job path that can save a skill and create a routine. The person still connects tools, sets boundaries, and defines triggers; examples stop at drafts. | https://docs.x.ai/grok-bot/use-cases ; https://docs.x.ai/grok-bot/get-started ; https://docs.x.ai/grok-bot/skills-routines-and-automations |

* **Raw mean:** 0.68
* **Weakest criterion:** 0.25
* **Weakest-link penalty:** 0.19
* **Uncapped score:** 0.49
* **Span cap:** none
* **Final score:** **0.49**

### What most limits coverage?

E.2 and E.5. There is no shared run or workspace for several people and the operator, only a template link and a finish notification. The work itself happens only in the Grok Bot chat client, not where company work already lives.
