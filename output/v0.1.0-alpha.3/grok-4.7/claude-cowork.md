## Intelligence Scale type

I'll follow the evaluation skill and rate only the product in the spec.

The skill and spec are long, so I’ll read them in sections and follow the skill exactly.

The skill and spec continue past the first section. I’ll finish both before scoring.

The spec is the brief. I’ll check the cited pages that decide process ownership, persistence, and triggers.

Help Center pages came back as HTML. I’ll extract the article text and check architecture, projects, and permissions.

**Intelligence Scale capability: 1.7 / 3.0**

Type I with partial Type II capabilities. Evaluated 2026-09-29 from the Cowork spec (reviewed 2026-09-28) and cited docs. Strongest supported configuration is paid Cowork (Pro, Max, Team, Enterprise) on Claude Desktop, with cloud sessions, schedules, connectors, skills, and plugins. Computer use and Dispatch are beta and are not treated as the ceiling.

Cowork natively assists and then executes bounded multi-step tasks: files, connectors, code, and optional browser or computer use, with a person steering and approving. Scheduled tasks rerun a saved prompt in the background. That is not an operator that owns each case of a business process. Sessions act as the signed-in user; sandboxes are destroyed at the end of the run.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| I.1 | 1.00 | Paid desktop, web, mobile, and Chrome side panel embed Cowork in ordinary Claude work, not an isolated API call. Web and mobile are beta; desktop task execution is the supported product. | https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile |
| I.2 | 1.00 | Local folders, directory connectors, skills, and plugins are first-class. Claude reads and writes files and can act in connected apps. Custom MCP is extra, not the only path. | https://claude.com/docs/cowork/overview |
| I.3 | 1.00 | A person states an outcome; Claude plans and finishes multi-step work (documents, spreadsheets, research), including parallel sub-tasks. | https://claude.com/docs/cowork/overview |
| I.4 | 1.00 | People start, steer, and review tasks; Manual, Auto, and Skip control approvals; deletions always need Allow; in-place edit and delete exist. | https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork |
| I.5 | 1.00 | Projects, skills, required org plugins, and scheduled tasks make the same setup repeatable. Team and Enterprise can disable Cowork and set egress and permissions. | https://claude.com/docs/cowork/guide/projects |
| II.1 | 0.50 | Scheduled tasks are a trigger engine: each run is its own session executing a saved prompt. No persistent actor takes cases from a channel or queue. Dispatch (limited beta) still starts from one human brief and splits it into child tasks. | https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork |
| II.2 | 1.00 | Once a run starts, Claude moves through steps, tools, and retries. Auto and Skip are available, so per-step approval is the organization's choice. Deletion approval is an exception, not routine orchestration. | https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork |
| II.3 | 1.00 | During a run Claude selects granted connectors, skills, files, code, plugins, and sub-agents without a person placing each call. Browser rollout and beta computer use are additional tools, not the only path. | https://claude.com/docs/connectors/getting-started |
| II.4 | 0.50 | Projects keep instructions and project memory; cloud sessions can resume. There is no actor principal. Connector tokens stay server-side under the member; each sandbox is created at start and destroyed at end. | https://support.claude.com/en/articles/14479288-claude-cowork-architecture-overview |
| II.5 | 1.00 | People see status and transcripts, get approval and input prompts, steer or delete, and are notified. Team and Enterprise add OpenTelemetry and the Compliance API. Auto mode means routine steps need not be executed by a person. | https://claude.com/docs/cowork/monitoring |
| II.6 | 0.75 | Cadence schedules (hourly through weekly) start remote runs while the computer is closed. No event, webhook, or queue trigger is documented. Cloud sessions are labeled beta. | https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork |

* **Completed floor:** 1
* **Next Type raw progress:** 0.79 (4.75 / 6 = 0.7917)
* **Weakest criterion:** 0.50 (II.1 and II.4)
* **Weakest-link penalty:** 0.10 (0.25 × 0.50 × 0.7917 = 0.0990)
* **Adjusted progress:** 0.69
* **Final score:** **1.7**

### What prevents the next Type?

Type II fails three criteria, so the score stays below 2.0.

* **II.1:** No first-class actor owns a process and takes each case from a trigger, channel, or queue across runs. The unit of work is a task or a repeated prompt.
* **II.4:** No durable operator with its own principal, credentials, permissions, and execution state. Memory and projects are user or project configuration; the sandbox does not persist.
* **II.6:** Schedules only. A new case in an app does not start a run by itself.

## Execution coverage

I'll follow the evaluation skill and rate only the product in the spec.

The skill is loaded. Next I’ll read the product brief and score only what it documents.

The brief is large, so I’ll read it in sections and stick to its cited sources.

I’ll check the cited docs for span, sharing, connectors, and the catalog before scoring.

The product page didn’t return usable docs. I’ll pull the cited help and catalog pages directly.

**Execution coverage: 0.70 / 1.00**

Claude Cowork, evaluated 2026-09-29 on the strongest supported paid configuration (Pro, Max, Team, Enterprise). Desktop on macOS and Windows is the full experience. Cloud sessions, web, and mobile are beta and are not graded above that limit. An organization can put general knowledge work on it today: multi-step tasks that return documents, spreadsheets, presentations, research, and organized files, plus scheduled runs. The run itself stays single-player.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| E.1 | 1.00 | General agentic workspace, not one craft or one suite. People across functions can put their own work on it: local files, research, Excel, PowerPoint, and formatted documents. Finance plugins and a contracts demo are examples, not the span limit. | [Overview](https://claude.com/docs/cowork/overview), [Get started](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork), [Product](https://claude.com/product/cowork) |
| E.2 | 0.50 | Team and Enterprise accounts exist. Sessions cannot be shared. Artifact sharing is after the fact. Current project docs say Cowork projects are not shared; Help claims Team and Enterprise view/edit sharing. That conflict is not credited. Phone alerts are notifications only. | [Get started](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork), [Projects](https://claude.com/docs/cowork/guide/projects), [Team and Enterprise](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans) |
| E.3 | 0.75 | Native read/write of local files. Directory connectors reach calendar, documents, and issue trackers and can take actions; documented examples are reads, so write-back is incomplete. Browser can click, type, and fill forms while Desktop is open (rolling out). Computer use is beta and Pro/Max only, not Team or Enterprise. | [Connectors](https://claude.com/docs/connectors/getting-started), [Overview](https://claude.com/docs/cowork/overview), [Browser](https://support.claude.com/en/articles/16607400-use-the-built-in-browser-in-claude-cowork), [Computer use](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork) |
| E.4 | 1.00 | First-party plugin marketplace and connectors directory, not limited to one craft or suite. Anthropic, partners, and paid accounts can publish; organizations can upload plugins or add a Git marketplace. | [Plugins](https://claude.com/docs/cowork/guide/plugins), [Directory](https://claude.com/docs/connectors/directory), [Skills](https://claude.com/docs/skills/overview) |
| E.5 | 0.75 | Desktop is generally available. Web, mobile, and the Chrome side panel also start Cowork sessions, but web and mobile are beta and the side panel is still rolling out. No documented workplace-chat, mail, or customer-channel surface, and no public work API or embed. Slack is a connector, not a surface. | [Surfaces](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile), [Get started](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork) |
| E.6 | 1.00 | Paid plans include Cowork. Desktop install and get-started path are documented. Team Cowork is on by default, with owner controls for access, connectors, plugins, and permissions. Enterprise can disable it and must opt in to cloud sessions; local desktop use does not require a services build. | [Team and Enterprise](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans), [Product](https://claude.com/product/cowork), [Pricing](https://claude.com/pricing) |
| E.7 | 0.75 | A non-specialist can describe an outcome, review a plan, and get a finished file, or confirm a scheduled task Claude drafts. Excel, Word, PowerPoint, and PDF skills ship and auto-invoke. Installed finance plugins cover one department family and still need provider credentials. Generation saves a prompt and cadence; it does not hand back a reviewed job with tools bound. | [Skills](https://claude.com/docs/skills/overview), [Schedule](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork), [FSI plugins](https://claude.com/docs/office-agents/fsi-plugins) |

* **Raw mean:** 0.82
* **Weakest criterion:** 0.50
* **Weakest-link penalty:** 0.13
* **Uncapped score:** 0.70
* **Span cap:** none
* **Final score:** **0.70**

### What most limits coverage?

E.2 is the gap that sets the penalty. A teammate cannot join the same Cowork session as the operator. Sharing is a later artifact link, and the current project docs still say projects are not shared. Write-back to named systems of record is not documented as shipped jobs, web and mobile remain beta, and ready-made jobs are a reviewed prompt or a finance plugin rather than a turn-on job for several functions.
