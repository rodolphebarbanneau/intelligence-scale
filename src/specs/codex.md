---
name: Codex
slug: codex
url: https://developers.openai.com/codex/
docs: https://developers.openai.com/codex/
kind: product
reviewed: 2026-09-28
---

# Codex

## Product

Codex is OpenAI's coding agent for software development. A person describes a goal, and Codex inspects a project, edits files, runs commands, reviews changes, debugs failures, and repeats development work such as refactors, tests, migrations, and setup. OpenAI also sells the models Codex can run; Codex is the product that hosts the agent loop, tools, surfaces, and admin controls.

ChatGPT Plus, Pro, Business, Edu, and Enterprise plans include Codex. Free and Go plans also include it for lighter use. A person can instead sign in with an OpenAI API key and pay API rates for local CLI, SDK, or IDE work; that path does not include cloud features such as GitHub code review and Slack. ChatGPT Work and Codex share usage limits on ChatGPT plans.

Codex runs on several surfaces. Local work uses the Codex CLI, the Codex IDE extension, and Codex in the ChatGPT desktop app. Cloud work runs in isolated OpenAI-managed containers started from the web, the CLI, the IDE, GitHub, GitLab (beta), Linear, or Slack. Codex Remote in the ChatGPT mobile app starts, guides, approves, and reviews tasks that run on a connected Mac or Windows PC. Pricing also lists Codex on iOS.

A typical local turn is a loop: the agent acts, reads tool output such as file reads and command results, and continues until the task finishes or the person cancels. Local commands run in an OS-enforced sandbox by default. An approval policy decides when Codex must stop and ask. Defaults live in `config.toml`. Cloud chats use a two-phase container: a setup phase that can reach the network, then an agent phase that is offline unless the environment enables internet access.

This file covers Codex only. The ChatGPT assistant is specified in `chatgpt`. ChatGPT Work, also called ChatGPT Workspace Agents, is specified in `chatgpt-work`. Those products share a docs host, some plans, and some desktop controls with Codex; they are separate product surfaces.

Official documentation lives on ChatGPT Learn at [learn.chatgpt.com/docs](https://learn.chatgpt.com/docs), reached from [developers.openai.com/codex](https://developers.openai.com/codex/). The same set documents ChatGPT, ChatGPT Work, and Codex. Codex-specific pages sit under Developers, plus the CLI, IDE, and cloud entries in Available on.

## Features

### Codex CLI

Primary source: https://learn.chatgpt.com/docs/codex/cli

- Installs with the standalone installer on macOS, Linux, and Windows, or with `npm install -g @openai/codex`, or with Homebrew `brew install --cask codex`.
- First launch in a project directory offers Sign in with ChatGPT or another available sign-in method.
- Interactive sessions inspect files, edit the local repository, run installed tools, and stream commands and diffs in one terminal loop.
- `codex resume` reopens a recent chat from the current repository or searches local chats.
- `codex --image` attaches an error screenshot, architecture diagram, or design reference to the first prompt; images can also be pasted into the composer.
- `codex --search` switches a run to live web search; search activity stays visible in the transcript.
- `codex cloud` browses active and completed cloud chats, submits work to a configured environment, and applies the result to the local repository.
- `codex mcp` adds local or remote MCP servers, authenticates when needed, and inspects tools available to the session.
- `/permissions` sets when Codex can edit files or run commands without asking, and shows the active sandbox and writable roots.
- `codex completion` generates shell completions; longer prompts open in the editor set by `VISUAL` or `EDITOR`.
- Skills and plugins package repeatable instructions and connect team tools without leaving the CLI. Source: https://learn.chatgpt.com/docs/plugins
- `/plugins` opens the CLI plugin browser to install, enable, or disable marketplace plugins. Source: https://learn.chatgpt.com/docs/plugins
- `/import` imports supported setup and recent chats from Claude Code or Cursor (up to 50 chats from the last 30 days). The command is unavailable during a running task, in a remote session, or while connected to a local app-server daemon. Source: https://learn.chatgpt.com/docs/import
- `/review` starts a dedicated reviewer against uncommitted changes, a commit, or a base branch without modifying the working tree. Source: https://learn.chatgpt.com/docs/code-review
- `/agent` inspects and switches between subagent threads. Source: https://learn.chatgpt.com/docs/agent-configuration/subagents
- `/hooks` reviews, trusts, or disables non-managed hooks. Source: https://learn.chatgpt.com/docs/hooks
- `/memories` controls whether the current chat can use or contribute to local memories when the feature is enabled. Source: https://learn.chatgpt.com/docs/customization/memories
- `/model` switches models or reasoning effort. Source: https://learn.chatgpt.com/docs/models
- `/status` shows remaining usage limits during an active session. Source: https://learn.chatgpt.com/docs/pricing

### Codex IDE extension

Primary source: https://learn.chatgpt.com/docs/codex/ide

- Ships for Visual Studio Code, Cursor, Windsurf, Visual Studio Code Insiders, Xcode, and JetBrains IDEs.
- In VS Code, Cursor, or Windsurf, the Codex icon or the Command Palette command Codex: Open Codex Sidebar opens the sidebar.
- In Xcode, the coding assistant starts a chat and can select Codex as the agent. In JetBrains IDEs, AI Chat can select Codex.
- The composer can attach an open file, a selection, or a recent chat.
- Reviews show a summary and changed lines beside the source; the person keeps or follows up on edits in the same view.
- Local work stays in the editor; longer tasks can connect to Codex web and return a reviewable result in the same chat.
- `/review` appears when the open project is a Git repository and can review against a base branch or uncommitted changes. Source: https://learn.chatgpt.com/docs/code-review
- The IDE extension does not support plugins. Source: https://learn.chatgpt.com/docs/plugins
- The IDE extension does not provide the Scheduled management interface. Source: https://learn.chatgpt.com/docs/automations
- The gear menu opens MCP servers and Codex Settings > Open config.toml. Source: https://learn.chatgpt.com/docs/config-file/config-basic

### Codex cloud

Primary source: https://learn.chatgpt.com/docs/cloud

- Runs coding tasks in isolated cloud environments so several tasks can continue in parallel.
- Sign-in uses a ChatGPT account. Codex cloud requires ChatGPT sign-in, not an API key. Source: https://learn.chatgpt.com/docs/auth
- Connects GitHub, or GitLab (beta), then creates an environment for the selected repository or project.
- A person watches task logs or lets the task run in the background, then reviews the summary and diff, asks for follow-up changes, or opens a pull request.
- Work can start from GitHub pull requests, GitLab merge requests and issues, Linear issues, or Slack channels and threads.
- Tasks can start and be reviewed from the web or from Codex CLI.
- The default model for Codex cloud chats cannot be changed. Source: https://learn.chatgpt.com/docs/models
- Email-and-password ChatGPT accounts must enable MFA before accessing Codex cloud. Source: https://learn.chatgpt.com/docs/auth

### ChatGPT desktop app

Primary source: https://learn.chatgpt.com/docs/environments/modes

- In the ChatGPT desktop app, the product selector includes Codex. A new Codex chat chooses Local (current project directory), Worktree, or Cloud.
- Local and Worktree chats run on the computer that holds the project.
- Codex chats focus on development projects and show developer details, including diff and review views. A pull requests pane is available when enabled. Source: https://learn.chatgpt.com/docs/use-chatgpt
- When available, Quick chat opens ChatGPT chats from web and mobile inside Codex. Source: https://learn.chatgpt.com/docs/use-chatgpt
- On all Codex plans, Share or `/share` creates a read-only snapshot of a local Codex thread on macOS. The snapshot does not grant access to the project or computer. Source: https://learn.chatgpt.com/docs/use-chatgpt
- Personal-account snapshot links are open to anyone with the link. Workspace snapshots are limited to authenticated workspace members, or to invited people and groups. A workspace administrator can turn off workspace share links. Source: https://learn.chatgpt.com/docs/use-chatgpt
- Snapshots can include user-visible messages, reasoning summaries, image attachments, generated images, and file diffs. They omit tool calls, shell commands, and tool input or output. Codex redacts known secret patterns before upload. Source: https://learn.chatgpt.com/docs/use-chatgpt
- Built-in Git controls stage, revert, commit, push, and create a pull request from the diff pane, including inline comments for Codex. Source: https://learn.chatgpt.com/docs/environments/local-environment
- Local environments (desktop Codex only) store setup scripts and named actions in the project's `.codex` folder and can be checked into Git. Setup scripts run when Codex creates a new worktree. Actions appear in the top bar and run in the integrated terminal. Source: https://learn.chatgpt.com/docs/environments/local-environment
- Settings > Import can import instructions, settings, skills, plugins, projects, and recent work from Claude Code, Claude Cowork, or Cursor, and can keep imported work in sync with automatic updates. Source: https://learn.chatgpt.com/docs/import
- ChatGPT Voice in the desktop app works in Chat, Work, and Codex on Plus, Pro, Business, Edu, and Enterprise, subject to rollout and workspace settings. Voice in existing Codex tasks is rolling out. Source: https://learn.chatgpt.com/docs/features/voice
- Voice on desktop uses the existing Codex usage budget at $0.05 per minute, or 1.25 credits per minute on credit-based Business, Edu, and Enterprise billing. It is not available via API key. Source: https://learn.chatgpt.com/docs/pricing
- The Apple Messages plugin, on the Apple Silicon macOS desktop app, can read and send iMessage, SMS, and RCS from Codex and ChatGPT Work after per-send approval. Source: https://learn.chatgpt.com/docs/plugins

### Codex Remote

Primary source: https://learn.chatgpt.com/docs/remote

- Codex Remote in the ChatGPT mobile app starts, guides, approves, and reviews Codex tasks that run on a connected Mac or Windows PC.
- Setup is Settings > Connections > Control this Mac or PC in the desktop app, then a QR scan from the phone on the same ChatGPT account and workspace.
- The phone can follow active tasks, send new instructions, approve requested commands, and inspect changed files, diffs, and test results.
- The computer must stay awake and online. Availability depends on rollout and workspace settings.
- Worktrees do not run on the phone; Remote controls worktrees on the connected computer. Source: https://learn.chatgpt.com/docs/environments/git-worktrees
- ChatGPT Voice can be used through Remote on iOS after pairing the phone with a desktop host. Source: https://learn.chatgpt.com/docs/features/voice

### Environments

Primary source: https://learn.chatgpt.com/docs/environments/modes

- Each Codex chat chooses Local, Worktree, or Cloud.
- Cloud environments configure dependencies, tools, environment variables, secrets, and setup steps in Codex settings. Source: https://learn.chatgpt.com/docs/environments/cloud-environment
- A cloud chat creates a container, checks out the selected branch or commit, runs the setup script, applies internet settings, then loops on terminal commands. If `AGENTS.md` is present, the agent uses it for project lint and test commands. Source: https://learn.chatgpt.com/docs/environments/cloud-environment
- The default cloud image is `universal`, documented in `openai/codex-universal`. Package versions for Python, Node.js, and other runtimes can be pinned. Common package managers can install automatically. Source: https://learn.chatgpt.com/docs/environments/cloud-environment
- Cloud secrets are encrypted and available only to setup scripts; they are removed before the agent phase. Environment variables last the full chat. Source: https://learn.chatgpt.com/docs/environments/cloud-environment
- Cloud containers cache for up to 12 hours. Business and Enterprise caches are shared across users who can access the environment. Source: https://learn.chatgpt.com/docs/environments/cloud-environment
- Agent internet access is off by default during the agent phase. Setup scripts still have internet. Per-environment options are off, or on with a domain allowlist and optional GET/HEAD/OPTIONS-only methods. Source: https://learn.chatgpt.com/docs/cloud/internet-access
- Cloud outbound traffic passes through an HTTP/HTTPS proxy. Source: https://learn.chatgpt.com/docs/environments/cloud-environment
- Worktrees use Git worktrees so several chats can run in the same project without sharing one working tree. Codex creates managed worktrees under `$CODEX_HOME/worktrees` in a detached HEAD. Source: https://learn.chatgpt.com/docs/environments/git-worktrees
- Handoff moves a chat between Local and Worktree and performs the Git operations needed to transfer the work. Source: https://learn.chatgpt.com/docs/environments/git-worktrees
- A `.worktreeinclude` file copies listed ignored paths (for example `.env`) into local managed worktrees. Ignored `AGENTS.override.md` is copied automatically. Source: https://learn.chatgpt.com/docs/environments/git-worktrees
- Permanent worktrees can be created from a project's menu and are not auto-deleted. Codex keeps the most recent 15 managed worktrees by default and snapshots a worktree before deleting it. Source: https://learn.chatgpt.com/docs/environments/git-worktrees

### Code review

Primary source: https://learn.chatgpt.com/docs/code-review

- `/review` in the desktop app, CLI, and IDE extension starts a dedicated reviewer that reports prioritized findings without changing the working tree.
- Desktop and IDE scopes include review against a base branch and review of uncommitted changes. The CLI also supports review of a selected commit and custom review instructions.
- The desktop review pane can show unstaged, staged, commit, branch, or last-turn diffs, including changes the person made, and can cover multiple Git repositories in one local project.
- Inline comments on a diff line become review guidance for a follow-up message.
- Settings can run `/review` in the current chat or in a detached review chat. CLI reviews can use a separate `review_model` in `config.toml`.
- With GitHub access and `gh` authenticated, the desktop app can load pull-request context and comments on the PR branch and apply fixes in the same chat.

### GitHub

Primary source: https://learn.chatgpt.com/docs/third-party/github

- After Codex cloud is set up, Code review can be turned on per repository in Codex settings.
- `@codex review` on a pull request posts a GitHub review focused on P0 and P1 issues.
- Automatic reviews post a review when someone opens a new PR for review, without an `@codex review` comment.
- `AGENTS.md` sections titled `## Code Review Rules` customize what Codex checks, with nested files applying to nearby code.
- `@codex security review` requests Security Review, a research-preview in-depth security pass that posts findings and a Security Report tab.
- `@codex fix the P1 issue` (or another non-review mention) starts a cloud chat on the pull request and can push a fix when Codex has permission.
- Any other `@codex` comment starts a cloud chat using the pull request as context.
- GitHub-triggered reviews count as Code Review usage. Local reviews outside GitHub count toward general usage. Source: https://learn.chatgpt.com/docs/pricing

### GitLab (Beta)

Primary source: https://learn.chatgpt.com/docs/third-party/gitlab

- GitLab support is in beta on all ChatGPT plans and runs in Codex cloud. Desktop GitHub-style controls such as Create pull request are not in this beta.
- GitLab.com uses a standard connection. Self-managed or Dedicated GitLab needs a workspace-admin template and a service-account token with the `api` scope.
- Project environments plus a project webhook enable coding tasks and, on GitLab.com, reviews. Self-managed group webhooks can enable reviews across a group without creating project environments.
- `@codex review` posts GitLab discussions. Manual reviews can include P0–P2 findings; automatic reviews focus on P0 and P1.
- Automatic reviews use repository policies (`Review my MRs`, `Review team MRs`, `Review all MRs`, or `Follow personal`) and triggers: On MR open, On every push, or Smart Trigger (experimental).
- `@codex` comments other than `review` start a cloud chat when a project environment exists. Group activity alone cannot run coding tasks.

### Slack

Primary source: https://learn.chatgpt.com/docs/third-party/slack

- Slack requires Plus, Pro, Business, Enterprise, or Edu, a connected GitHub account, and at least one cloud environment.
- After installing the Slack app from Codex settings, `@Codex` in a channel or thread creates a cloud chat and replies with a link and, depending on settings, an answer.
- Codex picks an environment from those the person can access, or the most recently used one, and runs against the default branch of the first repository in that environment's repo map.
- An Enterprise admin can clear Allow Codex Slack app to post answers on task completion so Codex posts only the chat link.

### Linear

Primary source: https://learn.chatgpt.com/docs/third-party/linear

- Codex in Linear is available on paid plans. Enterprise workspaces need Codex cloud chats and Codex for Linear enabled by an admin.
- After install, a Linear issue can be assigned to Codex, or `@Codex` can be mentioned in a comment. Codex posts progress and a summary with a chat link for opening a pull request.
- Linear triage rules can assign new issues to Codex automatically. Those chats run as the issue creator.
- Local Linear access uses the Linear MCP server (`codex mcp add linear --url https://mcp.linear.app/mcp`) from the desktop app, CLI, or IDE extension.

### Customization

Primary source: https://learn.chatgpt.com/docs/customization/overview

- `AGENTS.md` is durable project guidance loaded before work starts. Global files live in `~/.codex`; repo files nest from the project root. Closer files override earlier ones. Source: https://learn.chatgpt.com/docs/agent-configuration/agents-md
- Discovery order per directory is `AGENTS.override.md`, then `AGENTS.md`, then names in `project_doc_fallback_filenames`. Combined size defaults to 32 KiB (`project_doc_max_bytes`). Source: https://learn.chatgpt.com/docs/agent-configuration/agents-md
- Skills are `SKILL.md` folders with optional scripts and references. Global skills live in `~/.agents/skills`; repo skills live in `.agents/skills`. Codex loads metadata first, then the skill body when chosen. Source: https://learn.chatgpt.com/docs/customization/overview
- Plugins bundle skills, MCP servers, optional browser extensions, and hooks. They work in Codex in the ChatGPT desktop app and in Codex CLI. The IDE extension does not support plugins. Source: https://learn.chatgpt.com/docs/plugins
- ChatGPT and Codex share one public plugin directory with OpenAI, workspace, and personal tabs. Workspace admins can import and sync a GitHub marketplace. Source: https://learn.chatgpt.com/docs/plugins
- API-key sign-in can install supported OpenAI-curated plugins in the CLI and desktop Codex; some OAuth plugins are unavailable. Source: https://learn.chatgpt.com/docs/plugins
- Local Codex memories are experimental and off by default (`[features] memories = true`). After enablement, Codex writes memory files under `~/.codex/memories/` from eligible idle chats and can inject them into later sessions. Source: https://learn.chatgpt.com/docs/customization/memories
- Computer History on macOS can turn allowed app and website activity into memories and a timeline that Codex can reference. Business and Enterprise leave it off until a workspace owner grants access; each member still opts in. Source: https://learn.chatgpt.com/docs/customization/memories

### Subagents

Primary source: https://learn.chatgpt.com/docs/agent-configuration/subagents

- Current Codex releases enable subagent workflows by default. Activity appears in the ChatGPT desktop app, Codex CLI, and the IDE extension.
- Codex delegates when the person asks, or when `AGENTS.md` or a skill requests it. Each subagent does its own model and tool work and uses more tokens than a single-agent run.
- Built-in agents are `default` (general-purpose), `worker` (implementation and fixes), and `explorer` (read-heavy exploration).
- Custom agents are standalone TOML files in `~/.codex/agents/` or `.codex/agents/` with required `name`, `description`, and `developer_instructions`. They can override `model`, `model_reasoning_effort`, `sandbox_mode`, `mcp_servers`, and `skills.config`.
- `[agents]` in `config.toml` sets `enabled`, `max_concurrent_threads_per_session`, default subagent model and reasoning effort, and `interrupt_message`.
- Subagents inherit the parent turn's live sandbox and approval overrides, including `/permissions` and `--yolo`. A custom agent file can set a different `sandbox_mode`.
- In non-interactive runs, an action that needs a fresh approval fails and returns the error to the parent workflow.

### Model Context Protocol

Primary source: https://learn.chatgpt.com/docs/extend/mcp

- The ChatGPT desktop app, Codex CLI, and IDE extension share MCP configuration in `config.toml` (user `~/.codex/config.toml` or trusted project `.codex/config.toml`).
- Supported transports are STDIO (local process) and Streamable HTTP, with bearer tokens, OAuth (CIMD and DCR), and ChatGPT session auth for trusted first-party servers.
- `codex mcp add`, `codex mcp list`, and `codex mcp login` manage servers. `/mcp` lists connected servers in the TUI and desktop composer.
- Per-server options include startup and tool timeouts, `enabled` / `required`, tool allow and deny lists, and approval modes `auto`, `prompt`, `writes`, and `approve`.
- Installed plugins can bundle MCP servers. User config can still toggle those servers and set tool policy.
- Documented example servers include OpenAI Docs, Context7, Figma, Playwright, Chrome Developer Tools, Sentry, and GitHub.

### Hooks

Primary source: https://learn.chatgpt.com/docs/hooks

- Hooks run scripts or MCP tools at Codex lifecycle events, including `PreToolUse`, `PermissionRequest`, `PostToolUse`, `PreCompact`, `PostCompact`, `UserPromptSubmit`, `SubagentStart`, `SubagentStop`, `Stop`, `Interrupt`, `SessionStart`, and `SessionEnd`.
- Codex loads `hooks.json` and inline `[hooks]` from user, project (trusted only), plugin, system, MDM, and cloud-managed layers. Matching hooks all run; command hooks for the same event start concurrently.
- Non-managed hooks must be reviewed and trusted against their current hash before they run. Managed hooks from system, MDM, cloud, or `requirements.toml` are trusted by policy and cannot be disabled in the user hook browser.
- `--dangerously-bypass-hook-trust` runs enabled hooks for one invocation without persisted trust.

### Sandbox and approvals

Primary source: https://learn.chatgpt.com/docs/sandboxing

- Local commands in the desktop app, CLI, and IDE extension run inside a sandbox by default. The sandbox covers spawned commands, not only built-in file tools.
- Enforcement is Seatbelt on macOS, the native Windows sandbox in PowerShell, and bubblewrap on Linux and WSL2.
- Sandbox modes include `read-only`, `workspace-write` (default low-friction local mode), and `danger-full-access`.
- Approval policies are `on-request` (ask when leaving the sandbox) and `never`. `untrusted` is retired and can prevent startup if left in config. Source: https://learn.chatgpt.com/docs/agent-approvals-security
- `approvals_reviewer` is `user` (default) or `auto_review`, which sends eligible boundary approvals to a reviewer agent without changing the sandbox. Source: https://learn.chatgpt.com/docs/sandboxing
- Full access is `sandbox_mode = "danger-full-access"` plus `approval_policy = "never"`. Writable roots extend write access without removing the sandbox.
- Permission profiles are beta. Built-ins are `:read-only`, `:workspace`, and `:danger-full-access`. Custom `[permissions.<name>]` tables combine filesystem and network rules. They do not compose with older `sandbox_mode` settings unless managed `allowed_permission_profiles` forces profiles. Source: https://learn.chatgpt.com/docs/permissions
- Rules are experimental Starlark `.rules` files that `allow`, `prompt`, or `forbid` command prefixes outside the sandbox. `codex execpolicy check` tests a rule file. Admins can enforce `prefix_rule` entries from `requirements.toml`. Source: https://learn.chatgpt.com/docs/agent-configuration/rules
- GPT-6 Astra safety monitoring can pause a Codex or ChatGPT Work task asynchronously if it detects potentially unsafe model behavior. Source: https://learn.chatgpt.com/docs/agent-approvals-security
- Destructive MCP or app tool calls that advertise a destructive annotation require approval unless a read annotation takes priority. Source: https://learn.chatgpt.com/docs/agent-approvals-security

### Configuration

Primary source: https://learn.chatgpt.com/docs/config-file/config-basic

- User defaults live in `~/.codex/config.toml`. Trusted projects can add `.codex/config.toml` layers from the repo root to the working directory (closest wins).
- Untrusted projects skip project `.codex/` layers, including project config, hooks, and rules. User and system config still load.
- Precedence, highest first: CLI flags and `--config`, project config, `--profile` files, user config, cloud-managed defaults, system `/etc/codex/config.toml`, built-in defaults.
- Common keys set `model`, `approval_policy`, `sandbox_mode`, `default_permissions`, Windows sandbox elevation, `web_search` (`cached`, `indexed`, `live`, `disabled`), `model_reasoning_effort`, `personality`, TUI keymaps, `shell_environment_policy`, and `log_dir`.
- `[features]` toggles optional capabilities. Documented stable flags include `apps`, `goals`, `hooks`, `fast_mode`, `multi_agent`, `personality`, `remote_plugin`, `shell_snapshot`, `shell_tool`, and `unified_exec` (true except on Windows). `memories` is experimental and defaults to false.
- Managed `requirements.toml` can forbid values such as `approval_policy = "never"` or `sandbox_mode = "danger-full-access"`. Source: https://learn.chatgpt.com/docs/enterprise/managed-configuration
- Custom model providers can use OpenAI auth, an environment-variable API key, or no auth (for local models). Chat Completions API support is deprecated. Source: https://learn.chatgpt.com/docs/auth

### Authentication

Primary source: https://learn.chatgpt.com/docs/auth

- Local Codex (desktop app, CLI, IDE) supports Sign in with ChatGPT or an API key. Codex cloud requires ChatGPT sign-in.
- ChatGPT sign-in follows workspace RBAC, retention, and residency. API-key sign-in follows the API organization's retention and data-sharing settings and uses API pricing.
- CLI login is `codex login` (browser), `printenv OPENAI_API_KEY | codex login --with-api-key`, or `printenv CODEX_ACCESS_TOKEN | codex login --with-access-token`.
- Device code authentication is beta for headless or blocked-callback environments (`codex login --device-auth`) after the account or workspace enables it.
- Credentials cache in `~/.codex/auth.json` or the OS credential store. `cli_auth_credentials_store` can be `file`, `keyring`, `auto`, or `ephemeral`.
- Admins can set `forced_login_method` to `chatgpt` or `api` and `forced_chatgpt_workspace_id` to pin a workspace.
- `CODEX_CA_CERTIFICATE` (or `SSL_CERT_FILE`) supplies a custom CA bundle for corporate TLS.
- The CLI and IDE extension share cached login. Logging out of either requires a new sign-in.

### Models

Primary source: https://learn.chatgpt.com/docs/models

- Recommended ChatGPT-signed-in models are GPT-6 Astra, GPT-6 Sol, and GPT-6 Luna. GPT-5.6 Sol, Terra, and Luna remain available during rollout. GPT-6 Sol and Luna are available in Work and Codex, not in Chat.
- The desktop app, CLI (`--model` / `/model`), and IDE extension share `config.toml` `model`. Higher reasoning effort uses more tokens. Ultra uses subagents; GPT-6 Luna supports Max but not Ultra.
- Experimental context management for Plus and Pro ChatGPT sign-in lets Astra keep notes across context windows. It is off by default and unavailable with Business, Enterprise, or API-key sign-in.
- GPT-5.5 retires from ChatGPT, ChatGPT Work, and Codex on all plans on 14 October 2026. The OpenAI API is not affected. Plus through Enterprise replacements use `gpt-6-sol` when available; Free and Go use `gpt-6-luna` in the desktop app when available.
- `gpt-5.4` and `gpt-5.4-mini` retired from ChatGPT-signed-in Codex on 31 August 2026. `gpt-5.2` and `gpt-5.3-codex` are already deprecated for that sign-in path.
- Codex can point at any provider that supports Chat Completions or Responses APIs. Chat Completions support is deprecated.

### Scheduled tasks

Primary source: https://learn.chatgpt.com/docs/automations

- Recurring tasks run in the background. Create and manage them from ChatGPT web or the desktop app Scheduled view. Codex CLI and the IDE extension do not provide that interface.
- Desktop scheduled tasks can use a local project directory or a dedicated Git worktree. The computer must stay on and the app running for local files.
- Scheduled tasks created with Codex or ChatGPT Work in the desktop app can use plugins and skills. A prompt can invoke a skill with `$skill-name`.
- Event-triggered tasks (Gmail, Slack, GitHub) are available on eligible plans on web and mobile only. They are not available in the desktop app, CLI, or IDE extension.
- Scheduled tasks run unattended with default sandbox settings and use `approval_policy = "never"` when organization policy allows it.

### Codex SDK

Primary source: https://learn.chatgpt.com/docs/codex-sdk

- The TypeScript package `@openai/codex-sdk` starts, continues, and resumes local Codex threads from Node.js 18 or later (`thread.run`, `resumeThread`).
- The Python package `openai-codex` (Python 3.10+) drives the local app-server over JSON-RPC, with `Codex` and `AsyncCodex` and sandbox presets `read_only`, `workspace_write`, and `full_access`.
- Use the SDK for CI, internal tools, or embedding Codex. Use the app server to build a custom client. The removed `codex mcp-server` is replaced by the app server.

### App Server

Primary source: https://learn.chatgpt.com/docs/app-server

- `codex app-server` is the JSON-RPC interface used by rich clients such as the VS Code extension. It handles authentication, conversation history, approvals, and streamed agent events.
- Sources are open in `openai/codex/codex-rs/app-server`.
- Transports include stdio (default JSONL), experimental WebSocket (`--listen ws://`), Unix sockets, or `off`. WebSocket listeners expose `GET /readyz` and `GET /healthz`.
- Remote TUI mode runs app-server on one machine and connects with `codex --remote` over `ws://`, `wss://`, or `unix://`. Non-local connections should use TLS and a bearer token from an environment variable.
- `--code-mode-host` points app-server at a remote Code Mode host. The app-server command and WebSocket transport are experimental and are not supported for production workloads.

### GitHub Action

Primary source: https://learn.chatgpt.com/docs/github-action

- `openai/codex-action@v1` installs the Codex CLI, starts a Responses API proxy when an API key is provided, and runs `codex exec`.
- Inputs include `prompt` or `prompt-file`, `codex-args`, `model`, `effort`, `sandbox`, `output-file`, `codex-version`, and `codex-home`.
- `safety-strategy` defaults to `drop-sudo`. Windows requires `safety-strategy: unsafe`. `unprivileged-user` can run Codex as a named account. `allow-users` and `allow-bots` restrict who can trigger the workflow.
- The action emits `final-message`. `--output-schema` can be passed through `codex-args` for structured JSON.

### Non-interactive mode

Primary source: https://learn.chatgpt.com/docs/non-interactive-mode

- `codex exec "prompt"` runs without the TUI. Progress goes to stderr; the final agent message goes to stdout.
- Default sandbox is read-only. `--sandbox workspace-write` allows edits. `--sandbox danger-full-access` is for controlled environments. `--full-auto` is deprecated.
- `--json` emits JSONL events (`thread.started`, `turn.started`, `item.*`, `turn.completed`, and others). `--output-schema` constrains the final response to a JSON Schema.
- `--ephemeral` skips persisting session files. `--ignore-user-config` and `--ignore-rules` skip user config or execpolicy rules.
- `codex exec resume --last` or a session ID continues a previous run. Commands must run inside a Git repository unless `--skip-git-repo-check` is set.
- Automation auth uses `CODEX_API_KEY` for a single invocation, or ChatGPT-managed `auth.json` on trusted runners. Public repositories should not use the ChatGPT-auth CI path.

### Codex Security

Primary source: https://learn.chatgpt.com/docs/security

- Codex Security is an application-security agent that finds, confirms, and remediates vulnerabilities from Codex, the CLI, the TypeScript SDK, or connected GitHub repositories.
- The desktop Security workbench (Codex Security plugin) lists scans, findings, and repositories. Documented plugin flows include repository or folder scans, deep scans, change review, backlog triage, fix-and-verify, export, vulnerability reports, and hardening proposals.
- The public package `@openai/codex-security` provides the CLI (`npx @openai/codex-security`) and TypeScript SDK. Scans require Codex Security access; Trusted Access for Cyber is recommended.
- The CLI can discover GitHub repositories, resume bulk scans from a CSV inventory, upload SARIF, set a severity policy, and run in GitHub or GitLab CI.
- Codex Security cloud is a research preview that scans connected GitHub repositories commit by commit, validates high-signal issues in an isolated environment, and suggests fixes.

### Administration

Primary source: https://learn.chatgpt.com/docs/enterprise/roles-and-workspace-permissions

- Workspace seats, built-in roles (Owner, Admin, Member, Analytics Viewer), and custom roles control product access. Some workspaces offer separate ChatGPT and Codex seats.
- Local Codex access is Allow members to use Codex locally, or the combined Allow members to use Codex and Work Locally, depending on workspace layout. Enabling Work Local does not grant Codex.
- Managed configuration delivers `requirements.toml` constraints and `config.toml` defaults to the desktop app, CLI, and IDE via system files, a cloud config bundle, legacy `managed_config.toml`, or macOS MDM. It does not replace workspace RBAC. Source: https://learn.chatgpt.com/docs/enterprise/managed-configuration
- Requirements can constrain approval policy, reviewer, sandbox or permission profiles, web search mode, managed hooks, allowed MCP servers, plugin marketplaces, and feature flags. Source: https://learn.chatgpt.com/docs/enterprise/managed-configuration
- Codex access tokens (Business and Enterprise) authenticate trusted non-interactive local CLI and app-server runs as a ChatGPT workspace identity. They cannot trigger Workspace Agents. Source: https://learn.chatgpt.com/docs/enterprise/access-tokens
- Service accounts (pay-as-you-go plans) are non-human workspace identities with their own groups, roles, plugins, and tokens. They can be provisioned with SCIM (`userType: ServiceAccount`) or the Admin API. Source: https://learn.chatgpt.com/docs/enterprise/service-accounts
- Enterprise and Edu add SCIM, EKM, user analytics, domain verification, RBAC, Compliance API audit logs, and data retention and residency controls. Source: https://learn.chatgpt.com/docs/pricing
- Feature maturity labels are Under development, Experimental, Beta, Stable, and Deprecated. Source: https://learn.chatgpt.com/docs/feature-maturity

### Pricing

Primary source: https://learn.chatgpt.com/docs/pricing

- ChatGPT Work and Codex share usage, credits, and limits on ChatGPT plans. Local messages and cloud chats share the same allowance. Weekly limits may also apply.
- Documented ChatGPT plan names that include Codex are Free, Go, Plus, Pro, Business, Edu, and Enterprise. API-key login is a separate usage-based path.
- Plus includes Codex on the web, CLI, IDE extension, and iOS, plus cloud integrations such as automatic code review and Slack.
- Pro includes everything in Plus with 5x or 20x more Codex usage than Plus.
- API-key use covers the CLI, SDK, or IDE extension only. It excludes cloud features such as GitHub code review and Slack, and bills at API rates.
- Business adds standard or usage-based Codex seats, larger cloud VMs, a dedicated workspace, SAML SSO, MFA, and no training on business data by default.
- Enterprise and Edu add priority processing, SCIM, EKM, analytics, domain verification, RBAC, Compliance API logs, and retention and residency controls.
- Plus and Pro users can buy additional credits after hitting included limits. All users can run extra local chats with an API key.
- Eligible personal and Business users can send Codex invitations from the profile menu. Referrals are not available for ChatGPT Enterprise.

### Codex Micro

Primary source: https://learn.chatgpt.com/docs/features/codex-micro

- Codex Micro is a limited-run hardware keyboard from Codex and Work Louder that works with the ChatGPT desktop app over USB-C or Bluetooth.
- Six Agent Keys follow chats and show status (idle, thinking, complete, needs input, error). Command Keys, analog stick, and dial map to Fast mode, approvals, voice, Plan mode, composer navigation, skills, and other desktop actions.
- Settings live in Settings > Codex Micro. Availability is through OpenAI Supply Co.; the desktop app also supports Creator Micro 2.

### Open Source

Primary source: https://learn.chatgpt.com/docs/open-source

- Open-source components include the Codex CLI, Codex SDK, Codex app server, `openai/codex-universal`, skills, plugins, and Codex Security CLI and TypeScript SDK.
- The IDE extension and Codex cloud are not open source.
- Codex for OSS offers open-source maintainers API credits, six months of ChatGPT Pro with Codex, and selective Codex Security access.

## Sources

- https://developers.openai.com/codex/
- https://learn.chatgpt.com/docs
- https://learn.chatgpt.com/docs/use-chatgpt
- https://learn.chatgpt.com/docs/codex/cli
- https://learn.chatgpt.com/docs/codex/ide
- https://learn.chatgpt.com/docs/cloud
- https://learn.chatgpt.com/docs/cloud/internet-access
- https://learn.chatgpt.com/docs/environments/modes
- https://learn.chatgpt.com/docs/environments/cloud-environment
- https://learn.chatgpt.com/docs/environments/local-environment
- https://learn.chatgpt.com/docs/environments/git-worktrees
- https://learn.chatgpt.com/docs/remote
- https://learn.chatgpt.com/docs/code-review
- https://learn.chatgpt.com/docs/third-party/github
- https://learn.chatgpt.com/docs/third-party/gitlab
- https://learn.chatgpt.com/docs/third-party/slack
- https://learn.chatgpt.com/docs/third-party/linear
- https://learn.chatgpt.com/docs/customization/overview
- https://learn.chatgpt.com/docs/agent-configuration/agents-md
- https://learn.chatgpt.com/docs/agent-configuration/subagents
- https://learn.chatgpt.com/docs/agent-configuration/rules
- https://learn.chatgpt.com/docs/customization/memories
- https://learn.chatgpt.com/docs/plugins
- https://learn.chatgpt.com/docs/extend/mcp
- https://learn.chatgpt.com/docs/hooks
- https://learn.chatgpt.com/docs/sandboxing
- https://learn.chatgpt.com/docs/agent-approvals-security
- https://learn.chatgpt.com/docs/permissions
- https://learn.chatgpt.com/docs/config-file/config-basic
- https://learn.chatgpt.com/docs/auth
- https://learn.chatgpt.com/docs/models
- https://learn.chatgpt.com/docs/automations
- https://learn.chatgpt.com/docs/codex-sdk
- https://learn.chatgpt.com/docs/app-server
- https://learn.chatgpt.com/docs/github-action
- https://learn.chatgpt.com/docs/non-interactive-mode
- https://learn.chatgpt.com/docs/security
- https://learn.chatgpt.com/docs/enterprise/roles-and-workspace-permissions
- https://learn.chatgpt.com/docs/enterprise/managed-configuration
- https://learn.chatgpt.com/docs/enterprise/access-tokens
- https://learn.chatgpt.com/docs/enterprise/service-accounts
- https://learn.chatgpt.com/docs/pricing
- https://learn.chatgpt.com/docs/feature-maturity
- https://learn.chatgpt.com/docs/features/voice
- https://learn.chatgpt.com/docs/features/codex-micro
- https://learn.chatgpt.com/docs/import
- https://learn.chatgpt.com/docs/open-source
