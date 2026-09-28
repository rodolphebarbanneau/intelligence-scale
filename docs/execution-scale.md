# The Execution Scale

The **Execution Scale** rates how much of a company's work a product can carry as it ships.

The [Intelligence Scale](intelligence-scale.md) asks who gets the work done. This scale asks a different question:

> **Whose work fits on this product, and how far across the company can that work go?**

The two answers are independent. A coding agent that can own an engineering change can sit far to the right and still sit low here. A company-wide assistant that only amplifies people can sit high here and still sit left of center.

This is not a vendor-maturity score. It does not reward customer counts, logo walls, funding, a changelog, or a status page. It does not judge which foundation model is better, or how far the product sits on the Intelligence Scale.

The score runs from **0.00 to 1.00**. It judges the **chassis** an organization can adopt: the surfaces, jobs, systems, and catalog it ships today. A first-class wrap of another product counts only as this chassis exposes it — whose work still fits, who can share it, and whether an ordinary team can adopt the wrap without assembling the core. Wrapping several coding agents does not widen span beyond that craft. A product only one specialist craft can use cannot publish **0.50** or higher.

Be conservative. A current primary source is the basis for a full mark. Marketing language, launch posts, roadmap items, and "you could build this" leave a criterion low.

## How a criterion is graded

| Grade | Meaning |
| --- | --- |
| **1.00 — Native** | A current, supported, first-class capability or a documented fact directly satisfies the criterion. |
| **0.75 — Native but limited** | The fact is real, and it is beta, preview, narrowly scoped, or materially constrained. |
| **0.50 — Partial** | Official material shows meaningful progress, and the criterion is only partly met. |
| **0.25 — External or thin** | The criterion depends mainly on custom work, a third party, or a claim with weak public evidence. |
| **0.00 — Absent or unproven** | The criterion is absent, roadmap-only, or cannot be verified. |

A current primary source is required for **1.00**. Beta or preview cannot score above **0.75**. A claim inferred only from secondary sources cannot score above **0.50**. A connector name, a slogan, or a logo wall cannot raise coverage. When the evidence is ambiguous, the lower grade applies.

## What this scale is not

Do not raise a grade because the vendor is large, the product is generally available, or named customers exist. Those facts are not coverage.

Do not raise a grade because the product could theoretically do any job if the buyer assembled it. Generic APIs, MCP, and "you can build anything" stay at **0.25** or below unless the shipped catalog already carries other work. A platform that can cover every function only after an SDK project, custom actions, or a services team is not coverage as it ships.

A marketplace of coding plugins is still a coding marketplace. Shared Slack notifications are not multiplayer. A general chat box is not a path into the company's systems of record.

## E.1 — Domain span

Whose work fits on the product as it ships.

Span is about which work the product is for, not about who executes it. A general work surface can reach **1.00** even when its type score stays low. A coding product lands at **0.25**. A support product can still reach **0.50**. One business function, such as support or sales, is not a specialist craft.

| Grade | Meaning |
| --- | --- |
| **1.00** | People across the company can put their own work on it. More than one business function, in the product today. |
| **0.75** | Several functions, with a real limit: one suite, one family of departments, or the rest still in preview. |
| **0.50** | One business function, such as support or sales. The rest of the company has no native path onto it. |
| **0.25** | One specialist craft, such as writing code or editing video. Only that craft can use it. |
| **0.00** | Unproven, or the buyer has to build the product first. |

A current primary source is required for **1.00**. Functions that exist only in preview cannot lift the grade above **0.75**. A roadmap, a product the buyer must assemble before any work fits, or a claim with no source stays at **0.00**.

"One suite" means the product works only inside one vendor's application family, such as Microsoft 365, Salesforce, or a Notion workspace. A general work surface that connects to many vendors' systems is not one suite. Span is not lowered because jobs are not pre-built, because systems need connecting, or because there is only one surface. Those are E.7, E.3, and E.5.

When domain span is **0.25** or lower, the published score cannot reach the midline. A specialist-craft product sits with Niche or the Visionaries. It does not become a Challenger because it is polished.

## E.2 — Shared work

Can several people, and an operator, work on the same thing?

| Grade | Meaning |
| --- | --- |
| **1.00** | Native multiplayer: several people and an operator share a conversation, run, or workspace, hand work off, and see the same state. |
| **0.75** | A shared workspace or shared agent exists, and live collaboration is limited, preview, or missing the operator in the same thread. |
| **0.50** | The organization has a team account. Work itself stays single-player, and sharing is after the fact (a pull request, an export, a transcript). |
| **0.25** | Notifications, a share link, or a channel mention. Nobody else is in the work. |
| **0.00** | Single-player only, or unproven. |

A Slack or Teams *notification* that a run finished is **0.25**. A channel where teammates and the operator talk in one thread can be **0.75** or **1.00** when that thread is the work, not a status ping.

## E.3 — System reach

Can the product read and write the systems where company work already lives?

| Grade | Meaning |
| --- | --- |
| **1.00** | Native read and write into several systems of record the company already runs — mail, tickets, CRM, files, calendar, or the equivalent — as shipped jobs. |
| **0.75** | Reach into several systems, with a real limit: one suite, read-heavy connectors, or write-back incomplete. |
| **0.50** | Reach into one system or one suite's objects. |
| **0.25** | The product operates only on its own artifacts (a repository, a project, a canvas), or the buyer must wire generic tools. |
| **0.00** | Conversation or generation only, or unproven. |

Computer use that can operate the company's apps is evidence of reach. Computer use that browses the public web for an answer is not. A connector name in a list is not write-back.

Installing a listed application from the product's own catalog, then supplying its credentials or signing in, is not "the buyer wires generic tools". It can reach **0.75** when that catalog reaches several systems with write-back. **1.00** still needs named systems of record the product documents reading and writing as shipped jobs.

## E.4 — Extensible coverage

Can coverage grow into other use cases through a catalog the product ships?

E.4 grades the catalog as a way to grow: whether it exists, whether it is limited to one craft or suite, and who can add the next entry. How finished each entry is belongs to E.7.

| Grade | Meaning |
| --- | --- |
| **1.00** | A first-party marketplace or directory of installable agents, skills, apps, or workflows. It is not limited to one craft or one suite, and the vendor, third parties, and customer organizations can publish into it. |
| **0.75** | A real catalog exists, with a real limit: one suite or one family of jobs, closed to third-party publishing, mostly connectors, or preview. |
| **0.50** | Official templates or starter agents for more than one job, or an organization-internal directory, but not a marketplace. |
| **0.25** | Extensions, plugins, or MCP that a builder assembles, or a catalog that stays inside one craft. |
| **0.00** | No catalog, or unproven. |

- Growing coverage only through an SDK, custom actions, MCP the buyer wires, or a forward-deployed team stays at **0.25**, even if templates exist.
- A catalog open to community publishing is a strength. Community trust gates, such as a manager confirmation on install, do not lower it.

Plugins for linters, repos, and IDEs stay at **0.25**. "You can build anything with MCP" is **0.25** or below.

## E.5 — Work surfaces

Where can that work happen?

| Grade | Meaning |
| --- | --- |
| **1.00** | Native surfaces across the places company work already happens: the product UI plus workplace chat, mail or a customer channel, and an API or embed. |
| **0.75** | Several surfaces, with a real limit: one suite's apps, or a major channel still in preview. |
| **0.50** | Two surfaces (for example web and Slack, or an IDE and a CLI). |
| **0.25** | One surface: a single web app, an IDE, a terminal, or a chat box. |
| **0.00** | Unproven. |

Surfaces do not raise domain span. A coding agent with an IDE, a CLI, and Slack is still a coding product. Many customer channels for one support agent can still be high here and mid on span. Inbound webhooks are a trigger, not a place where people work. A documented public API or embed counts as a surface.

## E.6 — Adoption path

Can a team put that work on the product as it ships, without assembling the core system?

| Grade | Meaning |
| --- | --- |
| **1.00** | Documented administration, permissions, and a trial, install, or onboarding path so ordinary teams can put work on it today. |
| **0.75** | The path exists, and it is limited: one plan, preview admin, or thin documentation. |
| **0.50** | An individual can start. Organization administration is thin. |
| **0.25** | The product works only after the buyer assembles the core from generic APIs. |
| **0.00** | Unproven, waitlist-only, or no way to start. |

Ask whether an ordinary team can put work on it and add the next job without assembling a platform.

- A documented install, trial, or admin path for ordinary teams can still reach **1.00**.
- A path that exists only for one plan, or that needs a specialist to finish setup, stays at **0.75** or **0.50**.
- A product that works only after professional services, a custom platform build, or generic APIs stays at **0.25** or below.

This is not a trust-center, changelog, or interface-taste score. Missing SSO does not fail the criterion when a team can still adopt the product. A pile of APIs with no product around them stays at **0.25** or below.

## E.7 — Ready-made coverage

How quickly does a team get a working job, without designing the agent by hand?

A product may start empty. That is not a gap when the product itself gets the team to a running job. Three paths count:

- **Shipped** — the vendor ships the job ready to turn on.
- **Installed** — a finished job (an agent or workflow with its requirements declared) installs from the product's catalog, including community listings.
- **Generated** — the product's own AI builds the job from a plain-language description (instructions, tools, and triggers) and a person reviews it.

| Grade | Meaning |
| --- | --- |
| **1.00** | For several business functions, a team reaches a running job through one of those paths without a specialist: turn it on, install it, or describe it and approve what the product builds. |
| **0.75** | A path exists for several functions, with a real limit: one suite or one family of departments, or what the product installs or generates still needs a builder to connect tools, bind requirements, or set triggers. |
| **0.50** | Ready-made jobs for one business function, or starter templates and prompts a non-specialist still has to finish. |
| **0.25** | A blank canvas, a general assistant, or jobs that stay inside one craft. The buyer writes every job by hand. |
| **0.00** | Unproven. |

A transversal chat box with no shipped jobs and no builder can still score well on domain span and poorly here. A support agent that arrives ready to take conversations can score **0.50** here and **0.50** on span. A builder canvas that can do anything only after an SDK project or a services engagement is still a blank canvas. A catalog of connectors or plugins, not finished jobs, counts on E.3 and E.4, not here.

## Count each gap once

One missing fact lowers the one criterion it belongs to. It is not charged again elsewhere.

| Fact | Where it counts | Where it does not |
| --- | --- | --- |
| Jobs are not pre-built | E.7 | E.1 |
| Systems of record need connecting | E.3 | E.1, E.7 |
| There is only one surface | E.5 | E.1, E.2 |
| The catalog has no finished jobs, only connectors | E.4, E.7 | E.1 |
| Admin or trial is limited to one plan | E.6 | E.1, E.4 |
| The product is one specialist craft | E.1, and the span cap | a second penalty on every row, unless that row's table names the craft |

## The score

The raw score is the arithmetic mean of E.1 through E.7. One weak criterion cannot be averaged away. The penalty is a quarter of the gap between a full mark and the lowest grade. When domain span is **0.25** or lower, the published score is also capped below the midline. A span of **0.50** or **0.75** is not capped. It still enters the mean, and it sets the penalty when it is the lowest grade.

```text
raw = arithmetic mean of E.1 through E.7
penalty = 0.25 × (1 − lowest grade)
uncapped = clamp(raw − penalty, 0, 1)
if E.1 is 0.25 or lower, score = min(uncapped, 0.49)
otherwise score = uncapped
```

**0.49** is the highest published score below **0.50**. Apply the cap before rounding. The result is kept between 0 and 1 and published to two decimal places, with halves rounded down. `0.625` becomes **0.62**.

Six criteria at **1.00** and a domain span of **0.25** produce an uncapped score near **0.71**. The cap publishes **0.49**, so the product sits with Niche or the Visionaries. It does not stay a Challenger.
