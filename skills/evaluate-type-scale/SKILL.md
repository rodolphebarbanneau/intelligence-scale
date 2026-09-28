---
name: evaluate-type-scale
description: Research and conservatively rate an AI solution, technology, product, platform, or framework against the Intelligence Scale from 0.0 to 3.0. Use when evaluating how far a technology can natively enable organizations to shift operational agency from humans to AI across Type I Augmented, Type II Delegated, and Type III Autonomous operating models.
---

# Intelligence Scale Type Evaluator

Evaluate the **capability ceiling of a technology** against the [Intelligence Scale](https://github.com/rodolphebarbanneau/intelligence-scale).

The rating measures what operating model the technology can **natively enable**, not how much AI a particular customer currently uses.

This repository rates the **chassis**: the product an organization can adopt. It does not rate the **motor**: the foundation model inside that product. A first-class wrap of another agent is part of the chassis as this product exposes it. Do not copy a sibling dossier's scores.

The scale is:

* **Type I — Augmented:** People execute. AI assists.
* **Type II — Delegated:** AI executes. People supervise.
* **Type III — Autonomous:** AI orchestrates. People govern.

Be conservative. Do not reward marketing language, generic extensibility, demos, roadmap features, or theoretical possibilities as if they were native product capabilities.

Do not raise or lower the type score because the product is multiplayer, has a marketplace, or covers many business functions. That is the Execution Scale. A specialist craft tool can still reach Type II. A company-wide assistant can still stay at Type I.

## 1. Establish the evaluation scope

Before scoring, identify:

* the exact technology or product;
* the version or state being evaluated;
* the evaluation date;
* the relevant edition or plan, when capabilities differ;
* whether the subject is a product, open-source project, framework, or platform.

When a spec file is given, that file is the brief. Rate the product it names. Use the file's scope, edition, and cited sources. You may open URLs cited in the file. Do not replace the file with an open web search. A claim with no source is unproven and scores **0.00**.

Unless otherwise requested, evaluate the strongest **currently available and supported first-party configuration**. That configuration includes a documented, first-class wrap when the product starts and steers another agent as a supported provider.

Do not count unreleased roadmap features.

For open-source projects, prefer released or documented functionality over speculative code on an unreleased branch.

## 2. Research before rating

When a spec file is given, that file is the brief. Gather evidence from it and from the URLs it cites. Do not replace the file with an open web search.

If no spec is given, prefer sources in this order:

1. Official product documentation.
2. Official source repository and maintained README files.
3. Official technical documentation, architecture guides, changelogs, and release notes.
4. Official product or engineering articles.
5. Reputable independent technical sources.
6. Community discussions only when necessary.

Use current sources whenever the product changes rapidly.

Look for capabilities relevant to each criterion in those sources. Do not rely only on vendor terminology such as "autonomous", "agentic", "operator", or "multi-agent".

A product calling something an **agent**, **operator**, or **autonomous agent** is not evidence that it satisfies any particular Intelligence Scale Type.

Do not treat a marketplace, a shared workspace, or a long feature list as Type II or Type III. Coverage is the other axis.

For every scored criterion, record the evidence and source.

If a capability cannot be verified, treat it as **unproven**, not present.

## 3. Distinguish native capability from possibility

The Intelligence Scale evaluates what the technology enables **natively**.

Use these evidence grades:

| Grade                         | Meaning                                                                                                                                        |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **1.00 — Native**             | A current, supported, first-class capability directly enables the criterion end-to-end.                                                        |
| **0.75 — Native but limited** | The capability is native, but beta, preview, narrowly scoped, or materially constrained.                                                       |
| **0.50 — Composable**         | The product provides official primitives that can achieve the criterion, but users must substantially assemble or orchestrate them themselves. |
| **0.25 — External or custom** | The behavior is possible mainly through custom code, generic APIs, MCP, external automation, or another orchestration system.                  |
| **0.00 — Absent or unproven** | The capability is absent, roadmap-only, unsupported, or cannot be verified from reliable evidence.                                             |

Apply these rules strictly:

* A current primary source is required for a **1.00** rating.
* Beta or preview functionality cannot score above **0.75**.
* Capability inferred only from secondary sources cannot score above **0.50**.
* Generic API, plugin, MCP, scripting, or extension support does not prove a capability is native.
* "You could build this with the product" is not equivalent to "the product provides this".
* A feature the buyer must assemble with generic APIs, MCP, or an unsupported third party cannot score above **0.25**.
* A documented, first-class wrap of another product is not that case. Grade the adopted configuration: this product plus its strongest supported wrap, as this product exposes it. Do not copy a sibling dossier's scores. Discount what this product hides, breaks, or leaves on the other product's native UI. Credit what this product adds.
* Do not raise or lower a grade because the foundation model inside the chassis is stronger or weaker.
* Roadmap, announced, experimental-but-unavailable, or hypothetical functionality scores **0.00**.

## 4. Evaluate Type I — Augmented

**People execute. AI assists.**

Evaluate whether the technology can natively enable AI augmentation while humans remain responsible for the overall work.

### I.1 — Routine AI assistance

AI can be embedded in normal work rather than used only as an isolated experiment or API call.

### I.2 — Context and capability access

AI can access useful context, data, applications, tools, or other capabilities required to assist real work.

### I.3 — Bounded autonomous tasks

Agents or AI systems can independently execute meaningful multi-step tasks within a bounded objective.

Task autonomy may include operating software, editing files, using tools, executing commands, researching, or taking actions.

### I.4 — Human direction and review

Humans can initiate, direct, inspect, approve, correct, or continue AI work while remaining the owner of the broader process.

### I.5 — Repeatable organizational use

The technology supports persistent or repeatable use in real workflows rather than only one-off demonstrations.

Task-level autonomy does **not** by itself indicate Type II.

## 5. Evaluate Type II — Delegated

**AI executes. People supervise.**

Type II is the critical execution threshold.

A technology reaches Type II only when it natively enables AI to take responsibility for **complete business processes**, while humans move primarily into supervision.

In Type II, people **define** the work: objectives, the process, policy, permissions, and escalation. AI **executes** it. Who wrote the process does not decide the grade. A process a person designed, a publisher listed, or the product's AI generated and a person approved is still a Type II process. What decides the grade is who executes each instance of it. An AI that invents or rewrites the process belongs to Type III.

Each criterion below has its own grade table. The evidence grades in section 3 still cap every row: beta or preview stays at **0.75** or below, and generic APIs or MCP the buyer assembles stay at **0.25** or below.

### II.1 — End-to-end process ownership

A persistent AI actor can own and execute a meaningful end-to-end process over time.

| Grade | Meaning |
| ----- | ------- |
| **1.00** | A first-class persistent AI actor can be put in charge of a business process. It takes each case from its triggers, channel, or queue, carries it to an outcome, and keeps doing so across runs. Humans set the mandate and handle exceptions. |
| **0.75** | The same ownership exists, with a real limit: preview, one narrow kind of process, or routine cases that still stop at a draft a person must finish. |
| **0.50** | A workflow, automation, or trigger engine runs a designed multi-step process, with no persistent actor that owns it. Or official primitives that a builder must assemble into ownership. |
| **0.25** | Task runs a person or a single event dispatches: one change, one reply, one report. |
| **0.00** | Chat only, or unproven. |

Do not lower II.1 because a human, a publisher, or a template defined the process. That is the Type II mandate. Do lower it when each unit of work is still a task a person hands over.

### II.2 — Process-level execution

AI can execute and progress through the process without a human orchestrating each task or step.

| Grade | Meaning |
| ----- | ------- |
| **1.00** | Once a run starts, it moves through the process steps, branches, and retries with no person required between steps. Human approval steps exist but are the organization's choice or limited to exceptions. |
| **0.75** | Runs progress on their own, with a real limit: routine steps require a person and the organization cannot remove that, or the capability is preview. |
| **0.50** | The AI completes a multi-step task on its own. Moving between tasks of the process needs a person. |
| **0.25** | A person orchestrates most steps. |
| **0.00** | Unproven. |

A long multi-step task is not automatically a business process. That question belongs to II.1. Do not lower II.2 because the steps were written by a person, or because optional approval steps exist.

### II.3 — Multi-capability execution

The AI actor can use the agents, models, tools, applications, systems, or other capabilities required to complete its process.

| Grade | Meaning |
| ----- | ------- |
| **1.00** | During a run, the actor selects and uses the tools, applications, agents, and systems it was granted. No person coordinates each call. |
| **0.75** | The same, with a real limit: a key capability is beta or preview, or writes land only as drafts a person sends. |
| **0.50** | One family of tools only, or a person moves work between capabilities. |
| **0.25** | Capabilities are generic APIs or MCP the buyer wires. |
| **0.00** | Unproven. |

Granting, binding, or configuring the toolbox at setup does not lower II.3. Every actor is given its access by someone.

### II.4 — Persistent AI actor

The technology provides a durable AI worker or equivalent abstraction with the state necessary to own work over time.

For full credit, look for meaningful support for:

* persistent identity or principal;
* context or memory;
* permissions or authorization;
* credentials or controlled system access;
* durable execution state or environment.

| Grade | Meaning |
| ----- | ------- |
| **1.00** | A durable actor has its own principal, memory across runs, its own permissions, its own credentials, and a durable environment or execution state. |
| **0.75** | A durable actor exists and one element is limited: it acts only with a person's access, its memory is preview, or it is beta. |
| **0.50** | Persistent configuration, threads, or resumable sessions, with no principal of its own. |
| **0.25** | Each run gets an ephemeral environment that ends with it. |
| **0.00** | Unproven. |

An ephemeral agent invocation is not a persistent AI actor. Humans keeping admin rights over the actor does not lower II.4. That is governance, and it belongs to II.5 and III.6.

### II.5 — Human supervision and exceptions

The technology allows humans to supervise work rather than routinely execute it.

Look for capabilities such as:

* observability;
* approvals;
* escalations;
* exception handling;
* intervention;
* auditability;
* human decision points.

| Grade | Meaning |
| ----- | ------- |
| **1.00** | People can observe runs, receive approvals and exceptions, intervene or stop, and audit, without executing routine steps. |
| **0.75** | Supervision exists and is limited: some of those pieces are missing, preview, or only on one plan. |
| **0.50** | Review happens only after the fact: a diff, a transcript, a report. |
| **0.25** | Humans routinely execute the steps. |
| **0.00** | Unproven. |

### II.6 — Autonomous initiation and continuity

Processes can begin or continue without a person manually starting every execution.

Look for:

* schedules;
* event triggers;
* webhooks;
* queues;
* background execution;
* persistent monitoring;
* automatic continuation.

| Grade | Meaning |
| ----- | ------- |
| **1.00** | Schedules and event or webhook triggers start runs with no person starting each one. Work continues in the background. |
| **0.75** | One kind of trigger only, runs only while an app stays open, or the trigger capability is preview. |
| **0.50** | A person-started run repeats or continues in the background. |
| **0.25** | A person starts every run. |
| **0.00** | Unproven. |

A background task that was manually dispatched and simply takes a long time is not sufficient by itself. A person authoring the trigger rule does not lower II.6. Someone always sets the schedule.

### Type II hard gate

A technology **must score 1.00 on every Type II criterion to reach 2.0 or higher**.

If any Type II criterion scores below 1.00, the final rating must remain below **2.0**, regardless of Type III-like capabilities elsewhere in the product.

This is intentional.

A score above 2.0 means the technology is natively built to enable the complete Type II operating model.

## 6. Evaluate Type III — Autonomous

**AI orchestrates. People govern.**

Type III requires more than autonomous process execution. AI must be capable of orchestrating the operational system itself.

### III.1 — Autonomous routine operations

Routine operational execution can proceed across the organization without human participation being structurally required.

### III.2 — Work determination and allocation

AI can determine what operational work should happen next and allocate or delegate that work within human-defined mandates.

Executing tasks already placed in a queue is not sufficient.

### III.3 — AI-to-AI coordination

Persistent AI actors can coordinate, delegate, communicate, or collaborate directly without humans orchestrating each interaction.

Having multiple independent agents does not by itself satisfy this criterion.

### III.4 — Closed operational loop

The system can autonomously:

**detect → decide → execute → observe → evaluate**

The evaluation of outcomes must be capable of influencing subsequent operational decisions.

### III.5 — Adaptive orchestration

AI can adapt how work is organized when circumstances change.

This is stronger than following conditional branches in a workflow written by a human.

Look for the ability to change plans, reallocate responsibilities, alter processes, create new operational paths, or otherwise modify orchestration within defined authority.

### III.6 — Governance-level human role

The technology can support an operating model where routine human intervention is exceptional and humans primarily retain:

* purpose;
* strategy;
* policy;
* capital allocation;
* risk boundaries;
* major irreversible decisions.

Human governance controls do not reduce the score. Type III does not mean humans relinquish ultimate authority.

### Grading Type III

Type III criteria use the evidence grades in section 3. These anchors keep partial credit consistent:

| Grade | Meaning |
| ----- | ------- |
| **1.00** | The product natively does it: AI decides, coordinates, adapts, or closes the loop within its mandate. |
| **0.75** | Native, with a real limit: preview, one kind of work, or a bounded group of actors. |
| **0.50** | Official primitives that do it when people arrange them: several persistent actors in one channel or workflow, event triggers plus dashboards, operator memory that carries outcomes into the next run. |
| **0.25** | It happens only inside one human-started run or one designed workflow: subagents, conditional branches, a group chat. |
| **0.00** | Absent or unproven. |

### Type III hard gate

A technology reaches **3.0 only when every Type III criterion scores 1.00 and the complete Type II threshold is also satisfied**.

Anything less remains below 3.0.

## 7. Do not confuse these concepts

Apply the following distinctions explicitly during evaluation.

### Autonomous task ≠ Type II

An agent that independently writes code, researches a topic, answers emails, creates calendar events, or operates software may still be Type I.

The question is whether AI owns the **process**, not whether a task is impressive.

### Background execution ≠ process ownership

Running without an open browser or terminal does not establish Type II.

### Triggers ≠ Type II by themselves

Schedules and webhooks provide autonomous initiation. They do not establish persistent responsibility for a process.

### Multi-agent ≠ Type III

Several agents cooperating inside a human-authored workflow do not necessarily orchestrate the organization.

### Workflow automation ≠ adaptive orchestration

A predefined workflow can satisfy important Type II requirements while remaining far from Type III.

### Tool access ≠ operational agency

An agent having many tools says little about who determines, owns, and coordinates the work.

### Chassis ≠ motor, and a wrap is not a motor

The **motor** is the foundation model. Do not raise or lower the type score because one model is smarter than another.

The **chassis** is the product an organization adopts: surfaces, permissions, threads, jobs, and the first-class configurations it ships. A documented, supported wrap of another agent is part of that chassis as this product exposes it. Rate what a buyer can do while sitting in this product, not the sibling product's own dossier.

A thin wrap that hides half the agent scores lower than the wrapped product. A harness that surfaces the agent loop and adds its own automation can score as high or higher. Generic BYO, MCP, or "you could attach anything" is still **0.25** or below.

### Coverage ≠ type

A marketplace, a shared workspace, or a product that many functions can use does not move the type score. Those facts belong on the Execution Scale. Type asks who executes the work that already fits.

### Human approval ≠ lack of autonomy

Approvals, escalation boundaries, and governance controls are compatible with Type II and Type III when humans are handling exceptions rather than routine execution.

### Defining the process ≠ executing it

A person, a publisher, a template, or the product's own builder may define the process. That is the Type II mandate. Grade who executes each instance, not who wrote the definition.

### Count each gap once

One missing fact lowers the one criterion it belongs to. Do not charge it again elsewhere.

| Fact | Where it counts | Where it does not |
| ---- | --------------- | ----------------- |
| The unit of work is a task, not a process | II.1 | II.2, II.3 |
| Optional or exception-only approval steps | II.5 (as a strength) | II.2 |
| Tools were granted or bound at setup | nowhere | II.3 |
| Humans keep admin over the actor | II.5, III.6 (as governance) | II.4 |
| The process graph was written by people | III.2, III.5 | II.1, II.2 |
| A person authored the trigger rule | nowhere | II.6 |
| The product has a marketplace or builder | Execution Scale | any type criterion |

## 8. Calculate the score

Scores range from **0.0 to 3.0**.

Integer values represent complete operating-model thresholds.

Decimals represent progress toward the **next** Type.

### Step 1 — Determine the completed floor

Use the highest applicable threshold:

* **3** — every Type II and Type III criterion scores 1.00.
* **2** — every Type II criterion scores 1.00.
* **1** — every Type I criterion scores 1.00.
* **0** — otherwise.

Type II may be satisfied even by a specialized technology that does not expose every Type I-style user experience. Do not artificially lower a genuinely Type II system merely because it is not designed as an assistant.

### Step 2 — Measure progress toward the next Type

If the completed floor is:

* **0**, evaluate progress using the Type I criteria.
* **1**, evaluate progress using the Type II criteria.
* **2**, evaluate progress using the Type III criteria.
* **3**, the score is 3.0.

Calculate:

`raw_progress = arithmetic mean of the next Type criterion grades`

Then apply a weakest-link penalty proportional to that progress:

`penalty = 0.25 × (1 - lowest criterion grade) × raw_progress`

`adjusted_progress = raw_progress - penalty`

Clamp adjusted progress to the range `0.00–0.99`.

The penalty removes at most a quarter of the progress. It never erases real progress. Examples:

* Five criteria at 1.00 and one at 0.75: raw 0.96, penalty 0.06, adjusted 0.90.
* Two criteria at 0.50 and four at 0.25: raw 0.33, penalty 0.06, adjusted 0.27.
* Every criterion at 0.00: adjusted 0.00.

Then:

`score = completed_floor + adjusted_progress`

Round the final score to **one decimal place**.

### Why the penalty exists

The Intelligence Scale describes operating models, not collections of unrelated features.

A product with five strong capabilities and one fundamental missing capability should not appear almost equivalent to a product that natively satisfies the complete Type.

The weakest-link penalty makes ratings conservative while still recognizing meaningful progress. Because it is proportional, early primitives toward the next Type still show as a decimal. The integer gates below are what keep an incomplete Type from crossing the line.

### Hard caps override the formula

Regardless of the arithmetic:

* incomplete Type I cannot produce a score of 1.0 through rounding;
* incomplete Type II cannot produce a score of 2.0 or above;
* incomplete Type III cannot produce a score of 3.0.

Always round downward across a Type boundary when necessary.

For example, `1.96` with an incomplete Type II gate must be reported as **1.9**, never 2.0.

## 9. Perform a conservative challenge before finalizing

Before publishing the rating, try to disprove it.

For a proposed score near or above Type II, ask:

* Can AI genuinely own an end-to-end process?
* Who decides that work needs to start?
* Who determines the next operational step?
* Does a human still have to dispatch most units of work?
* Is there a persistent AI actor, or only isolated agent sessions?
* Does that actor have its own identity, state, permissions, and access?
* Can the process continue when humans stop actively interacting with the product?
* Are humans supervising exceptions, or still orchestrating execution?

For a proposed score above Type II, also ask:

* Does AI determine and allocate work, or merely consume predefined work?
* Can AI actors coordinate without human orchestration?
* Is the orchestration itself adaptive?
* Can observed outcomes alter future operations?
* Are workflows fundamentally designed by humans and merely executed by AI?
* Could humans realistically withdraw from routine supervision and remain primarily in governance?

Then challenge every grade below 1.00 the other way:

* Does the grade table for that criterion actually name the limit you found?
* Is that limit already counted on another criterion?
* Did you lower a Type II criterion because a person defined the process, granted the tools, or keeps admin rights?

If the evidence is ambiguous, choose the **lower** grade.

Do not award a score because the technology could theoretically reach it with sufficiently capable future models.

Do not zero a wrap because the agent loop lives in another product. Ask what this chassis surfaces of that loop, and what it adds. Do not paste a sibling spec's grades.

Rate the technology that exists now.

## 10. Output format

Start with:

> **Intelligence Scale capability: X.X / 3.0**

Then state the nearest interpretation, for example:

* below Type I;
* Type I with early Type II capabilities;
* approaching Type II;
* Type II with early Type III capabilities;
* approaching Type III;
* Type III.

Follow with a concise explanation of the operating model the product can natively enable.

Then provide an evidence table:

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| I.1       |  1.00 | ...      | ...    |
| ...       |   ... | ...      | ...    |
| II.1      |   ... | ...      | ...    |
| ...       |   ... | ...      | ...    |
| III.1     |   ... | ...      | ...    |

Include all criteria required to justify the completed floor and the progress toward the next Type. Include higher-Type criteria when they are relevant to claims being made.

Then show the calculation:

* **Completed floor:** X
* **Next Type raw progress:** X.XX
* **Weakest criterion:** X.XX
* **Weakest-link penalty:** X.XX
* **Adjusted progress:** X.XX
* **Final score:** **X.X**

Finish with:

### What prevents the next Type?

Identify the smallest set of concrete missing native capabilities preventing the technology from crossing the next integer threshold.

Do not provide vague recommendations such as "more autonomy" or "better agents". Name the exact missing Intelligence Scale criteria.

End with a single fenced JSON block and no text after it:

```json
{
  "axis": "type",
  "score": 1.4,
  "floor": 1,
  "criteria": {
    "I.1": 1.0,
    "I.2": 1.0,
    "I.3": 1.0,
    "I.4": 1.0,
    "I.5": 1.0,
    "II.1": 0.5
  }
}
```

`score` is the final score to one decimal place. `floor` is the completed floor. `criteria` includes every criterion you graded.

## 11. Citation requirements

Every material capability used to justify a grade must have a source.

Prefer direct links to the exact documentation page rather than a vendor homepage.

Clearly distinguish:

* documented fact;
* reasonable inference;
* evaluator judgment.

Do not present inference as documented product behavior.

Include the evaluation date because AI products change rapidly.

When sources conflict, prefer current technical documentation and released product behavior over marketing copy.


When evidence is insufficient, say so and score conservatively.
