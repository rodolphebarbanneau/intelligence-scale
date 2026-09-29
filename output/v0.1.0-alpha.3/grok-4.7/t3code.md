## Intelligence Scale type

I'll follow the evaluation skill and rate only the product in the spec.

The skill and spec are large, so I’ll read them in sections.

The skill and spec continue past the first section. I’ll read the rest before scoring.

The brief is a coding-agent harness. I’ll check how this repo scores wraps and open the cited docs that bear on process ownership.

I’ll verify the cited docs for triggers, persistent actors, and what the harness actually surfaces of each agent.

I’ll open the cited docs that decide whether this harness owns a process or only steers person-started coding tasks.

**Intelligence Scale capability: 1.6 / 3.0**

Type I with early Type II capabilities.

Evaluated 2026-09-29. Subject is T3 Code stable `v0.0.42` (spec reviewed 2026-09-28): an open-source harness with no plan of its own. Strongest supported setup is a local server steering Claude Code, Codex, or Cursor in Full access, with web, desktop, and mobile clients. People still own the engineering process and dispatch each thread. Once a thread starts, the wrapped agent can finish a multi-step coding task, use the tools it was granted, and be supervised, including in the background. Cloud automations on those providers’ own surfaces are not credited; T3 Code does not document starting or steering them.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| I.1 | 1.00 | Desktop, web, and mobile clients start and steer coding agents on the environment machine as ordinary development work, not a one-off API call. | https://github.com/pingdotgg/t3code/blob/main/README.md |
| I.2 | 1.00 | Threads attach files, terminal excerpts, review comments, and pull requests. Agents use the workspace, Git hosts, skills, browser integration, and device tools. | https://github.com/pingdotgg/t3code/blob/main/docs/user/composer.md |
| I.3 | 1.00 | A composer task runs as a provider turn: tool calls, edits, commands, questions, and pull-request linking. Full access can skip per-step approval. | https://github.com/pingdotgg/t3code/blob/main/docs/user/permission-modes.md |
| I.4 | 1.00 | People send, queue, or steer prompts; approve or reject; answer questions; stop, rewind, and revert; and review diffs and pull requests. | https://github.com/pingdotgg/t3code/blob/main/docs/user/composer.md |
| I.5 | 1.00 | Threads, project settings, provider logins, and `t3.json` scripts persist on the server across clients. A user service can keep the server up. | https://github.com/pingdotgg/t3code/blob/main/docs/user/background-service.md |
| II.1 | 0.25 | Each unit is a person-started thread (one change). No actor takes cases from a queue, channel, or trigger and owns that process across runs. Worktree scripts are shell hooks, not process ownership. | https://github.com/pingdotgg/t3code/blob/main/docs/user/thread-sidebar.md |
| II.2 | 1.00 | In Full access (the default) or provider Auto, a started turn moves through tool calls, branches, and retries with no person between steps. Approvals are optional. Task-vs-process is not charged here. | https://github.com/pingdotgg/t3code/blob/main/docs/user/permission-modes.md |
| II.3 | 1.00 | During the turn the agent selects granted provider tools and skills and, when enabled, browser access and `device_*` tools. No person coordinates each call. | https://github.com/pingdotgg/t3code/blob/main/docs/user/devices.md |
| II.4 | 0.50 | Threads and provider homes are resumable sessions on the person’s login. There is no actor principal with its own permissions or credentials. | https://github.com/pingdotgg/t3code/blob/main/docs/internals/overview.md |
| II.5 | 1.00 | Live tool output, subagent view, in-thread approvals, mobile alerts for failure, approval, or questions, plus stop, steer, and pull-request review. | https://github.com/pingdotgg/t3code/blob/main/docs/user/mobile-notifications.md |
| II.6 | 0.50 | A person starts every thread. A started run can continue on a background service and be watched from another device. No schedule, webhook, or event trigger is documented. Snooze only parks a thread. | https://github.com/pingdotgg/t3code/blob/main/docs/user/updating.md |

* **Completed floor:** 1
* **Next Type raw progress:** 0.71
* **Weakest criterion:** 0.25 (II.1)
* **Weakest-link penalty:** 0.13
* **Adjusted progress:** 0.58
* **Final score:** **1.6**

### What prevents the next Type?

Crossing 2.0 needs every Type II criterion at 1.00. Three are short:

* **II.1** — No persistent actor takes each case from a trigger, channel, or queue and carries it to an outcome across runs. A person still dispatches every thread.
* **II.4** — No actor principal with its own identity, cross-run memory, permissions, and credentials. Sessions reuse the person’s provider login.
* **II.6** — No schedules or event or webhook triggers that start runs. Only a person-started run continues in the background.

## Execution coverage

I'll follow the evaluation skill and rate only the product in the spec.

The spec is large, so I’ll read it in sections and use only its cited sources.

The spec frames a coding-agent harness. I’ll check the cited docs that decide sharing, reach, catalog, and adoption.

The docs host blocked a couple of fetches. I’ll pull the cited pages another way.

**Execution coverage: 0.04 / 1.00**

Evaluated 2026-09-29. Subject is T3 Code stable `v0.0.42` (spec reviewed 2026-09-28): an open-source harness that starts and steers coding agents already installed on one machine. Desktop, web, and mobile clients attach to that server. It does not resell a model or a company workspace.

An organization can put software-development work on it: a developer drives Claude Code, Codex, Cursor, Grok Build, OpenCode, or Antigravity against a local repo, terminal, and Git host. Other functions have no native path. Other people are not in the run.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| E.1 | 0.25 | Control surface for six coding agents on the person's computer. Wrapping several coding agents does not add another function. Judgment: one specialist craft. | https://github.com/pingdotgg/t3code/blob/main/README.md |
| E.2 | 0.00 | Phone, browser, and another desktop attach to the same person's server. Mobile alerts go to that phone. No team account, shared thread, or handoff with other people. Judgment: single-player. | https://github.com/pingdotgg/t3code/blob/main/docs/user/remote-access.md |
| E.3 | 0.25 | Reads and writes the repo and Git hosts (clone, pull request, review, merge). No shipped read/write of mail, tickets, CRM, files, or calendar. Host CLIs are installed by the user. Judgment: own coding artifacts. | https://github.com/pingdotgg/t3code/blob/main/docs/user/source-control.md |
| E.4 | 0.25 | No marketplace. `t3.json` holds up to 50 buyer-written scripts. `$` selects skills from the provider's folders, not a T3 Code directory. Judgment: builder-assembled extensions inside one craft. | https://github.com/pingdotgg/t3code/blob/main/docs/user/project-settings.md |
| E.5 | 0.50 | Work happens in the desktop app, local or hosted web client, and iOS/Android apps. The CLI launches the server or a desktop thread. No workplace chat, mail, customer channel, or public API/embed. | https://github.com/pingdotgg/t3code/blob/main/docs/user/install.md |
| E.6 | 0.50 | Documented install and a welcome wizard. An individual can start today. No organization administration, seats, or SSO. Pairing and session revoke are the owner's connection controls. | https://github.com/pingdotgg/t3code/blob/main/docs/user/install.md |
| E.7 | 0.25 | Each thread starts from a prompt the person writes. No shipped job, installable finished agent, or builder that generates instructions, tools, and triggers for review. | https://github.com/pingdotgg/t3code/blob/main/docs/user/composer.md |

* **Raw mean:** 0.29 (2.00 / 7 = 0.2857)
* **Weakest criterion:** 0.00 (E.2)
* **Weakest-link penalty:** 0.25
* **Uncapped score:** 0.04 (0.2857 − 0.25 = 0.0357)
* **Span cap:** 0.49, because E.1 is 0.25 or lower
* **Final score:** **0.04**

### What most limits coverage?

E.2 is absent: there is no documented shared run where several people and an operator see the same state and hand work off. Remote access and push alerts stay with one person. E.1 keeps the product inside coding, so the span cap applies even though the penalty already holds the score under 0.49. E.3 never leaves the repository and Git hosts. E.4 has no catalog other people can publish into. E.7 has no ready-made job outside a hand-written coding prompt.
