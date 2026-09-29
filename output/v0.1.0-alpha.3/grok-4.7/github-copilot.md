## Intelligence Scale type

I'll follow the evaluation skill and rate only the product in the spec.

The skill and spec are large, so I’ll read them in sections and follow the skill exactly.

I’ll finish the skill criteria and the rest of the Copilot spec before scoring.

Type II hinges on process ownership, so I’ll check the cited docs for automations, cloud agent, and workflows.

**Intelligence Scale capability: 1.7 / 3.0**

Type I with partial Type II capabilities.

Evaluated 2026-09-29 from `specs/github-copilot.md` and cited GitHub docs. Strongest current configuration: paid Copilot (Enterprise, or Pro/Pro+/Max) with cloud agent, automations, code review, CLI, and the Copilot app. GitHub Agentic Workflows and Copilot Memory are public preview and do not set the ceiling.

People still execute software delivery. Copilot is embedded in the IDE, GitHub, CLI, and app, and it can finish bounded coding tasks: edit, test, and open a pull request. Schedules and repository events can start those tasks in the background. What it does not provide is a durable actor that owns a case from trigger through outcome. Each run is an ephemeral session, attributed to a person, usually ending in a reviewable change.

| Criterion | Grade | Evidence | Source |
| --- | ---: | --- | --- |
| I.1 | 1.00 | Completions, chat, and agents are in the IDE, github.com, Mobile, CLI, and the Copilot app, not an isolated API. | https://docs.github.com/en/copilot/get-started/where-to-use-github-copilot |
| I.2 | 1.00 | Native repo, issue, and pull-request context; Spaces; GitHub MCP configured for Chat and cloud agent. Extra MCP is not required for that access. | https://docs.github.com/en/copilot/concepts/about-github-copilot-chat |
| I.3 | 1.00 | Cloud agent researches, edits, runs tests, and opens a pull request. IDE agent mode and CLI do the same class of multi-step task. | https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/start-copilot-sessions |
| I.4 | 1.00 | People start or steer work, approve CLI tools, review diffs, and merge. Plan mode and code review are first-class. | https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli |
| I.5 | 1.00 | Seats, AI controls, org and enterprise custom agents, content exclusion, budgets, and usage metrics make use repeatable. | https://docs.github.com/en/copilot/concepts/policies |
| II.1 | 0.50 | Automations are a GA trigger engine for defined tasks (label issues, nightly fix, release notes), one repo, one session each. No actor carries a case to a business outcome. Agentic Workflows are the same pattern in preview. | https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations |
| II.2 | 1.00 | Once a cloud-agent or automation run starts, it moves through its steps in the background. Per-tool approval is removable on CLI (`--allow-all-tools`). The task-versus-process gap is counted only on II.1. | https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations |
| II.3 | 1.00 | During a run the agent selects granted tools: files, shell, tests, default GitHub and Playwright MCP, skills, and CLI subagents. Toolbox binding at setup is not a penalty. | https://docs.github.com/en/copilot/concepts/context/mcp |
| II.4 | 0.50 | Custom agents, automations, and resumable CLI sessions persist as configuration. Cloud-agent runs are ephemeral Actions sessions. Automation pull requests are attributed to the creating user, not a Copilot principal. Memory is preview and stores repo facts and user preferences, not actor state. | https://docs.github.com/en/copilot/concepts/agents/copilot-memory |
| II.5 | 0.75 | Session logs, pull-request review, CLI steering, tool approval, confidence holds on issue edits, and org or enterprise audit logs exist. Mid-run stop and escalation are not documented as first-class on the unattended cloud path, so supervision is partly after the fact. | https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations |
| II.6 | 1.00 | GA automations start on hourly, daily, or weekly schedules and on issue or pull-request events, in Actions, without a person starting each run. | https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations |
| III.1 | 0.25 | Unattended work is inside a designed automation or workflow. Routine delivery still needs a person to review and merge. | https://docs.github.com/en/copilot/concepts/agents/about-github-agentic-workflows |
| III.2 | 0.25 | The agent consumes an assigned issue, prompt, or fired trigger. CLI subagents split work only inside that run. | https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli |
| III.3 | 0.25 | Subagents run inside one session. Review-to-cloud-agent handoff is public preview, not persistent actors coordinating. | https://docs.github.com/en/copilot/concepts/agents/code-review |
| III.4 | 0.25 | A run can test, observe failure, and retry. Preview Memory does not evaluate outcomes and change later operational decisions. | https://docs.github.com/en/copilot/concepts/agents/copilot-memory |
| III.5 | 0.25 | The agent can replan inside a run. Cross-run process design stays in human prompts, automations, and workflow files. | https://docs.github.com/en/copilot/concepts/agents/about-github-agentic-workflows |
| III.6 | 0.25 | Policies, budgets, and audit are real controls, but they do not make routine human review exceptional. | https://docs.github.com/en/copilot/concepts/policies |

* **Completed floor:** 1
* **Next Type raw progress:** 0.79
* **Weakest criterion:** 0.50
* **Weakest-link penalty:** 0.10
* **Adjusted progress:** 0.69
* **Final score:** **1.7**

### What prevents the next Type?

Type II is incomplete, so the score stays below 2.0.

* **II.1:** No persistent actor owns an end-to-end process. Automations dispatch one task per event or schedule and stop at a label, report, or pull request.
* **II.4:** No durable principal with its own credentials, permissions, memory, and execution state. Sessions are ephemeral and act as the user.
* **II.5:** Unattended cloud runs lack a complete supervise-and-intervene path; people still review the resulting change.

## Execution coverage

I'll follow the evaluation skill and rate only the product in the spec.

The Copilot spec is large, so I’ll read it in sections and use only that brief.

The brief is a coding product. I’ll check cited docs on sharing, integrations, and catalogs before scoring.

Docs fetches were blocked, so I’ll open the cited pages another way and check the scoring notes.

I’ll pull the cited GitHub docs that the fetch tool blocked.

**Execution coverage: 0.35 / 1.00**

GitHub Copilot, evaluated 2026-09-29 from the 2026-09-28 spec, is the hosted coding assistant in its strongest supported configuration: Copilot Enterprise on GitHub Enterprise Cloud, including generally available Business and paid-plan features. A software team can complete, chat about, review, and assign repository work that returns as a pull request. Other company functions have no native path onto it. Preview items (Memory, Agentic Workflows, third-party agents, Slack and Teams planning) are not treated as full coverage.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| E.1 | 0.25 | Copilot is an assistant for writing, understanding, and shipping software. Completions, chat, cloud agent, review, and repo automations stay in that craft. Issue triage and docs updates are still repository work. | https://docs.github.com/en/copilot/get-started/what-is-github-copilot |
| E.2 | 0.50 | Business and Enterprise are team plans. Shared state is a pull request, a review comment, or `@copilot` on that request. Spaces share context, not a live run. Automation logs are visible; the definition stays private to its creator. Canvas copy does not document several people and the operator in one thread. | https://docs.github.com/en/copilot/concepts/context/spaces |
| E.3 | 0.75 | Native read and write of GitHub code, issues, pull requests, branches, and merges. Jira, Linear, and Azure Boards are read for issue context; the documented write is a GitHub pull request, not write-back to those systems. Slack and Teams capture a thread. MCP the buyer wires does not raise this. | https://docs.github.com/en/copilot/concepts/tools/about-copilot-integrations |
| E.4 | 0.25 | Plugin marketplaces (`copilot-plugins`, `awesome-copilot`) and org or enterprise agent profiles exist, and customers can add entries. They package coding agents, skills, hooks, and MCP for CLI, cloud agent, and the Copilot app. A coding marketplace does not extend span. | https://docs.github.com/en/copilot/concepts/agents/about-plugins |
| E.5 | 0.75 | Work runs in IDEs, on github.com, in GitHub Mobile, in Copilot CLI, in the Copilot app, and through the documented SDK. Slack and Teams can start a session; planning there is public preview. No mail or customer channel. | https://docs.github.com/en/copilot/get-started/where-to-use-github-copilot |
| E.6 | 1.00 | Free start, paid individual plans, and Business or Enterprise seats with documented AI controls, permissions, content exclusion, budgets, and usage metrics. A team can assign seats and put repository work on it without assembling the core. | https://docs.github.com/en/copilot/concepts/policies |
| E.7 | 0.25 | Code review, pull-request summaries, completions, and cloud agent from an issue are ready to turn on, but only for software work. Custom agents and agentic workflows are still jobs a builder writes inside that craft. | https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent |

* **Raw mean:** 0.54
* **Weakest criterion:** 0.25
* **Weakest-link penalty:** 0.19
* **Uncapped score:** 0.35
* **Span cap:** 0.49, because E.1 is 0.25 or lower
* **Final score:** **0.35**

### What most limits coverage?

E.1, E.4, and E.7 are 0.25. Only software work fits, the installable catalog stays inside that craft, and the jobs you can turn on do not cover any other function. E.2 stops at after-the-fact pull-request sharing: there is no documented thread where several people and the operator share one run. External tickets are read; write-back to Jira, Linear, or Azure Boards is not documented.
