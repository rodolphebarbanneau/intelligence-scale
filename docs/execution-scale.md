# The Execution Scale

The **Execution Scale** rates how much of a company's work a product can carry as it ships.

The [Intelligence Scale](intelligence-scale.md) asks who gets the work done. This scale asks a different question:

> **Whose work fits on this product, and how far across the company can that work go?**

The two answers are independent. A coding agent that can own an engineering change can sit far to the right and still sit low here. A company-wide assistant that only amplifies people can sit high here and still sit left of center.

This is not a vendor-maturity score. It does not reward customer counts, logo walls, funding, a changelog, or a status page. It does not judge which foundation model is better, or how far the product sits on the Intelligence Scale.

The score runs from **0.00 to 1.00**. It judges the **chassis** an organization can adopt: the surfaces, jobs, systems, and catalog it ships today. A first-class wrap of another product counts only as this chassis exposes it. Wrapping several coding agents does not widen span beyond that craft. A product only one specialist craft can use cannot publish **0.50** or higher.

## How a criterion is graded

A product is rated from its spec in `src/specs/` and nothing else. Every criterion has four levels, **0.25**, **0.50**, **0.75**, and **1.00**, and each level has yes/no checks written in the [execution rubric](https://github.com/rodolphebarbanneau/intelligence-scale/blob/main/src/exec.yaml). A model answers the checks and quotes the spec for every check it passes. The scorer turns the answers into a grade:

* A check whose quote is not in the spec fails.
* The grade is the highest level whose checks all pass, plus a share of the next level.
* Preview features cap a criterion at **0.75**. A capability the buyer must wire from generic APIs or MCP caps it at **0.25**. Evidence that holds only on another plan caps it at **0.50**.

The tables below summarize the levels. The rubric holds the exact checks.

A connector name, a slogan, or a logo wall passes no check. Generic APIs, MCP, and "you can build anything" are not coverage as it ships. A marketplace of coding plugins is still a coding marketplace. Shared Slack notifications are not multiplayer.

## E.1 — Domain span

Whose work fits on the product as it ships. Span is about which work the product is for, not about who executes it.

| Level | Reached when |
| --- | --- |
| **0.25** | The product ships for some kind of work, such as a specialist craft. |
| **0.50** | It ships for a whole business function, such as support or sales. |
| **0.75** | It ships for two or more business functions. |
| **1.00** | It is a general work surface: people across the company put their own work on it. |

Working only inside one vendor's application family, such as Microsoft 365 or Salesforce, caps span at **0.75**. Span is not lowered because jobs are not pre-built, systems need connecting, or there is one surface. Those are E.7, E.3, and E.5.

When span is below **0.50**, the published score cannot reach the midline. A specialist-craft product sits with Niche or the Visionaries.

## E.2 — Shared work

Can several people, and an operator, work on the same thing?

| Level | Reached when |
| --- | --- |
| **0.25** | The product can notify others or share a link. |
| **0.50** | Team or organization accounts share a workspace. |
| **0.75** | Several people can open, continue, or contribute to the same conversation, run, or agent. |
| **1.00** | People and the AI actor work live in one shared thread, see the same state, and hand work off. |

## E.3 — System reach

Can the product read and write the systems where company work already lives?

| Level | Reached when |
| --- | --- |
| **0.25** | It reads and writes its own artifacts, such as a repository, project, or canvas. |
| **0.50** | It reads and writes one external system, or one suite's objects. |
| **0.75** | It reads and writes several external systems of record, such as mail, tickets, CRM, files, or calendar, through shipped integrations. |
| **1.00** | Those systems are read and written as part of shipped jobs, in more than one category. |

For a coding product, the git host, CI, and package registry are its own artifacts. Posting a message or a status update is not write-back. Computer use that operates the company's apps is reach. Browsing the public web is not.

## E.4 — Extensible coverage

Can coverage grow through a catalog the product ships? How finished each entry is belongs to E.7.

| Level | Reached when |
| --- | --- |
| **0.25** | It supports plugins, extensions, or MCP servers. |
| **0.50** | It offers official templates or starter agents for several jobs, or an internal directory. |
| **0.75** | It ships a first-party catalog of installable agents, skills, apps, or workflows. |
| **1.00** | That catalog is not limited to one craft or suite, and third parties or customers can publish into it. |

A catalog whose entries all serve one specialist craft caps this criterion at **0.25**.

## E.5 — Work surfaces

Where can that work happen?

| Level | Reached when |
| --- | --- |
| **0.25** | One surface, such as a web app, IDE, terminal, or chat box. |
| **0.50** | Two or more distinct surfaces. |
| **0.75** | Work starts or continues from workplace chat, such as Slack or Teams, not only notifications there. |
| **1.00** | Work also happens through mail or a customer channel, and through a documented API or embed. |

Surfaces do not widen span. Inbound webhooks are triggers, not places where people work.

## E.6 — Adoption path

Can a team put that work on the product as it ships, without assembling the core system?

| Level | Reached when |
| --- | --- |
| **0.25** | The spec says how to get the product. |
| **0.50** | There is a documented way to start: sign-up, install, trial, or an onboarding guide. |
| **0.75** | A team can be set up: invites, roles, shared billing, or workspace setup. |
| **1.00** | Documented administration and permissions let an organization roll it out without services or a custom build. |

A product that works only after professional services or a custom platform build caps this criterion at **0.25**. Missing SSO does not fail it when a team can still adopt the product.

## E.7 — Ready-made coverage

How quickly does a team get a working job without designing it by hand? A job counts when it is shipped, installs from the product's catalog, or is generated by the product's AI from a plain-language description.

| Level | Reached when |
| --- | --- |
| **0.25** | A person can build a job by hand. |
| **0.50** | Ready-made jobs exist for at least one function or craft. |
| **0.75** | Ready-made jobs exist for two or more business functions. |
| **1.00** | A non-specialist reaches a running job without a builder connecting tools, binding requirements, or setting triggers. |

Ready-made jobs that all serve one specialist craft cap this criterion at **0.25**.

## Count each gap once

One missing fact lowers the one criterion it belongs to. It is not charged again elsewhere.

| Fact | Where it counts | Where it does not |
| --- | --- | --- |
| Jobs are not pre-built | E.7 | E.1 |
| Systems of record need connecting | E.3 | E.1, E.7 |
| There is only one surface | E.5 | E.1, E.2 |
| The catalog has no finished jobs, only connectors | E.4, E.7 | E.1 |
| Admin or trial is limited to one plan | E.6 | E.1, E.4 |
| The product is one specialist craft | E.1, and the span cap | every other criterion, unless its limit names the craft |

## The score

The raw score is the arithmetic mean of E.1 through E.7. One weak criterion cannot be averaged away. The penalty is a quarter of the gap between a full mark and the lowest grade. When domain span is below **0.50**, the published score is also capped below the midline.

```text
raw = arithmetic mean of E.1 through E.7
penalty = 0.25 × (1 − lowest grade)
uncapped = clamp(raw − penalty, 0, 1)
if E.1 is below 0.50, score = min(uncapped, 0.49)
otherwise score = uncapped
```

**0.49** is the highest published score below **0.50**. Apply the cap before rounding. The result is published to two decimal places, with halves rounded down. `0.625` becomes **0.62**.
