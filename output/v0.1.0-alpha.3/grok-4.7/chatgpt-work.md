## Intelligence Scale type

I'll follow the evaluation skill and rate only the product in the spec.

The skill continues past Type II. I'll read the rest of the scoring rules and output format.

I'll verify the cited docs and check how prior evaluations are structured before scoring.

The API trigger and token docs check out. Help Center pages in the brief returned 403, so those claims stay tied to the spec’s cited sources.

**Intelligence Scale capability: 1.8 / 3.0**

Approaching Type II.

Evaluated 2026-09-29 for ChatGPT Workspace Agents on Business, Enterprise, and Edu, the strongest supported configuration with agents enabled. This rates the shared agent, channels, and workspace controls, not the model and not Codex. A published agent can be run from ChatGPT, Slack, a schedule, or an API trigger, with apps, skills, files, and memory. People still set the mandate, and each instance is a dispatched run that ends in a reply, a tool action, or a ChatGPT conversation. That completes Type I and covers much of a Type II chassis, without an operator that owns a process over time. Trigger and token docs were opened. Help Center URLs in the brief returned 403 and are used as cited there.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| I.1 | 1.00 | Agents sit in the ChatGPT sidebar and run from @mention, Slack, a schedule, or an API trigger inside normal workspace work. | https://help.openai.com/en/articles/20001143/ |
| I.2 | 1.00 | The builder attaches apps (Calendar, Drive, Slack, SharePoint), web search, image generation, skills, files, custom MCP, and memory, with end-user or agent-owned connections. | https://help.openai.com/en/articles/20001143/ |
| I.3 | 1.00 | A published agent follows instructions and skills and uses granted tools through a multi-step run, including Slack replies and scheduled jobs. | https://help.openai.com/en/articles/20001143/ |
| I.4 | 1.00 | People create, preview, edit, version, publish, direct with @mention or starter prompts, and approve write actions. Always ask is the default; some apps allow Never ask or Custom. | https://help.openai.com/en/articles/20001143/ |
| I.5 | 1.00 | Published agents persist, can be shared or listed in the directory, duplicated, scheduled, and deployed to Slack under workspace RBAC. | https://help.openai.com/en/articles/20001143/ |
| II.1 | 0.75 | A persistent agent can take Slack messages, schedules, and API events to an outcome across runs. Limit: each unit is still one dispatched run, not a case it owns through a queue or process record. The API returns a conversation URL, not the result. | https://developers.openai.com/workspace-agents/trigger-runs |
| II.2 | 1.00 | Once a run starts, the agent calls tools and can suspend for an external action without a person between steps. Write approval is the organization's choice where Never ask or Custom is available. | https://developers.openai.com/workspace-agents/trigger-runs |
| II.3 | 1.00 | During a run the agent selects the apps, web search, image generation, skills, and files it was granted. No person coordinates each call. Custom MCP is extra, not the basis of this grade. | https://help.openai.com/en/articles/20001143/ |
| II.4 | 0.75 | Durable Agent ID, Slack user-group handle, action permissions, optional agent-owned credentials, and per-user or per-channel memory. Limit: ChatGPT runs use the end-user connection; memory is not one agent-owned record across channels; no durable execution environment beyond files, memory, and run state. | https://cdn.openai.com/business-guides-and-resources/workspace-agents-security-overview.pdf |
| II.5 | 0.75 | Approvals, run analytics, admin activity review, version republish, unpublish or delete, and Enterprise compliance export. Limit: no escalation queue or documented in-run stop; run-status polling is beta. | https://cdn.openai.com/business-guides-and-resources/workspace-agents-security-overview.pdf |
| II.6 | 1.00 | Schedules, Slack message and mention events, and POST /trigger start runs with no person starting each one. The API returns 202 and queues the run. conversation_key continues a conversation across events. | https://developers.openai.com/workspace-agents/trigger-runs |
| III.1 | 0.50 | People arrange agents, schedules, and channels so specific routines run without a person in each step. Not organization-wide autonomous operations. | https://help.openai.com/en/articles/20001143/ |
| III.2 | 0.00 | The agent executes work already placed on a trigger, schedule, or channel. It does not determine what work should happen next or allocate it. | https://developers.openai.com/workspace-agents/trigger-runs |
| III.3 | 0.00 | Several agents can exist in one workspace. No documented agent-to-agent delegation. @mention is a human action. | https://help.openai.com/en/articles/20001143/ |
| III.4 | 0.50 | Triggers detect, the run decides and executes, analytics and compliance observe, and memory can carry context into the next run. Outcome evaluation does not change later orchestration. | https://cdn.openai.com/business-guides-and-resources/workspace-agents-security-overview.pdf |
| III.5 | 0.25 | The agent can vary steps inside human-authored instructions. Changing the process is a human publish. It does not reallocate work or create new operational paths. | https://help.openai.com/en/articles/20001143/ |
| III.6 | 0.50 | Enterprise RBAC, app and approval controls, compliance export, and admin unpublish support policy. No per-agent budget caps. Routine human intervention is not exceptional. | https://cdn.openai.com/business-guides-and-resources/workspace-agents-security-overview.pdf |

* **Completed floor:** 1
* **Next Type raw progress:** 0.875
* **Weakest criterion:** 0.75
* **Weakest-link penalty:** 0.055
* **Adjusted progress:** 0.820
* **Final score:** **1.8**

### What prevents the next Type?

Type II is incomplete, so the score stays below 2.0.

* **II.1:** A persistent actor must own each case from intake to a closed outcome, including returning an API result to the caller, not only produce one triggered reply, report, or ChatGPT conversation.
* **II.4:** That actor needs its own principal on interactive runs, memory it owns across channels, and durable execution state, not only an Agent ID plus an end-user or shared connection.
* **II.5:** Supervision needs an in-run stop and exception escalation, not only approvals, aggregate analytics, and after-the-fact audit.

## Execution coverage

I'll follow the evaluation skill and rate only the product in the spec.

I'll verify the cited docs before scoring domain span, sharing, reach, and ready-made jobs.

The API docs check out. I’ll look for scoring notes in the repo so the grades stay consistent with the rubric.

**Execution coverage: 0.70 / 1.00**

ChatGPT Workspace Agents, on Business, Enterprise, and Edu as of 2026-09-29, is a hosted builder for shared repeatable agents. People across a workspace can create an agent, connect enabled apps, publish it, run it in ChatGPT, put it in Slack, schedule it, or trigger it by API. It is not a specialist-craft tool. It does not ship a cross-organization job marketplace, a shared ChatGPT run, or documented read/write jobs for each connected system.

| Criterion | Grade | Evidence | Source |
| --- | ---: | --- | --- |
| E.1 | 1.00 | General workspace agent builder, not one craft or function. Enabled members create and run agents for their own tasks. Calendar, Drive, Slack, and SharePoint are connections, not a single-suite limit. | https://help.openai.com/en/articles/20001143/ |
| E.2 | 0.75 | Shared agent with Can chat/Can edit, groups, and a team directory. Slack puts the agent in a channel thread with teammates. ChatGPT runs and memory stay per user; simultaneous draft edits do not merge. | https://help.openai.com/en/articles/20001143/ ; https://help.openai.com/en/articles/20001199-chatgpt-agents-app-in-slack |
| E.3 | 0.75 | Listed apps include Google Calendar, Drive, Slack, and SharePoint, with sign-in and write-action approval. Slack replies and scheduled posts are documented writes. Read/write is not documented as shipped jobs for each system. | https://help.openai.com/en/articles/20001143/ ; https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-for-plugins-and-apps |
| E.4 | 0.50 | Team directory is an organization-internal listing. Templates start an agent. Skills are created, uploaded, or selected if already available. No marketplace where the vendor, third parties, and customers publish installable agents. Custom MCP is buyer-wired. | https://help.openai.com/en/articles/20001143/ ; https://help.openai.com/en/articles/20001066-skills-in-chatgpt |
| E.5 | 1.00 | Work happens in the ChatGPT sidebar or by @mention, in a Slack channel, and through the documented trigger API. The API returns a ChatGPT conversation URL, not the reply. Run-status polling is beta and is not required for the surface. | https://help.openai.com/en/articles/20001143/ ; https://developers.openai.com/workspace-agents/trigger-runs ; https://help.openai.com/en/articles/20001199-chatgpt-agents-app-in-slack |
| E.6 | 1.00 | Documented for Business, Enterprise, and Edu, with RBAC for run, build, and publish, an admin Agents area, and Slack admin setup. Enterprise stays off until an admin enables it. API tokens require an admin permission, then creation in Admin. | https://help.openai.com/en/articles/20001143/ ; https://developers.openai.com/workspace-agents/authentication ; https://help.openai.com/en/articles/20001236-deploy-chatgpt-workspace-agents-to-slack-admin-setup |
| E.7 | 0.75 | A prompt produces a draft plan, and guided setup asks questions. Templates still require choosing tools and refining in the builder. Schedules and API triggers are separate channel settings, not a turn-on catalog of finished jobs. | https://help.openai.com/en/articles/20001143/ ; https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes |

* **Raw mean:** 0.82
* **Weakest criterion:** 0.50
* **Weakest-link penalty:** 0.13
* **Uncapped score:** 0.70
* **Span cap:** none
* **Final score:** **0.70**

### What most limits coverage?

E.4 is the weakest grade. There is no first-party marketplace where OpenAI, third parties, and customer organizations publish installable agents or workflows. The team directory does not leave the workspace. Templates are not a cross-customer catalog, and custom MCP or uploaded skills do not replace one. E.2, E.3, and E.7 sit at 0.75: ChatGPT runs are not a shared thread, write-back is not documented as shipped jobs for calendar and files, and a generated agent still needs a person to connect tools and set triggers.
