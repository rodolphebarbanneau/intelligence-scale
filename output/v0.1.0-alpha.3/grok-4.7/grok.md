## Intelligence Scale type

I'll follow the evaluation skill and rate only the product in the spec.

The skill and spec are large, so I’ll read them in sections and follow the skill exactly.

The brief is the Grok assistant, not Grok Bot or Build. I’ll check the cited docs for process ownership, triggers, and persistent actors.

Previous ratings exist, but I’ll score from the spec and cited docs. Next I’ll confirm multi-agent, memory, projects, and any automation the assistant itself exposes.

The product page is mostly client-rendered. I’ll pull the cited pages for memory, multi-agent, projects, and write actions.

**Intelligence Scale capability: 1.4 / 3.0**

Type I with early Type II capabilities. Evaluated 2026-09-29. Strongest supported configuration of the Grok assistant (grok.com and the mobile apps, including Business and Enterprise). Grok Bot and Grok Build are separate products and are not scored.

People still execute. Grok assists in a synced chat: it searches, reads files, and can act in connected apps when asked. It does not own a process, keep its own worker, or start work on its own.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| I.1 | 1.00 | First-party chat on grok.com, iOS, and Android. Conversations, settings, and subscription sync. | https://docs.x.ai/grok/overview |
| I.2 | 1.00 | Uploads plus built-in connectors (Gmail, Calendar, Drive, Outlook, Teams, SharePoint, OneDrive, Salesforce) used automatically in chat. Web and X search. Custom MCP is extra and not required for this grade. | https://docs.x.ai/grok/connectors |
| I.3 | 1.00 | In one thread Grok searches, reads, drafts, creates files, sends mail or Teams messages, and creates or updates records without the person calling each tool. | https://docs.x.ai/grok/connectors/gmail-google-calendar |
| I.4 | 1.00 | The person starts and continues the thread, can review drafts before send, sees history, and can disconnect connectors or delete chats. | https://docs.x.ai/grok/connectors/gmail-google-calendar |
| I.5 | 1.00 | Persistent accounts, history, saved connector grants, team workspaces, licenses, SSO, and SCIM. Not a one-off demo. | https://docs.x.ai/grok/user-guide |
| II.1 | 0.25 | Each unit of work is a person-dispatched chat task: one reply, file, or record. No actor takes cases from a queue across runs. | https://docs.x.ai/grok/overview |
| II.2 | 0.50 | One request can chain tools on its own. The next task in a process still needs a person. | https://docs.x.ai/grok/connectors |
| II.3 | 1.00 | During that request Grok selects granted search, file, mail, calendar, Drive, Teams, and CRM tools. Setup grants do not lower this grade. | https://docs.x.ai/grok/connectors |
| II.4 | 0.50 | Threads, memory, and the user's OAuth grants persist. No AI principal, own credentials, or durable environment. Connector access is the signed-in user's. | https://docs.x.ai/grok/connectors/microsoft-teams |
| II.5 | 0.50 | Review is the transcript, visible reasoning, and optional drafts. No run approvals, exception queue, intervention, or process audit. | https://x.ai/grok |
| II.6 | 0.25 | A person starts every chat. No schedules, webhooks, queues, or background continuation in this product. | https://docs.x.ai/grok/faq |
| III.1 | 0.00 | Routine work does not proceed unless a person opens a chat. | https://docs.x.ai/grok/overview |
| III.2 | 0.00 | Grok does not decide what operational work is next or allocate it. | https://docs.x.ai/grok/overview |
| III.3 | 0.25 | Product page: multi-agent mode runs parallel sub-problem agents and merges one answer inside one human-started thread. Not persistent actors coordinating. | https://x.ai/grok |
| III.4 | 0.00 | No detect-decide-execute-observe loop that changes later operations. | https://docs.x.ai/grok/overview |
| III.5 | 0.00 | No native ability to change how work is organized. | https://docs.x.ai/grok/overview |
| III.6 | 0.00 | SSO, SCIM, and sharing govern chat access. They do not support a governance-only operating model. | https://docs.x.ai/grok/organization |

* **Completed floor:** 1
* **Next Type raw progress:** 0.50
* **Weakest criterion:** 0.25 (II.1 and II.6)
* **Weakest-link penalty:** 0.09
* **Adjusted progress:** 0.41
* **Final score:** **1.4**

### What prevents the next Type?

Type II needs every II criterion at 1.00. Missing native capabilities:

* **II.1** — no persistent actor that owns a process and takes each case to an outcome across runs.
* **II.2** — no process run that moves through steps, branches, and retries without a person between tasks.
* **II.4** — no durable AI worker with its own principal, credentials, and execution environment.
* **II.5** — no supervision of runs (approve exceptions, intervene, audit) beyond the chat transcript.
* **II.6** — no schedule or event trigger that starts work without a person opening a chat.

## Execution coverage

I'll follow the evaluation skill and rate only the product in the spec.

The spec is large, so I’ll read it in sections and use only that brief.

I’ll check how the rubric treats connectors versus shipped jobs, then verify the cited Grok docs.

I’ll open the cited docs for connectors, sharing, and the product surface before scoring.

**Execution coverage: 0.46 / 1.00**

Grok, the assistant on grok.com and the iOS and Android apps (Business and Enterprise as the strongest supported team setup; not Grok Bot, Grok Build, the developer API, or Grok on X), evaluated 2026-09-29. People across functions can put writing, research, files, mail, calendar, and CRM questions on the chat. Work stays in that chat. Teams can share a transcript afterward. There are no ready-made jobs.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| E.1 | 1.00 | General assistant for questions, writing, and problem-solving, plus first-party reach into mail, files, calendar, Teams, and Salesforce. More than one function; not one suite or craft. | https://docs.x.ai/grok/overview ; https://docs.x.ai/grok/connectors |
| E.2 | 0.50 | Business team workspace, licenses, and share links that licensed members open under Shared with me. Sharing policy covers conversations, projects, and skills. No documented live thread with several people and an operator. | https://docs.x.ai/grok/user-guide ; https://docs.x.ai/grok/management |
| E.3 | 0.75 | Named read and write on Outlook mail and calendar, Teams, and Drive; Gmail and Calendar write start off until admins enable them; SharePoint write is off by default; Salesforce create/update depends on a beta MCP server setup. Catalog sign-in, not shipped jobs. | https://docs.x.ai/grok/connectors/outlook ; https://docs.x.ai/grok/connectors/gmail-google-calendar ; https://docs.x.ai/grok/connectors/salesforce |
| E.4 | 0.75 | First-party connector directory (built-ins plus a catalog at grok.com/connectors) across vendors, not one craft. Mostly connectors. Custom MCP is buyer-wired. No documented third-party publishing of agents or workflows. | https://docs.x.ai/grok/connectors ; https://docs.x.ai/grok/connector-management |
| E.5 | 0.25 | Work happens in the Grok chat on the web and in the iOS and Android apps, which sync. No workplace-chat, mail, or embed surface for this product. The developer API and Grok on X are out of scope. | https://docs.x.ai/grok/overview |
| E.6 | 1.00 | Free start. Business console documents license purchase, email invite, seat assignment, role permissions, sharing policy, and connector provisioning so a team can put work on it without assembling a platform. | https://docs.x.ai/grok/management ; https://docs.x.ai/grok/user-guide ; https://docs.x.ai/grok/overview |
| E.7 | 0.25 | A general assistant. No shipped jobs, installable finished agents, or a builder that emits instructions, tools, and triggers for review. Connectors are not finished jobs. Skills are only a sharing-policy object. | https://docs.x.ai/grok/overview ; https://docs.x.ai/grok/management |

* **Raw mean:** 0.64
* **Weakest criterion:** 0.25
* **Weakest-link penalty:** 0.19
* **Uncapped score:** 0.46
* **Span cap:** none
* **Final score:** **0.46**

### What most limits coverage?

E.5 and E.7 are 0.25. Company work has no native place outside Grok’s own chat, and a team cannot turn on, install, or approve a generated job for another function. They still design every task in the thread. E.2 stays at transcript sharing, not a shared run.
