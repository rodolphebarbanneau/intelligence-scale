## Intelligence Scale type

I'll follow the evaluation skill and rate only the product in `specs/notion.md`.

The skill and Notion brief are long. I'll read the rest of the scoring rules and the spec in sections.

Custom Agents look like the Type II boundary. I'll check the cited help pages before scoring ownership, persistence, and supervision.

The help pages confirm background agents with their own permissions. I'll check memory, credentials, and whether runs finish without a person between steps.

**Intelligence Scale capability: 1.9 / 3.0**

Approaching Type II.

Evaluated 2026-09-29. Scope is Notion AI on Business and Enterprise, strongest current configuration: Custom Agents with native Notion, Slack, Mail, and Calendar access, plus Enterprise admin controls. Beta wraps (Claude and Cursor external agents, Workers, Meeting Notes, image generation) are not used to raise scores.

Notion AI is embedded in pages, search, and chat, so people can execute with AI help. Custom Agents go further: a named actor with its own Notion permissions can take triggered cases (mail, Slack, database, calendar, schedule) to an outcome in the background. That is real delegation. It is not yet Type II. Those actors have no documented memory across runs, external actions use the authenticator’s credentials, and supervision is logs, optional approvals, and stop controls rather than delivered exceptions. People still define each process. The product does not orchestrate the organization.

| Criterion | Grade | Evidence | Source |
| --- | ---: | --- | --- |
| I.1 | 1.00 | Notion Agent, inline edit, AI blocks, and search sit in the workspace, not a side experiment. | https://www.notion.com/help/notion-agent |
| I.2 | 1.00 | The agent uses the current page, workspace, files, connectors, and MCP apps the person can already access. | https://www.notion.com/help/notion-agent |
| I.3 | 1.00 | It runs multi-step work: pages, databases, Slack posts, inbox actions, and a code workspace for files. | https://www.notion.com/help/notion-agent |
| I.4 | 1.00 | People direct chat, accept or discard inline edits, confirm Gmail writes, and set instructions. | https://www.notion.com/help/notion-ai-faqs |
| I.5 | 1.00 | Business and Enterprise include shared skills, admin controls, a usage allowance, and team agents. | https://www.notion.com/help/custom-agents |
| II.1 | 1.00 | A Custom Agent keeps taking each triggered case (mail, Slack, database, calendar, schedule) to an action. People set the mandate. | https://www.notion.com/help/custom-agents |
| II.2 | 1.00 | Published runs continue in the background, including sub-agent handoff. Mail, calendar, and MCP confirmation can be turned off. | https://www.notion.com/help/connect-mail-to-custom-agents |
| II.3 | 1.00 | One run can use granted Notion pages, Slack, Mail, Calendar, web, and other Custom Agents without a person placing each call. | https://www.notion.com/help/custom-agents |
| II.4 | 0.75 | Own Notion principal, permissions, settings, and activity log. Cross-run memory is undocumented. Mail, Calendar, and MCP use the authenticator’s credentials. | https://www.notion.com/help/custom-agents-sharing-and-permissions |
| II.5 | 0.75 | Activity logs, optional approvals, disable/pause, and Enterprise audit exist. Exception delivery and in-run takeover are not documented. | https://www.notion.com/help/custom-agents |
| II.6 | 1.00 | Schedules plus Notion, Slack, Mail, and Calendar events start background runs. A person does not start each one. | https://www.notion.com/help/custom-agents |
| III.1 | 0.50 | Unattended work runs only for agents people design, scope, and publish. | https://www.notion.com/help/custom-agents |
| III.2 | 0.25 | Handoff follows instructions a person wrote. The agent does not decide what work should exist. | https://www.notion.com/help/custom-agents |
| III.3 | 0.25 | A primary agent can call other Custom Agents it was given, inside that designed workflow. | https://www.notion.com/help/custom-agents |
| III.4 | 0.00 | Triggers, actions, and logs do not show outcome evaluation changing later decisions. | https://www.notion.com/help/custom-agents |
| III.5 | 0.00 | Agents follow written instructions and filters. They do not change the process when conditions change. | https://www.notion.com/help/custom-agents |
| III.6 | 0.50 | Admins can pause agents, cap credits, set creation policy, and audit. Routine agent maintenance is still the designed human role. | https://www.notion.com/help/manage-custom-agents-with-the-admin-api |

* **Completed floor:** 1
* **Next Type raw progress:** 0.92
* **Weakest criterion:** 0.75
* **Weakest-link penalty:** 0.06
* **Adjusted progress:** 0.86
* **Final score:** **1.9**

### What prevents the next Type?

Type II is blocked by II.4 and II.5. Custom Agents need documented memory the actor carries across triggered runs, and credentials of their own for external systems rather than the authenticator’s Mail, Calendar, and MCP login. Supervisors also need a native way to receive exceptions and intervene in a run, not only read Activity after the fact or disable the agent.

## Execution coverage

I'll follow the evaluation skill and rate only the product in the spec.

The Notion spec is large, so I’ll read it in sections and use only that brief.

I’ll check the cited help pages for shared work, connectors, catalogs, and ready-made jobs before scoring.

**Execution coverage: 0.66 / 1.00**

Notion AI, on Business and Enterprise as of 2026-09-29, is the hosted AI inside a Notion workspace. People across functions can write, search, run databases, handle mail and calendar, and run shared agents there. It is still one vendor suite, not a company-wide surface outside Notion. Beta items (AI Meeting Notes, image generation, Workers, external agents, Jira) are not treated as full coverage.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| E.1 | 0.75 | Writing, databases, search, research, mail, calendar, and meetings fit today, across more than one function. The product only works inside the Notion workspace, which the rubric treats as one suite. | https://www.notion.com/help/notion-ai-faqs |
| E.2 | 0.75 | Custom Agents are shared teammates with their own access. People can interact, @mention them in pages, comments, and Slack, and agents can hand work to other agents. Chat is a private or shared 1:1; Activity is a log, so live multi-person collaboration in one thread is limited. | https://www.notion.com/help/custom-agents |
| E.3 | 1.00 | Documented read and write for mail (Gmail, Outlook, Notion Mail: draft, send, archive, labels), calendar (Google, Apple, Outlook, Notion Calendar: create, update, cancel, invite, RSVP), and Slack (search, post, reply, react). Drive, SharePoint, and Jira stay search-oriented; MCP names are not counted as write-back. | https://www.notion.com/help/connect-mail-to-custom-agents |
| E.4 | 0.50 | Skills Library is an in-workspace directory. Custom Agents can start from an official template. Pre-configured MCP is a connector list. No marketplace where the vendor, third parties, and other customers publish installable jobs. | https://www.notion.com/help/create-and-manage-skills |
| E.5 | 0.75 | Work runs in the Notion web, desktop, and mobile apps, and a Custom Agent can be mentioned and reply in Slack. In-page embed stays inside Notion. No mail-client or customer-channel surface, and the Admin API governs agents rather than carrying the work. | https://www.notion.com/help/custom-agents |
| E.6 | 1.00 | Business and Enterprise document Settings → Notion AI, agent permissions, creation policy, an Agent Directory, credits, and a first-agent walkthrough. Ordinary teams can put work on it without assembling a platform. Free and Plus only get complimentary responses. | https://www.notion.com/product/ai |
| E.7 | 0.75 | Shipped writing skills, Autofill, Enterprise Search, and Research Mode are on. Agents can be generated from a description or started from a template, then reviewed. Access still has to be granted, and jobs stay inside the Notion suite. AI Meeting Notes is beta. | https://www.notion.com/help/custom-agents |

* **Raw mean:** 0.79
* **Weakest criterion:** 0.50
* **Weakest-link penalty:** 0.13
* **Uncapped score:** 0.66
* **Span cap:** none
* **Final score:** **0.66**

### What most limits coverage?

E.4 is the weakest grade. There is no cross-organization catalog of finished agents or workflows; growth is workspace skills, official templates, and connectors. The same Notion-suite boundary keeps span and ready-made jobs at 0.75, and agent chat stays 1:1 rather than a shared live run.
