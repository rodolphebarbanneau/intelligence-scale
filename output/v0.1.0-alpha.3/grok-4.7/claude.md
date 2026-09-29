## Intelligence Scale type

I'll follow the evaluation skill and rate only the product in `specs/claude.md`.

The spec is loaded. Next I’ll read the evaluation skill in sections so I can follow its format exactly.

The brief scopes Claude chat, not Code or Cowork. I’ll check cited docs and the scale’s scoring examples before grading.

Prior scores stay unused. I’ll verify process ownership, triggers, and actor durability in the cited Help Center pages.

The Help Center pages didn’t render as text. I’ll pull the cited articles directly and extract the relevant sections.

I’ll pull the cited Help Center articles that decide process ownership, triggers, and actor durability.

Help Center pages are client-rendered, so I’ll use the sourced spec and pull the sections that decide Type II.

**Intelligence Scale capability: 1.5 / 3.0**

Type I with early Type II capabilities.

Evaluated 2026-09-29 from the Claude chat brief (reviewed 2026-09-28). Strongest supported configuration is paid chat on web, desktop, and mobile, including Claude in Chrome. Claude Code and Cowork-only surfaces are out of scope. Live Help Center pages are client-rendered; grades use the sourced brief.

People still execute. Claude assists inside threads with tools, research, and files. It does not field a worker that owns a business process across cases.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| I.1 | 1.00 | Chat is a supported work surface on web, desktop, and mobile, not an API demo. | https://support.claude.com/en/articles/8114491-get-started-with-claude |
| I.2 | 1.00 | Projects, uploads, web search, memory, skills, directory connectors, and sandboxed code execution are first-party. Custom MCP is not required for this grade. | https://support.claude.com/en/articles/9517075-what-are-projects |
| I.3 | 1.00 | Research iterates searches; code execution builds files; Chrome can click, type, and fill forms inside one bounded session. GA task autonomy does not depend on the beta side panel. | https://support.claude.com/en/articles/11088861-use-research-on-claude |
| I.4 | 1.00 | The person starts, steers, sets model and effort, approves tools, edits artifacts, and continues the thread. | https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features |
| I.5 | 1.00 | Projects, account and project instructions, org-provisioned skills, and shared Team or Enterprise projects make use repeatable. | https://support.claude.com/en/articles/12512176-what-are-skills |
| II.1 | 0.25 | Each unit is a task a person starts, or a schedule fires: one chat, report, file, or browser run. No actor takes cases from a queue across runs. Security (public beta) stops at findings and suggested patches; case triggers are not documented. Judgment. | https://support.claude.com/en/articles/14661296-use-claude-security |
| II.2 | 0.50 | Once research, code execution, or a browser session starts, Claude moves through its own steps. A person still starts the next task. Optional tool approval is not treated as a structural stop. | https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude |
| II.3 | 1.00 | In one run Claude selects search, code, skills, and granted connectors, including Research over Gmail, Calendar, and Docs. Sub-agents do not run in chat; that is not required here. | https://support.claude.com/en/articles/11176164-use-claude-cowork |
| II.4 | 0.50 | Threads, instructions, and memory persist, but Claude uses the person's permissions and connector credentials. No principal or durable actor environment. The code sandbox is per session. | https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context |
| II.5 | 0.75 | Transcript, thinking, tool calls, Always allow / Needs approval / Blocked, and stop-or-correct exist. No exception queue. Audit and Compliance API are Enterprise only. | https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan |
| II.6 | 0.75 | Scheduled recurring browser tasks are one trigger type on the Chrome extension. Event or inbound webhook start of chat runs is not documented. Cowork schedules are out of scope. Security webhooks send findings out; they do not start runs. Judgment. | https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome |
| III.1 | 0.25 | Routine work still needs a person. Unattended behavior is a scheduled browser task or a beta repo scan, not organization-wide operations. | https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome |
| III.2 | 0.00 | Claude does not decide what operational work happens next or assign it. It executes the prompt it was given. | https://support.claude.com/en/articles/8114491-get-started-with-claude |
| III.3 | 0.00 | Plugin sub-agents run in Cowork and Claude Code, not in chat. No persistent actors coordinate. | https://support.claude.com/en/articles/13837440-use-plugins-in-claude |
| III.4 | 0.25 | Inside one run, search and code observe results and continue. Memory personalizes later chats; it does not close an operational loop. | https://support.claude.com/en/articles/11088861-use-research-on-claude |
| III.5 | 0.25 | Claude can change approach inside a chat. It does not reallocate work or rewrite processes. | https://support.claude.com/en/articles/11088861-use-research-on-claude |
| III.6 | 0.25 | Enterprise policy, spend, retention, and tool blocks exist, but they govern an assistant people still operate. | https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan |

- **Completed floor:** 1
- **Next Type raw progress:** 0.625
- **Weakest criterion:** 0.25 (II.1)
- **Weakest-link penalty:** 0.117
- **Adjusted progress:** 0.508
- **Final score:** **1.5**

### What prevents the next Type?

Type II needs every II criterion at 1.00. Missing native capabilities:

- **II.1** — No persistent actor that takes each case from a trigger, channel, or queue and finishes it across runs.
- **II.4** — No durable worker with its own principal, permissions, credentials, and execution state.
- **II.2** — Multi-step tasks finish alone; the product does not advance a process from task to task.
- **II.5** — No exception or escalation path; audit is Enterprise-only.
- **II.6** — Browser schedules only. No event or webhook start of process runs in the background.

## Execution coverage

I'll follow the evaluation skill exactly and rate only the product in the spec.

The spec is the brief. I’ll verify the cited sources that decide span, sharing, reach, catalog, and ready-made jobs.

The help pages didn’t render cleanly. I’ll pull the cited articles directly and use those facts.

Help pages are client-rendered, so I’ll pull the article text from the allowed sources.

**Execution coverage: 0.70 / 1.00**

Evaluated 2026-09-29. Subject is the Claude chat assistant (strongest current Team/Enterprise configuration), not Claude Code or Cowork-only computer use. People across the company can put drafting, research, analysis, and files on it today. Shared projects and connectors exist, but most function jobs are not ready-made.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| E.1 | 1.00 | General assistant on web, desktop, and mobile. Drafting, analysis, research, spreadsheets, decks, and docs fit today. Not one craft or one suite. | [Get started](https://support.claude.com/en/articles/8114491-get-started-with-claude), [Create files](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude) |
| E.2 | 0.75 | Team/Enterprise projects are a shared workspace: view/edit, shared knowledge, members create chats. Chats are not one shared thread with the operator. Share is a snapshot. Live co-editing with Claude is Claude Docs, which is beta. | [Projects](https://support.claude.com/en/articles/9517075-what-are-projects), [Share chats](https://support.claude.com/en/articles/10593882-share-and-unshare-chats), [Claude Docs](https://support.claude.com/en/articles/16923645-get-started-with-claude-docs) |
| E.3 | 0.75 | Research reads Gmail, Calendar, and Google Docs. Connected apps include Drive, Gmail, Microsoft 365, and Slack, and connectors can take actions. Salesforce write-back is beta. Named read-and-write jobs for several systems of record are not fully documented. | [Research](https://support.claude.com/en/articles/11088861-use-research-on-claude), [One Claude](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude), [Connectors](https://support.claude.com/en/articles/11176164-use-claude-cowork), [Salesforce](https://support.claude.com/en/articles/16952186-use-salesforce-in-claude) |
| E.4 | 1.00 | First-party skills directory and plugin marketplaces (Knowledge Work, Life Sciences, Financial Services, Legal). Vendor, partner skills, Git marketplaces, and an organization library can publish. Not one craft. | [Skills](https://support.claude.com/en/articles/12512176-what-are-skills), [Plugins](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) |
| E.5 | 0.75 | Work runs on web, desktop, and mobile, and syncs. Chrome side panel is beta and often a Cowork session. No workplace chat, mail, or in-scope API or embed. | [Get started](https://support.claude.com/en/articles/8114491-get-started-with-claude), [Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome) |
| E.6 | 1.00 | Free start at claude.ai. Team documents seats, SSO, roles, and org controls. Enterprise has a self-serve create path. | [Get started](https://support.claude.com/en/articles/8114491-get-started-with-claude), [Team](https://support.claude.com/en/articles/9266767-what-is-the-team-plan), [Enterprise](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan) |
| E.7 | 0.50 | Shipped document skills and Research, plus beta Docs/Design/Slides templates. Salesforce is one beta sales pack. Domain marketplaces are not itemized as turnkey jobs. No documented job builder. | [Skills](https://support.claude.com/en/articles/12512176-what-are-skills), [Plugins](https://support.claude.com/en/articles/13837440-use-plugins-in-claude), [Salesforce](https://support.claude.com/en/articles/16952186-use-salesforce-in-claude), [Research](https://support.claude.com/en/articles/11088861-use-research-on-claude) |

* **Raw mean:** 0.82
* **Weakest criterion:** 0.50
* **Weakest-link penalty:** 0.13
* **Uncapped score:** 0.70
* **Span cap:** none
* **Final score:** **0.70**

### What most limits coverage?

E.7 is the floor. A team cannot turn on finished jobs for several business functions. Document skills, Research, and beta content templates ship; Salesforce is one beta pack; the other marketplaces are not shown as running jobs. E.2, E.3, and E.5 stay short of native: no shared chat with the operator, incomplete write-back into systems of record, and no workplace-chat, mail, or API surface.
