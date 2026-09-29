---
name: Cursor
slug: cursor
url: https://cursor.com/
docs: https://cursor.com/docs
kind: product
reviewed: 2026-09-28
---

# Cursor

## Product

Cursor is a coding agent for understanding a codebase, planning and building features, fixing bugs, reviewing changes, and working with existing development tools. An organization adopts the Cursor product: the desktop editor, Agents Window, CLI, web agents surface, iOS app, cloud agents, automations, and team or enterprise administration. The model selected for a run is part of that chassis.

Individuals download a desktop app for macOS 12 and later (Apple Silicon and Intel), Windows 10 and later, or Linux (apt, yum/dnf, or AppImage). After sign-in they open a folder and work in Agent (`Cmd/Ctrl+I`), or they switch to the Agents Window to run and review agents across local, cloud, and remote SSH workspaces. The same agent is available from the terminal via `agent`, from cursor.com/agents, and from Cursor for iOS. Cloud Agents require a paid plan and a source-control connection before they can start from a repository.

Individual plans are Start (India only), Pro, Pro Plus, and Ultra. Start covers the Cursor Models pool and Cloud Agents; it does not include the Other Models pool, on-demand usage, Bugbot, Auto, Automations, or the Cursor SDK. Pro, Pro Plus, and Ultra include Tab completions, agent usage, Bugbot, and Cloud Agents. Teams offers Standard ($40/user/mo) and Premium ($120/user/mo) seats plus an unpaid admin seat. Enterprise is a custom plan with pooled usage, invoicing, SCIM, and additional security controls.

Grok Bot (named AI teammates on a persistent cloud computer) and Origin (Cursor's git forge, early beta) are documented on the same docs host. They are out of scope for this dossier. No sibling spec files exist for those products. Sources: https://cursor.com/docs/grok-bot, https://cursor.com/docs/origin

## Features

### Agent

Primary source: https://cursor.com/docs/agent/overview

- Agent completes coding tasks, runs terminal commands, and edits files from the side pane with `Cmd/Ctrl+I`.
- An agent is instructions (system prompt and rules), tools, and a selected model. Cursor tunes instructions and tools per supported model.
- Tools include file and folder search, web search, fetch rules, reading files (including images for vision-capable models), editing files, shell commands, browser control, image generation (saved to `assets/` by default), and asking clarifying questions while work continues.
- There is no documented limit on the number of tool calls in a task.
- Checkpoints snapshot modified files before significant changes. Restoring a checkpoint reverts files only; it does not remove chat messages. Checkpoints are local and separate from Git.
- Messages can be queued while Agent works, sent immediately with `Cmd+Enter`, or used to steer the active turn at the next tool call.
- Side chats (`/side` or `/btw`) are durable conversations that use the parent thread as hidden context.
- Conversation search indexes past transcripts locally from the Agents Window (`Cmd/Ctrl+K`).
- `/goal` gives a long-lived objective. It is rolling out. In the CLI, `Ctrl+C` pauses a goal. Pair it with a Custom Mode or `/loop`. Source: https://cursor.com/docs/agent/overview
- Plan Mode researches the codebase, asks questions, writes an editable plan, and waits for approval before building. Toggle with `Shift+Tab` or the mode picker. Plans save to the home directory by default; "Save to workspace" moves them into the project. Source: https://cursor.com/docs/agent/plan-mode
- Debug Mode generates hypotheses, adds instrumentation to a local debug server, asks the user to reproduce the bug, then applies a targeted fix and removes instrumentation. Source: https://cursor.com/docs/agent/debug-mode
- Design Mode lives in the browser inside the Agents Window (`Cmd+Shift+D`). Users click elements, multi-select, draw on a frozen viewport, or narrate by voice. The agent receives xpath, component, styles, fiber props, and a screenshot. Source: https://cursor.com/docs/agent/design-mode
- Ask mode is read-only exploration: Agent answers questions without editing. Source: https://cursor.com/help/ai-features/ask-mode
- Tab suggests completions from recent edits, surrounding code, and linter errors. It can edit multiple lines, add imports, jump to the next edit location, and propose cross-file edits. Source: https://cursor.com/help/ai-features/tab
- Inline edit (`Cmd/Ctrl+K`) applies a described change to a selection. `Opt/Alt+Return` switches to question mode. `Cmd/Ctrl+L` opens Agent with the selection as context. Source: https://cursor.com/help/ai-features/inline-edit
- Worktrees give each task an isolated Git checkout. UI-native worktrees are Agents Window only; the IDE uses `/worktree` and `/best-of-n`. Setup is `.cursor/worktrees.json`. Source: https://cursor.com/docs/configuration/worktrees
- Agent Review runs a local code review automatically after commits or on demand (`/agent-review` or the Source Control tab). Depth is Quick or Deep. It reads `BUGBOT.md` repository rules. From Cursor 3.11 the setting moves to Git & PRs > Pull Requests. Source: https://cursor.com/docs/agent/agent-review
- Reading files and searching code do not require approval. Workspace file edits save immediately except configuration files, which need approval. Terminal commands need approval by default. MCP connections and each MCP tool call need approval unless allowlisted. Source: https://cursor.com/docs/agent/security
- `.cursorignore` blocks agent access to listed files. Source: https://cursor.com/docs/agent/security
- Workspace trust is disabled by default. When enabled, restricted mode breaks AI features. Organizations can enforce it through MDM. Source: https://cursor.com/docs/agent/security
- Run Modes (Settings > Agents > Approvals & Execution) are Auto-review, Allowlist, and Run Everything. Auto-review is the documented default as of Cursor 3.6. Sandboxing uses Seatbelt on macOS and Landlock/seccomp on Linux. Cloud Agents do not use Run Modes. Source: https://cursor.com/docs/agent/security/run-modes
- Browser tools can navigate, click, type, scroll, screenshot, read console output, and monitor network traffic (network traffic is Agent panel only). Session cookies and storage persist per workspace. Approval modes are manual, allow-listed, or auto-run. Enterprise can toggle browser MCP and set an origin allowlist (v2.1+; must be enabled for the org). Source: https://cursor.com/docs/agent/tools/browser
- The `CURSOR_AGENT` environment variable marks Cursor-run shells so users can skip heavy prompt themes. Source: https://cursor.com/docs/agent/tools/terminal

### Agents Window

Primary source: https://cursor.com/docs/agent/agents-window

- The Agents Window is an agent-first workspace across local, cloud, remote SSH, and other environments. Open it with Command Palette → Open Agents Window; return to the IDE with Open IDE.
- `Cmd+P` and `Cmd+Shift+F` search files without leaving the window.
- Features documented as Agents Window only: multi-workspace agents, a diffs view for commits and PRs, parallel cloud agents (also reachable from phone, web, Slack, GitHub, and Linear), local/cloud handoff, cloud subagents (`/in-cloud`, `/autopilot`), and worktrees.
- Agents Window is generally available with Cursor 3 (2 April 2026). For two weeks after launch, Enterprise admins can roll it out to the whole team or specific users. After that period, all users have access by default.

### Projects

Primary source: https://cursor.com/docs/agent/projects

- A Project is a larger body of work (feature, migration, or full app) directed by chatting with a coordinator agent. The coordinator plans and delegates; it does not write code itself.
- Projects live in the Agents Window left nav and run on Cloud Agents.
- Projects is rolling out to all users. It is not available on Enterprise plans. It is not available with Privacy Mode (Legacy).
- Shared context files sync across cloud and local machines used by the Project. Agents add research, artifacts, and learned workflow notes.
- Subscriptions let the coordinator watch Slack, a schedule, pull requests, CI on a branch, or other events and act without a new prompt. A Listening pill lists active subscriptions.

### Customize

Primary source: https://cursor.com/docs/customize-cursor

- The Customize page manages plugins, skills, MCPs, rules, subagents, commands, and hooks at user, workspace, or team scope.
- Users browse and install from the Cursor Marketplace, install Team MCP servers from the Default team marketplace, and see a team leaderboard of popular plugins, skills, and MCPs.
- Plugins bundle rules, skills, agents, commands, MCP servers, and hooks. Cursor supports Agent Plugins (`plugin.json`) and Cursor Plugins (`.cursor-plugin/plugin.json`). Official marketplace plugins are manually reviewed and must be open source. Source: https://cursor.com/docs/plugins
- Plugin canvases include Hex Canvas and Atlassian Canvas as shared setup templates. Source: https://cursor.com/docs/plugins
- Teams get one team marketplace; Enterprise gets unlimited team marketplaces. Installation modes are Default Off, Default On, and Required. Marketplace access can be scoped to Organization Groups. Source: https://cursor.com/docs/plugins
- Members on Teams and Enterprise can publish a personal skill from `~/.cursor/skills/` to the Default marketplace unless an admin turns publishing off. Source: https://cursor.com/docs/plugins
- Rules are Project Rules (`.cursor/rules` `.mdc` files), User Rules, Team Rules (Team and Enterprise), and `AGENTS.md` (root and nested). Application types are Always Apply, Apply Intelligently, Apply to Specific Files, and Apply Manually. Precedence is Team Rules → Project Rules → User Rules. Rules do not apply to Tab or Inline Edit. Source: https://cursor.com/docs/rules
- Skills are `SKILL.md` packages discovered from `.agents/skills/`, `.cursor/skills/`, user-level `~/.cursor/skills/` and `~/.agents/skills/`, plus Claude and Codex skill directories. Built-in skills include `/automate`, `/autopilot`, `/canvas`, `/create-hook`, `/create-rule`, `/create-skill`, `/create-subagent`, `/cursor-blame`, `/loop`, `/migrate-to-skills`, `/review`, `/review-bugbot`, `/review-security`, `/sdk`, `/shell`, `/split-to-prs`, `/statusline`, `/update-cli-config`, and `/update-cursor-settings`. Source: https://cursor.com/docs/skills
- Sync Skills for Cloud Agents copies `~/.cursor/skills/` for the user's own Cloud Agents. Team admins can disable sync. Source: https://cursor.com/docs/skills
- Subagents run in their own context window in the editor, CLI, and Cloud Agents. Built-in subagents are Explore, Bash, and Browser. Custom subagents live in `.cursor/agents/`. Foreground subagents block; background subagents return immediately. Source: https://cursor.com/docs/subagents
- Hooks are scripts in `hooks.json` that observe, block, or modify the agent loop over stdio JSON. Categories include agent hooks (`preToolUse`, `beforeShellExecution`, `afterFileEdit`, `subagentStart`/`subagentStop`, and others), Tab hooks, and `workspaceOpen`. Cloud Agents run repository `.cursor/hooks.json` command-based hooks once they have a writable environment. Enterprise plans also run team and enterprise-managed hooks. Source: https://cursor.com/docs/hooks
- MCP connects external tools over stdio, SSE, or Streamable HTTP. Cursor supports tools, prompts, resources, roots, elicitation, and MCP Apps UI. Config lives in `.cursor/mcp.json` or `~/.cursor/mcp.json`. Enterprise admins set an MCP allowlist and network modes. Source: https://cursor.com/docs/mcp

### Cloud Agents

Primary source: https://cursor.com/docs/cloud-agent

- Cloud Agents use the same agent fundamentals in isolated cloud VMs with cloned repos, dependencies, secrets, startup commands, and network access. They were formerly called Background Agents.
- They run in parallel without the local machine staying online. They can build, test, use a desktop and browser, and work across multiple repositories, opening pull requests in each repo they change.
- An account admin must connect source control before anyone starts an agent from a repository. Supported hosts are GitHub (Cloud and Enterprise Server), GitLab (Cloud and Self-Hosted), Bitbucket Cloud, and Azure DevOps. Start from scratch starts without a repository.
- Start points are Cursor for iOS, cursor.com/agents, the desktop app (Cloud in the agent input dropdown), Slack `@cursor`, a GitHub or Bitbucket `@cursor` comment, Linear `@cursor`, or the API. Android uses cursor.com/agents in Chrome or a PWA.
- Environments are configured with agent-led setup, a saved snapshot, or a Dockerfile via `.cursor/environment.json`. Resolution order is repo `.cursor/environment.json`, then a personal saved environment, then a team saved environment. Builds prepare install scripts in the background. Source: https://cursor.com/docs/cloud-agent/setup
- Start from scratch needs a paid plan and Origin. Cursor creates a draft Origin repository; Create repo publishes it. Port forwarding and Design Mode preview the app. Publish deploys via the Vercel plugin. If Origin is off for the team, the agent starts without a repository. Source: https://cursor.com/docs/cloud-agent/setup
- Cursor-configured Dockerfiles are private beta for Enterprise teams. Source: https://cursor.com/docs/cloud-agent/setup
- Computer use lets the agent drive mouse, keyboard, desktop, and browser. Artifacts include screenshots, videos, and logs. Users can take remote desktop control and hand it back. Source: https://cursor.com/docs/cloud-agent/capabilities
- Team MCP servers (HTTP and stdio, OAuth per user) are available. HTTP tool calls are proxied; stdio runs in the VM. Cursor Cloud MCP exposes run diagnostics. Team admins can disable it. Source: https://cursor.com/docs/cloud-agent/capabilities
- Subscriptions wake an agent on GitHub PR/CI events, Slack replies, Linear issue events, or timers (max 180 days). `/subscribe` and `/loop` are built-in skills. Source: https://cursor.com/docs/cloud-agent/capabilities
- On Teams, Cloud Agents automatically try to fix CI failures on PRs they create (GitHub Actions only), with skip rules and `@cursor autofix off`/`on`. Source: https://cursor.com/docs/cloud-agent/capabilities
- VMs can mint short-lived OIDC JWTs and serve agent metadata from a local socket. Source: https://cursor.com/docs/cloud-agent/capabilities
- Teammates on the same Cursor team who also have repository access can open a run read-only. Team follow-ups (Disabled, Service accounts only, or All) let others send messages. Source: https://cursor.com/docs/cloud-agent/settings
- Billing is API pricing for the selected model, with an optional context-window size. Users set a spend limit on first use. A paid Cursor plan is required.
- Secrets are workspace/team-scoped and injected at start. Already-running agents do not pick up new secrets.
- Each run uses a dedicated Firecracker-based microVM in a separate AWS account. Data is TLS 1.2+ in transit and AES-256 at rest with per-agent keys. Enterprise can use CMEK/BYOK. Commits are signed with an HSM-backed Ed25519 key. Source: https://cursor.com/docs/cloud-agent/security
- Access is inherited from the triggering user's Git access. Protected Git Scopes lock a Git org to the Cursor org. A repository blocklist excludes repos. Source: https://cursor.com/docs/cloud-agent/security
- Network modes are allow all, default plus allowlist, or allowlist only. Enterprise can lock the policy. Source: https://cursor.com/docs/cloud-agent/settings
- Cursor for iOS (App Store, iOS/iPadOS 26.0+, English) starts and reviews cloud agents, merges PRs, uses Design Mode and voice, and supports Remote Control of a local Agents Window session (Cursor 3.9.8+; Pro and above with Cloud Agents access). It is not an IDE or admin console. Android is planned. Source: https://cursor.com/docs/cloud-agent/mobile

### Automations

Primary source: https://cursor.com/docs/cloud-agent/automations

- Automations run Cloud Agents on a schedule or on events from GitHub, GitLab, Slack, webhooks, Linear, Sentry, PagerDuty, and more.
- Create them in the Agents Window, at cursor.com/automations, with `/automate`, or from a Marketplace template.
- Cursor-managed agents on the Automations page are Bugbot, Security Agents, and PR Routing & Approval.
- Triggers include cron, source-control PR/push/comment events (GitHub has the widest set), Slack channel/emoji/channel-created (public channels only), webhook POST with an API key, Linear issue/status/cycle, Sentry issues, and PagerDuty incidents. Fork PRs are not supported except merged-PR triggers.
- Tools include PR creation, PR comments and optional approvals, request reviewers, Slack send/read, MCP, memories (`MEMORIES.md` by default), and computer use.
- Team Share sets Run as (Me or a dedicated service account) and Access (Private, Members can view, Members can edit). Usage bills to the creator or the team pool.
- Automations always use each model's maximum context window. They are billed as Cloud Agent usage. Start does not include Automations.

### Bugbot

Primary source: https://cursor.com/docs/bugbot

- Bugbot reviews pull requests for bugs, security issues, and code quality, and leaves comments with explanations and fix suggestions.
- It runs automatically on PR updates or when someone comments `cursor review` or `bugbot run`.
- It uses existing PR comments as context. Fix in Cursor and Fix in Web links open the issue in the editor or cursor.com/agents.
- Providers: GitHub (including Enterprise Server), GitLab (including Self-Hosted), Bitbucket (including Data Center), and Azure DevOps Services.
- CI statuses: GitHub check `Cursor Bugbot`, Bitbucket key `cursor-bugbot`, Azure DevOps context `cursor-bugbot/review`. Conclusions are success, neutral, or failure (when fail-on-unresolved is configured).
- Individual, Team, and Enterprise settings control per-repo enablement, mention-only runs, once-per-PR, draft PRs, and reviewer allow/deny lists. On team repos Bugbot runs for all contributors, not only Cursor team members.
- Pro and above include Bugbot. Start does not.

### Security Agents

Primary source: https://cursor.com/docs/security-agents

- Security Agents scan for security bugs, risky patterns, and vulnerabilities. They require Cloud Agents and run on Automations.
- Security Reviewer checks pull requests. Vulnerability Scanner scans a codebase on a cron schedule.
- Both types have built-in checks, custom instructions, and optional tools/MCPs. A Reviewer needs at least one tool or MCP to save. A Scanner reports to Flagged vulnerabilities without one.
- `/review-security` and `/review` run the Security Agent from the editor, cursor.com/agents, or CLI (Cursor 3.7+).
- Usage bills to the team pool under a shared service account.
- Analytics track vulnerabilities found, issues fixed, and resolution rate. Fix in Cursor starts a Cloud Agent. View in codebase opens the scan in Origin when Origin is enabled.
- Security Agents require a team or enterprise plan.

### PR Routing & Approval

Primary source: https://cursor.com/docs/approval-agents

- PR Routing & Approval assigns reviewers from code ownership and commit history and can approve low-risk PRs against configured criteria.
- It can wait on Bugbot and Security Agent findings, apply risk scoring and a maximum risk threshold, and read `APPROVAL_POLICY.md` files plus `.cursor/approval-policies/ROUTING.md`.
- Supported repositories are GitHub and Origin only. GitLab, Bitbucket, and Azure DevOps must be removed before save.
- Triggers include PR opened, PR pushed/updated, and PR commented (regex).
- Required actions are Request Reviewers and/or Approve PR. Optional Slack, Microsoft Teams, and MCP tools are available.
- On Teams, every member can create and edit the agent. On Enterprise, only team admins can edit.

### Rollouts

Primary source: https://cursor.com/docs/rollouts

- Rollouts watches a pull request from review to production: it writes a rollout plan, checks telemetry after deploy, and reports health per environment.
- Available on Teams and Enterprise. Watches Origin, GitHub, GitLab.com, and Bitbucket Cloud (up to 200 repos).
- On GitHub, GitLab.com, and Bitbucket Cloud the plan is a PR comment. On Origin it appears on the PR page. Users with write access can revise the plan by mentioning the named handle.
- Deploy events come from the CI pipeline via a Cursor API key. Telemetry needs at least one connected observability tool (for example Datadog). Checks run at deploy, then after 20 minutes, 1 hour, 1 day, and 3 days.
- On regression it names the suspected change, opens an issue, and notifies the author. It does not merge, revert, or roll back. Fix starts a Cloud Agent.
- Slack notifications require a team admin to add Rollouts to Slack. They are not available in Privacy Mode.

### CLI

Primary source: https://cursor.com/docs/cli/overview

- Cursor CLI installs with `curl https://cursor.com/install -fsS | bash` on macOS, Linux, and WSL, or `irm 'https://cursor.com/install?win32=true' | iex` on Windows PowerShell. Verify with `agent --version`. It auto-updates; `agent update` updates manually. Source: https://cursor.com/docs/cli/installation
- Interactive mode is `agent` or `agent "prompt"`. Modes match the editor: Agent (default), Plan (`/plan`, `--plan`), Ask (`/ask`, `--mode=ask`).
- Print mode (`-p` / `--print`) runs non-interactively for scripts and CI. `--output-format` is text, json, or stream-json. `--force` / `--yolo` applies file changes in print mode. Source: https://cursor.com/docs/cli/headless
- Prepending `&` to a message hands the conversation to a Cloud Agent.
- Sessions resume with `agent ls`, `agent resume`, `--continue`, or `--resume=id`.
- `/sandbox` or `--sandbox` toggles sandboxing and network access. Sudo prompts send the password to sudo over IPC; the model does not see it.
- MCP uses the same `mcp.json` as the editor. `agent mcp` lists, enables, and logs in to servers. ACP is `agent acp` over stdio JSON-RPC.
- The CLI loads `.cursor/rules`, `AGENTS.md`, and `CLAUDE.md`. `--worktree` runs in an isolated checkout under `~/.cursor/worktrees`. Source: https://cursor.com/docs/cli/using
- `CURSOR_API_KEY` authenticates headless scripts. Source: https://cursor.com/docs/cli/headless

### Integrations

Primary source: https://cursor.com/docs/integrations/github

- GitHub.com and GitHub Enterprise Server (v3.8+ recommended) connect repositories for Cloud Agents and Bugbot. Setup needs Cursor admin and GitHub org admin. GHES supports IP allowlists, AWS PrivateLink, and Cloudflare Tunnel. Source: https://cursor.com/docs/integrations/github
- GitLab.com and GitLab Self-Hosted require a paid GitLab plan (Premium or Ultimate) because project access tokens are unavailable on GitLab Free. Self-hosted needs Teams or Enterprise. Source: https://cursor.com/docs/integrations/gitlab
- Azure DevOps Services (`dev.azure.com`) is public beta for Cloud Agents and Bugbot. Azure DevOps Server is not supported. Automations, Bugbot autofix, and Security Agents do not support Azure DevOps yet. Source: https://cursor.com/docs/integrations/azure-devops
- Bitbucket Cloud (`bitbucket.org`) is public beta for Cloud Agents and Bugbot. Bitbucket Data Center supports Bugbot only (Teams or Enterprise) and does not support Cloud Agents. Source: https://cursor.com/docs/integrations/bitbucket
- Slack starts Cloud Agents with `@Cursor`, including repo/env/branch/model/worker/pool options, channel defaults, routing rules, and team/channel default pools. Source: https://cursor.com/docs/integrations/slack
- Microsoft Teams starts Cloud Agents with `@Cursor` and similar repo, environment, branch, and model options. Source: https://cursor.com/docs/integrations/microsoft-teams
- Linear delegates issues to Cursor or mentions `@Cursor` in comments. Agents post status and open PRs. Source: https://cursor.com/docs/integrations/linear
- Jira (Teams and Enterprise; Jira Commercial Cloud with Rovo) assigns work items to Cursor or mentions `@Cursor`. Not supported on Atlassian HIPAA or FedRAMP. Authentication is service account or per-user. Source: https://cursor.com/docs/integrations/jira
- Notion (beta; Notion Business or Enterprise) runs Cursor agents from mentions and task assignment via a user API key and the Cursor SDK. Usage bills as Cloud Agent usage. GitHub is required for PRs. Source: https://cursor.com/docs/integrations/notion
- JetBrains IDEs (2025.1+, AI Assistant plugin, paid Cursor plan) run Cursor as an ACP agent for file edits and terminal commands. Source: https://cursor.com/docs/integrations/jetbrains
- Xcode 26.3+ exposes 20 MCP tools through `xcrun mcpbridge` (builds, tests, SwiftUI previews, Apple docs search, and file operations). Requires a paid plan and Xcode running with a project open. Source: https://cursor.com/docs/integrations/xcode

### Self-Hosted Machines

Primary source: https://cursor.com/docs/cloud-agent/self-hosted

- Self-Hosted Machines move Cloud Agent tool execution to a customer-managed worker. Cursor still runs the agent loop, inference, and planning. The worker edits files, runs commands, computer-use tools, and local MCP servers.
- My Machines register a personal worker (browser login or user API key). Multiple agents can share one machine.
- Team Pools (Enterprise) register workers under a pool name with a service account API key, one agent per machine, optional controller scaling. Admins can allow or require self-hosted for all Cloud Agent runs.
- Workers open outbound HTTPS to `api2.cursor.sh`, `api2direct.cursor.sh`, and artifact S3. No inbound ports are required. Limits are 200 workers per user and 1000 per team.
- Partner host guides include AWS Lambda, Cloudflare, Namespace, Modal, Daytona, E2B, Vercel, Tensorlake, Coder, and SuperServe, plus Kubernetes (`anysphere/k8s-workers`).
- Computer use on self-hosted needs `--computer-use`: macOS helper app or Linux X11/TigerVNC stack.

### Teams

Primary source: https://cursor.com/docs/account/teams/setup

- Create a team at cursor.com/team/new-team or by upgrading from the dashboard. Billing is per active paid seat, prorated when members are added. A removed member who used credits keeps the seat until the cycle ends.
- Domain matching lets verified matching email domains join without an invite.
- An Unpaid Admin manages the team without a Cursor license. Teams need at least one paid member.
- On Teams, an account belongs to one team at a time. In an Enterprise Organization, a user can belong to multiple teams in the same org.
- Team features include centralized billing, a team marketplace, Bugbot, shared Cloud Agents and automations, usage analytics, team-wide Privacy Mode enforcement, and SAML/OIDC SSO. Source: https://cursor.com/docs/account/teams/pricing
- Seat types are Standard ($40/user/mo), Premium ($120/user/mo, 5× Agent limits), and Free unpaid admin. Usage is per user in two pools and does not transfer. On-demand usage is on by default. Monthly team-wide spend limits are available; per-member limits are Enterprise. Source: https://cursor.com/docs/account/teams/pricing
- SAML 2.0 SSO is included on Teams and Enterprise. Domain verification requires SSO for that domain. JIT provisioning is supported. Source: https://cursor.com/docs/account/teams/sso
- MDM download links are on cursor.com/downloads, with guides for Workspace ONE, Intune, and Kandji. Source: https://cursor.com/docs/account/teams/setup

### Enterprise

Primary source: https://cursor.com/docs/enterprise

- Enterprise adds organizations and organization groups, SCIM, MDM policies, repository blocklists, model access restrictions, enforceable sandbox mode, CLI and Cloud Agent user restrictions, BYOK disable, billing groups, service accounts, audit logs, SIEM streaming, OpenTelemetry export, Conversation Insights, AI Code Tracking API, Cursor Blame, HIPAA BAA, and priority support (8-hour critical / 24-hour standard first human response).
- Certifications include SOC 2 Type II. A Trust Center, security page, privacy overview, and DPA are published.
- Privacy Mode is on by default for Enterprise and can be enforced so members cannot disable it. Cloud Agents are optional; they are the feature that stores code. Source: https://cursor.com/docs/enterprise/privacy-and-data-governance
- Most models run under zero-data-retention agreements. Claude Fable 5 and 5.1 require provider retention for harm prevention and need admin approval when Privacy Mode is on. Guardrail trips route to Claude Opus. Source: https://cursor.com/docs/enterprise/privacy-and-data-governance
- US-only data residency (Enterprise, per team) keeps inference, processing, and storage in the US for eligible models and features, with a 10% model-pricing uplift. CMEK encrypts Cloud Agent data with a customer key. Source: https://cursor.com/docs/enterprise/privacy-and-data-governance
- Marketplace: Enterprise has unlimited team marketplaces, community plugin import off by default, admin-only marketplace edits, and SCIM-gated marketplace access.

### Models & Pricing

Primary source: https://cursor.com/docs/models-and-pricing

- Two monthly usage pools: Cursor Models (Grok 4.7, Grok 4.6, Grok 4.5, Composer 2.5) and Other Models (third-party models at API price). Start includes only Cursor Models.
- Individual list prices: Start ₹649/mo tax inclusive (India); Pro $20/mo; Pro Plus $60/mo; Ultra $200/mo. After included usage, users add on-demand usage or upgrade. Requests are not downgraded.
- Auto has Cost, Balance, and Intelligence modes. On Teams and Enterprise, Cursor Router picks the model for Auto. All Auto modes bill at the routed model's list price.
- Teams and Enterprise add a Cursor Token Rate of $0.25 per million tokens on third-party model requests, including Auto-routed third-party models and BYOK. Grok and Composer are exempt.
- Max Mode (extended context at API rate plus 20%) exists only on legacy request-based plans.
- The docs list frontier models from OpenAI, Anthropic, Google, SpaceXAI/Cursor (Grok, Composer), Moonshot, Z.ai, and Meta, with per-model context windows, hidden-by-default flags, and token rates.
- Regional data residency adds a 10% uplift on eligible model pricing.

### APIs and SDK

Primary source: https://cursor.com/docs/api

- Admin API (Enterprise): members, settings, usage, spending, model access, audit logs, repo blocklists, directory groups, billing groups. Basic auth with `admin:*` keys (`crsr_…`).
- Analytics API (Enterprise): DAU, model usage, Tab, MCP/skills/plans adoption, conversation insights, leaderboard, Bugbot analytics, by-user endpoints. HTTP caching with ETags.
- AI Code Tracking API (Enterprise): per-commit and per-change AI metrics as JSON or CSV.
- Bugbot API (Enterprise): trigger reviews and retrieve per-review analytics.
- Cloud Agents API (beta, all plans): create and manage agents and runs, stream, artifacts, archive/delete, workers and pools, webhooks. Basic or Bearer auth. User or service-account keys.
- Origin API (early beta): repositories, commits, checks, pull requests, apps. Bearer via Origin CLI or Origin Apps.
- TypeScript SDK (`@cursor/sdk`, Node.js 22.13+) and Python SDK run the same agent locally or in Cursor-hosted cloud with one interface. SDK Bridge targets other languages. Start does not include the SDK. Source: https://cursor.com/docs/sdk/typescript
- Default rate limit is 20 requests/minute unless an endpoint documents a different limit. 429 responses include `Retry-After` on Admin/Organization APIs.

## Sources

- https://cursor.com/docs
- https://cursor.com/docs/get-started/quickstart
- https://cursor.com/docs/agent/overview
- https://cursor.com/docs/agent/agents-window
- https://cursor.com/docs/agent/projects
- https://cursor.com/docs/agent/agent-review
- https://cursor.com/docs/agent/plan-mode
- https://cursor.com/docs/agent/debug-mode
- https://cursor.com/docs/agent/design-mode
- https://cursor.com/docs/agent/tools/terminal
- https://cursor.com/docs/agent/tools/browser
- https://cursor.com/docs/agent/security
- https://cursor.com/docs/agent/security/run-modes
- https://cursor.com/docs/configuration/worktrees
- https://cursor.com/docs/customize-cursor
- https://cursor.com/docs/plugins
- https://cursor.com/docs/rules
- https://cursor.com/docs/skills
- https://cursor.com/docs/subagents
- https://cursor.com/docs/hooks
- https://cursor.com/docs/mcp
- https://cursor.com/docs/cloud-agent
- https://cursor.com/docs/cloud-agent/setup
- https://cursor.com/docs/cloud-agent/capabilities
- https://cursor.com/docs/cloud-agent/automations
- https://cursor.com/docs/cloud-agent/settings
- https://cursor.com/docs/cloud-agent/security
- https://cursor.com/docs/cloud-agent/self-hosted
- https://cursor.com/docs/cloud-agent/mobile
- https://cursor.com/docs/bugbot
- https://cursor.com/docs/security-agents
- https://cursor.com/docs/approval-agents
- https://cursor.com/docs/rollouts
- https://cursor.com/docs/cli/overview
- https://cursor.com/docs/cli/installation
- https://cursor.com/docs/cli/using
- https://cursor.com/docs/cli/headless
- https://cursor.com/docs/integrations/github
- https://cursor.com/docs/integrations/gitlab
- https://cursor.com/docs/integrations/azure-devops
- https://cursor.com/docs/integrations/bitbucket
- https://cursor.com/docs/integrations/slack
- https://cursor.com/docs/integrations/microsoft-teams
- https://cursor.com/docs/integrations/linear
- https://cursor.com/docs/integrations/jira
- https://cursor.com/docs/integrations/notion
- https://cursor.com/docs/integrations/jetbrains
- https://cursor.com/docs/integrations/xcode
- https://cursor.com/docs/models-and-pricing
- https://cursor.com/docs/account/teams/setup
- https://cursor.com/docs/account/teams/pricing
- https://cursor.com/docs/account/teams/sso
- https://cursor.com/docs/enterprise
- https://cursor.com/docs/enterprise/privacy-and-data-governance
- https://cursor.com/docs/api
- https://cursor.com/docs/sdk/typescript
- https://cursor.com/docs/grok-bot
- https://cursor.com/docs/origin
- https://cursor.com/help/ai-features/tab
- https://cursor.com/help/ai-features/inline-edit
- https://cursor.com/help/ai-features/ask-mode
