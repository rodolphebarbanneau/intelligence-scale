---
name: Devin
slug: devin
url: https://devin.ai/
docs: https://docs.devin.ai/
kind: product
reviewed: 2026-09-28
---

# Devin

## Product

Devin is Cognition's AI software engineer product. The docs describe it as an AI software engineer that can write, run, and test code. Cognition names itself an applied AI lab building end-to-end software agents. Sign up is at [app.devin.ai](https://app.devin.ai). Official documentation lives at [docs.devin.ai](https://docs.devin.ai/). Source: https://docs.devin.ai/get-started/devin-intro

The product is aimed at engineering teams. Documented work includes Linear and Jira tickets, new features, bug reproduction and fixes, migrations and refactors, pull-request review, codebase questions, unit tests, documentation, integrations, and internal tools. The intro page's rule of thumb is that a task a person could do in about three hours is the kind of task Devin can most likely do. The docs also say Devin may not handle extremely difficult tasks, and that documentation may be out of date. Source: https://docs.devin.ai/get-started/devin-intro

Devin Cloud sessions run in virtual machines. The default platform is Linux. Organizations can also run sessions on macOS VMs and, on a limited basis, Windows VMs. Each organization keeps one active environment snapshot that sessions boot from. People start and watch work from the web app, Slack, Microsoft Teams, the Devin CLI, Devin Desktop, or the Devin API. Devin Outposts run session execution on customer-managed machines while inference stays in Cognition's cloud.

Self-serve plans are Free, Pro, Max, and Teams, signed up at app.devin.ai. Enterprise is a separate contract billed in Agent Compute Units (ACUs). Federal deployments of the Cognition platform run on AWS GovCloud with a dedicated portal.

## Features

### Devin Cloud sessions

Primary source: https://docs.devin.ai/get-started/first-run

- A new session offers Ask mode and Agent mode. Ask explores the codebase and plans work without changing code. Agent writes code, runs commands, browses the web, and completes tasks end to end.
- Agent sessions select one or more repositories already on Devin's machine and an agent configuration. Available agents include Devin (default), Fast Mode, and Data Analyst (DANA).
- The agent can be switched mid-session from the session page. In Slack, a message that starts with `!ultra`, `!fast`, `!lite`, `!fusion`, `!swe`, or `!normal` switches mode.
- `@` mentions attach context: repositories, files, knowledge macros, playbooks, skills, secrets, and prior sessions.
- Sessions handle branching, pull-request creation, and CI monitoring as part of the built-in workflow. Source: https://docs.devin.ai/get-started/first-run
- Devin can launch managed child sessions in parallel, each on its own isolated VM. The coordinator scopes work, messages children, tracks ACU use, and can sleep or terminate children. Source: https://docs.devin.ai/work-with-devin/advanced-capabilities
- Auto-approve child sessions is on by default. It can be turned off under Settings > Preferences. Source: https://docs.devin.ai/work-with-devin/advanced-capabilities
- Dynamic Workflows run a deterministic Python script that fans out agents, pipes structured results between stages, and resumes a run from recorded results. Enterprise accounts keep the feature off until an admin enables Dynamic workflows. Source: https://docs.devin.ai/work-with-devin/dynamic-workflows
- Voice mode starts a call from the home page in Agent mode or from an existing session. Mute, hold Space to talk while muted, silence Devin, and end call are available. Source: https://docs.devin.ai/work-with-devin/voice-mode
- Session Insights analyzes a completed session: ACU usage, user-message count, XS–XL size, task category, issue timeline, an improved prompt, and knowledge usage. Full analysis is automatic for L and XL sessions and optional for smaller ones. Source: https://docs.devin.ai/product-guides/session-insights
- For standalone apps Devin builds from scratch, it can host static frontends on `devinapps.com` and FastAPI backends on Fly.io after an explicit approve/deny prompt. Native deployments are off for enterprise organizations and for sessions in secure mode or under a network policy. Source: https://docs.devin.ai/product-guides/deployment-capabilities

### Session workspace

Primary source: https://docs.devin.ai/work-with-devin/devin-session-tools

- The Progress tab logs shell commands, code edits, and browser activity in one view.
- Side chats answer questions about a session without interrupting the main run. They are read-only: Devin can search and read code but cannot edit files or run commands.
- The Shell shows command history, output previews, copy, and time navigation. Taking over the machine makes the IDE terminal writable.
- The IDE is an embedded VS Code environment. A person can watch edits, stop the session, and take over with Cmd/Ctrl+K, Cmd/Ctrl+I, and Tab autocomplete.
- The Interactive Browser (labeled Computer when Computer Use is on) lets a person watch and take over browsing, including CAPTCHAs, MFA, and OAuth. Cookies persist for the session and can be saved into the organization blueprint as a browser profile. Source: https://docs.devin.ai/work-with-devin/devin-session-tools
- Computer Use gives Devin a 1024×768 graphical desktop with mouse, keyboard, screenshots, and recordings on Linux, Windows, and macOS sessions. Organization admins enable it under Settings > Devin. Source: https://docs.devin.ai/work-with-devin/computer-use
- After Devin opens a pull request, a Test the app control starts an end-to-end test with a video recording. Devin can also test on request or when the task needs GUI interaction. Source: https://docs.devin.ai/work-with-devin/computer-use
- Devin's Chrome exposes a Chrome DevTools Protocol endpoint on port 29229 so Playwright scripts can attach and persist cookies and `localStorage`. Source: https://docs.devin.ai/work-with-devin/computer-use
- On GitHub.com only, Devin can split large work into a stacked PR series (2–100 PRs) that lands bottom-up through GitHub's atomic stack merge. Source: https://docs.devin.ai/work-with-devin/stacked-prs

### Ask Devin

Primary source: https://docs.devin.ai/work-with-devin/ask-devin

- Ask Devin answers codebase questions with cited code search and plans tasks before implementation.
- After a repository is connected, Devin indexes it so Ask Devin and DeepWiki can use it. Repositories are added for indexing from Settings > DeepWiki.
- A session started from Ask Devin inherits that conversation as context. Session status stays visible in the Ask Devin thread.
- Ask mode can be opened from the main page or from a DeepWiki page, which scopes the question to that repository.

### DeepWiki

Primary source: https://docs.devin.ai/work-with-devin/deepwiki

- DeepWiki auto-generates repository wikis with architecture diagrams, source links, and summaries. Ask Devin uses the wiki as context.
- A public DeepWiki and Ask Devin for public GitHub repositories is available at [deepwiki.com](https://deepwiki.com). The full Ask Devin planning and session-creation flow is in the Devin app.
- Wiki generation effort is Low (default, free), Medium (~5–10 ACUs), or High (~20–40 ACUs). Enterprise organizations always run at low effort.
- A `.devin/wiki.json` file in the repo root steers generation with required `repo_notes` and `pages`. Limits are 30 pages (80 for enterprise) and 100 notes.

### Devin Review

Primary source: https://docs.devin.ai/work-with-devin/devin-review

- Devin Review is a code-review surface in the web app at app.devin.ai/review. It supports GitHub (including Enterprise Server and Enterprise Cloud), GitLab (including Self-Managed), and connected Azure DevOps repositories.
- Features include grouped smart diffs, copy/move detection, a bug catcher with confidence labels, security scanning with CWE classification, codebase-aware chat, comments synced to the host, and (on GitHub) merge, close, draft, ready-for-review, and auto-merge actions.
- Chat can propose code edits and apply them as a commit on GitHub and GitLab. Azure DevOps supports diffs, analysis, comments, and auto-review but not chat edits, merge, or auto-merge.
- Public GitHub PRs can be reviewed at [devinreview.com](https://devinreview.com) by replacing `github.com` in the URL, without a Devin account. Source: https://docs.devin.ai/admin/billing/self-serve
- Auto-review trigger modes are Auto review, On PR creation, and Manual. Draft PRs are skipped until marked ready.
- Commenting `/devin review` on a connected GitHub PR starts a review. Source: https://docs.devin.ai/work-with-devin/devin-review
- When Devin Review Auto-Fix is enabled, Devin responds to review comments, flagged bugs, and CI failures on the PR. Source: https://docs.devin.ai/essential-guidelines/when-to-use-devin
- Enterprise admins control Review permission tiers, ACU consumption dashboards, and a per-PR auto-review spend limit. Source: https://docs.devin.ai/work-with-devin/devin-review

### Devin CLI

Primary source: https://docs.devin.ai/cli/index

- Devin CLI is a local coding agent for the terminal on macOS, Linux, WSL, and Windows. Installers include `curl -fsSL https://cli.devin.ai/install.sh | bash`, Homebrew (`brew install --cask devin-cli`), a Windows PowerShell setup script, and a bundled install from Devin Desktop on Legacy Windsurf Enterprise and Devin Enterprise plans.
- `devin` starts an interactive REPL. `devin -- prompt` preloads a prompt. `devin -p` runs a single turn to stdout. Source: https://docs.devin.ai/cli/essential-commands
- Permission modes are Normal, Accept Edits, Smart (rolling out gradually), Bypass, and Autonomous (only with `--sandbox`). Agent modes include Normal, Plan (`/plan`), and Ask (`/ask`). Source: https://docs.devin.ai/cli/essential-commands
- Sessions resume with `-c` / `--continue` or `-r` / `--resume`. `/cloud`, `/handoff`, `/open`, and `/archive` move work between local and cloud. `devin ssh` opens a shell on a cloud session VM. Source: https://docs.devin.ai/cli/essential-commands
- `/handoff` packages conversation context and the current git branch into a cloud Devin session. An open-source Devin Handoff plugin does the same from other coding agents using a Devin API key. Source: https://docs.devin.ai/work-with-devin/devin-handoff
- Models include Adaptive routing, Fusion (a frontier lead plus a cost-efficient sidekick), Cognition SWE models, and current models from Anthropic, OpenAI, Google, and others. Short names such as `opus`, `sonnet`, and `swe` resolve to the latest in that family. Source: https://docs.devin.ai/cli/models
- The CLI does not yet support Knowledge, Playbooks, or Secrets from the Devin account. Source: https://docs.devin.ai/cli/index

### Devin Desktop

Primary source: https://docs.devin.ai/desktop/getting-started

- Devin Desktop is an IDE for Mac (OS X Yosemite+), Windows 10+, and Linux (glibc ≥ 2.28). Linux packages are `devin-desktop` via apt or yum; repository URLs still use pre-rebrand `windsurf` names.
- Onboarding can import VS Code or Cursor settings and install a `devin-desktop` terminal command. Login uses a Devin account or a Devin API key.
- Devin Local is the primary local agent and shares the Devin CLI harness: subagents, sandboxing, plan mode, worktrees, and permissions. Source: https://docs.devin.ai/_llms/en/desktop.md
- Cascade remains documented as Devin Desktop's agentic assistant, with Code/Chat modes, Arena Mode, memories and rules, skills, AGENTS.md, workflows, worktrees, MCP, and hooks. Source: https://docs.devin.ai/_llms/en/desktop.md
- Editor features include Tab completions, Command (Cmd/Ctrl+I), an enhanced terminal, local previews, AI commit messages, DeepWiki hover explanations, and Codemaps. Source: https://docs.devin.ai/_llms/en/desktop.md
- Agent Command Center is a Kanban view of local and cloud agents. Spaces group sessions, PRs, files, and context. Third-party agents can run via ACP. Source: https://docs.devin.ai/_llms/en/desktop.md
- Devin Desktop Next is a prerelease channel. Custom app icons are beta and Mac-only for paying users. Source: https://docs.devin.ai/desktop/getting-started
- Windsurf Plugins remain documented for JetBrains, VS Code, Visual Studio, Vim, NeoVim, and other IDEs. Source: https://docs.devin.ai/_llms/en/desktop.md

### Environments

Primary source: https://docs.devin.ai/onboard-devin/environment

- Devin's environment is a VM snapshot with cloned repos, tools, dependencies, environment variables, and secrets. Each organization has one active snapshot. Session changes do not write back to the snapshot.
- Setup can be done by asking Devin to generate a blueprint, or by editing declarative YAML. Builds produce the snapshot.
- Blueprints support GitHub Actions-style steps, env vars, secrets, file attachments, and a `runs-on` platform of `linux`/`default`, `macos`, or `windows`. Source: https://docs.devin.ai/onboard-devin/environment/macos-support
- macOS sessions include Xcode, iOS Simulator, Homebrew, and Chrome. They can build Apple-platform apps and upload to TestFlight when App Store Connect secrets are configured. Dedicated SaaS customers ask their account team to enable macOS VMs. Source: https://docs.devin.ai/onboard-devin/environment/macos-support
- Windows sessions are available on a limited basis. Default shell is Git Bash; blueprint steps can use PowerShell. Package installs use Chocolatey. Windows sessions consume about 9% more usage than equivalent Linux sessions. Source: https://docs.devin.ai/onboard-devin/environment/windows-support
- Android emulator support installs the Android SDK and an AVD in the Linux snapshot. Devin uses `adb` and Computer Use against the emulator window, including Espresso/UI Automator runs and video recordings. Source: https://docs.devin.ai/onboard-devin/environment/android-emulation
- OIDC workload identity federation issues short-lived session tokens for AWS, GCP, Vault, JFrog, Databricks, and custom audiences, without storing static cloud keys. Source: https://docs.devin.ai/product-guides/oidc
- AGENTS.md files inject repository instructions, with a 16 KiB automatic injection limit. Source: https://docs.devin.ai/onboard-devin/agents-md

### Devin Outposts

Primary source: https://docs.devin.ai/cloud/outposts/overview

- Outposts run command execution, file edits, and repository access on customer machines. Devin's agent loop stays in Cognition's cloud.
- A worker is `devin worker start --outpost=<name>`. Workers need outbound HTTPS only. N workers serve N concurrent sessions.
- Sessions pick an outpost in Configuration → Virtual environment, or in Slack with `!outpost`.
- An orchestrator can poll the queue, provision a VM or container per session, and tear it down. Cognition publishes an open-source Kubernetes operator (`devin-outpost-k8s`).
- Documented partner integrations include Namespace, Modal, OpenShell, Brev, Daytona, E2B, and Cloudflare.
- Outposts are available on Pro, Max, and Teams. On Dedicated Tenant they are off by default.
- Network allowlists from security profiles are published to the orchestrator as `spec.network_policy`; the operator must enforce them on customer machines. Source: https://docs.devin.ai/product-guides/security-profiles

### Skills, Playbooks, and Knowledge

Primary source: https://docs.devin.ai/product-guides/skills

- Skills are `SKILL.md` files that follow the Agent Skills standard. Devin discovers them from `.agents/skills/`, `.devin/skills/`, `.github/skills/`, `.claude/skills/`, `.cognition/skills/`, and `.windsurf/skills/`.
- Devin indexes skills across connected repos and re-scans cloned repos mid-session. Invoke with `@skills:name`, or let Devin auto-invoke unless `triggers: ["user"]`.
- After testing an app, Devin can suggest a skill and open a PR to commit it.
- Playbooks are reusable prompt templates in the web app, with Procedure, Specifications, Advice, Forbidden Actions, and Required from User sections. Macros such as `!data-tutorial` attach a playbook. Organization and Enterprise playbooks are supported. Version history can revert edits. Source: https://docs.devin.ai/product-guides/creating-playbooks
- Knowledge is deprecated and is being migrated into Skills in plugins. Existing notes remain usable during the rollout. New instructions should be Skills. Source: https://docs.devin.ai/product-guides/knowledge
- Knowledge items (until removed) have triggers, macros, folders, repo pinning, and organization or enterprise scope. Source: https://docs.devin.ai/product-guides/knowledge

### Plugins and MCP

Primary source: https://docs.devin.ai/product-guides/plugins

- A plugin bundles skills and optionally rules, hooks, MCP servers, and subagents. Install scopes are Personal, Organization, and Enterprise.
- The Customize page has Plugins, Skills, MCPs, Hooks, and Rules tabs. Plugins install from the official marketplace, a git repo, a zip upload, an in-app editor, `devin plugins install`, or a Devin session card.
- Cloud sessions, CLI, and Desktop read the same managed manifests so an install follows the user across surfaces.
- MCP transports are STDIO, SSE, and HTTP. Official plugins usually ship one MCP plus skills. Custom servers need the Manage MCP Servers permission. Source: https://docs.devin.ai/work-with-devin/mcp
- OAuth MCP access can be Organization-shared or Personal per member. Source: https://docs.devin.ai/work-with-devin/mcp
- The built-in Devin MCP exposes session, playbook, knowledge, schedule, integration, and repository-doc tools to Devin sessions and external MCP clients. Source: https://docs.devin.ai/work-with-devin/advanced-capabilities

### Automations

Primary source: https://docs.devin.ai/product-guides/automations

- An automation has a trigger, optional conditions, and an action: start session, message session, Triage Devin, or email notification.
- Trigger sources include Slack, GitHub, GitLab, Linear, Jira, Pylon, PagerDuty, Schedule (cron/RRULE or run-once), and authenticated webhooks (200 KB payload cap).
- A single automation can attach multiple triggers (OR). Automations can also be generated by Devin, created from templates, or managed with a Terraform provider.
- Built-in templates cover Slack/Pylon triage, CI auto-fix, scheduled Sentry/Datadog sweeps, dependency and secret scans, and Linear/Asana/Notion reports.
- Safeguards include per-session ACU limits, invocation rate limits (default 50/hour; 150/hour for Slack triage), and an optional network policy intersected with the session's security profile.
- Auto-triage is a persistent Devin that monitors a Slack channel and spawns child sessions for items that need investigation.

### Security Swarm and Code Scans

Primary source: https://docs.devin.ai/work-with-devin/security-swarm

- Security Swarm scans repositories for vulnerabilities (RCE, injection, SSRF, auth bypass, and others), builds a threat model, validates findings, and can assign Devin to open a fix PR.
- Scans can be interactive (review the threat model first) or unattended. Scan profiles capture scope, threat model, investigation and triage guidance, sandbox validation, and remediation constraints.
- Findings carry severity, exploitability, confidence, evidence, sandbox validation, and linked PRs. Actions are Assign to Devin, Feedback, Adjust severity, and status Open/Reviewed/Dismissed.
- Code Scans cover non-security types: Performance, Database queries, Test coverage, Dead code, Code quality, Cleanup, Telemetry, Accessibility, Compliance, Migration docs, and Custom. Start with `/scan`. Source: https://docs.devin.ai/work-with-devin/code-scans
- After a scan completes, Scan new commits runs an incremental pass. Automations can create a new scan or scan new commits on a schedule or event. Source: https://docs.devin.ai/work-with-devin/code-scans

### Data Analyst

Primary source: https://docs.devin.ai/work-with-devin/data-analyst

- DANA is a specialized agent for SQL queries, analysis, and seaborn charts. It is not available on free or trial plans.
- Start it from the agent picker (Mode → Data), Slack `/dana`, or `@Devin !dana`. `!discovery` after `!dana` catalogs reachable MCP databases.
- It requires at least one data-source MCP (for example PostgreSQL, Snowflake, BigQuery, Redshift, Datadog, Metabase, Grafana, Sentry).
- Responses include tables, charts, the SQL used, and optional Metabase links. Schema notes can persist in Knowledge.

### Integrations

Primary source: https://docs.devin.ai/integrations/overview

- Native source-control integrations: GitHub, GitLab (15.0+), Bitbucket Cloud or Data Center, and Azure DevOps (OAuth or service principal). Comment `/devin` on a GitHub PR to start a session.
- Slack: `@Devin` starts a session in-thread. Keywords include `!ask`, `!deep`, mute/unmute, sleep, archive, EXIT, mode bangs, `!windows`, `!mac`, `!outpost`, `!dana`, and playbook macros. Slash commands are `/ask-devin` and `/dana`. Code channels and bidirectional thread sync are documented. Source: https://docs.devin.ai/integrations/slack
- Microsoft Teams: `@Devin AI` in a channel, group chat, or 1:1 DM starts a session. Private channels are not supported. Mode keywords and `!ask` / `!deep` work as in Slack. Source: https://docs.devin.ai/integrations/microsoft-teams
- Microsoft 365 marketplace plugins (separate from the Teams bot) cover OneDrive & SharePoint, Mail & Contacts, Calendar, To Do, Teams, and Directory, using the signed-in account's Graph permissions. Source: https://docs.devin.ai/integrations/microsoft-teams
- Project and incident tools: Linear, Jira, PagerDuty, and Pylon (via automations). Databricks connects with a service principal and Unity Catalog grants.
- Self-hosted SCM and artifact repositories are a documented connection path. Enterprise source-code setup lists GitHub, GitHub Enterprise, GitLab, Bitbucket, and Azure DevOps. Source: https://docs.devin.ai/enterprise/getting-started/get-started
- GitHub-style pull-request templates, including a custom Devin template filename, control PR descriptions. Source: https://docs.devin.ai/integrations/overview

### Secrets and security profiles

Primary source: https://docs.devin.ai/product-guides/secrets

- Secrets store raw values, site cookies, and TOTP seeds. Scopes are organization, personal, repository (blueprint Secrets tab), and session-only.
- Organization secrets are encrypted at rest. All members can use them; only admins can view or edit them. Personal secrets stay in the creator's sessions.
- Devin injects secrets into the specific browser fields or shell commands that need them, rewriting names into valid environment variables.
- Security profiles bundle network allowlists, MCP allowlists, Devin MCP read-only, git read-only vs full, and GitHub CLI token removal. Bindings cascade from enterprise default → org default → automations default → one automation → one session. Source: https://docs.devin.ai/product-guides/security-profiles
- Recommended profiles can be overridden. Mandatory profiles intersect with lower bindings and cannot be loosened. Child sessions inherit the parent's chain. Source: https://docs.devin.ai/product-guides/security-profiles

### Plans, billing, and membership

Primary source: https://docs.devin.ai/admin/billing/self-serve

- Self-serve plans at app.devin.ai: Free (limited usage, Review, DeepWiki), Pro ($20/month, one user, Slack/Linear/MCP), Max ($200/month, larger weekly quota, no daily cap), Teams ($80/month minimum, up to 200 members).
- Teams full seats are $40/month and include a Pro-equivalent quota plus Devin Desktop. Flex seats are free, draw shared on-demand credits, and do not include Devin Desktop.
- On-demand credits roll over, never expire, and can auto-reload. On Teams they are shared. Automations and Devin Review on Teams draw from that pool, not full-seat quota.
- Enterprise contracts bill ACUs per the order form. Admins set organization ACU limits and per-user usage policies. Limits apply to cloud sessions, Review, Desktop, Windsurf JetBrains, and CLI billed to that org. Source: https://docs.devin.ai/admin/billing/enterprise
- Team and Enterprise membership roles are Member, Admin, and DeepWiki Only. Invites go out from Settings > Membership. Source: https://docs.devin.ai/product-guides/invite-team
- Feedback goes to support@cognition.ai, Slack Connect on Teams, or Help → Contact support in the web app. Source: https://docs.devin.ai/get-started/devin-intro

### Enterprise

Primary source: https://docs.devin.ai/enterprise/getting-started/get-started

- An enterprise contains multiple organizations. Each organization has its own shared Devin machine, repository access, and members.
- Default users are Enterprise Admins, Organization Admins, and Members. Custom roles and RBAC exist at organization and account (enterprise) scope. One role per user per organization, plus one account-level role. Source: https://docs.devin.ai/enterprise/security-access/custom-roles
- SSO supports Okta, Microsoft Entra ID, SAML, and generic OIDC. SCIM 2.0 provisions users and groups. IdP groups can auto-assign roles. Source: https://docs.devin.ai/enterprise/getting-started/get-started
- Deployment models are Enterprise Cloud (multi-tenant) and Customer Dedicated Deployment (single-tenant VPC via AWS PrivateLink or IPSec). Enterprise Assured adds customer-managed AWS KMS keys. Devin's "brain" always runs in Cognition's cloud; the Devbox location depends on the model. Source: https://docs.devin.ai/enterprise/deployment/overview
- MFA VPNs are not compatible with Enterprise Cloud. Dedicated deployments support OpenVPN. User workstations need `*.devinapps.com` on HTTPS/443 for the IDE and desktop viewer. Source: https://docs.devin.ai/enterprise/deployment/overview
- Third-party LLM API keys are not supported. Source: https://docs.devin.ai/enterprise/deployment/overview
- Enterprise security pages state encryption in transit and at rest, SOC 2 Type II since September 2024, and a Trust Center. Cognition does not train on Enterprise customer data or code by default. Source: https://docs.devin.ai/enterprise/security-access/security/enterprise-security
- Account-level custom roles include View Audit Logs and Manage IP Whitelist among other permissions. Source: https://docs.devin.ai/enterprise/security-access/custom-roles
- The Trust Center lists CCPA, SOC 2 Type 2, and ISO/IEC 27001:2022 among published compliance items. Source: https://docs.devin.ai/enterprise/security-access/trust-center
- Paid-plan users can opt out of training on the Data Controls page, which also enables zero data retention with model providers. On Teams, only an administrator can opt out. Source: https://docs.devin.ai/admin/security
- Output produced by Devin is the customer's intellectual property, except that it may not be used to train a competing product. Source: https://docs.devin.ai/admin/security

### Devin API

Primary source: https://docs.devin.ai/api-reference/overview

- The current API is v3. Organization scope is `https://api.devin.ai/v3/organizations/*` (sessions, knowledge, playbooks, secrets). Enterprise scope is `https://api.devin.ai/v3/enterprise/*` (analytics, audit logs, users, billing, infrastructure).
- Authentication uses service users (`cog_` prefix) with RBAC, or a Personal Access Token. `create_as_user_id` attributes a session to a human user and counts toward that user's usage.
- v1 and v2 remain during deprecation and do not receive new features.
- Code Scans and Session Insights expose API start/poll/read endpoints. Source: https://docs.devin.ai/work-with-devin/code-scans
- Skill management for migrated Knowledge uses v3 beta managed-plugin endpoints. Source: https://docs.devin.ai/product-guides/knowledge

### Devin for government

Primary source: https://docs.devin.ai/federal/introduction

- Federal documentation covers deployments of the Cognition platform on AWS GovCloud for U.S. Government and mission-partner workloads.
- The page names FedRAMP, ITAR, IL4/5, and on-prem as compliance targets and points to a Public Sector Trust Center.
- The federal portal uses dedicated enterprise SSO via OIDC or SAML. Some features from other Devin offerings are not available in the federal environment.
- Contact listed on the federal intro is public.sector@cognition.ai.

## Sources

- https://docs.devin.ai/
- https://docs.devin.ai/get-started/devin-intro
- https://docs.devin.ai/get-started/first-run
- https://docs.devin.ai/essential-guidelines/when-to-use-devin
- https://docs.devin.ai/onboard-devin/environment
- https://docs.devin.ai/onboard-devin/environment/macos-support
- https://docs.devin.ai/onboard-devin/environment/windows-support
- https://docs.devin.ai/onboard-devin/environment/android-emulation
- https://docs.devin.ai/onboard-devin/agents-md
- https://docs.devin.ai/cloud/outposts/overview
- https://docs.devin.ai/work-with-devin/devin-session-tools
- https://docs.devin.ai/work-with-devin/computer-use
- https://docs.devin.ai/work-with-devin/ask-devin
- https://docs.devin.ai/work-with-devin/deepwiki
- https://docs.devin.ai/work-with-devin/devin-review
- https://docs.devin.ai/work-with-devin/stacked-prs
- https://docs.devin.ai/work-with-devin/advanced-capabilities
- https://docs.devin.ai/work-with-devin/dynamic-workflows
- https://docs.devin.ai/work-with-devin/data-analyst
- https://docs.devin.ai/work-with-devin/security-swarm
- https://docs.devin.ai/work-with-devin/code-scans
- https://docs.devin.ai/work-with-devin/mcp
- https://docs.devin.ai/work-with-devin/devin-handoff
- https://docs.devin.ai/work-with-devin/voice-mode
- https://docs.devin.ai/cli/index
- https://docs.devin.ai/cli/essential-commands
- https://docs.devin.ai/cli/models
- https://docs.devin.ai/desktop/getting-started
- https://docs.devin.ai/_llms/en/desktop.md
- https://docs.devin.ai/product-guides/knowledge
- https://docs.devin.ai/product-guides/skills
- https://docs.devin.ai/product-guides/creating-playbooks
- https://docs.devin.ai/product-guides/plugins
- https://docs.devin.ai/product-guides/automations
- https://docs.devin.ai/product-guides/secrets
- https://docs.devin.ai/product-guides/security-profiles
- https://docs.devin.ai/product-guides/session-insights
- https://docs.devin.ai/product-guides/invite-team
- https://docs.devin.ai/product-guides/deployment-capabilities
- https://docs.devin.ai/product-guides/oidc
- https://docs.devin.ai/integrations/overview
- https://docs.devin.ai/integrations/slack
- https://docs.devin.ai/integrations/microsoft-teams
- https://docs.devin.ai/admin/billing/self-serve
- https://docs.devin.ai/admin/billing/enterprise
- https://docs.devin.ai/admin/security
- https://docs.devin.ai/enterprise/getting-started/get-started
- https://docs.devin.ai/enterprise/deployment/overview
- https://docs.devin.ai/enterprise/security-access/security/enterprise-security
- https://docs.devin.ai/enterprise/security-access/custom-roles
- https://docs.devin.ai/enterprise/security-access/trust-center
- https://docs.devin.ai/federal/introduction
- https://docs.devin.ai/api-reference/overview
- https://app.devin.ai
- https://deepwiki.com
- https://devinreview.com
