---
name: T3 Code
slug: t3code
url: https://t3.codes/
docs: https://github.com/pingdotgg/t3code/tree/main/docs
kind: product
reviewed: 2026-09-29
---

# T3 Code

## Product

T3 Code is an open-source control surface for coding agents that already run on a person's machine. The repository calls it an agent harness control surface. It starts and steers Claude Code, Codex, Cursor, Grok Build, OpenCode, and Google Antigravity from one desktop, web, or mobile interface. T3 Code does not resell model tokens. A person installs and authenticates each provider CLI (or Antigravity's managed runtime) and keeps that provider's subscription or API credentials. Source: https://github.com/pingdotgg/t3code/blob/main/README.md

There is no dedicated documentation site. Official user guides live in the public repository under `docs/`, with the index at [docs/README.md](https://github.com/pingdotgg/t3code/blob/main/docs/README.md). The product homepage is [t3.codes](https://t3.codes/). The hosted web client is [app.t3.codes](https://app.t3.codes). Source: https://github.com/pingdotgg/t3code/blob/main/docs/README.md

A T3 Code server owns the workspace, provider processes, terminals, and Git. Web, desktop, and mobile clients talk to that server over authenticated RPC. The Electron desktop app bundles a server; its renderer follows the same boundary. Agents run on the environment machine, including when a phone or another computer is the client. Source: https://github.com/pingdotgg/t3code/blob/main/docs/internals/overview.md

A person installs the `t3` CLI, the desktop app, or both, then enables at least one provider in **Settings → Providers**. `t3` starts the server and opens the local web app. `t3 serve` runs headless. The desktop app can open a thread for the current directory with `t3 app`. The iOS and Android apps connect to a server through T3 Connect or a pairing URL. Installers cover curl and PowerShell for the CLI, plus winget, Homebrew, `.deb`, and Arch AUR packages for the desktop app. Source: https://github.com/pingdotgg/t3code/blob/main/docs/user/install.md

T3 Code is MIT-licensed software from T3 Tools Inc. GitHub Releases publish a stable train (latest `v0.0.42` as of this review) and a nightly train. `T3CODE_CHANNEL=nightly` installs nightlies; `preview` is a maintainers' test train that the installer and `t3 update` treat as opt-in. The README states the project is early and to expect bugs. The homepage states “Tolerated by over 300,000 devs”. T3 Code sells no paid plan of its own. Sources: https://github.com/pingdotgg/t3code/blob/main/LICENSE, https://github.com/pingdotgg/t3code/releases/tag/v0.0.42, https://t3.codes/

The agents T3 Code drives are separate products. Claude Code is specified in `claude-code`, Codex in `codex`, Cursor in `cursor`, and Grok Build in `grok-build`. OpenCode and Antigravity have no sibling spec files in this repository.

## Features

### Install T3 Code

Primary source: https://github.com/pingdotgg/t3code/blob/main/docs/user/install.md

- T3 Code runs coding agents on a computer and lets a person control them from the desktop, web, or mobile app.
- The machine where the agents work is set up first. A person can launch T3 Code and configure providers afterwards.
- The CLI installs with `curl -fsSL https://t3.codes/install.sh | sh` on Unix-like systems, or `irm https://t3.codes/install.ps1 | iex` in Windows PowerShell.
- The installer puts `t3` in `~/.local/bin`. Set `T3CODE_CHANNEL=nightly` for the nightly train, or `T3CODE_VERSION` to pin a version.
- `t3` starts the server and opens the web app. `t3 serve` starts the server without a browser. `t3 update` moves to a newer release. `t3 uninstall` removes the CLI.
- `t3 service install` keeps the server running in the background on macOS and Linux.
- `npx t3@latest` starts T3 Code once without installing it and needs Node.js for `npx`.
- There is no `t3` executable for Intel Macs. The desktop app is available there. A server on an Intel Mac is built from source with Node.js 24 and `vp`, then run with `node apps/server/dist/bin.mjs`.
- The desktop app installs from [GitHub Releases](https://github.com/pingdotgg/t3code/releases), `winget install T3Tools.T3Code`, `brew install --cask t3-code`, a `.deb` on Debian or Ubuntu, `yay -S t3code-bin` on Arch, or `yay -S t3code-nightly-bin` for Arch nightly.
- The `.deb` updates itself and asks for a password. If the desktop has no password prompt, the update fails and the person installs a new `.deb` by hand.
- **Settings → Connections** can choose a WSL distro so agents and projects run there. Provider CLIs install inside that distro. T3 Code installs its server runtime there automatically.
- With the desktop app already running on the same machine, `t3 app` opens a new thread for the current directory and adds the project if needed. `t3 app ../my-project` opens another path. A standalone server or an SSH session is not enough.
- The iOS app is [T3 Code](https://apps.apple.com/us/app/t3-code-remote-claude-more/id6787819824). The Android app is on [Google Play](https://play.google.com/store/apps/details?id=com.t3tools.t3code). The phone connects to a server on another machine.
- If the mobile app crashes during launch, **Settings → Diagnostics** on the next successful launch lists startup crashes from the last 7 days.

### Providers

Primary source: https://github.com/pingdotgg/t3code/blob/main/docs/user/install.md

- **Settings → Providers** enables a provider on a selected environment. Installation, login, and configuration belong to that environment's machine.
- Supported providers and login commands are Codex (`codex login`), Claude Code (`claude auth login`), Cursor (`agent login` with the `cursor-agent` binary), Grok Build (`grok login`), OpenCode (`opencode auth login`), and Antigravity (install and Google sign-in from provider settings).
- Provider CLIs must be on the server's `PATH`, or a **Binary path** is set in provider settings. Antigravity can use its managed runtime without a `PATH` entry.
- T3 Code warns when a provider version has known compatibility problems and can show a recommended version range.
- **Update now** appears when T3 Code can tell which installer owns the CLI (the provider's update command, Homebrew, or a global npm, pnpm, bun, or Vite+ install) and runs that installer.
- A person can add another provider instance for a separate account or configuration, each with its own environment variables. Secret values can be marked sensitive; after saving, T3 Code does not display their original values.
- Dedicated setup pages cover Codex, Claude, OpenCode, and Antigravity. Cursor and Grok Build use the shared provider settings.

### Codex

Primary source: https://github.com/pingdotgg/t3code/blob/main/docs/user/providers-codex.md

- The default Codex provider uses a normal Codex login on the environment machine.
- Two Codex instances can share `~/.codex` while a second account signs into a shadow home such as `~/.codex_personal`, so work and personal accounts continue the same threads and share Codex sessions while keeping separate logins and models.
- A completely separate `CODEX_HOME` with no shadow home keeps separate Codex sessions and configuration and cannot continue threads from the other home.
- The thread model picker can switch to another Codex instance that shares the thread's `CODEX_HOME` path.
- Codex can ask a question and keep working. The answer is sent from the thread's question panel. Unanswered questions survive reconnects. Dismissing a question sends nothing to Codex.
- Codex tools can request access to another app. The person approves one request, the current session, or permanent access from the thread on web, desktop, or mobile.
- When Codex hits a usage limit, the thread names the window that ran out and when it resets, when Codex reports them. On a workspace plan the message also says whether the workspace owner needs to add credits or raise the spend limit.
- `/feedback` in a Codex thread uploads the conversation and Codex logs to OpenAI and returns a thread ID for OpenAI support.

### Claude

Primary source: https://github.com/pingdotgg/t3code/blob/main/docs/user/providers-claude.md

- T3 Code uses Claude Code's login and configuration. A second account uses `CLAUDE_CONFIG_DIR` and its own provider instance.
- Existing threads can switch only between Claude instances with the same config directory. Separate directories stay isolated, including local conversation state.
- **Auto-compact after** in Claude provider settings accepts an integer between `100000` and `1000000` tokens. `/compact` and **Compact context** from the context meter also reduce context when the provider supports it.
- If a Claude subscription runs out mid-turn, the thread shows which limit was reached and the remaining wait when Claude provides a reset time. Claude Code holds the turn until that window reopens.
- Claude skills come from the config directory `skills` folder and the project's `.claude/skills` folder. The config-directory copy wins on a name conflict. `$` in the composer selects a skill.
- A Claude instance can point at OpenRouter or another router through environment variables such as `ANTHROPIC_BASE_URL` and `ANTHROPIC_AUTH_TOKEN`. Custom model IDs are added with **Add custom model**.

### OpenCode

Primary source: https://github.com/pingdotgg/t3code/blob/main/docs/user/providers-opencode.md

- T3 Code requires OpenCode 1.14.19 or newer, including when connecting an existing OpenCode server.
- An empty **Server URL** lets T3 Code start OpenCode locally. A configured **Server URL** and password connect to an existing server.
- After a lost connection, sending another prompt reconnects to the same OpenCode session.
- **Auto** permission mode has the same rules as **Supervised** because OpenCode has no AI approval reviewer. `.env` and `.env.local` need approval in restricted modes; `.env.example` is allowed.
- **Allow for workspace** applies to matching requests in other OpenCode sessions using the same workspace.
- **Refresh provider status** reloads models, commands, and skills after an OpenCode login or configuration change.

### Antigravity

Primary source: https://github.com/pingdotgg/t3code/blob/main/docs/user/providers-antigravity.md

- T3 Code runs Google's official Antigravity ACP agent on the selected environment. Sign-in is separate from the Antigravity IDE or CLI. Provider setup is not available in the mobile app.
- Sign-in methods are Google account, Gemini Enterprise, Gemini API key, and Agent Platform / Vertex AI.
- Managed installation supports Apple Silicon macOS, Linux x64 or ARM64, and Windows x64 or ARM64. Intel Macs can connect to a supported remote environment.
- A person can instead set **Binary path** to a manual ACP Registry install.
- The model list comes from the Antigravity account. T3 Code's separate Plan mode is unavailable; Antigravity's native `/plan` command is used instead.
- Antigravity cannot rewind its conversation. Reverting a thread or editing and resubmitting an earlier turn is unavailable.
- Project skills are read from `.gemini/skills`, then `.agents/skills`, then the legacy `.agent/skills` directory. User skills live in `~/.gemini/config/skills` or `~/.gemini/antigravity-cli/skills`.
- Antigravity accepts images, PDFs, text files, and supported audio formats natively, with documented per-type size limits. ZIP archives and videos are passed as file paths.
- Subagent activity is grouped into batches. A person cannot open or control individual subagents.
- `/logout` in a thread signs out that Antigravity instance and stops its other sessions.

### Messages and context

Primary source: https://github.com/pingdotgg/t3code/blob/main/docs/user/composer.md

- The composer sends a task to the agent. Messages can contain up to 120,000 characters.
- Pasting 32 KiB or more of text adds that fragment as a text-file attachment. `Cmd+Shift+V` or `Ctrl+Shift+V` keeps a large paste editable in the composer.
- A message can attach up to 100 files. Each image can be up to 10 MiB, with at most 80 MiB of images in one message. Other files, including videos, can be up to 50 MiB each.
- A video attachment gives the agent a file path. It does not enable native video input.
- On mobile, files can be sent through another app's system share sheet. HEIC and HEIF photos convert to JPEG.
- On web and desktop, a message sent during a running turn waits as a dashed bubble and goes out after the next tool call or when the turn ends. **Follow-up behavior** chooses **Queue** or **Steer**. **Steer** sends new messages into the running turn immediately.
- **Stop** halts the running turn and returns every queued message to the composer.
- A turn runs the provider's own agent loop, not a single reply. Claude Code, for example, decides what each step requires from what it learned in the previous step, chaining many tool calls and course-correcting until it ends the turn. T3 Code shows each tool call in the thread. Source: https://code.claude.com/docs/en/how-claude-code-works
- Mobile keeps local copies of draft attachments so messages can be queued while disconnected. Drafts and queued messages survive app restarts.
- **Settings → Providers → Models** adds an unlisted model on web and desktop. Antigravity uses its account catalog and does not support custom models.
- T3 Code remembers provider, model, and model options for new threads. A project's configured model takes precedence.
- On web and desktop, selected assistant text can be cited in the composer with an optional comment. Mobile displays saved quotes but does not create citations.
- `ArrowUp` in an empty composer recalls earlier prompts sent in the thread. Attachments and extras from the original message are not restored.
- **Edit from here** rewinds the conversation to before a sent message when the provider supports rewind. **Revert files too** is offered only for a worktree that no other thread is using.
- `Cmd+S` or `Ctrl+S` stashes the current prompt and attachments. Stashes with uploaded files must be restored in their original environment. Uploaded files are retained for 24 hours.
- On iPhones with iOS 26 or later, the composer microphone records up to five minutes and transcribes on device. T3 Code deletes the temporary audio after transcription or cancellation.
- `/` opens commands. `$` adds a skill from the selected environment and provider. Provider commands must start the message. T3 Code commands such as `/model` and `/plan`, and skill mentions, work on any line.
- Context chips include files, terminal excerpts, review comments, preview annotations, and pull requests. `#` browses recent pull requests in the current project's repository.
- Attached files can be previewed with syntax highlighting, rendered Markdown, HTML, CSV, or TSV, and audio playback. Files outside the workspace open read-only.
- When an agent asks a question that accepts a custom answer, files and images can be attached to that answer. Questions that only accept predefined choices do not offer attachments. Source: https://github.com/pingdotgg/t3code/blob/main/docs/user/question-attachments.md

### Permission modes

Primary source: https://github.com/pingdotgg/t3code/blob/main/docs/user/permission-modes.md

- Permission modes control when an agent needs approval. The mode is chosen in the composer and applies to that thread.
- The default for new threads is set in **Settings → General → New threads → Permissions**. Projects can override the environment default. The initial default is **Full access**.
- **Supervised** requests approval for commands and file changes.
- **Auto-accept edits** approves file edits automatically. Other actions can still require approval.
- **Auto** uses the provider's automatic review on Codex, Claude, and Cursor. OpenCode and Antigravity fall back to asking.
- **Full access** allows commands and edits without approval prompts. Antigravity can still send native approval requests in this mode.
- For Grok, **Always allow this session** remembers the matching command or tool input.

### Working with threads

Primary source: https://github.com/pingdotgg/t3code/blob/main/docs/user/thread-sidebar.md

- A new thread keeps the current project and carries model and mode selections unless the destination project has its own model default.
- **New worktree** gives the thread a separate branch and working directory. **New thread in this worktree** continues in an existing worktree.
- `Cmd+Enter` or `Ctrl+Enter` starts a new thread in the background and opens another draft.
- Shift-clicking models in a new thread's model picker starts a separate thread and worktree per model. This requires a Git project.
- Threads can be pinned, reordered, settled, snoozed, archived, and undone from a five-second notice. The server saves the order across connected devices.
- Settling moves finished work out of the active list without deleting the conversation. Environments settle inactive threads after three days by default and can settle threads whose pull request merged.
- **Auto-settle behavior** on a thread can disable automatic settlement for that thread.
- The command palette (`Cmd/Ctrl+K`) searches threads across connected environments. Message search starts after two characters and includes user messages and final agent responses.
- **Agents** follows work delegated to subagents. Expanding a tool call shows its full command and output.
- **Snooze** parks a thread until a chosen date, time, or duration. Several selected threads can be snoozed together on web and desktop.

### Terminal history

Primary source: https://github.com/pingdotgg/t3code/blob/main/docs/user/terminal.md

- Each terminal keeps up to 5,000 lines and 8 MiB of scrollback on its environment server. T3 Code removes the oldest output when either limit is reached.
- These limits apply when reconnecting and when T3 Code restores saved terminal history. A client can show less scrollback than the server keeps.

### Source control

Primary source: https://github.com/pingdotgg/t3code/blob/main/docs/user/source-control.md

- T3 Code integrates with GitHub, GitLab, Forgejo, Gitea, Bitbucket, and Azure DevOps to clone and publish repositories, create pull requests, and review changes.
- GitHub uses GitHub CLI 2.81.0 or newer (`gh auth login`). GitLab uses `glab auth login`. Forgejo and Gitea share one integration entry (`fj` preferred, `tea` fallback). Bitbucket uses `T3CODE_BITBUCKET_ACCESS_TOKEN` or email plus API token. Azure DevOps uses Azure CLI with the DevOps extension.
- **Add Project** in the command palette clones a repository. The project opens while the clone runs in the background.
- **Publish Repository** creates a hosted repository for a local Git repo without a remote, adds it as `origin`, and pushes commits.
- A thread's Git actions commit, push, and create a pull request. T3 Code can generate commit messages, review titles, and descriptions. Writing style and model are set in **Settings → Source Control**.
- **Pull requests** reviews changes and comments, requests reviewers, checks out a branch, or merges. GitHub, GitLab, and Azure DevOps support auto-merge while checks are outstanding.
- GitHub sharing is off by default. **Settings → Connections → GitHub sharing** can grant **Read PRs** or **Read and act** so another connected environment signed into the same GitHub account can serve review details and actions.
- Viewed-file marks on GitHub use GitHub's own marks. On Forgejo, GitLab, Bitbucket, and Azure DevOps the connected server stores them.
- The **Code** tab is a web and desktop surface. The mobile app reports pull-request status but does not show the diff.
- A thread can hold several linked pull requests, including reviews from another repository on the same host. Agents can call the `link_pull_request` tool.
- The Pull Requests page shows GitHub stack position. **Merge stack** and **Rebase stack** operate on the selected pull request and the unmerged layers below it.

### Settings and project overrides

Primary source: https://github.com/pingdotgg/t3code/blob/main/docs/user/project-settings.md

- Settings pages apply to a selected project and environment. Device preferences such as appearance stay on the current device. Everything else is stored on a server.
- A project can override environment defaults. Settings resolve in this order: project override, environment setting, `t3.json`, then the built-in default.
- General holds the model and workspace for new threads. Integrations controls agent browser access. Source Control holds automatic pull, the default pull-request merge method, and text generation.
- Project actions belong to a project. A project's `t3.json` actions can be imported there.
- New worktrees initialize git submodules recursively by default. **Submodules** can be **Top level only** or **Skip**, matching `worktreeSubmodules` in `t3.json`.
- **Settings → Storage** can remove T3-managed worktrees after inactive days, after merging, when they have no commits beyond the default branch, or when their last thread is deleted.
- Project icons can be automatic, an emoji, a monogram, or an image (SVG, PNG, ICO, JPEG, GIF, AVIF, or WebP).
- **Automatically pull** fast-forwards the default-branch checkout when it has no local changes, untracked files, or local commits.
- A repository-root `t3.json` can set `iconPath`, `defaultThreadEnvMode` (`local` or `worktree`), `worktreeSubmodules`, and up to 50 named scripts. Scripts can run on worktree create and can open a desktop in-app browser preview. Source: https://t3.codes/schema/t3.json

### Appearance and themes

Primary source: https://github.com/pingdotgg/t3code/blob/main/docs/user/appearance.md

- Web and desktop choose a theme and follow the system appearance or stay in light or dark mode. Appearance preferences are saved separately on each device or browser.
- Mobile has its own themes and text, code, and terminal preferences. It does not follow environment themes.
- Android 12 or newer can use the **Material You** theme and **Material You Layout**.
- **Create theme** adjusts a palette or imports a T3 Code or VS Code theme. Themes export as JSON.
- `t3 theme set`, `t3 theme clear`, and `t3 theme show` publish a default theme from the server. Saved custom themes live in `~/.t3/userdata/themes/`.
- **Panel animations** can last up to 400 ms unless the operating system has reduced motion enabled.

### Keybindings

Primary source: https://github.com/pingdotgg/t3code/blob/main/docs/user/keybindings.md

- **Settings → Keybindings** lists every command and shortcut on web and desktop. The same rules live in `~/.t3/userdata/keybindings.json` on the environment machine.
- **Settings → General → Send shortcut** chooses whether Enter sends. **Follow-up behavior** chooses Queue or Steer while the agent runs.
- Shortcuts select model, host, effort, access mode, workspace, and Git branch. The workspace menu includes the current checkout, a new worktree, and the previous worktree.
- On iPad with a hardware keyboard, `Cmd+1` through `Cmd+9` open the first nine displayed threads. `Cmd+K` opens the command palette.
- Project scripts are addressable as `script.{id}.run`.
- `thread.stop` has no default shortcut. `thread.undo` (`mod+z`) reverses recent sidebar actions. `navigation.back` and `navigation.forward` move through visited pages.
- The desktop quit shortcut can require a hold, a double press, or a single press.
- While the command palette or model picker is open, number shortcuts select its entries instead of switching threads. Source: https://github.com/pingdotgg/t3code/blob/main/docs/user/keyboard-focus.md

### SnapShots

Primary source: https://github.com/pingdotgg/t3code/blob/main/docs/user/snap-shot.md

- A SnapShot captures the window a person is working in and attaches it to the current draft, including the app name, window title, and, when available, accessibility data.
- SnapShots are off by default. They are available in the desktop app on macOS, Windows, and Linux with Wayland. X11 sessions are not supported.
- The default shortcut on macOS and Windows is both Shift keys. Pressing it while T3 Code is in front captures T3 Code itself.
- **Include app text** controls whether captures include accessibility data.
- Linux setup covers GNOME (bundled extension), KDE Plasma 6, Hyprland, Omarchy, Niri, and other Wayland desktops through the screenshot portal.

### Import browser sessions

Primary source: https://github.com/pingdotgg/t3code/blob/main/docs/user/browser-import.md

- The desktop app can import cookies from another browser into a preview-browser profile under **Settings → Integrations → Browser profiles**.
- The import is a one-time copy. Later logins stay separate. Partitioned cookies are skipped on all platforms.
- On macOS, Safari imports need Full Disk Access. On Windows, import supports Firefox and Helium profiles that use standard profile encryption. Other Chromium-based browsers use app-bound encryption and cannot be imported.

### Devices

Primary source: https://github.com/pingdotgg/t3code/blob/main/docs/user/devices.md

- The Device panel shows a live iOS Simulator or Android Emulator beside a thread. Agents use `device_*` tools and the `agent-device` command line that T3 Code sets up.
- iOS needs macOS with Xcode. Android needs SDK Platform-Tools, Android Emulator, Command-line Tools, and a virtual device from Android Studio.
- The screen is interactive. The toolbar covers Home, Back, and Recents on Android, rotate on iOS, power off, 3D view, and foldable posture controls.
- The Tools drawer can switch light and dark mode, change text size, overlay accessibility frames, set a fake location, and grant or revoke app permissions.
- **Agent device access** in **Settings → Integrations → Devices** must be on before T3 Code installs `agent-device` for agents.
- The device stream works over the local network, Tailscale, and T3 Connect. Live video needs HTTPS or localhost.
- **Device hosts** add SSH machines that expose simulators or emulators. Password prompts are not supported.
- The connected T3 server manages device-hub and agent-tool versions on its machine and configured SSH hosts.

### Usage and limits

Primary source: https://github.com/pingdotgg/t3code/blob/main/docs/user/usage.md

- **Usage** combines Codex, Claude Code, Grok Build, OpenCode, Antigravity, and Cursor history from connected environments. It shows token use, cache savings, model breakdowns, and estimated API-equivalent cost. These estimates are not a subscription bill.
- Custom model prices can be set per environment as USD rates per million input and output tokens.
- **Usage → Limits** pools subscription accounts per provider and shows remaining quota and reset times when the provider reports them.
- `/usage-limits` checks the current model's limits without running the agent.
- **Settings → Providers → Usage providers → Add hub** connects a CLIProxyAPI hub so pooled accounts appear under Limits.
- An iOS or Android **Subscription usage** widget shows remaining Codex and Claude quotas.

### Product usage data

Primary source: https://github.com/pingdotgg/t3code/blob/main/docs/user/telemetry.md

- The T3 Code server sends product usage events to PostHog, associated with a hashed account or installation identifier.
- Events include provider, model, reasoning effort, permission mode, turn result, duration, and main-agent token totals when available.
- Events do not include prompts, responses, file contents, authentication tokens, conversation IDs, raw provider events, or child-agent output.
- `T3CODE_TELEMETRY_ENABLED=false` in the server environment disables collection.

### Remote access

Primary source: https://github.com/pingdotgg/t3code/blob/main/docs/user/remote-access.md

- A phone, browser, or another desktop app can connect to T3 Code running on a different machine. That machine must stay running and reachable.
- **T3 Connect** exposes an environment to other devices without router forwarding. On a desktop host, sign in under **Settings → Connections** and enable T3 Connect. On a CLI host, run `t3 connect`.
- Direct pairing uses **Network access** in the desktop app, `t3 serve --host <private-ip>`, or `t3 pair` for an already-running server. Scan the QR code or paste the pairing URL.
- **Load balancing** can automatically choose a machine for new threads in projects grouped across connected environments. Preferences are Prefer, Normal, Less often, or Manual only.
- `t3 serve --tailscale-serve` and `t3 pair --tailscale` create an HTTPS pairing link on a tailnet.
- [app.t3.codes](https://app.t3.codes) needs an HTTPS endpoint and connects directly to the server. A hosted pairing link does not proxy traffic or convert HTTP to HTTPS.
- Desktop-managed SSH starts or reuses a T3 Code server on a Linux host or Apple Silicon Mac and opens the port forward. Projects, provider credentials, and agent work stay on the remote machine.
- **Settings → Connections** lets authorized administrators create pairing links and revoke client sessions. Command-line management is `t3 auth --help`.
- Turning off **Local environment** makes the desktop app remote-only: no local agents or terminals run, and other devices can no longer connect to that computer.

### Running in the background

Primary source: https://github.com/pingdotgg/t3code/blob/main/docs/user/background-service.md

- On Linux and macOS, `t3 service install` runs T3 Code as a user service so a terminal does not need to stay open.
- Linux uses systemd user services and enables lingering so T3 Code starts at boot and keeps running after logout.
- macOS starts the service at login and stops it at logout. The Mac must stay logged in and awake for unattended remote access.
- Windows background services are not supported.
- `t3 update` downloads the newest release on the current channel. `t3 uninstall` removes the service and launcher and keeps projects, threads, and settings under `~/.t3/userdata`.
- `preview` builds can be broken and are never offered as updates. The installer and `t3 update` ask for confirmation before installing one.

### Updating T3 Code

Primary source: https://github.com/pingdotgg/t3code/blob/main/docs/user/updating.md

- When a server is behind the web or desktop app, an update notice appears in the conversation and **Settings → Connections**.
- Server updates restart the connection and can interrupt active agents and terminal commands. Saved threads, settings, and project files remain.
- **Continue threads after restarts** is off by default. When enabled, supported active threads resume after an update, crash, or machine restart.
- Update actions include **Update server**, **Update the desktop app**, and **Copy update command**. On the host, `t3 update <client-version>` matches the notice.
- The mobile app can update a connected environment from **Settings → Environments** and can download its own App Store or Google Play updates in the background.

### Mobile notifications

Primary source: https://github.com/pingdotgg/t3code/blob/main/docs/user/mobile-notifications.md

- With T3 Connect and **Device Notifications** enabled, the phone alerts when an agent finishes, fails, needs approval, or asks for input.
- **Ongoing Agent Activity** on Android and **Live Activity Updates** on iOS follow work without opening the app. Finished results remain visible for up to 15 minutes.
- Background delivery requires T3 Connect. A direct or Tailscale connection alone does not enable push notifications.
- Android notifications require Android 7.0 or newer and Google Play services.

### Welcome wizard

Primary source: https://github.com/pingdotgg/t3code/blob/main/docs/user/welcome-wizard.md

- A setup flow appears when opening a new installation or connecting to the hosted app for the first time. Existing workspaces skip it.
- The wizard can connect computers through T3 Connect or a pairing link, then checks Claude Code and Codex on each selected computer.
- It finds directories Claude Code or Codex has used and can import git repositories active within the last 30 days that have at least three conversations.
- Imported conversations keep the first user prompt and the newest remaining visible user and assistant messages, with 200 messages total. Tool activity and attachments are omitted.

### Open source licenses

Primary source: https://github.com/pingdotgg/t3code/blob/main/docs/user/open-source-licenses.md

- **Settings → General → Open source licenses** on web and desktop, or **Settings → About T3 Code** on mobile, lists third-party license and attribution notices, including optional device tools installed on demand.
- The repository is MIT-licensed, copyright 2026 T3 Tools Inc. Source: https://github.com/pingdotgg/t3code/blob/main/LICENSE
- The maintainers are not actively accepting contributions. Small bug, reliability, and performance fixes are the work they say they are most likely to accept. Feature requests belong in Ideas discussions. Support is also offered in Discord. Sources: https://github.com/pingdotgg/t3code/blob/main/CONTRIBUTING.md, https://github.com/pingdotgg/t3code/blob/main/README.md
- Desktop and CLI builds are published on GitHub Releases, including stable tags such as `v0.0.42` and dated nightlies. Source: https://github.com/pingdotgg/t3code/releases

## Sources

- https://github.com/pingdotgg/t3code/blob/main/docs/README.md
- https://github.com/pingdotgg/t3code/blob/main/docs/user/install.md
- https://github.com/pingdotgg/t3code/blob/main/docs/user/composer.md
- https://github.com/pingdotgg/t3code/blob/main/docs/user/question-attachments.md
- https://github.com/pingdotgg/t3code/blob/main/docs/user/thread-sidebar.md
- https://github.com/pingdotgg/t3code/blob/main/docs/user/permission-modes.md
- https://github.com/pingdotgg/t3code/blob/main/docs/user/terminal.md
- https://github.com/pingdotgg/t3code/blob/main/docs/user/source-control.md
- https://github.com/pingdotgg/t3code/blob/main/docs/user/project-settings.md
- https://github.com/pingdotgg/t3code/blob/main/docs/user/appearance.md
- https://github.com/pingdotgg/t3code/blob/main/docs/user/keybindings.md
- https://github.com/pingdotgg/t3code/blob/main/docs/user/keyboard-focus.md
- https://github.com/pingdotgg/t3code/blob/main/docs/user/snap-shot.md
- https://github.com/pingdotgg/t3code/blob/main/docs/user/browser-import.md
- https://github.com/pingdotgg/t3code/blob/main/docs/user/devices.md
- https://github.com/pingdotgg/t3code/blob/main/docs/user/usage.md
- https://github.com/pingdotgg/t3code/blob/main/docs/user/telemetry.md
- https://github.com/pingdotgg/t3code/blob/main/docs/user/remote-access.md
- https://github.com/pingdotgg/t3code/blob/main/docs/user/background-service.md
- https://github.com/pingdotgg/t3code/blob/main/docs/user/updating.md
- https://github.com/pingdotgg/t3code/blob/main/docs/user/mobile-notifications.md
- https://github.com/pingdotgg/t3code/blob/main/docs/user/welcome-wizard.md
- https://github.com/pingdotgg/t3code/blob/main/docs/user/open-source-licenses.md
- https://github.com/pingdotgg/t3code/blob/main/docs/user/providers-codex.md
- https://github.com/pingdotgg/t3code/blob/main/docs/user/providers-claude.md
- https://github.com/pingdotgg/t3code/blob/main/docs/user/providers-opencode.md
- https://github.com/pingdotgg/t3code/blob/main/docs/user/providers-antigravity.md
- https://github.com/pingdotgg/t3code/blob/main/docs/internals/overview.md
- https://code.claude.com/docs/en/how-claude-code-works
- https://t3.codes/schema/t3.json
- https://github.com/pingdotgg/t3code/blob/main/README.md
- https://github.com/pingdotgg/t3code/blob/main/LICENSE
- https://github.com/pingdotgg/t3code/blob/main/CONTRIBUTING.md
- https://github.com/pingdotgg/t3code/releases
- https://github.com/pingdotgg/t3code/releases/tag/v0.0.42
- https://t3.codes/
- https://app.t3.codes
- https://apps.apple.com/us/app/t3-code-remote-claude-more/id6787819824
- https://play.google.com/store/apps/details?id=com.t3tools.t3code
