---
name: evaluate-type-scale
description: Rate an AI product against the Intelligence Scale from 0.0 to 3.0 by answering yes/no checks from its spec. Use when evaluating how far a technology natively enables organizations to shift operational agency from humans to AI across Type I Augmented, Type II Delegated, and Type III Autonomous operating models.
---

# Intelligence Scale Type Evaluator

Rate the **capability ceiling of a technology** against the [Intelligence Scale](https://github.com/rodolphebarbanneau/intelligence-scale).

The scale is:

* **Type I — Augmented:** People execute. AI assists.
* **Type II — Delegated:** AI executes. People supervise.
* **Type III — Autonomous:** AI orchestrates. People govern.

You do not pick grades. You answer yes/no checks, each backed by a verbatim quote from the spec. The scorer turns the checks into grades, applies the caps and gates, and computes the score. That keeps ratings consistent across models and runs.

## 1. Scope

The spec file is the brief and the **only evidence**. Rate the product it names, in the edition and state it describes. Do not browse, and do not use what you remember about the product. A URL in the spec is a citation, not something to open. A capability the spec does not state is unproven, and its check fails.

Rate **one configuration**: the strongest currently available, supported, first-party configuration the spec describes. State it in `configuration`: the product, the plan or edition, and any first-class wrap. Every check must hold in that one configuration. Do not combine features from different plans, editions, or sibling products into one answer. When evidence only holds elsewhere, the `other_plan` limit applies.

This repository rates the **chassis**: the product an organization adopts. It does not rate the **motor**: the foundation model inside it. A documented, first-class wrap of another agent is part of the chassis as this product exposes it. Credit what this product surfaces and adds. Do not import a sibling product's capabilities.

The type score is not coverage. A marketplace, a shared workspace, or many business functions belong to the Execution Scale. A specialist craft tool can reach Type II. A company-wide assistant can stay at Type I.

## 2. Evidence rules

* A check passes only when the spec states the capability. Quote the words that prove it.
* A quote is text copied character for character from the spec. You may join two excerpts of the same passage with `...`. Do not paraphrase, translate, or fix typos. The scorer rejects quotes it cannot find, and the check fails.
* A feature name alone does not prove how it works. When a check asks how something behaves, the quote must say so.
* Marketing words such as "autonomous", "agentic", "operator", or "AI employee" prove nothing by themselves.
* Roadmap, announced, coming-soon, or hypothetical features fail every check.
* "You could build this" is not "the product provides this". A capability available only through a generic API, SDK, webhook, or MCP server the buyer wires triggers the `buyer_wired` limit.
* Beta, preview, experimental, and waitlist capabilities can pass checks. They trigger the `preview` limit.
* When the evidence is ambiguous, the check fails.

## 3. Definitions

* **Task:** one unit of work with one result, such as one change, one reply, one report, or one pull request.
* **Case:** one instance flowing through a process, such as one ticket, one invoice, one lead, or one change request.
* **Business process:** a recurring flow of cases through stages toward a business outcome.
* **Stage:** one step of a process that produces an intermediate artifact, such as triage, a draft, a pull request, or a review.
* **Outcome:** the result the process exists for, recorded in the system where it lives, such as a sent reply, a closed ticket, a merged change, or an updated record.
* **Persistent AI actor:** a named agent, worker, operator, or bot that exists between runs, as opposed to a session or a saved configuration.
* **Principal:** an identity with its own permissions, separate from any person's account.
* **Run:** one execution of the AI, from start to stop.
* **Trigger:** a schedule or an event that starts a run with no person starting it.

## 4. How the scorer grades

Each criterion has four cumulative levels: **0.25**, **0.50**, **0.75**, **1.00**. Each level has one or more checks.

* The base grade is the highest level whose checks all pass, going up from 0.25. A level counts only when every level below it holds.
* The next level adds a share: `0.25 × passed checks ÷ checks at that level`. For example, 0.50 plus one of two 0.75 checks gives **0.62**.
* Each limit that applies caps that criterion at its value.
* Cross-criterion caps then apply, in the order listed below.

Answer **every** check and limit, at every level, even after a lower level fails. The scorer needs all of them.

## 5. Rubric

<!-- rubric:start -->

Common limits. Answer these for every criterion. Each one caps that criterion when it applies:

* `preview` caps at **0.75**: The spec marks the capability behind this criterion's highest passed check as preview, beta, experimental, research preview, early access, or waitlist.
* `buyer_wired` caps at **0.25**: The spec shows this capability only through a generic API, SDK, webhook, or MCP server the buyer must build or wire, not as a shipped feature.
* `other_plan` caps at **0.50**: The evidence for this criterion's highest passed check applies only to a different product, plan, edition, or deployment than the configuration you stated.

Cross-criterion caps. The scorer applies these after grading:

* Owning a process needs a durable actor: II.1 stays at or below 0.50 unless II.4 is at least 0.75.
* Whole-process outcomes need someone to own the process: II.7 stays at or below II.1 + 0.25.
* Orchestration needs process owners to orchestrate: every Type III criterion stays at or below 0.50 unless II.1 is at least 0.75.

### Type I — Augmented

#### I.1 — Routine AI assistance

AI sits in the normal flow of work, not only as an experiment or an API call.

| Level | Check | Passes when |
| ----: | ----- | ----------- |
| 0.25 | `available` | The spec describes AI that people can use for real work tasks in the product. |
| 0.50 | `in_surface` | The AI is available inside a work surface people already use (an app, editor, workspace, inbox, or chat they work in), not only through an API or a separate playground. |
| 0.75 | `acts_in_place` | The AI can act on the work item itself in that surface, such as editing a file, document, record, ticket, or message, not only answering questions about it. |
| 1.00 | `standard_feature` | The spec documents the AI as a standard part of the product for its users, not a lab, demo, or separate experiment. |

#### I.2 — Context and capability access

AI can reach the data and tools real work needs.

| Level | Check | Passes when |
| ----: | ----- | ----------- |
| 0.25 | `session` | The AI can use content provided in the session, such as uploaded files, pasted text, or the open item. |
| 0.50 | `org_context` | The AI can use organizational context beyond the session, such as a workspace, repository, drive, knowledge base, or indexed company data. |
| 0.75 | `actions` | The AI can call tools or take actions in applications or systems, not only read or retrieve. |
| 1.00 | `connectors` | The product ships first-party connectors or integrations to two or more distinct systems, such as mail, files, tickets, CRM, or code hosting. |
| 1.00 | `permissions` | The spec states that the AI's access to data respects the user's or the organization's permissions. |

#### I.3 — Bounded autonomous tasks

AI can run a meaningful multi-step task inside a bounded objective.

| Level | Check | Passes when |
| ----: | ----- | ----------- |
| 0.25 | `multi_part` | The AI can produce a multi-part result from one request, such as a document, a set of edits, or a report. |
| 0.50 | `tool_loop` | The AI can run a task of several steps that uses tools or actions, such as searching, editing, running commands, or operating software. |
| 0.75 | `self_directed` | Within a task, the AI decides the next step from the result of the previous one and continues until the task is done or a stop condition is reached. |
| 1.00 | `effectful` | Within a task, the AI can take effectful actions (write files, run commands, change records, send or post) without a person approving every step. |
| 1.00 | `artifact` | The task ends in a documented, inspectable result, such as a diff, pull request, report, changed record, or run log. |

* Task autonomy is Type I. A long or impressive task does not show that the AI owns a process.

#### I.4 — Human direction and review

People can start, inspect, approve, correct, and continue AI work while owning the broader process.

| Level | Check | Passes when |
| ----: | ----- | ----------- |
| 0.25 | `start_see` | A person can start AI work and see its result. |
| 0.50 | `stop` | A person can stop or interrupt AI work while it runs. |
| 0.75 | `review_before` | A person can review proposed changes or actions before they take effect, such as a plan, a diff, a draft, or an approval prompt. |
| 1.00 | `correct_continue` | A person can correct or redirect the AI's work and have it continue from where it was, not only start over. |

#### I.5 — Repeatable organizational use

The product supports ongoing, repeatable use in real workflows, not one-off demos.

| Level | Check | Passes when |
| ----: | ----- | ----------- |
| 0.25 | `persists` | Work, threads, or results persist so a person can return to them in a later session. |
| 0.50 | `reusable` | People can save reusable configuration, such as instructions, prompts, rules, skills, custom agents, or templates. |
| 0.75 | `shared` | That configuration or work can be shared with a team or organization, not only kept by one person. |
| 1.00 | `managed` | Admins can manage organization-wide settings, policies, or defaults for the AI. |

### Type II — Delegated

#### II.1 — End-to-end process ownership

A named AI actor is put in charge of a business process and keeps taking its cases over time.

| Level | Check | Passes when |
| ----: | ----- | ----------- |
| 0.25 | `dispatched` | A person can hand a whole task to the AI and receive the finished result. |
| 0.50 | `rule_repeats` | A trigger, schedule, or workflow rule makes the AI run the same kind of work repeatedly without a person handing over each run. |
| 0.75 | `named_actor` | A named, persistent AI actor (an agent, worker, operator, or bot that exists between runs) is assigned a process, queue, channel, or role. |
| 0.75 | `own_intake` | That actor takes each new case from its own intake (its queue, channel, inbox, or triggers), rather than a person handing it each case. |
| 1.00 | `standing_mandate` | The actor keeps that responsibility across runs under a standing mandate, handling case after case over time. |
| 1.00 | `exceptions_only` | People handle exceptions or escalations; they do not accept, dispatch, or approve each routine case. |

* A business process is a recurring flow of cases through stages toward a business outcome, such as a support queue, invoice handling, lead follow-up, or change delivery. One change, one reply, or one report is a task.
* A job that runs per artifact (per pull request, commit, scan, or document) is a trigger rule. It meets the 0.50 level, not 0.75.
* Do not fail a check because a person, a template, or the product's builder defined the process. That is the mandate. Fail it when each unit of work is still handed over by a person.
* Whether each case reaches its final outcome is II.7, not II.1.

#### II.2 — Process-level execution

AI progresses the process without a person orchestrating each task or step.

| Level | Check | Passes when |
| ----: | ----- | ----------- |
| 0.25 | `multi_step` | Once started, the AI performs more than one step of the work on its own. |
| 0.50 | `no_person_between` | A multi-step task runs from start to finish with no person required between its steps. |
| 0.75 | `across_stages` | A run moves work across tasks or stages of a process (for example triage, act, verify, hand off) with no person moving it between them. |
| 1.00 | `optional_humans` | Human steps inside a run are configurable or limited to exceptions; the organization can run routine cases without them. |

Limits, on top of the common limits:

* `required_approval` caps at **0.75**: The spec states that a routine step inside the run always requires a person's approval and the organization cannot turn it off.

* Do not fail a check because people wrote the steps, or because optional approval steps exist.
* Output that stops at a draft or an open pull request counts on II.7, not here.

#### II.3 — Multi-capability execution

The actor uses the tools, applications, agents, and systems needed to finish its process.

| Level | Check | Passes when |
| ----: | ----- | ----------- |
| 0.25 | `one_tool` | During a run the AI uses at least one tool or action beyond generating text. |
| 0.50 | `several_tools` | During a run the AI selects among several tools, such as file, shell, and search tools in one environment. |
| 0.75 | `cross_family` | During a run the AI uses capabilities of different kinds, such as separate applications or systems, other agents or subagents, browser or computer use, and connectors. |
| 1.00 | `self_coordinated` | The AI chooses which of its granted capabilities to call and in what order; no person coordinates each call. |

* Granting or binding tools at setup does not fail a check. Every actor is given its access by someone.
* Writes that land only as drafts count on II.7, not here.

#### II.4 — Persistent AI actor

A durable AI worker with its own identity, state, permissions, and access.

| Level | Check | Passes when |
| ----: | ----- | ----------- |
| 0.25 | `run_state` | The AI keeps working state within a run, such as an environment, files, or a conversation, until the run ends. |
| 0.50 | `across_runs` | State persists across runs, such as resumable sessions, saved threads, memory, or a persistent configuration. |
| 0.75 | `durable_actor` | The product provides a durable, named AI actor that exists between runs, not only a saved configuration or a session. |
| 0.75 | `managed_memory` | That actor has memory the product manages across its runs, not only a file the prompt reads. |
| 1.00 | `own_principal` | The actor is its own principal with its own permissions, separate from any person's account. |
| 1.00 | `own_credentials` | The actor holds its own credentials or secrets for the systems it uses. |
| 1.00 | `durable_env` | The actor has a durable environment or execution state that persists between runs, such as a persistent machine, volume, or workspace. |

Limits, on top of the common limits:

* `person_access` caps at **0.75**: The spec states the actor acts only with a person's identity or access, such as never holding more access than the signed-in user, or running with the triggering user's authentication.

* A service account used by a job, or a memory file the prompt reads, meets the 0.50 level only.
* An ephemeral environment per run is state within a run, not a durable environment.
* Humans keeping admin rights over the actor does not fail a check. That is governance.

#### II.5 — Human supervision and exceptions

People supervise the work and handle exceptions instead of executing it.

| Level | Check | Passes when |
| ----: | ----- | ----------- |
| 0.25 | `after_view` | People can see what the AI did after the fact, such as a transcript, diff, log, or report. |
| 0.50 | `in_progress` | People can observe work in progress or browse a history of runs. |
| 0.75 | `escalation` | The AI can pause for an approval or escalate an exception to a person, then continue after the person responds. |
| 1.00 | `intervene` | People can intervene in or stop a running piece of work. |
| 1.00 | `audit` | An audit trail or audit log records AI activity for review. |

#### II.6 — Autonomous initiation and continuity

Work starts and continues without a person manually starting every run.

| Level | Check | Passes when |
| ----: | ----- | ----------- |
| 0.25 | `start` | A person can start a run that proceeds without the person staying in it. |
| 0.50 | `background` | A run continues or repeats in the background after a person starts it, such as running on when the person leaves or repeating on an interval. |
| 0.75 | `trigger` | Runs start from at least one kind of automatic trigger, a schedule or an event, with no person starting each run. |
| 1.00 | `both_triggers` | Runs start both from schedules and from events such as webhooks, app events, messages, or queue items. |
| 1.00 | `no_open_app` | Triggered runs execute in the background or in the cloud without any person's app or computer staying open. |

* A person authoring the trigger rule does not fail a check. Someone always sets the schedule.
* A trigger starts work. It does not make anyone own the process. That is II.1.

#### II.7 — Whole-process outcome

For the routine cases of its process, the AI delivers the final business outcome in the system where it lives, not an intermediate artifact a person must finish.

| Level | Check | Passes when |
| ----: | ----- | ----------- |
| 0.25 | `stage` | The AI completes at least one stage of a process on its own, producing a finished artifact such as a draft, a triage, a pull request, or a report. |
| 0.50 | `consecutive` | The AI completes two or more consecutive stages of the same process with no person between them, such as triage then resolve, or build then verify. |
| 0.75 | `final_outcome` | For routine cases, the AI delivers the final outcome in the system of record without a person finishing it, such as the reply sent, the ticket closed, the change merged or deployed, or the record updated. |
| 1.00 | `across_case_types` | The spec shows that final outcome across the routine case types of the process, not for one narrow case type. |

* An opened pull request is not a merged change. A draft is not a sent reply. A proposed update is not an updated record.
* Grade the process the product documents. When routine output always stops at a draft or review a person must complete, the 0.75 check fails.

### Type III — Autonomous

#### III.1 — Autonomous routine operations

Within the product's own scope, routine operations run with no structural human step.

| Level | Check | Passes when |
| ----: | ----- | ----------- |
| 0.25 | `some_unattended` | Some routine operations run unattended: they start automatically and finish with no person in the loop. |
| 0.50 | `one_process` | At least one whole process runs unattended for its routine cases, from automatic start to final outcome. |
| 0.75 | `several_processes` | Several distinct processes run unattended end to end within the product's scope. |
| 1.00 | `no_structural_step` | Across the product's scope, no routine operation structurally requires a person; people step in only for exceptions and policy. |

* Rate within the product's own scope, its craft or function. Company coverage is the Execution Scale.

#### III.2 — Work determination and allocation

AI decides what operational work should happen next and who does it, within a mandate.

| Level | Check | Passes when |
| ----: | ----- | ----------- |
| 0.25 | `next_step` | Within a run, the AI decides which step or task to do next. |
| 0.50 | `proposes` | The AI proposes new work no one asked for, such as suggested tasks, issues, or follow-ups, from what it observes. |
| 0.75 | `creates_starts` | The AI creates and starts new work itself, within its mandate, without a person approving each item. |
| 1.00 | `allocates` | The AI assigns or delegates that work to other AI actors or people by its own decision, not by a fixed routing rule. |

* Executing items already placed in a queue, or following a routing graph a person drew, does not pass the 0.75 or 1.00 checks.

#### III.3 — AI-to-AI coordination

Persistent AI actors coordinate and delegate without a person brokering each exchange.

| Level | Check | Passes when |
| ----: | ----- | ----------- |
| 0.25 | `subagents` | Within one run, an AI spawns or calls subagents and uses their results. |
| 0.50 | `shared_channel` | Several persistent AI actors work in a shared channel, thread, or workflow that people arranged. |
| 0.75 | `direct_delegation` | Persistent AI actors message or delegate work directly to each other, with no person relaying each exchange. |
| 1.00 | `open_handoffs` | Those actors hand off work beyond a fixed pipeline: they choose at run time which actor to involve. |

* Subagents inside one human-started run are 0.25. Several independent agents are not coordination by themselves.

#### III.4 — Closed operational loop

Detect, decide, execute, observe, and evaluate, with outcomes shaping the next decisions.

| Level | Check | Passes when |
| ----: | ----- | ----------- |
| 0.25 | `observes` | Within a run, the AI observes the result of its own actions, such as running tests or checking output, and reacts. |
| 0.50 | `outcomes_shown` | Outcomes of AI work are measured and shown to people, such as dashboards, evaluations, or analytics. |
| 0.75 | `fed_forward` | Evaluated outcomes of earlier runs feed into later runs automatically, such as remembered results, learned rules, or scores the AI reads. |
| 1.00 | `changes_decisions` | Those outcomes change later operational decisions (what to do, when, or how) without a person promoting each change. |

#### III.5 — Adaptive orchestration

AI changes how work is organized when conditions change, beyond branches a person wrote.

| Level | Check | Passes when |
| ----: | ----- | ----------- |
| 0.25 | `authored_branches` | Work follows conditional branches or retries that people wrote. |
| 0.50 | `replans` | The AI changes its plan within a run when conditions change. |
| 0.75 | `reorganizes` | Across runs, the AI changes how work is organized in a bounded scope, such as reassigning responsibilities or altering a workflow, within its authority. |
| 1.00 | `new_paths` | The AI creates new operational paths (new workflows, actors, or processes) without a person shipping each change. |

#### III.6 — Governance-level human role

People govern through enforced policy and limits, not routine supervision.

| Level | Check | Passes when |
| ----: | ----- | ----------- |
| 0.25 | `access_control` | Admins control who and what can access the AI, such as roles, SSO, SCIM, or permissions. |
| 0.50 | `behavior_policy` | Admins set policies on what AI actors may do, such as allowed tools, actions, data, or approval rules. |
| 0.75 | `enforced_limits` | The product enforces budgets, spending, rate, risk, or action limits on AI actors. |
| 1.00 | `irreversible_gated` | Irreversible or high-risk actions are gated by policy (a required approval or a block), while routine actions proceed. |
| 1.00 | `decision_audit` | Audits cover AI decisions against policy, such as blocked actions, policy violations, or decision records, not only an activity log. |

* SSO, SCIM, or roles alone are access control and meet the 0.25 level only.
* An activity log is II.5. The 1.00 audit check needs records of AI decisions against policy.
* Human governance controls never fail a check. Type III does not mean people give up authority.

<!-- rubric:end -->

## 6. Count each gap once

One missing fact fails the check it belongs to. Do not fail other checks for it.

| Fact | Where it counts | Where it does not |
| ---- | --------------- | ----------------- |
| The unit of work is a task, not a process | II.1 | II.2, II.3, II.7 |
| A job runs per artifact (per pull request, commit, or scan) | II.1 at the 0.50 level | II.6 |
| Routine output stops at a draft, an open pull request, or a review a person completes | II.7 | II.2, II.3, II.5 |
| Optional or exception-only approval steps | II.5, as a strength | II.2 |
| Tools were granted or bound at setup | nowhere | II.3 |
| The actor acts only with a person's access | II.4 `person_access` | II.1, III.6 |
| Humans keep admin over the actor | III.6, as governance | II.4 |
| The process graph was written by people | III.2, III.5 | II.1, II.2 |
| A person authored the trigger rule | nowhere | II.6 |
| SSO, SCIM, or roles only | III.6 at the 0.25 level | II.5 |
| The product has a marketplace or builder | Execution Scale | any type criterion |

## 7. Do not confuse these

* **Autonomous task ≠ Type II.** An agent that writes code, answers mail, or operates software can still be Type I. The question is whether AI owns the process.
* **Background execution ≠ ownership.** Running without an open app is II.6, not II.1.
* **Triggers ≠ ownership.** A schedule or webhook starts work. Ownership needs a named actor with its own intake.
* **Opened ≠ delivered.** An opened pull request is not a merged change. A draft is not a sent reply.
* **Multi-agent ≠ Type III.** Subagents inside a human-authored workflow do not orchestrate operations.
* **Workflow automation ≠ adaptive orchestration.** A predefined workflow can meet Type II and stay far from Type III.
* **Defining the process ≠ executing it.** A person, a template, or the product's builder may define the process. That is the Type II mandate. Grade who executes each case.
* **Human approval ≠ lack of autonomy.** Approvals and escalation for exceptions fit Type II and Type III.

## 8. Score

The scorer computes the score from the grades. You do not.

* **Completed floor:** 3 when every Type II and Type III criterion is 1.00; 2 when every Type II criterion is 1.00; 1 when every Type I criterion is 1.00; otherwise 0.
* **Progress:** the mean of the next Type's criteria, minus a weakest-link penalty of `0.25 × (1 − lowest) × mean`, clamped to 0.00–0.99.
* **Score:** floor plus progress, rounded to one decimal, half down. An incomplete Type never rounds up across its gate: 1.96 with an incomplete Type II publishes as **1.9**.

## 9. Before you answer

Try to disprove every passed check:

* Does the quote state this capability, in the configuration you named?
* Is the quote about this product, not a sibling or another plan?
* Does a person still hand over each case, accept each result, or finish each outcome?
* Is the actor persistent, or is each run a fresh session?

Then challenge every failed check the other way:

* Did you fail it for a fact the count-once table puts elsewhere?
* Did you fail it because a person defined the process, granted the tools, authored the trigger, or keeps admin rights?
* Is the evidence in the spec under a different name?

## 10. Output

Return one JSON object with this shape:

```json
{
  "configuration": "Product, plan or edition, and any first-class wrap rated.",
  "summary": "Two to four sentences on the operating model the product enables today.",
  "criteria": [
    {
      "key": "II.7",
      "checks": [
        {"id": "stage", "passed": true, "quote": "text copied from the spec"},
        {"id": "consecutive", "passed": true, "quote": "text copied from the spec"},
        {"id": "final_outcome", "passed": false, "quote": ""},
        {"id": "across_case_types", "passed": false, "quote": ""}
      ],
      "limits": [
        {"id": "preview", "applies": false, "quote": ""},
        {"id": "buyer_wired", "applies": false, "quote": ""},
        {"id": "other_plan", "applies": false, "quote": ""}
      ],
      "note": "One or two sentences on the evidence and the limit that decide this criterion."
    }
  ],
  "gap": "The smallest set of concrete missing capabilities, named by criterion, that blocks the next Type."
}
```

List every criterion from I.1 to III.6 in rubric order. Every check and every limit of each criterion appears once. A quote is required when `passed` or `applies` is true, and empty otherwise.

To score an answer by hand, save it as JSON and run `uv run intelligence-scale score answer.json --axis type --spec <slug>`.
