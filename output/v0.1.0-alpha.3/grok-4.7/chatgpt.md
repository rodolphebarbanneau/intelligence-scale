## Intelligence Scale type

I'll follow the evaluation skill and rate only the product in the spec.

The skill and spec are large, so I’ll read them in sections and rate only ChatGPT.

I’ll finish the skill criteria and the rest of the ChatGPT spec before scoring.

Scope is the Chat assistant, not Work or Codex. I’ll check how other evaluations are written and which cited pages pin the agent boundary.

Work and Codex are out of scope. I’ll verify the cited pages that decide whether Chat itself owns a process.

I’ll open the cited docs that separate Chat from Work, especially tasks, apps, and agent mode.

**Intelligence Scale capability: 1.5 / 3.0**

Type I with early Type II capabilities. Evaluated 2026-09-29 from the ChatGPT Chat brief (reviewed 2026-09-28). Strongest in-scope configuration is a paid plan (Pro, Business, or Enterprise) with memory, plugins, connected apps, code execution, and scheduled tasks. Workspace Agents and Codex are out of scope.

People still execute. ChatGPT assists on web, desktop, and mobile with files, apps, and bounded multi-step work. Schedules and a few app events can start background runs, and ChatGPT can choose tools during a run. Nothing in this chassis is a worker that owns a business process.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| I.1 | 1.00 | Chat is the everyday assistant on web, desktop, iOS, and Android. A person opens it and works in natural language. | https://learn.chatgpt.com/docs/use-chatgpt.md |
| I.2 | 1.00 | Projects, Library, uploads, web search, memory, and first-party apps (Drive, Slack, GitHub, and others), plus plugins, supply work context and tools. | https://help.openai.com/en/articles/11487775-connected-apps-in-chatgpt |
| I.3 | 1.00 | Code execution analyzes data; a matching skill follows a workflow; web search synthesizes sources; a scheduled run continues without the person typing each step. | https://help.openai.com/en/articles/9260256-chatgpt-capabilities-overview |
| I.4 | 1.00 | People start, redirect, and revise chats, branch threads, set app approvals, edit memory, and use temporary chats. | https://learn.chatgpt.com/docs/use-chatgpt.md |
| I.5 | 1.00 | Projects, custom instructions, installed skills and plugins, memory, and Business or Enterprise admin controls make use persistent, not a demo. | https://help.openai.com/en/articles/10169521-projects-in-chatgpt |
| II.1 | 0.25 | A schedule or a Gmail, Slack, or GitHub event dispatches one saved prompt. No actor takes each case from a queue to an outcome across runs. | https://learn.chatgpt.com/docs/automations.md |
| II.2 | 0.50 | A started run can search, run code, and call tools with no person between those steps. The next task still needs a person or a new dispatch. | https://help.openai.com/en/articles/9260256-chatgpt-capabilities-overview |
| II.3 | 1.00 | During a run, ChatGPT can select installed plugins, skills, web search, code execution, and connected apps. Allow-all is available for eligible app actions. | https://learn.chatgpt.com/docs/plugins.md |
| II.4 | 0.50 | Chats, projects, memory, and named tasks persist, but they use the person’s identity, permissions, and app credentials. No worker principal. | https://help.openai.com/en/articles/8590148-memory-in-chatgpt |
| II.5 | 0.75 | Activity, permission notifications, app approvals, run history, and Enterprise audit exist. Structured escalation and a general stop control are not documented. | https://learn.chatgpt.com/docs/notifications.md |
| II.6 | 1.00 | Time schedules and Gmail, Slack, and GitHub events start background runs on web and mobile. A person does not start each run. | https://learn.chatgpt.com/docs/automations.md |

- **Completed floor:** 1
- **Next Type raw progress:** 0.67
- **Weakest criterion:** 0.25 (II.1)
- **Weakest-link penalty:** 0.13
- **Adjusted progress:** 0.54
- **Final score:** **1.5**

### What prevents the next Type?

Type II stays incomplete until II.1, II.2, II.4, and II.5 are native. There is no persistent actor that owns a process and carries each case to an outcome (II.1), so execution stays a multi-step task rather than unaided process progression (II.2). Memory and apps stay on the person’s principal, not a worker with its own permissions, credentials, and durable execution state (II.4). Supervision lacks a full exception and intervention loop (II.5).

## Execution coverage

I'll follow the evaluation skill and rate only the product in the spec.

The ChatGPT spec is large, so I’ll read it in sections and use only that brief.

I’ll check the cited docs that decide span, sharing, connectors, plugins, and surfaces.

Help Center pages blocked the fetch. I’ll use the cited ChatGPT docs that are still reachable.

**Execution coverage: 0.76 / 1.00**

ChatGPT here is the Chat assistant (chatgpt.com and the ChatGPT apps), not ChatGPT Work or Codex. Evaluated 2026-09-29 from the 2026-09-28 spec and cited docs, on the strongest supported Chat configuration (Business/Enterprise admin where it applies to Chat). People across a company can draft, search, study, and analyze files in Chat today. Shared projects, connectors, and plugins are real, but live multiplayer, named write-back, workplace surfaces, and turnkey jobs are not.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| E.1 | 1.00 | Chat is a general assistant for brainstorming, writing, studying, planning, math, coding, and file or image analysis. Chat covers questions, web search, drafts, and comparisons, not one craft or one suite. Judgment: Work-only deliverables do not narrow whose work fits. | https://help.openai.com/en/articles/12677804-what-is-chatgpt-faq ; https://learn.chatgpt.com/docs/use-chatgpt.md |
| E.2 | 0.75 | Shared projects give edit or chat access so invitees can see and use chats, files, and instructions. Business can invite people or groups. Chat links are read-only snapshots; members do not automatically see each other's chats. Judgment: shared workspace, not documented live multiplayer with the operator in one thread. | https://help.openai.com/en/articles/10169521-projects-in-chatgpt ; https://help.openai.com/en/articles/7925741-sharing-conversations-and-scheduled-tasks-in-chatgpt |
| E.3 | 0.75 | Plugins and apps reach Gmail, Drive, Docs, Sheets, Slides, Slack, GitHub, Outlook, SharePoint, Teams, Box, and Notion. Examples are summarize, pull files, and draft replies. Action permissions exist, but named write jobs are not documented. Slack and Gmail events start tasks; they are not write-back. | https://learn.chatgpt.com/docs/plugins.md ; https://help.openai.com/en/articles/11487775-connected-apps-in-chatgpt |
| E.4 | 0.75 | A Plugins directory has OpenAI, workspace, and Personal tabs, and plugins install in Chat. Workspace admins can import a GitHub marketplace; individuals can create plugins. Public examples are mostly connectors. Third-party listing is a review submission, not an open store. GPTs are retiring and personal creation is closed. | https://learn.chatgpt.com/docs/plugins.md ; https://help.openai.com/en/articles/8554407-gpts-in-chatgpt |
| E.5 | 0.75 | Native clients are web, desktop (macOS, Windows, Linux), and iOS/Android, plus voice on those clients. Email, SMS, and push are notifications. Slack `@ChatGPT` is a task trigger. The API platform is separate. No workplace chat, mail, or embed surface. | https://learn.chatgpt.com/docs/web.md ; https://learn.chatgpt.com/docs/app.md ; https://learn.chatgpt.com/docs/automations.md |
| E.6 | 1.00 | Free works at chatgpt.com, including without an account in supported regions. Business is self-serve (2+ seats) with admin controls, SAML SSO, and MFA. Enterprise adds SCIM, RBAC, domain verification, and audit logs. | https://learn.chatgpt.com/docs/pricing.md ; https://help.openai.com/en/articles/8792828-chatgpt-business-overview |
| E.7 | 0.75 | `@skill-creator` builds a skill from a description for review and install. Scheduled tasks are created by describing the work. Public GPTs can be used, but the spec does not list shipped jobs across functions, and plugins are mostly connectors. Judgment: generation still needs tools and triggers bound. | https://learn.chatgpt.com/docs/skills-and-plugins.md ; https://learn.chatgpt.com/docs/automations.md |

* **Raw mean:** 0.82 (5.75/7 = 0.8214)
* **Weakest criterion:** 0.75
* **Weakest-link penalty:** 0.06 (0.25 × 0.25 = 0.0625)
* **Uncapped score:** 0.76 (0.8214 − 0.0625 = 0.7589, half down)
* **Span cap:** none
* **Final score:** **0.76**

### What most limits coverage?

The 0.75 grades are the limit. Project sharing is not a documented live thread with the operator. Connectors do not document write-back into mail, tickets, or CRM as shipped jobs. The plugin directory is mostly connectors, not a clearly open third-party job store. Work stays in ChatGPT's own clients. A team still has to describe a skill and connect tools; there is no sourced set of turn-on jobs for several functions.
