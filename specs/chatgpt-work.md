---
name: ChatGPT Workspace Agents
slug: chatgpt-work
url: https://help.openai.com/en/articles/20001143/
docs: https://developers.openai.com/workspace-agents/
kind: product
reviewed: 2026-09-28
---

# ChatGPT Workspace Agents

## Product

ChatGPT Workspace Agents is OpenAI’s agent builder for repeatable tasks and workflows inside a ChatGPT workspace. A builder creates an agent, tests it before publishing, chooses its model and reasoning effort, connects apps and tools, shares it with teammates or the workspace, uses it in Slack, runs it on a schedule, or triggers it through an API. The product is the shared agent, its tools, channels, and workspace controls, not the model selected for a run.

Workspace agents are documented for ChatGPT Business, Enterprise, and Edu. They are not available on personal ChatGPT accounts. On ChatGPT Enterprise they are off by default at launch, and an admin enables them for eligible workspaces. Eligible Enterprise workspaces with Enterprise Key Management (EKM) can use them after an admin turns on building, publishing, and Slack usage. The ChatGPT assistant (`chatgpt`) and Codex (`codex`) are separate products. The Codex Workspace Agents plugin can author these agents; it does not run them.

People open Agents in the ChatGPT sidebar. They browse recently used agents, agents they built, and a team directory. Creation starts from a template or from a prompt that produces a draft plan, which the builder edits in the agent builder or in Agent Studio. After publish, anyone with access can run the agent in ChatGPT by opening it from Agents or by typing `@` and the agent name. Published agents can also run from Slack, from a schedule, or from the Workspace Agents API.

OpenAI publishes API docs at [developers.openai.com/workspace-agents](https://developers.openai.com/workspace-agents/). That host covers triggering a published agent and provisioning Workspace Agent access tokens. The builder, Slack, sharing, and admin surfaces are documented in the Help Center. A Workspace Agents Security Overview covers access, memory, logging, spend, and rollout for Enterprise and Edu.

## Features

### Browse and create workspace agents

Primary source: https://help.openai.com/en/articles/20001143/

- Open Agents in the left sidebar to browse Recently used, Built by me, and Team directory.
- Create from a template: browse templates, choose tools, create the agent, then refine it in the builder.
- Create with the agent builder: enter a prompt or start blank, review the draft plan, select Build this agent, then Create.
- ChatGPT can ask setup questions during guided agent setup. Source: https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes
- Preview an agent in the builder with a sample prompt before creating it.
- After create, select Update in the builder to save changes to a live agent.
- Duplicate an agent to create a draft copy under Built by me.
- Delete an agent permanently. The help article says this cannot be undone.

### Agent builder

Primary source: https://help.openai.com/en/articles/20001143/

- The builder sets the agent’s name, description, instructions, model, reasoning effort, icon, tagline, category, and starter prompts.
- Agent Studio is the in-product builder at `chatgpt.com/agents/studio/new`. The Codex plugin still requires it for preview, analytics, sharing, new Slack deployments, file and skill-file edits, access-token creation, and some app, custom MCP, or deployment setup.
- A published agent keeps a draft and a live version. Existing users keep the latest published version until the builder publishes the draft.
- Version history can preview an earlier version and republish it.
- The Agent Analytics page shows unique users and run counts over time.
- Agents can create audio files as part of their responses. Source: https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes

### Tools, apps, skills, and files

Primary source: https://help.openai.com/en/articles/20001143/

- Add tools, apps, custom MCP servers, skills, and files in the builder.
- Add apps such as Google Calendar, Google Drive, Slack, and SharePoint, plus image generation and web search. Available apps depend on what the workspace enables. Some apps require a connection.
- For each app, choose End-user account (each runner authenticates as themselves) or Agent-owned account (a shared connection).
- Workspace-level app enablement and action availability still apply. Per-agent controls set which actions the agent may use and when runners are asked to approve them. Source: https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-for-plugins-and-apps
- Write actions for apps and connectors default to Always ask. Some apps also allow Never ask or a Custom approval setting for specific write actions.
- Connector Action Constraints restrict how a supported connector action may be used. They do not filter data the connector returns. A builder describes the restriction in the conversational builder or in the connector Safety section.
- Add a skill by creating one, uploading a skill file, or selecting a skill already available. Skills help an agent follow a defined process or use specialized instructions.
- Skills in ChatGPT are reusable workflows that can include instructions, examples, and code. Source: https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- Files are limited to 512 MB each and 10 GB total per agent. Large collections can slow or prevent runs.
- Memory is a builder setting. The Codex plugin can enable and configure it. Source: https://help.openai.com/en/articles/20001143/
- Agent memory is scoped per user for ChatGPT runs and per deployed channel for Slack runs. Memory is not cross-referenced across ChatGPT and Slack runs. Source: https://cdn.openai.com/business-guides-and-resources/workspace-agents-security-overview.pdf

### ChatGPT channel

Primary source: https://help.openai.com/en/articles/20001143/

- Every agent includes a ChatGPT entry point from the sidebar.
- ChatGPT access can be Private to me, Anyone at the organization with the link, or Publish to the organization directory.
- Customize appearance with a short description, starter prompts, and a preview of how the agent appears in ChatGPT.
- Add a schedule on the ChatGPT channel: channel, schedule type, frequency, and extra instructions.
- Edit a created agent from the sidebar with Edit agent. Set or update a schedule from Schedule.
- Run an agent in ChatGPT by typing `@` and the agent name in a conversation, or by opening the agent from Agents and entering a prompt.
- The more-options menu can copy a share link, unpin the agent from the sidebar, or duplicate it.

### Slack

Primary source: https://help.openai.com/en/articles/20001143/

- Add a Slack channel in the builder. A Slack admin may need to approve access first.
- Before connecting, add the ChatGPT Agents app to the Slack channel from channel settings, Integrations, Add apps.
- Connecting Slack requires a Slack workspace, a Slack handle for the agent, and a channel. The handle must be unique among user groups in that Slack workspace. Source: https://help.openai.com/en/articles/20001199-chatgpt-agents-app-in-slack
- Slack requires shared authentication on every app connection. Personal connections must be switched before the agent can work in Slack.
- While an active Slack channel deployment exists, only the owner can add or update the agent’s apps and connectors.
- For a connected channel, the agent can respond to every message or only when someone mentions its Slack handle. Channel instructions can further steer Slack behavior.
- Creators can also choose whether the agent replies to relevant Slack thread follow-ups or only when mentioned. Source: https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes
- Changing the Slack workspace removes previously configured Slack channels and resets the Slack bot connection.
- Agents can run on a schedule and send results to a Slack channel. They can be used in public or private channels. Private-channel use requires adding the ChatGPT Agents app to that channel. Source: https://help.openai.com/en/articles/20001199-chatgpt-agents-app-in-slack
- Slack deployment needs a paid Slack plan and a Business, Edu, or Enterprise ChatGPT account. Slack must allow the ChatGPT Agents app and must let members create user groups, because each deployed agent gets a user group for `@mention`. Source: https://help.openai.com/en/articles/20001236-deploy-chatgpt-workspace-agents-to-slack-admin-setup
- Admin Slack setup is three steps: enable Workspace Agents in Slack in ChatGPT, install the ChatGPT Agents app in Slack, and enable Slack user-group management. That setup only makes Slack available; each agent’s channel and reply behavior are configured later. Source: https://help.openai.com/en/articles/20001236-deploy-chatgpt-workspace-agents-to-slack-admin-setup
- Workspace Agents in Slack is an additional ChatGPT app that must be enabled alongside the regular Slack app in ChatGPT. Enable it from Workspace Settings, Apps, Directory. Source: https://help.openai.com/en/articles/20001236-deploy-chatgpt-workspace-agents-to-slack-admin-setup
- Slack Enterprise Grid needs org-level approval, then adding the app to each Slack workspace, then members connecting one approved Slack workspace from ChatGPT. After that, users can invoke any agent added to one of their Slack workspaces. Source: https://help.openai.com/en/articles/20001199-chatgpt-agents-app-in-slack
- The Slack app in ChatGPT is enabled by default for Business accounts. Enterprise admins enable Workspace agents in Slack from Admin app settings, including RBAC. Source: https://help.openai.com/en/articles/20001199-chatgpt-agents-app-in-slack

### Workspace Agents API

Primary source: https://developers.openai.com/workspace-agents/trigger-runs

- Add an API channel in the workspace agent builder. The published channel has a public trigger id in `agtch_...` format.
- `POST https://api.chatgpt.com/v1/workspace_agents/{id}/trigger` starts a published agent from a server-side system or automation.
- The request body requires `input`. Optional `conversation_key` continues the same agent conversation across trigger events.
- An optional `Idempotency-Key` header retries the same source event without queuing a second trigger.
- The API queues the trigger and returns `202 Accepted` with a `conversation_url` on ChatGPT. The agent’s response is not returned through the API.
- Run-status polling is beta. Send `OpenAI-Beta: workspace_agent_runs=v1` on trigger to receive `agent_trigger_run_id` (`apirun_...`), then `GET https://api.chatgpt.com/v1/workspace_agents/{id}/runs/{run_id}`.
- Run statuses are `queued`, `in_progress`, `suspended`, `completed`, and `failed`. Terminal statuses are `completed` and `failed`. Failed runs can report `dispatch_failed` or `run_failed`.
- Authenticate with a Workspace Agent access token as a bearer credential on `api.chatgpt.com`. These tokens are scoped to Workspace Agents API operations only. Source: https://developers.openai.com/workspace-agents/authentication
- Before a user can create a token, an admin must enable Workspace agents and turn on Allow users to create personal access tokens in Admin > Permissions & roles. Create the token in ChatGPT Admin > Access tokens and select the Workspace Agents scope. Source: https://developers.openai.com/workspace-agents/authentication
- Schedules and API trigger changes require a published agent before they become live. Source: https://help.openai.com/en/articles/20001143/

### Workspace Agents plugin in Codex

Primary source: https://help.openai.com/en/articles/20001143/

- The plugin is beta. It creates, inspects, updates, and publishes workspace agents from Codex. Codex updates configuration; it does not run the agent.
- The plugin is available in supported ChatGPT workspaces with Workspace Agents enabled. The same RBAC applies in ChatGPT and in the plugin. There is no Codex-only toggle. Disabling Workspace Agents for a user or role also disables the plugin for that user or role.
- The plugin can find agents the user created or can edit; inspect draft and published configuration; edit name, description, instructions, model, icon, tagline, category, and starter prompts; configure Memory, web search, image generation, apps, app actions, write approvals, and app parameter constraints; choose end-user or agent-owned connections; upload new files and inspect attached files or skills; create, update, or delete schedules; configure API trigger channels and retrieve live trigger endpoints; inspect or update existing Slack deployments where supported; and publish when the user explicitly asks.
- Agent instructions do not grant app access. The app must be configured on the agent. Constraints narrow action inputs; they do not filter outputs.
- The plugin can upload ordinary files to new paths. It does not overwrite existing files.
- Workflows that still require Agent Studio include previewing or running the agent, viewing analytics, changing sharing or access, setting up a new Slack channel, editing or detaching existing files or skill files, creating access tokens, retrieving API-triggered responses, and unsupported app, custom MCP, or deployment setup.

### Sharing and collaboration

Primary source: https://help.openai.com/en/articles/20001143/

- The owner can invite workspace members to Can chat or Can edit. Sharing is not available on an uncreated draft.
- Can chat lets a person chat with the agent and view its configuration. Can edit adds editing the shared draft and publishing new versions. Owner keeps full editing, permission management, workspace distribution, and deletion.
- Sharing by workspace link or listing in the directory does not make everyone an editor.
- Editors can change name, description, instructions, conversation starters, files, Builder skills, and supported apps, then preview, save, and publish. They cannot grant Can edit to others, change another editor’s access, change workspace-wide access or directory visibility, transfer or remove the owner, delete the agent, or manage owner-only configuration such as channel setup, shared ChatGPT skills, or custom MCP setup.
- Some dependencies stay with the owner. Collaborators may only attach certain connector accounts or shared skills that belong to the owner.
- Multiplayer editing uses a shared draft. It does not merge simultaneous changes. A Save conflict requires Refresh agent, which replaces the local draft.
- Owners can share with a workspace group where Groups are enabled. The agent must be owned by a workspace account, already created, and in the same workspace as the group. Personal agents cannot be shared with groups.
- Group access is Can chat or Can edit. Access follows current group membership. The highest access from any source applies.
- Workspace administrators manage group membership separately from the agent’s Share controls.

### Workspace admin controls

Primary source: https://help.openai.com/en/articles/20001143/

- Role-based controls include Enable agents (browse and run), Enable agent building (create, edit, and duplicate), Enable agent publishing (publish to the workspace directory), and Enable agent publishing with agent-owned connections (publish agents that use personal or shared authenticated connections).
- The same RBAC applies in ChatGPT and in the Codex plugin.
- Eligible EKM Enterprise workspaces can create and use workspace agents, connect supported tools and apps, add skills, files, and custom MCP servers, schedule runs, use Slack, and view version history and analytics. Agents stay off until an admin enables them. Source: https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes
- The global admin console has an Agents area. Admins can open an agent to review Agent ID, recent activity, connected apps, memory files, schedules, and analytics, or move into Builder to edit it. Source: https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes
- Admins and owners can unpublish or delete agents through the Workspace Agents API exposed via the Compliance Platform or the admin console at `admin.openai.com`. Source: https://cdn.openai.com/business-guides-and-resources/workspace-agents-security-overview.pdf
- Enterprise and Edu admins can control which connected tools and actions user groups can access, and who can use, build, and share agents. Source: https://cdn.openai.com/business-guides-and-resources/workspace-agents-security-overview.pdf
- To create a Slack handle, builders may need Slack permission to create, edit, and deactivate user groups.

### Security, compliance, and spend

Primary source: https://cdn.openai.com/business-guides-and-resources/workspace-agents-security-overview.pdf

- Workspace agents run inside the managed ChatGPT workspace. Access uses the workspace identity, role, app, and connector controls already used for ChatGPT Enterprise or Edu.
- An agent can use instructions, attached files, memory where enabled, connected apps, custom MCPs, Slack channel context for Slack-deployed agents, schedules and triggers, and generated artifacts. The data boundary depends on source-system permissions, app scopes, admin-enabled connectors, and authentication mode.
- ChatGPT runs can use the relevant end-user connection where supported. Slack and other non-interactive surfaces generally use shared or builder-configured connections because Slack cannot pause the run to authenticate each invoking user.
- Workspace agents inherit the ChatGPT Enterprise and Edu control plane, including identity and role management, SSO/SCIM where configured, app controls, supported retention and residency, and no training on business data by default.
- Agent-related data can include definitions and sanitized snapshots, prompts and instructions, published versions, schedules and triggers, run metadata, agent-authored messages, connector-call metadata, skill usage, memory paths or actions, and generated artifacts.
- For Enterprise and Edu, the Compliance Platform can export agent lifecycle, run, trigger, connector, skill, and memory events as immutable JSONL for SIEM, DLP, eDiscovery, or audit workflows. The Compliance API can expose each agent’s configuration, change audit logs, and run traces.
- Workspace agents use credits when they run. Cumulative credit usage is visible in ChatGPT Workspace Settings. Agent-specific budget caps or alerts are not a distinct product surface in that overview.
- On credit-based Business and Enterprise/Edu pricing, Workspace Agent runs use token-based credit pricing. A typical end-to-end run using GPT-5.6 may consume between 5 and 25 credits. Workspace Agents share agentic usage and credits with Codex and other ChatGPT agentic features when those features are on the plan. Source: https://help.openai.com/en/articles/11481834-chatgpt-rate-card-business-enterpriseedu-credit-based-pricing
- Enterprise agreements billed in USD use a separate token-based rate card. Source: https://help.openai.com/en/articles/11481834-chatgpt-rate-card-business-enterpriseedu-credit-based-pricing
- ChatGPT respects Slack’s existing permissions for searchable messages and files. Enterprise admins may use the Compliance API to access user content. Source: https://help.openai.com/en/articles/20001199-chatgpt-agents-app-in-slack

## Sources

- https://developers.openai.com/workspace-agents/
- https://developers.openai.com/workspace-agents/trigger-runs
- https://developers.openai.com/workspace-agents/authentication
- https://help.openai.com/en/articles/20001143/
- https://help.openai.com/en/articles/20001199-chatgpt-agents-app-in-slack
- https://help.openai.com/en/articles/20001236-deploy-chatgpt-workspace-agents-to-slack-admin-setup
- https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-for-plugins-and-apps
- https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes
- https://help.openai.com/en/articles/11481834-chatgpt-rate-card-business-enterpriseedu-credit-based-pricing
- https://cdn.openai.com/business-guides-and-resources/workspace-agents-security-overview.pdf
