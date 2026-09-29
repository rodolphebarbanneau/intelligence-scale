---
name: Replit Agent
slug: replit
url: https://replit.com/
docs: https://docs.replit.com/
kind: product
reviewed: 2026-09-28
---

# Replit Agent

## Product

Replit Agent is the AI that builds and changes work on Replit from plain language. Official documentation is at https://docs.replit.com/. The docs describe Agent as a partner that sets up a project, writes code, checks its work, and fixes problems. A person describes an app, design, slides, video, document, or other outcome; Agent plans, implements, tests, and publishes. The docs say no code or technical knowledge is required for that path.

Replit is the chassis Agent runs in. People sign in on the web at replit.com, in the Desktop App for macOS and Windows, or in the Mobile App for iOS and Android. Agent also runs from ChatGPT, Claude, Slack, and any MCP client that connects to the Replit MCP Server. Work lives in a Workspace: a Personal Workspace for solo projects, or a Team Workspace on paid plans for shared projects, settings, integrations, and billing.

Use starts in Chat or in a Project. A chat is a private thread for questions, research, Routines, and describing an outcome. When the work becomes a substantial build or design, the chat can become a Project. A Project holds code, data, and artifacts — web apps, mobile apps, dashboards, slide decks, animations, 3D games, and designs. Agent chats in the Project Editor, writes files, sets up infrastructure, and publishes artifacts together.

Plans split what Agent can do. Starter includes daily Agent credits, Design Canvas, Visual Editor, and one published app that goes down after 30 days. Core adds paid Agent modes, intelligent model routing, Plan Mode, connectors, all artifact types, one active background task, five collaboration seats, and unlimited published apps. Pro raises background tasks to ten, seats to fifteen, and adds tiered credits with two-month rollover, priority support, and a 28-day database recovery window. Enterprise adds SSO and SCIM, organization governance, audit logs, warehouse connectors, unlimited seats, and a dedicated support team. Enterprise workspaces use one Auto mode instead of Free Mode; account admins manage which models are allowed.

There is no separate sibling product spec for Replit Chat, Replit Design, or Replit publishing. Those surfaces are part of this product.

## Features

### Replit Agent

Primary source: https://docs.replit.com/features/agent/overview

- Agent takes a plain-language description, sets up the project, writes code, checks its work, and fixes problems.
- In the Project Editor, a person chats to build an app, ask a question, research a topic, or pull data from connected services such as BigQuery, Slack, or Notion.
- A person can optionally select a project type — web app, mobile app, slides, design, data visualization, and more — or leave Agent to choose the setup.
- Agent writes code, sets up infrastructure, and tests the result. After the project exists, the person can switch Agent modes.
- A project can hold more than one output. A person can start with a web app and later add a mobile app, slides, or a video that share the same backend.
- Documented outputs include web apps, mobile apps, data dashboards, AI-powered tools, visual designs on the Design Canvas, files and documents (CSVs, PDFs, PowerPoint, Markdown), and connected-service queries from chat.
- Agent creates checkpoints as it works. A person can roll back to a previous state or describe a mistake and ask Agent to fix it.
- Agent chat and building, Free Mode, intelligent model routing, Power, Max, Design Canvas, and multi-artifacts are listed as available on Core and Pro.
- Core allows one active background task. Pro allows ten.
- Enterprise workspaces use one Auto mode instead of Free Mode. Auto chooses the mode and an allowed model for each task. Account admins manage model access with Enterprise model controls.

### Plan Mode

Primary source: https://docs.replit.com/features/agent/plan-mode

- Plan Mode lets a person ask questions, brainstorm, and plan with Agent before Agent changes the app's code or data.
- With the Plan toggle off, Agent builds directly. The docs also call that Build mode.
- Plan Mode is available while building a Replit App with Agent. It is not available directly from Conversations.
- Agent generates an ordered task list from the requirements. The person can review it, select Revise, Cancel, Build here, or Build in background.
- Build here implements the plan in the current Agent session. Build in background runs it as a separate task.
- Background tasks wait for review and apply by default. A person can enable Automatically apply changes in the background build options.
- Before the project's first checkpoint, the approval button is Start building.
- Plan Mode uses the same effort-based pricing as other Agent interactions. Planning, guidance, and task lists are billed.
- Plan Mode requires Core or Pro. Source: https://docs.replit.com/billing/plans/starter-plan

### Agent Modes

Primary source: https://docs.replit.com/features/agent/agent-modes

- Agent modes are Free Mode, Power Mode, and Max Mode. A person opens the Agent settings dropdown in the prompt box to choose one.
- Economy Mode is no longer available. Power Mode replaces it at the same price.
- Free Mode is no-cost everyday Agent work within the plan's allowance. It always uses intelligent model routing. A person cannot select a model manually in Free Mode.
- Core and Pro Free Mode allowances reset every five hours and have weekly limits. Starter keeps its existing limits. Usage is in Settings → Usage. Source: https://docs.replit.com/features/agent/overview
- If a request needs more than Free Mode, Agent may offer a paid Allow once option. Replit asks for confirmation before a paid action starts, then Agent returns to Free Mode. Source: https://docs.replit.com/features/agent/overview
- Power Mode is a paid mid-tier mode. Max Mode is a paid top-tier mode for complex work, larger codebases, and harder problems.
- In Power or Max, Core and Pro builders can select Auto so Replit chooses a model up to that mode's capability, or choose a model manually.
- Enterprise workspaces use one Auto mode instead of Free Mode. Enterprise Auto can choose both the mode and an allowed model.
- Routines run in Power or Max Mode and require a per-run budget. They cannot run in Free Mode.
- ⌘+Shift+I (Ctrl+Shift+I on Windows) cycles modes. The shortcut is inactive while Auto is on.
- Agent settings are per person, not per project: mode, primary model and Effort, Plan Mode, auto-merge for background tasks, and auto-approve for plans.
- Starter includes Agent chat and Free Mode with a daily cap. Full build, paid modes, intelligent model routing, Plan Mode, connectors, and all artifact types require Core or Pro. Source: https://docs.replit.com/billing/ai-billing

### Model selector

Primary source: https://docs.replit.com/features/agent/model-selector

- Intelligent model routing chooses a model per task. When the product shows Auto, Replit is routing.
- Core and Pro builders can choose an available primary model in Power Mode or Max Mode. The list in the product is the source of truth; availability can vary by rollout, organization settings, and authorization.
- Documented Power Mode models include GPT-6 Sol, GPT-6 Luna Fast, Claude Sonnet 5, and Claude Sonnet 4.6.
- Documented Max Mode models include GPT-6 Astra, Claude Fable 5.1, Claude Opus 5.5, Claude Opus 4.8, Claude Opus 5, Claude Opus 5 Fast, and Kimi K3.
- Fast model variants require a Pro or Enterprise plan.
- Effort is a per-model control from Low through Max. Higher Effort can take longer and cost more. Agent applies extra reasoning selectively on harder work.
- Compare models is in beta. It runs the next prompt across up to four models at once and is only supported with Chat. Each model in a comparison uses credits.
- Build and Design keep separate model selections.

### App Testing

Primary source: https://docs.replit.com/features/agent/app-testing

- App Testing lets Agent test the apps it builds in a real browser. Agent clicks through the UI, enters mock data, reports results, and fixes issues it finds.
- When enabled, Agent decides when enough has changed to test. It does not test after every user message.
- App Testing is available for Full Stack JavaScript and Streamlit Python web applications.
- The live browser appears inside the background task. After the run, a recording is in the same task view.
- App Testing lives in Advanced settings in the Agent settings dropdown. Turn it on in Power Mode or Max Mode. Free Mode keeps it off.
- If Agent hits a roadblock such as a login, it shows Begin take over. Skip ends testing if Agent cannot continue. After 10 minutes with no response, Agent continues as if Skip was pressed.
- App Testing is billed as part of Agent's effort-based pricing.

### General Agent

Primary source: https://docs.replit.com/features/agent/general-agent

- General Agent starts without a pre-selected artifact type. A person can create a CSV or PDF, research a topic, query connectors, or build a full app from the same chat.
- Access it by selecting General on the Replit home page, by chatting in any existing project, or by importing from GitHub, which gets General Agent automatically.
- Connectors named on this page include BigQuery, Linear, Slack, Notion, Amplitude, Segment, and Hex.
- General Agent sets up its own environment and run commands. A person may need to ask it to configure publishing.
- Each chat is contained in a single project. Projects do not talk to each other.
- General Agent is listed as available on Core and Pro, and the page also says it is available to all users.

### Tasks

Primary source: https://docs.replit.com/features/agent/task-lifecycle

- Every Agent task moves through Draft, Active, Queued, Ready, Applying, and Done.
- A Draft holds a title, description, and plan. A person can start it, ask Agent to revise, or archive it.
- An Active task runs in an isolated copy of the project. The main version stays unchanged until the person applies the work.
- A Queued task waits when it depends on another task or when the plan's active background-task limit is reached. It starts when a slot opens.
- A Ready task is finished but not applied. The person reviews the work log, test results, and preview, then applies or dismisses it.
- Agent handles conflicts automatically when applying changes from multiple tasks.
- Archive is available for Drafts and is reversible from Done. Cancel is available after a task has started building and is not reversible.
- The task board shows Drafts, Active (including queued), Ready, and Done columns. A person can search by title or task number, filter drafts, rename tasks, and bulk-manage drafts. Source: https://docs.replit.com/features/agent/task-board
- Each task has settings for auto-apply changes, auto-approve plan, apply changes, rename, review changes, and cancel. Auto-apply and auto-approve are one-time actions. Source: https://docs.replit.com/features/agent/task-board
- After a task is applied, Agent suggests follow-up tasks. Start sends a suggestion to the background; View plan inspects it first. Closing the dialog cancels the suggestions. Source: https://docs.replit.com/features/agent/follow-up-tasks

### Agent capabilities

Primary source: https://docs.replit.com/features/agent/web-search

- Web Search is built in. Agent searches the web, fetches page content, and shows source citations. A person can nudge it with words such as search or research.
- Image generation is built in. Agent creates images from descriptions, can produce transparent PNGs, saves files into the project, and updates code to reference them. The docs say it is powered by Google's Imagen 4. Source: https://docs.replit.com/features/agent/image-generation
- Audio generation creates music, sound effects, and speech, saves the files, and wires them into the app. It is billed at the provider's rate against Replit credits. The docs say it is powered by ElevenLabs. Source: https://docs.replit.com/features/agent/audio-generation
- Voice Mode transcribes speech into the chat box for review before send. It does not read Agent replies aloud. Recording lasts up to 6 minutes and stops after about 30 seconds of silence or when the tab is backgrounded. It is available on all plans in the Project Editor and on the home-screen Agent prompt, on desktop web, mobile web, and the mobile app. Source: https://docs.replit.com/features/agent/voice-mode
- Steer sends a follow-up into the active turn. Queue saves it for the next turn. Steer is the default in chats and Projects; Design mode always steers. Preferences live in Settings > Personalization > Agent. Cmd+Enter or Ctrl+Enter sends the opposite behavior. The queue drawer supports steer now, edit, delete, reorder, and add. Queued messages process automatically only while an active Project Editor session is connected. Stop interrupts the current turn. Source: https://docs.replit.com/features/agent/steer-and-queue-messages

### Agent Skills

Primary source: https://docs.replit.com/features/agent/skills

- A skill is a folder with a `SKILL.md` file and optional supporting files. Project skills live in `/.agents/skills` and follow the Agent Skills open standard.
- Agent sees every installed skill's name and description, and loads the full body only when the task is relevant.
- Pre-defined skills are available from the Use a skill picker and the new-project starting-point picker without installation.
- Skills can be project-level or workspace-level. Workspace skills are managed in Workspace Settings.
- Workspace member access policies are Required, Available, and No access. A new custom skill starts as Private.
- Skills can be imported from a public GitHub repository, folder, or file URL. Each import is limited to 50 skills, 3,500 files, or 200 MiB. Private repositories are not supported.
- Custom instructions are always-on workspace guidelines injected on every project and session. Skills load only when relevant. Custom instructions are available on Pro and Enterprise; skills are available on all paid plans. On Enterprise, only admins manage them. On Pro, any workspace member can. On Core, members can manage skills; custom instructions are not available. Source: https://docs.replit.com/features/agent/agent-customization
- A person can attach a skill to a message, install one in a project, type `/` plus the skill name, or ask Agent to draft a skill and upload the zip to the workspace. Source: https://docs.replit.com/features/agent/agent-customization
- The skills directory lists Replit-built skills (sales, career, research, finance, documents, creative, productivity, security, quality) and partner skills for Stripe, PayPal, RevenueCat, Mixpanel, BigQuery, Resend, Google Workspace, Atlassian, and Google Maps. Skills in the Replit picker are audited; external skills are not. Source: https://docs.replit.com/features/agent/skills-directory

### Memories

Primary source: https://docs.replit.com/chat/memories

- Memories let Replit retain context across chats and Projects. Replit can write Memories while a person works.
- Settings → Customization → Memory is where a person opts in, turns Memory off, chooses collaborator sharing, and edits the Memory file.
- Memories are private by default. Collaborator sharing is off by default.
- User memory belongs to one builder and workspace. Project memory stays with one Project. Custom memory follows its own access settings.
- The docs say Memories do not retain personal or sensitive information, credentials, or project-confidential facts. Explicit requests and Custom Instructions take priority over memory.

### Chats

Primary source: https://docs.replit.com/features/conversations-and-routines/conversations

- A chat is a single thread for questions, exploration, Routines, and describing an outcome. Every task in Replit starts with a chat.
- Chats are private. Only the owner can access them in the Workspace. For collaboration, Replit creates a Project.
- A chat can research the web, connected tools, and uploaded files; run a Routine; or turn an idea into an app, presentation, or design.
- Background tasks are not available in chats. Routines are available in chats and not in Projects. Integrations are available in both.
- A chat can become a Project when the work becomes a substantial build or design.
- Chat can use uploaded documents, spreadsheets, images, screenshots, connected tools, and a Figma frame as context. Source: https://docs.replit.com/chat/overview

### Routines

Primary source: https://docs.replit.com/chat/routines

- A Routine schedules recurring work from a chat and returns each result to that thread.
- Routines are available on Core, Pro, and Enterprise. They are not available on Starter.
- Schedules can be hourly, daily, or weekly, at intervals of one hour or more. Replit uses the device time zone when the person confirms the schedule.
- Routines default to deterministic code for predictable tasks and bring in Agent when the work needs reasoning.
- A Routine can gather information from connected tools, create projects or tasks in connected services, and send messages. It cannot schedule publishing.
- A Routine remains personal. It inherits the chat's permissions and connected-tool access.
- If other work is running when a Routine is due, the Routine waits. Replit does not add another pending run for the same Routine.
- Core allows up to five active Routines per user. Pro allows up to ten.
- Routines run in Power or Max Mode, not Free Mode. Core and Pro set a per-run budget. Enterprise Routines do not have a per-run budget. A run can go slightly over if a step is already in progress.
- The Routines sidebar lists schedules, status, and run history. A person can run a Routine now or delete it.

### Connectors

Primary source: https://docs.replit.com/features/integrations/overview

- Agent integrations are Replit managed, Connectors, External integrations, and Agent services.
- Replit-managed integrations include Replit Database, Replit App Storage, Replit Auth, and Replit Domains. They work without extra setup.
- Connectors are first-party integrations. A person signs in once on the Connectors page; connections persist across apps on that Replit account.
- Most connectors require Core, Pro, or Enterprise. The catalog in the workspace shows what the current plan allows. Free-plan builders can use Replit-managed integrations.
- Documented connector groups include Google Workspace, Microsoft 365, developer tools (GitHub, GitLab, Bitbucket, Linear, Jira, and others), cloud storage, communication (Slack, Discord, Gmail-related mail APIs, Twilio, Zoom), CRM, HR, payments (Stripe, Square, Plaid, Shopify, RevenueCat), AI and media, data and analytics, marketing and social, maps, and productivity (Notion, Airtable, ClickUp, and others).
- Slack can search messages, read private channels and DMs the connected account can access, send messages as the person, and manage Slack canvases.
- When a person asks for a capability without naming a provider, Agent shows a short list of fitting connectors.
- External integrations such as OpenAI, Gemini, Anthropic, Perplexity, Mistral, OpenRouter, Workato, HubSpot, and Discord are set up with API keys stored in Secrets.
- Agent services (Brave Image Search, ElevenLabs, Google Gemini image generation / Nano Banana) use paid third-party APIs with no API keys. Usage is billed at the provider rate against Replit credits.
- Custom connectors are in beta for Pro and Enterprise. A workspace admin adds a public HTTPS REST API with name, description, base URL, Agent instructions (500-character limit), and authentication, then can test a GET endpoint. Source: https://docs.replit.com/features/integrations/custom-connectors
- Enterprise can bring its own OAuth app for a connector, with Client ID, Client Secret, scopes, and callback `https://replit.com/connectors/oauth/callback`.
- On Core and Pro, the account admin manages connectors for a collaborative workspace. On Enterprise, management is organization-wide, with group access, custom OAuth clients, API-key access controls, and an option to bring your own OpenAI key. Source: https://docs.replit.com/replitai/managing-connectors
- Warehouse connectors for BigQuery, Databricks, Snowflake, and Microsoft Fabric (private preview) are Enterprise. Segment, Amplitude, and Hex analytics connectors are on Core, Pro, and Enterprise. Source: https://docs.replit.com/connectors/warehouses/overview

### MCP

Primary source: https://docs.replit.com/features/mcp/overview

- Agent connects to external tools through MCP. Pre-listed servers install with one click. A custom MCP server can be added.
- Documented listed servers include Airtable, Amplitude, Apollo, Atlassian, Figma (built in — paste a Figma link), Linear, Notion, Stripe, Supabase, Twilio, Zapier, and others on the page.
- All MCP traffic passes through Replit's security scanner, which can block unsafe tools before they run.
- Authentication options are OAuth dynamic client registration and custom headers.
- An install link can add a server via `https://replit.com/integrations?mcp=` plus a base64 JSON payload.
- The Replit MCP Server URL is `https://replit-mcp.com/server/mcp` over Streamable HTTP with OAuth. Tools include `create_app_from_prompt`, `search_apps`, `resolve_app_by_name`, `list_apps`, `ask_question`, `update_app_using_prompt`, `publish_app`, and `get_publish_status`. `app_stack` values include `react_website`, `mobile_app`, `design`, `slides`, `animation`, `data_visualization`, `3d_game`, `document`, and `spreadsheet`. Source: https://docs.replit.com/platforms/mcp-server

### Projects and artifacts

Primary source: https://docs.replit.com/features/projects-and-artifacts/projects

- A Project is the container for code, data, and artifacts. Agent sets up the project and builds artifacts inside it.
- Artifact types on the Projects page are web app, mobile app, data visualization, slide deck, animation, 3D game, and design.
- Publishing pushes the entire project live at once. All artifacts go live together.
- The Projects page lists created and invited projects, shows artifact icons, filters by build type, sorts by last opened, and supports private pins.
- An artifact is a publishable output with its own shareable URL. Files such as CSVs, images, and Markdown support artifacts but cannot be published alone. Source: https://docs.replit.com/features/projects-and-artifacts/artifacts
- A project can hold up to 7 artifacts, with a maximum of 1 mobile app. Artifacts in the same project share backend and data. Source: https://docs.replit.com/features/projects-and-artifacts/artifacts
- Add an artifact from chat, the + button in the preview panel, or the Library sidebar. Switch artifacts in the preview panel, the Library, or by asking Agent. Source: https://docs.replit.com/features/projects-and-artifacts/artifacts

### Artifact types

Primary source: https://docs.replit.com/features/artifact-types/web-apps

- Web apps are the default output. Agent builds a full-stack app with frontend, backend, API routes, and a database as needed. Apps are responsive. Publish is one click.
- Native mobile apps are React Native and Expo. Preview uses an iOS Simulator or Android Emulator in the Project Editor (Core, Pro, and Enterprise; not in Firefox) or Expo Go on a phone. Hardware features such as camera, haptics, push notifications, and GPS need a real device. Source: https://docs.replit.com/features/artifact-types/building-mobile-apps
- iOS publishing uses a guided flow to TestFlight and the App Store and requires an Apple Developer Program membership. Google Play publishing is not supported by Replit. Native iOS work is done in the Project Editor at replit.com, and in the Android Replit app where supported. Source: https://docs.replit.com/features/artifact-types/building-mobile-apps
- Data visualizations, slide decks, and animated videos (export as MP4) are documented artifact types. Slide decks and videos can be published with their own URLs. Source: https://docs.replit.com/features/projects-and-artifacts/artifacts

### Replit Design

Primary source: https://docs.replit.com/design/what-is-replit-design

- Replit Design generates interactive mockups from a prompt, a template, an import (Figma, Claude, a site URL, or a screenshot), or a saved design system.
- Explore creates new frames from suggestions or by switching the Design model.
- Refine uses Agent chat, the Visual Editor (simple edits apply to source code without credits), Draw markup that Agent reads, and generated images, video clips, and vector graphics.
- Build your design turns a frame into a new working app. Restyle applies a frame's look to an existing app. Building a new app from a design frame requires Core or Pro; other Design capabilities work on every plan.
- A design system captures tokens, colors, typography, and components. New work can start from it, and existing apps can be restyled to match.

### Project Editor

Primary source: https://docs.replit.com/features/editor/editor-and-tools

- The Project Editor is the development environment: windows, panes, and tabs for the file editor, Preview, Agent, and other tools.
- The file tree lists project files. The tools dock opens Project Editor tools. The Run button runs the selected workflow.
- Search finds files, text, or tools. The resources panel shows RAM, CPU, and storage.
- Agent automatically creates `replit.md` in the project root and includes it in context for architecture, coding patterns, and preferences. A person can edit it. It must live in the project root. Source: https://docs.replit.com/features/project-setup/replit-dot-md

### Publishing

Primary source: https://docs.replit.com/features/publishing/overview

- The Publishing tool sets domain, access, production database, monitoring, security, and hosting. Open it from Replit Cloud in Tools or Publish in the Project Editor.
- Replit suggests a `.replit.app` name. A custom domain can be connected after publishing.
- Access options are Public, Password protected, Workspace only (Private), and Invite only (Private). Personal workspaces default to Public; organization workspaces default to a private option. Scheduled Deployments have no access options. Changing access requires unpublishing first. Source: https://docs.replit.com/features/publishing/private-deployments
- Monitoring can email the owner if the app goes down. A feedback widget can collect visitor reports for Agent. A security scan can run before publish. Publishing can be blocked when critical vulnerabilities are found.
- Deployment types are Autoscale (default; scales to zero), Static (files only; not compatible with Agent-built full-stack apps), Reserved VM (always on), and Scheduled (cron, no public URL). Source: https://docs.replit.com/features/publishing/deployment-types
- Machine configuration sets CPU, memory, and maximum machines. Deployment secrets sync from development. Geography is locked after the first publish; changing region requires a remix.
- Starter includes one published app for 30 days with a Made with Replit badge. Core and Pro allow unlimited published apps and badge removal. Source: https://docs.replit.com/billing/plans/replit-core

### Database

Primary source: https://docs.replit.com/features/data-and-storage/sql-database

- Replit Database is a managed SQL database in the Project Editor. Agent can add it, create the schema, and wire the app.
- The Database tool lists databases and has Overview, My Data, and Settings tabs. Apps include 20 GB of free storage.
- Agent-added databases use an ORM with schema validation and input sanitization.
- Development and production databases are separate. Development can restore to an Agent checkpoint. Production uses point-in-time restore. Pro extends the recovery window to 28 days versus 7 days on Core. Source: https://docs.replit.com/billing/plans/replit-pro

### Users and Auth

Primary source: https://docs.replit.com/features/auth-and-identity/overview

- Users & Auth, under Replit Cloud, lists people who have signed in and configures the login screen, providers, and session secret.
- Replit Auth is the zero-setup option: a prebuilt login page, user management, and sessions with Replit accounts.
- Clerk Auth is the option for custom sign-in flows, branding, and OAuth providers such as Google, GitHub, Apple, and X. Apps can add company SSO through Clerk.

### Security

Primary source: https://docs.replit.com/features/security/overview

- Package Firewall blocks malicious and compromised packages at install time. It is on by default, part of Auto-Protect, and powered by Socket. It covers npm, yarn, pnpm, pip, and Go modules. Source: https://docs.replit.com/features/security/package-firewall
- After install, automatic dependency scans detect new CVEs. Auto-Protect can prepare Agent patches. The severity threshold is in Settings > Account > Advanced.
- Before publish, Security Agent audits code, dependencies, and privacy. The Project Security Center reviews findings. A Level 3 black-box pen test reviews source and tests the running app.
- The Workspace Security Center scans projects across the workspace, shows CVEs by severity, and can export SBOMs.
- Publish > Advanced can block publishing of critical vulnerabilities.
- Replit hosts data primarily in GCP in the United States, with an optional India region. GCP is described as ISO 27001 and SOC 2 Type 2 certified. Replit states it has SOC 2 Type 2 attestation. Transit uses TLS 1.2+; data at rest uses AES-256. Source: https://docs.replit.com/teams/information-security/overview
- A Trust Center is linked from the information-security page. Vulnerability reports go to security@replit.com. Source: https://docs.replit.com/legal-and-security-info/security

### App Storage

Primary source: https://docs.replit.com/features/data-and-storage/object-storage

- App Storage is Replit's object storage, formerly Object Storage, powered by Google Cloud Storage.
- Agent can create buckets and generate upload, download, and access-control code. A bucket belongs to one project and cannot be shared across apps.
- The App Storage tool creates buckets, uploads and downloads objects, organizes folders, and shows a Bucket ID. JavaScript and Python SDKs authenticate automatically.

### Growth

Primary source: https://docs.replit.com/features/publishing/seo-agent

- SEO Agent, in the Growth pane, runs a technical SEO audit on a published app and offers one-click Agent fixes for crawlability, metadata, structured data, Open Graph tags, and semantic markup.
- It requires a published public web deployment and a paid plan. The Growth pane is locked until the app is published.
- An automatic Lighthouse SEO Rating after each publish labels the app Healthy, Needs Work, or Weak. Republishing after a fix refreshes the rating.

### Checkpoints

Primary source: https://docs.replit.com/features/version-control/checkpoints-and-rollbacks

- Agent checkpoints snapshot project files, AI conversation context, environment and publishing configuration, Agent memory of the project, and optionally database contents.
- Roll back restores that state. Database restore is optional and off by default. Production database restore is a separate point-in-time operation.
- A person can roll forward to a later checkpoint until new changes create an alternate history.
- Agent creates checkpoints at feature completion, major milestones, stable states, and before error recovery. Each checkpoint has a description, timestamp, and billing information.
- Checkpoints appear in the Agent tab, as Git commits in the Git pane, and in the Agent history view.

### Secrets

Primary source: https://docs.replit.com/core-concepts/project-editor/app-setup/secrets

- Secrets stores encrypted credentials as environment variables. Configurations store non-sensitive settings. Secrets use AES-256 at rest and TLS in transit.
- Secrets are available for all deployment types except Static Deployments. Production secrets are in Publishing → Adjust settings.
- Account secrets can be linked across projects the owner owns.
- Adding Replit Database creates a `DATABASE_URL` secret. Replit also sets `REPLIT_DOMAINS`, `REPLIT_USER`, `REPLIT_DEPLOYMENT`, and `REPLIT_DEV_DOMAIN`.
- Multiplayer collaborators and organization owners can see secret values. Remixers and non-owners generally see names but not values.

### Workspaces

Primary source: https://docs.replit.com/features/collaboration/workspaces

- A Workspace holds Projects, people, settings, shared resources, integrations, and billing.
- Every account has a Personal Workspace. The owner is the sole admin. Guests are invited to individual projects.
- Paid plans can create Team Workspaces. Members get access to all projects in the Workspace. The admin manages billing and settings. Pro Team Workspaces use pooled credits from the admin's account.

### Platforms

Primary source: https://docs.replit.com/features/platforms/desktop-app

- The Desktop App for Windows and Mac matches the web product and adds multitasking across apps, status signals when Agent needs attention or finishes, and tab previews. Work stays in sync with replit.com. Enterprise IT can distribute it through MDM.
- The Mobile App for iOS and Android supports Agent chat, editing, publishing, voice input, Live Activities, and notifications when Agent needs help, finishes, or there is a billing update. Supported devices include iPhone and iPad on iOS 18+, Mac on macOS Tahoe+, and paired Apple Watch. Native iOS app work is done on replit.com. Pro cannot be purchased in the mobile app. Source: https://docs.replit.com/features/platforms/mobile-app
- Replit in ChatGPT connects via Settings → Apps & Connectors or from a conversation. Invoke with `Replit,`, `/Replit`, or the composer menu. Agent creates, updates, and inspects one app per conversation and publishes it. Starter ChatGPT apps are public only. Work is billed as Replit Agent usage. Regional availability is all regions outside the EU. Source: https://docs.replit.com/features/platforms/chatgpt
- Replit in Claude is a connector that relays requests to Agent and returns a live-app link. A Claude design-canvas frame can be sent to Replit as a runnable app. Source: https://docs.replit.com/features/platforms/claude
- Replit in Slack is installed from Replit for Slack. Mention `@Replit` with a prompt to get a prototype in the thread. `/replit unlink` revokes the account link for that Slack workspace. Source: https://docs.replit.com/features/platforms/slack

### Monetization

Primary source: https://docs.replit.com/features/monetization/overview

- Agent can add Whop (digital products, memberships, subscriptions; account created for the builder), Stripe (web payments and subscriptions, starting in a sandbox), or RevenueCat (mobile in-app subscriptions in test mode).
- Shopify is the path for physical goods with inventory and fulfillment.

### Billing and plans

Primary source: https://docs.replit.com/billing/ai-billing

- Agent uses usage-based, effort-based billing. Paid work creates checkpoints that capture completed work. One checkpoint per request is the billed unit.
- Plan Mode can be billable even when it does not change code.
- Agent services that call third-party APIs are billed at the provider's public rate against Replit credits.
- Usage appears in the Agent tab (hover a checkpoint), the usage dashboard (up to 30 minutes delay), and Account → Billing alerts and budgets.
- Starter includes daily Agent credits with a monthly cap, monthly cloud credits for databases, object storage, and publishing, Lite/Free Mode building, and one 30-day published app. Source: https://docs.replit.com/billing/plans/starter-plan
- Core includes Agent, paid modes, Free Mode allowance, intelligent model routing, Design Canvas, Visual Editor, all artifact types, Plan Mode, connectors, one background task, five seats, monthly credits, and unlimited published apps. Source: https://docs.replit.com/billing/plans/replit-core
- Pro includes up to 10 parallel tasks, up to 15 builders, tiered credits with two-month rollover, priority support-engineer access on business days, and 28-day database recovery. Source: https://docs.replit.com/billing/plans/replit-pro
- Credit packs for Core and Pro come in $100, $300, $480-for-$500, and $950-for-$1,000 sizes, expire after six months, do not auto-renew, and can auto-reload. Usage limits cap spend beyond monthly credits. Enterprise admins can set per-user spend limits. Source: https://docs.replit.com/billing/managing-spend

### Enterprise

Primary source: https://docs.replit.com/billing/plans/replit-enterprise

- Enterprise includes Pro features plus SSO/SAML, SCIM, role-based access, audit logs via SIEM, publishing and geography policies, Enterprise Security Center, custom-scoped integrations, warehouse connectors, dedicated Product Advocate and Field Engineer, and unlimited seats.
- A person can upgrade to Enterprise inside Replit from any plan. Collaborative Team Workspaces transfer; the personal Workspace stays on the personal account. Published apps stay live.
- Billing models are an annual credit commitment or pay-as-you-go after a credit limit.
- SAML SSO is self-serve in Enterprise settings → Authentication for Microsoft Entra ID, Google Workspace, Okta, or another IdP. Claimed email domains must match a billing admin and cannot be public domains. Existing users on those domains must use SSO. Seats are consumed when an invitation is accepted, not when the IdP grants access. Source: https://docs.replit.com/teams/identity-and-access-management/saml
- SCIM automates provisioning from Entra ID, Okta, and other IdPs. Synced groups map to workspace roles Admin, Member, Viewer, and Guest. An account-admin group is required. Custom Replit groups can exist alongside locked SCIM groups. Source: https://docs.replit.com/teams/identity-and-access-management/scim
- Audit logs are Enterprise-only, admin-only, powered by WorkOS, retained 30 days by default, and can stream to Datadog, Splunk, Amazon S3, or an HTTP endpoint. Categories include deployments, access, workspace administration, project activity, secrets, connectors, domains, and Agent activity. The Compliance API can retrieve prompt text for `project.message_sent` events with the `compliance:messages:read` scope. Source: https://docs.replit.com/teams/identity-and-access-management/audit-logs
- Enterprise admins choose approved models per Workspace, set publishing privacy and deployment geography, require security scans, and use the Workspace Security Center and Auto-Protect. Source: https://docs.replit.com/teams/welcome
- Named customers quoted on the product homepage include Databricks, Zillow, Gusto, Payouts.com, Talkdesk, and SMFL Digital Lab. Source: https://replit.com/

## Sources

- https://docs.replit.com/
- https://docs.replit.com/features/agent/overview
- https://docs.replit.com/features/agent/plan-mode
- https://docs.replit.com/features/agent/agent-modes
- https://docs.replit.com/features/agent/model-selector
- https://docs.replit.com/features/agent/app-testing
- https://docs.replit.com/features/agent/general-agent
- https://docs.replit.com/features/agent/task-lifecycle
- https://docs.replit.com/features/agent/task-board
- https://docs.replit.com/features/agent/follow-up-tasks
- https://docs.replit.com/features/agent/web-search
- https://docs.replit.com/features/agent/image-generation
- https://docs.replit.com/features/agent/audio-generation
- https://docs.replit.com/features/agent/voice-mode
- https://docs.replit.com/features/agent/steer-and-queue-messages
- https://docs.replit.com/features/agent/skills
- https://docs.replit.com/features/agent/agent-customization
- https://docs.replit.com/features/agent/skills-directory
- https://docs.replit.com/chat/memories
- https://docs.replit.com/chat/overview
- https://docs.replit.com/features/conversations-and-routines/conversations
- https://docs.replit.com/chat/routines
- https://docs.replit.com/features/integrations/overview
- https://docs.replit.com/features/integrations/custom-connectors
- https://docs.replit.com/replitai/managing-connectors
- https://docs.replit.com/connectors/warehouses/overview
- https://docs.replit.com/features/mcp/overview
- https://docs.replit.com/platforms/mcp-server
- https://docs.replit.com/features/projects-and-artifacts/projects
- https://docs.replit.com/features/projects-and-artifacts/artifacts
- https://docs.replit.com/features/artifact-types/web-apps
- https://docs.replit.com/features/artifact-types/building-mobile-apps
- https://docs.replit.com/design/what-is-replit-design
- https://docs.replit.com/features/editor/editor-and-tools
- https://docs.replit.com/features/project-setup/replit-dot-md
- https://docs.replit.com/features/publishing/overview
- https://docs.replit.com/features/publishing/private-deployments
- https://docs.replit.com/features/publishing/deployment-types
- https://docs.replit.com/features/publishing/seo-agent
- https://docs.replit.com/features/data-and-storage/sql-database
- https://docs.replit.com/features/data-and-storage/object-storage
- https://docs.replit.com/features/auth-and-identity/overview
- https://docs.replit.com/features/security/overview
- https://docs.replit.com/features/security/package-firewall
- https://docs.replit.com/features/version-control/checkpoints-and-rollbacks
- https://docs.replit.com/core-concepts/project-editor/app-setup/secrets
- https://docs.replit.com/features/collaboration/workspaces
- https://docs.replit.com/features/platforms/desktop-app
- https://docs.replit.com/features/platforms/mobile-app
- https://docs.replit.com/features/platforms/chatgpt
- https://docs.replit.com/features/platforms/claude
- https://docs.replit.com/features/platforms/slack
- https://docs.replit.com/features/monetization/overview
- https://docs.replit.com/billing/ai-billing
- https://docs.replit.com/billing/plans/starter-plan
- https://docs.replit.com/billing/plans/replit-core
- https://docs.replit.com/billing/plans/replit-pro
- https://docs.replit.com/billing/plans/replit-enterprise
- https://docs.replit.com/billing/managing-spend
- https://docs.replit.com/teams/welcome
- https://docs.replit.com/teams/information-security/overview
- https://docs.replit.com/teams/identity-and-access-management/saml
- https://docs.replit.com/teams/identity-and-access-management/scim
- https://docs.replit.com/teams/identity-and-access-management/audit-logs
- https://docs.replit.com/legal-and-security-info/security
- https://replit.com/
