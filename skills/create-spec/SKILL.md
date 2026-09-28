---
name: create-spec
description: Write or rewrite a product dossier in specs/. Use when adding a spec, refreshing a spec, or aligning dossiers to one format. Produces a detailed summary of what the product is and does, plus an exhaustive sourced feature list. Prefers the official docs site. Does not answer Intelligence Scale or Execution Scale criteria.
---

# Create spec

Write `specs/<slug>.md` as a sourced product dossier. Later ratings treat this file as the brief and may open only the URLs it cites. A missing fact cannot be scored later. Write the product, not the score.

## What a spec is

A detailed summary of what the product is and does, and an exhaustive list of its features, each tied to a source.

The rated object is the product an organization can adopt, not the model inside it. Related products (chat vs coding agent vs workspace agents) get their own files. When this product starts or steers another product as a first-class provider, write that wrap as a product fact: what it launches, what it surfaces, and what it leaves on the other product's native UI. Do not score the wrap.

## What a spec is not

Do not write a reply to the Intelligence Scale or the Execution Scale. Do not pre-score, hint at grades, or organize the file around those criteria.

Do not use these sections or headings:

- What is being rated
- Evaluation scope
- Capability notes
- Execution notes
- Assistance, human direction, process ownership, coordination, persistence
- Production readiness, dependability, proven use, stewardship, shipping record, operability
- Domain span, shared work, system reach, extensible coverage, work surfaces, adoption path, ready-made coverage, span of work
- What is not established here

Do not mention Type I / II / III, E.1–E.7, native vs composable, or published scores. Do not write “this does not establish…” or “a rater should not…”. Those sentences belong in an evaluation, not in the dossier.

Do not pad with “unproven” lists. If the official pages do not describe a feature, omit it.

## File

Path: `specs/<slug>.md`

`slug` is lowercase ASCII, digits, and hyphens. It matches the filename. Keep an existing slug when rewriting a file.

Frontmatter:

```yaml
---
name: Product name
slug: product-slug
url: https://product.example/
docs: https://docs.product.example/
kind: product
reviewed: YYYY-MM-DD
# draft: true
---
```

- `name` is the product as the vendor names it.
- `url` is the public product URL.
- `docs` is the official documentation root. Omit the field when there is no docs host.
- `kind` is `product` unless the user names another kind.
- `reviewed` is the date of this research, ISO `YYYY-MM-DD`.
- `draft` is optional. Set `draft: true` while the dossier is unfinished. Draft specs can be rated in a `test-` run. Published releases and the GitHub evaluation workflow skip them. Omit the field, or set `false`, when the spec is ready to ship.

The `#` heading matches `name`.

## Research

Prefer the official **docs site** as the best source. When a docs page and a marketing page disagree, keep the docs page.

Work in this order:

1. Find the official documentation host and walk its navigation: overview, every product surface, integrations, admin, security, billing, changelog.
2. Fill gaps from the official help center, API reference, changelog, pricing, and trust or security pages.
3. Use the product homepage only for identity and for facts the docs do not cover.
4. Use an official blog or announcement only when no docs page states the fact.
5. Do not take features from unofficial recaps, social posts, or secondary roundups.

Open the pages. Do not invent a feature from a nav label or a slogan. Label beta, preview, or experimental the way the docs do. Skip roadmap, waitlist-only, and unreleased items.

When there is no docs site, say so in **Product** and write only what official pages actually specify. A thin official record stays thin.

## Body

Use this shape and no other top-level sections:

```markdown
# Product name

## Product

## Features

### Surface or area as the vendor names it

## Sources
```

### Product

Several paragraphs, present tense, specific.

Cover what the product is, who it is for, where it runs, how someone uses it, and which edition or plan the docs describe when that splits the product. Name sibling products that are out of scope and, if those specs exist, their slugs. If this product wraps other agents as supported providers, name them and say what this product owns versus what stays with the provider.

Write as a product description, not as a brief for a rater. No scores. No “the model is not the rated object” boilerplate — one sentence that the product is the chassis is enough when the vendor also sells models.

### Features

Exhaustive. Group by the product’s own surfaces or doc sections, not by rating axes.

Walk the docs until every documented capability is in a bullet: editor and agents, channels, tools, integrations, triggers, memory, permissions, admin, security, compliance, billing, install, APIs. If the vendor documents it as something the product does, it belongs here.

Each group starts with its primary docs URL. A bullet that comes from another page cites that page.

```markdown
### Cloud Agents

Primary source: https://cursor.com/docs/cloud-agent

- Run in isolated virtual machines with cloned repositories, dependencies, secrets, startup commands, and network access.
- Start from the iOS app, cursor.com/agents, the desktop app, Slack, a GitHub or Bitbucket comment, Linear, or an API.
- Enterprise plans can run team and enterprise-managed hooks, including checks before shell execution and after file edits. Source: https://cursor.com/docs/cloud-agent#hooks
```

Rules:

- One feature per bullet. One or two factual sentences.
- Use the vendor’s names (`Cloud Agents`, `Custom Agents`, `Ghostwriter`).
- Do not interpret (“this is only coding work”, “this is not a business process”).
- When the product wraps another agent, record what this product starts, what it surfaces, and what the docs say stays on the provider. That is a product fact, not a grade.
- Do not drop admin, security, or pricing because they feel like execution topics. They are product facts.
- Do not copy marketing adjectives (`powerful`, `leading`, `autonomous`) unless you are quoting a named claim and citing it.
- Named customers, counts, and case studies stay only if an official page states them, as vendor-published facts, not as proof of adoption.

### Sources

List every URL used above. Documentation first, then help, API, changelog, pricing, trust, product site, then any official announcement.

Do not list a URL that supports no sentence in the file.

## Voice

- Present tense, short sentences, no hype.
- Facts the pages state. No synthesis toward a type or an execution grade.
- Same structure for every product, whether the vendor is a chat app, a coding agent, or a support platform.

## Done when

- The file is `specs/<slug>.md` with valid frontmatter.
- **Product** explains the thing without referring to the scales.
- **Features** is grouped by vendor surfaces and is exhaustive against the docs nav.
- Every bullet is backed by a cited official URL, with the docs site preferred.
- **Sources** is docs-first and has no unused links.
- No rating headings, no grades, no “not established” closers.
