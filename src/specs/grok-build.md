---
name: Grok Build
slug: grok-build
url: https://x.ai/
docs: https://docs.x.ai/build/overview
kind: product
reviewed: 2026-09-28
---

# Grok Build

## Product

Grok Build is xAI's coding agent. Official documentation is on the xAI docs host under Build. The product is the local `grok` CLI and its agent surfaces, not a separate hosted workspace. `grok-4.7` is also published on the xAI API for use in other agent loops, IDE integrations, or coding tools.

It runs on the user's machine. The interactive path is a mouse-interactive fullscreen TUI in a project directory (`cd your-project` then `grok`). The same binary runs headlessly in scripts, bots, and CI (`grok -p`), or as an Agent Client Protocol (ACP) agent over stdin/stdout (`grok agent stdio`). Installers documented by xAI are `curl -fsSL https://x.ai/cli/install.sh | bash`, Windows PowerShell `irm https://x.ai/cli/install.ps1 | iex`, and `npm install -g @xai-official/grok`.

On first launch the TUI opens a browser for authentication. Non-browser environments use `XAI_API_KEY`. Enterprise pages add device-code login, corporate OIDC, an external `auth_provider_command`, and managed policy files. Settings persist under `~/.grok/config.toml` (on Windows, `%USERPROFILE%\.grok\config.toml`). `$GROK_HOME` relocates that home. `grok inspect` reports the config sources, instructions, skills, plugins, hooks, and MCP servers discovered for the current directory.

The Grok assistant (`grok`) and Grok Bot (`grok-bot`) are out of scope. Docs link Grok Bot as AI teammates on a cloud computer. This file covers Grok Build only.

The Build docs do not publish a public price list. `/usage` in the TUI views credit usage or manages billing.

## Features

### Install and interactive TUI

Primary source: https://docs.x.ai/build/overview

- Grok Build is used through an interactive TUI, headlessly in scripts or bots, or through ACP in other apps.
- The TUI is a mouse-interactive fullscreen session for coding with agents.
- Install on Unix-like systems with `curl -fsSL https://x.ai/cli/install.sh | bash`.
- Install on Windows with `irm https://x.ai/cli/install.ps1 | iex`.
- Start an interactive session with `cd your-project` then `grok`.
- First launch opens a browser for authentication. In non-browser environments, set `XAI_API_KEY` and run `grok`.
- Prompts can attach files with `@`, for example `@src/main.rs`.
- Custom models are added under `[model.*]` in `~/.grok/config.toml`. After edits, `grok inspect` shows discovered config, and `grok -p "Hello" -m my-model` or `/model <name>` selects the model.
- `grok-4.7` is available on `https://api.x.ai/v1` for a separate agent loop, IDE integration, or coding tool.

### Headless & Scripting

Primary source: https://docs.x.ai/build/cli/headless-scripting

- `grok -p "Your prompt here"` (`--single`) runs one prompt without the TUI.
- `-m` / `--model` selects a model. `--cwd` sets the working directory.
- `-s` / `--session-id` creates or resumes a named headless session. `-r` / `--resume` resumes an existing session. `-c` / `--continue` continues the most recent session in the current directory.
- `--output-format` is `plain`, `json`, or `streaming-json`. `json` emits one object at the end. `streaming-json` emits newline-delimited events.
- `--always-approve` auto-approves tool executions. `--no-alt-screen` keeps the process inline without fullscreen TUI takeover.
- Headless sessions created with `--session-id`, `--resume`, or `--continue` are stored in `~/.grok/sessions`.
- `--no-auto-update` skips background update checks in headless or ACP runs. `auto_update = false` under `[cli]` in `~/.grok/config.toml` disables them persistently.

### Agent Client Protocol

Primary source: https://docs.x.ai/build/cli/headless-scripting

- `grok agent stdio` runs Grok as an ACP agent over JSON-RPC on stdin/stdout.
- Authentication is a local `grok login` session or `XAI_API_KEY`. The initialize handshake advertises `authMethods`; clients pick `xai.api_key` or `cached_token`.
- Clients call `session/new` with a cwd and MCP server list, then `session/prompt`. Assistant text arrives as `session/update` chunks (`agent_message_chunk`). `session/prompt` returns completion metadata such as `stopReason`.

### CLI

Primary source: https://docs.x.ai/build/cli/reference

- `grok` with no arguments starts the interactive TUI. `grok --help` lists the full flag set.
- `grok login` signs in. `--device-auth` uses device-code authentication for headless or remote environments. `grok logout` signs out and clears cached credentials.
- `grok inspect [--json]` shows configuration discovered for the directory: rules, skills, plugins, hooks, and MCP servers.
- `grok models` lists available models.
- `grok mcp <list|add|remove|doctor>` manages MCP servers. `grok plugin <list|install|uninstall|update|enable|disable|details|validate>` manages plugins. `grok plugin marketplace <list|add|remove|update>` manages marketplace sources.
- `grok sessions <list|search|delete>` lists, searches, or deletes sessions. `grok export [output]` exports a session transcript as Markdown. `grok import [targets...]` imports sessions from Claude Code.
- `grok memory clear [--workspace|--global|--all]` clears cross-session memory files.
- `grok worktree <list|show|rm|gc>` manages git worktrees created for sessions.
- `grok dashboard` opens the Agent Dashboard.
- `grok wrap <command...>` runs a command in a local PTY that forwards OSC 52 clipboard writes.
- `grok update` checks for updates or installs a version (`--check`, `--version <ver>`, `--alpha`, `--stable`). `grok version` prints version information. `grok completions <shell>` generates shell completion scripts. `grok setup` fetches and installs managed configuration.
- Common flags include `--cwd`, `-r` / `--resume`, `-c` / `--continue`, `-s` / `--session-id`, `--fork-session`, `-w` / `--worktree`, `--ref`, `-m` / `--model`, `--effort`, `--always-approve` (alias `--yolo`), `--allow` / `--deny`, `--sandbox`, `--rules`, `--system-prompt-override`, `--tools` / `--disallowed-tools`, `--max-turns`, `--no-plan`, `--no-subagents`, `--no-memory`, `--disable-web-search`, `--experimental-memory`, and `--oauth`.
- Claude Code flag names are accepted as aliases where they overlap: `--allowedTools`, `--disallowedTools`, `--append-system-prompt`, `--system-prompt`, and `--dangerously-skip-permissions`.

### Modes and Commands

Primary source: https://docs.x.ai/build/modes-and-commands

- The TUI has pager-local slash commands plus a smaller set from `xai-grok-shell`. User-invocable skills also appear as slash commands.
- `Shift+Tab` cycles session modes. Plan, Auto, and Always-approve are documented as the TUI modes.
- `/plan [description]` enters plan mode. `/view-plan` reopens the current plan.
- `/auto` toggles Auto mode when that feature is enabled. `/always-approve` toggles always-approve. `grok --always-approve` starts in always-approve.
- Session commands include `/quit` (`/exit`), `/help`, `/home`, `/new` (`/clear`), `/resume`, `/sessions`, `/fork`, `/rename` (`/title`), `/share`, `/session-info`, `/context`, `/compact [context]`, `/rewind`, `/export`, `/copy [N]`, `/find`, and `/transcript`.
- `/model <id>` (`/m`) switches the active model. `/effort` sets reasoning effort for the current model.
- `/btw <question>` asks a side question without interrupting the main turn.
- `/loop [interval] <prompt>` runs a prompt on a recurring interval.
- `/imagine <prompt>` generates an image from text. `/imagine-video <prompt>` generates a video from text. Both appear only when the feature is available.
- `/tasks` lists background tasks, subagents, and scheduled tasks. `/queue` lists prompts queued behind the running turn. `/dashboard` opens the Agent Dashboard.
- `/create-workflow [description]` authors and saves a workflow. `/workflow [args]` launches a saved workflow or `pause` / `resume` / `stop` / `save` a run. `/workflows` opens the live workflow run dashboard. `/deep-research <query>` starts a built-in research workflow.
- Workflows orchestrate a bounded set of subagents in the background. They are on by default. Saved files are `.grok/workflows/<name>.rhai` in the project or `~/.grok/workflows/<name>.rhai` for every project. Disable with `[workflows] enabled = false` or `GROK_WORKFLOWS=0`.
- `/settings` (`/config`) opens the settings modal. `/theme [name]` (`/t`) switches the color theme. `/compact-mode` toggles a denser layout. `/multiline` (`/ml`) toggles multiline input. `/vim-mode` toggles vim-style scrollback keybindings. `/timestamps` toggles message timestamps. `/terminal-setup` checks terminal and clipboard setup.
- `/config-agents` (`/agents`) manages agent definitions. `/personas` manages personas. `/remember <note>` saves a memory note. `/import-claude` opens the Claude settings import modal.
- `/feedback [text]` sends feedback about the current session. `/release-notes` (`/changelog`) shows release notes for the current version. `/usage` views credit usage or manages billing. `/privacy` shows or toggles privacy and data-retention status. `/login` and `/logout` sign in or out.
- `/hooks`, `/plugins`, `/marketplace`, `/skills`, and `/mcps` open the same extensions modal on different tabs.
- When cross-session memory is enabled, `/flush` writes conversation memory to disk, `/memory` (`/mem`) browses and manages memories, and `/dream` runs memory consolidation.
- A colliding skill slash command uses a qualified form such as `/local:commit`.

### Keyboard shortcuts

Primary source: https://docs.x.ai/build/keyboard-shortcuts

- `Ctrl+.` (`Ctrl+X` on Windows and terminals without the Kitty keyboard protocol) opens the shortcut list. Inapplicable entries are dimmed.
- `Enter` sends the prompt. `Tab` moves focus between prompt and scrollback. `Esc` or `Ctrl+C` cancels the running turn. `Esc Esc` clears the prompt or opens rewind when the prompt is empty.
- `Ctrl+P` or `?` opens the command palette. `F2` or `Ctrl+,` opens settings. `Ctrl+Q` / `Ctrl+D` quits (press twice).
- `Ctrl+Enter` or `Ctrl+I` interjects while a turn is running. `Shift+Enter` inserts a newline, or sends in multiline mode. `Ctrl+M` toggles multiline input when the prompt is focused, and opens the model picker when it is not. `Ctrl+R` searches prompt history. `!` on an empty prompt enters shell mode.
- Scrollback supports expand/collapse, thinking-block toggle (`Ctrl+E`), raw markdown (`r`), copy (`y` / `Shift+Y`), a fullscreen viewer, search in vim mode, and `x` to kill a selected background task.
- `Ctrl+T` toggles the todo pane. `Ctrl+B` backgrounds the running command. `Ctrl+;` or `Ctrl+'` toggles the prompt queue. `Ctrl+S` opens sessions. `Ctrl+L` opens extensions. `Ctrl+G` toggles the tasks pane. `Ctrl+O` toggles always-approve. `Ctrl+N` starts a new session (press twice). `Ctrl+\` opens the Agent Dashboard.
- VS Code-family terminals (VS Code, Cursor, Windsurf, Zed) use `Ctrl+D` to quit, `Ctrl+L` to interject, `Shift+D` for half-page scroll, `/plugins` instead of `Ctrl+L` for extensions, and `Alt+Enter` for newlines.
- Apple Terminal uses `Ctrl+O` to interject. WezTerm needs `enable_kitty_keyboard = true` for `Ctrl+Enter` and `Shift+Enter`.

### Plan Mode

Primary source: https://docs.x.ai/build/features/plan-mode

- In plan mode the agent explores the codebase and drafts a plan for approval before it edits files.
- Enter with `/plan`, `/plan <description>` (enters and starts a turn), or `Shift+Tab` from Normal.
- The agent can enter plan mode on its own when a task looks ambiguous. That is not a permission prompt. Leave with `Shift+Tab` when idle, or `q` on the approval screen.
- When planning finishes, the TUI opens a plan preview. Auto and always-approve do not skip this review. `/view-plan` (`/show-plan`, `/plan-view`) reopens a saved preview, including an empty plan.
- On the preview, `a` approves and starts building, `s` requests changes, `c` comments on a line or range, `q` quits plan mode, and `Tab` moves between the preview and the prompt.
- Until approval, only the session plan file may be edited. Other edit tools are rejected, including under auto or always-approve. Reads, bash, and MCP still follow permission mode. Bash can still write via redirection.
- Subagents are not edit-gated by the parent's plan mode. They inherit the parent's permission mode.
- Status shows `plan` while planning and `plan approval` on the review screen.

### Permissions

Primary source: https://docs.x.ai/build/features/permissions

- Permissions decide which tool calls may run. The sandbox is separate and limits what an approved call can do on the filesystem and network.
- Ask (default) prompts for anything not already allowed.
- Auto uses a classifier to auto-approve safe tools; dangerous ones may still prompt. Deny rules and hooks still apply. Toggle with `/auto` or `Shift+Tab` when the feature is on.
- Always-approve auto-approves tool calls. Deny rules and PreToolUse hooks still apply. Toggle with `/always-approve`, `Ctrl+O`, `Shift+Tab`, or `grok --always-approve`.
- `Shift+Tab` cycles Normal → Plan → Auto (when available) → Always-approve. `/auto` only appears when the auto permission-mode feature is enabled. Auto and always-approve switch rather than stack.
- Default permission mode is set only in user config (`~/.grok/config.toml` or managed/requirements), not in project `.grok/config.toml`: `[ui] permission_mode = "auto"` or `"ask"` or `"always-approve"`. Legacy keys `approval_mode` and `yolo = true` still work; `permission_mode` wins when more than one is set.
- Allow and deny rules live under `[permission] rules` or `--allow` / `--deny`. Supported filters include `Bash`, `Edit`, `Read`, `Grep`, `MCPTool`, `WebFetch`, and `WebSearch`. `deny` always wins over `allow`.
- A remembered “always allow” grant still prompts for dangerous patterns such as `rm` and `git push`. An explicit config or CLI allow rule auto-approves them. Under always-approve they run unless a deny is set.
- Plan mode is independent of permission mode: edit tools stay limited while planning, and the plan review UI is not skipped under auto or always-approve.

### Sandbox

Primary source: https://docs.x.ai/build/features/sandbox

- The sandbox limits what the agent process and its children can read, write, and reach on the network. It uses Landlock on Linux and Seatbelt on macOS. It is off by default.
- Built-in profiles are `off` (unrestricted), `workspace` (write to CWD, `~/.grok/`, and temp; network allowed), `devbox` (write to top-level dirs except `/data`; network allowed), `read-only` (write to `~/.grok/` and temp only; child network blocked), and `strict` (read CWD and system paths; write CWD, `~/.grok/`, temp; child network blocked).
- Child-network restrictions are enforced on Linux only and are a no-op on macOS for `read-only` and `strict`.
- Built-in profiles do not permanently protect paths such as `~/.ssh`; a custom `deny` list is required. `~/.grok/` stays writable under sandboxed profiles. Model API and web tools are not blocked by child-network settings.
- Enable a profile with `grok --sandbox workspace`, `[sandbox] profile` in `~/.grok/config.toml`, `GROK_SANDBOX=workspace`, or a managed `requirements.toml` pin.
- Custom profiles live in `~/.grok/sandbox.toml` or project `.grok/sandbox.toml` and can `extends` a built-in, set `restrict_network`, and add `deny` globs. Built-in names cannot be redefined for selection.

### Sessions

Primary source: https://docs.x.ai/build/features/sessions

- Every conversation is saved to disk automatically — prompts, responses, tool calls, and file snapshots — under `~/.grok/sessions/`, keyed by working directory.
- Sessions work the same in the TUI, headless mode, and over ACP.
- `/resume` opens a picker of recent sessions for the current workspace. The welcome screen lists them too. `grok --resume <session-id>`, `grok --resume`, and `grok -c` resume from the CLI.
- Headless JSON output includes `sessionId` for multi-step automations with `-r`.
- `-s` / `--session-id` names a new session with a supplied UUID and does not resume existing ones. `--fork-session` branches a resumed session instead of continuing it.
- `/fork [directive]` branches the current session into a peer that starts from a copy of the conversation. `--worktree` or `--no-worktree` chooses whether the fork runs in an isolated repository copy.
- `/rewind` (or `Esc Esc` while idle) lists a rewind point per prompt. Selecting one restores files to that point and truncates the conversation. Reverted changes are lost unless committed to git.
- `/compact [context]` compresses history to reclaim context, with optional preserve instructions. Grok also auto-compacts as the window fills. `/context` and `/session-info` show usage.
- The agent keeps a structured todo list with statuses pending, in progress, completed, and cancelled. `Ctrl+T` opens the todo pane. Todos persist when the same session is resumed. They are separate from background tasks.
- `/sessions` switches, renames, or closes active sessions. `/rename` retitles the current session. `grok sessions list`, `grok sessions search <query>`, and `grok sessions delete <id>` manage stored sessions. `grok export [file]` writes a Markdown transcript (`--clipboard` to copy).

### Skills, Plugins & Marketplaces

Primary source: https://docs.x.ai/build/features/skills-plugins-marketplaces

- Skills are reusable folders of markdown instructions, script files, and resources. Grok discovers them from `./.grok/skills/` (walked up to the repo root), `~/.grok/skills/`, enabled plugins' `skills/` directories, and extra `[skills] paths`.
- User-invocable skills appear as slash commands. `SKILL.md` uses YAML frontmatter with `name`, `description`, `when-to-use`, `paths`, `allowed-tools`, `argument-hint`, `user-invocable`, `disable-model-invocation`, and `metadata`. `allowed-tools` does not grant or restrict tools. Grok accepts `model`, `effort`, `license`, and `compatibility` and does not apply them.
- Plugins extend Grok with additional skills, agents, hooks, MCP servers, and LSP servers. Load paths are `./.grok/plugins/`, `~/.grok/plugins/`, marketplace installs under `~/.grok/plugins/marketplaces/`, extra `[plugins] paths`, and `--plugin-dir`.
- The TUI extensions modal manages plugins, hooks, skills, and MCP servers (`/plugins`, `/hooks`, `/skills`, `/mcps`).
- Hooks run scripts on tool and session lifecycle events. Discovery includes `~/.grok/hooks/` (extra roots via `~/.grok/hooks-paths`), project `.grok/hooks/` (requires `/hooks-trust`), and enabled plugins.
- The Marketplace tab browses and installs plugins from `[[marketplace.sources]]` in `~/.grok/config.toml` and `~/.grok/plugins/known_marketplaces.json`.
- Grok reads Claude Code marketplaces, plugins, skills, MCPs, agents, hooks, and instruction files (`CLAUDE.md`, `Claude.md`, `CLAUDE.local.md`, `.claude/rules/`) alongside `.grok/` with no extra setup.
- Grok reads the `AGENTS.md` family walked from cwd to the repo root, and discovers user-level skills and commands from `~/.agents/skills/` and `~/.agents/commands/`.

### MCP Servers

Primary source: https://docs.x.ai/build/features/mcp-servers

- MCP servers expose external tools alongside built-ins, namespaced as `<server>__<tool>`.
- `grok mcp add` registers a local stdio server or a remote HTTP server. `--transport http` is used for remote URLs. `--header` is repeatable. OAuth on remote servers is handled automatically.
- `grok mcp list`, `grok mcp remove <name>`, and `grok mcp doctor [name]` inspect, delete, and diagnose servers. `list` and `doctor` accept `--json`.
- Servers can be declared in `~/.grok/config.toml` under `[mcp_servers.<name>]` with `command`/`args`/`env` for stdio or `url`/`headers` for HTTP. `${VAR}` and `${VAR:-default}` expand in `url`, `command`, `args`, `env`, and `headers`. `{{session_id}}` is allowed in headers.
- OAuth tokens are stored under `~/.grok/mcp_credentials.json`.
- `--scope project` writes `.grok/config.toml` in the current directory. On load, Grok walks from cwd to the git root; a project server with the same name as a user server replaces it entirely.
- In the TUI MCP tab, `Space` toggles a server, `r` refreshes after config edits, `i` authenticates OAuth servers, and `a` / `x` add or remove.
- Grok also loads MCP config from `~/.claude.json`, `.cursor/mcp.json`, and project `.mcp.json`, merged below `config.toml`. Disable a vendor with `[compat.claude] mcps = false` or `[compat.cursor] mcps = false`.
- Failed stdio stderr is captured at `~/.grok/logs/mcp/<name>.stderr.log`. Cold-start `npx` servers may need a higher `startup_timeout_sec` (default 30). Default `tool_timeout_sec` is 6000.

### Hooks

Primary source: https://docs.x.ai/build/features/hooks

- A hook is a shell command or HTTP endpoint called on a lifecycle event: block a command before it runs, log tool use, run a formatter after edits, or notify when a turn ends.
- Hooks are JSON files in `~/.grok/hooks/*.json` and project `.grok/hooks/*.json`. Claude Code `.claude/settings.json` and Cursor `.cursor/hooks.json` are also read, including Cursor camelCase event names.
- Each entry has an optional `matcher` regex on the tool name (Claude names such as `Bash`, `Read`, and `Edit` are mapped), `type` `"command"` or `"http"` (with `url`), and `timeout` in seconds (default 5).
- Project hooks require trust: `/hooks-trust` or `--trust` on first open. The decision is stored in `~/.grok/trusted_folders.toml` and also covers project MCP and LSP servers.
- Events are `SessionStart`, `SessionEnd`, `UserPromptSubmit`, `PreToolUse` (the only blocking event), `PostToolUse`, `PostToolUseFailure`, `PermissionDenied`, `Stop`, `StopFailure`, `Notification`, `SubagentStart`, `SubagentStop`, `PreCompact`, and `PostCompact`.
- The event is JSON on stdin (`hookEventName`, `sessionId`, `cwd`, `workspaceRoot`, and for tool events `toolName` and `toolInput`). Environment includes `GROK_HOOK_EVENT`, `GROK_HOOK_NAME`, `GROK_SESSION_ID`, and `GROK_WORKSPACE_ROOT`. Plugin hooks also receive `GROK_PLUGIN_ROOT` and `GROK_PLUGIN_DATA`.
- A `PreToolUse` hook denies with `{"decision":"deny","reason":"..."}` on stdout or exit code 2. Exit 0 allows. Timeouts, crashes, and malformed output are fail-open: the failure is recorded and the tool call proceeds.

### AGENTS.md

Primary source: https://docs.x.ai/build/features/project-rules

- Project rules are Markdown files loaded into context for every session in a directory tree. An `AGENTS.md` at the repo root can hold conventions, build and test commands, and architecture notes.
- Load order is global rules in `~/.grok/`, then every directory from the repo root down to the working directory (or only the working directory outside a git repo). Deeper files win on conflicts.
- In each directory Grok reads `AGENTS.md`, `Agents.md`, `AGENT.md`, `CLAUDE.md`, `Claude.md`, `CLAUDE.local.md`, every `*.md` in `.grok/rules/`, and for compatibility `.claude/rules/` and `.cursor/rules/`. Files ignored by `.gitignore` are skipped.
- A nested `AGENTS.md` scopes to its subtree. Files are loaded in full with no size cap.
- `--rules` appends text to the system prompt for one run. `--system-prompt-override` replaces the system prompt entirely.
- `grok inspect` lists each rules file found, with path and approximate token count.

### Subagents

Primary source: https://docs.x.ai/build/features/subagents

- Subagents are independent child sessions with their own context. They return a summary to the parent when finished. They are enabled by default when the setting is unset.
- Built-in types are `general-purpose` (full-capability child), `explore` (read, list, and search only; no shell, no edits), and `plan` (drafts an implementation plan; no shell, no edits).
- Add or override types under `.grok/agents/` or `~/.grok/agents/`. Manage agents and personas with `/config-agents` (`/agents`) or `/personas`.
- Personas are behavioral overlays (tone, focus, contracts) under `[subagents.personas]` or `.grok/personas/*.toml` / `~/.grok/personas/*.toml`.
- Settings reference keys include `[subagents] enabled`, `[subagents.toggle]` per type, and `[subagents.models]` for per-subagent model routing. `GROK_SUBAGENTS` and `GROK_AGENT` override from the environment. Source: https://docs.x.ai/build/settings/reference

### Worktrees

Primary source: https://docs.x.ai/build/features/worktrees

- A worktree session runs in an isolated git checkout so parallel agents do not overwrite each other's files. Worktrees require a git repository, live under `~/.grok/worktrees/<repo>/<id>`, and start from current HEAD including uncommitted changes.
- Subagents can request worktree isolation when the parent delegates parallel work.
- Start with `grok -w`, `grok --worktree=<name> "<prompt>"`, `grok -w --ref <ref> "<prompt>"`, or `grok -w -r <session-id>`.
- In the TUI, `/fork --worktree` forks into a worktree. `Ctrl+W` on the welcome screen opens the New Worktree dialog. `Ctrl+W` in the Agent Dashboard dispatches new agents into worktrees.
- A worktree is a real git checkout, detached at its base commit. Changes are landed with ordinary git.
- Ending or deleting a session leaves the worktree in place. `gc` runs only when invoked.
- `grok worktree list`, `grok worktree show <id>`, `grok worktree rm <ids...>` (`--dry-run` to preview), and `grok worktree gc` (`--max-age 7d` expires idle unused worktrees) manage tracked worktrees.

### Background Tasks

Primary source: https://docs.x.ai/build/features/background-tasks

- Grok can run commands, subagents, and monitors in the background while the conversation continues.
- `Ctrl+G` opens the tasks pane. `/tasks` prints a snapshot in the scrollback. `Ctrl+B` demotes a running foreground command to the background.
- Agent todos (`Ctrl+T` on the agent screen) track planned multi-step work, not running processes.
- The agent can start dev servers, builds, and other long-running commands as background tasks and collect their output. In the scrollback, select a background task and press `x` to kill it.
- `/loop <interval> <prompt>` runs a prompt on a recurring interval (`Ns` with a 60-second minimum, `Nm`, `Nh`, `Nd`). The prompt fires immediately, then repeats as a new agent turn. Loops expire after 7 days. At most 50 scheduled tasks can be active. Cancel from the tasks pane or by asking the agent.
- A monitor attaches to a script; each printed line becomes a conversation notification (logs, CI, ports).
- Prompts submitted during a turn are queued. `Ctrl+;` toggles the queue panel. `/queue` lists it.

### Agent Dashboard

Primary source: https://docs.x.ai/build/features/dashboard

- The dashboard is a fullscreen overview of every session. Open it with `Ctrl+\`, `/dashboard`, or `grok dashboard`.
- Rows are grouped live by Needs input, Working, Idle, Inactive, Completed, and Failed. `Ctrl+G` groups by directory instead.
- Selecting a row opens a peek panel. Typing replies immediately to an idle agent or queues a message for a busy one. Permission prompts and questions can be answered inline with number keys.
- `Enter` attaches to the session. `Ctrl+\` returns to the dashboard. `Ctrl+[` / `Ctrl+]` cycle sessions.
- The bottom input bar dispatches prompts to new sessions. `Ctrl+L` changes the working directory for new agents. `Ctrl+W` toggles whether they start in a git worktree.
- Search is `Ctrl+/` (`a:<name>` by agent, `s:<state>` by state, or plain text). `Ctrl+T` pins or unpins. `Ctrl+R` renames. `Ctrl+X` twice stops or closes. `Shift+↑` / `Shift+↓` reorder pinned agents.
- Grouping and pins persist under `[dashboard]` in `~/.grok/config.toml`. `enabled = false` or `GROK_AGENT_DASHBOARD=0` disables the feature.

### Status Line

Primary source: https://docs.x.ai/build/features/status-line

- The status line is an optional row for live session values (model, context-window usage, cost, or a user script). It is off by default.
- In fullscreen it sits above the shortcuts bar. In minimal mode it sits under the prompt info row. It is hidden on the welcome screen and while a fullscreen subagent view is open.
- Configure `[ui.status_line]` in `~/.grok/config.toml` (user or administrator managed only; a cloned repository cannot set it). Restart Grok after edits. `type` is `builtin`, `command`, or `disabled` (`off`, `none`, and `hidden` mean the same).
- Built-in items are `cwd`, `model`, `context`, `cost` (hidden below $0.005; a resumed session counts from the resume), `turn-timer`, and `session-name`. Default items are `cwd`, `model`, and `context`.
- A `command` status line runs a script that reads JSON on stdin and prints one line. `~/` expands to the home directory. The docs mark command status lines as untested on Windows. `refresh_interval` (seconds) re-runs an idle command row on a timer.
- `grok inspect` reports problems in the `[ui.status_line]` section.

### Theming

Primary source: https://docs.x.ai/build/features/theming

- `/theme` (`/t`) opens a theme picker with a live preview. `/theme <name>` switches directly. `[ui] theme` in `~/.grok/config.toml` persists the choice.
- Built-in themes are GrokNight (`groknight`, `dark`; default), GrokDay (`grokday`, `light`, `day`), TokyoNight (`tokyonight`, `tokyo`; truecolor), RosePineMoon (`rosepine`, `rose-pine-moon`; truecolor), and OscuraMidnight (`oscura`, `oscura-midnight`; truecolor).
- Terminals without truecolor quantize themes and hide truecolor-only entries.
- `theme = "auto"` (`"system"`) follows the OS light/dark setting without a restart. Dark maps to GrokNight and light to GrokDay unless `auto_dark_theme` / `auto_light_theme` override them.
- `/compact-mode` reduces padding and persists. Finer appearance controls live in `~/.grok/pager.toml`.

### Terminal Support

Primary source: https://docs.x.ai/build/cli/terminal-support

- The TUI uses terminal escape sequences for color, clipboard, mouse, and fullscreen. `/terminal-setup` (`/terminal-check`, `/terminal-info`) reports detection, clipboard routes, and fixes.
- `COLORTERM=truecolor` is the documented color fix. tmux needs 24-bit RGB, `set-clipboard on`, and `allow-passthrough on`.
- Clipboard writes go to the native OS clipboard, the tmux paste buffer, and OSC 52 for SSH, containers, and Linux.
- `grok wrap ssh user@host` (also `docker exec` and `kubectl exec`) runs the remote command in a local PTY that intercepts OSC 52. The docs label `grok wrap` experimental.
- Grok runs inline under Zellij and tmux control mode (`tmux -CC`). Force fullscreen with `alt_screen = "always"` under `[terminal]` in `~/.grok/pager.toml`, or disable it with `--no-alt-screen`.

### Settings

Primary source: https://docs.x.ai/build/settings

- Many options are available in the TUI under `/settings`. Settings persist in `~/.grok/config.toml` or `$GROK_HOME/config.toml`.
- Scopes are environment (`GROK_*` and related), user (`~/.grok/config.toml`), project (`.grok/config.toml`: MCP, plugins, and permission rules only), managed (`~/.grok/managed_config.toml`, `/etc/grok/managed_config.toml`), and requirements (`~/.grok/requirements.toml`, `/etc/grok/requirements.toml`).
- Example user config sets `[models] default = "grok-build"`, a `web_search` model, per-model `base_url` / `env_key` / `api_backend`, MCP servers, and `[ui]` keys such as `compact_mode`, `theme`, and `show_thinking_blocks`.
- `grok inspect` confirms which configs were picked up.

### Settings reference

Primary source: https://docs.x.ai/build/settings/reference

- `GROK_HOME` defaults to `~/.grok` for config, auth, sessions, skills, plugins, and logs. `XAI_API_KEY` is the API-key path when not using browser or session login.
- Model env vars include `GROK_DEFAULT_MODEL`, `GROK_WEB_SEARCH_MODEL`, `GROK_MODELS_BASE_URL`, `GROK_MODELS_LIST_URL`, and `GROK_XAI_API_BASE_URL` (default `https://api.x.ai/v1`). `GROK_DISABLE_AUTOUPDATER` suppresses the auto-updater for the process.
- Tool env vars include `GROK_SANDBOX` (default `off`), `GROK_SANDBOX_AUTO_ALLOW_BASH`, `GROK_RESPECT_GITIGNORE`, `GROK_WEB_FETCH` (default off), `GROK_WEB_FETCH_PROXY`, `GROK_MEMORY` (default off), `GROK_SUBAGENTS` (default `0` in this table), `GROK_AGENT` (default `grok-build`), `GROK_WRITE_FILE`, `GROK_TOOL_SEARCH`, and `GROK_LSP_TOOLS` (default off).
- `[models]` sets `default` (example `"grok-build"`), `web_search`, `default_reasoning_effort`, `session_summary`, `image_description`, sampling defaults, `allowed_models`, `hidden_models`, and `disabled_models`.
- Custom and BYOK models use `[model.<name>]` with OpenAI-compatible or Anthropic Messages backends (`chat_completions`, `responses`, or `messages`), `env_key` or `api_key`, `context_window`, and reasoning flags.
- `[tools] respect_gitignore` defaults false. `[tools] disable_zdr_incompatible_tools` restricts tools that need xAI-hosted output (video) under ZDR. `[toolset.bash]` sets foreground timeout (default 120s), output byte limit (default 20000), max timeout (default 36000s), and auto-background on timeout (default true).
- `[session] auto_compact_threshold_percent` defaults to 85. `load_envrc` (default true) injects `.envrc` variables into bash.
- `[cli] channel` is `stable` or `alpha`. `[cli] auto_update` checks for CLI updates on launch.
- `[ui]` covers compact and screen modes, timestamps, thinking blocks, permission mode, hunk tracker mode, mermaid rendering, prompt suggestions, and voice dictation (`voice_keybind_enabled` for Ctrl+Space / F8; `/voice` still works when the keybind is off).
- `[memory] enabled` defaults off. Cursor and Claude compatibility scanners default on and can be disabled per surface under `[compat.cursor]` / `[compat.claude]` or `GROK_*_ENABLED` env vars.
- `HTTPS_PROXY`, `HTTP_PROXY`, and `NO_PROXY` apply to outbound traffic. `GROK_LOG_FILE`, `RUST_LOG`, and `GROK_CRASH_HANDLER` control logging and crash reports under `$GROK_HOME/crash/`.

### Enterprise Deployments

Primary source: https://docs.x.ai/build/enterprise

- Core hosts are `cli-chat-proxy.grok.com` (inference proxy and settings) and `auth.x.ai` (OAuth2/OIDC). Enterprise OIDC also needs the IdP domain.
- Optional hosts include `api.x.ai` (API-key path), `code.grok.com` (remote session sync, sharing, WebSocket relay), `assets.grok.com` (avatars), `x.ai` (shell-script installer and `grok update`), and `storage.googleapis.com` (installer CDN fallback).
- `npm install -g @xai-official/grok` is the documented alternative that does not require the `x.ai` download host.
- All connections use TLS 1.2 or 1.3 via `rustls`. There is no option to disable TLS. TLS-inspecting proxies need their CA in the OS trust store.
- The CLI honors `HTTPS_PROXY`, `HTTP_PROXY`, and `NO_PROXY`. Default pool idle timeout is 90 seconds (`GROK_POOL_IDLE_TIMEOUT_SECS`). Inference SSE per-chunk idle timeout defaults to 600 seconds. Docs recommend proxy idle timeouts of at least 10 minutes.
- Config layers, lowest to highest priority, are `/etc/grok/managed_config.toml`, `~/.grok/managed_config.toml`, `~/.grok/config.toml`, `~/.grok/requirements.toml`, and `/etc/grok/requirements.toml`. `requirements.toml` cannot be overridden by lower layers, remote settings, or user config. All layers support `[[version_overrides]]` and `$VAR` expansion.
- `/etc/grok/requirements.toml` is the MDM, golden-image, and onboarding pin for policies such as disabling telemetry, enforcing sandbox profiles, restricting tools, or pinning feature flags.
- Grok reads a subset of Claude Code `managed-settings.json` (permission rules, MCP allowlists, some telemetry/feedback flags, marketplace restrictions). `/etc/grok/requirements.toml` always takes precedence.
- Authentication methods are browser OIDC (`grok login`), device code (`grok login --device-auth`, RFC 8628), external `auth_provider_command`, and API key (`XAI_API_KEY` or `model.api_key`). Resolution per model is `model.api_key` > `model.env_key` > active session token > `XAI_API_KEY`.
- Enterprise OIDC uses `[auth.oidc]` or `GROK_OIDC_ISSUER` / `GROK_OIDC_CLIENT_ID`, with PKCE and `refresh_token` renewal. `auth_provider_command` prints a token or JSON; `GROK_AUTH_EXPIRED=1` marks a silent refresh.
- `disable_api_key_auth` in `requirements.toml` forces interactive IdP login for first-party xAI keys. BYOK endpoints whose `base_url` is not on `x.ai` keep working. `force_login_team_uuid` pins login to one or more team UUIDs and also turns on `disable_api_key_auth`.
- Headless permission modes include `dontAsk` (silently deny anything without an explicit allow) and `acceptEdits` (auto-approve file edits; prompt for shell). `--permission-mode dontAsk` is the CI example.
- `disable_bypass_permissions_mode = true` under `[ui]` in a root-owned `/etc/grok/requirements.toml` turns always-approve off and blocks `--yolo`, `--permission-mode bypassPermissions`, in-session toggles, and catch-all `allow` rules such as `*` or `**`. The lock is not honored from user-writable `~/.grok/requirements.toml`. Claude Code `disableBypassPermissionsMode` is not applied to Grok's always-approve.
- Session data path: local assembly, TLS to the inference proxy, inference (ZDR organizations use a dedicated service identity that skips logging), local tool execution, streamed response, then local history in `~/.grok/`. For ZDR organizations, prompts, code, and responses are not persisted at the inference layer.
- Zero Data Retention is enforced at the team level. When enabled for a team or enterprise, ZDR applies to Grok Build. Video tools under ZDR require user-supplied output storage.

### Video Output Storage under ZDR

Primary source: https://docs.x.ai/build/settings/zdr-video-storage

- Under ZDR, generated videos must be stored in user-supplied S3-compatible storage. Until storage is configured, video tools return an error.
- Configure `[tools.zdr_video_output_s3]` in `~/.grok/managed_config.toml` with `bucket`, `endpoint`, `region`, optional `key_prefix` (default `grok-videos/`), optional `expires_secs` (default 900), `read_write` credentials for the upload URL, and optional `read_only` credentials for playback.
- Grok Build presigns an upload URL so the video lands in the bucket and is not stored by SpaceXAI. Credentials themselves are never sent to xAI. Restart Grok Build after changing the config.
- Video tools are enabled if the privacy setting is off (`/privacy`).

## Sources

- https://docs.x.ai/build/overview
- https://docs.x.ai/build/modes-and-commands
- https://docs.x.ai/build/keyboard-shortcuts
- https://docs.x.ai/build/features/skills-plugins-marketplaces
- https://docs.x.ai/build/features/project-rules
- https://docs.x.ai/build/features/mcp-servers
- https://docs.x.ai/build/features/hooks
- https://docs.x.ai/build/features/sessions
- https://docs.x.ai/build/features/plan-mode
- https://docs.x.ai/build/features/permissions
- https://docs.x.ai/build/features/sandbox
- https://docs.x.ai/build/features/subagents
- https://docs.x.ai/build/features/worktrees
- https://docs.x.ai/build/features/background-tasks
- https://docs.x.ai/build/features/dashboard
- https://docs.x.ai/build/features/status-line
- https://docs.x.ai/build/features/theming
- https://docs.x.ai/build/settings
- https://docs.x.ai/build/settings/reference
- https://docs.x.ai/build/settings/zdr-video-storage
- https://docs.x.ai/build/cli/headless-scripting
- https://docs.x.ai/build/cli/reference
- https://docs.x.ai/build/cli/terminal-support
- https://docs.x.ai/build/enterprise
