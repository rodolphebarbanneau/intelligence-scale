## Intelligence Scale type

I'll follow the evaluation skill and rate only the product in the spec.

The skill and spec are large, so I’ll read them in sections and follow the skill exactly.

The skill is loaded. Next I’ll read the Codex brief and rate only that product.

I’ll verify the docs that decide process ownership: automations, GitHub, Linear, security, and service accounts.

**Intelligence Scale capability: 1.6 / 3.0**

Type I with partial Type II capabilities.

Evaluated 2026-09-29 from `specs/codex.md` (reviewed 2026-09-28) and cited docs. Strongest supported configuration: ChatGPT Business or Enterprise Codex with cloud, GitHub, Linear, and scheduled tasks. API-key sign-in is out, because it drops cloud features. Experimental memories and research-preview Codex Security are not treated as native 1.00.

Codex is a coding agent people direct. A run can inspect a repo, edit files, run commands, and finish a bounded task while a person reviews the diff. Schedules, GitHub PR events, and Linear triage can start those runs, and a run can proceed unattended. That is task execution plus triggers, not an operator that owns a business process. Each case is still one dispatched task: one review, one issue, one prompt. There is no durable worker with its own principal, memory, credentials, and standing environment.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| I.1 | 1.00 | First-class agent in CLI, IDE, desktop, cloud, and mobile Remote, used inside normal software work. | https://learn.chatgpt.com/docs/codex/cli |
| I.2 | 1.00 | Runs use the repo, shell, AGENTS.md, skills, web search, plugins, and granted MCP; cloud adds setup and GitHub, GitLab, Linear, and Slack context. | https://learn.chatgpt.com/docs/extend/mcp |
| I.3 | 1.00 | The loop edits, runs commands, and continues until the task finishes or is cancelled. Cloud tasks run in the background. Subagents split work inside the task. | https://learn.chatgpt.com/docs/agent-configuration/subagents |
| I.4 | 1.00 | People set sandbox and approval policy, inspect diffs and logs, comment, follow up, and cancel. `/review` reports findings without editing the tree. | https://learn.chatgpt.com/docs/code-review |
| I.5 | 1.00 | AGENTS.md, skills, plugins, shared cloud environments, per-repo review, managed `requirements.toml`, and workspace RBAC make use repeatable. | https://learn.chatgpt.com/docs/enterprise/managed-configuration |
| II.1 | 0.25 | A person, mention, schedule, PR-open event, or Linear assignment starts one run that yields one review, diff, fix, or summary. Linear stops at a link for a person to open a PR. No persistent actor carries each case of a process to an outcome across runs. Security cloud only suggests fixes and is a research preview. | https://learn.chatgpt.com/docs/third-party/github |
| II.2 | 1.00 | Once a run starts, the agent moves through tools, results, retries, and subagents with no person between steps. Scheduled tasks use `approval_policy = never` when policy allows. Approvals are an organization choice. | https://learn.chatgpt.com/docs/automations |
| II.3 | 1.00 | During a run the agent selects files, shell, Git, search, skills, and granted plugins or MCP tools. No person coordinates each call. | https://learn.chatgpt.com/docs/plugins |
| II.4 | 0.50 | Resumable threads, config, and follow-ups exist. Service accounts authenticate runs; they are not a standing worker. Memories are experimental and off by default. Cloud containers cache for up to 12 hours. Linear chats run as the issue creator. | https://learn.chatgpt.com/docs/enterprise/service-accounts |
| II.5 | 1.00 | People can watch logs, receive approvals or auto-review, see Scheduled runs that need attention, intervene or cancel, and on Enterprise or Edu use Compliance API audit logs, without executing routine steps of an unattended run. | https://learn.chatgpt.com/docs/agent-approvals-security |
| II.6 | 1.00 | Schedules and events start runs with no person starting each one. GitHub automatic review fires on PR open in cloud. Linear triage can assign new issues. Web and mobile tasks can watch Gmail, Slack, or GitHub. Cloud work continues in the background. Local desktop schedules need the app running; that is not the only path. | https://learn.chatgpt.com/docs/automations |
| III.1 | 0.25 | Auto-review and scheduled prompts are narrow designed workflows, not organization-wide routine operations without humans structurally required. | https://learn.chatgpt.com/docs/third-party/github |
| III.2 | 0.25 | Codex executes work a person, rule, or event already placed. Subagents only split a run. Executing a queue is not work determination. | https://learn.chatgpt.com/docs/third-party/linear |
| III.3 | 0.25 | Subagents run inside a parent thread and return summaries. They are not persistent actors coordinating across runs. | https://learn.chatgpt.com/docs/agent-configuration/subagents |
| III.4 | 0.25 | Tool output changes the next step inside a run. No product loop evaluates operational outcomes and changes later operations. Experimental memories are recall, not that loop. | https://learn.chatgpt.com/docs/customization/memories |
| III.5 | 0.25 | The agent can change its plan inside a run. It does not rewrite processes or reallocate responsibilities outside that run. | https://learn.chatgpt.com/docs/agent-configuration/subagents |
| III.6 | 0.50 | RBAC, `requirements.toml`, approval constraints, and Compliance API set policy for agent runs. They do not support a model where routine intervention is exceptional. | https://learn.chatgpt.com/docs/enterprise/managed-configuration |

Type III grades are recorded above and do not enter the score. The floor is Type I, so progress is Type II only.

* **Completed floor:** 1
* **Next Type raw progress:** 0.79
* **Weakest criterion:** 0.25 (II.1)
* **Weakest-link penalty:** 0.15
* **Adjusted progress:** 0.64
* **Final score:** **1.6**

`(0.25 + 1.00 + 1.00 + 0.50 + 1.00 + 1.00) / 6 = 0.7917`. Penalty = `0.25 × (1 − 0.25) × 0.7917 = 0.1484`. Adjusted = `0.6433`. `1 + 0.6433 = 1.643`, rounded to **1.6**. Incomplete Type II cannot reach 2.0.

### What prevents the next Type?

Two Type II criteria are below 1.00. Both must be native before the score can reach 2.0.

* **II.1 — End-to-end process ownership.** No first-class persistent actor is put in charge of a process, takes each case from a trigger, channel, or queue, carries it to an outcome, and keeps doing so across runs. GitHub review, Linear assignment, Slack mentions, and scheduled prompts each dispatch one task.
* **II.4 — Persistent AI actor.** No durable worker has its own principal, memory across runs, its own permissions and credentials, and a durable execution environment. Service accounts only authenticate runs. Sessions are resumable, not a standing operator.

## Execution coverage

I'll follow the evaluation skill and rate only the product in `specs/codex.md`.

The skill is long, so I’ll read it in sections and open the Codex spec next.

Codex is a coding agent. I’ll check the cited docs that decide span, sharing, reach, and the plugin catalog.

The plugin directory is shared and not coding-only. I’ll confirm sharing, write-back, and whether those plugins are finished jobs.

**Execution coverage: 0.46 / 1.00**

Codex, evaluated 2026-09-29, is OpenAI’s coding agent on the strongest supported ChatGPT sign-in (Business or Enterprise: cloud, GitHub, Slack, Linear, plugins, and admin). The CLI and SDK are open source; the IDE extension and cloud are hosted. An organization can put software work on it: edit a repo, run tests, review a pull request, and scan for vulnerabilities. Other company functions have no native path.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| E.1 | 0.25 | Coding agent for software work: edit projects, run commands, review PRs. The selector sends other work to Chat or Work. A knowledge-work overlap and connectors do not give other functions a native path. | https://learn.chatgpt.com/docs/use-chatgpt |
| E.2 | 0.50 | Workspaces and roles exist, but a thread stays single-player. Share is a read-only macOS snapshot; results leave as a pull request, a GitHub review, or a Slack link and answer. | https://learn.chatgpt.com/docs/use-chatgpt |
| E.3 | 0.75 | Documented read and write on GitHub (reviews and pushes), Linear (issue progress), and Slack (replies). The plugin directory adds Gmail, Drive, and Slack, but those examples are read-heavy. GitLab write-back is beta. | https://learn.chatgpt.com/docs/plugins |
| E.4 | 1.00 | One plugin directory in Codex desktop and CLI, with OpenAI, workspace, and personal tabs. It is not one craft or suite. OpenAI, third parties, and a workspace GitHub marketplace can publish. | https://learn.chatgpt.com/docs/plugins |
| E.5 | 0.75 | Work runs in the desktop app, web cloud, CLI, IDE, Slack, and the SDK or app server. No mail or customer-channel surface. GitLab is beta; mobile Remote only steers a paired computer. | https://learn.chatgpt.com/docs/codex/cli |
| E.6 | 1.00 | Install and ChatGPT sign-in are documented from Free through Enterprise. Business and Enterprise add roles, permissions, SSO, and managed configuration, so a team can start without assembling the core. | https://learn.chatgpt.com/docs/pricing |
| E.7 | 0.25 | Shipped jobs are code review and security scans, both inside the coding craft. The directory holds connectors and skills, not finished jobs for other functions. Other work is still a prompt the buyer writes. | https://learn.chatgpt.com/docs/code-review |

* **Raw mean:** 0.64 (4.50 / 7 = 0.6429)
* **Weakest criterion:** 0.25
* **Weakest-link penalty:** 0.19 (0.25 × 0.75 = 0.1875)
* **Uncapped score:** 0.46 (0.6429 − 0.1875 = 0.4554, above the halfway point, so 0.46)
* **Span cap:** 0.49, because E.1 is 0.25 or lower
* **Final score:** **0.46**

### What most limits coverage?

E.1 and E.7 are both 0.25. Codex is a software-development surface: non-developers have no native product for their own jobs, and the only turnkey jobs are code review and security scans. The plugin directory does not install finished jobs for other functions. The span cap keeps the published score under 0.50.
