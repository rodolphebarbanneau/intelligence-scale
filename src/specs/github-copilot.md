---
name: GitHub Copilot
slug: github-copilot
url: https://github.com/features/copilot
docs: https://docs.github.com/en/copilot
kind: product
reviewed: 2026-09-28
---

# GitHub Copilot

## Product

GitHub Copilot is GitHub’s AI assistant for writing, understanding, and shipping software. It suggests code as you type, answers questions about a codebase, reviews changes, and works on tasks you assign it. Because Copilot is built into GitHub, it uses the repository, its history, issues, pull requests, and repository automations as context. A change can start as an issue, be picked up by an agent, return as a pull request, be reviewed, and be merged in the same workflow.

Individuals can start with Copilot Free, subscribe to Copilot Pro, Copilot Pro+, or Copilot Max, or qualify for Copilot Student. Verified teachers and maintainers of popular open source projects may be eligible for free Copilot Pro. Organization and enterprise owners buy Copilot Business or Copilot Enterprise seats and decide who has access, which features and models are available, which files Copilot can see, and how usage is billed. Members request access from an organization or enterprise that already has a plan. The product you adopt is Copilot itself; it hosts many models rather than being a single model.

Copilot runs in Visual Studio Code, Visual Studio, JetBrains IDEs, Eclipse, Xcode, Vim/Neovim, and Azure Data Studio; on github.com and GitHub Mobile; in Windows Terminal; in GitHub Copilot CLI; in the GitHub Copilot desktop app on macOS, Linux, and Windows; and in GitHub Desktop for commit messages and summaries. You can also call the same platform through the GitHub Copilot SDK. The GitHub Copilot app is the surface GitHub documents for coordinating parallel agent work, issues, pull requests, and the pull request lifecycle in one workspace. Copilot is not currently available for GitHub Enterprise Server.

How you use it depends on the surface. In an IDE you take ghost-text completions, next edit suggestions, and chat or agent mode that can edit local files. On GitHub you open Copilot Chat from any page or at https://github.com/copilot, ask about a repository, issue, or pull request, and start Copilot cloud agent from issues, the agents tab, Chat, the dashboard, new repositories, or failing Actions runs. Cloud agent runs in an ephemeral GitHub Actions environment, can research a repository, plan, edit a branch, and open a pull request. Copilot CLI and the Copilot app run agent sessions on your machine or in a cloud sandbox. Copilot code review comments on pull requests and can review a selection in the IDE.

Plans split included GitHub AI Credits, model choice, and some features. Copilot Free limits completions and uses auto model selection only. All documented plans include Copilot CLI and the Copilot app. Cloud agent is available on all paid Copilot plans; Business and Enterprise need an administrator to enable the policy. Capabilities also depend on the client and on organization or enterprise policies. GitHub Code Quality is a separate GitHub product that the code-review docs point to for rules-based analysis and coverage metrics. GitHub Spark appears on the plans page as a public-preview feature; this dossier does not expand it beyond that listing.

## Features

### Code suggestions

Primary source: https://docs.github.com/en/copilot/concepts/completions/code-suggestions

- Ghost text suggestions appear as dimmed text at the cursor as you type. You can also describe a goal in a natural-language comment and receive suggested code.
- Next edit suggestions predict where the next edit is likely to be and what that edit should be. In Visual Studio, Xcode, and Eclipse the docs mark next edit suggestions as public preview. In Visual Studio Code they are a current completions feature.
- Supported editors for suggestions include Visual Studio Code, Visual Studio, JetBrains IDEs, Vim/Neovim, Azure Data Studio (SQL), Xcode, and Eclipse.
- Copilot provides suggestions for many languages and frameworks. The docs say it works especially well for Python, JavaScript, TypeScript, Ruby, Go, C#, and C++, and can assist with database queries, APIs, frameworks, and infrastructure as code.
- You can switch the model used for ghost text suggestions in current VS Code, Visual Studio 17.14 Preview 2 or later, and current JetBrains IDEs with the latest Copilot extension. Changing that model does not change next edit suggestions or Copilot Chat.
- On Copilot Free and Copilot Pro the inline-suggestion model switcher is on by default. On Copilot Business and Copilot Enterprise the organization or enterprise must enable Editor preview features.
- On Copilot Free, all completions count against a monthly completions quota regardless of model. Source: https://docs.github.com/en/copilot/get-started/plans
- Copilot Free includes 2,000 completions per month. Paid plans keep code completions and next edit suggestions unlimited and do not bill them in AI credits. Source: https://docs.github.com/en/copilot/get-started/plans
- The Copilot feature matrix (public preview) lists code completion in VS Code, Visual Studio, JetBrains, Eclipse, Xcode, and Neovim, and next edit suggestions in VS Code and Visual Studio, with JetBrains, Eclipse, and Xcode marked preview. Source: https://docs.github.com/en/copilot/reference/copilot-feature-matrix

### Copilot Chat

Primary source: https://docs.github.com/en/copilot/concepts/about-github-copilot-chat

- Copilot Chat is the conversational interface for coding assistance, explanations, unit tests, and suggested fixes.
- Chat is available on the GitHub website, in supported IDEs, in GitHub Mobile, in GitHub Copilot CLI, and in the GitHub Copilot app.
- On GitHub, Chat is available from any page. You can start at https://github.com/copilot, ask follow-up questions in a thread, stop a response, and switch or compare models. Source: https://docs.github.com/en/copilot/how-tos/copilot-on-github/chat-with-copilot/chat-in-github
- Copilot Chat on GitHub stores up to 100 recent conversations. Messages are kept for 28 days, then deleted. Source: https://docs.github.com/en/copilot/how-tos/copilot-on-github/chat-with-copilot/chat-in-github
- You can attach JPEG, PNG, GIF, WEBP, PDF, HEIC, and HEIF files when the selected model supports image input. Attachments are on all Copilot plans and on by default. Source: https://docs.github.com/en/copilot/how-tos/copilot-on-github/chat-with-copilot/chat-in-github
- Viewing, editing, and downloading files Copilot generates in Chat on GitHub is in public preview. Subthreads let you branch a conversation from an earlier question. Source: https://docs.github.com/en/copilot/how-tos/copilot-on-github/chat-with-copilot/chat-in-github
- Starting a cloud agent session from Chat on GitHub carries the chat context. You can keep chatting while the session runs and ask about progress. Chat can also read agent session logs for pull requests Copilot created. Source: https://docs.github.com/en/copilot/concepts/about-github-copilot-chat
- In the IDE, Chat modes include agent mode (autonomous edits and tool use in the local environment), plan mode (a structured plan before implementation), and ask mode (answers and suggestions without making code changes). Source: https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-ide
- Plans list Chat in IDEs, inline chat, slash commands, Chat in GitHub Mobile, Chat on GitHub, and Chat in Windows Terminal. Copilot Chat skills in IDEs are available in Visual Studio Code and Visual Studio and are not available on Copilot Free. Source: https://docs.github.com/en/copilot/get-started/plans
- Personal, repository, and organization custom instructions tailor Chat responses in GitHub, Visual Studio Code, and Visual Studio. Source: https://docs.github.com/en/copilot/concepts/about-github-copilot-chat
- On GitHub, the GitHub MCP server is configured automatically so Chat can perform a limited set of GitHub tasks on request, such as creating branches or merging pull requests. Source: https://docs.github.com/en/copilot/concepts/about-github-copilot-chat
- GitHub Desktop uses Copilot for commit messages and summaries. Source: https://docs.github.com/en/copilot/get-started/where-to-use-github-copilot
- Plans list Copilot pull request summaries as a Copilot feature. Source: https://docs.github.com/en/copilot/get-started/plans

### Copilot cloud agent

Primary source: https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent

- Copilot cloud agent researches a repository, creates an implementation plan, and makes code changes on a branch. You review the diff, iterate, and create a pull request, or ask for a pull request immediately.
- Documented tasks include bug fixes, incremental features, test coverage, documentation, technical debt, and merge conflicts.
- You can start a session from GitHub issues, the agents tab, the dashboard, Copilot Chat, new repositories, failing GitHub Actions runs, GitHub Mobile, Visual Studio Code, JetBrains IDEs, Eclipse, Visual Studio 2026, the REST API, GitHub CLI, the GitHub MCP server, Jira, Slack, Microsoft Teams, Azure Boards, Linear, or Raycast. Source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/start-copilot-sessions
- Mention `@copilot` on an existing pull request to ask the agent to make changes.
- Security campaigns can assign alerts to Copilot.
- Work runs in an ephemeral GitHub Actions development environment where the agent can explore code, edit files, and run tests and linters.
- Cloud agent is distinct from IDE agent mode. Agent mode edits in the local environment. Cloud agent works in the Actions-powered environment and can open a pull request.
- Deep research, planning, and iterating on a branch before a pull request are available on GitHub.com, and in public preview for Microsoft Teams and Slack. Azure Boards, Jira, and Linear integrations open a pull request directly.
- Cloud agent is available on all paid Copilot plans. Business and Enterprise subscribers need an administrator to enable the policy. Repository owners can opt repositories out.
- Each session has a hard 59-minute maximum. You can set a shorter timeout in `copilot-setup-steps.yml`.
- The agent can change only the repository specified when the task starts, works on one branch at a time, and opens exactly one pull request per task.
- Default context is that repository. The GitHub MCP server is configured by default for issues and historic pull requests there. Broader access is configured in repository MCP settings.
- Cloud agent works only with repositories hosted on GitHub.
- Rulesets or branch protection that the agent cannot satisfy block it. You can add Copilot as a bypass actor on a ruleset.
- Cloud agent uses GitHub Actions minutes and AI credits. Included minutes and credits cover use until they run out.
- You can select the model (and, for supported models, reasoning level) in supported entry points. Source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/start-copilot-sessions
- Custom instructions, Copilot Memory (public preview on eligible individual plans), MCP servers, custom agents, hooks, and skills customize how the agent works.
- The GitHub MCP server and Playwright MCP server are enabled by default for cloud agent and code review.
- Automations run cloud agent on a schedule or on repository events. They are available on Pro, Pro+, Max, Business, and Enterprise, only in private or internal repositories, and are created from the Agents tab or the Copilot app. Source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations
- Automation triggers are hourly, daily, or weekly schedules; issue created; pull request opened; and pull request synchronized, with optional search and file-change filters. Source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations
- By default, automations ignore events from users without write access. You choose which tools an automation may use. Sessions and logs are visible to people with repository access; the automation definition is private to its creator. Source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations
- When an automation changes an issue, it can explain the change and rate confidence, applying high-confidence changes and holding others for review. Source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations

### GitHub Copilot CLI

Primary source: https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli

- Copilot CLI runs Copilot from the terminal to answer questions, write and debug code, and interact with GitHub.com, including making changes and creating a pull request.
- It runs on Linux, macOS, and Windows in PowerShell or WSL.
- Interactive mode starts with `copilot`. Plan mode (Shift+Tab) builds a structured plan before writing code. Programmatic mode uses `-p` / `--prompt` and then exits.
- Local sandboxing (`/sandbox enable`) restricts filesystem, network, and system access. Cloud sandboxing (`copilot --cloud`) runs the session in an isolated cloud environment. Both sandbox types are in public preview.
- Cloud sandbox policies inherit from Copilot cloud agent policies, including firewall rules.
- You can steer a running conversation, enqueue follow-ups, and give inline feedback when you reject a tool request.
- Context auto-compacts near 95% of the token limit. `/compact` and `/context` give manual control and a usage breakdown.
- Customization includes custom instructions (combined rather than priority fallback), MCP servers, custom agents and built-in subagents, hooks, skills, and Copilot Memory.
- Trusted-directory confirmation is required at session start. Tools that modify or execute files prompt for approval unless you pass `--allow-all-tools`, `--allow-tool`, or `--deny-tool`.
- For Copilot Business and Copilot Enterprise, CLI respects enterprise, organization, and repository content exclusion.
- CLI cannot currently enforce the organization MCP-servers-in-Copilot policy or the MCP Registry URL policy.
- `/model` or `--model` selects the model. Some models offer a 1 million token context window and configurable reasoning levels, which increase AI credit use.
- You can point CLI at your own OpenAI-compatible, Azure OpenAI, or Anthropic endpoint, including local Ollama, with `COPILOT_PROVIDER_*` environment variables. The model must support tool calling and streaming.
- ACP (Agent Client Protocol) lets third-party tools host Copilot CLI as an agent.
- You can start a CLI task in the terminal and continue the same session on GitHub.com or GitHub Mobile. Source: https://docs.github.com/en/copilot/get-started/where-to-use-github-copilot

### GitHub Copilot app

Primary source: https://docs.github.com/en/copilot/concepts/agents/github-copilot-app

- The GitHub Copilot app is a desktop application for agent-driven development. It is built on Copilot CLI and connects to GitHub repositories, branches, issues, pull requests, and CI.
- It is available on all Copilot plans. For Business and Enterprise the GitHub Copilot app policy must stay enabled. That policy is on by default and is separate from the Copilot CLI policy.
- Supported operating systems are macOS, Linux, and Windows.
- You can run multiple isolated agent sessions at once, each with its own git worktree and branch, locally or in a cloud sandbox.
- Session modes are Interactive, Plan, and Autopilot. You select a model and reasoning effort per session, including BYOK models.
- From the app you can browse issues, start sessions, create and close pull requests, review pull requests, view CI checks, and search repositories.
- Customizations include global instructions, MCP servers, and agent skills. Automations save recurring tasks on a schedule or on demand. Chats are conversations without a dedicated branch.
- `/chronicle` reports insights from previous sessions. Canvases are custom agent-driven artifacts and interfaces for collaboration.
- For Business and Enterprise, the app respects content exclusion. The app may still generate code that matches public code even when the public-code policy is set to Block.

### Copilot code review

Primary source: https://docs.github.com/en/copilot/concepts/agents/code-review

- Copilot code review reviews pull request code in any language, identifies issues, and suggests fixes you can apply in a few clicks.
- It is supported on GitHub.com, GitHub CLI, GitHub Mobile, VS Code, Visual Studio, Xcode, JetBrains IDEs, and Azure DevOps (public preview).
- Organization members without a Copilot license can use review on GitHub.com when an administrator enables AI credits paid usage and the policy that allows unlicensed members to use code review. That path is not available in IDEs.
- Agentic review gathers full-project context and can pass suggestions to Copilot cloud agent (public preview) to open a pull request with fixes. These capabilities use GitHub Actions runners.
- Review effort is Lite (default, faster) or Balanced (higher-reasoning, more AI credits). Admins can set defaults for automatic reviews.
- You can request a review, or configure automatic review for your own pull requests, for a repository, or for an organization. Triggers include opening a pull request, marking a draft ready, reviewing drafts, and reviewing new pushes.
- Copilot approvals are in public preview. When enabled, an approving Copilot review can satisfy a required-approval rule. A new push dismisses the approval.
- Review can use repository agent skills and MCP servers. GitHub and Playwright MCP servers are on by default. A repository setting can disable MCP for review while leaving it on for cloud agent.
- Dependency files, log files, and SVG files are excluded from review.
- Model switching is not supported for code review. Review may use models that are not enabled on the organization’s Chat model settings.
- Each review consumes AI credits. Agentic capabilities also consume Actions minutes on the runner you configure. Usage is attributed to the requester, the pull request author, a cloud-agent co-author, or the organization.
- Copilot Free includes only “Review selection” in VS Code, not full pull request review. Source: https://docs.github.com/en/copilot/get-started/plans

### GitHub Agentic Workflows

Primary source: https://docs.github.com/en/copilot/concepts/agents/about-github-agentic-workflows

- GitHub Agentic Workflows (public preview) are markdown automations compiled to GitHub Actions workflows and executed by a coding agent.
- You define YAML frontmatter (triggers, permissions, safe outputs) and natural-language instructions in the body, then compile to a `.lock.yml` workflow.
- Documented examples include issue triage, CI investigation, status reports, documentation updates, and test coverage.
- Supported engines include GitHub Copilot (default; requires a Copilot plan), Anthropic Claude, OpenAI Codex, and Google Gemini.
- Agents run in firewalled Actions environments with read-only tokens by default. Writes go through declared `safe-outputs` and threat detection.
- Cost is Actions minutes plus inference. Copilot inference maps to AI credits (`1 AIC = $0.01 USD`). `max-ai-credits` caps a run; the default cap is 1,000 AIC.
- Organization-owned workflows can bill Copilot through `GITHUB_TOKEN` when an administrator enables Copilot CLI and organization-billed Copilot CLI, and the workflow grants `copilot-requests: write`.

### Copilot Memory

Primary source: https://docs.github.com/en/copilot/concepts/agents/copilot-memory

- Copilot Memory is in public preview. It stores repository-level facts and user-level preferences that Copilot deduces from activity.
- It is used by Copilot cloud agent, Copilot code review, Copilot CLI, and agentic autofix. Facts learned in one feature can be used in another.
- CLI applies repository facts plus the initiating user’s preferences. Code review uses repository facts only.
- Repository facts are stored with citations and re-validated against the current branch before use. Only users with write access and Memory enabled create them. Repository owners can delete them.
- User-level preferences stay tied to that user. On Business and Enterprise, administrators can export or delete them. Ownership follows the billing entity.
- Unused memories are deleted after 28 days unless validated and used again.
- Memory is enabled per user. It is on by default on individual plans. On organization- and enterprise-managed plans an administrator must enable the policy first; users can opt out.

### Custom agents

Primary source: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-custom-agents

- Custom agents are specialized Copilot agents defined as Markdown agent profiles with YAML frontmatter for name, description, prompt, tools, and optional MCP servers.
- You can store profiles in a repository at `.github/agents/`, in an organization’s `.github` or `.github-private` repository at `/agents/`, or enterprise-wide in a designated `.github-private` repository.
- Once created, custom agents are available to Copilot cloud agent on GitHub.com, cloud agent in Visual Studio Code, JetBrains IDEs, Eclipse, and Xcode, the GitHub Copilot app, and Copilot CLI.
- Custom agents are in public preview for JetBrains IDEs, Eclipse, and Xcode.
- Copilot CLI also includes built-in agents the main agent can run as subagents, including Explore, Task, general-purpose, code-review, and a research agent invoked with `/research`. Source: https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli

### Agent skills, hooks, and plugins

Primary source: https://docs.github.com/en/copilot/concepts/agents/about-agent-skills

- Agent skills are folders of instructions, scripts, and resources Copilot loads when relevant. They work with cloud agent, code review, Copilot CLI, the Copilot app, and agent mode in Visual Studio Code and JetBrains IDEs.
- Project skills live in `.github/skills`, `.claude/skills`, or `.agents/skills`. Personal skills live in `~/.copilot/skills` or `~/.agents/skills`. You can install skills with `gh skill`.
- Hooks run shell commands at `sessionStart`, `sessionEnd`, `userPromptSubmitted`, `preToolUse`, `postToolUse`, `agentStop`, `subagentStop`, and `errorOccurred`. `preToolUse` can approve or deny tool use. Source: https://docs.github.com/en/copilot/concepts/agents/hooks
- Hooks apply to Copilot cloud agent and Copilot CLI. Repository hooks are `.github/hooks/*.json`. CLI also supports `~/.copilot/hooks/*.json`. Source: https://docs.github.com/en/copilot/concepts/agents/hooks
- Plugins package custom agents, skills, hooks, MCP configs, and LSP configs for Copilot CLI, cloud agent, and the Copilot app. Source: https://docs.github.com/en/copilot/concepts/agents/about-plugins
- Two plugin formats exist: Agent Plugins 1.0 (portable skills and MCP) and legacy Copilot plugins (configurable paths). Install from a marketplace, repository, or local path. Default marketplaces include copilot-plugins and awesome-copilot. Source: https://docs.github.com/en/copilot/concepts/agents/about-plugins
- Enterprise administrators can define plugin standards and auto-installed plugins. Source: https://docs.github.com/en/copilot/concepts/agents/about-plugins

### Model Context Protocol

Primary source: https://docs.github.com/en/copilot/concepts/context/mcp

- MCP connects Copilot to external data sources and tools in IDEs, Copilot CLI, the Copilot app, and agents on GitHub.com.
- For Copilot Business and Copilot Enterprise, the “MCP servers in Copilot” policy is disabled by default. Individual plans are not governed by that policy.
- Local MCP is broadly supported in VS Code, JetBrains, Xcode, and other clients. Remote MCP with OAuth or a PAT is documented for VS Code, Visual Studio, JetBrains, Xcode, Eclipse, Cursor, and Windsurf.
- Copilot CLI includes the GitHub MCP server. The Copilot app uses repository or CLI MCP config and can add more servers in settings.
- Repository-level MCP on GitHub.com applies to cloud agent and code review. GitHub MCP and Playwright MCP are configured by default.
- The GitHub MCP server can run remotely in VS Code Chat or locally. Toolsets enable or disable groups of GitHub API tools, resources, and prompts.
- For public repositories, and private repositories with GitHub Advanced Security, GitHub MCP interactions are covered by push protection against secrets in AI-generated responses.
- The GitHub MCP Registry (public preview) lists partner and community servers.
- Agent finder is a discovery service for MCP servers, tools, agents, and skills at runtime. It implements the Agentic Resource Discovery (ARD) specification.

### Copilot Spaces

Primary source: https://docs.github.com/en/copilot/concepts/context/spaces

- Copilot Spaces collect repositories, code, pull requests, issues, free-text notes, images, and file uploads so Chat answers are grounded in that context.
- Anyone with a Copilot license, including Copilot Free, can create and use Spaces.
- Organization-owned spaces can be shared with admin, editor, or viewer access, or hidden. Individual spaces can be public (view-only), shared with specific users, or private. Viewers only see sources they can access.
- You use Spaces in Copilot Chat on GitHub, and in IDE agent mode through GitHub MCP tools `get_copilot_space` and `list_copilot_spaces`.
- GitHub-based sources in a space update as the files change. Questions in a space consume Chat AI credits (or the Free chat allowance).

### Models

Primary source: https://docs.github.com/en/copilot/get-started/plans

- Copilot Free and Copilot Student use auto model selection only.
- Paid individual and organization plans list models from Anthropic (including Claude Haiku 4.5, Sonnet 4.6 and 5, Opus 4.7–5.5, Opus 4.8 fast mode preview, and Claude Fable 5 / 5.1), Google Gemini 3.5–3.8 Flash, OpenAI GPT-5 mini through GPT-6 variants, xAI Grok 4.5–4.7, Kimi K2.7 Code and Kimi K3, and MAI-Code-1.1-Flash.
- GPT-5.4 nano is available only in the Codex Visual Studio Code extension on Copilot Pro+, not in Copilot Chat.
- Claude Fable 5 and 5.1 retain prompts and outputs for Anthropic safety classifiers unless the enterprise is approved for zero data retention through the end of 2026. Other Claude models continue under ZDR. An admin must still enable each Fable model.
- You can change the Chat model, and, in supported IDEs, the inline-suggestion model. Auto model selection is documented as a Copilot feature that picks a model per task. Source: https://docs.github.com/en/copilot/concepts/models
- Bring your own key is documented for Copilot so you can use an existing LLM provider. Source: https://docs.github.com/en/copilot/concepts/models
- Paid individual plans get a 10% discount on model costs when using auto model selection in Chat, CLI, the Copilot app, or cloud agent. Source: https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-individuals

### Third-party coding agents

Primary source: https://docs.github.com/en/copilot/concepts/agents/about-third-party-coding-agents

- Third-party coding agents are in public preview. You can assign an issue or a prompt to a partner agent, which opens a pull request and can iterate from review comments.
- Supported agents on GitHub are Anthropic Claude and OpenAI Codex. Enabling them installs a corresponding GitHub App (`anthropic code agent` or `openai code agent`).
- You start tasks from the Agents tab, issue assignment, `@AGENT_NAME` on a pull request, GitHub Mobile, or Visual Studio Code.
- Individual and organization or enterprise policies must allow the agents. Those policies do not apply to local agents in Visual Studio Code.
- Codex models include Auto, GPT-5.3-Codex, GPT-5.4, and GPT-5.4 nano. Claude models include Auto, Claude Opus 4.7, and Claude Sonnet 4.6. Auto here does not use Copilot auto model selection.
- GitHub scans generated code with CodeQL, secret scanning, and Advisory Database checks on new dependencies. GitHub Advanced Security is not required for this validation.
- Sessions consume Actions minutes and AI credits.
- Agent apps, as listed in the Copilot docs index, let you use partner-built agents in GitHub workflows on a Copilot subscription. Source: https://docs.github.com/en/copilot

### Integrations

Primary source: https://docs.github.com/en/copilot/concepts/tools/about-copilot-integrations

- Copilot cloud agent integrations are documented for Microsoft Teams, Slack, Linear, Azure Boards, and Jira.
- The agent captures the thread or issue for context and stores that context in the artifacts it creates.
- Deep research and planning before a pull request are on GitHub.com and in public preview for Teams and Slack. Linear, Azure Boards, and Jira open a pull request directly. Source: https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent

### Administration and policies

Primary source: https://docs.github.com/en/copilot/concepts/policies

- Enterprise and organization policies live under AI controls and control which Copilot features, agents, and models users can access.
- Enterprise owners can enable, disable, or let organizations decide most policies. For cloud agent, the enterprise can select exactly which organizations get access.
- Policies generally apply to users who receive a Business or Enterprise license from that enterprise or organization. A few policies apply to everyone, such as blocking cloud agent on the enterprise’s repositories.
- Policies can apply wherever users authenticate, including IDEs, github.com, and Copilot CLI. Not every policy applies to every surface.
- The Copilot app and Copilot CLI have separate client policies.
- Two policies control whether unconfigured GA features and models default to enabled or disabled. The models default policy is already active; the feature default policy is documented as becoming active soon.
- When a user has licenses from multiple organizations in one enterprise, the least restrictive policy usually applies, with exceptions. Across enterprises, the most restrictive policy almost always applies.
- Assigning a Business or Enterprise seat cancels the user’s individual Copilot plan.
- Enterprise owners set policies for agents, Copilot administration/privacy/models/billing, features and clients, and MCP. Source: https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-enterprise-policies
- Suggestions matching public code default to Blocked for Copilot Business. Source: https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-enterprise-policies
- Organization and enterprise owners assign seats, review usage and audit logs, and exclude files Copilot should not see. Source: https://docs.github.com/en/copilot/get-started/what-is-github-copilot

### Security and content controls

Primary source: https://docs.github.com/en/copilot/concepts/content-exclusion

- Content exclusion stops inline suggestions in excluded files, stops those files from informing other suggestions or Chat, and skips them in Copilot code review. Repository, organization, and enterprise admins can configure it on Business and Enterprise.
- Content exclusion is in public preview on the GitHub website and GitHub Mobile. The docs say it is not currently supported in Edit and Agent modes of Copilot Chat in Visual Studio Code and other editors.
- Copilot may still see semantic information the IDE provides indirectly, such as types and hover definitions. Exclusions do not apply to symlinks or repositories on remote filesystems.
- After exclusion is configured, the client sends the repository URL to GitHub so the server can return the policy. The docs say those URLs are not logged.
- Copilot checks suggestions against an index of public GitHub.com repositories. Matches are discarded or shown with a code reference, depending on the public-code policy. Private and non-GitHub code is not in that index. Source: https://docs.github.com/en/copilot/concepts/completions/code-referencing
- Code referencing applies when you accept an inline suggestion or when Chat (and cloud agent session logs) include matching public code. The public index refreshes every few months. Source: https://docs.github.com/en/copilot/concepts/completions/code-referencing
- Local and cloud sandboxes isolate tool, filesystem, and network access for CLI and app sessions. Cloud sandboxing is in public preview. Source: https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli

### Plans and billing

Primary source: https://docs.github.com/en/copilot/get-started/plans

- Individual plans: Copilot Free, Copilot Student, Copilot Pro ($10 USD/month), Copilot Pro+ ($39 USD/month), Copilot Max ($100 USD/month). All plans include Copilot CLI and the Copilot app.
- Organization and enterprise plans: Copilot Business ($19 USD per granted seat per month) and Copilot Enterprise ($39 USD per granted seat per month, for GitHub Enterprise Cloud).
- Paid individual monthly AI credits: Pro 1,000 base + 500 flex (1,500 total); Pro+ 3,900 + 3,100 (7,000); Max 10,000 + 10,000 (20,000). Free and Student have a documented allowance without those totals.
- Business includes 1,900 AI credits per user per month; Enterprise includes 3,900. Credits pool at the billing entity. Unused credits do not roll over. The pool resets at 00:00:00 UTC on the first day of each calendar month. Source: https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises
- 1 AI credit equals $0.01 USD. Chat, CLI, cloud agent, Spaces, Spark, and third-party coding agents consume credits. Completions and next edit suggestions do not, and stay unlimited on paid plans. Source: https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises
- Additional usage is on by default for organizations and enterprises. Admins can disable paid usage in AI Controls. User-level, cost-center, organization, and enterprise budgets cap draw from the pool and metered overage. Source: https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises
- Individuals who exhaust included credits can upgrade (paying only the plan difference), set an additional-usage budget, or wait for the monthly reset. A personal plan is canceled with a prorated refund if the user later receives a Business or Enterprise seat. Source: https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-individuals
- Copilot is not currently available for GitHub Enterprise Server. Source: https://docs.github.com/en/copilot/get-started/plans

### Usage metrics

Primary source: https://docs.github.com/en/copilot/concepts/copilot-usage-metrics

- Copilot usage metrics report adoption and use across an organization, including engagement, activity, code generation, and pull request lifecycle trends.
- Enterprise administrators and organization owners can use usage metrics APIs for cloud-agent pull request outcomes: pull requests created and merged, cloud-agent pull requests merged, and median time to merge. Source: https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent

### GitHub Copilot SDK

Primary source: https://docs.github.com/en/copilot/get-started/where-to-use-github-copilot

- The GitHub Copilot SDK uses the same platform primitives as first-party Copilot surfaces so you can build applications and internal workflows that call Copilot.
- The docs describe a tutorial that uses the SDK to build a command-line assistant with streaming responses and custom tools. Source: https://docs.github.com/en/copilot

## Sources

- https://docs.github.com/en/copilot
- https://docs.github.com/en/copilot/get-started/what-is-github-copilot
- https://docs.github.com/en/copilot/get-started/where-to-use-github-copilot
- https://docs.github.com/en/copilot/get-started/plans
- https://docs.github.com/en/copilot/concepts/completions/code-suggestions
- https://docs.github.com/en/copilot/concepts/completions/code-referencing
- https://docs.github.com/en/copilot/concepts/about-github-copilot-chat
- https://docs.github.com/en/copilot/how-tos/copilot-on-github/chat-with-copilot/chat-in-github
- https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-ide
- https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent
- https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/start-copilot-sessions
- https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations
- https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-custom-agents
- https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli
- https://docs.github.com/en/copilot/concepts/agents/github-copilot-app
- https://docs.github.com/en/copilot/concepts/agents/code-review
- https://docs.github.com/en/copilot/concepts/agents/about-github-agentic-workflows
- https://docs.github.com/en/copilot/concepts/agents/copilot-memory
- https://docs.github.com/en/copilot/concepts/agents/about-agent-skills
- https://docs.github.com/en/copilot/concepts/agents/hooks
- https://docs.github.com/en/copilot/concepts/agents/about-plugins
- https://docs.github.com/en/copilot/concepts/agents/about-third-party-coding-agents
- https://docs.github.com/en/copilot/concepts/context/mcp
- https://docs.github.com/en/copilot/concepts/context/spaces
- https://docs.github.com/en/copilot/concepts/models
- https://docs.github.com/en/copilot/concepts/tools/about-copilot-integrations
- https://docs.github.com/en/copilot/concepts/policies
- https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-enterprise-policies
- https://docs.github.com/en/copilot/concepts/content-exclusion
- https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises
- https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-individuals
- https://docs.github.com/en/copilot/concepts/copilot-usage-metrics
- https://docs.github.com/en/copilot/reference/copilot-feature-matrix
