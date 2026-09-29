---
name: Plateforme
slug: plateforme
kind: product
reviewed: 2026-09-28
draft: true
---

# Plateforme AI

## Product

Plateforme AI is a collaborative workspace product for user, organization, and enterprise accounts. A workspace is the account a person is working in: a personal workspace is the user account; an organization or enterprise workspace is that account. People build reusable assets — agents, skills, applications, workflows, and reports — cut immutable releases, optionally distribute them on a marketplace, and run them as instances: agent instances, deployments, connections, actions, and dashboards. They talk in chats (Message, Ask, Run, and Build), operate through licensed Operators, automate with Workflows that become Actions, and observe with Reports that become Dashboards. Chat, operators, actions, and dashboards share the same access rules and the same billing.

Outside the web product, a public API prompts agents directly. Integrations with workplace tools such as Slack and mail are handled by applications installed from the marketplace.

There is no public product URL or documentation host. This dossier is written from the vendor’s product source-of-truth document. Plan figures below are that document’s designed grid; it states that published prices on a plans page are the commercial source of truth when that page exists.

The product is the workspace chassis: assets, instances, operators, grants, and licenses. A model is chosen on the agent instance or the turn. The agent asset itself does not carry a model.

A user is a person and may belong to many organizations. An organization is a shared workspace with members, roles, teams, and its own billing. An enterprise is an organization that can manage other accounts, register a tenant, and buy enterprise SaaS. A managed user or organization is linked to an enterprise; the enterprise is the default payer. A managed person has no personal plan; their personal workspace is billed by the enterprise.

Four independent licenses — SaaS, AI seats, Pool, and Operator — each gate only their own thing. None requires another. Money is in dollars. Compute and tokens are billed separately. No sibling product specs are in scope.

## Features

### Accounts, workspaces, and people

- Account types are user, organization, and enterprise.
- Workspace membership roles are owner, manager, member, and guest.
- Settings that change the account need manager or owner.
- Checkout, the customer portal, and the pay-as-you-go cap need the owner.
- Team membership is separate from role.
- Owners and managers invite by email, with a role and optional teams.
- Invitations expire, can be resent or revoked, and are accepted or declined on a public preview page. Sign-in is required to accept.
- Accepting an invitation counts against purchased SaaS seats, including pending invites.
- People pages show role, teams, AI seat, and join date. The last owner cannot be removed.
- Member detail shows that person’s teams and seat.
- Teams nest, with a depth limit. A child team’s members inherit the parent team’s BUILD permissions and RUN grants.
- Team pages are Members, Teams, Assets, Instances, and Settings.
- Sign-in is a standard account session with email verification and OAuth sign-in.
- Avatars and listing images are uploaded. They are never a free URL.
- Personal access tokens and session management live under user Settings → Developer.
- The product remembers the last workspace. A one-shot `?context=<alias>` enters another workspace and is then stripped. A stale memory falls back to the personal workspace.

### Access

- The strongest matching grant or permission wins.
- BUILD permissions on assets, instances, and operators are cumulative: read < triage < write < maintain < admin.
- A manager or owner of the workspace is admin everywhere.
- Organizations set base permissions and creation flags per kind (who may create agents, applications, and so on).
- On an asset, read may view draft, files, releases, and contributors; star; and use a release.
- On an asset, triage may edit About (description, tags) and deprecate or undeprecate a release.
- On an asset, write may edit files and configuration and cut a release.
- On an asset, maintain may rename the slug and manage the marketplace listing (distribute, image, links).
- On an asset, admin may set visibility, archive or restore, delete, and change permissions.
- On an instance, read may view, select in the composer, and probe.
- On an instance, triage may start or stop a deployment.
- On an instance, write may edit settings, bindings, model, source values, and secrets.
- On an instance, maintain may rebind to another release and rename the slug.
- On an instance, admin may delete and change permissions.
- On an operator, read may view, open the runs list, and see session metadata.
- On an operator, triage may enable or disable the operator and cancel a run.
- On an operator, write may set identity, primary agent, and triggers, and use the operator in a composer turn.
- On an operator, maintain may edit the environment (repositories, setup, egress).
- On an operator, admin may manage secrets, license, memory edits, discard sessions, delete, and change permissions.
- The last human admin on an asset cannot be removed. Operators cannot be that last admin.
- Anyone may read a public asset, including signed-out visitors. Private assets need permissions, base permissions, or manager+.
- Visibility alone never lists an asset.
- RUN grants on chats, projects, actions, and dashboards are read < write < manage. The creator gets manage. At least one manage grant must remain.
- Operators may hold read or write on RUN objects, never manage.
- On a chat, read may read the thread; write may send, stop, regenerate, vote, and trailing-delete; manage may set title, label, and project, delete, change grants, and create a share link.
- On a project, read may read the project and its recent chats; write may edit instructions and files and start a chat in the project; manage may edit details, archive, delete, and change grants.
- Documents follow their chat. Files follow the chat or the uploader.
- Project knowledge is injected only when the sender may write that project.
- If no manage grant resolves to an active member, remaining writers may claim manage.
- Managers see metadata at Settings → Access → Ownerless and may assign manage to someone already granted, or delete. A fully private orphan can only be deleted.
- Workspace owner or manager does not get implicit access to chats.
- Share links are gated by the workspace openness dial: anyone (works signed-out), members (only members of the owning account), or restricted (links cannot be created; existing ones resolve for nobody).
- Personal workspaces behave as anyone.
- Recipients fork a share-link snapshot into a workspace they pick, or sign in first. Fork is explicit and idempotent per target workspace.
- Without a session, a visitor can read workspace overview and public asset pages, the marketplace, share links when openness allows, and search over public names.
- Instance pages, operators, settings, chat (except a share link), library, projects, feed, actions, and dashboards require a session. Instance lists are members only.

### Assets

- Every asset has a name, slug, alias (`account/slug`), description, and tags (lowercase topics, at most 20).
- Visibility is public or private.
- Distribute on the marketplace is opt-in. A private listing needs a paid SaaS tier.
- Files have GitHub-like history: `main`, release versions, commit history, and compare. `README.md` is required. The license, when present, is a `LICENSE` file.
- Releases are immutable semver snapshots (patch, minor, major) with a changelog. A release that did not change is refused.
- Deprecate flags a release. Installed instances keep resolving it.
- Contributors are derived from who committed.
- Stars are a personal bookmark of an asset, shown on personal workspaces, not organizations. Assets have no image; the marketplace card image is on the listing.
- A pin is an overview highlight of up to six assets of the workspace.
- Settings are General (slug, danger zone), Permissions, and Marketplace.
- Delete, archive, slug, and visibility live only in the danger zone.
- Content is Files | Configuration, plus an About pane (description, tags, stars, releases, marketplace, contributors). Cut release is on the Content toolbar.
- Name, description, and tags are edited from About, not Settings.
- History shows commits by day, a commit page with diffs, and compare between two refs. Concurrent edits that race are rejected; the editor reloads.
- Create routes are `/new/agent`, `/new/application`, `/new/skill`, `/new/workflow`, and `/new/report`. The header “+” lists them. Optional `?workspace=` preselects the context field.

### Agents

- An agent is a reusable AI specification: instructions (`INSTRUCTIONS.md` body), run options, pinned skill releases, and application requirements. There is no model on the agent.
- Run options are retries, effort, reasoning, service tier, context window, temperature, style, and verbosity.
- Asset dependencies run Agent → skill → application only. There is no agent-to-agent or skill-to-skill asset dependency.
- One application per agent: a key and an application are one-to-one. The requirement key is the tool namespace the model sees.
- At release, the agent’s requirements and those of reachable pinned skills merge by application: same key, highest version, required if any side requires it.
- Inherited rows show “Required by *skill*” and cannot be removed from the agent.
- A required skill or application must be released to cut. A recommended one may stay unbound when the release is used.
- Create is at `/new/agent`. “Use in a workspace” opens the one creation dialog used everywhere instances are created.

### Skills

Primary source: https://agentskills.io

- A skill is a reusable procedural package in the Agent Skills format: `SKILL.md` is required, with optional `scripts/`, references, and assets.
- Configuration covers compatibility, allowed tools, extra attributes, and application requirements. The license is the `LICENSE` file.
- Skills have no instance. Skills have no Instances tab.
- Skills are saved to a workspace from the marketplace. The composer skill picker is the workspace’s released skills plus its saved skills.
- Scripts run in the chat’s computer (the chat sandbox or the selected operator).
- Community skills that ship scripts require a manager confirmation on save.

### Applications

- An application is reusable access to tools, data, and actions. Applications expose tools and resources. Two kinds are chosen at create: deployment (the platform runs it) and connection (a remote server).
- A deployment has named sources, mixed freely: HTTP APIs and databases. Each tool or resource file names its source.
- A setting is fixed by the release or filled by the installing workspace. Secrets never live in the draft or the release. The installer supplies passwords and API keys on the deployment.
- A connection points at a remote tool server. Transport is streamable HTTP.
- Connection auth is none, a static header, or OAuth (scopes, optional issuer, dynamic registration when the server supports it).
- The person who will use an OAuth connection must Connect once. Missing identity stops the run and opens an issue.
- Operators do not use a person’s OAuth identity. They may use none or static connections.
- Applications may require human approval for mutating tools (`approval required`).
- Create is at `/new/application`. Header actions are Deploy or Add.
- A `read-only` hint keeps a tool available in Ask and Build. Destructive tools should require approval in Run.
- Requirement keys must not collide in one run.

### Workflows

- A workflow is a releasable orchestration: steps, agents, operators, applications, conditions, human approvals, and triggers.
- Triggers are schedule, webhook, workspace event (release cut, asset published, install, member joined), or start from this chat.
- A workflow has inputs and outputs. An execution may open or attach a chat so people can see and intervene.
- A workflow uses the same draft, files, releases, and marketplace rules as other assets.
- A workflow does not run until someone or a trigger creates an Action.
- A working chat can be promoted into a workflow when the pattern should repeat.

### Reports

- A report is a releasable definition of an observational view. It declares the application capabilities it needs, using the same requirement idea as agents.
- Widgets include usage, outcomes, listings, action history, and custom views fed by those applications.
- A report uses the same draft, files, releases, and marketplace rules as other assets.
- A report does not show live data until someone creates a Dashboard in a workspace and binds the applications.

### Instances

- Instances are what a workspace runs: agent instance, deployment, connection, action, or dashboard. One namespace per workspace. Slugs are unique across kinds. Instances are never public and never publishable.
- Creation is always explicit. The same dialog serves asset pages, release cards, marketplace Add, and the composer “Add agent…”.
- Workspace Instances lists All, Agents, Applications (deployments and connections), Actions, and Dashboards, plus Operators.
- An asset’s Instances tab lists that asset’s instances in the current workspace.

### Agent instances

- An agent instance is an agent release realized in a workspace: model, settings overrides, and bindings of requirements to deployments or connections. The composer selects an agent instance.
- Bindings prefill with compatible deployments or connections (same application, pinned release or newer).
- Install missing is on by default and installs required unbound applications from the marketplace. Recommended slots are never auto-installed.
- The model sees the same requirement-key names in every workspace. Applications attached only to one chat keep the instance slug as prefix.

### Deployments

- Create a deployment with a release, name or slug, and source values and secrets. Every required field must be filled before create.
- Incomplete deployments stay Needs configuration and cannot start.
- The page edits values (Replace / Clear on stored secrets), shows missing fields, and disables Start until complete.
- The page supports start, stop, status, and probe. “Update available” offers Rebind to a newer release.
- If the listing later goes private or unlisted, the instance keeps working, warns, and cannot rebind.

### Connections

- Create a connection with a release and an optional static secret or pre-registered OAuth client.
- Connect / Disconnect is per user. Probe lists tools.
- Settings → Connections lists the person’s identities across workspaces. Each can be revoked.

### Actions

- An action is a running job of a workflow in a workspace: a workflow release bound to agents, operators, and applications.
- Status is queued, running, waiting for approval, completed, failed, or cancelled.
- An action may attach a chat. The execution writes there; people and operators participate.
- An action starts from the workflow’s triggers or by hand.
- Access is RUN grants. Operators may be granted write so they can start or continue steps. They cannot manage the action.

### Dashboards

- A dashboard is a report release realized in a workspace, bound to the application instances the report requires.
- Widgets are pinnable on the workspace overview and the Dashboards area.
- A dashboard is live while the bound applications are readable. Access is grants, not visibility.

### Chat and the composer

- Chat is the only conversation. Humans, operators, and the assistant write into the same thread. Workflow actions that want a conversation attach to a chat.
- The current person’s messages are on the right. Other people and operators are on the left, with a name. The assistant is a bare answer (markdown, tools, documents), not a person bubble.
- Message is a channel post with no model. `@Operator` dispatches. Message is the default when more than one human is granted, and is hidden when the chat is not a channel.
- Ask is a conversational answer with read-only tools, skills, web, and documents. It is the default when the chat is not a multi-human channel.
- Run is agentic execution using tools. Approvals apply to mutating tools. Run uses the chat’s computer and never uses Build tools.
- Build is agentic execution editing assets. It uses Build tools plus read-only tools, and uses the chat’s computer for authoring.
- Shortcuts are Shift+Mod+1 through 4 for Message, Ask, Run, and Build. Message, Ask, Run, and Build are otherwise always available as listed above.
- The assistant may suggest a mode with a reason. Approve within a few seconds or dismiss; the turn continues either way.
- The agent selector lists workspace agent instances plus “Add agent…”. None uses the platform default assistant.
- The model selector uses the workspace registry. The instance model is preselected. Virtual ids are `default` and `auto`.
- Settings expose effort, reasoning, service tier, and context window — only what the selected model supports.
- The environment row (Run / Build only) is No operator (chat sandbox) or a licensed operator the member may use. The choice is remembered per chat.
- Environment status is sleeping, waking, or active, plus “files restored” or “files not kept” when a sandbox snapshot exceeded its cap. On an operator, the row shows the chat’s branch. Ask does not use the computer.
- The Web switch is on by default and remembered per chat. On: search the web and fetch pages or pasted URLs. Off: no outbound fetch.
- Capability chips show attached applications and skills, “*Skill* needs *Application* · Attach”, and “Web off”.
- Typed triggers fire only after whitespace or at the start: `@` for people on the chat (or greyed “Not in this chat” with Share with…) and for context (files, documents, chats, projects); `+` for files, applications, skills, Web, and mode; `/` for commands.
- A pick becomes a chip. Typed text that was never picked stays text.
- Action commands run at once with no model: `/rename`, `/pin`, `/unpin`, `/label`, `/project`, `/branch`, `/share`, `/new`. They are shown only when the person may do that.
- `/summarize` is a read-only summary. In Message it switches the turn to Ask.
- URLs become link chips. With Web on they are fetched as sources. With Web off they stay text.
- Ask uses read-only tools, skill instructions, web search and fetch, and documents. It reads operator memory if an operator is selected, never writes it, and never starts the computer.
- Run uses all tools (mutating ones wait for approval), skills including scripts, web, planning, the chat’s computer, and operator memory updates when an operator is selected.
- Build uses read-only application tools, skills, web, planning, the computer for authoring and testing, and built-in Build tools (list, create, and update drafts of agents, skills, and applications; cut a release). Each Build tool uses the person’s session and asks for approval.
- Web search is billed per call. Fetching a page has no per-call price; the text counts as model input. BYOK never covers search.
- Chat features include pins (per user), labels, project membership, votes, branch, trailing delete, unread cursor, live run state, share link, and grants.
- Titles and labels may be filled automatically. That work is platform-absorbed and not billed.
- Sidebar history shows date, unread, label, project, and pinned.
- A visible viewer marks the chat read. Hidden tabs do not.

### Projects, library, documents, and files

- A project is a shared space: details, instructions, files, recent chats, and grants. Starting a chat inside a project attaches it.
- The library lists Chats, Documents, and Files. Documents lists bookmarks the person may still open.
- Documents are durable artifacts created in chat (text, code, and similar). They have versions, suggestions, and per-user bookmarks. Open, edit, quote, and regenerate follow chat write.
- Files are uploads for chats, projects, and the library. They attach as sources with `@` or `+`.
- Published files from a computer (sandbox or operator) attach to the reply and become durable.

### Chat sandbox

- Every chat, in every workspace, whatever the licenses, has No operator: a small free computer for Run and Build.
- The sandbox has no identity, memory, triggers, mentions, or license.
- Files snapshot when idle and restore on the next turn. Processes do not survive. An oversized snapshot is discarded (“files not kept”).
- Egress is limited to package registries. There are no secrets, repositories, or setup script.
- The sandbox is bounded by size, idle time, and concurrent sandboxes per workspace.

### Operators

- An operator is a licensed workspace teammate: persistent computer, identity, memory, primary agent, and triggers. Operators are never publishable and are never listed on the marketplace.
- Environment includes plan, repositories (HTTPS), setup script, egress allowlist, secrets (write-only; a git token becomes the git credential), and a persistent volume.
- Identity is a principal, granted on chats and projects like a person (read or write only).
- Memory is operator-wide notes any agent working there should know. It crosses chats and is visible when written. Admins edit or clear it. Agents stay stateless. Project files remain project knowledge.
- The primary agent is the agent instance the operator uses when it acts itself.
- Triggers are mention (always), schedule, webhook (signed; the secret is not in the URL), and events (release cut, asset published, install, member joined). Each trigger names a chat.
- Automatic replies (`auto`, default `mentions`) fire on human Message posts when the operator is granted write and was not mentioned, with cooldown and hourly cap. A workspace may turn automatic replies off.
- When a person selects the operator in the composer, the brain is the agent they picked, the place is that operator’s computer (this chat’s session), the actor is the person (their grants and OAuth identities), memory is the operator’s, the reply is the assistant, and tokens follow the person’s funding chain.
- When a person mentions the operator or a trigger fires, the brain is the operator’s primary agent, the place is the same computer, the actor is the operator (its grants, secrets, and static credentials), memory is the operator’s, the reply is the operator as a participant, and tokens follow the operator’s seat, then workspace pay-as-you-go under its budget.
- An unlicensed operator (never subscribed, canceled, unpaid) can be configured but not selected, mentioned, or triggered. Its volume is kept a short time, then removed.
- Runs in different chats of one operator may run in parallel up to the plan. Extra work queues.

### Marketplace

- The marketplace is the public registry of listed released assets (agents, skills, applications, workflows, reports). Nothing is listed automatically. Distribution is Settings → Marketplace on the asset.
- Browse is Featured, All, Agents, Applications, Skills, Workflows, and Reports, with search, creator, sort (recent, installs, rating), and tags.
- Featured is a platform highlight on a listing or a curated home section. It is set by platform operators, not by the publisher.
- A listing page shows media, Add or Save, README and LICENSE of the latest release, About (installs, publisher, rating, requires, tags, repository when public, resource links), and Report abuse.
- Add (agents, applications, workflows, reports) opens the instance dialog. Save to workspace is for skills.
- Trust is verified or community. Verified publishers skip the community safety gate.
- Community connections and community skills with scripts need a manager confirmation. Community deployments are not gated that way (the installer supplies targets and credentials) but show the fields they will ask.
- Ratings are 1–5, only if one of the person’s workspaces installed or saved the listing.
- An instance page shows a newer release and Rebind. Rebind needs the release to still be distributed.
- Platform operators set trust, featured, and unlisted. Unlisted listings disappear from search and Add; existing instances keep working with a warning.
- Listings are free to distribute and free to add.
- Entry points are `/marketplace` and public workspace or asset pages. Both open the same create dialog.
- Private assets need a paid SaaS tier to list. Switching a listed asset to private without that tier is refused. Public assets may list on any tier.
- Agent and skill listings show Requires (applications, including those inherited from pinned skills).

### Public API and integrations

- A public API prompts agents directly, without the web product.
- Integrations with Slack and mail are handled by applications installed from the marketplace, using the same install, credential, and approval rules as other applications.

### Models

- The workspace model registry is what runs: catalog models the workspace enabled, plus custom models (slug, name, provider alias). Slug is the wire id. A custom slug may not shadow a catalog id.
- Providers are Anthropic, OpenAI, Google, xAI, Mistral, Azure, Bedrock, and Ollama.
- `default` resolves to the workspace default, else the platform default. `auto` prefers the platform auto model when entitled, else the cheapest enabled low-tier catalog model.
- Run options live on the agent instance or turn: effort, reasoning, service tier, context window. Changing model resets unsupported options.
- BYOK is the workspace’s provider secret or a custom model. Token usage is recorded and billed at $0. Search is never covered by BYOK.
- Provider secrets are write-only; reads show only that a secret exists. A disabled provider keeps its key while runs use platform credentials.
- Settings are `/settings/models` (personal) and workspace Settings → Workspace → Models (manager+): catalog toggles, custom CRUD, per-provider enable and secret.
- The assistant in a chat uses the instance model unless the turn overrides it.
- Custom models are never billed at list price (BYOK). They still need a runnable configuration at run time, not at create.

### Navigation

- The header has Search, Issues (open assigned count), Notifications (unread count), New chat, workspace switcher, and user menu.
- The left product sheet has Marketplace plus the context destinations.
- Workspace tabs are Overview, Assets, Instances, Stars (personal accounts), Teams, People, and Settings (manager+). Enterprises add Managed. Counts hide at zero.
- The context sidebar has New chat, Feed, Projects, Library (Chats / Documents / Files), Actions, Dashboards, chat history, then the workspace block.
- Asset page tabs are Content, Releases, Instances (where the kind runs), and Settings. Skills have no Instances tab.
- Settings groups, hidden when empty, are General, Access, Workspace, Billing, Enterprise, and Developer.
- Create routes include `/new/organization` in addition to the asset create routes.
- Public routes are `/marketplace/**`, public `/w/<alias>` reads, share links, and `/search`.

### Search

- Search is GitHub-like over names and descriptions.
- Qualifiers are `type:agent|skill|application|workflow|report|operator|chat|document|file|project|member|action|dashboard`, `owner:<alias>`, `is:public|private|mine|shared`, `in:name|description`, `label:<name>`, and `project:<name>`.
- Quick results appear in the header. `/search?q=` has per-type tabs. Public scope works signed-out.

### Feed, notifications, and issues

- The feed has a new-chat composer on top, then the workspace’s activity grouped by day and live. Overview shows a compact Activity. Member detail can filter by actor. Retention is 180 days.
- Activities include asset updates (grouped per asset, person, and day), release cut, listed, install, instance created, operator run, action run, chat created or shared, channel post, document created, member joined, and sponsor received.
- Stars, team or permission edits, invitations, and computer lifecycle are not activities.
- Unreadable subjects are dropped for outsiders and masked for members (“a private chat”).
- Notifications are Inbox, Saved, and Done, with filters for Mentioned, Participating, Assigned, and workspaces. Bulk mark read, done, or save.
- Notification kinds are mention, operator reply, grant, release, billing, sponsor, invitation, issue, and system.
- An issue is a decision the product needs from a person: approval, connection identity, uncovered run, or system. It stays open until resolved or dismissed.
- Issue lists are Assigned to me, Created by me, Mentioning me, and Recently updated. Creating an issue also notifies assignees.
- The issue row links to the run, connection, or billing page where it is resolved.

### Billing and licenses

- Four independent licenses: SaaS plan, AI plan (seats), Pool plan, and Operator plan. A free SaaS workspace on BYOK can still buy a pool or an operator.
- A usage line has an actor (who spent it: the person, or the operator on operator or action runs), a usage owner (the workspace), and a billing account (who pays: the workspace’s payer, or the member’s personal account when the personal plan pays).
- A seat is an AI allowance in dollars, held by one member or one operator. Seats are not pooled.
- Funds are a dollar balance on the billing account, fed by sponsorships, applied to any invoice before the card. They never expire, are never refunded, and cannot be earmarked.
- Any account may sponsor an unmanaged organization, one-off or monthly, optionally anonymous in the product. Sponsors show on the organization overview unless anonymous. Managed organizations cannot be sponsored.
- Coverage is which source will pay the next run for the current person or operator. It is shown in the workspace switcher. The member toggles “Use my plan” themselves.
- Who pays never changes what may run. The workspace registry and providers apply either way.
- A run with no covering source does not start. Exhausted mid-run stops the run. The next turn resolves again.
- The person sees why a run does not start: no seat, seat exhausted, no budget, budget reached, cap reached, funds exhausted, or personal plan off, exhausted, or managed.
- An enterprise-managed user without a SaaS seat cannot run.
- A composer turn in an operator is still the sender’s turn. Mentions, triggers, and actions follow the operator.
- Web search resolves the same funding chain per call. A refusal is a tool error; the run continues without search.
- Titles, labels, and “should this operator reply?” are platform-absorbed at $0.

### SaaS plans

- SaaS gates product capabilities and member seats.
- Designed user plans are Free at $0 and Pro at $4 / month.
- Designed organization plans are Community at $0 and Team at $4 / user / month.
- Designed enterprise plans are Cloud at $21 / user / month and On-prem at a custom price.
- Tier-gated capabilities include listing a private asset, seat counts, and a dedicated tenant (enterprise).
- Trials are 14 days on Team. SaaS may be annual.

### AI plans

- An AI plan’s monthly dollar allowance equals the price. List price is used inside the allowance, with no markup.
- Designed AI tiers are Free at $0 with $1 / month plus unlimited BYOK at $0 (user accounts only); Pro at $20; Premium at $60; and Ultra at $200.
- Pro, Premium, and Ultra include SaaS Pro (user) or Team (org).
- Seats are assigned to a principal: a member or an operator. An operator seat is not a SaaS member seat and does not grant the included SaaS tier.
- Enterprise AI seats are additive to the SaaS seat. Organizations have no free $1. Unused monthly allowance does not roll over. Annual AI purchases prepay twelve months.
- Pay-as-you-go (no seat, or beyond it) is list price plus plan markup (default +20%), on the invoice, only if the actor’s budget on the workspace allows it, the billing account’s monthly cap allows it, and, without a card, available funds cover it.
- Members without a budget row get the organization default (designed $0). Operators without a row get $0. The owner-set monthly cap defaults to none.
- For a member of an organization, payment order is their org seat, then org pay-as-you-go (budget, cap, funds), then their personal plan if they left “Use my plan” on and are not enterprise-managed.
- For an operator of an organization, payment order is its seat, then workspace pay-as-you-go under its budget. Never a member seat or personal plan.
- For an operator of a personal workspace, payment order is its seat, then the owner’s seat and the owner’s pay-as-you-go when “use owner plan” is on (default). A budget then caps everything it spends on the owner.
- For a user in their personal workspace, payment order is their seat or $1 free, then their pay-as-you-go under their cap.
- BYOK is first for every actor at $0.

### Pool plans

- A pool is where deployments run. Shared by default. A workspace may buy a dedicated pool.
- Dedicated capacity is billed hourly. Shared pools exist without a purchase.

### Operator plans

- One subscription per operator. Operator hours are part of the operator license, not AI pay-as-you-go, and budgets do not apply. The chat sandbox is free and not a plan.
- Designed Standard is 1 vCPU / 2 GB / 10 GB, on demand, $0.05 / running hour, 2 concurrent chats, 30 min run length.
- Designed Performance is 2 vCPU / 4 GB / 20 GB, on demand, $0.10 / running hour, 4 concurrent chats, 30 min run length.
- Designed Always-on is 2 vCPU / 4 GB / 20 GB, always on, $60 / month, 4 concurrent chats, 2 h run length.
- On-demand idle timeout is 15 minutes. A 14-day trial applies to the first Standard of an account.

### Billing UI

- Workspace billing (manager+) shows overview, plans, seats, budgets, default member budget, funds, sponsors, infrastructure, usage (by actor, owner, payer, model, kind, source, day), and invoices. The owner also has checkout, portal, and cap.
- The personal mirror shows overview, plans, cap, the person’s seat and their operators’ seats and budgets, checkout, portal, usage they paid (including other workspaces), and invoices. It has no funds, sponsorships, or default budget.
- Checkout kinds are SaaS, AI seats, sponsorship, pool, and operator (target = that operator). The customer portal is for cards and invoices.
- Refunds and disputes mark the mirrored invoice and notify. They do not automatically change seats.

### Enterprise

- An enterprise manages organizations and users under one enterprise.
- A tenant is a dedicated explorer: the product UI and conversation data on infrastructure the enterprise registers. The enterprise owner registers a host. Members of managed accounts are served there.
- Tenant hosting is Cloud (the vendor runs the tenant) or on-prem (the customer runs it). Same product, same registration. Health is shown on Enterprise settings.
- SAML is available for enterprise sign-in.
- Enterprise AI seats are additive.

### Security, compliance, and trust

- Workspaces are isolated. Conversation data of a tenant stays with that tenant.
- Secrets are write-only, masked on read, and never stored on an asset draft or release. Deployment and connection credentials live on the instance.
- Outbound calls to customer-supplied hosts refuse private and link-local targets on hosted infrastructure.
- Community marketplace installs that can run scripts or open a remote connection ask a manager.
- Approvals apply to mutating tools in Run. Issues collect decisions.
- Organizations and enterprises have an append-only audit log at Settings → Access → Audit, with CSV export and 1-year retention. The feed shows activities; the audit log is the compliance record.
- Export lets the person or the workspace owner download a zip of account data, asset archives, usage, invoices, and conversation data, never secrets. The link lives 7 days.
- Deletion is scheduled by the owner (recent sign-in, 14-day grace, cancel by signing in). After grace: credentials revoked, subscriptions cancelled, assets and operators removed, personal fields scrubbed. Messages in shared chats remain as “Deleted user”.
- Mail supports unsubscribe and bounce suppression.
- A status page covers the product. An in-app banner appears during an incident.
- Support is community on free, priority on Team, and enterprise support on Enterprise.

## Sources

- https://agentskills.io
