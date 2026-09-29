## Intelligence Scale type

I'll follow the evaluation skill and rate only the product in the spec. Let me read both files first.

The skill and spec are large, so I’ll read them in sections and follow the skill exactly.

The skill is loaded. Next I’ll read the Grok Build spec and rate only that product.

The spec is in. I’ll open the cited docs that decide process ownership, triggers, and persistent actors before scoring.

A few docs pages failed to load. I’ll pull those cited sources directly and check memory, loops, and enterprise controls.

**Intelligence Scale capability: 1.7 / 3.0**

Type I with partial Type II capabilities.

Evaluated 2026-09-29. Grok Build is xAI’s local coding CLI and TUI, not Grok Bot and not the grok-4.7 API in another loop. In the strongest supported setup, a person still owns the work. The agent assists in the repo, completes multi-step coding runs, and can fan out a saved workflow after someone launches it. It is not a persistent operator that takes the next case on its own.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| I.1 | 1.00 | Interactive TUI, headless `grok -p`, and ACP put the agent in ordinary coding work. | https://docs.x.ai/build/overview |
| I.2 | 1.00 | Reads the repo, `@` files, AGENTS.md, skills, web search, and configured MCP tools. | https://docs.x.ai/build/features/skills-plugins-marketplaces |
| I.3 | 1.00 | A turn can explore, edit, run commands, and spawn subagents inside a bounded task. | https://docs.x.ai/build/features/subagents |
| I.4 | 1.00 | Ask, auto, and always-approve; plan review; deny hooks; cancel and rewind. | https://docs.x.ai/build/features/permissions |
| I.5 | 1.00 | Sessions, skills, plugins, and saved project workflows repeat across runs. | https://docs.x.ai/build/features/sessions |
| II.1 | 0.50 | Rhai workflows fan out subagents and return a result. A person launches each run. No actor takes cases from a channel or queue. | https://docs.x.ai/build/modes-and-commands |
| II.2 | 1.00 | Once a turn or workflow starts, steps proceed. Always-approve is an organizational choice, not a forced gate between steps. | https://docs.x.ai/build/features/permissions |
| II.3 | 1.00 | During a run the agent selects shell, file, search, web, and subagent tools, plus granted MCP, without a person placing each call. | https://docs.x.ai/build/features/permissions |
| II.4 | 0.50 | Sessions and worktrees resume under the user’s login. No actor principal. `--experimental-memory` is off by default. | https://docs.x.ai/build/cli/reference |
| II.5 | 0.75 | Live prompts, plan approval, stop, and local transcripts. No escalation path or audit beyond the session file. | https://docs.x.ai/build/features/sessions |
| II.6 | 0.75 | `/loop` repeats a prompt on an interval. One trigger kind. No webhook or queue. Survival after the CLI exits is unproven. | https://docs.x.ai/build/modes-and-commands |
| III.1 | 0.25 | Routine coding can continue only inside a person-started run or workflow. | https://docs.x.ai/build/modes-and-commands |
| III.2 | 0.25 | Todos and subagent fan-out split work a person already handed over. | https://docs.x.ai/build/features/subagents |
| III.3 | 0.25 | Child sessions report to the parent inside one run or a saved workflow. Separate sessions do not coordinate. | https://docs.x.ai/build/features/subagents |
| III.4 | 0.25 | A run can observe tool results and continue. That does not retune later operations. | https://docs.x.ai/build/features/sessions |
| III.5 | 0.25 | The agent can revise a plan inside one task. It does not reorganize work across runs. | https://docs.x.ai/build/features/plan-mode |
| III.6 | 0.00 | Humans still dispatch each run. A governance-only operating model is not supported. | https://docs.x.ai/build/enterprise |

* **Completed floor:** 1
* **Next Type raw progress:** 0.75
* **Weakest criterion:** 0.50 (II.1 and II.4)
* **Weakest-link penalty:** 0.09
* **Adjusted progress:** 0.66
* **Final score:** **1.7**

Penalty is `0.25 × (1 − 0.50) × 0.75 = 0.09375`. Adjusted progress is `0.65625`. Rounded score is 1.7, below the Type II gate.

### What prevents the next Type?

Type II needs every II criterion at 1.00. Four are short:

* **II.1** — No persistent actor owns a process across cases. Workflows are person-launched runs, not a worker that takes the next case from a trigger, channel, or queue.
* **II.4** — No durable actor principal, own credentials, or own permissions. Sessions resume as the user. Cross-session memory is experimental and off by default.
* **II.5** — No exception escalation, and no audit beyond the local session transcript.
* **II.6** — Only an in-session interval loop. No event or webhook trigger that starts runs without a person, and no proven continuation after the CLI exits.

## Execution coverage

I'll follow the evaluation skill and rate only the product in the spec.

The spec is large, so I'll read it in sections and use only its cited sources.

The brief is a local coding agent. I'll check the cited docs for sharing, surfaces, and any catalog beyond that craft.

**Execution coverage: 0.24 / 1.00**

Grok Build, evaluated 2026-09-29, is xAI’s local coding-agent CLI (`grok`): a terminal TUI, headless runs, and an ACP embed. A team can put software-engineering work on it today — edit a repo, plan a change, run a workflow — after install and login, including an enterprise-managed install. Other company functions have no native path. Grok Bot is out of scope. Sessions stay single-player; sharing is a URL or a transcript.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| E.1 | 0.25 | Documented as a coding agent for a project directory. `/imagine`, `/imagine-video`, and `/deep-research` are commands inside that CLI, not a path for other functions. | https://docs.x.ai/build/overview |
| E.2 | 0.50 | Team and enterprise accounts exist (OIDC, team UUID, team-level ZDR). Sessions are local. `/share` is a URL; `grok export` is a transcript. The dashboard is one operator over local agents, not several people in one run. | https://docs.x.ai/build/enterprise ; https://docs.x.ai/build/modes-and-commands ; https://docs.x.ai/build/features/sessions ; https://docs.x.ai/build/features/dashboard |
| E.3 | 0.25 | Reads and writes the local repository. Web search is the public web. Other systems need the buyer to add MCP servers; the Linear example is a generic add, not a shipped job. | https://docs.x.ai/build/overview ; https://docs.x.ai/build/features/mcp-servers |
| E.4 | 0.25 | A Marketplace tab installs plugins from configured sources, including Claude Code marketplaces. That catalog stays inside the coding craft. | https://docs.x.ai/build/features/skills-plugins-marketplaces |
| E.5 | 0.50 | Work happens in the terminal TUI (headless is the same CLI) and through the documented ACP embed for other apps. No workplace chat, mail, or product web app. | https://docs.x.ai/build/overview ; https://docs.x.ai/build/cli/headless-scripting |
| E.6 | 1.00 | Public install (curl, PowerShell, npm), browser or device-code login, in-product billing (`/usage`), permission rules, and managed setup (`grok setup`, enterprise requirements and OIDC). | https://docs.x.ai/build/overview ; https://docs.x.ai/build/cli/reference ; https://docs.x.ai/build/enterprise ; https://docs.x.ai/build/modes-and-commands |
| E.7 | 0.25 | The shipped job is a coding assistant. `/create-workflow` and `/deep-research` stay inside that craft. No ready-made jobs for other business functions. | https://docs.x.ai/build/overview ; https://docs.x.ai/build/modes-and-commands |

* **Raw mean:** 0.43
* **Weakest criterion:** 0.25
* **Weakest-link penalty:** 0.19
* **Uncapped score:** 0.24
* **Span cap:** 0.49, because E.1 is 0.25 or lower
* **Final score:** **0.24**

### What most limits coverage?

E.1, E.3, E.4, and E.7 are 0.25. Only coding work fits. There is no shipped read/write into mail, tickets, CRM, or calendar, and the plugin marketplace does not leave the coding craft. Ready-made jobs do not cover other business functions. The span cap would hold any higher average at 0.49; the weakest-link penalty already sets 0.24.
