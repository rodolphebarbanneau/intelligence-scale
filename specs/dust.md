---
name: Dust
slug: dust
url: https://dust.tt/
docs: https://docs.dust.tt
kind: product
reviewed: 2026-09-28
---

# Dust

## Product

Dust is a workspace product for creating, sharing, and running customizable AI agents on company knowledge and tools. An organization adopts the Dust workspace: agents, skills, spaces, pods, connectors, triggers, and admin controls. The model selected for a conversation or agent is part of that chassis.

People use Dust in the web app at dust.tt (US) or eu.dust.tt (EU). They mention an agent with `@` in a conversation, or send a message with no mention and Dust routes it to the workspace default agent ( `@dust` unless an admin sets another). The same agents can be called from Slack, Microsoft Teams, email (`agent-name@dust.team` when an admin enables Email Agents), a Chrome/Firefox/Chromium browser extension, the Dust CLI, a Raycast extension, a Google Sheets add-on, a Zendesk app, Zapier, Make, self-hosted n8n, Power Automate, and the Dust API.

A builder opens Create from the home page, starts from scratch or a template, and uses Sidekick inside Agent Builder to draft instructions and propose tools, skills, and a model. Each agent has a handle, description, tags, editors, and a published or unpublished state. Published agents are visible to workspace members who can also reach the spaces those agents use. Unpublished agents stay visible to their editors.

Dust documents two plans. Business is self-serve: a free option (no credit card, up to 5 users, 3 connectors, 5 spaces) and paid Pro and Max seats (up to 100 seats). Enterprise is sold through sales and adds unlimited connectors and MCP servers, workspace-pooled credits, SCIM, audit logs, custom retention, single-tenant deployment, and priority support with an SLA. Seats on credit-priced plans are Free (500 lifetime credits), Pro (8,000 credits per seat per month), and Max (40,000 credits per seat per month). Enterprise also offers a pooled plan where members draw from a shared workspace credit pool.

The homepage states that Dust is used by teams at 3,000+ organizations. That figure is vendor-published. No sibling product specs are in scope.

## Features

### Workspace and conversations

Primary source: https://docs.dust.tt/docs/user-documentation/getting-started/intro-to-dust

- A workspace is the collaborative environment where members talk to agents, organize data in spaces, manage connections, and apply roles and permissions. Source: https://docs.dust.tt/docs/user-documentation/admins/admin-governance/access-controls-and-permissions
- Members mention an agent with `@` to ask a question. Multiple agents can be called in one discussion. Source: https://docs.dust.tt/docs/user-documentation/getting-started/intro-to-dust
- Conversations are scoped to one active agent at a time. The composer shows that agent, and a message does not require an `@` mention. Source: https://docs.dust.tt/docs/user-documentation/agents/steering-conversations
- While an agent runs, thinking blocks, tool calls, searches, and file operations appear live. A person can inspect any action. Source: https://docs.dust.tt/docs/user-documentation/agents/steering-conversations
- A person can send a message while the agent is still working. The agent finishes its current round of actions, then picks up queued messages with the prior context. Source: https://docs.dust.tt/docs/user-documentation/agents/steering-conversations
- Stopping an agent keeps work already completed and cancels only what has not started. Source: https://docs.dust.tt/docs/user-documentation/agents/steering-conversations
- Share opens a conversation so colleagues can join and work with the same agents. Source: https://docs.dust.tt/docs/user-documentation/getting-started/faq/managing-agents/can-i-share-a-conversation
- Branching creates a new conversation from a point in an existing one. The child starts with a compaction summary plus copies of files and tool outputs. Edits in the child do not affect the parent. Source: https://docs.dust.tt/docs/user-documentation/agents/branch-a-conversation
- Context compaction summarizes earlier messages so later runs use the summary instead of the full older history. Original messages stay stored and visible. Compaction is offered at 33% context use, warned at 70%, and required at 80% before new user messages. Source: https://docs.dust.tt/docs/user-documentation/agents/context-compaction
- Convert to agent, after the first agent response, opens Agent Builder with Sidekick pre-loaded from that conversation. Source: https://docs.dust.tt/docs/user-documentation/agents/default-agents/agent-builder-sidekick

### Agents

Primary source: https://docs.dust.tt/docs/user-documentation/agents/create-your-first-agent

- An agent combines a model with instructions, tools, and company knowledge. Source: https://docs.dust.tt/docs/developer-platform/overview/developer-platform
- Create starts from scratch or a template. Sidekick opens to draft instructions and a working configuration.
- Instructions direct the agent's responses. Tools & Knowledge give it search, web, and other actions. The agent chooses which tools to use before replying.
- Preview next to the builder tests the agent while editing.
- A handle becomes the `@` name. A description helps teammates and `@dust` route people to the right agent. Tags organize agents. Only administrators can create new tags.
- Publishing makes an agent visible and usable by workspace members who have access to the data sources it uses. A non-published agent is visible only to its editors.
- Editors are listed on the agent. Admins can open any agent in view-only mode and click Become an editor to edit it. Source: https://docs.dust.tt/docs/user-documentation/admins/agents-management
- Use the agent in the web app with `@NAME`, in Slack with `@dust +NAME`, or from Zapier when the agent is shared or company-scoped.
- Templates open a Sidekick-guided flow pre-loaded with the template's context. Source: https://docs.dust.tt/docs/user-documentation/agents/templates
- Advanced > Structured Response Format accepts a JSON schema so the agent returns structured output. The option appears only when the selected model supports it (ChatGPT 5 and later, Sonnet and Haiku from 4.5, Gemini 3.0 and later). Source: https://docs.dust.tt/docs/user-documentation/agents/structured-output-format
- JIT tools can be enabled from the composer for the current conversation only. They do not change the saved agent. Source: https://docs.dust.tt/docs/user-documentation/agents/tools/jit-tools
- Manage Agents supports search and filters including Editable by me and Default. Source: https://docs.dust.tt/docs/user-documentation/admins/agents-management

### Default agents

Primary source: https://docs.dust.tt/docs/user-documentation/agents/default-agents/dust

- `@dust` is the general-purpose default agent. Unmentioned messages go to the workspace default agent, which is `@dust` unless an admin configures another. It uses Company Data the account can access. Default agents cannot be edited in Agent Builder; admins can only enable or disable them.
- `@deep-dive` runs longer investigations (docs describe 10 to 30 minutes when needed). It plans, consults a planning agent, spawns up to 6 sub-agents in parallel, and synthesizes a cited report. It uses Company Data knowledge and tools, web search, dynamic tool discovery, and Frames. It cannot use the Table Query tool or Restricted Spaces. Source: https://docs.dust.tt/docs/user-documentation/agents/default-agents/deep-dive-agent
- `@help` answers questions about Dust from public docs and dust.tt. It cannot be deactivated. Source: https://docs.dust.tt/docs/user-documentation/agents/default-agents/help
- `@analyst` answers workspace usage questions from analytics data. It is available to admins and managers by default. Source: https://docs.dust.tt/docs/user-documentation/agents/default-agents/analyst
- Sidekick lives only in Agent Builder. It is not mentionable and has no API. It drafts instructions as accept/reject diffs, recommends tools, skills, and models, and can research workspace data sources after asking. It cannot create or edit triggers or draft skills. Sidekick usage does not consume workspace credits; fair-use caps are 100 messages per user per 24 hours (200 on Enterprise) plus a global free-usage cost cap. Source: https://docs.dust.tt/docs/user-documentation/agents/default-agents/agent-builder-sidekick

### Models

Primary source: https://docs.dust.tt/docs/user-documentation/agents/model-selection

- Every agent runs on a model. The composer picker changes the model for the next message in that conversation. Agent Builder sets the agent's default model.
- Auto models Basic, Standard, and Premium are ordered lists of model and reasoning-effort combinations that Dust benchmarks and updates. Dust uses the first candidate available to the workspace. Auto models do not pick a model per task.
- Specific models from OpenAI, Anthropic, Google, Mistral, and other providers remain available through More models when plan and admin settings allow them.
- Reasoning effort on a pinned model can be None, Light, Medium, or High where the model supports it.
- During a detected provider outage, auto models skip degraded models. A pinned specific model is not replaced automatically; the picker warns and offers retry with the matching auto-model level.
- Slack and triggers use the agent's configured model, not a composer pick. The conversation API accepts an optional `modelSelection` override per message.
- Model access tiers (Basic, Standard, Premium, Ultra) let admins cap models and reasoning efforts for the workspace, a group, or one member. Ultra is an admin tier, not a fourth auto-model row. A Published agents setting lets everyone run published agents above their personal ceiling. Source: https://docs.dust.tt/docs/user-documentation/admins/usage-seats-and-credits/model-access-tiers
- Premium models and reasoning-effort combinations require a usage-based credit plan. Source: https://docs.dust.tt/docs/user-documentation/agents/model-selection

### Skills

Primary source: https://docs.dust.tt/docs/user-documentation/agents/skills/skills-overview

- Skills are reusable packages of instructions, knowledge, and tools shared across agents. Updating a skill updates every agent that uses it.
- Default skills include Discover Knowledge, Discover Tools, Go Deep, and Frame sharing. Builders can create custom skills and customize a global skill (labeled "Based on [original]").
- Skill creation and editing is reserved to people with create-skill permission (docs still say Builders and Admins on this page). Anyone can use a skill if they can reach its underlying resources.
- Instructions can reference MCP tools, other skills, and knowledge (Notion, Google Drive, Confluence) via `/` or Add capabilities / Attach knowledge.
- An agent enables a skill when the situation matches. Unused skills are not loaded.
- A skill is scoped to the spaces its resources require. An agent can use a skill only if it has every required space. Space requirement changes apply immediately.
- Editors edit the skill. Admins can open any skill view-only and become an editor.
- Skills are versioned. History lists past versions with date and author.
- Availability is Editors only, All members, or Members and agents. Members and agents requires Manage skill availability plus Make skills discoverable to agents. A restricted Pod on a skill limits who can view or use it. Source: https://docs.dust.tt/docs/user-documentation/agents/skill-availability
- Discover Skills lets an agent find and enable discoverable workspace and Dust-provided skills during a conversation. `@dust` includes it by default. It does not bypass space permissions. Source: https://docs.dust.tt/docs/user-documentation/agents/discover-skills
- Discover Knowledge lets an agent search and browse company documents and query warehouses without configuring each source as a separate tool. It does not write to third-party apps. Source: https://docs.dust.tt/docs/user-documentation/agents/discover-knowledge
- Discover Tools lets an agent find and enable specialized toolsets for live data or write actions. `@dust` includes dynamic tool discovery. Source: https://docs.dust.tt/docs/user-documentation/agents/discover-tools
- Go Deep equips an agent with the same research capabilities as `@deep-dive` (sub-agents, company data exploration, warehouses, web search). Disabling `@deep-dive` removes Go Deep from all agents. Source: https://docs.dust.tt/docs/user-documentation/agents/go-deep
- Self-improving skills (optional) analyzes conversations nightly and proposes instruction and tool edits. Editors accept or reject each suggestion. Workspace and per-skill toggles control it. Analysis is billed as programmatic usage; batch mode is half the cost of streaming. Batch mode is not covered by provider ZDR; admins can switch to streaming mode. Source: https://docs.dust.tt/docs/user-documentation/agents/self-improving-skills

### Knowledge and data sources

Primary source: https://docs.dust.tt/docs/user-documentation/data-sources/overview

- Data source types are Connections (auto-synced apps), Tools (MCP access to third-party systems), Public Websites (crawler), Folders (static uploads), Conversation Files (per-conversation uploads), and Custom Connections (API or scripts).
- Connections sync automatically. Admins choose which Slack channels, Drive folders, Notion pages, and similar objects Dust can read. Updates usually appear within a few minutes. Source: https://docs.dust.tt/docs/user-documentation/data-sources/connections
- Documented managed connections include Google Drive, Notion, Confluence, Intercom, GitHub, Microsoft, Snowflake, BigQuery, Zendesk, Gong, Slack, and Salesforce. Source: https://docs.dust.tt/docs/user-documentation/data-sources/connections
- After ingest, data is exposed through Company Data or a specific space. Source: https://docs.dust.tt/docs/user-documentation/data-sources/connections
- Knowledge methods on an agent are Search (semantic/RAG), Include Data (exhaustive, newest first, up to the context window), Query tables (SQL on warehouses, CSV, Google Sheets, or Notion databases), Extract Data (schema extraction), and Find in data sources (filesystem-style browse). Source: https://docs.dust.tt/docs/user-documentation/agents/knowledge/index
- Websites crawl public same-domain links from a start URL. Page limit is 1024 per connection. Login-gated sites are not crawled. Source: https://docs.dust.tt/docs/user-documentation/data-sources/websites
- Folders hold uploaded docs and CSV tables. There is no file-count limit. Manual upload limits are 30 MB via Folders and 10 MB in conversation on the folders page. Source: https://docs.dust.tt/docs/user-documentation/data-sources/folders
- Conversation files are scoped to that conversation and are not indexed as workspace data sources. Supported types include images (5 MB), audio (25 MB), and data/code/delimited files (50 MB). Audio and video are transcribed. Source: https://docs.dust.tt/docs/user-documentation/data-sources/conversation-files/conversation-files

### Tools

Primary source: https://docs.dust.tt/docs/user-documentation/agents/tools/index

- An agent with no tools uses only the model. With several capabilities it combines tools. Uploaded files can activate dynamic tools.
- Default tools that do not require a data source include Data visualization, Web Search & Browse, Create Files, Create Images, Agent Memory, and Run an agent.
- Web Search & Browse infers a Google query, browses up to 10 results, and can return markdown, raw HTML, or screenshots. Source: https://docs.dust.tt/docs/user-documentation/agents/tools/web-search-and-browse
- Agent Memory stores per-user items across conversations for that agent. Only that user can view or delete their memories. Each agent keeps a separate memory space. Source: https://docs.dust.tt/docs/user-documentation/agents/tools/agent-memory
- Run agent calls another agent in the background (separate conversation, result returned) or hands off so the selected agent replies to the user. Recursion depth is capped at 4. Source: https://docs.dust.tt/docs/user-documentation/agents/tools/run-agent
- The tools index documents third-party tools with workspace or personal credentials, including Notion (search, update, create pages; workspace), Slack (search and post; personal), GitHub (search, update, comment, create PRs and issues; workspace), Confluence (search, create, update; personal or workspace), HubSpot, Salesforce, Gmail (search and drafts), Google Calendar, Outlook, and Zendesk (tickets, metrics, draft replies).
- Admins add and configure tools under Spaces > Tools, including remote MCP servers. Tools default to workspace-wide (Company Space). Sharing can restrict a tool to selected spaces.
- An admin can restrict an MCP server so its tools are available only through skills that reference them, not from the agent builder, input bar, or just-in-time discovery. Source: https://docs.dust.tt/docs/user-documentation/admins/tools-management/adding-an-mcp-server
- Tools may use shared credentials (one account for everyone) or personal credentials (each user authenticates). Admins complete an initial OAuth flow for personal credentials. Users can disconnect personal credentials from Tools & Triggers. Source: https://docs.dust.tt/docs/user-documentation/admins/tools-management/personal-vs-shared-credentials
- The Tools section of the docs also lists dedicated pages for Airtable, Asana, Ashby, Attio, Canva, Databricks, File Generation, Fathom, Gong, Freshservice, Front, Google Drive, Image Generation, Jira, Microsoft Outlook, SharePoint and OneDrive, Microsoft Teams, Microsoft Excel, Miro, Monday, NetSuite, Power BI, Productboard, UKG Ready, Val Town, Vanta, Voice and sound generation, Salesloft, Semrush, ServiceNow, Slab, Snowflake, and Statuspage. This dossier does not copy action lists from those individual pages.
- Dust Apps as custom code tools are documented as deprecated. Source: https://docs.dust.tt/docs/user-documentation/agents/tools/index

### Computer

Primary source: https://docs.dust.tt/docs/user-documentation/agents/tools/computer

- Computer is a temporary workspace where an agent can run code, inspect and create files, process data, and return artifacts. Dust often uses it when working with files without an explicit request.
- Documented file work includes Excel/CSV transform and export, PowerPoint create and edit, Word and PDF handling (including OCR on scans for English, French, and mixed English/French), images, zip archives, and exact calculations.
- Computer does not have open internet access by default. Outbound requests must match Dust's system allowlist, a workspace admin allowlist, or a user approval for the current Computer when admins enable Agent-requested domains.
- Admins set `DST_*` configuration variables (readable, non-secret) and `DSEC_*` HTTPS secrets (placeholders inside Computer; Dust substitutes the secret only on approved HTTPS requests to configured domains). Source: https://docs.dust.tt/docs/user-documentation/admins/tools-management/computer-admin-setup
- `dsbx` is a CLI inside Computer for interacting with the Dust environment without dumping large intermediates into the conversation.

### Triggers

Primary source: https://docs.dust.tt/docs/user-documentation/agents/triggers/schedules

- Agent Builder has a Triggers section. A schedule has a name, a natural-language frequency that Dust turns into a confirmed cron-like schedule, an optional custom message, and a timezone (default: the user's location).
- A trigger run costs credits like any other agent run. Credits can be My credits (the editor) or Workspace credits (programmatic pool). Changing the pool requires editor rights plus workspace-pool access, or an admin/manager change on the Automations page. Source: https://docs.dust.tt/docs/user-documentation/agents/triggers/credits-usage
- Admins set Charge automations to the workspace as everyone, selected groups, or admins only. Source: https://docs.dust.tt/docs/user-documentation/agents/triggers/credits-usage
- Admins and managers see every trigger under Programmatic Usage > Automations. Members review their own automations from Tools in the user menu and can enable, disable, or delete them. Source: https://docs.dust.tt/docs/user-documentation/agents/triggers/credits-usage
- A trigger stops when its credit pool or programmatic cap is exhausted. Missed runs are not replayed. Source: https://docs.dust.tt/docs/user-documentation/agents/triggers/credits-usage
- Webhook payloads can be filtered. Dust can generate a filter from a description for supported sources. Custom webhooks use a Lisp-style filter expression language. Source: https://docs.dust.tt/docs/user-documentation/agents/triggers/webhooks/filter-webhooks-payload
- Each webhook trigger defaults to at most 42 runs per sliding 24 hours. Editors can change that limit. Scheduled triggers have no such cap. Requests over the limit are dropped, not queued. Source: https://docs.dust.tt/docs/user-documentation/agents/triggers/webhooks/rate-limiting
- The API lists and gets agent triggers (scheduled runs and webhooks) with a workspace admin API key, and exposes an endpoint to receive external webhooks. Source: https://docs.dust.tt/llms.txt

### Wake-ups

Primary source: https://docs.dust.tt/docs/user-documentation/agents/tools/wake-ups

- Wake-ups let an agent schedule a future run in the same conversation (a date or a cron-like schedule). Agents discover the tools automatically or a builder can add them.
- Tools are `schedule_wakeup` (high stake, requires user confirmation), `list_wakeups`, and `cancel_wakeup`.
- The wake-up runs with the authentication of the user whose message created it. Other users cannot post to a conversation that has an active wake-up.
- At most one wake-up per conversation. Scheduled wake-ups run at most 32 times; the agent is told on the last run so it can schedule another.
- Wake-ups are enabled by default with no admin setup. Executions bill against the wake-up user's quota.

### Frames

Primary source: https://docs.dust.tt/docs/user-documentation/agents/frames/overview

- Frames are interactive agent outputs (reports, dashboards, calculators, visualizations). They can be edited in place, reverted one step at a time, downloaded, and shared by token-gated links.
- Add the Create Frames skill in Agent Builder. Frames in a conversation are listed from the folder icon.
- Admins set the Frame sharing policy. Public sharing is enabled by default.
- White-labeled Frames (plan-gated; contact sales) replace Dust branding on public Frames with a company logo and favicon configured under Admin > Branding. Source: https://docs.dust.tt/docs/user-documentation/agents/frames/white-labeled-frames

### Pods

Primary source: https://docs.dust.tt/docs/user-documentation/pods/overview

- A Pod is a shared workspace for conversations, tasks, and files around a common goal. Conversations are visible to Pod members and indexed for agent context.
- Tasks are lightweight work items that humans or agents can create, assign, start an agent on, and mark done. States are Open, In progress, and Done. Source: https://docs.dust.tt/docs/user-documentation/pods/tasks
- Files hold uploads, folders, Company Data links, and agent artifacts such as Frames.
- The Pods skill is available to all agents by default, including `@dust`, agents invoked inside a Pod, and triggered agents. Agents can list Pods, post conversations, manage tasks, upload and read files, search Pod knowledge, and (with Editor permissions) create Pods and manage members and a pinned Frame.
- Visibility is Open (any member can join) or Restricted (invite only).
- Pod roles are Member and Editor. A Pod always has at least one Editor. Mentioning a non-member can prompt an invite. Source: https://docs.dust.tt/docs/user-documentation/pods/members-and-roles
- Admins can require Restricted Pods only and can disable manual file adds so only agents and connectors populate Files. Source: https://docs.dust.tt/docs/user-documentation/pods/admin-controls
- Docs describe syncing Pod tasks with Jira, Asana, or Linear through an agent plus wake-ups. Source: https://docs.dust.tt/docs/user-documentation/pods/tasks

### Spaces

Primary source: https://docs.dust.tt/docs/user-documentation/admins/spaces-management

- Spaces organize and control access to data. Open spaces are available to all workspace members. Restricted spaces are limited to designated members or provisioned IdP groups.
- Company Data is a default space that cannot be modified or restricted.
- Only workspace admins create and manage spaces and add Connection data to a space.
- For folders, websites, and apps: in open spaces only admins and builders can add data; in restricted spaces all members can add data.
- An agent that uses a space is visible only to members of that space.
- Business supports up to 5 spaces. Enterprise supports up to 100.

### Slack, Teams, and email

Primary source: https://docs.dust.tt/docs/user-documentation/admins/quickstart

- Admins install the Dust Slack app, add it to channels, and members call `@dust` (optionally `+agent_name`). A channel can be linked so `@dust` in that channel uses a chosen agent. Source: https://docs.dust.tt/docs/user-documentation/agents/create-your-first-agent
- Slack auto-reply (available with Dust in Slack) lets a published agent's default channel answer without `@Dust`. Modes are all messages (including threads) or top-level posts only. Bot messages are ignored. Only admins change these settings. Empty responses are retried, so instructions cannot make all-messages mode conditional. Source: https://docs.dust.tt/docs/user-documentation/agents/integrations/dust-in-slack/slack-auto-reply
- Slack workflows can summon a Dust agent. Admins allow a workflow by exact sender name and grant Spaces (Company Data is always included). On credit-priced plans this is under Programmatic Usage > Automations > Slack workflows. Legacy plans email support@dust.tt. Source: https://docs.dust.tt/docs/user-documentation/agents/integrations/dust-in-slack/slack-workflows
- Dust in Teams is installed by a Dust admin (enable Microsoft Teams Bot, upload the app zip in Teams admin). Syntax is `@dust +agent_name` or `@dust ~agent_name`. Thread context and file attachments are supported. Meeting and voice/video integration are not. Source: https://docs.dust.tt/docs/user-documentation/agents/integrations/dust-in-teams
- Send Email to Agents is opt-in under Workspace Settings > Capabilities. Addresses are `agent-name@dust.team`. The agent reads the thread and attachments on that message, replies only to the sender, and emails Accept/Reject links before write tools. Only workspace members whose mail passes DKIM/SPF are processed. Agents do not initiate outbound email. Source: https://docs.dust.tt/docs/user-documentation/agents/integrations/send-and-forward-email-to-agents

### Browser, desktop, and in-app extensions

Primary source: https://docs.dust.tt/docs/user-documentation/agents/integrations/browser-extension

- The browser extension (Chrome Web Store and Firefox Add-ons) opens a side panel with the same composer, conversation history, inbox, and workspace MCP tools as the web app.
- Agents can read tab text or screenshots only after the user attaches them or approves a prompt. Multi-tab access is permission-gated. PDFs and images on the current page can be auto-attached.
- Agents can click and type on the current page except where a dedicated MCP tool exists (for example Notion or Gmail).
- Admins can disable Browser Extension Tools so agents cannot list or read tabs.
- The Raycast extension runs a Dust agent on selected Mac text and can replace the selection in place. EU workspaces set the Dust URL to eu.dust.tt. Source: https://docs.dust.tt/docs/user-documentation/agents/integrations/raycast-extension
- The Google Sheets add-on (Google Workspace Marketplace) calls an agent on a cell range and writes to a target column. Setup uses workspace ID, admin API key, and optional `eu` region. Agents must respond within 30 seconds. Source: https://docs.dust.tt/docs/user-documentation/agents/integrations/google-sheets-add-on
- The Zendesk marketplace app uses workspace ID and API key, optional default agent IDs, optional hidden customer metadata, and Zendesk group/role restriction. The Zendesk user must have a Dust account with the same email. Source: https://docs.dust.tt/docs/user-documentation/agents/integrations/dust-in-zendesk
- Meeting transcripts is a beta feature activated by Dust support. It can watch Google Meet transcripts in the organizer's Drive (`drive.meet.readonly`) and send them to a selected agent. Gong and notetaker MCPs (Granola, Fathom, Praiz) are documented separately. Source: https://docs.dust.tt/docs/user-documentation/agents/integrations/meeting-transcripts

### Automation platforms

Primary source: https://docs.dust.tt/docs/user-documentation/agents/integrations/zapier

- Zapier "Talk to an Agent" uses workspace ID and an admin API key. The agent must be Shared or Company; personal agents do not appear. Output is the `AgentMessage` property.
- Make.com has the same Talk to an Agent fields and Shared/Company agent restriction. Output content is in the `content` field. Source: https://docs.dust.tt/docs/user-documentation/agents/integrations/make-com
- n8n community node `n8n-nodes-dust` is documented for self-hosted n8n only (not n8n cloud). Actions are Talk to an agent and Upload a document. Only Company and Shared agents appear. Source: https://docs.dust.tt/docs/user-documentation/agents/integrations/n8n
- Power Automate installs DustAssistantSolution.zip as a custom connector. Actions include Talk to an Agent and Upload document. Auth is `Bearer` plus an API key. Source: https://docs.dust.tt/docs/user-documentation/agents/integrations/power-automate
- Pricing lists Zapier, Make, n8n, and Power Automate as automation platforms on Business and Enterprise. Source: https://dust.tt/home/pricing

### MCP

Primary source: https://docs.dust.tt/docs/user-documentation/agents/integrations/dust-mcp-server

- Dust can expose the workspace as a remote MCP server at `https://dust.tt/mcp` (US/global) or `https://eu.dust.tt/mcp` (EU), with OAuth (DCR or CIMD) and a required `resource` parameter.
- Documented first-version tools include current user/workspace, list agents, conversations and messages, Pod info and tasks, conversation/Pod files, and search across Spaces. It does not proxy every third-party tool in the workspace.
- The client acts as the authenticated user. Tokens are not Dust API keys. Admins can disable the server and restrict redirect URIs.
- Admins add inbound remote MCP servers from Spaces > Tools (OAuth automatic, bearer token, or static OAuth). Business pricing lists 5 remote MCP servers; Enterprise lists unlimited. Source: https://docs.dust.tt/docs/user-documentation/admins/tools-management/adding-an-mcp-server
- Client Side MCP Server is Preview. A developer app registers local tools for a conversation via the Conversations API. Tools run in the client. It requires OAuth personal access tokens, not API keys, and is not available inside the Dust web app or official browser extensions. Source: https://docs.dust.tt/docs/user-documentation/developers/client-side-mcp-server

### Admin and governance

Primary source: https://docs.dust.tt/docs/user-documentation/admins/admin-governance/workspace-governance-roles-groups-and-permissions

- Workspace roles are Admin, Manager, and Member. Access is the role plus group permissions plus resource access (spaces, agents, skills). Grants are additive.
- Admins configure settings, members, groups, billing and security (by default), governance permissions, external Frame sharing policy, and audit logs. They always retain Admin-only capabilities and manage model providers.
- Managers invite and remove members, change non-admin roles, view analytics, set group spend limits, review credit upgrade requests, and choose which groups can create and publish agents and skills. They do not get billing or security by default and cannot manage the external Frame policy or audit logs.
- Groups are provisioned (SCIM) or manual. Permissions are granted to groups in Everyone, Groups, or Admin only mode.
- Permission matrix includes create/publish agents, create skills, make skills discoverable to agents (admin only by default), view/export audit logs, billing, security and provisioning, model providers, Frame invite/publish (when policy allows), analytics, and group spend limits.
- The Builder role is being replaced by create/publish permissions. Existing builders are placed in a Builders group during the transition.
- Admins and managers can manage manual groups through the workspace management MCP server (`list_groups`, `get_group_members`, `create_group`, `update_group_members`).
- SSO uses the workspace IdP. Enforcing SAML logs out users who are not on SAML. Source: https://docs.dust.tt/docs/user-documentation/admins/admin-governance/single-sign-on-sso/single-sign-on-sso
- SCIM 2.0 provisions users and groups for enterprise customers. Settings & Governance > Roles can map groups to Admin or Manager. Source: https://docs.dust.tt/docs/user-documentation/admins/admin-governance/users-and-groups-provisioning
- Users create agents from spaces they can access and interact with agents built on spaces they belong to. Source: https://docs.dust.tt/docs/user-documentation/admins/admin-governance/access-controls-and-permissions

### Security

Primary source: https://dust.tt/home/security

- The security page states GDPR compliance, SOC 2 Type II certification, and that Dust enables HIPAA compliance.
- Data is encrypted with AES-256 at rest and TLS in transit. Hosting can be EU or US.
- The page states data is not used to train models and that third-party model providers have zero data retention.
- The homepage also lists dedicated single-tenant deployment, custom retention, SSO, automated provisioning, and audit logs. Source: https://dust.tt/
- Audit logs are an Enterprise feature. They record who did what, to which resource, from where, and when, and distinguish human vs agent-driven actions via metadata. Admins open Admin > IT & Security > Audit Logs with search, time filter, and CSV export. Streaming destinations include Datadog, Splunk, AWS S3, GCP GCS, and custom HTTPS. Source: https://docs.dust.tt/docs/user-documentation/admins/audit-logs/audit-logs
- Static egress IPs apply only to remote MCP servers on a workspace-verified domain and to Snowflake connections: `34.46.9.232` (US) and `35.195.191.222` (EU). Other outbound traffic uses dynamic cloud IPs. Source: https://docs.dust.tt/docs/user-documentation/admins/tools-management/static-egress-ips

### Billing, seats, and credits

Primary source: https://dust.tt/home/pricing

- Business seats: Free 0€ / 500 lifetime credits; Pro 24€ per seat per month yearly (8,000 credits); Max 120€ per seat per month yearly (40,000 credits). Monthly list prices on the FAQ are 30€ and 150€.
- Business includes 20+ models, custom agents, skills, knowledge, tools, schedules and triggers, Slack/Notion/GitHub/Drive plus other connectors or MCP, team workspaces, SSO (Okta, Entra ID, Jumpcloud; 5+ seats on demand), US/EU residency, up to 3 connectors, 5 spaces, 5 remote MCP servers, standard Frames, Pods, conversation API, and automation platforms. Programmatic usage is $0.01 per credit.
- Enterprise adds unlimited connectors and MCP servers, pooled credits and volume pricing, SCIM, audit logs, custom retention, single-tenant, white-labeled Frames, Data Source API, dedicated CSM, priority support and SLA, and custom legal terms.
- Credits are `token credits + action credits`. Action tiers are Free (0), Basic (1), and Advanced (3). Sub-agent costs add to the total. Unused monthly credits do not roll over. Source: https://docs.dust.tt/docs/user-documentation/admins/usage-seats-and-credits/credits
- Sidekick tokens and actions do not consume credits. Source: https://docs.dust.tt/docs/user-documentation/admins/usage-seats-and-credits/credits
- A 600 AWU-credit checkpoint can pause a root task started from the web app or browser extension. Admins can disable the checkpoint; managers can exempt an agent. Source: https://docs.dust.tt/docs/user-documentation/admins/usage-seats-and-credits/credits
- Roles and seat types are independent. Unassigned members can open the workspace but cannot post. Source: https://docs.dust.tt/docs/user-documentation/admins/usage-seats-and-credits/seat-management
- Credit draw order is individual seat credits, then workspace pool, then Enterprise PAYG. Free seats cannot use the pool. Programmatic usage (API, Zapier, n8n, Sheets, Slack bots, triggers) uses only the workspace pool, then PAYG. Source: https://docs.dust.tt/docs/user-documentation/admins/usage-seats-and-credits/credit-management
- Admins manage subscriptions from Admin > Billing. Canceling a paid Business subscription at period end reverts to free: one remaining admin, connections deleted, custom agents deactivated. Source: https://docs.dust.tt/docs/user-documentation/admins/billing/subscriptions-and-payments

### Analytics

Primary source: https://docs.dust.tt/analytics

- Admin > Analytics is for admins and managers. Periods include this credit cycle and rolling 7/30/90/180 days.
- The page shows pace vs cap, consumption charts, and attribution by agents, members, groups, models, tools, skills, sources, triggers, and API keys.
- Download raw data exports CSV for up to 15 days. Exports exclude message content.
- `GET /api/v1/w/{wId}/analytics/export` exports analytics with a workspace admin API key.

### Developer platform

Primary source: https://docs.dust.tt/docs/developer-platform/overview/developer-platform

- The developer platform is the Dust API, a JavaScript SDK (npm; docs on the package page), and the Dust CLI. Source: https://docs.dust.tt/docs/developer-platform/overview/javascript-sdk
- The API is documented as OpenAPI 3.0 with a Postman collection. Source: https://docs.dust.tt/docs/developer-platform/dust-api-documentation/openapi-and-postman
- Documented API areas include conversations (create, message, events/SSE, edit, cancel, validate actions, answer agent questions, files), agents (list, get, search, import, update, archive, export YAML), skills (list, import, archive), triggers, spaces, data sources and views, apps/runs, MCP client-side register/heartbeat/results, mentions, feedbacks, tools (MCP server views), and analytics export. Source: https://docs.dust.tt/llms.txt
- Business pricing includes the Conversation API. Enterprise adds the Data Source API. Source: https://dust.tt/home/pricing
- The CLI (`npm install -g @dust-tt/dust-cli`) defaults to interactive chat with `@Dust` and local filesystem access. Commands include login, status, logout, chat (interactive or `--message` programmatic), `skill:init`, and cache:clear. Headless auth uses `DUST_API_KEY` and `DUST_WORKSPACE_ID`. Source: https://docs.dust.tt/docs/developer-platform/dust-cli/dust-cli

## Sources

- https://docs.dust.tt
- https://docs.dust.tt/llms.txt
- https://docs.dust.tt/docs/user-documentation/getting-started/intro-to-dust
- https://docs.dust.tt/docs/user-documentation/agents/create-your-first-agent
- https://docs.dust.tt/docs/user-documentation/agents/model-selection
- https://docs.dust.tt/docs/user-documentation/agents/templates
- https://docs.dust.tt/docs/user-documentation/agents/structured-output-format
- https://docs.dust.tt/docs/user-documentation/agents/steering-conversations
- https://docs.dust.tt/docs/user-documentation/agents/branch-a-conversation
- https://docs.dust.tt/docs/user-documentation/agents/context-compaction
- https://docs.dust.tt/docs/user-documentation/agents/default-agents/dust
- https://docs.dust.tt/docs/user-documentation/agents/default-agents/deep-dive-agent
- https://docs.dust.tt/docs/user-documentation/agents/default-agents/help
- https://docs.dust.tt/docs/user-documentation/agents/default-agents/analyst
- https://docs.dust.tt/docs/user-documentation/agents/default-agents/agent-builder-sidekick
- https://docs.dust.tt/docs/user-documentation/agents/skills/skills-overview
- https://docs.dust.tt/docs/user-documentation/agents/skill-availability
- https://docs.dust.tt/docs/user-documentation/agents/discover-knowledge
- https://docs.dust.tt/docs/user-documentation/agents/discover-skills
- https://docs.dust.tt/docs/user-documentation/agents/discover-tools
- https://docs.dust.tt/docs/user-documentation/agents/go-deep
- https://docs.dust.tt/docs/user-documentation/agents/self-improving-skills
- https://docs.dust.tt/docs/user-documentation/agents/knowledge/index
- https://docs.dust.tt/docs/user-documentation/data-sources/overview
- https://docs.dust.tt/docs/user-documentation/data-sources/connections
- https://docs.dust.tt/docs/user-documentation/data-sources/websites
- https://docs.dust.tt/docs/user-documentation/data-sources/folders
- https://docs.dust.tt/docs/user-documentation/data-sources/conversation-files/conversation-files
- https://docs.dust.tt/docs/user-documentation/agents/tools/index
- https://docs.dust.tt/docs/user-documentation/agents/tools/web-search-and-browse
- https://docs.dust.tt/docs/user-documentation/agents/tools/agent-memory
- https://docs.dust.tt/docs/user-documentation/agents/tools/run-agent
- https://docs.dust.tt/docs/user-documentation/agents/tools/jit-tools
- https://docs.dust.tt/docs/user-documentation/agents/tools/computer
- https://docs.dust.tt/docs/user-documentation/agents/tools/wake-ups
- https://docs.dust.tt/docs/user-documentation/agents/triggers/schedules
- https://docs.dust.tt/docs/user-documentation/agents/triggers/credits-usage
- https://docs.dust.tt/docs/user-documentation/agents/triggers/webhooks/filter-webhooks-payload
- https://docs.dust.tt/docs/user-documentation/agents/triggers/webhooks/rate-limiting
- https://docs.dust.tt/docs/user-documentation/agents/frames/overview
- https://docs.dust.tt/docs/user-documentation/agents/frames/white-labeled-frames
- https://docs.dust.tt/docs/user-documentation/pods/overview
- https://docs.dust.tt/docs/user-documentation/pods/members-and-roles
- https://docs.dust.tt/docs/user-documentation/pods/tasks
- https://docs.dust.tt/docs/user-documentation/pods/admin-controls
- https://docs.dust.tt/docs/user-documentation/admins/spaces-management
- https://docs.dust.tt/docs/user-documentation/admins/quickstart
- https://docs.dust.tt/docs/user-documentation/admins/agents-management
- https://docs.dust.tt/docs/user-documentation/admins/admin-governance/workspace-governance-roles-groups-and-permissions
- https://docs.dust.tt/docs/user-documentation/admins/admin-governance/access-controls-and-permissions
- https://docs.dust.tt/docs/user-documentation/admins/admin-governance/single-sign-on-sso/single-sign-on-sso
- https://docs.dust.tt/docs/user-documentation/admins/admin-governance/users-and-groups-provisioning
- https://docs.dust.tt/docs/user-documentation/admins/tools-management/adding-an-mcp-server
- https://docs.dust.tt/docs/user-documentation/admins/tools-management/personal-vs-shared-credentials
- https://docs.dust.tt/docs/user-documentation/admins/tools-management/computer-admin-setup
- https://docs.dust.tt/docs/user-documentation/admins/tools-management/static-egress-ips
- https://docs.dust.tt/docs/user-documentation/admins/audit-logs/audit-logs
- https://docs.dust.tt/docs/user-documentation/admins/usage-seats-and-credits/seat-management
- https://docs.dust.tt/docs/user-documentation/admins/usage-seats-and-credits/credits
- https://docs.dust.tt/docs/user-documentation/admins/usage-seats-and-credits/credit-management
- https://docs.dust.tt/docs/user-documentation/admins/usage-seats-and-credits/model-access-tiers
- https://docs.dust.tt/docs/user-documentation/admins/billing/subscriptions-and-payments
- https://docs.dust.tt/analytics
- https://docs.dust.tt/docs/user-documentation/agents/integrations/dust-mcp-server
- https://docs.dust.tt/docs/user-documentation/agents/integrations/dust-in-slack/slack-auto-reply
- https://docs.dust.tt/docs/user-documentation/agents/integrations/dust-in-slack/slack-workflows
- https://docs.dust.tt/docs/user-documentation/agents/integrations/send-and-forward-email-to-agents
- https://docs.dust.tt/docs/user-documentation/agents/integrations/zapier
- https://docs.dust.tt/docs/user-documentation/agents/integrations/make-com
- https://docs.dust.tt/docs/user-documentation/agents/integrations/n8n
- https://docs.dust.tt/docs/user-documentation/agents/integrations/power-automate
- https://docs.dust.tt/docs/user-documentation/agents/integrations/browser-extension
- https://docs.dust.tt/docs/user-documentation/agents/integrations/raycast-extension
- https://docs.dust.tt/docs/user-documentation/agents/integrations/google-sheets-add-on
- https://docs.dust.tt/docs/user-documentation/agents/integrations/dust-in-zendesk
- https://docs.dust.tt/docs/user-documentation/agents/integrations/dust-in-teams
- https://docs.dust.tt/docs/user-documentation/agents/integrations/meeting-transcripts
- https://docs.dust.tt/docs/user-documentation/developers/client-side-mcp-server
- https://docs.dust.tt/docs/developer-platform/overview/developer-platform
- https://docs.dust.tt/docs/developer-platform/overview/javascript-sdk
- https://docs.dust.tt/docs/developer-platform/dust-api-documentation/openapi-and-postman
- https://docs.dust.tt/docs/developer-platform/dust-cli/dust-cli
- https://docs.dust.tt/docs/user-documentation/getting-started/faq/managing-agents/can-i-share-a-conversation
- https://dust.tt/home/pricing
- https://dust.tt/home/security
- https://dust.tt/
