---
name: evaluate-exec-scale
description: Conservatively rate how much of a company's work a product can carry, from 0.00 to 1.00. Use when scoring organizational coverage: domain span, shared work, system reach, extensible coverage, work surfaces, adoption path, and ready-made jobs. Does not rate vendor size, customer counts, Intelligence Scale type, or foundation-model quality.
---

# Execution coverage evaluator

Rate how much of a company's work a product can carry as it ships.

The score runs from **0.00 to 1.00**. It is the vertical axis of the Intelligence Scale quadrant. It is not the Intelligence Scale type, and it is not a judgment of which foundation model is better.

This repository rates the **chassis**: the software or solution an organization can adopt. It does not rate the **motor**: the model inside that product. A documented, first-class wrap of another product is part of the chassis as this product exposes it. Do not copy a sibling dossier's scores. Do not raise a grade because the wrapped model is stronger.

This is not a vendor-maturity score. Customer counts, logo walls, funding, changelogs, and status pages do not raise a grade.

Be conservative. Marketing language, launch posts, roadmap items, and "you could build this" are not coverage.

## 1. Establish the evaluation scope

Before scoring, identify:

* the exact product being rated;
* the version, edition, or plan;
* the evaluation date;
* whether the subject is a hosted product, an open-source project, or both.

When a spec file is given, that file is the brief. Rate the product it names. Use its scope, edition, and cited sources. You may open URLs cited in the file. Do not replace the file with an open web search. A claim with no source is unproven and scores **0.00**.

Unless the spec says otherwise, evaluate the strongest **currently available and supported** configuration. That includes a documented wrap when the product starts and steers another agent as a supported provider. Grade what this product surfaces and adds, not the sibling product's own dossier. A thin wrap that hides work, or that only the same person can reach from another device, stays thin. Do not count unreleased roadmap features.

## 2. What this axis is not

Do not raise or lower the score because the product can enable Type I, Type II, or Type III. That is the type evaluator.

Do not raise a grade because the vendor is large, the product is generally available, or named customers exist.

Apply these distinctions:

* A Type III prototype that only one craft can use still scores low here.
* A widely used Type I assistant can score high here when people across the company can put their own work on it.
* A famous model does not make the product a company surface.
* Wrapping several coding agents does not widen span beyond that craft.
* A long feature list inside one craft is not span.
* A marketplace of coding plugins is still a coding marketplace.
* Shared Slack notifications are not multiplayer.
* A product only one specialist craft can use cannot publish **0.50** or higher, however strong the other criteria are.

## 3. Evidence grades

| Grade | Meaning |
| ----- | ------- |
| **1.00 — Native** | A current, supported, first-class capability or a documented fact directly satisfies the criterion. |
| **0.75 — Native but limited** | The capability or fact is real, but beta, preview, narrowly scoped, or materially constrained. |
| **0.50 — Partial** | Official material shows meaningful progress, but the criterion is only partly met. |
| **0.25 — External or thin** | The criterion depends mainly on custom work, a third party, or a claim with weak public evidence. |
| **0.00 — Absent or unproven** | The criterion is absent, roadmap-only, or cannot be verified from the spec and its sources. |

Apply these rules strictly:

* A current primary source is required for a **1.00** rating.
* Beta or preview functionality cannot score above **0.75**.
* A claim inferred only from secondary sources cannot score above **0.50**.
* A connector name, a slogan, or a logo wall cannot raise coverage.
* Generic API, plugin, MCP, or "you can build anything" support cannot score above **0.25** unless the shipped catalog already carries other work.
* A platform that can cover every function only after an SDK project, custom actions, or a services team is not coverage as it ships.
* Roadmap, announced, or hypothetical capability scores **0.00**.

If the evidence is ambiguous, choose the **lower** grade.

## 4. Criteria

### E.1 — Domain span

Whose work fits on the product as it ships.

Span is about which work the product is for, not about who executes it. A general work surface can reach **1.00** even when its type score stays low. A coding product lands at **0.25**. A support product can still reach **0.50**. One business function, such as support or sales, is not a specialist craft.

| Grade | Meaning |
| ----- | ------- |
| **1.00** | People across the company can put their own work on it. More than one business function, in the product today. |
| **0.75** | Several functions, with a real limit: one suite, one family of departments, or the rest still in preview. |
| **0.50** | One business function, such as support or sales. The rest of the company has no native path onto it. |
| **0.25** | One specialist craft, such as writing code or editing video. Only that craft can use it. |
| **0.00** | Unproven, or the buyer has to build the product first. |

A current primary source is required for **1.00**. Functions that exist only in preview cannot lift the grade above **0.75**. A roadmap, a product the buyer must assemble before any work fits, or a claim with no source in the spec scores **0.00**.

Grade from the dossier's product description and the sourced feature list. Do not widen span from a logo, a connector name alone, or a roadmap.

"One suite" means the product works only inside one vendor's application family, such as Microsoft 365, Salesforce, or a Notion workspace. A general work surface that connects to many vendors' systems is not one suite. Do not lower span because jobs are not pre-built (that is E.7), because reach needs connecting (E.3), or because there is only one surface (E.5).

### E.2 — Shared work

Can several people, and an operator, work on the same thing?

| Grade | Meaning |
| ----- | ------- |
| **1.00** | Native multiplayer: several people and an operator share a conversation, run, or workspace, hand work off, and see the same state. |
| **0.75** | A shared workspace or shared agent exists, and live collaboration is limited, preview, or missing the operator in the same thread. |
| **0.50** | The organization has a team account. Work itself stays single-player, and sharing is after the fact (a pull request, an export, a transcript). |
| **0.25** | Notifications, a share link, or a channel mention. Nobody else is in the work. |
| **0.00** | Single-player only, or unproven. |

A Slack or Teams *notification* that a run finished is **0.25**. A channel where teammates and the operator talk in one thread can be **0.75** or **1.00** when that thread is the work, not a status ping.

### E.3 — System reach

Can the product read and write the systems where company work already lives?

| Grade | Meaning |
| ----- | ------- |
| **1.00** | Native read and write into several systems of record the company already runs — mail, tickets, CRM, files, calendar, or the equivalent — as shipped jobs. |
| **0.75** | Reach into several systems, with a real limit: one suite, read-heavy connectors, or write-back incomplete. |
| **0.50** | Reach into one system or one suite's objects. |
| **0.25** | The product operates only on its own artifacts (a repository, a project, a canvas), or the buyer must wire generic tools. |
| **0.00** | Conversation or generation only, or unproven. |

Computer use that can operate the company's apps is evidence of reach. Computer use that browses the public web for an answer is not. A connector name in a list is not write-back.

Installing a listed application from the product's own catalog, then supplying its credentials or signing in, is not "the buyer wires generic tools". It can reach **0.75** when that catalog reaches several systems with write-back. **1.00** still needs named systems of record the product documents reading and writing as shipped jobs. A persistent computer that can operate the company's apps with the credentials it is given is reach.

### E.4 — Extensible coverage

Can coverage grow into other use cases through a catalog the product ships?

E.4 grades the catalog as a way to grow: whether it exists, whether it is limited to one craft or suite, and who can add the next entry. It does not grade how finished each entry is. That is E.7.

| Grade | Meaning |
| ----- | ------- |
| **1.00** | A first-party marketplace or directory of installable agents, skills, apps, or workflows. It is not limited to one craft or one suite, and the vendor, third parties, and customer organizations can publish into it. |
| **0.75** | A real catalog exists, with a real limit: one suite or one family of jobs, closed to third-party publishing, mostly connectors, or preview. |
| **0.50** | Official templates or starter agents for more than one job, or an organization-internal directory, but not a marketplace. |
| **0.25** | Extensions, plugins, or MCP that a builder assembles, or a catalog that stays inside one craft. |
| **0.00** | No catalog, or unproven. |

* Growing coverage only through an SDK, custom actions, MCP the buyer wires, or a forward-deployed team stays at **0.25**, even if templates exist.
* A catalog open to community publishing is a strength here. Community trust gates, such as a manager confirmation on install, do not lower it.

Plugins for linters, repos, and IDEs stay at **0.25**. A marketplace of coding plugins is still a coding marketplace.

### E.5 — Work surfaces

Where can that work happen?

| Grade | Meaning |
| ----- | ------- |
| **1.00** | Native surfaces across the places company work already happens: the product UI plus workplace chat, mail or a customer channel, and an API or embed. |
| **0.75** | Several surfaces, with a real limit: one suite's apps, or a major channel still in preview. |
| **0.50** | Two surfaces (for example web and Slack, or an IDE and a CLI). |
| **0.25** | One surface: a single web app, an IDE, a terminal, or a chat box. |
| **0.00** | Unproven. |

Surfaces do not raise domain span. A coding agent with an IDE, a CLI, and Slack is still a coding product. Inbound webhooks that start a run are a trigger, not a place where people work. A documented public API or embed counts as a surface.

### E.6 — Adoption path

Can a team put that work on the product as it ships, without assembling the core system?

| Grade | Meaning |
| ----- | ------- |
| **1.00** | Documented administration, permissions, and a trial, install, or onboarding path so ordinary teams can put work on it today. |
| **0.75** | The path exists, and it is limited: one plan, preview admin, or thin documentation. |
| **0.50** | An individual can start. Organization administration is thin. |
| **0.25** | The product works only after the buyer assembles the core from generic APIs. |
| **0.00** | Unproven, waitlist-only, or no way to start. |

Ask whether an ordinary team can put work on it and add the next job without assembling a platform.

* A documented install, trial, or admin path for ordinary teams can still reach **1.00**.
* A path that exists only for one plan, or that needs a specialist to finish setup, stays at **0.75** or **0.50**.
* A product that works only after professional services, a custom platform build, or generic APIs stays at **0.25** or below.

This is not a trust-center, changelog, or interface-taste score. Missing SSO does not fail the criterion when a team can still adopt the product.

### E.7 — Ready-made coverage

How quickly does a team get a working job, without designing the agent by hand?

A product may start empty. That is not a gap when the product itself gets the team to a running job. Three paths count:

* **Shipped** — the vendor ships the job ready to turn on.
* **Installed** — a finished job (an agent or workflow with its requirements declared) installs from the product's catalog, including community listings.
* **Generated** — the product's own AI builds the job from a plain-language description (instructions, tools, and triggers) and a person reviews it.

| Grade | Meaning |
| ----- | ------- |
| **1.00** | For several business functions, a team reaches a running job through one of those paths without a specialist: turn it on, install it, or describe it and approve what the product builds. |
| **0.75** | A path exists for several functions, with a real limit: one suite or one family of departments, or what the product installs or generates still needs a builder to connect tools, bind requirements, or set triggers. |
| **0.50** | Ready-made jobs for one business function, or starter templates and prompts a non-specialist still has to finish. |
| **0.25** | A blank canvas, a general assistant, or jobs that stay inside one craft. The buyer writes every job by hand. |
| **0.00** | Unproven. |

A transversal chat box with no shipped jobs and no builder can still score well on domain span and poorly here. A builder canvas that can do anything only after an SDK project or a services engagement is still a blank canvas. A catalog that holds only connectors or plugins, not finished jobs, counts on E.3 and E.4, not here.

## Count each gap once

One missing fact lowers the one criterion it belongs to. Do not charge it again elsewhere.

| Fact | Where it counts | Where it does not |
| ---- | --------------- | ----------------- |
| Jobs are not pre-built | E.7 | E.1 |
| Systems of record need connecting | E.3 | E.1, E.7 |
| There is only one surface | E.5 | E.1, E.2 |
| The catalog has no finished jobs, only connectors | E.4, E.7 | E.1 |
| Admin or trial is limited to one plan | E.6 | E.1, E.4 |
| The product is one specialist craft | E.1, and the span cap | a second penalty on every row, unless that row's table names the craft |

## 5. Calculate the score

```text
raw = arithmetic mean of E.1 through E.7
penalty = 0.25 × (1 − lowest grade)
uncapped = clamp(raw − penalty, 0, 1)
if E.1 is 0.25 or lower, score = min(uncapped, 0.49)
otherwise score = uncapped
```

The lowest grade includes E.1 when span is the weakest criterion. A span of **0.50** or **0.75** is not capped. It still enters the mean, and it sets the penalty when it is the lowest grade.

**0.49** is the highest published score below **0.50**. Apply the cap before rounding. Round the result to **two decimal places**, half down. For example, `0.625` becomes **0.62**, and `0.635` becomes **0.63**.

Six criteria at **1.00** and a domain span of **0.25** produce an uncapped score near **0.71**. The cap publishes **0.49**. The product then sits with Niche or the Visionaries.

There is no integer gate. A missing criterion still pulls the score down through the weakest-link penalty, so one fatal gap cannot be averaged away. The span cap is separate from that penalty, and both apply when E.1 is **0.25** or lower.

## 6. Conservative challenge

Before publishing the rating, try to disprove it.

* Whose work can go on the product today, and which functions have no native path?
* Can several people and an operator share the same work, or only a notification?
* Which systems of record can it read and write without the buyer wiring them?
* Does the catalog carry other functions, or only the same craft?
* Where does the work happen, and is that one specialist surface?
* Can an ordinary team put work on it as shipped, and add the next job without an SDK project or a services team?
* Can a team reach a working job by turning it on, installing it, or describing it, or must someone design every job by hand?

If a high grade rests on marketing copy, a connector list, or "you can build this", lower it.

Then challenge every grade below 1.00 the other way. Does that criterion's table name the limit you found? Is the same limit already counted on another criterion?

If the product wraps another agent, ask what this chassis actually exposes: whose work still fits, who can share it, which systems it reaches, and whether an ordinary team can adopt the wrap without assembling the core. Do not import a sibling spec's coverage.

## 7. Output format

Start with:

> **Execution coverage: 0.XX / 1.00**

Then write a short explanation of what work an organization can put on the product today.

Provide an evidence table for every criterion:

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| E.1 | 1.00 | ... | ... |
| E.2 | ... | ... | ... |
| E.3 | ... | ... | ... |
| E.4 | ... | ... | ... |
| E.5 | ... | ... | ... |
| E.6 | ... | ... | ... |
| E.7 | ... | ... | ... |

Then show the calculation:

* **Raw mean:** X.XX
* **Weakest criterion:** X.XX
* **Weakest-link penalty:** X.XX
* **Uncapped score:** X.XX
* **Span cap:** 0.49, because E.1 is 0.25 or lower — or **none**
* **Final score:** **0.XX**

Finish the narrative with:

### What most limits coverage?

Name the lowest criteria and the concrete missing evidence. Do not give vague advice such as "improve execution".

End with a single fenced JSON block and no text after it:

```json
{
  "axis": "exec",
  "score": 0.62,
  "criteria": {
    "E.1": 0.75,
    "E.2": 0.75,
    "E.3": 0.75,
    "E.4": 0.5,
    "E.5": 0.75,
    "E.6": 1.0,
    "E.7": 0.5
  }
}
```

`score` is the final score to two decimals, after the penalty, the span cap, and half-down rounding. When E.1 is **0.25** or lower, `score` is at most **0.49**. `criteria` includes E.1 through E.7. The example above is not capped, because E.1 is **0.75**: the mean of those seven grades is **0.71**, the penalty is **0.125**, and `0.589` publishes as **0.58**.

## 8. Citation requirements

Every material claim used to justify a grade must have a source.

Prefer a direct link to the documentation page that states the fact. Distinguish documented fact, reasonable inference, and evaluator judgment. Include the evaluation date.
