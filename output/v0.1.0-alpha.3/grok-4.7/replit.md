## Intelligence Scale type

I'll follow the evaluation skill and rate only the product in the Replit spec.

The skill and spec are large, so I’ll read them in sections and follow the skill exactly.

The skill is clear. Next I’ll read the Replit brief and score only that product.

The middle of the spec was truncated. I’ll read the connector, MCP, and project sections next.

I’ll verify the docs that decide Type II: routines, task ownership, and whether Agent has its own principal.

**Intelligence Scale capability: 1.7 / 3.0**

Approaching Type II. Evaluated 2026-09-29 from the Replit Agent brief and cited docs. Strongest supported configuration: Enterprise, which includes Pro Agent execution.

People still own the work. They describe an outcome, and Agent plans, builds, tests, and can publish that task, using connectors and tools without a person placing each call. Routines repeat scheduled chat work and return a result to continue. There is no persistent actor that takes each case from a queue and carries it to an outcome, and no worker with its own principal or credentials.

| Criterion | Grade | Evidence | Source |
| --- | ---: | --- | --- |
| I.1 | 1.00 | Agent is the normal way to build and change work in the Project Editor, Chat, desktop, and mobile apps. | https://docs.replit.com/features/agent/overview |
| I.2 | 1.00 | Agent uses project files, `replit.md`, opt-in Memories, web search, uploads, and first-party connectors. | https://docs.replit.com/features/integrations/overview |
| I.3 | 1.00 | A prompt becomes a plan Agent implements, tests in a browser for supported web apps, and fixes, including in the background. | https://docs.replit.com/features/agent/plan-mode |
| I.4 | 1.00 | People revise or cancel plans, steer or stop a turn, review and apply or dismiss tasks, and roll back checkpoints. | https://docs.replit.com/features/agent/plan-mode |
| I.5 | 1.00 | Team and Enterprise workspaces, skills, custom instructions, and Routines support repeated use, not a one-off demo. | https://docs.replit.com/features/collaboration/workspaces |
| II.1 | 0.50 | Routines are a schedule engine for chat work that returns a result for a person to continue. Builds and follow-ups are tasks a person starts. No actor owns cases from a queue. | https://docs.replit.com/chat/routines |
| II.2 | 1.00 | After a run starts, Agent implements, tests, and fixes with no person between steps. Plan approval and apply can be set to automatic. | https://docs.replit.com/features/agent/plan-mode |
| II.3 | 1.00 | During a run, Agent uses granted connectors, search, code, and generation. Routines can read tools, create tasks, and send messages without a person placing each call. | https://docs.replit.com/chat/routines |
| II.4 | 0.50 | Threads, project state, Memories, and Routine schedules persist. The actor has no principal of its own and inherits the person's permissions and connectors. | https://docs.replit.com/chat/memories |
| II.5 | 1.00 | People observe the task board, get help notifications, approve or take over exceptions, stop work, and on Enterprise audit Agent activity. | https://docs.replit.com/teams/identity-and-access-management/audit-logs |
| II.6 | 0.75 | Routines start hourly, daily, or weekly with no person starting each run, and continue in the background. No native event or webhook trigger is documented. | https://docs.replit.com/chat/routines |

* **Completed floor:** 1
* **Next Type raw progress:** 0.79
* **Weakest criterion:** 0.50
* **Weakest-link penalty:** 0.10
* **Adjusted progress:** 0.69
* **Final score:** **1.7**

### What prevents the next Type?

Type II is incomplete. II.1: no persistent actor owns a process and takes each case from a channel or queue to an outcome across runs. II.4: no durable actor with its own principal, permissions, and credentials. II.6: schedules only, with no native event or webhook trigger.

## Execution coverage

I'll follow the evaluation skill and rate only the product in the spec.

The skill file is large, so I’ll read it in sections and open the Replit spec.

The spec is longer than the first page. I’ll finish it and the rest of the scoring rules.

The spec cuts off on warehouse connectors and collaboration. I’ll read that section and check the cited docs that decide span, sharing, and reach.

I’ll verify the load-bearing claims in the cited docs: span, collaboration, connectors, skills, and surfaces.

**Execution coverage: 0.87 / 1.00**

Replit Agent is the hosted builder and chat on Replit, rated on 2026-09-29 in its strongest supported configuration (Enterprise, including Core and Pro capabilities). People can describe apps, designs, slides, documents, research, and recurring routines without writing code, and teams can share projects. Coverage stops short of a shared operator thread and of shipped jobs that already read and write company systems of record.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| E.1 | 1.00 | Documented outcomes include apps, designs, slides, video, documents, and spreadsheets, with no coding required. General Agent covers knowledge work, research, and files without building an app. The skills directory spans sales, finance, research, documents, and productivity. Judgment: more than one function, not one suite or preview-only. | https://docs.replit.com/features/agent/overview ; https://docs.replit.com/features/agent/general-agent ; https://docs.replit.com/features/agent/skills-directory |
| E.2 | 0.75 | Team Workspaces share projects, settings, and a Kanban. Invitees each start their own Agent threads on the same project. Chats and Routines stay private to the owner. Slack lets a channel refine a prototype with @Replit, but that thread is not the project work model. | https://docs.replit.com/features/collaboration/workspaces ; https://docs.replit.com/build/invite-teammates ; https://docs.replit.com/billing/plans/replit-core ; https://docs.replit.com/features/conversations-and-routines/conversations ; https://docs.replit.com/features/platforms/slack |
| E.3 | 0.75 | First-party connectors document chat read and write for Gmail, Calendar, Docs, Sheets, Slack, Linear, Jira, Zendesk, Notion, and others after one sign-in. That is a multi-system catalog with write-back, not named shipped jobs on those systems. | https://docs.replit.com/features/integrations/overview ; https://docs.replit.com/features/agent/general-agent |
| E.4 | 1.00 | The skills directory is a first-party, multi-function catalog. Replit and partners publish into it. Customer organizations create workspace skills, set member access, and import public GitHub skills. Community listings install from the documented skills.sh path. | https://docs.replit.com/features/agent/skills-directory ; https://docs.replit.com/features/agent/skills ; https://docs.replit.com/features/agent/agent-customization |
| E.5 | 1.00 | Work runs in the web product, desktop app, and mobile app, in Slack by mentioning @Replit, and through the documented Replit MCP server from ChatGPT, Claude, or any MCP client. | https://docs.replit.com/features/platforms/desktop-app ; https://docs.replit.com/features/platforms/slack ; https://docs.replit.com/platforms/mcp-server |
| E.6 | 1.00 | Starter can start immediately. Core is a self-serve join with seats, workspace invites, and permissions. Enterprise adds in-product upgrade, SSO, SCIM, groups, and admin controls. A team does not have to assemble the core. | https://docs.replit.com/billing/plans/replit-core ; https://docs.replit.com/billing/plans/replit-enterprise ; https://docs.replit.com/teams/welcome |
| E.7 | 1.00 | Several functions have a non-specialist path: attach a pre-defined skill, or describe an outcome and approve Plan Mode or a Routine. Examples include sales, finance, research, documents, and recurring mail, calendar, and Slack work. Connecting systems is not counted again here. | https://docs.replit.com/features/agent/skills-directory ; https://docs.replit.com/features/agent/plan-mode ; https://docs.replit.com/chat/routines |

* **Raw mean:** 0.93 (6.50 / 7 = 0.9286)
* **Weakest criterion:** 0.75
* **Weakest-link penalty:** 0.06 (0.25 × 0.25 = 0.0625)
* **Uncapped score:** 0.87 (0.8661, half-up off an exact half)
* **Span cap:** none
* **Final score:** **0.87**

### What most limits coverage?

Shared work and system reach, both 0.75. Collaborators share a workspace and Kanban, but Agent chats and Routines are single-owner, and the operator is not in one project thread. Connectors can read and write mail, calendar, files, tickets, and chat after sign-in, yet Replit does not ship named jobs that already run those systems of record.
