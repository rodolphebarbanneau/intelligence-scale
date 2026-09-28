---
name: Glean
slug: glean
url: https://www.glean.com/
docs: https://docs.glean.com/
kind: product
reviewed: 2026-09-28
---

# Glean

## Product

Glean is enterprise Work AI. It connects to the applications and documents an organization already uses, mirrors source permissions, and gives employees a permission-aware interface to search, ask questions, draft work, and run agents. The official documentation host is [docs.glean.com](https://docs.glean.com/). Glean describes the product as an enterprise AI coworker: search is one job it does, not the whole product. Source: https://docs.glean.com/user-guide/about/what-is-glean. The model selected for Assistant or an agent is part of that chassis.

Anyone with a work account on a Glean tenant can use it. Sign-in is through the organization's identity provider. The default web surface is `app.glean.com` or the tenant URL. The same product also runs as Glean for Desktop on macOS 12 and later and Windows 10 and later, as iOS and Android apps, as a browser extension sidebar, and as Glean companion on highlighted page text. Admins can embed Glean in Slack, Microsoft Teams, Zoom, GitHub, and Miro at the same Assistant entitlements, and Insights reports usage in Zendesk, ServiceNow, and Service Cloud. MCP hosts such as Cursor, Claude Desktop, ChatGPT, and Codex can call a Glean MCP server.

People start in Chat for most questions. Keyword queries can jump to documents inline. A dedicated Search page adds filters and a full results list. Agents are purpose-built assistants launched from the Agent Library. Skills package reusable instructions and tools. Memory, where the deployment supports it, stores user-level preferences and work context. Deep Research produces a long-form, citation-rich report. The Library holds artifacts, projects, meeting notes, Go Links, Answers, and Announcements.

Admins configure the tenant from the Admin Console: connectors, tools, SSO, RBAC, models, agents, Protect, Insights, and usage. Connectors index content into an isolated tenant and, where configured, expose live tools. Two model-key modes exist: Glean Universal Model Key, where Glean provisions models, and Customer Key (BYOK), where the customer supplies Azure OpenAI, Amazon Bedrock, Google Vertex AI, OpenAI, or Anthropic credentials. Pricing documented on the Enterprise Flex page is per-user seats plus a pooled FlexCredit allowance for metered Assistant, agent, and API usage. Glean Core Suite is a separate seat-based plan with its own usage dashboard. Glean Protect is included; Protect+ is a licensed add-on. No sibling product specs exist for this dossier.

## Features

### Glean Chat

Primary source: https://docs.glean.com/user-guide/assistant/glean-chat/

- Chat is the conversational interface to company knowledge. Users ask questions, create documents and presentations, analyze data, and get work done, with responses personalized by permissions, activity, and role.
- Answers include citations from company documents, messages, and data. Keyword-style queries can show search results inline so a user can open a document without switching pages.
- An agentic engine plans tasks step by step. Users pick a reasoning mode in the chat input: Adaptive, Fast, Thinking, or Deep research. Adaptive is the default when available. The selection persists across queries.
- Adaptive starts with a fast response and switches to deeper reasoning when the question needs it or needs tools that Fast mode does not support.
- Fast answers simple tasks quickly. Tools from connected apps are not available. Switch to Thinking to use those tools.
- Thinking uses more reasoning, searches company knowledge more thoroughly, and supports the full tool set, including connected-app tools.
- Deep research is a read-only mode for multi-source reports. An admin must enable it. It does not use tools that change connected apps.
- Users can tag a document or person with `@`, attach files, turn on web search, and continue a thread with follow-ups. Source: https://docs.glean.com/user-guide/about/end-user-quick-start-guide
- Chat supports Canvas documents, slide generation, spreadsheet generation, HTML artifacts, podcast artifacts, and image generation from natural-language prompts.
- Users can search repositories and generate code with draft pull requests grounded in the organization's codebase.
- Users can ask natural-language questions against Databricks and Snowflake datasets without writing SQL.
- Real-time voice conversations run on web, desktop, and mobile.
- Users can rename and queue chats, search chat history, share conversations, and ask Glean to search past chats from a new conversation.
- Sharing a chat does not transfer the original asker's permissions. Each recipient sees only sources they can access. Source: https://docs.glean.com/security/security-principles
- Autocomplete suggests documents as the user types. Short keyword queries can show high-confidence results inline, with a link to the full Search page. Source: https://docs.glean.com/user-guide/assistant/glean-chat/search-and-autocomplete
- Thumbs-up and thumbs-down feedback is available on each response. Source: https://docs.glean.com/user-guide/about/end-user-quick-start-guide

### How Glean accesses information

Primary source: https://docs.glean.com/user-guide/assistant/how-glean-accesses-info

- Every response can combine company knowledge (connected apps the user can access, plus the user's past chats and agent runs), web knowledge, and the model's pre-trained knowledge.
- The default is All Knowledge mode. Glean selects sources per question. The plus menu in chat can restrict a query to Both, Web search only, Company sources only, or No sources (LLM-only).
- Web search options appear only if an admin has enabled web search. No sources is unavailable in Deep Research.
- LLM-only mode does not retrieve company or web sources and does not invoke retrieval tools. Attached documents and write tools can still be used. Responses usually have no citations.
- In a project chat, Glean can still read that project's sources when No sources is selected.
- Results follow connector permissions and the user's activity. Permission changes in a connector are reflected quickly.
- Users can influence results by creating collections, marking documents verified, or attaching a URL or `@` mention.

### Search

Primary source: https://docs.glean.com/administration/search/about

- Search covers document contents, comments, @mentions, user activity, attachments, and team messages across connected applications.
- Queries can be natural language, acronyms, organization-specific terms, and custom synonyms. Glean builds a knowledge graph of content and interactions.
- Ranking uses access patterns, sharing, cross-application references, team discussions, and collaboration signals.
- Results are personalized by role, department, team, reporting structure, office location, past activity, and collaboration patterns.
- People search opens colleague profiles and expertise. Customer views can combine Salesforce, Zendesk, Jira, and other connected systems.
- Filters include UI controls, command-line style syntax, and custom metadata fields. Exact phrases use quotation marks.
- The dedicated Search page is for advanced filters and browsing a full results list. Chat is the default starting point for most questions. Source: https://docs.glean.com/user-guide/about/end-user-quick-start-guide

### Deep Research

Primary source: https://docs.glean.com/user-guide/assistant/deep-research

- Deep Research is an agent that writes a citation-rich report from enterprise systems and the web. A typical report is 5–10 pages.
- It searches company knowledge and the web, synthesizes across models, and outputs a structured report with linked citations.
- An admin must enable it. Users start it from Chat by selecting Deep research mode.
- Generation typically takes 5–30 minutes. It is supported on the web application only.
- It supports Glean Universal Key and Customer Key. Customer Key supports GPT-5, GPT-5.1, Claude Sonnet 4.5, and Gemini Pro 3 on Azure OpenAI, AWS Bedrock, and Google Vertex AI.
- Web content uses Brave Web Search only. Connected-app write tools (MCP tools) are not supported.

### Skills

Primary source: https://docs.glean.com/user-guide/assistant/skills

- Skills are reusable packages of instructions, templates, and tools for a specific task. They follow the open Agent Skills standard.
- Available Skills can be reused in Auto mode agents as well as Assistant.
- Glean Skills are built-in and run under the hood. They appear as intermediate steps in Assistant, not in the Skills library.
- Personal Skills are visible only to the owner and are managed from Settings → Skills.
- Shared Skills come from teammates or the organization. Consumers stay on the owner's latest version.
- Glean can route a query to a Skill automatically from its description, or the user can name a Skill, type `/skill-name`, or pick one from the composer `+` menu. Routing works best in Thinking mode.
- Users can upload a `.zip`, `.md`, or `.skill` file, import from a public or private GitHub URL, import a directory of Skills at once, or create a Skill by chatting.
- GitHub imports sync about once a day. Sync is one-way from GitHub to Glean. A Skill can contain up to 100 files across up to 6 directory levels.
- GitHub import, preview, and sync require Skills access. An admin must enable Third-party skills. If Skills is limited to a test group, people outside that group cannot use GitHub Skills.

### Memory and personalization

Primary source: https://docs.glean.com/user-guide/assistant/memory-personalization

- Memory stores user-level preferences, role, projects, and related work context across sessions. It does not store document content or grant extra document access.
- Availability is documented for GCP deployments that use Glean Universal Key. On unsupported deployments the Personalization section does not appear.
- Saved memories are explicit. Extracted memories come from chats and work activity. Users can view, edit, and delete memories in Settings or in chat.
- MCP hosts can add, update, and delete memories through `memory` and `memory_schema` tools on the default Glean MCP server.
- Users can import memories from another assistant with a prompt Glean provides. Import is not supported in Fast mode.
- Chat commands can disable memory for a conversation, enable it, or ask which memories are in use.
- Memories are private to the user. Admins cannot view individual memories. Memory is on by default on supported deployments, with no organization-level off switch documented on the user page.
- Agents can use memories subject to agent configuration and the user's settings.
- Extracted memories consolidate about daily. The Writing profile section in Settings is temporarily removed.

### Agents

Primary source: https://docs.glean.com/agents/how-agents-work

- Agents are reusable solutions that combine a goal and instructions, knowledge and context, tools, execution, and output plus working memory.
- Auto mode is the default builder. A person describes an outcome in Builder Assistant, then reviews, refines, and tests the draft. Source: https://docs.glean.com/agents/auto-mode-agent
- Workflow mode is a fixed sequence of steps, branches, loops, and hand-offs. Use it when the path must stay the same each run.
- Auto mode patterns documented are research, analysis, summarization, and drafting.
- In Auto mode the agent selects tools from the outcome. In Workflow mode a builder assigns tools to steps.
- Auto mode can use the Task tool to split work into sub-tasks and delegate them to sub-agents. The primary agent keeps permissions and error handling. This is on by default for supported Auto mode agents.
- Workflow mode stores each step's output in working memory. Context can be sequential (default), all prior outputs, or no prior outputs. `[[ ]]` references pass a specific step output or the original input.
- Builders test in Preview and inspect behavior in Debug. Glean saves the Builder Assistant conversation with the agent. Source: https://docs.glean.com/agents/auto-mode-agent
- Templates supply pre-configured prompts, tools, and logic by category, including General, Engineering, HR, IT, Marketing, Sales, and Support. Source: https://docs.glean.com/agents/templates
- Admins control who can create, publish, and run agents, which credentials are available, and which write tools can execute without user confirmation. Source: https://docs.glean.com/agents/independent-agents
- Write actions in the Glean web app pause for user approval by default. Admins can mark specific actions as run without confirmation. That default confirmation does not apply in Slack or Microsoft Teams. Source: https://docs.glean.com/security/security-principles

### Agent Library

Primary source: https://docs.glean.com/agents/concepts/agent-library

- The Agents page lists agents the signed-in user may run. Users search, filter, favorite, and launch agents from one catalog.
- Filters include creator, verification status, and admin-defined categories such as Sales, Marketing, Support, and HR.
- Verified / by Company badges mark agents reviewed by admins or moderators.
- Scheduled and content-triggered agents show trigger details and activation controls. Users can pause, resume, and review last-run status.
- Glean-managed agents list Glean as the author. Admins and Agent Moderators with global permissions can disable them for the organization.

### Independent Agents

Primary source: https://docs.glean.com/agents/independent-agents

- Independent Agents are in beta. Available templates, triggers, channels, and admin controls depend on the deployment.
- An independent agent runs a shared workflow without an individual user session. It has its own profile and can use admin-approved identities in connected apps.
- Documented building blocks are a dedicated profile, Slack or Microsoft Teams presence, event or schedule triggers, workflow-specific knowledge and tools, scoped service credentials, and admin publishing controls.
- Use an independent agent to monitor events, respond in a shared channel, or keep running until work resolves. Use an interactive or scheduled agent for a one-time or user-supervised run.
- A service credential is separate from independence. An independent agent can run without one, and a non-independent agent can still use one. Source: https://docs.glean.com/administration/agent-identity/overview

### Agent identity

Primary source: https://docs.glean.com/administration/agent-identity/overview

- By default an agent runs as the invoking user and uses that user's tokens and permissions.
- With agent identity, an admin registers a scoped service credential. A builder attaches it to an agent. The agent then acts as its own bot or service account.
- Credentials are injected server-side. The raw secret is not placed in the model context or agent sandbox.
- Documented credential templates include Slack, Microsoft Teams, Outlook, Atlassian, GitHub, GitLab, Salesforce, ServiceNow, Gong, Snowflake, BigQuery, GCP, AWS CloudWatch, Cursor, Linear, Zendesk MCP, Datadog, Grafana, Intercom, Sentry, and Coda.
- Templates are enabled per deployment. Missing templates require a Glean representative.

### Triggers

Primary source: https://docs.glean.com/agents/concepts/triggers

- A chat message trigger opens a conversational agent. Steps receive the current message plus prior turns. Conversation starters can include `[[placeholder]]` fields.
- An input form trigger shows text, document, or multiple-choice fields. Steps see a field only when the builder tags `[[field name]]`.
- A content trigger starts a run when connected content changes and passes `[[Trigger input]]`. Source: https://docs.glean.com/agents/concepts/content-trigger
- Recommended content-trigger sources are Gong, Jira, Salesforce Sales Cloud, Gmail, Google Calendar, Outlook, and Slack. Experimental sources include Google Drive, GitHub, OneDrive, SharePoint, ServiceNow, Zendesk, Zoom, and Outlook Calendar.
- Content-trigger activation is per user. The run uses that user's permissions. Admins set Content triggers to on for everyone, on for some teammates, or off.
- Slack content triggers exclude Gleanbot messages. External Slack channels are not supported.
- Schedule triggers let each user set when an agent runs for them. Independent Agents are a separate model for shared, agent-owned schedules. Source: https://docs.glean.com/agents/concepts/schedule-triggers
- Scheduled triggers default to off. Admins enable them for everyone or for selected users and IdP groups. A user may have at most 10 active background agents unless Glean raises the limit.
- Auto mode sets the schedule in the builder before publish. Workflow mode uses an input form trigger plus Activate agent in the library after publish.

### Tools

Primary source: https://docs.glean.com/administration/tools

- Tools let Assistant and agents create tickets, post comments, search records, and update fields in connected apps on the user's behalf.
- After setup, tools can be enabled for Assistant, Agents, and the Glean MCP server.
- Admins add catalog MCP integrations from Connectors, then manage tools under Platform → Tools. They can also import a custom MCP server.
- Each tool group has its own OAuth connection, Assistant and Agents toggles, per-operation enable/disable, and visibility scoping to users or groups.
- Admins can allow in-line execution of write tools in interactive agents, allow background agents to run write tools without confirmation, and restrict which builders can add a tool.
- Setup guides exist for calendar search, Code Writer, Confluence, Databricks, GitHub, Google, Jira (including extension tools), Microsoft 365, Salesforce, Snowflake, web search (OpenAI, Brave, or Google Gemini), Workday, Zendesk, and redirect URL tools.
- Users authenticate connectors in Settings. Per-tool choices include Always allow and Needs approval unless an admin has blocked the tool. Source: https://docs.glean.com/connectors/about

### Connectors

Primary source: https://docs.glean.com/connectors/about

- A connector integrates Glean with a source application. It fetches content and the source permission map into the customer's isolated tenant and parses native content plus common file types.
- Native connectors call source APIs for crawling, attachments, threads, mentions, people data, and activity signals.
- Web history connectors use the browser extension to make page titles from a user's browsing history searchable. Those results stay private to that user.
- Push API and partner connectors send data through the Indexing API for custom, self-hosted, or partner-maintained sources.
- Access modes are indexed, live (query-time fetch), and hybrid. Some connectors require per-user authentication for live access.
- Some catalog entries provide live tools without making the source searchable.
- Each connector supports inclusion and exclusion filters, authentication modes, and crawl scope settings. Admins monitor sync, visibility, and health from Admin console → Connectors.
- The Connectors hub lists native sources including Asana, Box, Confluence, Dropbox, GitHub, GitLab, Gmail, Gong, Google Calendar, Google Drive, Jira, Microsoft 365, Notion, OneDrive, Outlook, PagerDuty, Salesforce, SharePoint, Slack Real-Time Search, Teams, Website, and many others. Source: https://docs.glean.com/connectors/
- Indexed data is encrypted in transit to the tenant and encrypted at rest inside tenant boundaries.

### Code Writer

Primary source: https://docs.glean.com/administration/assistant/features/code-writer

- Code Writer proposes code changes and opens draft pull requests in GitHub from Assistant, from an agent step, or from Glean in Slack.
- It reads repositories through the GitHub connector and GitHub App, plans a targeted change, creates a branch and draft PR, and returns the URL and a summary.
- Review and merge stay in GitHub. Admins enable the tool and control who can use it.

### Code Search

Primary source: https://docs.glean.com/user-guide/assistant/code-search

- After GitHub, GitHub Enterprise Server, GitLab, or GitLab Server is connected, Assistant can run Code Search automatically on questions about code.
- It locates snippets, explains changes, generates snippets, and points at recent pull requests and commits. Agents can invoke the Code Search tool explicitly.
- Results follow the user's repository permissions.

### Data analysis

Primary source: https://docs.glean.com/administration/assistant/data-analysis/about-data-analysis

- Assistant can analyze CSV, XLSX, XLSM, JSON, XLS, and Google Sheets in chat. Thinking mode is required. Fast mode does not support data analysis.
- Users upload a file or tag an indexed link. Uploads use the raw file within size limits. Indexed links use crawled content, which may be truncated.
- Analysis runs in a per-user sandbox. Universal Key and Azure Glean-key customers use OpenAI Code Interpreter in a dedicated OpenAI project per customer.
- Cross-file numerical aggregation across multiple indexed spreadsheets is not supported. Consolidate data into one uploaded file instead.

### MCP

Primary source: https://docs.glean.com/administration/platform/mcp/about

- A Glean MCP server exposes Glean tools, agents-as-tools, and external tools proxied through the MCP Gateway to an MCP host.
- Documented Glean tools include Search, Chat, Read Document, Code Search, People, Artifacts, and image generation.
- The MCP Gateway can add custom tools, third-party MCP servers, and connector tools.
- Plug-ins for Cursor, Claude Code, and Codex discover skills and tools dynamically through Glean's gateway.
- Documented hosts include Antigravity, ChatGPT, LibreChat, Linear, Microsoft Copilot Studio, Windsurf, Claude Desktop, and any MCP-compliant client via Custom in the MCP Configurator.
- Preferred auth is the Glean OAuth 2.1 authorization server with PKCE, using the company's SSO. User-scoped Client API tokens are a fallback and need MCP, AGENT, SEARCH, CHAT, DOCUMENTS, TOOLS, and ENTITIES scopes.
- Admins can create multiple MCP servers with distinct URLs and tool sets, deploy config with MDM, and sign users out of MCP sessions from the Admin UI.
- MCP usage is subject to FlexCredit terms. Source: https://docs.glean.com/glean-enterprise-flex-pricing

### Agent2Agent

Primary source: https://docs.glean.com/administration/platform/a2a-host

- The A2A host lets an Auto mode agent call a registered third-party agent over Agent2Agent v0.3. The external server must publish `/.well-known/agent-card.json`.
- Authenticated servers use OAuth 2.0 authorization code flow. Each user authorizes separately. API keys and client-credentials OAuth are not supported. Messages are text only.
- A Glean A2A server lets an external platform invoke Glean Assistant. A per-agent A2A endpoint publishes one Auto mode agent to external clients.

### Embedded integrations

Primary source: https://docs.glean.com/administration/platform/embedded-integrations/slackbot

- Glean in Slack (Gleanbot) answers questions when `@Glean` is mentioned or a question is detected, supports `/glean` search, can run Code Writer, and can send a daily digest DM.
- Slack answers are private to the asker unless Public Mode is on. Slack RTS fetches live messages at query time and does not index message content.
- Admins can configure channel bot responses, custom question detection, a Slack sidebar, announcements from Slack, Public Mode, daily digest, and permissions.
- Enterprise Flex lists the same entitlements for Glean in Slack, Zoom, Microsoft Teams, GitHub, and Miro as for Assistant. Source: https://docs.glean.com/glean-enterprise-flex-pricing
- Insights includes an embedded-integrations report for Glean in Zendesk, ServiceNow, and Service Cloud. Source: https://docs.glean.com/administration/insights/overview

### Browser extension

Primary source: https://docs.glean.com/user-guide/apps/extension-sidebar

- The extension sidebar adds Chat, Search, and Agents on indexed and unindexed pages. Open it with `⌘ + J` (Mac) or `Alt + J` (Windows), the toolbar icon, or a sticky tab.
- Supported browsers are Chrome, Edge, Firefox, Safari, and Brave.
- Users can screenshot page content they cannot copy and send it into Chat.
- The content tools can add or view Collections and Go Links for the current page.
- The Agents tab runs on Zendesk tickets, Salesforce Lightning cases, and ServiceNow incidents and cases (including CSM and HR). It replaces Glean Assist for those support workflows. Admins can feature agents and enable automatic runs.
- Users can set Glean as the new-tab page from Settings. Source: https://docs.glean.com/user-guide/about/end-user-quick-start-guide
- IT can deploy the extension to managed devices. The sidebar page points to that admin deployment guide.

### Glean companion

Primary source: https://docs.glean.com/user-guide/apps/glean-companion

- Companion is a floating extension widget on highlighted text. Actions are Explain, Find related documents, Find experts, Improve writing, Summarize this, and Translate (13 languages).
- It reads page content only when the user highlights text and invokes it. Users can hide it per site or turn it off in sidebar settings.
- It is enabled by default on a documented list of workplace domains. Extra permissions extend it to all pages.

### Glean for Desktop

Primary source: https://docs.glean.com/administration/management/features/glean-for-desktop

- Desktop provides spotlight-like search and chat from any application on macOS and Windows. Quick entry defaults to `Cmd+Shift+J` / `Ctrl+Shift+J`.
- Downloads are DMG or PKG on macOS and x64 or ARM64 on Windows. The Mac App Store build is deprecated.
- Settings include a custom shortcut, hiding the menu bar or Dock icon, and opening quick-entry results in the browser.
- The app does not search local files. MDM deployment is documented for Jamf, Kandji, and Intune.
- Users can attach a screenshot for visual context. Source: https://docs.glean.com/user-guide/about/end-user-quick-start-guide

### Mobile

Primary source: https://docs.glean.com/administration/management/features/mobile

- iOS and Android apps provide Search and Assistant. Bundle ID is `com.glean.app`.
- Apps integrate Microsoft Intune App Protection (MAM) without full device enrollment, including Edge sign-in for Conditional Access.
- There is no Admin Console toggle to disable mobile. Organizations restrict access through the IdP or MDM.

### Meeting notes

Primary source: https://docs.glean.com/user-guide/assistant/meeting-notes

- Meeting notes is a desktop companion for Google Meet, Microsoft Teams, Zoom, Slack huddles, and in-person meetings. No bot joins the call. Transcription uses local microphone and system audio.
- During a meeting, users can take notes, ask chat questions against the live transcript, and use Catch me up for the last two minutes (transcript only).
- After the meeting, Glean stores a transcript, a summary with decisions and action items, and related artifacts. Notes are indexed for Assistant, search, and agents, private to the user by default.
- Glean does not store raw audio. Transcript retention is admin-configurable and cannot exceed chat-history retention.
- Docs describe it as generally available to Glean Key customers on the desktop app, with admin rollout for all users, admins only, or off.
- Usage is billed in FlexCredits. Summary templates and manual transcript-language lock are not supported.

### Library and knowledge

Primary source: https://docs.glean.com/user-guide/assistant/assistant-library

- Library is where users browse artifacts they created and content shared with them. Tabs include Artifacts, Projects, Meeting notes, Go Links, and More (Answers and Announcements).
- Artifact types include Audio, Documents, Emails, Images, Interactive, Messages, Slides, and Spreadsheets. Content is private until shared.
- Share options are restricted people, anyone at the company with a link, or company-wide discovery in Search and Library.
- Library replaces the former Content item in the left navigation. Created content stays until deleted. Standard chat replies follow chat retention.
- Projects keep related chats, documents, and artifacts in one workspace. The Collections docs state that Projects are replacing Collections and that existing Collections migrate with content and permissions. Source: https://docs.glean.com/user-guide/knowledge/collections/how-collections-work
- Collections group related indexed documents and external URLs under one topic, appear on search results, support `app:collections`, and can nest as subcollections.
- Go Links are `go/name` bookmarks. They need the browser extension or DNS redirection (`go.glean.com` or a custom domain). Names ignore punctuation differences. Variable and appending Go Links are supported. Source: https://docs.glean.com/user-guide/knowledge/go-links/how-go-links-work
- Admins manage Answers, Announcements, Collections, Go Links, and Pins from User-generated content. Moderator roles can be scoped to one content type. Pins are created from a search result. Source: https://docs.glean.com/administration/management/user-generated-content
- The home page can show a Mentions card for tags and assignments across connected apps. Admins can set default left-nav items, branding, and home-page cards. Source: https://docs.glean.com/user-guide/about/end-user-quick-start-guide

### People and identity

Primary source: https://docs.glean.com/administration/identity/roles/about

- RBAC includes Setup Admin, Admin, and Super Admin, plus Member with optional Moderator privileges. Only Admin and Super Admin can manage RBAC.
- Roles can attach to individual users or identity-provider groups. Group members inherit roles from Azure AD, Google Workspace, or Okta.
- Setup Admins configure SSO, connect sources such as M365, Google, GitHub, and Atlassian, and start crawls. Admins manage workspace settings, roles, and feature enablement. Super Admins access security tooling such as Sensitive Content Search and DLP, and that role requires written authorization from the company's CISO or security manager.
- Members with Moderator permissions can manage content in specific features but cannot open the Admin Console.
- Insights employee and signup counts come from people data on the admin People page and the org chart. Source: https://docs.glean.com/administration/insights/overview
- Enterprise Flex seats include an unlimited People Directory with people, teams, and org charts. Source: https://docs.glean.com/glean-enterprise-flex-pricing

### Admin Console

Primary source: https://docs.glean.com/administration/about

- The Admin Console is the self-serve control plane for SSO, connectors, search visibility, generative AI setup, roles, and adoption.
- Admin Chat is an admin-only widget that answers from public Help Center, developer docs, and Gleaniverse. It does not read tenant content or change settings.
- The tenant backend domain is `tenant_id-be.glean.com`.
- Audit logs capture admin and internal-support configuration changes and can export to CSV or a SIEM. Customer Event logs record searches, chats, workflow runs, and citation clicks. Source: https://docs.glean.com/security/security-principles
- Admins enable Deep Research, data analysis, meeting notes, scheduled triggers, and content triggers from Assistant or Agents settings. Sources: https://docs.glean.com/user-guide/assistant/deep-research, https://docs.glean.com/administration/assistant/data-analysis/about-data-analysis, https://docs.glean.com/user-guide/assistant/meeting-notes, https://docs.glean.com/agents/concepts/schedule-triggers, https://docs.glean.com/agents/concepts/content-trigger
- MCP authentication prefers the Glean OAuth 2.1 authorization server with PKCE, using the company's SSO, with user-scoped Client API tokens as a fallback. Source: https://docs.glean.com/administration/platform/mcp/about

### Model Hub

Primary source: https://docs.glean.com/administration/configure-llms

- Admins choose which models appear in Assistant and Agents under Glean Universal Model Key or Customer Key (BYOK).
- Universal Key uses per-model toggles grouped by creator. Open models use one switch per creator region. Glean selects defaults.
- Customer Key groups toggles by hosting provider: Azure OpenAI, Amazon Bedrock (self-hosted AWS), Google Vertex AI (self-hosted GCP), OpenAI, and Anthropic. Admins set defaults. Image-generation defaults may use a different provider.
- Individual agents and steps can override the organization default model.
- Admins can exclude or restrict models to specific departments. Source: https://docs.glean.com/administration/configure-llms
- Open models are controlled with one switch per creator region rather than model by model.
- Feature availability for Assistant capabilities differs by Glean Universal Model Key versus Customer Key and by cloud. The configure-LLMs page points to a feature-availability matrix.

### Protect and security

Primary source: https://docs.glean.com/administration/protect/overview

- Every deployment includes an isolated cloud (AWS, Azure, or GCP), Glean-hosted or customer-hosted options, permission enforcement, zero LLM data retention and no training on enterprise data, SSO, RBAC, encryption in transit and at rest, audit logs, and regional data residency.
- Documented certifications on this page include ISO 42001, SOC 2 Type II, and ISO 27001. The product homepage also lists HIPAA, TX-RAMP Level 2, and GDPR. Source: https://www.glean.com/
- Glean Protect includes inclusion/exclusion indexing rules and one-time sensitive-content CSV reports with manual hide-via-CSV remediation.
- Protect+ is a separately licensed add-on. It adds continuous scanning across 100+ sources, dashboards and API, automated hiding of overshared sensitive content in AI surfaces, classifiers, email summaries, prompt-injection and toxic-content guardrails, restricted topics, and partner integrations (Palo Alto Networks and Tines). Agent alignment models that check tools before execution are beta.
- Only Super Admins and Sensitive Content Moderators can open Protect findings.
- Permission mirroring applies to search, AI answers, agents, MCP, and embeds. An agent run uses the triggering user's permissions unless a service credential is attached. Source: https://docs.glean.com/security/security-principles
- Compliance reports live in the Glean Trust Portal under NDA. A bug bounty runs on Bugcrowd. Source: https://docs.glean.com/security/

### Insights

Primary source: https://docs.glean.com/administration/insights/overview

- Insights is limited to the Insights Moderator role. Overview metrics include coverage (signups / employees), activity (MAU / signups), and stickiness (WAU / MAU), plus search, Assistant, and agent-run counts.
- A user is active when they search, open results, create or view knowledge objects, chat, use summarization, engage Gleanbot, or call user-initiated Search, Chat, or Summarization APIs. Viewing the home page alone does not count.
- MAU is a trailing 28 days, WAU 7 days, DAU the previous UTC day. The dashboard retains 270 days.
- Other tabs include Assistant insights, Agents insights, Departments and Managers, embedded-integration usage, Insights chat (natural-language analytics, 270 days), LLM insights, and MCP insights.
- Skill adoption has no built-in dashboard. Use Glean Customer Event logs (`WORKFLOW_RUN`, `CLIENT_EVENT`) or an account-team export.

### Developer platform

Primary source: https://developers.glean.com/

- The developer portal documents Chat, Search, Agents, a Web SDK, and an Indexing SDK. Platform APIs for search, agents, skills, and chat are described as rolling out in experimental preview.
- Client libraries are `glean-api-client` (Python), `@gleanwork/api-client` (TypeScript), Java, and Go.
- The Web SDK (`@gleanwork/web-sdk`) renders permission-aware search box, results, and chat in other apps.
- The Indexing SDK builds custom connectors that push documents, users, groups, and ACLs. Push API connectors cover custom, self-hosted, or firewalled sources. Source: https://docs.glean.com/connectors/about
- An agent toolkit exposes Glean retrieval as tools for LangChain, CrewAI, and similar frameworks.
- Client Search, Chat, and Agents APIs consume FlexCredits. Platform, admin, indexing, connector, and tools APIs are listed as unlimited on Enterprise Flex. Source: https://docs.glean.com/glean-enterprise-flex-pricing
- On some deployments, POST `/api/search`, GET `/api/search/filters`, and POST `/api/chat` no longer require an experimental header. That change is private beta. Source: https://docs.glean.com/release-notes/releases/2026-09-15-september-release

### Billing and usage

Primary source: https://docs.glean.com/glean-enterprise-flex-pricing

- Enterprise Flex combines per-user seats with a pooled FlexCredit allowance. Extra FlexCredit packs can be purchased. Seats and credits are discounted when the customer supplies LLM keys or self-hosts.
- Fast Mode queries are unlimited on seats. Thinking and Adaptive queries with standard models include up to 100 per user per week; excess and premium-model queries consume FlexCredits. A Thinking query over 30 FlexCredits counts as multiple queries.
- Metered items include Code Writer, slide generation, Deep Research, meeting notes, voice sessions, image generation, memory (per monthly active user), and agent runs. Basic search from Assistant is unlimited; the Search API costs 1 FlexCredit per query.
- Agent creation, testing, and sharing are unlimited. Agent runs consume FlexCredits, including Assistant queries that route to an agent.
- Protect+ and Premium Support (24x7, 1-hour critical SLA) are site-wide annual add-ons.
- Models are tiered Basic, Standard, and Premium. The rate card lists families including Glean Waldo, OpenAI, Gemini, Anthropic, Amazon Nova, and open models hosted by Fireworks or Baseten.
- Admins set organization, user, team, and agent usage limits and alerts, and can block usage until the next calendar month. On Flex, basic chat can continue after a limit while premium models are blocked. Source: https://docs.glean.com/administration/management/usage/set-usage-limits-and-alerts
- Usage dashboards differ for Enterprise Flex (FlexCredits) and Glean Core Suite (Model Hub dollar cost). Legacy Enterprise plans no longer show the Flex dashboard. Source: https://docs.glean.com/administration/management/usage/flexcredits-dashboard

## Sources

- https://docs.glean.com/
- https://docs.glean.com/user-guide/about/what-is-glean
- https://docs.glean.com/user-guide/about/end-user-quick-start-guide
- https://docs.glean.com/user-guide/assistant/glean-chat/
- https://docs.glean.com/user-guide/assistant/how-glean-accesses-info
- https://docs.glean.com/user-guide/assistant/glean-chat/search-and-autocomplete
- https://docs.glean.com/user-guide/assistant/deep-research
- https://docs.glean.com/user-guide/assistant/skills
- https://docs.glean.com/user-guide/assistant/memory-personalization
- https://docs.glean.com/user-guide/assistant/code-search
- https://docs.glean.com/user-guide/assistant/meeting-notes
- https://docs.glean.com/user-guide/assistant/assistant-library
- https://docs.glean.com/user-guide/apps/extension-sidebar
- https://docs.glean.com/user-guide/apps/glean-companion
- https://docs.glean.com/user-guide/knowledge/go-links/how-go-links-work
- https://docs.glean.com/user-guide/knowledge/collections/how-collections-work
- https://docs.glean.com/administration/search/about
- https://docs.glean.com/agents/how-agents-work
- https://docs.glean.com/agents/auto-mode-agent
- https://docs.glean.com/agents/independent-agents
- https://docs.glean.com/agents/concepts/agent-library
- https://docs.glean.com/agents/concepts/triggers
- https://docs.glean.com/agents/concepts/content-trigger
- https://docs.glean.com/agents/concepts/schedule-triggers
- https://docs.glean.com/agents/templates
- https://docs.glean.com/connectors/
- https://docs.glean.com/connectors/about
- https://docs.glean.com/administration/tools
- https://docs.glean.com/administration/assistant/features/code-writer
- https://docs.glean.com/administration/assistant/data-analysis/about-data-analysis
- https://docs.glean.com/administration/platform/mcp/about
- https://docs.glean.com/administration/platform/a2a-host
- https://docs.glean.com/administration/platform/embedded-integrations/slackbot
- https://docs.glean.com/administration/management/features/glean-for-desktop
- https://docs.glean.com/administration/management/features/mobile
- https://docs.glean.com/administration/management/user-generated-content
- https://docs.glean.com/administration/management/usage/set-usage-limits-and-alerts
- https://docs.glean.com/administration/management/usage/flexcredits-dashboard
- https://docs.glean.com/administration/about
- https://docs.glean.com/administration/identity/roles/about
- https://docs.glean.com/administration/agent-identity/overview
- https://docs.glean.com/administration/configure-llms
- https://docs.glean.com/administration/protect/overview
- https://docs.glean.com/administration/insights/overview
- https://docs.glean.com/security/
- https://docs.glean.com/security/security-principles
- https://docs.glean.com/glean-enterprise-flex-pricing
- https://docs.glean.com/release-notes/releases/2026-09-15-september-release
- https://developers.glean.com/
- https://www.glean.com/
