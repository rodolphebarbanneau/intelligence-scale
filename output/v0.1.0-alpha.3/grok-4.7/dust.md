## Intelligence Scale type

I'll follow the evaluation skill and rate only the product in the spec.

The skill and spec are large, so I’ll read them in sections and follow the skill exactly.

I'll check how prior evaluations are written, then verify the Dust claims that decide Type II.

The triggers section was cut off. I’ll read that gap and the scale definition before scoring Type II.

I’ll open the cited docs that decide process ownership, actor durability, and how runs start.

**Intelligence Scale capability: 1.7 / 3.0**

Approaching Type II.

Evaluated 2026-09-29 from the Dust brief (reviewed 2026-09-28) and the docs it cites. Strongest supported configuration: Enterprise workspace (audit logs, pooled credits, unlimited connectors) with published agents, skills, spaces, pods, shared-credential tools, schedules, and webhooks. The chassis is the Dust workspace, not the model behind an agent.

Dust can natively run Type I: people work in Dust, Slack, Teams, or email, and agents assist with company data and tools. It does not natively delegate a business process. Schedules, webhooks, and channel auto-reply start agent runs. Each run is still a dispatched task. No persistent actor owns a case from queue to outcome, under its own principal, across runs. Humans still define, dispatch, and often finish the work.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| I.1 | 1.00 | Agents are the normal workspace surface: web app, Slack, Teams, email, browser extension, CLI, Sheets, Zendesk. Unmentioned messages route to the default agent. | https://docs.dust.tt/docs/user-documentation/getting-started/intro-to-dust |
| I.2 | 1.00 | First-party connections (Drive, Notion, Slack, Salesforce, warehouses, and others), spaces, search/SQL/extract, web browse, Computer, and managed tools. Not only buyer-wired MCP. | https://docs.dust.tt/docs/user-documentation/data-sources/connections |
| I.3 | 1.00 | A run selects tools, shows actions live, and can run code and files. `@deep-dive` plans, spawns up to six sub-agents, and returns a cited report. | https://docs.dust.tt/docs/user-documentation/agents/default-agents/deep-dive-agent |
| I.4 | 1.00 | People start work, inspect actions, queue follow-ups, stop a run, branch, and edit agents. Email writes and wake-ups require confirmation. | https://docs.dust.tt/docs/user-documentation/agents/steering-conversations |
| I.5 | 1.00 | Published agents, versioned skills, spaces, pods, SSO/SCIM, and saved triggers are repeatable org configuration, not a demo. | https://docs.dust.tt/docs/user-documentation/agents/skills/skills-overview |
| II.1 | 0.50 | Schedules, filtered webhooks, Slack auto-reply, and email start agent runs. Excess webhooks are dropped, not queued. Pod tasks are items a person or agent starts an agent on. Judgment: a trigger engine and assembly kit, not an actor that owns each case to an outcome. | https://docs.dust.tt/docs/user-documentation/agents/triggers/schedules |
| II.2 | 1.00 | Once a run starts, the agent moves through tool calls, branches, and sub-agents without a person between steps. Email write approval and wake-up confirmation are channel-specific, not the run model. | https://docs.dust.tt/docs/user-documentation/agents/steering-conversations |
| II.3 | 1.00 | During a run the agent selects granted knowledge, Computer, other agents, and write tools (Notion, Slack, GitHub, Confluence). Some tools only draft (Gmail); that is not the write model. | https://docs.dust.tt/docs/user-documentation/agents/tools/index |
| II.4 | 0.50 | An agent is a saved handle with threads, per-user memory, and space scope. It acts with the user’s auth or a shared connector. Computer is temporary. No own principal, credentials, or durable environment. | https://docs.dust.tt/docs/user-documentation/admins/tools-management/personal-vs-shared-credentials |
| II.5 | 0.75 | Live traces, stop, some confirmations, automations review, and Enterprise audit exist. Dropped webhooks and missed runs are not delivered as exceptions a supervisor handles. | https://docs.dust.tt/docs/user-documentation/admins/audit-logs/audit-logs |
| II.6 | 1.00 | Schedules and webhooks start background runs with no person starting each one. Slack auto-reply and inbound email are additional event channels. | https://docs.dust.tt/docs/user-documentation/agents/triggers/webhooks/rate-limiting |
| III.1 | 0.50 | Unattended runs exist only where people attach triggers or auto-reply. Routine org work is not structurally free of human participation. | https://docs.dust.tt/docs/user-documentation/agents/integrations/dust-in-slack/slack-auto-reply |
| III.2 | 0.25 | Sub-agents and pod tasks run inside a started run or a designed pod. The product does not decide what operational work happens next. | https://docs.dust.tt/docs/user-documentation/pods/tasks |
| III.3 | 0.25 | Run-agent and `@deep-dive` sub-agents coordinate inside one run (depth cap 4). Independent agents do not collaborate on their own. | https://docs.dust.tt/docs/user-documentation/agents/tools/run-agent |
| III.4 | 0.50 | Triggers detect and execute; analytics observe; Agent Memory can carry notes forward. Outcome evaluation does not change the next operational decision unless people arrange it. Skill edits wait for an editor. | https://docs.dust.tt/docs/user-documentation/agents/tools/agent-memory |
| III.5 | 0.25 | Tool choice and in-run replanning follow a human-written agent. Self-improving skills only propose edits. No native change to how work is organized. | https://docs.dust.tt/docs/user-documentation/agents/self-improving-skills |
| III.6 | 0.50 | Roles, spaces, spend caps, SSO/SCIM, and audit are real governance controls. They do not support an operating model where routine human intervention is exceptional. | https://docs.dust.tt/docs/user-documentation/admins/admin-governance/workspace-governance-roles-groups-and-permissions |

- **Completed floor:** 1
- **Next Type raw progress:** 0.79
- **Weakest criterion:** 0.50 (II.1 and II.4)
- **Weakest-link penalty:** 0.10
- **Adjusted progress:** 0.69
- **Final score:** **1.7**

### What prevents the next Type?

Type II is blocked because II.1, II.4, and II.5 are below 1.00. Dust still lacks a first-class actor that owns a process and takes each case from a trigger, channel, or queue to an outcome across runs (II.1); that actor’s own principal, credentials, cross-run work memory, and durable execution state (II.4); and a supervision path that receives failed, dropped, or blocked cases as exceptions (II.5).

## Execution coverage

I'll follow the evaluation skill and rate only the product in `specs/dust.md`.

The skill and brief are in place. I'll read the Dust spec in sections and score only that product.

Key claims need primary sources. I'll open the cited docs that decide span, sharing, reach, catalog, and ready-made jobs.

**Execution coverage: 0.83 / 1.00**

Dust is the hosted workspace (dust.tt / eu.dust.tt), rated on 2026-09-29 at the strongest supported configuration: self-serve Business plus documented Enterprise controls. Teams run agents on company knowledge from the web app, Slack, Teams, email, Zendesk, and the API. Coverage stops short of turnkey write-back jobs and a third-party job marketplace.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| E.1 | 1.00 | Company workspace, not one craft or suite. Members use `@dust` on Company Data or published agents. Docs describe work across domains for anyone in the company; a sales guide is linked from the intro, and a Zendesk app is a native support path. | https://docs.dust.tt/docs/user-documentation/getting-started/intro-to-dust ; https://docs.dust.tt/docs/developer-platform/overview/developer-platform |
| E.2 | 1.00 | Share lets colleagues join a conversation and work with the same agents. Pods are a shared workspace: members see conversations; humans or agents create, assign, and complete tasks. Slack/Teams threads are the work, not a status ping. | https://docs.dust.tt/docs/user-documentation/getting-started/faq/managing-agents/can-i-share-a-conversation ; https://docs.dust.tt/docs/user-documentation/pods/overview ; https://docs.dust.tt/docs/user-documentation/pods/tasks |
| E.3 | 0.75 | Read sync into several systems (Drive, Notion, Slack, Confluence, GitHub, Zendesk, Salesforce, warehouses). Documented writes include Notion pages, Slack posts, GitHub issues/PRs, and Confluence updates. Mail is search and drafts; Zendesk includes draft replies. Knowledge discovery does not write. | https://docs.dust.tt/docs/user-documentation/data-sources/connections ; https://docs.dust.tt/docs/user-documentation/agents/tools/index ; https://docs.dust.tt/docs/user-documentation/agents/discover-knowledge |
| E.4 | 0.75 | First-party tool directory, template gallery, and workspace skills. Admins install tools; members with permission publish skills and agents inside the workspace. No marketplace where third parties publish installable agents or workflows. Remote MCP is buyer-wired. | https://docs.dust.tt/docs/user-documentation/agents/templates ; https://docs.dust.tt/docs/user-documentation/agents/skills/skills-overview ; https://docs.dust.tt/docs/user-documentation/admins/tools-management/adding-an-mcp-server |
| E.5 | 1.00 | Web app, Slack, Teams, member email (`agent-name@dust.team`), Zendesk app, browser extension, CLI, and a documented Conversation API. Email is opt-in and reply-only; that does not remove the other native surfaces. | https://docs.dust.tt/docs/user-documentation/agents/create-your-first-agent ; https://docs.dust.tt/docs/user-documentation/agents/integrations/dust-in-teams ; https://docs.dust.tt/docs/user-documentation/agents/integrations/send-and-forward-email-to-agents ; https://docs.dust.tt/docs/user-documentation/agents/integrations/dust-in-zendesk ; https://docs.dust.tt/docs/developer-platform/overview/developer-platform |
| E.6 | 1.00 | Business starts free, no card, up to 5 users, with self-serve Pro/Max. Documented Admin, Manager, and Member roles, groups, spaces, and billing. Enterprise adds SCIM and audit logs via sales; ordinary teams can still put work on Business today. | https://dust.tt/home/pricing ; https://docs.dust.tt/docs/user-documentation/admins/admin-governance/workspace-governance-roles-groups-and-permissions ; https://docs.dust.tt/docs/user-documentation/admins/quickstart |
| E.7 | 0.75 | `@dust`, `@deep-dive`, `@help`, and `@analyst` ship as general agents, not function jobs. Templates open a Sidekick flow; Sidekick drafts instructions and recommends tools for a person to accept. It cannot set triggers or attach data connections. | https://docs.dust.tt/docs/user-documentation/agents/templates ; https://docs.dust.tt/docs/user-documentation/agents/default-agents/agent-builder-sidekick ; https://docs.dust.tt/docs/user-documentation/agents/default-agents/dust |

* **Raw mean:** 0.89
* **Weakest criterion:** 0.75
* **Weakest-link penalty:** 0.06
* **Uncapped score:** 0.83
* **Span cap:** none
* **Final score:** **0.83**

### What most limits coverage?

E.3, E.4, and E.7. Connections are read-heavy, and mail and ticket writes stop at drafts rather than shipped read/write jobs. The catalog is first-party tools, templates, and in-workspace skills, not a marketplace third parties publish into. Sidekick does not turn a description into a finished triggered job; someone still binds sources and sets triggers by hand.
