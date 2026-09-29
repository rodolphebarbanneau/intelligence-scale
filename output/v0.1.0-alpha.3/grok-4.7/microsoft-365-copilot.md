## Intelligence Scale type

I'll follow the evaluation skill and rate only the product in the spec.

The skill is loaded. Next I’ll read the product brief and the rest of the scoring rules.

The brief names Microsoft 365 Copilot. I’ll verify the cited pages that decide process ownership, not marketing claims.

**Intelligence Scale capability: 1.6 / 3.0**

Type I with partial progress toward Type II.

Evaluated 2026-09-29. Configuration: Microsoft 365 Copilot (Premium) for work or school, including generally available Cowork under a usage-based spending policy. Copilot Studio as a separate maker product, consumer Copilot, Security Copilot, and GitHub Copilot are out of scope. Model choice does not affect the score.

People still execute. Copilot is embedded in Microsoft 365 and can finish bounded multi-step tasks. It does not put a persistent AI actor in charge of a business process.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| I.1 | 1.00 | Copilot sits in Word, Excel, PowerPoint, Outlook, Teams, OneNote, SharePoint, Edge, and the Copilot app. | https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview |
| I.2 | 1.00 | Premium grounds on Graph and Work IQ within the user's permissions, plus Copilot Search and connectors. | https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview |
| I.3 | 1.00 | Cowork (GA) works through steps: mail, calendar, Office files, Teams, search, research. Excel edit mode makes multi-step workbook changes. | https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/ |
| I.4 | 1.00 | People start, interrupt, pause, resume, cancel, and approve sensitive actions. Excel plan mode confirms first. | https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/ |
| I.5 | 1.00 | Licensed org product: admin controls, usage reports, organizational prompts, notebooks, scheduled prompts, Purview history. | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-controls/overview |
| II.1 | 0.25 | Unit of work is a task a person or one event dispatches (scheduled prompt, one mail, one Teams message). No actor owns a case queue. SharePoint workflows are still public preview. Unprompted custom engine agents need separate hosting. | https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/ |
| II.2 | 0.75 | A Cowork run moves through its steps on its own. Send and schedule pause for approval by default; session skip exists. Standing removal for unattended runs is not shown. | https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/ |
| II.3 | 1.00 | During a run, Cowork selects granted skills (mail, calendar, Office, Teams, search, files) and admin-deployed plugins. No person places each call. | https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/ |
| II.4 | 0.50 | Automations and notebooks persist, but runs use the creating user's identity. The task environment is temporary and removed when the task ends. No actor principal or own credentials. Memory is Frontier preview. | https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance |
| II.5 | 0.75 | Sessions show steps, risk approvals, and pause/cancel. Scheduled and event runs have approval defaults and unified audit logging. No exception queue or live stop for background runs beyond those defaults. | https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance |
| II.6 | 1.00 | Schedules and event triggers (mail or Teams messages) start tasks with no person starting each run. Work continues in the service. | https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/ |
| III.1 | 0.25 | Recurring tasks can repeat bounded work. People still define it; org-wide operations are not autonomous. | https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/ |
| III.2 | 0.00 | No capability to decide the next operational work or allocate it. Step breakdown stays inside a requested task. | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-overview |
| III.3 | 0.25 | Agent-to-agent delegation is on separately hosted custom engine agents and the separately billed Work IQ API, not native Copilot actors. | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-overview |
| III.4 | 0.00 | No detect-decide-execute-observe-evaluate loop that changes later operations. | https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/ |
| III.5 | 0.00 | No ability to reorganize work when conditions change, beyond the requested task. | https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/ |
| III.6 | 0.50 | Admins have spending policy, Conditional Access, Purview, labels, and agent lifecycle. Those controls do not sit over operators who execute without routine human dispatch. | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-controls/overview |

* **Completed floor:** 1
* **Next Type raw progress:** 0.71 (4.25/6 = 0.7083)
* **Weakest criterion:** 0.25 (II.1)
* **Weakest-link penalty:** 0.13 (0.25 × 0.75 × 0.7083 = 0.1328)
* **Adjusted progress:** 0.58 (0.5755)
* **Final score:** **1.6**

### What prevents the next Type?

Crossing 2.0 needs every Type II criterion at 1.00. The blocking gaps are:

* **II.1** — No persistent actor that takes each case from a queue or channel and carries it to an outcome across runs.
* **II.4** — No durable actor with its own principal, credentials, permissions, and execution environment.
* **II.2** — Unattended runs still stop on approval defaults for routine sends and schedules.
* **II.5** — Background runs lack a full observe, exception, and intervene loop beyond approval defaults and audit.

## Execution coverage

I'll follow the evaluation skill and rate only Microsoft 365 Copilot from the spec.

The spec is large, so I’ll read it in sections and use only its cited sources.

The brief is Microsoft 365 Copilot. I’ll check cited docs for shared work, catalogs, surfaces, and ready-made jobs before scoring.

Web fetch was blocked, so I’ll pull the cited Microsoft docs with curl and check how shared work is documented.

**Execution coverage: 0.72 / 1.00**

Microsoft 365 Copilot (Premium), evaluated 2026-09-29, is the licensed work product inside Microsoft 365, including generally available Cowork for work or school accounts. People in many functions can draft, analyze, mail, meet, search, and run multi-step jobs on files, mail, calendar, and Teams. That work stays inside one vendor suite. Preview items (SharePoint Copilot, Frontier memory and App skill, federated write-back) do not raise grades.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| E.1 | 0.75 | Several functions ship today: Word, Excel, PowerPoint, Outlook, Teams, search, Researcher, and Cowork. The product sits inside Microsoft 365, so work outside that suite has no native path. Connector names do not widen span. | https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview |
| E.2 | 0.75 | Shared agents exist: site agents can be shared in Teams or Copilot Chat, and admins assign agents to groups. No documented run where several people and the operator share one thread, hand off, and see the same state. Shared Office files are not a shared Copilot session. | https://support.microsoft.com/en-US/SharePoint/copilot-in-sharepoint/get-started-with-agents-in-sharepoint |
| E.3 | 0.75 | Shipped read and write covers mail, calendar, files, and Teams (Outlook triage and scheduling; Cowork sends mail, edits OneDrive or SharePoint files, posts in Teams). External connectors are read-heavy. Federated write-back is dated early October 2026, so it does not count. | https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/ |
| E.4 | 0.75 | Agent Store is a first-party directory. Microsoft, partners, and customer organizations can publish, and users install across Teams and Office apps. The catalog is the Microsoft 365 suite store, not an open cross-suite marketplace. | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-agent-store |
| E.5 | 0.75 | Work already happens in the Copilot app (web, desktop, mobile), Teams, Outlook, and Word, Excel, and PowerPoint. Those are several surfaces, all one suite’s apps. The separate Work IQ API is not treated as an extra workplace. | https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-app-overview |
| E.6 | 1.00 | Admins assign the add-on on many eligible plans, use Copilot controls and an AI Administrator role, and follow a documented setup guide. Permissions follow the user’s Graph access, Conditional Access, and sensitivity labels. No core assembly is required. | https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-licensing |
| E.7 | 0.75 | A non-specialist can turn on in-app Copilot, preinstalled Researcher and Analyst, Cowork skills (mail, scheduling, briefing, research), and store agents. That covers several functions, limited to this suite. Frontier app generation is preview and does not lift the grade. | https://learn.microsoft.com/en-us/microsoft-365/copilot/researcher-agent |

* **Raw mean:** 0.79
* **Weakest criterion:** 0.75
* **Weakest-link penalty:** 0.06
* **Uncapped score:** 0.72
* **Span cap:** none
* **Final score:** **0.72**

### What most limits coverage?

E.1, E.2, E.3, E.4, E.5, and E.7 all stop at 0.75. The product is bound to Microsoft 365: no native path for work that does not live in that suite, no shipped write-back to external systems of record, a suite-only agent catalog and surfaces, and ready-made jobs that stay inside those apps. Shared agents can be assigned or opened in Teams, but a joint run with the operator in the same thread is not documented.
