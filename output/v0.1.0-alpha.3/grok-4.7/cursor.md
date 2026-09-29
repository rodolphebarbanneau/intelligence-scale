## Intelligence Scale type

I'll follow the evaluation skill and rate only the product in the spec.

The skill and spec are large, so I’ll read them in sections and follow the skill exactly.

The skill is loaded. Next I’ll read the Cursor spec and score only that product.

I’ll verify the Type II and Type III claims in the cited Cursor docs before scoring.

Cursor’s strongest current configuration is a Type II coding chassis: managed agents and automations own repeated software-delivery processes, while people set policy and handle exceptions. Adaptive, organization-level orchestration is only partial.

**Intelligence Scale capability: 2.7 / 3.0**

Approaching Type III.

Evaluated 2026-09-29 from `specs/cursor.md` and cited docs. Scope is the Cursor coding product (editor, Agents Window, CLI, cloud agents, automations, Teams/Enterprise admin). Grok Bot and Origin are out of scope. The strongest supported setup is a paid Teams or Enterprise plan with Cloud Agents, Automations, Bugbot, Security Agents, PR Routing & Approval, and Rollouts on GitHub. Projects is included only as a rolling-out, non-Enterprise limit.

People define triggers, prompts, and policy. Cursor-managed agents and service-account automations then take each pull request, scan, incident, or schedule and carry it to a review, approval, finding, or health verdict without a person stepping the run. That is delegated execution. It is not yet an operating model where AI sets the agenda, coordinates actors generally, and changes later operations from what it learns.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| I.1 | 1.00 | Agent, Tab, and inline edit are in the editor; the same agent runs in the CLI, on the web, on iOS, and from Slack, Linear, Teams, GitHub, and Jira. | https://cursor.com/docs/agent/overview |
| I.2 | 1.00 | Tools include codebase search, file edit, shell, browser, web, rules, skills, MCP, and cloud VMs with repos, secrets, and computer use. | https://cursor.com/docs/agent/overview |
| I.3 | 1.00 | Agent edits, runs commands, and tests with no documented tool-call cap. Cloud agents build, verify, and open PRs without the laptop staying online. | https://cursor.com/docs/cloud-agent |
| I.4 | 1.00 | Plan Mode waits for approval. Run Modes, checkpoints, queued steering, follow-ups, and remote desktop handoff let a person direct and correct work. | https://cursor.com/docs/agent/plan-mode |
| I.5 | 1.00 | Teams and Enterprise add shared rules, skills, marketplaces, SSO, Bugbot, automations, and spend controls for repeated org use. | https://cursor.com/docs/account/teams/setup |
| II.1 | 1.00 | Bugbot reviews every PR update. PR Routing assigns reviewers and can approve low-risk PRs. Security Agents scan on PR or cron. Rollouts watches each change through deploy. Automations take each trigger to a comment, approval, Slack message, or PR. Humans set the mandate. | https://cursor.com/docs/approval-agents |
| II.2 | 1.00 | Automations run cloud agents with no manual input. Bugbot and PR Routing move from trigger to posted result, waiting on other reviewer checks when configured. Run Everything removes local approval prompts; that is an org choice, not a required step. | https://cursor.com/help/ai-features/automations |
| II.3 | 1.00 | During a run the agent selects granted tools: shell, repo edits, computer use, PR comment/approval, Slack, MCP, and built-in subagents. Toolbox binding is setup, not per-call coordination. | https://cursor.com/docs/cloud-agent/automations |
| II.4 | 1.00 | A service-account automation has its own principal, default cross-run `MEMORIES.md`, team permissions, and `cursor` GitHub identity. Saved environments, secrets, and short-lived OIDC tokens provide controlled access. VMs are per run; actor state is not. | https://cursor.com/docs/cloud-agent/automations |
| II.5 | 1.00 | Run history, transcripts, artifacts, Rollouts attention states, and Bugbot/Security analytics are observable. Risk thresholds escalate. Follow-ups, desktop takeover, and disable stop or redirect work. Enterprise audit logs and SIEM cover admin actions. | https://cursor.com/docs/rollouts |
| II.6 | 1.00 | Cron, GitHub/GitLab/Bitbucket events, Slack, Linear, Sentry, PagerDuty, and webhooks start runs. Cloud agents continue in the background. Subscriptions wake the same agent for up to 180 days. | https://cursor.com/docs/cloud-agent/automations |
| III.1 | 0.75 | Review, low-risk approval, scanning, and deploy monitoring run without a person in the routine steps. Shipping still stops short: Rollouts will not merge, revert, or roll back, and Fix starts only when a person clicks it. | https://cursor.com/docs/rollouts |
| III.2 | 0.75 | A Project coordinator plans work and delegates fixes from Slack, PRs, CI, or a schedule without a new prompt. Projects is rolling out and unavailable on Enterprise. Automations only execute work a trigger already queued. | https://cursor.com/docs/agent/projects |
| III.3 | 0.75 | PR Routing waits for Bugbot and Security Agent checks and uses their findings. That is direct coordination among a bounded set of managed agents. Subagents cooperate only inside one run. | https://cursor.com/docs/approval-agents |
| III.4 | 0.50 | Memories can carry notes into the next run if the prompt uses them. CI autofix retries one agent-authored PR. Rollouts evaluates telemetry and opens an issue; it does not change later rollout decisions from that result. | https://cursor.com/docs/cloud-agent/capabilities |
| III.5 | 0.75 | The Project coordinator changes how many agents it runs and what they do as signals arrive. That is rolling out and project-scoped. Automations follow a human-written prompt and do not rewrite how work is organized. | https://cursor.com/docs/agent/projects |
| III.6 | 1.00 | Admins keep SSO/SCIM, spend limits, repo and model restrictions, hooks, and audit. Approval policies and risk thresholds block auto-approval. Irreversible merge and rollback stay human. | https://cursor.com/docs/enterprise/compliance-and-monitoring |

- **Completed floor:** 2
- **Next Type raw progress:** 0.75
- **Weakest criterion:** 0.50 (III.4)
- **Weakest-link penalty:** 0.09 (0.25 × 0.50 × 0.75)
- **Adjusted progress:** 0.66
- **Final score:** **2.7**

### What prevents the next Type?

3.0 needs every Type III criterion at 1.00. These are still short:

- **III.1** — Routine delivery is not human-free. Managed agents finish review, low-risk approval, scans, and health checks. They do not merge, roll back, or start remediation on their own.
- **III.2** — GA automations consume a queue. Only the rolling-out Project coordinator, absent on Enterprise, decides what work to start and assigns it.
- **III.3** — Actor coordination is the review pipeline, not general delegation among persistent actors.
- **III.4** — Evaluated outcomes do not natively change later operations. Memory and CI retry are primitives, not a closed operational loop.
- **III.5** — The product does not adapt organizational orchestration. Replanning is limited to a rolling-out project, and automations stay on human-written instructions.

## Execution coverage

I'll follow the evaluation skill and rate only the product in `specs/cursor.md`.

The spec is large, so I'll read it in sections and use only its cited sources.

The spec frames Cursor as a coding agent. I'll check the cited docs for shared work, system reach, surfaces, and ready-made jobs before scoring.

Shared runs and write-back are the unclear grades. I'll read those cited pages next.

**Execution coverage: 0.42 / 1.00**

Cursor, as documented on 2026-09-28 and evaluated on 2026-09-29, is a hosted coding agent (desktop, Agents Window, CLI, web, iOS, and cloud). This rating uses the strongest current Teams and Enterprise setup. Grok Bot and Origin are out of scope. An organization can put software work on it: edit a repo, review pull requests, run security checks, and start agents from Slack, Teams, Linear, or Jira. Other company functions have no native path.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| E.1 | 0.25 | Coding agent for repos, plans, edits, reviews, and bugfixes. Linear drops non-development work. Design Mode, Bugbot, and Security Agents stay in software engineering. | https://cursor.com/docs/agent/overview, https://cursor.com/docs/integrations/linear |
| E.2 | 0.75 | Teammates with repo access can open a cloud run read-only. Admin-gated team follow-ups let others message that run. Slack threads can steer it under the same gate. Live collaboration is limited, not default multiplayer. | https://cursor.com/docs/cloud-agent, https://cursor.com/docs/cloud-agent/settings, https://cursor.com/docs/integrations/slack |
| E.3 | 0.75 | Sign-in integrations read and write GitHub/GitLab pull requests and reviews, Slack messages, Linear status, and Jira progress. No shipped mail, CRM, calendar, or general file jobs. Notion write-back is beta. | https://cursor.com/docs/bugbot, https://cursor.com/docs/cloud-agent/automations, https://cursor.com/docs/integrations/jira, https://cursor.com/docs/integrations/linear |
| E.4 | 0.25 | First-party and team marketplaces install plugins, skills, and MCP. Members can publish skills. The catalog stays inside the coding agent. | https://cursor.com/docs/plugins |
| E.5 | 1.00 | Work runs in the IDE, Agents Window, CLI, cursor.com/agents, and iOS, plus Slack and Teams threads, and the TypeScript/Python SDK. Cloud Agents API is beta and is not required for this grade. | https://cursor.com/docs/cloud-agent, https://cursor.com/docs/cli/overview, https://cursor.com/docs/integrations/slack, https://cursor.com/docs/integrations/microsoft-teams, https://cursor.com/docs/sdk/typescript |
| E.6 | 1.00 | Documented install and sign-in, team creation, invites, domain join, SSO, unpaid admin, and Enterprise permissions. A team can put a repo on it without assembling the core. | https://cursor.com/docs/get-started/quickstart, https://cursor.com/docs/account/teams/setup, https://cursor.com/docs/enterprise |
| E.7 | 0.25 | Bugbot, Security Agents, PR routing, Rollouts, marketplace automation templates, and `/automate` are ready-made or generated coding jobs. They do not cover other business functions. | https://cursor.com/docs/bugbot, https://cursor.com/docs/security-agents, https://cursor.com/docs/cloud-agent/automations |

* **Raw mean:** 0.61 (4.25 / 7 = 0.6071)
* **Weakest criterion:** 0.25
* **Weakest-link penalty:** 0.19 (0.25 × 0.75 = 0.1875)
* **Uncapped score:** 0.42 (0.6071 − 0.1875 = 0.4196)
* **Span cap:** 0.49, because E.1 is 0.25 or lower
* **Final score:** **0.42**

### What most limits coverage?

E.1, E.4, and E.7 are 0.25. Only software-engineering work fits. The marketplace and shipped jobs stay in that craft, so sales, support, finance, and other functions have no native path. The span cap does not lower the score further.
