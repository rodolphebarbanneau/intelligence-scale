---
name: Sierra
slug: sierra
url: https://sierra.ai/
docs: https://docs.sierra.ai/
kind: product
reviewed: 2026-09-28
---

# Sierra

## Product

Sierra is Sierra Technologies, Inc.'s platform for building and running customer-facing AI agents. The company names the runtime Agent OS. Teams use it to put one agent on voice, chat, email, SMS, messaging, and ChatGPT, and to connect that agent to knowledge, systems of record, and contact-center handoff. The product is the chassis a company adopts. Sierra also routes work across a constellation of frontier, open-weight, and proprietary models; those models are not a separate product in this dossier.

There is no public documentation site. `https://docs.sierra.ai/` exists and asks for a username and password. This dossier uses official marketing product pages, the Trust Center entry point, legal pages, and official blog posts for facts those product pages do not state.

Sierra is sold as an enterprise platform, not a self-serve consumer app. The public site describes a partnership with a forward-deployed agent development team, outcome-based pricing, and a Sign in entry in the main navigation. There is no public price list or self-serve plan grid. The vendor names two build paths on the same platform: Agent Studio (no code) and Agent SDK (code), plus Ghostwriter, an agent that builds and updates other agents from prompts and uploaded source material. Insights, Explorer, simulations, monitors, and experiments sit on top of either build path.

The official Product navigation lists Product overview, Ghostwriter, Agent Studio, Horizon, Context Engine, Insights, Explorer, Channels, and Trust and reliability. Dedicated pages also exist for Agent SDK, Voice, Live Assist, and Meet your agent. Horizon is the long-running outbound and inbound orchestration surface. Context Engine is the memory, signals, and personalization layer. Live Assist is the same agent used to draft and act for human care representatives. The vendor does not publish a separate sibling product that needs its own spec in this repo.

Sierra Technologies, Inc. was co-founded by Bret Taylor and Clay Bavor. The About page lists offices in New York, Atlanta, London, Singapore, Tokyo, Paris, Madrid, Toronto, and San Francisco (https://sierra.ai/about). The public privacy policy at https://sierra.ai/privacy-policy covers the website and Sierra-operated demo or recruiting agents. Customer Data processed through a customer's deployment is governed by that customer's contracts and data-processing agreement, not by the website privacy policy. The product site states that customer data is never used to train models and is never shared with other customers.

The Product overview states that 40% of the Fortune 50 partner with Sierra, that an expert agent development team has supported hundreds of deployments, and that agents can go live in weeks. Industry pages exist for financial services, healthcare, telecommunications, media, travel and hospitality, retail and consumer goods, and technology. Those pages are vertical marketing, not separate products.

## Features

### Product overview

Primary source: https://sierra.ai/product

- Create one agent and deploy it across voice, chat, email, and WhatsApp in 59 languages, available 24/7/365.
- Agents use natural language to understand context, sense frustration, and respond while staying on brand.
- Connect the agent to systems of record such as order management and CRM so it can complete tasks end to end, including processing an insurance claim, returning an order, or originating a mortgage.
- The site states that 40% of the Fortune 50 partner with Sierra.
- The product is positioned for financial services, telecom, tech, healthcare, travel, and retail.
- Built-in testing, automated monitoring, and proactive insights are part of the platform.
- Sierra staffs an expert agent development team and describes hundreds of deployments.
- Pricing on this page is outcome-based: pay when the software achieves specific, valuable outcomes.
- Related product cards describe Ghostwriter (prompt workflows, integrations, guardrails, tone, and style) and Explorer (natural-language questions answered from analytics and sample conversations).

### Ghostwriter

Primary source: https://sierra.ai/product/ghostwriter

- Ghostwriter is named the agent-building agent. Teams describe how the agent should behave; Ghostwriter builds or modifies it.
- Prompts can update workflows, systems integrations, guardrails, tone, and style.
- Teams can upload SOPs, raw transcripts, or audio interviews of subject matter experts to create customer journeys from scratch. The homepage also lists whiteboard photos and audio recordings, and building from a goal stated in plain English. Source: https://sierra.ai/
- Ghostwriter shows what it built before anything goes live so a person can review, approve, and ship.
- Ghostwriter runs tests on every build or update before the change reaches the reviewer.
- It identifies and tests edge cases beyond the obvious scenarios.
- When a simulation fails, Ghostwriter diagnoses the issue and implements the fix.
- Teams can feed golden recordings or transcripts from support associates; Ghostwriter uses them to improve the agent.
- Explorer recommendations can be implemented automatically through Ghostwriter.
- Every filed issue has a Fix with Ghostwriter control.
- The homepage describes Ghostwriter output as a multilingual, multichannel agent with built-in guardrails, and Optimize as automated updates from flagged issues and proactive insights with visibility so a person can review, validate, and ship. Source: https://sierra.ai/
- Journeys, actions, policies, and personas created with Ghostwriter are visible and editable in Agent Studio. Source: https://sierra.ai/blog/your-agent-laid-bare-and-why-it-matters
- Ghostwriter can turn conversation patterns into experiment hypotheses and ship those hypotheses as experiments in Agent Studio. Source: https://sierra.ai/blog/let-your-customers-shape-your-agents

### Agent Studio

Primary source: https://sierra.ai/product/agent-studio

- Agent Studio is the no-code surface for building and managing agents.
- Journeys are composable building blocks for step-by-step workflows. Teams can write them from scratch or generate them with AI from existing operating procedures.
- Tools and dynamic data keep responses current from external systems and knowledge sources.
- Agent Traces show every decision, tool call, and response in real time while a journey is being built.
- Knowledge management lets teams view, manage, and edit Help Center content, FAQs, and policies that ground the agent.
- Sierra identifies common themes missing from the knowledge base.
- Expert Answers drafts knowledge articles from how care representatives resolve edge cases.
- The site states 40+ pre-built integrations for third-party knowledge bases, systems of record, and contact centers.
- Custom integrations use Sierra's integration framework and are configurable in Agent Studio.
- Agent actions use those integrations inside journeys, including taking action for a customer and routing a conversation to the care team with context.
- Simulations run AI-powered evaluations of conversations against defined outcomes.
- Regression testing builds a suite to catch regressions before a new agent version is released.
- Voice Sims test transcription, background noise, and speaker variation before go-live.
- Branding covers agent name, voice, welcome message, logo, and colors.
- Dynamic updates can change the agent in real time for promotions, service updates, or other current information.
- Multimodality lets teams upload images and videos for product display and troubleshooting.
- Agent Studio 2.0 uses the same building blocks as the Agent SDK in a no-code interface. Source: https://sierra.ai/blog/agent-studio-2-0
- Workspaces are private editing spaces. Journeys, configuration, and simulations are versioned. Updates combine into numbered snapshots that move from QA to staging to production, with history and rollback. Source: https://sierra.ai/blog/agent-studio-2-0
- The Integration Library lets a team pick an integration, add credentials and endpoints, and publish tools into Agent Studio and the Agent SDK. Custom integrations can still be written in the Agent SDK. Source: https://sierra.ai/blog/agent-studio-2-0
- Teams can create custom monitors in Agent Studio with a natural-language interface. Source: https://sierra.ai/blog/agent-monitoring
- Experiments in Agent Studio is the surface for running, reviewing, and shipping A/B tests. Source: https://sierra.ai/blog/let-your-customers-shape-your-agents
- Roles and permissions, separate environments, and versioned releases control who can change an agent and when a change goes live. Source: https://sierra.ai/blog/your-agent-laid-bare-and-why-it-matters
- Agent logic (journeys, policies, prompts, and other instructions) can be exported in a structured format. The agent also lives in a Git repository the customer can access. Source: https://sierra.ai/blog/your-agent-laid-bare-and-why-it-matters

### Agent SDK

Primary source: https://sierra.ai/product/agent-sdk

- Agent SDK is the code path for building agents. The page calls Agent OS the platform that hosts those tools.
- Developers set goals and guardrails so the agent follows policy and brand tone.
- Composable skills such as triage, respond, and confirm are mixed into workflows.
- Tuning sets how flexible or deterministic each workflow is.
- One build deploys across chat, phone, email, SMS, and messaging.
- Simulations cover a range of scenarios and check for regressions.
- Debugging inspects API calls and logic traces.
- A knowledge engine takes proprietary FAQs, policies, and documentation.
- The agent can take action in connected systems, with examples that include updating a subscription or submitting a warranty.
- Contact-center handoff routes a conversation to a person and generates a summary.
- Developers work in their existing programming environment and software development lifecycle.
- The page states that building on Sierra includes documentation, interactive training, and support from Sierra's team. That documentation is the gated host at `https://docs.sierra.ai/`.
- Customer data is never used to train models. Source: https://sierra.ai/product/agent-sdk
- The official blog states that the Agent SDK includes version control, release gating, continuous integration, delivery and deployment, and audit. Source: https://sierra.ai/blog/serving-customer-experience-and-engineering-teams-all-from-one-platform
- Agent SDK capabilities for Voice Personas include adjusting pacing, responding to interruptions, and switching voices or languages mid-conversation. Source: https://sierra.ai/blog/introducing-voice-personas
- A company can mix Agent SDK and Agent Studio on one Agent OS deployment. The blog example is a warranty-claim journey in code and a returns journey in Agent Studio. Source: https://sierra.ai/blog/serving-customer-experience-and-engineering-teams-all-from-one-platform

### Horizon

Primary source: https://sierra.ai/product/horizon

- Horizon stays with a job across days or months and acts on signals to decide what happens next.
- Signals trigger proactive engagement from customer behavior, conversations, or milestones.
- Playbooks take an outcome such as a mortgage, a claim, or a renewal and plan the work over weeks or months.
- Built-in suppression skips customers who are already in progress, opted out, or no longer relevant.
- The same agent and context follow a customer across channels for outbound and inbound contact.
- Engagements are two-way conversations, not one-way broadcasts.
- Consent and opt-out are enforced per customer and per channel on every touch.
- Customer context uses full history to decide the next step in a long-running journey.
- Persistent memory recalls what matters to each customer across touchpoints.
- Next-best-action decisioning updates personalized decisions as new signals arrive.
- Messaging can be fully autonomous by default, with exact wording where required.
- Goals and guardrails define what the agent may do alone and where human sign-off is required.
- Auditing and analysis show what triggered an engagement, what the agent decided, and why anyone was suppressed.
- The page walkthrough shows Horizon calling patients and payers, using a scheduling API, sending provider messages, and confirming appointments by phone and SMS after EHR signals such as an open referral or a prior-authorization change.

### Context Engine

Primary source: https://sierra.ai/product/context-engine

- Context Engine is the memory, signals, and personalization layer. Horizon's page names it as the context engine used with long-horizon planning. Source: https://sierra.ai/product/horizon
- Continuity ties interactions to one person so a conversation can resume across channels.
- The memory layer is permissioned, retained on the customer's terms, and exportable to a warehouse or other external system.
- Integrations with systems of record supply customer history such as purchases and account information.
- First- and third-party signals include behavior, transactions, and account changes.
- Continuous reasoning keeps working between conversations as new information arrives.
- Contextual relevance weighs each signal against full customer context before acting.
- Next best action uses AI and custom strategies instead of static rules.
- Guardrails set non-negotiables such as protecting NPS or margins while the agent pursues an outcome.
- The page describes learning from every interaction so later decisions use that history.
- A November 2025 announcement names Agent Data Platform (ADP) as Agent OS's memory and intelligence layer: it unifies unstructured conversation data with structured CRM, billing, and transaction data, can deploy via a Headless API, and takes a customer-defined strategy of audience, outcomes, inventory, and triggers. Source: https://sierra.ai/blog/agent-data-platform

### Channels

Primary source: https://sierra.ai/product/channels

- Voice covers inbound and outbound calls. The same page introduces Voice Personas for how the agent sounds and speaks, using a constellation of models tuned across 60+ locales.
- Messaging covers website chat, mobile app, WhatsApp, Apple Business Chat, and SMS, including outbound personalized messages and multimodal images and videos.
- Email agents respond to customer mail using CRM data and real-time account context, and the page describes branded replies at chat speed.
- Live Assist is listed as a channel surface that drafts ready-to-send replies, exposes the same tools to care representatives, and feeds assisted conversations back into the system.
- ChatGPT publishing uses one Sierra agent for first-party channels and a ChatGPT app. Teams choose which journeys, data, and capabilities each channel sees.
- ChatGPT apps can use universal web attachments such as maps, fillable forms, and charts.
- Publish to ChatGPT is one click or via CI/CD. Sierra agents are described as natively compatible with ChatGPT Apps via Model Context Protocol (MCP).
- The homepage also lists SMS, WhatsApp, email, voice, and ChatGPT as a single-agent channel set. Source: https://sierra.ai/
- Meet your agent repeats phone (including replacing IVR), chat, SMS, messaging, and email, and states that a conversation does not reset if the customer steps away. Source: https://sierra.ai/product/meet-your-agent
- Agents can connect through MCP, REST, GraphQL, or custom integrations, call tools in the customer's stack, and expose Sierra capabilities to other agents through APIs. Source: https://sierra.ai/blog/your-agent-laid-bare-and-why-it-matters

### Voice

Primary source: https://sierra.ai/product/voice

- Voice handles inbound and outbound calls with low-latency turn-taking, interruptions, background noise, accents, and real-time sentiment used to adapt tone and pace.
- The agent can replace IVR menus, use memory for personalization, and escalate to a care representative with full context and history.
- This page states support in over 55 languages with mid-conversation language switching.
- Build, test, deploy, and optimize on voice uses Ghostwriter, voice simulations, all-channel deploy, and AI-driven insights.
- Each turn is routed to a selected model for language and tone.
- Voice payments collect card and ACH payments on the same call with no IVR handoff.
- Card details are collected via DTMF through Level 1 PCI-compliant infrastructure and routed to the customer's payment processor.
- Voice payments use a standard integration to an existing payment processor.
- Voice Personas combine voice, personality, and language-aware behavior. One agent can use different personas for different brands, markets, and experiences. Source: https://sierra.ai/blog/introducing-voice-personas
- Voices are sealed in production so the tested voice is the production voice. Personas can be run through simulations and A/B tests. The announcement states Voice Personas are available on Sierra. Source: https://sierra.ai/blog/introducing-voice-personas

### Live Assist

Primary source: https://sierra.ai/product/live-assist

- Live Assist gives care associates the same agent used for automated conversations.
- Real-time guidance walks a representative through next steps in chat or on calls and updates customer context as the work proceeds.
- Auto-drafted responses produce on-brand replies or call scripts grounded in knowledge and systems.
- One-click actions start workflows from the conversation without switching tabs.
- The page describes using that guidance to move CSAT, average handle time, and first-contact resolution.
- Voice and digital conversations share the same knowledge, SOPs, and brand voice.
- Assisted conversations generate insight that is used to improve the agent.
- Autonomous and assisted experiences run from the same Sierra platform without a second agent build.

### Explorer

Primary source: https://sierra.ai/product/explorer

- Explorer is named the agent-optimizing agent. It runs continuously in the background.
- It delivers a weekly briefing on trends, emerging issues, and recommendations.
- It surfaces patterns a team may not have queried.
- Analyses can be shared, and a query can be branched without changing the original.
- Teams ask natural-language questions; Explorer answers across customer conversations.
- Each answer includes a summary, categorized themes with data, and links to the underlying conversations.
- Follow-ups can narrow to journeys, channels, or time windows.
- Recommendations can be sent to Ghostwriter in one click for automatic implementation.
- Teams can compare agent performance before and after those automated changes.
- The Product overview card describes Explorer as answering questions with analytics and sample conversations and producing actionable recommendations. Source: https://sierra.ai/product

### Insights

Primary source: https://sierra.ai/product/insights

- Reporting includes custom reports and metrics such as CSAT and case resolution.
- Clicking a data point on a report opens Explorer on that trend.
- Automated tagging categorizes conversations.
- Experimentation includes value discovery on potential cancellations, conversation-design variants such as hand-off rules or determinism, and decisioning that uses agent memory and customer profile.
- Observability monitoring reviews conversations that need attention and alerts on them.
- Auditing shows the reasoning for an action or answer, including knowledge sources and systems accessed.
- Alerting covers abuse attempts and performance drops and can integrate with existing tools.
- Out-of-the-box experiments measure outcomes such as resolution rate and churn reduction. The dashboard shows statistical significance, when an effect emerged, and stability over time. Traffic can ramp from a slice to 100% when a variant is promoted. Source: https://sierra.ai/blog/let-your-customers-shape-your-agents
- Monitors are an always-on evaluation layer that uses an LLM-as-judge on every conversation. Sierra ships monitors for looping, increasing frustration, and false transfers. Each flag includes the monitor's rationale. Source: https://sierra.ai/blog/agent-monitoring
- Pulse proactively surfaces issues and opportunities. Agent data can be sent through OpenTelemetry, Amazon EventBridge, Google Cloud Pub/Sub, or Sierra's export API. Conversation logs and performance data can be exported to a warehouse, BI tools, or reporting systems. Source: https://sierra.ai/blog/your-agent-laid-bare-and-why-it-matters

### Trust and reliability

Primary source: https://sierra.ai/product/trust-and-reliability

- System-of-record access is described as deterministic and controlled to follow the customer's policies and security procedures.
- The page lists SOC 2, HIPAA, GDPR, PCI, FedRAMP High, CCPA, CSA STAR, ISO 27001, and ISO 42001.
- Supervisor models wrap LLMs to reduce hallucinations, enforce security, and prevent abuse.
- Customer data is used only as the customer instructs and is never shared with other customers.
- PII shared with the agent is automatically encrypted and masked.
- Built-in filters and monitors block topics and keywords the customer marks off-limits.
- Payment card data flows through dedicated PCI-certified infrastructure and does not touch Sierra's core platform, LLMs, or persistent storage.
- Sierra states PCI DSS Level 1 Service Provider certification.
- The page states that businesses complete thousands of card and ACH transactions daily across voice and chat.
- A constellation of frontier, open-weight, and proprietary models is used for decisions, understanding, and responses. Sierra switches providers to maintain continuity if one provider is down.
- The Sierra Trust Center at `https://trust.sierra.ai/` is where customers review controls and request security documentation. Source: https://trust.sierra.ai/
- An official announcement states ISO 27001 and ISO 42001 certification by an accredited body, including encryption, access control, model evaluation, AI impact assessment, and traceable agent decisions. For sensitive actions such as system access or record updates, Sierra supports absolute determinism. Supervisory agents watch for topic drift and inconsistent logic. Customers control where data lives, how it is used, and when it is deleted. Source: https://sierra.ai/blog/sierra-is-now-iso-42001-and-iso-27001-certified
- An official announcement states AIUC-1 certification after an AIUC technical test of chat and voice agents and a Schellman review of controls. Testing recurs at least quarterly, with a full audit every year. Supervisors can correct, block, or escalate live responses. Deterministic guards cover authentication and access requirements. The same post states SOC 2 Type II attestation alongside ISO 27001 and ISO 42001. Source: https://sierra.ai/uk/blog/sierra-achieves-aiuc-1-certification

### Outcome-based pricing

Primary source: https://sierra.ai/product

- The Product overview defines outcome-based pricing as paying only when the software achieves specific, valuable outcomes.
- The official pricing post ties charges to impacts such as a resolved support conversation, a saved cancellation, an upsell, or a cross-sell. If the conversation is unresolved, in most cases there is no charge. Escalated cases are also, in most cases, not charged. Source: https://sierra.ai/blog/outcome-based-pricing-for-ai-agents
- Outcome criteria are agreed up front. Straightforward answers and longer L2-style work can be priced as different outcomes. Source: https://sierra.ai/blog/outcome-based-pricing-for-ai-agents
- When outcome-based pricing is a poor fit, Sierra describes a blended model. Routing or greeter interactions may use consumption-based pricing by conversation count. The post states Sierra does not use seat-based pricing. Source: https://sierra.ai/blog/outcome-based-pricing-for-ai-agents
- The same post says Sierra continues directed optimizations after launch because payment is tied to completed outcomes. Source: https://sierra.ai/blog/outcome-based-pricing-for-ai-agents
- A forward-deployed agent development team can embed with engineering, customer experience, or operations. Source: https://sierra.ai/blog/serving-customer-experience-and-engineering-teams-all-from-one-platform

## Sources

- https://docs.sierra.ai/
- https://sierra.ai/product
- https://sierra.ai/product/ghostwriter
- https://sierra.ai/product/agent-studio
- https://sierra.ai/product/agent-sdk
- https://sierra.ai/product/horizon
- https://sierra.ai/product/context-engine
- https://sierra.ai/product/channels
- https://sierra.ai/product/voice
- https://sierra.ai/product/live-assist
- https://sierra.ai/product/meet-your-agent
- https://sierra.ai/product/explorer
- https://sierra.ai/product/insights
- https://sierra.ai/product/trust-and-reliability
- https://trust.sierra.ai/
- https://sierra.ai/about
- https://sierra.ai/privacy-policy
- https://sierra.ai/
- https://sierra.ai/blog/your-agent-laid-bare-and-why-it-matters
- https://sierra.ai/blog/agent-studio-2-0
- https://sierra.ai/blog/agent-monitoring
- https://sierra.ai/blog/let-your-customers-shape-your-agents
- https://sierra.ai/blog/serving-customer-experience-and-engineering-teams-all-from-one-platform
- https://sierra.ai/blog/introducing-voice-personas
- https://sierra.ai/blog/agent-data-platform
- https://sierra.ai/blog/sierra-is-now-iso-42001-and-iso-27001-certified
- https://sierra.ai/uk/blog/sierra-achieves-aiuc-1-certification
- https://sierra.ai/blog/outcome-based-pricing-for-ai-agents
