---
name: Claude Code
slug: claude-code
url: https://code.claude.com/docs/en/overview
docs: https://code.claude.com/docs
kind: product
reviewed: 2026-09-28
---

# Claude Code

## Product

Claude Code is Anthropic's agentic coding product. It reads a codebase, edits files, runs commands, and connects to development tools. The same engine runs in the terminal CLI, VS Code, JetBrains IDEs, the Claude desktop app's Code tab, the browser at claude.ai/code, and the Claude app for iOS and Android.

The product is the chassis around Claude models: built-in tools, permissions, sessions, and the surfaces that start and steer them. Anthropic also sells the Claude assistant (spec `claude`) and Claude Cowork (spec `claude-cowork`). Those sit in the same desktop app as Chat and Cowork tabs. This file covers only Claude Code.

Most surfaces need a Claude subscription or an Anthropic Console account. The terminal CLI, VS Code, and JetBrains also accept third-party providers: Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry, and Claude Platform on AWS. Cloud sessions, Desktop, Routines, Remote Control, Chrome, computer use, Artifacts, and Slack coding sessions require a claude.ai account. Desktop is a paid-subscription surface. Computer use and Dispatch are Pro and Max only. Code Review is Team and Enterprise. Projects are a public beta on Pro and Max.

A person starts work by installing the CLI and running `claude` in a project, opening the VS Code or JetBrains plugin, signing into the desktop app and clicking Code, or submitting a task at claude.ai/code. Local sessions run on the machine. Cloud sessions run on Anthropic-managed VMs or a self-hosted environment. Remote Control drives a local session from a phone or browser. Configuration, `CLAUDE.md`, and MCP servers are shared across local surfaces.

Documented work includes writing tests, fixing lint and merge conflicts, updating dependencies, writing release notes, multi-file features, debugging from a symptom, staging and committing with git, opening pull requests, and running the same loop from CI, Slack, or a schedule.

## Features

### Terminal

Primary source: https://code.claude.com/docs/en/overview

- The CLI is the full-featured terminal surface. It edits files, runs commands, and manages a project from the command line.
- Native installers cover macOS, Linux, WSL, Windows PowerShell, and Windows CMD. Native installs update in the background.
- Homebrew offers `claude-code` (stable, typically about a week behind, skips major regressions) and `claude-code@latest`. Homebrew does not auto-update.
- WinGet installs `Anthropic.ClaudeCode` and does not auto-update. apt, dnf, and apk are also documented for Debian, Fedora, RHEL, and Alpine.
- Git for Windows is recommended on native Windows so the Bash tool is available. Without it, Claude Code uses PowerShell as the shell tool.
- First launch prompts for login. If `ANTHROPIC_API_KEY` is set, Claude Code skips login and asks the person to approve the key.
- `claude -p` runs a prompt and exits. The CLI accepts piped input and can run in CI. Source: https://code.claude.com/docs/en/cli-reference
- `claude --continue` / `-c` and `claude --resume` / `-r` reopen sessions. `--fork-session` copies history into a new session ID. `--worktree` / `-w` starts an isolated git worktree. Source: https://code.claude.com/docs/en/cli-reference
- `claude --cloud` starts a cloud session. `claude --teleport` pulls a cloud session into the terminal. `--teleport` requires a claude.ai subscription. Source: https://code.claude.com/docs/en/claude-code-on-the-web
- `/desktop` continues a terminal session in the Desktop app for visual diffs. It requires a claude.ai subscription and is available on macOS and x64 Windows.
- `claude agents` opens agent view for background sessions. `claude remote-control` starts a Remote Control server. `claude setup-token` prints a long-lived OAuth token for CI. Source: https://code.claude.com/docs/en/cli-reference
- Scripting, the Agent SDK, and computer use on macOS (Pro and Max) are CLI capabilities. Source: https://code.claude.com/docs/en/platforms

### Visual Studio Code

Primary source: https://code.claude.com/docs/en/vs-code

- The extension is a graphical Claude Code panel in VS Code 1.94.0 or later. It also installs in Cursor and other VS Code forks, including from Open VSX.
- It provides inline diffs, @-mentions with line ranges, plan review as a Markdown document, conversation history, and multiple conversations in tabs or windows.
- The extension bundles its own CLI for the chat panel. Running `claude` in the integrated terminal still needs the standalone CLI.
- Sign-in uses a paid Claude subscription or a Console account. Third-party providers are supported.
- Permission modes in the prompt box include Auto, Manual, Plan, and Edit automatically. Auto is the built-in starting mode on Claude Code v2.1.283 or later.
- The Customize menu covers MCP servers, commands, output styles, hooks, memory, instructions, permissions, plugins, sandbox, and Claude in Chrome.
- Side questions use `/btw`. Remote Control can be enabled for all sessions. Focus view hides tool calls and thinking behind expandable rows.
- Selected editor text is attached automatically. `files.exclude`, `search.exclude`, and gitignored files can withhold selected text from the chat panel.

### JetBrains IDEs

Primary source: https://code.claude.com/docs/en/jetbrains

- A JetBrains plugin covers IntelliJ IDEA, PyCharm, Android Studio, WebStorm, PhpStorm, and GoLand.
- Features include `Cmd+Esc` / `Ctrl+Esc` launch, diffs in the IDE viewer, automatic selection and tab context, file-reference shortcuts, and `getDiagnostics` for inspection errors.
- The plugin runs the `claude` CLI in the IDE terminal and does not bundle the CLI. `/ide` from an external terminal connects Claude Code to the IDE and can install the plugin.
- Any paid Claude subscription or a Console account works. No API key is required.
- The plugin runs a hidden local MCP server named `ide` for diffs, selection, and diagnostics. Enabling "Accept connections from all network interfaces" exposes the unencrypted WebSocket beyond loopback.
- Remote Development requires the plugin on the remote host. WSL2 needs a firewall or mirrored-networking fix for IDE detection.

### Desktop application

Primary source: https://code.claude.com/docs/en/desktop

- The Claude desktop app has Chat, Cowork, and Code tabs. Code is the Claude Code surface. The app includes Claude Code; a separate CLI install is not required. A paid subscription is required.
- Installers cover macOS (Intel and Apple Silicon), Windows x64, Windows ARM64, and Linux (beta) on Ubuntu and Debian via apt.
- A session picks environment (Local, Cloud, SSH, or WSL on Windows), project folder, model, and permission mode. Cloud sessions can attach multiple repositories.
- Panes include chat, diff, browser, terminal, file editor, plan, tasks, subagent, and on macOS an iOS Simulator. Panes can be rearranged, popped out, or split.
- The Browser pane can preview a local app, open HTML, PDF, image, and video files, and browse external sites in a clean profile. Safety classifiers review write actions on external pages.
- Diff view supports line comments, a Review code pass for compile errors, logic errors, security issues, and obvious bugs, and PR monitoring via the GitHub CLI with Auto-fix and squash Auto-merge.
- Parallel sessions can use git worktrees. Side chats (`Cmd+;` / `/btw`) use session context without writing back. Claude can list, message, rename, and archive other Code-tab sessions it runs.
- Continue in can send a local session to Claude Code on the web (clean working tree; not SSH) or open the project in a supported IDE.
- Dispatch lives in the Cowork tab. A person messages a task and Dispatch can spawn a Code session. Dispatch requires Pro or Max and is not on Team or Enterprise.
- Desktop scheduled tasks run on the machine while the app is open and the computer is awake. The Routines page can also create cloud routines. Source: https://code.claude.com/docs/en/desktop-scheduled-tasks
- Computer use is a research preview on macOS and Windows for Pro and Max. It is off by default. On macOS it can run in the background.

### Cloud sessions

Primary source: https://code.claude.com/docs/en/claude-code-on-the-web

- Cloud sessions run on Anthropic-managed VMs by default, or on a self-hosted environment. They keep running after the laptop closes.
- Available on Pro, Max, and Team, and on Enterprise with premium seats or Chat + Claude Code seats.
- Start from claude.ai/code, the Claude mobile Code tab, Desktop (Cloud environment), `claude --cloud`, or a routine.
- Environments set network access, environment variables, and setup scripts. The Default environment uses Trusted network access.
- GitHub access is via the Claude GitHub App or `/web-setup` (sends a local `gh` token). Threads in a project need the GitHub App on each cloned repo. Organizations with Zero Data Retention cannot use `/web-setup` or other cloud session features.
- `claude --cloud` from a repo with no remote, or without the GitHub App, can upload a local git bundle (under 100 MB; untracked files omitted; credential-like files skipped on macOS, Linux, and WSL).
- `--teleport` / `/teleport` pulls a cloud session into the terminal: correct repo, clean git state, pushed branch, same claude.ai account. The terminal copy stays local.
- Permission modes in the cloud are Accept edits, Plan, and Auto. Bypass permissions is not available.
- Sessions can be Private or Team (Enterprise/Team) or Private or Public (Max/Pro). Slack-created sessions on Team/Enterprise use Team visibility.
- Auto-fix watches a PR for CI failures and review comments when the GitHub App is installed. `/autofix-pr` from the terminal spawns a cloud session and turns auto-fix on.
- Each Anthropic-hosted session runs in an isolated VM with network controls, credentials kept outside the sandbox, branch-restricted git push, audit logging, and VM reclaim after inactivity.
- Repository clone and PR creation require GitHub. GitHub Enterprise Server is supported on Team and Enterprise. GitLab, Bitbucket, and other remotes can be bundled with `CCR_FORCE_BUNDLE=1` but cannot push back.

### Mobile

Primary source: https://code.claude.com/docs/en/mobile

- The Claude app for iOS and Android is a client, not an execution host. Cloud sessions, projects, Remote Control, and Dispatch are reached from the app.
- `/mobile`, `/ios`, and `/android` show a QR code for the store listing. Sign-in uses the same claude.ai account. Console API keys and third-party providers cannot reach cloud sessions or Remote Control.
- Cloud sessions and Remote Control live in the Code tab. Dispatch is messaged as a task. Dispatch requires Pro or Max.
- Remote Control can send photos and other attachments to the local session. Push notifications fire when a long task finishes or Claude needs a decision.
- The app cannot run terminal-only commands such as `/plugin` and `/resume`. Bypass permissions cannot be selected. Auto is not offered for Remote Control sessions.

### Remote Control

Primary source: https://code.claude.com/docs/en/remote-control

- Remote Control drives a local CLI, Desktop, or VS Code session from claude.ai/code or the Claude mobile app. Execution and files stay on the machine.
- Start with `claude remote-control`, `/remote-control`, or `claude --remote-control`. On Team and Enterprise it is admin-enabled. Source: https://code.claude.com/docs/en/feature-availability
- The machine must stay on. If it sleeps, Claude Code reconnects when it wakes.
- Session traffic uses the Anthropic API over TLS. While connected, the transcript is stored on Anthropic servers to sync across devices. Source: https://code.claude.com/docs/en/security

### Chrome

Primary source: https://code.claude.com/docs/en/chrome

- Claude Code connects to the Claude in Chrome extension (v1.0.36+) for browser automation from the CLI or VS Code. It shares the browser's login state.
- Works with Chrome, Edge, and other Chromium browsers (Brave, Arc, Vivaldi, Opera). Not supported in WSL.
- Requires a direct Anthropic plan (Pro, Max, Team, or Enterprise) and `/login`. API keys, `claude setup-token`, and third-party providers cannot authenticate the extension.
- Documented actions include live debugging, form testing, data extraction, file uploads (up to 10 MB), GIF session recording, and acting in logged-in web apps.
- Enable with `claude --chrome` or `/chrome`. Site permissions inherit from the extension settings.

### Computer use

Primary source: https://code.claude.com/docs/en/computer-use

- Computer use is a research preview. In the CLI it is macOS-only, Pro or Max, interactive sessions only (not `-p`). In Desktop it is macOS and Windows, Pro or Max. Source: https://code.claude.com/docs/en/desktop
- Claude opens apps, clicks, types, and sees the screen. It is reserved for GUIs that MCP, Bash, and Chrome cannot reach.
- CLI enablement is the built-in `computer-use` MCP server, off by default, plus macOS Accessibility and Screen Recording. Apps are approved per session.
- Only one session can hold the computer-use lock. Other apps are hidden while Claude works. The terminal is excluded from screenshots. `Esc` aborts.

### Slack

Primary source: https://code.claude.com/docs/en/slack

- `@Claude` in a Slack channel can start a Claude Code cloud session. It works in public and private channels, not DMs.
- The earlier per-user Slack integration remains the setup path on Pro and Max. Anthropic is retiring it for Team and Enterprise in favor of Claude Tag.
- Claude Tag runs `@Claude` as the organization's shared identity with admin-configured access on Team and Enterprise. Channel sessions use organization-level environments. Source: https://code.claude.com/docs/en/platforms
- Routing modes are Code only and Code + Chat. Actions include View Session, Create PR, Retry as Code, and Change Repo.
- Each earlier-version session runs under the person's Claude account, repositories, and plan limits. Requires cloud sessions and a connected GitHub repo.
- Limitations: GitHub only, one PR per session, and cloud session access.

### Projects

Primary source: https://code.claude.com/docs/en/claude-projects

- Projects are a public beta on Pro and Max. They are not on Team or Enterprise yet. Rollout is gradual; a waitlist exists when the sidebar item is missing.
- One coordinating conversation starts parallel threads. Threads are usually cloud sessions. A thread can run on the local machine through Remote Control when asked.
- Every new thread gets the project's repositories or uploaded files, instructions, memory, repo `CLAUDE.md` and skills, and the account's connectors.
- The Overview pane tracks thread state, a Library of files, pull requests, and routines. Cloud threads do not load the local machine's Claude Code setup.
- Create at claude.ai/code, in the desktop Code tab, or in the Claude mobile app. Continue as a project can promote an existing cloud session.

### Routines

Primary source: https://code.claude.com/docs/en/routines

- Routines are a research preview. A routine is a saved prompt, repositories, and connectors that run as a full cloud session without a permission-mode picker.
- Triggers are schedule (minimum one hour), API POST with a bearer token, and GitHub events. A routine can combine triggers.
- Create at claude.ai/code/routines, from Desktop (Cloud routine), or with `/schedule` (alias `/routines`) in the CLI.
- Available on Pro, Max, Team, and Enterprise. Team and Enterprise Owners can disable routines in admin settings.
- Routines belong to the individual account, count against that account's daily run allowance, and act as the person on GitHub and connectors.

### Channels

Primary source: https://code.claude.com/docs/en/channels

- Channels are a research preview. An MCP server pushes events into an already-open local session so Claude can reply while the person is away.
- Official plugins in the preview include Telegram, Discord, and iMessage. Fakechat is a localhost demo. Each plugin requires Bun.
- Requires claude.ai or a Console API key. Not available on Bedrock, Agent Platform, or Foundry. Team and Enterprise must enable channels.
- Enable per session with `--channels`. Sender allowlists gate who can push. Permission relay can forward tool prompts to the chat app.

### How Claude Code works

Primary source: https://code.claude.com/docs/en/how-claude-code-works

- A session loops through gather context, take action, and verify. The person can interrupt with `Esc` or queue a correction.
- Built-in tool categories are file operations, search, execution, web, and code intelligence (language-server plugins).
- Claude can switch models with `/model` or `claude --model`. Sonnet and Opus are the documented tradeoff pair.
- Sessions save to plaintext JSONL under `~/.claude/projects/`. File edits are checkpointed so `Esc` twice or an undo request can restore files. Checkpoints do not cover remote side effects.
- Context includes conversation, file contents, command output, `CLAUDE.md`, auto memory, skills, and system instructions. Auto-compaction summarizes as the window fills. `/context` shows usage.
- Attribution lines such as `Co-Authored-By` can be changed with `attribution` or turned off with `includeGitInstructions`.
- `/init` generates a starter `CLAUDE.md`. `/doctor` runs a setup checkup.

### Memory

Primary source: https://code.claude.com/docs/en/memory

- `CLAUDE.md` is human-written persistent instruction. Claude also reads `AGENTS.md` on its own or alongside `CLAUDE.md`.
- Scopes are managed policy (org-wide path), user (`~/.claude/CLAUDE.md`), project (`./CLAUDE.md` or `./.claude/CLAUDE.md`), and local (`./CLAUDE.local.md`, typically gitignored).
- Nested `CLAUDE.md` files load as Claude works in those directories. `@path` imports additional files up to four hops.
- `.claude/rules/` can scope instructions to file paths. Auto memory writes learnings Claude saves; the first 200 lines or 25KB of `MEMORY.md` load each session.
- Instructions are context, not enforcement. A `PreToolUse` hook is the documented way to block an action regardless of model choice.

### Skills

Primary source: https://code.claude.com/docs/en/skills

- A skill is a `SKILL.md` workflow or knowledge file. Invoke with `/name`, or let Claude load it when the description matches.
- Custom commands in `.claude/commands/` still work and are treated as skills. Skills follow the Agent Skills open standard plus Claude Code extensions.
- Bundled skills include `/doctor`, `/code-review`, `/batch`, `/debug`, `/loop`, `/claude-api`, `/run`, `/verify`, and `/run-skill-generator`. `disableBundledSkills` turns them off.
- Descriptions load at session start; full content loads when used. `disable-model-invocation: true` hides a skill until the person invokes it.

### Hooks

Primary source: https://code.claude.com/docs/en/hooks-guide

- Hooks run a shell command, HTTP request, MCP tool, prompt, or subagent at lifecycle events such as `PostToolUse`, `SessionStart`, prompt submission, permission requests, and compaction.
- They fire deterministically on the event. Use them for format-on-edit, lint before commit, notifications, and blocking unsafe commands.
- Hooks merge from user, project, plugin, and managed sources. Managed settings can restrict hooks and HTTP hook URLs. Source: https://code.claude.com/docs/en/admin-setup

### MCP

Primary source: https://code.claude.com/docs/en/mcp

- Model Context Protocol connects Claude Code to external tools and data. The overview names Google Drive, Jira, Slack, and custom servers. Source: https://code.claude.com/docs/en/overview
- Add servers with `claude mcp`, `/mcp`, or project config. `claude mcp login` runs an OAuth flow from the shell. Source: https://code.claude.com/docs/en/cli-reference
- Tool search defers full MCP schemas until a tool is used. Connectors from claude.ai load only when a claude.ai subscription is the active auth method. Source: https://code.claude.com/docs/en/feature-availability
- Admins can allowlist, denylist, or deploy managed MCP servers. Source: https://code.claude.com/docs/en/admin-setup

### Agents and parallel work

Primary source: https://code.claude.com/docs/en/agents

- Subagents run a side task in isolated context and return a summary. Custom subagents live under `.claude/agents/`.
- Agent view (`claude agents`) is a research preview for dispatching and watching background sessions.
- Agent teams are experimental and disabled by default. A lead coordinates teammates with a shared task list and messaging.
- Dynamic workflows are scripts Claude writes that run many subagents and return one result. `/workflows` lists runs.
- `/batch` splits a large change into 5 to 30 worktree-isolated subagents. Worktrees isolate parallel checkouts.
- Cross-session messaging lets Claude list and message other sessions on the machine, and, with Remote Control, sessions on other machines or in the cloud.

### Plugins

Primary source: https://code.claude.com/docs/en/plugins/overview

- A plugin is a directory of skills, agents, hooks, MCP servers, or other components, usually with `.claude-plugin/plugin.json`.
- Install from a marketplace via `/plugin` or `claude plugin`. Anthropic's official marketplace is added on first interactive terminal session unless policy blocks it.
- Install scopes are user, project (committed `.claude/settings.json`), and local. Cloud sessions do not load plugins from local settings.
- Organizations can allowlist or block marketplaces, force-install plugins, and require plugin-only customization. Source: https://code.claude.com/docs/en/admin-setup
- Code intelligence plugins connect language servers so Claude sees type errors after edits and navigates by symbol. Source: https://code.claude.com/docs/en/features-overview

### Code Review

Primary source: https://code.claude.com/docs/en/code-review

- Managed GitHub PR review is a research preview for Team and Enterprise. It is not available with Zero Data Retention. Other plans can review a local diff with `/code-review`.
- An Owner enables it and picks repositories. Triggers are once after PR creation, after every push, or manual via `@claude review`.
- Multiple agents analyze the diff against the full codebase. Findings are tagged Important, Nit, or Pre-existing and posted as inline comments. The check run is always neutral.
- Tune reviews with `CLAUDE.md` or `REVIEW.md`. Fork PRs review only when someone comments `@claude review`.

### GitHub Actions

Primary source: https://code.claude.com/docs/en/github-actions

- `anthropics/claude-code-action` runs Claude Code in repository workflows. `@claude` in an issue or PR comment can analyze, edit, and push. A `prompt` input runs without a mention.
- `/install-github-app` installs the Claude GitHub App, writes a secret, and opens a workflow PR. Manual setup is also documented.
- Auth is `ANTHROPIC_API_KEY`, `CLAUDE_CODE_OAUTH_TOKEN` from `claude setup-token`, or Console workload identity federation. Bedrock, Agent Platform, and Foundry have a separate guide.
- The GitHub App is shared with Code Review and web auto-fix. A custom app can limit permissions to the Action only.

### GitLab CI/CD

Primary source: https://code.claude.com/docs/en/gitlab-ci-cd

- Claude Code for GitLab CI/CD is beta and maintained by GitLab. Jobs run the CLI or Agent SDK in isolated runners and return changes as merge requests.
- Triggers include web, merge-request events, and `@claude` comments when a listener is configured.
- Providers documented are the Claude API, Amazon Bedrock (OIDC), and Google Cloud's Agent Platform (Workload Identity Federation).
- Claude can create and update MRs, implement from issues, fix bugs, and iterate on follow-up comments. `CLAUDE.md` is read during runs.

### Permissions and sandboxing

Primary source: https://code.claude.com/docs/en/permissions

- Permission modes include Manual (`default`), Accept edits, Plan, Auto, Bypass permissions, and CLI-only `dontAsk`. Cycle modes with `Shift+Tab` in the CLI.
- Auto uses a classifier to review most actions. On v2.1.283 or later it is the built-in start mode for interactive terminal and VS Code sessions. Organizations can set `disableAutoMode`.
- Allow, ask, and deny rules live in settings from org policy down to the session. Sandboxed Bash isolates filesystem and network. Source: https://code.claude.com/docs/en/security
- In Manual mode, writes stay inside the start directory unless extra directories are granted. Read-only Bash commands such as `ls`, `cat`, and `git status` run without asking.

### Administration

Primary source: https://code.claude.com/docs/en/admin-setup

- Managed settings override developer config. Delivery is the claude.ai admin console (Team/Enterprise), MDM plist or Windows registry, or a managed-settings file on disk.
- Server-managed settings refresh hourly. File and OS policy work with any provider; Bedrock, Agent Platform, and Foundry can use a Claude apps gateway for remote delivery.
- Controls include permission lockdown, sandbox domain allowlists, managed `CLAUDE.md`, MCP and marketplace restrictions, hook restrictions, login method and org UUID, agent-view disable, model and effort caps, and version floors.
- SSO, SCIM, and seat assignment are configured at the Claude account level, not only in Claude Code settings.
- Owners create organization-shared cloud environments and pick a default at claude.ai/admin-settings/claude-code.
- Analytics dashboards are on Team and Enterprise (claude.ai) and Console. The Enterprise Analytics API is Enterprise-only. OpenTelemetry export is available on every provider. Source: https://code.claude.com/docs/en/feature-availability
- A self-hosted Claude apps gateway adds SSO, per-group model access, OTLP telemetry, and per-developer spend limits. Source: https://code.claude.com/docs/en/feature-availability

### Security and data

Primary source: https://code.claude.com/docs/en/security

- Anthropic publishes SOC 2 Type 2 and ISO 27001 materials at the Trust Center.
- Safeguards include permission prompts, sandboxed bash, working-directory write bounds, web-fetch isolation, first-run trust verification, and command-injection checks in Manual mode.
- Cloud sessions use isolated VMs, network allowlists, credential proxies, branch push limits, audit logs, and automatic VM cleanup.
- Consumer Free/Pro/Max accounts can allow training on Claude Code data. Team, Enterprise, API, and third-party commercial traffic is not used for training unless the customer opts in. Source: https://code.claude.com/docs/en/data-usage
- Retention is 5 years when consumer training is on, 30 days when off, and 30 days standard for commercial accounts. Qualified Enterprise accounts can request Zero Data Retention, which disables cloud session features. Source: https://code.claude.com/docs/en/data-usage
- Local transcripts stay under `~/.claude/projects/` for 30 days by default (`cleanupPeriodDays`). Feedback via `/feedback` or `/bug` is retained 5 years. Source: https://code.claude.com/docs/en/data-usage
- A BAA extends to Claude Code API traffic when the customer has a BAA and ZDR. Use is under Commercial or Consumer Terms and the Usage Policy. Source: https://code.claude.com/docs/en/legal-and-compliance

### Authentication, plans, and usage

Primary source: https://code.claude.com/docs/en/authentication

- Login methods are claude.ai (Pro, Max, Team, Enterprise), Anthropic Console (with or without an API key), Bedrock, Agent Platform, Foundry, and a self-hosted Claude apps gateway with SSO.
- Features that require a Claude subscription include cloud sessions, mobile Code, Slack coding, Desktop, Routines, Ultrareview, Remote Control, Chrome, computer use, Artifacts, and voice dictation. Source: https://code.claude.com/docs/en/feature-availability
- Team adds Code Review, analytics, server-managed settings, and SSO. Enterprise adds SCIM, the Compliance API, and optional ZDR. Source: https://code.claude.com/docs/en/feature-availability
- Claude Code charges by API token consumption for Console and provider billing. Subscription plan prices are on claude.com/pricing. `/usage` shows session tokens and, on subscriptions, plan-limit bars. Source: https://code.claude.com/docs/en/costs
- Across enterprise deployments the docs state an average of about $13 per developer per active day and $150–250 per developer per month, with 90% of users below $30 per active day. Source: https://code.claude.com/docs/en/costs
- Cloud sessions share the account's rate limits. There is no separate compute charge for the Anthropic-hosted VM. Source: https://code.claude.com/docs/en/claude-code-on-the-web

### Agent SDK

Primary source: https://code.claude.com/docs/en/agent-sdk/overview

- The Agent SDK is a Python and TypeScript library that runs the Claude Code binary with the same tools, loop, permissions, sessions, hooks, skills, and plugins.
- It is distinct from the interactive CLI, the Client SDK (raw API), and Managed Agents (Anthropic-hosted harness).
- Other languages can drive the loop with `claude -p` and `--output-format json`.
- Third-party products must use API key auth, not claude.ai login or subscription rate limits, unless Anthropic has approved otherwise.
- Branding may say "Claude Agent" or "Powered by Claude". "Claude Code" as a product name for a third-party agent is not permitted.

### Artifacts

Primary source: https://code.claude.com/docs/en/artifacts

- An artifact is a live HTML or Markdown page published from a session to a private claude.ai URL. It updates in place as the session continues.
- Available on Pro, Max, Team, and Enterprise (admin-enabled on Enterprise). Requires `/login`. Source: https://code.claude.com/docs/en/feature-availability
- Share privately, with the organization, or as a public link. Pages can pull live data through MCP connectors. There is no backend or multi-route hosting.

### Built-in tools

Primary source: https://code.claude.com/docs/en/tools-reference

- File and edit tools include `Read`, `Write`, `Edit`, `NotebookEdit`, `Glob`, and `Grep`. `Bash` runs the shell; `PowerShell` is the native Windows shell tool.
- Web tools are `WebFetch` and `WebSearch`. `LSP` provides language-server navigation after a code-intelligence plugin is installed.
- Orchestration tools include `Agent`, `Skill`, `Workflow`, `AskUserQuestion`, `SendMessage`, `ListAgents`, task-list tools, and `Monitor`.
- `CronCreate` / `CronDelete` / `CronList` schedule prompts inside a session (`/loop`). `RemoteTrigger` creates and runs Routines on claude.ai.
- `Artifact` publishes a page. `PushNotification` sends desktop and, with Remote Control, phone push. `EnterPlanMode` / `ExitPlanMode` gate plan approval.

## Sources

- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/platforms
- https://code.claude.com/docs/en/how-claude-code-works
- https://code.claude.com/docs/en/features-overview
- https://code.claude.com/docs/en/cli-reference
- https://code.claude.com/docs/en/vs-code
- https://code.claude.com/docs/en/jetbrains
- https://code.claude.com/docs/en/desktop
- https://code.claude.com/docs/en/desktop-scheduled-tasks
- https://code.claude.com/docs/en/claude-code-on-the-web
- https://code.claude.com/docs/en/mobile
- https://code.claude.com/docs/en/remote-control
- https://code.claude.com/docs/en/chrome
- https://code.claude.com/docs/en/computer-use
- https://code.claude.com/docs/en/slack
- https://code.claude.com/docs/en/claude-projects
- https://code.claude.com/docs/en/routines
- https://code.claude.com/docs/en/channels
- https://code.claude.com/docs/en/memory
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/hooks-guide
- https://code.claude.com/docs/en/mcp
- https://code.claude.com/docs/en/agents
- https://code.claude.com/docs/en/plugins/overview
- https://code.claude.com/docs/en/code-review
- https://code.claude.com/docs/en/github-actions
- https://code.claude.com/docs/en/gitlab-ci-cd
- https://code.claude.com/docs/en/permissions
- https://code.claude.com/docs/en/admin-setup
- https://code.claude.com/docs/en/security
- https://code.claude.com/docs/en/data-usage
- https://code.claude.com/docs/en/legal-and-compliance
- https://code.claude.com/docs/en/authentication
- https://code.claude.com/docs/en/feature-availability
- https://code.claude.com/docs/en/costs
- https://code.claude.com/docs/en/agent-sdk/overview
- https://code.claude.com/docs/en/artifacts
- https://code.claude.com/docs/en/tools-reference
