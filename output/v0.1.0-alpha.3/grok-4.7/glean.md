## Intelligence Scale type

I'll follow the evaluation skill and rate only the product in the spec.

The skill and spec are large, so I’ll read them in sections and follow the skill exactly.

The skill is loaded. Next I’ll read the Glean brief and score only that product.

I’ll check prior evaluations for format and open the cited agent docs that decide the Type II grades.

Independent agents look like the Type II hinge. I’ll verify identity, triggers, memory, and supervision in the cited docs.

I’ll check how evaluations are validated so the score and JSON match the skill.

**Intelligence Scale capability: 1.8 / 3.0**

Approaching Type II.

Evaluated 2026-09-29 from the Glean spec (reviewed 2026-09-28) and the docs it cites. Strongest supported configuration: Enterprise Assistant and Agents, connectors, scheduled and content triggers, and agent identity. Independent Agents are beta and cannot score above 0.75.

Glean can run a Type I workplace. People search and chat against permission-aware company knowledge, and agents finish bounded multi-step tasks. Designed workflows can also run in the background from schedules and content events, use granted tools, and be supervised through run history, write approval, and audit. That is not yet Type II. There is no generally available operator that owns a business process across cases and keeps memory and execution state between runs.

| Criterion | Grade | Evidence | Source |
| --- | ---: | --- | --- |
| I.1 | 1.00 | Chat, Search, desktop quick entry, mobile, browser sidebar, and Slack, Teams, Zoom, GitHub, and Miro embeds are normal work surfaces, not an isolated API. | https://docs.glean.com/user-guide/assistant/glean-chat/ |
| I.2 | 1.00 | Connectors mirror source permissions. Chat and agents use company knowledge, web search, files, tools, code search, and data analysis. | https://docs.glean.com/connectors/about |
| I.3 | 1.00 | Thinking mode and Auto and Workflow agents plan and run multi-step tool use, including sub-tasks, research, and draft pull requests. | https://docs.glean.com/agents/how-agents-work |
| I.4 | 1.00 | People start work, follow citations, preview and debug agents, and approve or cancel writes. Sharing does not transfer permissions. | https://docs.glean.com/security/security-principles |
| I.5 | 1.00 | Agent Library, skills, templates, admin RBAC, and saved triggers support repeatable org use. | https://docs.glean.com/agents/concepts/agent-library |
| II.1 | 0.50 | Content and schedule triggers run a designed multi-step workflow per event or tick, under the activating user's subscription. Judgment: that is a trigger engine, not a persistent owner of each case through outcome. Independent Agents are beta, and the creation flow has no event or schedule setup and is Slack-presence only, so case ownership is not proven. | https://docs.glean.com/agents/concepts/content-trigger |
| II.2 | 1.00 | Once a run starts, Workflow steps, branches, loops, and Auto mode tool use proceed without a person between steps. Write confirmation is the default in the web app; admins can allow specific writes to run without it, including background runs. | https://docs.glean.com/security/agents/background-agents |
| II.3 | 1.00 | During a run the agent uses the tools it was granted across connectors. Auto mode selects tools. No person coordinates each call. Setup-time grants do not lower this grade. | https://docs.glean.com/administration/tools |
| II.4 | 0.75 | Agent identity gives a saved agent its own principal, scoped permissions, and server-side credentials. Independent Agents add a beta profile and Slack presence. Limit: agent memory is step output inside one run, and scheduled runs end at about 30 minutes. No cross-run memory or durable environment. | https://docs.glean.com/administration/agent-identity/overview |
| II.5 | 1.00 | People can view run history and traces, approve writes, get email when a background step needs confirmation, pause or unpublish, revoke credentials, and export audit and workflow-run logs. | https://docs.glean.com/security/agents/background-agents |
| II.6 | 1.00 | Schedules and content triggers start background runs without a person starting each one. Recommended sources include Jira, Salesforce, Gong, Gmail, Outlook, Calendar, and Slack. Authoring the rule does not lower this grade. | https://docs.glean.com/agents/concepts/schedule-triggers |
| III.1 | 0.50 | Event triggers and scheduled agents can repeat arranged workflows without a person on each run. Routine org operations are not structurally hands-off. | https://docs.glean.com/agents/concepts/content-trigger |
| III.2 | 0.25 | The Task tool splits one request into sub-tasks. AI does not decide what operational work the organization should do next. | https://docs.glean.com/agents/how-agents-work |
| III.3 | 0.25 | Sub-agents and A2A calls happen inside one Auto mode run. A2A is text-only and each user authorizes. Not persistent actor-to-actor coordination. | https://docs.glean.com/administration/platform/a2a-host |
| III.4 | 0.25 | Triggers detect and a run executes. Working memory ends with the run. Outcomes do not natively change the next operational decision. | https://docs.glean.com/agents/concepts/memory |
| III.5 | 0.25 | Auto mode can vary a path inside one run. It does not change how work is organized. Workflow branches are human-authored. | https://docs.glean.com/agents/auto-mode-agent |
| III.6 | 0.50 | Admin RBAC, Protect, usage limits, and credential scope are governance controls. They do not yet support a model where routine human intervention is exceptional. | https://docs.glean.com/administration/protect/overview |

- **Completed floor:** 1
- **Next Type raw progress:** 0.88
- **Weakest criterion:** 0.50
- **Weakest-link penalty:** 0.11
- **Adjusted progress:** 0.77
- **Final score:** **1.8**

Exact Type II mean is 5.25/6 = 0.875. Penalty is 0.25 × (1 − 0.50) × 0.875 = 0.109. Adjusted progress is 0.766. Floor 1 plus that progress is 1.766, which rounds to 1.8. Type II is incomplete, so the score stays below 2.0.

### What prevents the next Type?

II.1 and II.4. Glean needs a generally available actor that takes each case from a trigger, channel, or queue and carries it to an outcome across runs. Today each unit is a user-subscribed workflow run. It also needs that actor's own memory across runs and a durable execution environment. Service credentials and a beta Slack profile do not supply that state.

## Execution coverage

I'll follow the evaluation skill and rate only the product in `specs/glean.md`.

The spec is large, so I’ll read it in sections and use only that brief.

I’ll check the cited docs for span, shared work, reach, and ready-made jobs before scoring.

I’ll locate the cited tool and template pages so write-back and ready-made jobs are scored from the docs, not the connector list.

**Execution coverage: 0.79 / 1.00**

Glean, evaluated 2026-09-29, is the hosted enterprise Work AI product (strongest supported configuration: Enterprise Flex with Admin Console, connectors, Assistant, and Agents). Employees across support, sales, operations, product, engineering, and people teams can search, ask, draft, and run agents on company knowledge. Independent Agents are beta and are not treated as native multiplayer.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| E.1 | 1.00 | Anyone with a work account can put their own work on Chat, Search, and Agents. Documented users include support, sales, operations, product, engineering, and people teams. Templates span General, Engineering, HR, IT, Marketing, Sales, and Support. Not one suite or one craft. | https://docs.glean.com/user-guide/about/what-is-glean ; https://docs.glean.com/agents/templates |
| E.2 | 0.75 | Projects are a shared workspace with view or edit, but chats and artifacts stay private unless shared, and Projects are still rolling out. Chat share is permission-filtered viewing, not one shared run. Slack answers are private unless Public Mode is on. Independent Agents can sit in a shared Slack or Teams thread, but they are beta. | https://docs.glean.com/user-guide/knowledge/projects/how-projects-work ; https://docs.glean.com/security/security-principles ; https://docs.glean.com/agents/independent-agents ; https://docs.glean.com/administration/platform/embedded-integrations/slackbot |
| E.3 | 1.00 | Catalog connectors index source systems, and shipped tools read and write named systems of record: Jira search, create, edit, and comment; Zendesk public replies and internal notes; Google Docs, Sheets, Drive files, and Gmail drafts; Microsoft 365 Word, Excel, and OneDrive updates; GitHub draft pull requests; Slack read and post. Admin install and user sign-in, not a custom integration. | https://docs.glean.com/administration/tools ; https://docs.glean.com/administration/tools/setup-tools/zendesk-tools-setup ; https://docs.glean.com/tools/connector/google ; https://docs.glean.com/tools/connector/microsoft-365 ; https://docs.glean.com/administration/assistant/features/code-writer |
| E.4 | 0.75 | Agent Library, category templates, Glean-managed agents, and shared Skills are a real cross-function catalog. Customers and Glean can publish into the tenant. Third parties do not publish into that directory; GitHub Skill import needs an admin to enable third-party skills. | https://docs.glean.com/agents/concepts/agent-library ; https://docs.glean.com/agents/templates ; https://docs.glean.com/user-guide/assistant/skills |
| E.5 | 0.75 | Work runs in the web app, desktop, mobile, and browser extension, plus Slack, Teams, Zoom, Miro, and GitHub, and through the Web SDK, Client APIs, and MCP. Native Zendesk, ServiceNow, and Service Cloud embeds are retiring in favor of the extension. No mail-client surface. | https://docs.glean.com/user-guide/assistant/glean-chat/ ; https://docs.glean.com/glean-enterprise-flex-pricing ; https://docs.glean.com/administration/platform/embedded-integrations/glean-in-zendesk ; https://docs.glean.com/administration/platform/mcp/about |
| E.6 | 1.00 | Admin Console is the self-serve control plane for SSO, connectors, RBAC, and adoption, without a dedicated implementation project. Members, moderators, and admins are documented. End-user quick start is documented. | https://docs.glean.com/administration/about ; https://docs.glean.com/administration/identity/roles/about ; https://docs.glean.com/user-guide/about/end-user-quick-start-guide |
| E.7 | 0.75 | Turn-on templates exist for personal productivity and marketing, including jobs that need no input. Auto mode builds an agent from a plain-language description for a person to review. The draft still needs tools, resources, and triggers refined, and finished templates are not documented for every listed function. | https://docs.glean.com/agents/templates ; https://docs.glean.com/agents/auto-mode-agent |

* **Raw mean:** 0.86 (6.00 / 7 = 0.85714…)
* **Weakest criterion:** 0.75
* **Weakest-link penalty:** 0.06 (0.25 × 0.25 = 0.0625)
* **Uncapped score:** 0.79 (0.85714 − 0.0625 = 0.79464)
* **Span cap:** none
* **Final score:** **0.79**

### What most limits coverage?

E.2, E.4, E.5, and E.7 are tied at 0.75. People do not share one run with the operator and the same state; Independent Agents that can do that are beta. The catalog is an organization directory, not a marketplace third parties publish into. Native support embeds are retiring, and there is no mail surface. Ready-made jobs and Auto mode exist, but a person still has to finish tools and triggers, and turn-key templates are not documented across every function.
