---
name: Claude Cowork
slug: claude-cowork
url: https://claude.ai/
docs: https://claude.com/docs/
kind: product
reviewed: 2026-09-28
---

# Claude Cowork

## Product

Claude Cowork is Anthropic's agentic workspace. A person describes an outcome; Claude plans the work, runs multi-step tasks, and returns finished files such as formatted documents, organized folders, spreadsheets with formulas, presentations, and synthesized research. It uses the same agentic architecture as Claude Code, inside Claude rather than a terminal.

Cowork is included on paid Claude plans: Pro, Max, Team, and Enterprise. It is not on Free. The full local-file, browser, and computer-use experience is the Claude Desktop app for macOS and Windows. Linux appears for some desktop features and is marked beta where the pages say so. Sessions also run at [claude.ai](https://claude.ai/), in Claude for iOS and Android, and in the Claude in Chrome side panel. Web and mobile Cowork are in beta on Pro, Max, and Team, and on Enterprise when an owner enables them.

Sessions run in the cloud by default (in beta): the agent loop and code execution run in an isolated sandbox on Anthropic's servers, and sessions and files are saved to the Claude account. Work continues if the laptop closes. When a task needs a local folder, the built-in browser, or the computer, Claude reaches the machine through Claude Desktop while that app is open. Local execution remains available for existing desktop deployments: the agent loop runs on the device, and code runs in an isolated Linux VM.

On desktop, web, and mobile, chat and Cowork share one home. The person selects Cowork in the message box, describes the task, reviews the plan, and lets it run. Opening the Chrome side panel starts a Cowork session directly. A gradual "one Claude" rollout on Pro and Max removes the Chat and Cowork selector: every conversation can take on a Cowork task. Team and Enterprise organizations keep chat and Cowork as separate options. Existing Cowork tasks, projects, connectors, skills, artifacts, and files carry into the new experience.

This file is Cowork only. The Claude assistant people use in chat is a different product (`claude`). Claude Code, the coding agent in the terminal, IDE, desktop Code tab, and claude.ai/code, is a different product (`claude-code`). Claude Tag, Claude Science, and Claude for Microsoft 365 have their own docs sections and are out of scope here.

## Features

### Cowork

Primary source: https://claude.com/docs/cowork/overview

- Cowork is Anthropic's agentic workspace in Claude Desktop: Claude takes multi-step tasks and returns completed work such as polished documents, organized files, and synthesized research.
- Claude reads and writes local files on the computer without manual uploads or downloads.
- Pairing Cowork with Claude in Chrome automates tasks on websites.
- Complex work is split into smaller tasks with parallel workstreams (sub-agent coordination).
- Outputs include Excel spreadsheets with functional formulas, PowerPoint presentations, and formatted documents.
- Connectors, skills, and plugins are managed from Customize in the sidebar. Cowork loads the ones enabled for the claude.ai account, synced at session start, and does not read Claude Code's `~/.claude` directory. A skill or plugin that exists only in `~/.claude` must be added in Customize.
- Monitoring tracks usage and activity across the organization.
- Multi-step tasks that run code, create files, or use connected apps and the browser consume more of the plan's usage than a quick question. Source: https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
- When Claude drafts a Markdown document, the person can highlight text, choose Edit with Claude, and have the edit applied in place. Source: https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
- Global instructions apply to every Cowork session (tone, output format, role). In the new Claude experience they live under Instructions for Claude in Settings > General. Source: https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
- Folder instructions add project-specific context when a local folder is selected on desktop. Claude can update them during a session. Source: https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
- The person can delete a task from the task menu or Tasks list. It leaves task history immediately and is deleted from Anthropic's backend storage within 30 days under Anthropic's retention periods. Source: https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
- Sessions cannot be shared with other people. Individual artifacts created in a session can be shared. Source: https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
- The product page lists file types Cowork can read, create, edit, and analyze, including Word, PDF, plain text, Markdown, HTML, JSON, CSV, TSV, Excel, PowerPoint, common images, YAML, XML, TOML, Jupyter notebooks, and common source-code extensions. Connectors can add more file access. Source: https://claude.com/product/cowork

### Desktop, web, and mobile

Primary source: https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile

- Claude Cowork is available on desktop, web, mobile, and in the Claude in Chrome side panel. Sessions and files live with the Claude account.
- Web and mobile Cowork are in beta for Pro, Max, and Team, and for Enterprise where an admin has enabled them.
- The Chrome side panel is available on Max and Team, on Pro as it rolls out, and on Enterprise where an admin has enabled it.
- On desktop, web, and mobile, the person starts Cowork from the same message box as chat by selecting Cowork, then describing the task. Selecting Chat returns to a regular conversation.
- In the new Claude experience there is no Cowork selector; describing the task in any conversation is enough.
- Opening the Chrome side panel starts a Cowork session with no chat/Cowork switch.
- Desktop is the full Cowork experience: local files and browser use. Web is claude.ai. Mobile is the latest Claude for iOS or Android.
- Start, steer, and review tasks; resume a session started on another surface; connectors; skills and plugins; preview files Claude creates; scheduled tasks; and projects are available across the documented surfaces, with the limits in that article's feature table.
- Local file access, local connectors, browser use, and computer use from web or mobile go through Claude Desktop. A cloud session can read and write connected folders only while the desktop app is open and the session was started on desktop. If the app is closed, the session keeps running but cannot reach local files.
- Projects tied to a local folder support Cowork sessions on desktop only. Cowork does not change a project's contents; the person adds anything they want to keep.
- Local connectors and plugins that include local MCP servers work through the desktop app only.
- When a task finishes or needs input, the person can get a notification on their phone.
- Claude Desktop for macOS and Windows is available on all paid plans. Download and updates are at claude.com/download. Source: https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork

### Sessions in the cloud

Primary source: https://support.claude.com/en/articles/14479288-claude-cowork-architecture-overview

- Cloud sessions run the agent loop and code execution in an isolated, temporary sandbox on Anthropic-managed infrastructure. Each session gets its own sandbox, created at start and destroyed at end. Sandboxes do not share state with each other or across organizations.
- The sandbox cannot reach private, internal, link-local, or cloud-metadata addresses, or Anthropic-internal systems, by default.
- Network access follows the same network-access setting that governs local Cowork and chat. No network access is the default for Enterprise organizations.
- All traffic leaving the sandbox passes through a mandatory proxy the sandbox cannot reconfigure. Only allow-listed destinations are reachable.
- The sandbox holds only session-scoped tokens that expire within hours. Connector authorization tokens never enter the sandbox; connector calls are made on the server side.
- When a cloud session needs a local file or the browser, the request goes through Claude Desktop over an Anthropic-brokered connection, limited to folders the member connected, with each local tool call checked against the member's permissions. If the desktop app is offline, the session cannot reach the device.
- Work in a cloud session, including local files opened through the desktop app, is processed on Anthropic's servers. Team and Enterprise conversation data is handled under the same commercial commitments as other Team and Enterprise data and is not used to train Claude.
- Local sessions (existing desktop deployments) run the agent loop on the device. Code execution runs in a dedicated Linux VM isolated by Apple Virtualization.framework on macOS or Hyper-V on Windows, with its own egress filtering, syscall restrictions, and per-session user isolation.
- If the local VM cannot start, Cowork continues file and web tools. Shell commands and code execution report "workspace unavailable" until the VM recovers.
- Endpoint detection tools cannot inspect activity inside the VM. Cloud sessions run outside the organization's endpoints.

### Dispatch

Primary source: https://claude.com/docs/cowork/guide/dispatch

- Dispatch is a long-running agent in Cowork. The person describes an outcome in one conversation; the Dispatch agent breaks it into tasks, runs each as a separate Cowork or Code session, and surfaces results in the sidebar.
- Docs require a Pro or Max plan and the latest Claude Desktop app on macOS or Windows.
- The agent appears as Dispatch in the left sidebar and opens a single conversation.
- Child tasks appear under the Dispatch group with their own status. Child tasks do not spawn further children.
- Coding work runs in Code against a workspace already set up. Knowledge work runs in Cowork in the specified project or the default project.
- Child-task states are Running, Awaiting input, Awaiting answer, Completed, Error, and Archived.
- Permission prompts from a child task (for example a command or a write outside the workspace) are forwarded to the person. If there is no response within ten minutes, the request is denied and the task continues without that action.
- The person can open a child task's transcript, send follow-ups, or ask Dispatch to start a new task that builds on the result.
- When Claude Desktop is running, the computer registers as a Dispatch host. From the Claude mobile app, a Dispatch conversation can run on the desktop. The computer should stay awake and online with Claude Desktop open.
- Help marks Dispatch as limited beta for some Pro and Max plans, requiring both Claude Desktop and the Claude mobile app. It is not available to new users in the new Claude experience; existing users can keep using it. If Dispatch is not in the side panel, the pages direct people to Cowork in the cloud instead. Source: https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork
- Help describes Dispatch as one persistent thread that does not reset, with development tasks routed to Claude Code and knowledge work to Cowork, and a push notification when a task finishes or needs approval. Source: https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork
- Computer use is not in the Linux desktop beta. On Linux, Dispatch still uses files, connectors, and plugins. Source: https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork

### Projects

Primary source: https://claude.com/docs/cowork/guide/projects

- A Cowork project collects local folders to read and write, standing instructions, useful links, and a dedicated memory store so each session in the project starts with that setup.
- The docs page states that projects live on the computer and are not synced to the cloud or shared with other people.
- Each project can hold a description (Dispatch reads it when choosing a project), folders, instructions, links, linked projects from Chat on claude.ai, and project-scoped memory.
- Creation starts from Projects in the left navigation: Start from scratch (empty project with a new folder), Import a project (bring a claude.ai project into Cowork), or Use an existing folder.
- Starting a session from a project mounts that project's folders and applies its instructions. Files Claude creates land in the project's folders. What Claude learns is saved to the project's memory.
- Dispatch can route background tasks into a project so long-running work picks up the same folders, instructions, and memory.
- Dragging files or folders into a project copies individual files into the project's first folder and mounts folders as additional project folders. Claude reads individual files up to 50 MB.
- A Cowork project is stored separately from a claude.ai project. Linking a claude.ai project lets Cowork sessions draw on its knowledge without merging the two. The docs table says a claude.ai project can be shared with teammates on Team and Enterprise; a Cowork project cannot.
- Archiving removes the project from the list and deletes its metadata (name, instructions, links, memory). Attached local folders are not touched.
- Help states that new projects created in Cowork can be saved to the Claude account and picked up on other devices, while projects created from a folder on the computer stay on that computer. Source: https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork
- Help lists scheduled tasks that are specific to the project as part of what a project holds. Source: https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork
- Help says project memory is scoped to that project and does not carry to other projects. Source: https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork
- Help says project sharing is available on Team and Enterprise, with Can view or Can edit, the same as projects in Claude. Group sharing is in beta on Enterprise. Source: https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork
- Help says Cowork projects are not available in Claude Code. Source: https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork
- Team and Enterprise help: there are no separate admin controls for project creation. For local sessions, project data is stored on the user's computer; for cloud sessions, projects are saved with the member's Claude account. Source: https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans

### Scheduled tasks

Primary source: https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork

- Scheduled tasks run automatically on a cadence or on demand. Claude saves the prompt as the task's instructions and runs them at the chosen schedule.
- They are available on all paid plans (Pro, Max, Team, Enterprise), in Claude Cowork and in the new Claude experience rolling out to Pro and Max.
- A scheduled task has the same capabilities as a regular Cowork task, including connectors, skills, and installed plugins. Each run is its own Cowork session.
- Scheduled tasks run remotely and keep their cadence when the computer is asleep or Claude Desktop is closed. Upcoming and past runs are under Scheduled in the left sidebar on any surface.
- They use built-in schedule options and work with connectors and files saved to the Claude account. They cannot be tied to a folder on the computer. A scheduled task that requires local files or apps runs only locally.
- In Cowork, create from Scheduled > New task with Create with Claude or Set up manually. Manual setup includes task name, prompt, approval mode, frequency (hourly, daily, weekly, on weekdays, or manually), optional model, and optional folder.
- Type `/schedule` in a Cowork task to launch a skill that creates a scheduled task. Source: https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
- From the Scheduled page the person can view tasks, review runs, edit instructions or cadence, pause, resume, delete, or run on demand.
- In the new Claude experience, the person can describe the task and cadence in any conversation, review the proposal, and confirm Schedule.

### Connectors

Primary source: https://claude.com/docs/connectors/getting-started

- A connector links Claude to an outside app or service so Claude can find information there and take actions.
- The person adds a connector from Customize > Connectors in claude.ai or Claude Desktop, including from the Connectors directory.
- On Team and Enterprise, an Owner adds a connector for the organization; members then connect with their own account.
- In a conversation, the + menu's Connectors list turns each connector on or off for that conversation. Claude can ask for Allow once or Always allow before using a tool.
- Tool permissions on a connector's page are Always allow, Needs approval, or Blocked, per tool group or single tool.
- Disconnect signs Claude out of the service and leaves the connector in the list. Remove takes it off the account. Owners remove organization connectors from Organization settings > Connectors.
- Connectors work across Claude apps. Cowork is listed as a surface that uses connectors and plugins. The Claude desktop app also supports local connectors installed as desktop extensions (MCP Bundles).
- The Connectors Directory is one catalog for claude.ai, Claude Desktop, mobile, Claude Code, and Cowork, with Verified and Community labels. Directory connectors are eligible for Suggested Connectors. Source: https://claude.com/docs/connectors/directory
- On Team plans, members without permission to enable connectors see Request on a directory connector. Owners handle requests in Organization settings > Connectors and Notifications. Source: https://claude.com/docs/connectors/directory
- A remote MCP server that is not in the directory is added as a custom connector by URL. Free plans can add one custom connector. Team and Enterprise Owners add custom connectors for the organization. Source: https://claude.com/docs/connectors/custom/add-unlisted
- A desktop extension (`.mcpb`) installs from Settings > Extensions in Claude Desktop when signed in to claude.ai. The organization can turn extensions off or limit which ones members install. Source: https://claude.com/docs/connectors/custom/add-unlisted
- Network egress permissions do not apply to web fetch, web search, or MCPs, including Claude in Chrome. Web fetch runs server-side and is limited to search results and URLs the person shared. Team or Enterprise owners can turn off web search for Cowork and Chat in Organization settings > Capabilities. Source: https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork

### Skills

Primary source: https://claude.com/docs/skills/overview

- Skills are directories of instructions, scripts, and resources that Claude loads for specific tasks. Each skill has a `SKILL.md` that defines when it activates and what to follow.
- Skills are available on Pro, Max, Team, and Enterprise. They run in Claude's code sandbox, so Code execution and file creation must be on under Settings > Capabilities (or Organization settings > Capabilities on Team and Enterprise).
- Claude sees each skill's name and one-line description, loads the matching `SKILL.md`, and opens extra files only when needed.
- Skills live at Customize > Skills, grouped as Created by you, From your organization, Shared with you, and From Anthropic & Partners. Discover lists skills to add.
- The person turns a skill on, then describes a task or types `/` in the message box to pick one. Plugin skills turn on and off with the plugin.
- Types include Anthropic skills (Excel, Word, PowerPoint, PDF), partner skills built for MCP connectors, organization-provisioned skills on Team and Enterprise, and custom skills.
- On Team and Enterprise, a skill's page shows Adoption, Activity, and You usage figures.

### Plugins

Primary source: https://claude.com/docs/cowork/guide/plugins

- A plugin extends Cowork with skills, MCP connectors, subagents, commands, or hooks in one package. Sources are the marketplace, the organization, or an uploaded file.
- A plugin installed in Cowork is saved to the account, so its skills and connectors are also available in chat and Claude Code.
- Components: skills (reusable workflow instructions), connectors (MCP servers), agents (specialized subagents), and hooks (scripts at defined points in a session).
- Browse, install, and upload from Customize > Plugins. Discover uses Anthropic's official catalog; other marketplaces can be added by URL.
- Installing a plugin does not add or sign in to any connector. Connect each bundled connector from the plugin's Connectors tab.
- Upload a plugin package from the Plugins page.
- A Git repository can serve as a marketplace. For a marketplace the person adds themselves, GitHub (including GitHub Enterprise) and public GitLab and Bitbucket repositories work. Team and Enterprise Owners sync a repository from organization settings to distribute plugins to everyone.
- Default limits: 200 MB uncompressed plugin package, 5,000 files per package, 512 MB marketplace archive, 500 plugins per marketplace, 25 marketplaces the person can add. The in-app skill viewer previews files up to 1 MB.
- On Team and Enterprise, administrators can require plugins. Required plugins install automatically, show "This plugin is required by your organization," and cannot be removed.
- Cowork checks for marketplace updates and warns before overwriting locally edited plugin files.
- Chat loads skills, commands (as a skill), and remote MCP connectors. Cowork also loads agents, hooks, and local MCP servers when the session runs on the computer. Executables in `bin/`, LSP servers, output styles, themes, and `settings` are ignored or cannot be installed in Cowork. Source: https://claude.com/docs/plugins/platform-support
- In Cowork, type `/plugin-name:command` to run a command, or describe the task and let Claude load the matching skill. Cowork also runs the plugin's agents. Source: https://claude.com/docs/plugins/overview
- A bundled connector marked Runs in each session runs on the computer. It works in Claude Code and in a Cowork session that runs on the computer in the desktop app, not in chat. Source: https://claude.com/docs/plugins/overview
- Organization plugin states include Installed by default (can be turned off) and Required (always on). Source: https://claude.com/docs/plugins/overview
- An open-source financial services plugin set for Cowork covers financial modeling, equity research, investment banking, private equity, and wealth management. Add the GitHub marketplace `https://github.com/anthropics/financial-services` and install the financial analysis core plugin first. The core plugin includes connectors for providers such as Daloopa, Morningstar, S&P Global, FactSet, Moody's, MT Newswires, Aiera, LSEG, PitchBook, Chronograph, and Egnyte; those may need a separate provider subscription or API key. The plugins also work in Claude Code. Source: https://claude.com/docs/office-agents/fsi-plugins

### Built-in browser and Claude in Chrome

Primary source: https://support.claude.com/en/articles/16607400-use-the-built-in-browser-in-claude-cowork

- Cowork has a browser built into Claude Desktop. When a task involves a website, the browser opens in the side panel. Claude opens sites, reads pages, clicks, types, and fills forms. Links in the task transcript open in the same panel.
- The built-in browser is rolling out to Cowork in Claude Desktop for macOS, Windows, and Linux (beta) on Pro, Max, and Team, and on Enterprise where an owner has enabled it. When the desktop app is online, it is also available in Cowork on web or mobile.
- Claude Desktop must be open and online for the built-in browser, even when the Cowork session runs in the cloud. A task started on desktop can be steered from web or mobile while the desktop app stays open.
- The first time the built-in browser opens, the person can import cookies site by site. Banking, email, and single sign-on sites stay unchecked by default. Import is available from Chrome, Edge, and Firefox on macOS, and from Firefox on Windows and Linux (beta). Import is not available from Safari.
- Claude can also sign in as it goes and remembers logins across Cowork sessions on that computer.
- The built-in browser is separate from the person's own browser. Claude does not see saved logins unless they are imported.
- Claude in Chrome uses the person's Chrome browser and signed-in accounts through the extension. If Claude in Chrome is already in use, it stays the default for web tasks in Cowork; otherwise Cowork uses the built-in browser once it is available.
- Preferred browser is set in Settings > Cowork: Built-in browser or Chrome (Claude in Chrome). If the preferred browser is unavailable, Claude says so and continues with the other one.
- If the preferred browser is the built-in browser, tasks started on web or mobile use the desktop app's browser while the app is open. If the preference is Claude in Chrome, web or mobile tasks use the extension; the session needs to be connected to a desktop, but the app does not have to be open.
- Safeguards: permission before acting on a site for the first time, a blocklist for high-risk sites, and safety checks that compare each action with the request.
- In the Chrome side panel, Claude can read the tab the person is on without the desktop app. Claude driving a browser as part of a task still needs the desktop app open. Source: https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile
- Team owners control the built-in browser from Organization settings > Cowork (on by default as it rolls out). Enterprise: off by default at launch, on by default starting 10 September 2026 unless turned off. Claude in Chrome is controlled from Organization settings > Claude in Chrome. Source: https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans
- Browser traffic comes from the user's machine. To site operators it looks like traffic from that device, even when the session is steered from web or mobile. Source: https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans

### Computer use

Primary source: https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork

- Computer use is in beta for Pro and Max. It is available in Cowork and Claude Code in Claude Desktop on macOS and Windows. Team and Enterprise do not have it.
- When it is enabled and there is no connector or tool for the work, Claude may click, type, and open apps on the screen.
- Cowork tries connectors first, then the built-in browser or Claude in Chrome, then screen interaction.
- Enable it in Settings > General (under Desktop app) with Enable computer use. Claude asks for permission before accessing each application. Some apps are off-limits by default.
- The computer must be awake and Claude Desktop open.
- On macOS 15 or later, Claude works in background windows by default and does not take over the pointer or keyboard. It generally waits if the person is typing. Full-screen takeover is under Settings > General > When Claude requests access to an app.
- Claude takes screenshots of permitted apps to navigate. An app blocklist denies requests for listed apps. Investment, trading, and cryptocurrency apps are blocked by default.
- Computer use has no sandbox between Claude and the applications. Actions in one app can open another (for example a link opening in Chrome).

### Artifacts

Primary source: https://support.claude.com/en/articles/14729249-use-artifacts-in-claude-cowork

- Artifacts made in Cowork on or after 19 August 2026 use Claude's updated artifacts system: they are saved to the account, can be shared with people in the organization, and open on the web. They appear in the Artifacts view in the Cowork sidebar with a Cowork label.
- Live artifacts are artifacts made in Cowork before 19 August 2026. They stay in the Artifacts view and keep working. They cannot be edited in place. Republish via Share to continue editing as a new artifact.
- Organizations that use customer-managed encryption keys (CMEK), zero data retention (ZDR), or a HIPAA-ready configuration keep using live artifacts.
- Live-artifact sharing stays inside the organization: no external or public links and no per-person recipient selection. Shared artifacts use the viewer's connectors and data sources, not the author's.
- Artifacts created on or after 19 August 2026 are available on desktop and web. Live artifacts created before that date are available on the desktop app only. Source: https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile
- Spreadsheets and slides Cowork produces can be edited further with Claude for Excel and Claude for PowerPoint. Source: https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork

### Permissions

Primary source: https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork

- Cowork has three modes that control when Claude asks before an action such as using a connector. Change the mode from the selector in the chat box: Manually approve (Manual), Automatically approve (Auto), and Skip all approvals (Skip).
- In the new Claude experience the permission setting offers Auto and Manual (default).
- Manual: Claude pauses and asks Allow or Deny for actions.
- Auto: Claude keeps working. It reviews each action for safety and blocks actions it determines unsafe, then looks for a safer path or asks. If it keeps hitting blocks, it switches back to asking. Auto applies to existing connectors, plugins, the built-in browser, Claude in Chrome, and some Cowork actions such as fetching websites. Auto consumes more of the usage limit than the other modes.
- Skip: Claude does not pause and nothing checks its actions automatically.
- Claude requires explicit Allow before permanently deleting files, in any mode.
- Team and Enterprise owners control whether Automatically approve appears (Allow “Automatically approve” mode in Organization settings > Cowork, on by default). Source: https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans
- Allow "Always allow" for connector tools (Organization settings > Cowork, under Permissions) is off by default. When it is off, Allow for all tasks is grayed out for write-capable connector tools, and saved always-allow preferences for write tools are not honored. Read-only tools are exempt only when the connector annotates them as read-only. Source: https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans
- Action screening in Auto mode and deletion protection are listed among Cowork safety measures. Source: https://support.claude.com/en/articles/13364135-use-claude-cowork-safely
- Memory is shared between chat and Cowork when Cowork runs in the cloud. Local Cowork sessions do not use that shared memory. On Team and Enterprise, memory is off by default until an owner turns it on. Source: https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context

### Administration

Primary source: https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans

- Cowork is on by default. Organization owners can disable it for the organization from Organization settings > Cowork > Enable for your organization.
- Run Cowork in the cloud is a separate toggle. Team: on by default. Enterprise: off by default; an owner turns it on, then grants the Cowork in the cloud capability to a group with custom roles.
- On Enterprise, groups and custom roles can enable Cowork for specific teams.
- Plugins in Cowork are controlled by the same admin toggle as Cowork. There is no separate plugin-access setting inside Cowork.
- Owners can create plugin marketplaces and set each plugin to Installed by default, Available to install, Required, or Not available. Enterprise admins can override those preferences for specific groups.
- Team and Enterprise owners can configure company branding, including a redesigned home screen, in Organization settings.
- Cowork respects organization network egress settings under Organization settings > Capabilities > Code execution. Settings apply when a new session is created; a change during an active conversation does not apply until a new conversation starts.
- Two MDM keys restrict Cowork on managed devices: `isLocalDevMcpEnabled` false disables plugin-bundled and locally configured MCP servers; `isDesktopExtensionEnabled` false blocks MCPB and DXT extension servers. They apply to local sessions and to what a cloud session reaches through the desktop app. Local MCP servers do not run in cloud sessions. Source: https://support.claude.com/en/articles/14479288-claude-cowork-architecture-overview
- Organization controls for cloud sessions include turning cloud sessions on or off while leaving local desktop Cowork available, setting network-access policy, requiring fresh approval for every permission-gated tool call, controlling whether members can run sessions without per-call approval prompts, and requiring trusted-device enrollment and a recent sign-in. Source: https://support.claude.com/en/articles/14479288-claude-cowork-architecture-overview
- Cowork via Claude, Claude Desktop, and Claude Mobile is captured in the Compliance API.
- For local sessions, conversation history is stored on users' computers and is not subject to Anthropic's standard data retention policies. Admins cannot centrally manage or delete it. Enterprise admins can retrieve it through the Compliance API. Deletion endpoints for local sessions are not available yet.
- Enterprise Security, including skill and plugin scanning when skills and plugins are installed, is described on the safety page for Enterprise. Source: https://support.claude.com/en/articles/13364135-use-claude-cowork-safely

### Monitoring

Primary source: https://claude.com/docs/cowork/monitoring

- Team and Enterprise plans can export Cowork events through OpenTelemetry (OTel logs/events): user prompts, model responses, API requests, tool usage, and errors.
- Configure OTLP endpoint, protocol (`http/json` or `http/protobuf`), and headers under Admin settings > Cowork. Settings load at session start.
- Docs require Claude desktop app version 1.1.4173 or later. Help says monitoring cloud sessions requires Claude Desktop 1.22209.3 or later, and local desktop sessions require 1.1.4173 or later. Source: https://support.claude.com/en/articles/14477985-monitor-claude-cowork-activity-with-opentelemetry
- The OTel exporter runs inside the Cowork VM and follows the session's egress rules. Cowork adds the collector hostname to the session egress allowlist automatically.
- Events include metadata only by default. Prompt content, model response text, and tool details are included only when `otlpContentCapture` enables them.
- `prompt.id` links all events produced while processing one user prompt.
- Event names include `user_prompt`, `assistant_response`, `tool_result`, `api_request`, `api_error`, and `tool_decision`.
- Resource `service.name` is `cowork`. On first-party deployments, events include `user.email` and account attributes. Cost values in events are approximations; official billing is on the billing dashboard.
- Help says OTel is for security monitoring and incident investigation and does not replace audit logging for compliance. The Compliance API covers Cowork alongside chats and Claude Code. Source: https://support.claude.com/en/articles/14477985-monitor-claude-cowork-activity-with-opentelemetry

### Plans and usage

Primary source: https://claude.com/product/cowork

- Claude Cowork is included in Pro, Max 5x, Max 20x, Team, and Enterprise. The product page states Cowork consumes limits faster than Chat.
- Team includes Cowork and the Slack connector on standard and premium seats, self-serve seat management, and extra usage at API rates, for teams of 2 to 150.
- Enterprise includes admin controls, usage analytics, the Analytics API, and OpenTelemetry observability.
- The product FAQ states Cowork runs on web and mobile in beta; the desktop app adds folders and applications on the computer.
- The product FAQ states starting a task from the phone, with work continuing in the cloud when the laptop is closed, is available on Pro, Max, and Team automatically, and Enterprise can opt in.
- Admins can toggle Cowork off in Admin Settings and manage access across teams with role-based access controls.
- The product page states Cowork can run with a Claude account or the organization's own cloud provider: Amazon Bedrock, Google Cloud, or Microsoft Foundry.
- Compare plan matrices and seat pricing on the Claude pricing page. Source: https://claude.com/pricing
- Usage credits on Pro, Max 5x, and Max 20x continue work after included limits at standard API rates from Settings > Usage. Source: https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans
- In the new Claude experience, longer agentic tasks that search the web, run code, or create files generally use more usage than a quick question. Check Settings > Usage. Source: https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude

## Sources

- https://claude.com/docs/
- https://claude.com/docs/cowork/overview
- https://claude.com/docs/cowork/guide/dispatch
- https://claude.com/docs/cowork/guide/plugins
- https://claude.com/docs/cowork/guide/projects
- https://claude.com/docs/cowork/monitoring
- https://claude.com/docs/plugins/overview
- https://claude.com/docs/plugins/platform-support
- https://claude.com/docs/connectors/getting-started
- https://claude.com/docs/connectors/directory
- https://claude.com/docs/connectors/custom/add-unlisted
- https://claude.com/docs/skills/overview
- https://claude.com/docs/office-agents/fsi-plugins
- https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
- https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile
- https://support.claude.com/en/articles/14479288-claude-cowork-architecture-overview
- https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork
- https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork
- https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork
- https://support.claude.com/en/articles/16607400-use-the-built-in-browser-in-claude-cowork
- https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork
- https://support.claude.com/en/articles/14729249-use-artifacts-in-claude-cowork
- https://support.claude.com/en/articles/13364135-use-claude-cowork-safely
- https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans
- https://support.claude.com/en/articles/14477985-monitor-claude-cowork-activity-with-opentelemetry
- https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context
- https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude
- https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans
- https://claude.com/pricing
- https://claude.com/product/cowork
- https://claude.ai/
