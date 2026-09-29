## Intelligence Scale type

I'll follow the evaluation skill and rate only the product in the spec.

The skill and spec are large, so I'll read them in sections and follow the skill exactly.

I'll verify the cited docs that decide Type II, especially routines, projects, agents, and triggers.

Routines and projects are the Type II hinge. I'll pull the remaining cited pages on identity, review, and agents.

**Intelligence Scale capability: 1.7 / 3.0**

Approaching Type II. Evaluated 2026-09-29 from `specs/claude-code.md` (reviewed 2026-09-28) and cited docs. Strongest supported configuration: cloud sessions, connectors, Auto or Accept edits, GitHub Actions, plus research-preview routines and code review and public-beta projects. Those preview surfaces cannot score above 0.75.

Claude Code natively embeds an agent in the terminal, IDEs, desktop, and web. It reads a repo, edits files, runs commands, and opens pull requests while a person still owns the work. Routines can repeat a saved prompt from a schedule, webhook, or GitHub event, but each event starts a new session that acts as the user. That is assisted execution plus a trigger engine, not an operator that owns a process.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| I.1 | 1.00 | Coding agent is a supported daily surface in the CLI, VS Code, JetBrains, Desktop Code tab, claude.ai/code, and mobile. | https://code.claude.com/docs/en/overview |
| I.2 | 1.00 | Sessions load the repo, `CLAUDE.md`, auto memory, web, GitHub, skills, and connectors. Custom MCP is extra, not the only path. | https://code.claude.com/docs/en/memory |
| I.3 | 1.00 | The session loop gathers context, edits, runs commands, and verifies multi-step coding work without the person performing each step. | https://code.claude.com/docs/en/how-claude-code-works |
| I.4 | 1.00 | People start work, switch permission modes, review diffs and plans, interrupt with Esc, and resume sessions. | https://code.claude.com/docs/en/permissions |
| I.5 | 1.00 | Skills, hooks, plugins, managed settings, and the GitHub App make the same loop repeatable for a team. | https://code.claude.com/docs/en/admin-setup |
| II.1 | 0.50 | A routine is a saved prompt, repos, and connectors. GitHub events start independent sessions and do not reuse them. Projects still take tasks a person pastes. Judgment: trigger engine, not a persistent owner. | https://code.claude.com/docs/en/routines |
| II.2 | 1.00 | Once started, Auto, Accept edits, Bypass, or a routine proceeds through steps without a person between them. Approvals are a mode choice. Artifact asks are the exception. | https://code.claude.com/docs/en/routines |
| II.3 | 1.00 | During a run the agent selects shell, files, web, skills, subagents, GitHub, and included connectors without a person placing each call. | https://code.claude.com/docs/en/tools-reference |
| II.4 | 0.50 | Routines, resumable sessions, and project memory persist as configuration. Runs act with the person's GitHub identity and connectors. No worker principal or durable state across events. | https://code.claude.com/docs/en/routines |
| II.5 | 0.75 | People can watch a session URL, review diffs, get Desktop or Remote Control alerts, and cloud runs are audit-logged. No documented exception inbox or stop control for unattended cloud routines. | https://code.claude.com/docs/en/security |
| II.6 | 0.75 | Routines combine schedule, API POST, and GitHub events and keep running in the cloud, but they are research preview. Desktop schedules run only while the app is open. | https://code.claude.com/docs/en/routines |
| III.1 | 0.25 | Unattended work is a person-authored routine, review rule, or Action, not organization-wide operations. | https://code.claude.com/docs/en/routines |
| III.2 | 0.25 | A project coordinator splits work a person already sent. Agent teams are experimental, off by default, and inside one session. | https://code.claude.com/docs/en/claude-projects |
| III.3 | 0.25 | Subagents, experimental teams, and cross-session messages collaborate inside human-started sessions, not as persistent actors. | https://code.claude.com/docs/en/agents |
| III.4 | 0.25 | A session can verify its own edits. Independent routine sessions do not show outcome evaluation changing the next run. | https://code.claude.com/docs/en/how-claude-code-works |
| III.5 | 0.25 | The agent can change its plan inside a run. It does not revise standing processes or reallocate responsibilities. | https://code.claude.com/docs/en/agents |
| III.6 | 0.25 | Admin policy, spend limits, and audit exist, but people still dispatch and review routine coding work. | https://code.claude.com/docs/en/admin-setup |

* **Completed floor:** 1
* **Next Type raw progress:** 0.75
* **Weakest criterion:** 0.50
* **Weakest-link penalty:** 0.09
* **Adjusted progress:** 0.66
* **Final score:** **1.7**

Mean of II.1–II.6 is 4.50 / 6 = 0.75. Penalty = 0.25 × (1 − 0.50) × 0.75 = 0.09375. Adjusted = 0.65625. Rounded to one decimal is 1.7. Type II is incomplete, so the score stays below 2.0.

### What prevents the next Type?

Crossing 2.0 needs every Type II criterion at 1.00. These are short:

* **II.1** — No persistent actor owns a process across cases. Routines and code review fire a fresh session per event and usually stop at a draft, comment, or report.
* **II.4** — No durable worker with its own principal, cross-run memory, own permissions and credentials, and durable execution state. Sessions act as the user and are not reused across events.
* **II.5** — Unattended cloud runs lack a first-class exception channel and a documented stop control short of opening the session.
* **II.6** — Schedule, webhook, and GitHub triggers that run with the laptop closed are research preview. Desktop schedules die when the app is closed.

## Execution coverage

I'll follow the evaluation skill and rate only the product in the spec. Let me read both files first.

The spec is large, so I'll read it in sections and use only that brief for the rating.

I'll verify the cited docs that decide span, sharing, reach, and the catalog before scoring.

Sharing and the catalog still need primary-source checks. I'll open those cited pages next.

**Execution coverage: 0.35 / 1.00**

Claude Code, evaluated 2026-09-29, is Anthropic’s agentic coding chassis: CLI, VS Code, JetBrains, Desktop Code, claude.ai/code, and mobile as a client. The strongest supported setup is a current claude.ai plan (Pro, Max, Team, or Enterprise). An engineering team can install it, administer it, and put repository work on it. Other company functions have no native path.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| E.1 | 0.25 | Agentic coding tool for tests, bugs, commits, and pull requests. Projects can accept non-code uploads, but that path is public beta, Pro/Max only, gradual, and not a native path for other functions. | https://code.claude.com/docs/en/overview ; https://code.claude.com/docs/en/claude-projects |
| E.2 | 0.50 | Team and Enterprise accounts exist. Session sharing is Private or Team/Public; recipients see the latest state, not a live shared thread. Slack starts a cloud session and posts status. Collaboration after the fact is the pull request. | https://code.claude.com/docs/en/claude-code-on-the-web ; https://code.claude.com/docs/en/slack |
| E.3 | 0.75 | Desktop Connectors install Google Calendar, Slack, GitHub, Linear, Notion, and others. Docs state Claude can read a calendar, send messages, and create issues. Cloud and WSL lack that add flow; write-back is not a shipped job matrix for mail, CRM, or files. | https://code.claude.com/docs/en/desktop |
| E.4 | 0.25 | Official plugin marketplace, plus org and third-party marketplaces, installs skills, agents, hooks, MCP, and language servers. That catalog stays inside the coding craft. | https://code.claude.com/docs/en/desktop ; https://code.claude.com/docs/en/plugins/overview |
| E.5 | 0.75 | Work runs in the CLI, VS Code, JetBrains, Desktop, the web, and the mobile Code tab. Slack is a delegation channel. The Agent SDK is a documented API. No mail or customer channel. Telegram, Discord, and iMessage channels are research preview. | https://code.claude.com/docs/en/platforms ; https://code.claude.com/docs/en/agent-sdk/overview ; https://code.claude.com/docs/en/channels |
| E.6 | 1.00 | Documented install and sign-in for CLI, IDE, Desktop, and web. Team adds server-managed settings and SSO; Enterprise adds SCIM. Permissions and admin controls are documented. | https://code.claude.com/docs/en/overview ; https://code.claude.com/docs/en/feature-availability ; https://code.claude.com/docs/en/admin-setup |
| E.7 | 0.25 | Bundled commands such as `/code-review` and `/debug`, plus managed PR review, stay inside coding. A person still describes each task. No shipped, installed, or generated jobs for other business functions. | https://code.claude.com/docs/en/overview ; https://code.claude.com/docs/en/skills ; https://code.claude.com/docs/en/code-review |

* **Raw mean:** 0.54
* **Weakest criterion:** 0.25
* **Weakest-link penalty:** 0.19
* **Uncapped score:** 0.35
* **Span cap:** 0.49, because E.1 is 0.25 or lower
* **Final score:** **0.35**

### What most limits coverage?

E.1, E.4, and E.7 are the floor. Only software development fits as shipped. The plugin marketplace does not carry jobs for other functions, and there is no turn-on, install, or describe-and-approve path that produces a running job outside that craft. Session sharing is a transcript and a pull request, not live multiplayer, but that is a higher grade than the craft limits.
