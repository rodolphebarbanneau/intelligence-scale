## Intelligence Scale type

I'll follow the evaluation skill and rate only the product in `specs/devin.md`.

The skill and spec are long, so I'll read them in sections and follow the skill exactly.

The brief is Devin. I’ll check the cited docs that decide process ownership, triggers, and persistent actors.

Auto-fix and actor identity still decide the Type II grades. I’ll pull those sections next.

**Intelligence Scale capability: 1.8 / 3.0**

Approaching Type II.

Evaluated 2026-09-29 from the 2026-09-28 Devin brief and cited docs. The rated configuration is Teams or Enterprise cloud Devin with automations, auto-triage, GitHub, Slack, playbooks, skills, Computer Use, and dynamic workflows. CLI-only and federal deployments are weaker and are not the ceiling.

Devin can sit inside engineering work and finish bounded tasks: code, tests, a pull request, a triage note. People still define most work and finish or merge the result. Schedules and events can start runs, and one persistent monitor owns Slack triage. That is Type I plus real Type II machinery, not a durable owner of complete processes.

| Criterion | Grade | Evidence | Source |
| --- | ---: | --- | --- |
| I.1 | 1.00 | Web, Slack, Teams, CLI, Desktop, and API put Devin in ordinary engineering work. | https://docs.devin.ai/get-started/devin-intro |
| I.2 | 1.00 | Sessions use indexed repos, an org snapshot, secrets, skills, playbooks, MCP, and native GitHub, Slack, Linear, and Jira connections. | https://docs.devin.ai/get-started/first-run |
| I.3 | 1.00 | Agent mode writes code, runs commands, browses, tests, opens pull requests, and monitors CI for a bounded task. | https://docs.devin.ai/get-started/first-run |
| I.4 | 1.00 | People start work, watch Progress, take over the IDE or browser, stop a run, and review the pull request. | https://docs.devin.ai/work-with-devin/devin-session-tools |
| I.5 | 1.00 | Playbooks, skills, one org snapshot, Teams and Enterprise roles, and saved automations make use repeatable. | https://docs.devin.ai/product-guides/creating-playbooks |
| II.1 | 0.75 | Auto-triage is a persistent Devin that takes each Slack report to a diagnosis and owner. Other automations start a new task session per event and usually stop at a note or pull request a person finishes. | https://docs.devin.ai/product-guides/auto-triage |
| II.2 | 1.00 | Once a session, child batch, workflow, or triage child starts, it moves through steps with no person between them. Child and workflow approval can stay off. | https://docs.devin.ai/work-with-devin/dynamic-workflows |
| II.3 | 1.00 | During a run Devin selects shell, editor, browser, Computer Use, git, granted MCP, and child agents. Setup grants do not require a person to place each call. | https://docs.devin.ai/work-with-devin/devin-session-tools |
| II.4 | 0.50 | Auto-triage is a long-running session with a scratchpad, and every session boots a fresh copy of one org snapshot. Sessions are attributed to a requesting user, auto-triage needs that person's Slack, and session changes do not persist. There is no worker principal with its own permissions and credentials. | https://docs.devin.ai/onboard-devin/environment |
| II.5 | 1.00 | People observe Progress and automation activity, set optional approvals and ACU caps, intervene or stop, and on Enterprise read audit logs, without executing routine steps. | https://docs.devin.ai/product-guides/automations |
| II.6 | 1.00 | Cron, webhooks, and Slack, GitHub, GitLab, Linear, Jira, and PagerDuty events start cloud runs. Nobody has to start each one. | https://docs.devin.ai/product-guides/automations |

* **Completed floor:** 1
* **Next Type raw progress:** 0.88 (5.25 / 6 = 0.875)
* **Weakest criterion:** 0.50 (II.4)
* **Weakest-link penalty:** 0.11 (0.25 × 0.50 × 0.875 = 0.109)
* **Adjusted progress:** 0.77 (0.875 − 0.109 = 0.766)
* **Final score:** **1.8**

### What prevents the next Type?

Two Type II criteria are below 1.00, so the score cannot reach 2.0.

* **II.1:** A persistent actor owns only Slack triage. Ticket, CI, and schedule automations still dispatch one task session per event, and the usual outcome is a diagnosis or pull request a person finishes.
* **II.4:** There is no durable Devin principal with its own permissions, its own credentials, and an environment that keeps state across runs.

## Execution coverage

I'll follow the evaluation skill and rate only the product in the spec.

The spec is too large to read at once. I'll load it in sections and use only that brief.

The brief is Devin, Cognition’s software-engineer product. I’ll check the cited docs that decide span, sharing, reach, and catalogs.

**Execution coverage: 0.42 / 1.00**

Devin is Cognition’s hosted AI software engineer (Teams and Enterprise, evaluated 2026-09-29). An engineering team can put coding work on it today: tickets, features, bugs, reviews, scans, and data questions. Sales, support, finance, and the rest of the company have no native path.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| E.1 | 0.25 | Documented as an AI software engineer for engineering teams: tickets, features, bugs, migrations, PR review, tests, docs, internal tools. Data Analyst is a mode of that same product, not a second business function. | https://docs.devin.ai/get-started/devin-intro |
| E.2 | 0.75 | Slack and Teams threads are the work: teammates tag Devin, it replies in-thread, and web messages sync back. Live IDE handoff between people is not documented; Slack code channels still depend on Slack’s rollout. | https://docs.devin.ai/integrations/slack |
| E.3 | 0.75 | Native write to GitHub/GitLab and Jira, plus catalog write to Outlook mail, calendar, SharePoint files, and Linear/Notion via templates. CRM write is unproven; broad write-back is connect-and-install, not a complete shipped job set. | https://docs.devin.ai/integrations/overview |
| E.4 | 0.25 | First-party marketplace, and orgs can add git or zip plugins, but entries are skills and connectors for the coding agent (Linear, Notion, Datadog, Snowflake). A coding marketplace stays in one craft. | https://docs.devin.ai/product-guides/plugins |
| E.5 | 1.00 | Work runs in the web app, Slack, Microsoft Teams, the CLI, Desktop, and the documented v3 API. | https://docs.devin.ai/api-reference/overview |
| E.6 | 1.00 | Free, Pro, Max, and Teams sign up at app.devin.ai. Teams has invites, seats, and admin; Enterprise adds SSO, SCIM, and custom roles. | https://docs.devin.ai/admin/billing/self-serve |
| E.7 | 0.25 | Review, scans, and automation templates (CI fix, triage, Notion/Asana/Linear reports) can be turned on or generated, but every ready-made job stays inside software engineering. | https://docs.devin.ai/product-guides/automations |

* **Raw mean:** 0.61 (4.25 / 7 = 0.607…)
* **Weakest criterion:** 0.25
* **Weakest-link penalty:** 0.19 (0.25 × 0.75 = 0.1875)
* **Uncapped score:** 0.42 (0.607… − 0.1875 = 0.420, half down)
* **Span cap:** 0.49, because E.1 is 0.25 — does not lower the score further
* **Final score:** **0.42**

### What most limits coverage?

E.1, E.4, and E.7. The product is a software-engineering craft. The marketplace does not carry other functions, and the shipped jobs (review, scans, triage and report templates) do not either. Mail, calendar, and file write exist only as connectors for that same agent.
