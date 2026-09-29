---
name: evaluate-exec-scale
description: Rate how much of a company's work a product can carry, from 0.00 to 1.00, by answering yes/no checks from its spec. Use when scoring organizational coverage: domain span, shared work, system reach, extensible coverage, work surfaces, adoption path, and ready-made jobs. Does not rate vendor size, customer counts, Intelligence Scale type, or foundation-model quality.
---

# Execution coverage evaluator

Rate how much of a company's work a product can carry as it ships.

The score runs from **0.00 to 1.00**. It is the vertical axis of the Intelligence Scale quadrant. It is not the Intelligence Scale type, and it is not a judgment of which foundation model is better.

You do not pick grades. You answer yes/no checks, each backed by a verbatim quote from the spec. The scorer turns the checks into grades, applies the caps, and computes the score.

## 1. Scope

The spec file is the brief and the **only evidence**. Rate the product it names, in the edition and state it describes. Do not browse, and do not use what you remember about the product. A URL in the spec is a citation, not something to open. A capability the spec does not state is unproven, and its check fails.

Rate **one configuration**: the strongest currently available, supported configuration the spec describes. State it in `configuration`. Every check must hold in that one configuration. Do not combine features from different plans, editions, or sibling products. When evidence only holds elsewhere, the `other_plan` limit applies.

This repository rates the **chassis**, not the **motor**. A documented, first-class wrap of another product is part of the chassis as this product exposes it. Wrapping several coding agents does not widen span beyond that craft.

This is not a vendor-maturity score. Customer counts, logo walls, funding, changelogs, and status pages do not pass any check. Do not raise or lower coverage because the product can reach Type I, II, or III. That is the type evaluator.

## 2. Evidence rules

* A check passes only when the spec states the capability. Quote the words that prove it.
* A quote is text copied character for character from the spec. You may join two excerpts of the same passage with `...`. The scorer rejects quotes it cannot find, and the check fails.
* A connector name in a list, a slogan, or a logo does not prove read and write.
* Roadmap, announced, or hypothetical features fail every check.
* A capability available only through a generic API, SDK, webhook, or MCP server the buyer wires triggers the `buyer_wired` limit.
* Beta, preview, experimental, and waitlist capabilities can pass checks. They trigger the `preview` limit.
* When the evidence is ambiguous, the check fails.

## 3. Definitions

* **Specialist craft:** a trade such as writing code, design, or video editing. Only people in that craft use the product.
* **Business function:** a department's work, such as support, sales, marketing, HR, finance, or IT operations.
* **System of record:** a system where company work already lives, such as mail, tickets, CRM, files, or calendar.
* **Surface:** a place where people do the work, such as a web app, desktop app, IDE, CLI, workplace chat, mail, a customer channel, or an API.
* **Job:** a running agent, workflow, or automation that does a piece of work.

## 4. How the scorer grades

Each criterion has four cumulative levels: **0.25**, **0.50**, **0.75**, **1.00**. Each level has one or more checks.

* The base grade is the highest level whose checks all pass, going up from 0.25.
* The next level adds a share: `0.25 × passed checks ÷ checks at that level`.
* Each limit that applies caps that criterion at its value.

Answer **every** check and limit, at every level, even after a lower level fails.

## 5. Rubric

<!-- rubric:start -->

Common limits. Answer these for every criterion. Each one caps that criterion when it applies:

* `preview` caps at **0.75**: The spec marks the capability behind this criterion's highest passed check as preview, beta, experimental, research preview, early access, or waitlist.
* `buyer_wired` caps at **0.25**: The spec shows this capability only through a generic API, SDK, webhook, or MCP server the buyer must build or wire, not as a shipped feature.
* `other_plan` caps at **0.50**: The evidence for this criterion's highest passed check applies only to a different product, plan, edition, or deployment than the configuration you stated.

Span cap. The scorer applies this to the final score:

* A product only one specialist craft can use cannot publish 0.50 or higher: when E.1 is below 0.50, the score is at most 0.49.

### E.1 — Domain span

Whose work fits on the product as it ships.

| Level | Check | Passes when |
| ----: | ----- | ----------- |
| 0.25 | `some_work` | The spec names at least one kind of work the product ships for, such as a specialist craft or a business task. |
| 0.50 | `function` | The product ships for a whole business function (such as support, sales, marketing, HR, finance, or IT operations), not only a specialist craft. |
| 0.75 | `two_functions` | The product ships for two or more distinct business functions. |
| 1.00 | `general` | The product is a general work surface: people across the company can put their own work on it, whatever their function. |

Limits, on top of the common limits:

* `one_suite` caps at **0.75**: The product works only inside one vendor's application family for the work it covers.

* One business function, such as support or sales, is not a specialist craft. A specialist craft is a trade such as writing code, design, or video editing.
* Wrapping several agents of one craft, or a long feature list inside one craft, does not widen span.
* Do not fail a check because jobs are not pre-built (E.7), systems need connecting (E.3), or there is one surface (E.5).
* One suite means the product works only inside one vendor's application family, such as Microsoft 365, Salesforce, or one workspace product. A general surface that connects to many vendors' systems is not one suite.

### E.2 — Shared work

Several people, and an operator, can work on the same thing.

| Level | Check | Passes when |
| ----: | ----- | ----------- |
| 0.25 | `notify` | The product can notify other people about AI work, or share a link to it with them. |
| 0.50 | `team_account` | The product has team or organization accounts where members share a workspace. |
| 0.75 | `same_run` | Several people can open, continue, or contribute to the same AI conversation, run, or agent. |
| 1.00 | `live_thread` | People and the AI actor work together live in one shared thread or workspace, see the same state, and hand work off. |

* A chat notification that a run finished is not shared work. A channel where teammates and the operator talk in one thread is, when that thread is the work.
* Alerts to the same person on another device, or continuing one's own session elsewhere, are not `notify`. It needs another person.

### E.3 — System reach

The product reads and writes the systems where company work already lives.

| Level | Check | Passes when |
| ----: | ----- | ----------- |
| 0.25 | `own_artifacts` | The AI reads and writes the product's own artifacts, such as its repository, project, documents, or canvas. |
| 0.50 | `one_external` | The AI reads and writes at least one external system, or one suite's objects, that the company already runs. |
| 0.75 | `several_external` | The AI reads and writes several external systems of record, such as mail, tickets, CRM, files, or calendar, through shipped integrations. |
| 1.00 | `shipped_jobs` | The spec names systems the product reads and writes as part of shipped jobs, not only as available connectors. |
| 1.00 | `categories` | Those systems span more than one category, such as mail and CRM, or tickets and files. |

* The craft's own toolchain (for a coding product, the git host, CI, and package registry) counts as the product's own artifacts.
* Posting a message or a status update is not write-back. A connector name in a list is not read and write.
* Computer use that operates the company's apps with the credentials it is given is reach. Browsing the public web for an answer is not.
* Installing a listed application from the product's own catalog and signing in is not buyer wiring.

### E.4 — Extensible coverage

Coverage can grow through a catalog the product ships.

| Level | Check | Passes when |
| ----: | ----- | ----------- |
| 0.25 | `extensions` | The product supports plugins, extensions, or MCP servers that add tools, actions, or content. |
| 0.50 | `templates_directory` | The product offers official templates or starter agents for more than one job, or an organization-internal directory of agents, skills, or workflows. |
| 0.75 | `first_party_catalog` | The product ships a first-party catalog or marketplace of installable agents, skills, apps, or workflows. |
| 1.00 | `not_one_lane` | That catalog is not limited to one craft or one suite. |
| 1.00 | `open_publishing` | Third parties or customer organizations can publish into that catalog. |

Limits, on top of the common limits:

* `craft_catalog` caps at **0.25**: Every extension or catalog entry the spec shows serves one specialist craft, such as coding plugins for linters, repositories, and IDEs.

* E.4 grades the catalog as a way to grow: whether it exists, whether it is limited to one craft or suite, and who can publish. How finished each entry is counts on E.7.
* Community trust gates, such as a manager confirming an install, do not fail a check.
* Supporting more model or agent providers is not an extension. An extension adds tools, actions, or content the AI can use.

### E.5 — Work surfaces

Where that work can happen.

| Level | Check | Passes when |
| ----: | ----- | ----------- |
| 0.25 | `one_surface` | People can work with the AI in at least one surface, such as a web app, IDE, terminal, or chat. |
| 0.50 | `two_surfaces` | People can work with the AI in two or more distinct surfaces, such as web and desktop, or an IDE and a CLI. |
| 0.75 | `workplace_chat` | People can start or continue work from workplace chat, such as Slack or Teams, as a working surface and not only for notifications. |
| 1.00 | `mail_or_customer` | Work can happen through mail or a customer-facing channel, such as email, voice, SMS, or a website chat. |
| 1.00 | `api_embed` | A documented public API or embed lets work happen from other software. |

* Inbound webhooks that start a run are triggers, not surfaces. Status notifications in chat are not a working surface.
* Surfaces do not widen span.

### E.6 — Adoption path

A team can put work on the product without assembling the core system.

| Level | Check | Passes when |
| ----: | ----- | ----------- |
| 0.25 | `access` | The spec documents how an organization gets or turns on the product: sign-up, install, trial, a sales or partner engagement, or enabling it in an account it already has. |
| 0.50 | `start_path` | There is a documented way to start putting work on the product, such as self-serve sign-up, install, trial, or an onboarding guide. |
| 0.75 | `team_setup` | A team can be set up in the product: invites, roles, shared billing, or workspace setup. |
| 1.00 | `admin_no_services` | Documented administration and permissions let an organization roll it out without professional services or a custom build. |

Limits, on top of the common limits:

* `services_required` caps at **0.25**: The spec states the product works only after professional services, a forward-deployed team, or a custom platform build.

* Missing SSO does not fail a check when a team can still adopt the product. This is not a trust-center or changelog score.
* A documented start path, team setup, or rollout shows how the product is obtained. When a higher check passes, `access` passes too.

### E.7 — Ready-made coverage

A team reaches a working job without designing it by hand.

| Level | Check | Passes when |
| ----: | ----- | ----------- |
| 0.25 | `hand_built` | A person can build a job (an agent, workflow, or automation) in the product by hand. |
| 0.50 | `one_function` | The product offers ready-made jobs for at least one business function or craft, shipped, installable from its catalog, or generated from a plain-language description. |
| 0.75 | `two_functions` | Ready-made jobs exist for two or more business functions. |
| 1.00 | `no_wiring` | A non-specialist reaches a running job through one of those paths without a builder connecting tools, binding requirements, or setting triggers by hand. |

Limits, on top of the common limits:

* `craft_jobs` caps at **0.25**: Every ready-made job the spec shows serves one specialist craft.

* Three paths count: shipped (the vendor ships the job ready to turn on), installed (a finished job installs from the product's catalog), and generated (the product's AI builds the job from a plain-language description and a person reviews it).
* A catalog of connectors or plugins, not finished jobs, counts on E.3 and E.4, not here.

<!-- rubric:end -->

## 6. Count each gap once

| Fact | Where it counts | Where it does not |
| ---- | --------------- | ----------------- |
| Jobs are not pre-built | E.7 | E.1 |
| Systems of record need connecting | E.3 | E.1, E.7 |
| There is only one surface | E.5 | E.1, E.2 |
| The catalog has connectors, not finished jobs | E.4, E.7 | E.1 |
| Admin or trial is limited to one plan | E.6 | E.1, E.4 |
| The product is one specialist craft | E.1, and the span cap | a second failure on every other criterion, unless its limit names the craft |

## 7. Score

The scorer computes the score from the grades. You do not.

```text
raw = mean of E.1 through E.7
penalty = 0.25 × (1 − lowest grade) × raw
uncapped = clamp(raw − penalty, 0, 1)
if E.1 is below 0.50, score = min(uncapped, 0.49)
otherwise score = uncapped
```

The score is rounded to two decimals, half down.

## 8. Before you answer

* Whose work can go on the product today, and which functions have no native path?
* Can several people and an operator share the same work, or only a notification?
* Which systems of record can it read and write without the buyer wiring them?
* Does the catalog carry other functions, or only the same craft?
* Where does the work happen?
* Can an ordinary team adopt it without an SDK project or a services team?
* Can a team reach a working job by turning it on, installing it, or describing it?

Then challenge every failed check the other way: did you fail it for a fact the count-once table puts elsewhere?

## 9. Output

Return one JSON object with this shape:

```json
{
  "configuration": "Product, plan or edition, and any first-class wrap rated.",
  "summary": "Two to four sentences on what work an organization can put on the product today.",
  "criteria": [
    {
      "key": "E.3",
      "checks": [
        {"id": "own_artifacts", "passed": true, "quote": "text copied from the spec"},
        {"id": "one_external", "passed": true, "quote": "text copied from the spec"},
        {"id": "several_external", "passed": false, "quote": ""},
        {"id": "shipped_jobs", "passed": false, "quote": ""},
        {"id": "categories", "passed": false, "quote": ""}
      ],
      "limits": [
        {"id": "preview", "applies": false, "quote": ""},
        {"id": "buyer_wired", "applies": false, "quote": ""},
        {"id": "other_plan", "applies": false, "quote": ""}
      ],
      "note": "One or two sentences on the evidence and the limit that decide this criterion."
    }
  ],
  "gap": "The lowest criteria and the concrete missing evidence."
}
```

List every criterion from E.1 to E.7 in rubric order. Every check and every limit of each criterion appears once. A quote is required when `passed` or `applies` is true, and empty otherwise.

To score an answer by hand, save it as JSON and run `uv run intelligence-scale score answer.json --axis exec --spec <slug>`.
