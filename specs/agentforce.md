---
name: Agentforce
slug: agentforce
url: https://www.salesforce.com/agentforce/
docs: https://help.salesforce.com/s/articleView?id=ai.copilot_overview.htm
kind: product
reviewed: 2026-09-28
---

# Agentforce

## Product

Agentforce is Salesforce’s agent platform on the Salesforce Platform. An organization builds agents that hold natural-language conversations, choose a job (a subagent), run actions, and return a response. The Atlas reasoning engine orchestrates that path. Agents run in Lightning Experience in Enterprise, Performance, Unlimited, and Developer Editions. Required add-on licenses vary by agent type. Many types also need Foundations or Agentforce 1 Editions.

Some agent types assist a Salesforce user in the flow of work. Others act on behalf of a user or customer inside the use cases and guardrails an admin sets. Agents respect standard Salesforce access controls: licenses, permissions, field-level security, and sharing. They use the Einstein Trust Layer for grounding, prompt defense, toxicity detection, and audit logging. The product is the Agentforce chassis in a customer org. Salesforce-managed and partner large language models (Anthropic, Google, OpenAI, and optional BYOLLM or LLM Open Connector models) power reasoning.

A builder turns on Einstein generative AI and Agentforce in Setup, opens the Agentforce Studio app, and creates an agent from a template or from scratch. Configuration happens in Agentforce Builder with Agent Script: subagents, actions, variables, filters, data libraries, and connections. The builder tests in Agentforce Builder and Agentforce Testing Center, adds channel connections, then activates the agent. Employees reach some agents in the Agentforce panel in Lightning Experience, the Salesforce mobile app, or Slack. Customers reach Service agents on enhanced messaging, Service Email, and voice. Developers call agents through the Agent API, Agentforce DX, Testing API, and invocable actions from Flow or Apex.

Salesforce also ships Einstein Bots, a separate scripted chatbot product. Prompt Builder, Agentforce Grid, and Einstein Data Prism sit in the same Help tree. None of those products have sibling specs in this repo.

Agentforce (Default) stopped receiving new features on 17 June 2025 and is not available in new Salesforce environments. Salesforce recommends Agentforce Employee Agent. Agent for Setup is retired for new orgs beginning April 2026; Setup with Agentforce replaces it. Beginning in April 2026, Help calls former agent topics subagents.

## Features

### Agents and Atlas reasoning

Primary source: https://help.salesforce.com/s/articleView?id=ai.copilot_overview.htm

- Agents are goal-oriented AI assistants that start and complete a sequence of tasks, hold natural-language conversations, and answer from business data.
- Some types assist and collaborate with a Salesforce user. Other types act on behalf of a user or customer inside admin-specified use cases and guardrails.
- Agents can automate routine tasks such as updating a Salesforce record, answering a question, or drafting an email. During a conversation the agent chooses the actions the task needs and runs them.
- Agents can generate context-aware replies to employee and customer questions. For more complex issues they can escalate the conversation to a live agent.
- Agents can summarize a Salesforce record or page and suggest actions based on the page a user is viewing.
- Agents can draft emails, newsletters, and text messages, and can help users brainstorm and plan.
- Einstein Bots use predefined rules and scripted dialogs. Agents use LLMs, conversation context, subagents, and actions. Channel and UI availability depend on agent type.

Primary source: https://help.salesforce.com/s/articleView?id=ai.copilot_building_blocks.htm

- An agent is a conversational assistant that can identify opportunities for action, anticipate next steps, and start tasks within specified guardrails, with or without a human in the loop.
- An agent is created from scratch or from a template.
- The Atlas reasoning engine is graph-based. It uses Agent Script to separate big-picture workflow from conversational skills and combines LLM reasoning with deterministic, rules-based execution (hybrid reasoning).
- When an agent is triggered or a user sends a request, Atlas routes to a subagent, resolves instructions (including inline actions and conditionals), then reasons with the LLM.
- The reasoning engine calls an LLM at different points in a task. The number and size of calls depend on the task and which subagents and actions run.

Primary source: https://help.salesforce.com/s/articleView?id=ai.agent_builder_reasoning_engine.htm

- A session starts when a user sends a question or request.
- The agent moves to the starting subagent. In Agent Script that subagent uses the `start_agent` prefix. By default this is the Agent Router, which selects a subagent from recent conversation history and the agent’s available subagents.
- The agent then resolves that subagent’s reasoning instructions from top to bottom before any LLM call. A scripted transition can leave the subagent before reasoning starts.
- The prompt sent to the LLM includes agent-level instructions, recent conversation history, resolved subagent reasoning instructions, and the reasoning actions the subagent allows.
- The LLM can run an agent action or utility, ask for more information, ask a clarifying question, or reply from information the agent already has.
- After an action runs, the agent loops: it adds the output to conversation state and decides whether to run another action, ask again, or send a final reply. The loop continues up to seven times.
- Agentforce Service agents run a final response validation: the reply must be grounded, stay in the subagent’s scope and instructions, and exclude hallucinations, unverified information, and prompt-injection risks. A failed draft is regenerated. If validation keeps failing, the agent tells the user it cannot help.
- Agents stream LLM tokens as they arrive. Validation applies to the final reply. If validation fails after streaming has started, the streamed reply is deleted and a new one is generated.

### Agent types

Primary source: https://help.salesforce.com/s/articleView?id=ai.agent_setup_explore_types.htm

- Agentforce Employee Agent assists employees with company knowledge, tasks, and cross-department workflows. It is available in Enterprise, Performance, Unlimited, and Developer Editions with Foundations or Agentforce 1 Editions. It requires Flex Credits. Creating and managing it needs the Manage AI Agents permission.
- Agentforce Lead Nurturing (formerly SDR) engages leads with personalized content, answers common questions, and schedules meetings. It is available in those same editions with Foundations or Agentforce 1 Editions.
- Agentforce Sales Coach gives reps personalized, stage-specific feedback on a sales pitch or role-play session. It is available in those same editions with Foundations or Agentforce 1 Editions.
- Agentforce Service Agent supports customers on common inquiries and escalates complex issues. It is available in those same editions with Foundations or Agentforce 1 Editions. Some standard actions need extra add-on licenses. The Manage Agentforce Service Agents permission set includes Manage AI Agents, which grants org-wide agent management.
- Service Assistant helps service reps with case summaries and step-by-step resolution guidance. It is available in Enterprise, Performance, and Unlimited Editions with Foundations and the Agentforce for Service add-on, or Agentforce 1 Service Edition.
- Setup with Agentforce helps admins with Setup tasks such as managing users, troubleshooting, and customizing the org. Salesforce creates this agent automatically when the feature is enabled. It is not visible or customizable in Agentforce Builder.
- Agentforce (Default) is retired. From 17 June 2025 it does not receive new features and is not available in new Salesforce environments. Salesforce recommends migrating to Agentforce Employee Agent.
- Agent for Setup is retired and cannot be enabled in new orgs beginning April 2026. Salesforce recommends Setup with Agentforce.

### Agentforce Studio and Agentforce Builder

Primary source: https://help.salesforce.com/s/articleView?id=ai.agent_parent_setup.htm

- Agentforce Studio is the home of the new Agentforce Builder and a hub for building, testing, and monitoring agents. In orgs with Agentforce access it appears in the App Launcher by default. Each Studio feature has its own permissions.
- A builder creates an agent for customers or employees, then sets agent-level instructions and system messages (welcome and error messages) that apply in all situations.
- Language and tone settings can be changed to match a company’s brand.
- Agents have draft and committed states and support versioning. In the legacy builder, creating a version copies the agent’s subagents, actions, and other assets; assets are not shared across versions.
- Salesforce recommends the Salesforce Default model option, which lets Salesforce choose the model mix. A builder can instead choose an AWS-hosted or Google Gemini model option.

Primary source: https://help.salesforce.com/s/articleView?id=ai.agent_parent_configure.htm

- Agentforce Builder is where a builder customizes an out-of-the-box agent or creates one, using Agent Script plus subagents, actions, filters, and variables.
- Canvas view summarizes Agent Script into blocks. A builder can expand a block to edit the script, type `/` for common expressions, and type `@` to insert subagents, actions, and variables. Source: https://developer.salesforce.com/docs/ai/agentforce/guide/agent-script.html
- Script view edits Agent Script directly with syntax highlighting, autocompletion, and validation. Source: https://developer.salesforce.com/docs/ai/agentforce/guide/agent-script.html
- A builder can chat with Agentforce to describe desired behavior (for example a shipping rule). Agentforce converts the request into subagents, actions, instructions, and expressions. Source: https://developer.salesforce.com/docs/ai/agentforce/guide/agent-script.html
- Build, Extend, and Troubleshoot Your Agent with AI Assistance is beta. The Agentforce assistant is a built-in coding agent that extends, refines, and troubleshoots agents inside Agentforce Builder at no additional cost.
- A builder can choose an AI model per subagent to balance speed, accuracy, and reasoning depth.
- File upload support lets users share screenshots, receipts, and PDFs. The agent can interpret one file or a group, answer questions from those files, and attach files to a Salesforce record.
- In the legacy builder, filters restrict when a subagent or action is available. For customer-channel agents, Salesforce recommends filters that require authentication before subagents and actions that act for a user.

### Agent Script, subagents, actions, and variables

Primary source: https://developer.salesforce.com/docs/ai/agentforce/guide/agent-script.html

- Agent Script is the language for building agents in Agentforce Builder. It combines natural-language instructions with programmatic expressions for if/else conditions, transitions, variables, subagent selection, and action sequencing (action chaining).
- A builder can mark where the LLM may reason and where the agent must run deterministically.
- Variables store agent state instead of relying only on LLM context memory.
- A transition to another subagent can be deterministic or exposed to the LLM as a tool.
- Developers generate or retrieve a script file with Agentforce DX and edit it in Visual Studio Code. The Agentforce DX VS Code extension supports Agent Script.

Primary source: https://help.salesforce.com/s/articleView?id=ai.copilot_building_blocks.htm

- A subagent is a job the agent can do. It contains actions (tools for that job) and instructions (how the agent decides). Collectively, assigned subagents define what the agent handles.
- Salesforce provides standard subagents for common use cases. A builder can create custom subagents.
- Actions get information or perform tasks in Salesforce. Standard actions cover common Salesforce tasks. Custom actions target a flow, prompt template, or Apex class.
- An action can be run deterministically from script or exposed as a reasoning tool the LLM may choose. Source: https://developer.salesforce.com/docs/ai/agentforce/guide/ascript-ref-actions.html

Primary source: https://help.salesforce.com/s/articleView?id=ai.agent_parent_configure.htm

- Variables store and reuse values for reasoning and interaction. Variable behavior differs between Agentforce Builder and the legacy builder.

### Data, grounding, and Agent Memory

Primary source: https://help.salesforce.com/s/articleView?id=ai.copilot_building_blocks.htm

- Agents are grounded in CRM data on the Salesforce Platform. The org controls which data an agent can access.
- A builder can ground an agent in knowledge articles and fields, uploaded files, or web sources through Agentforce Data Libraries and the Search the Web standard action.
- For unstructured sources, Retrieval Augmented Generation (RAG) is the documented advanced retrieval path.

Primary source: https://developer.salesforce.com/docs/ai/agentforce/guide/adl.html

- Agentforce Data Libraries connect agents to unstructured or semi-structured sources. They turn web content, documents, or large text fields into searchable information.
- The ADL Connect API creates and manages data libraries programmatically.

Primary source: https://help.salesforce.com/s/articleView?id=ai.agent_parent_setup.htm

- Agent Memory remembers details from users’ conversations so the agent can personalize later replies and reduce repeated questions.

Primary source: https://help.salesforce.com/s/articleView?id=ai.agent_parent_deploy.htm

- Agentforce Service agents that answer Service Email ground those replies in Agentforce Data Libraries.

### Language support

Primary source: https://help.salesforce.com/s/articleView?id=ai.agent_language_support.htm

- Language testing for standard actions and retrieval covers Agentforce (Default), Agentforce Employee Agent, and Agentforce Service Agent. Beta languages can retrieve information inconsistently.
- Supported languages include English (en_AU, en_GB, en_US) and a published list of generally available and beta locales (among them French, German, Japanese, Spanish, Portuguese, Chinese, Korean, Arabic (Beta), and others listed on that page).
- Spoken-language support for voice-enabled agents is documented separately and can differ from the text-agent list.
- End User Language comes from the channel: Lightning Experience uses the Salesforce user’s language; Enhanced Chat v1 uses an admin pre-chat field; other channels (for example Lead Nurturing) can set it through the Agent API.
- Agent Default Language is the fallback when no language is detected or the detected language is unsupported. Agent Allowed Languages are secondary languages the agent may switch to.
- Adaptive language mode is beta. In Agentforce Builder the agent can detect each message’s language and reply in that language, including languages outside Allowed Languages. It is not available for voice-enabled agents.
- Only agents created in the new Agentforce Builder support language switching mid-conversation among configured languages. Action outputs stay in the session’s end-user language; the wrapping utterance can switch, so mixed-language replies are possible.
- System messages (welcome, error, and Service escalation) are authored in one language and translated only when End User Language is an allowed secondary language.

### Channels, connections, and escalation

Primary source: https://help.salesforce.com/s/articleView?id=ai.agent_parent_deploy.htm

- A connection carries channel-specific reasoning instructions, adaptive response formats (images, buttons, links, videos), and Omni-Channel flows that route conversations to and from the agent.
- A builder authors an agent once and attaches it to multiple channels through connections. Each template supports a specific set of connections.
- Documented channels include the Agentforce panel in Lightning Experience, the Salesforce mobile app, Slack, messaging platforms, and email. Channel support varies by agent type.
- Employee agents deploy to Lightning Experience and the Salesforce mobile app by activating the agent.
- Employee agents can use a Slack connection so the team works with the agent in Slack.
- Service agents and Employee agents can use messaging channels, including Enhanced Chat and other enhanced messaging channels, with context variables, multiple languages, and progress indicators.
- Service agents can answer customer email. Replies are grounded in Agentforce Data Libraries.
- Messaging and email agents have at least one inbound and one outbound Omni-Channel flow. An inbound flow routes a conversation record to one agent. An outbound flow can route to a service rep, queue, or another agent.
- When a conversation is complex or sensitive, or the user asks for a person, the agent launches the Escalation subagent. On some channels that subagent transfers the conversation and its history through the outbound Omni-Channel flow.
- In the new Agentforce Builder, Agent Script can run the Escalation subagent with the escalate utility.
- Activating an agent that is deployed to one or more channels, including the Agentforce panel, makes it available to users immediately. Deactivating it removes that availability.

Primary source: https://developer.salesforce.com/docs/ai/agentforce/guide/get-started-agents.html

- Enhanced Chat v2 provides JavaScript web APIs for customer-facing Service Cloud chat, including context events.
- The Enhanced In-App Chat SDK embeds messaging in native mobile apps and escalates from an Agentforce agent to a human service rep with conversation context.
- The Agentforce Mobile SDK embeds Agentforce conversations in native iOS and Android apps.

### Agentforce Voice

Primary source: https://help.salesforce.com/s/articleView?id=ai.agentforce_voice.htm

- Agentforce Voice lets Agentforce Service agents speak and understand customer voice conversations. It is available in Lightning Experience in Enterprise, Unlimited, and Developer Editions with Foundations or Agentforce 1 Editions, plus Salesforce Voice add-ons.
- That page states Agentforce Voice is supported only in English.
- Spoken words are transcribed with a speech-to-text model (the page names Deepgram), planned with a Flash Planner that uses an OpenAI GPT model the way Atlas does, then spoken with a text-to-speech model (the page names ElevenLabs).
- Built-in instructions cover spoken delivery (for example pauses in addresses), concise replies, and content-safety guardrails. Those instructions sit in the Flash Planner.
- Deepgram is used with an opt-out so audio is kept only long enough to process the request and is not used to improve the model. ElevenLabs is used in zero-retention mode.
- Voice-enabled Service agents replace static IVR trees with intent-driven telephony conversations. A builder chooses a telephony provider and can connect partner telephony.
- Agentforce Voice for Enhanced Chat v2 lets a customer switch between text and voice in the same thread. A transcript appears in the chat window.

Primary source: https://help.salesforce.com/s/articleView?id=ai.agent_parent_deploy.htm

- Voice-enabled Service agents use Agentforce Voice as the AI layer for the contact center.

Primary source: https://help.salesforce.com/s/articleView?id=ai.agent_parent_monitor.htm

- Supervisors can monitor voice-enabled agents on active calls in Omni Supervisor and review performance in agent analytics.

### Testing

Primary source: https://help.salesforce.com/s/articleView?id=ai.agent_parent_test.htm

- Single-session testing in Agentforce Builder is the first step: a builder walks utterances, checks configuration, and revisits tests after changes.
- Agentforce Testing Center runs batch tests. It generates custom scenarios and evaluates response accuracy, conversation quality, subagent recognition, action execution, and knowledge retrieval.
- An Agent Testing Strategy page ties intended outcomes to observability tools, KPIs, and a test-and-monitor plan before go-live.
- Enhanced event logs, on supported agent types, store conversation data so a session’s events and messages appear in one place. Without them, message-sent events are logged but message text is not.
- The legacy builder has a separate troubleshooting guide.

Primary source: https://developer.salesforce.com/docs/ai/agentforce/guide/get-started-agents.html

- Testing Center uses CSV test definitions in the Salesforce UI and does not support custom evaluations.
- Agentforce DX runs YAML test specifications from the CLI and supports custom evaluations.
- Testing API uses Metadata API and Connect API with XML test definitions and supports custom evaluations.

Primary source: https://help.salesforce.com/s/articleView?id=ai.generative_ai_usage.htm

- Agentforce Grid is a metered surface used for testing and also across design and production. Grid usage is metered in every AI lifecycle phase.

### Monitoring and session tracing

Primary source: https://help.salesforce.com/s/articleView?id=ai.agent_parent_monitor.htm

- Agent Analytics reports on performance, usage, quality, trust, cost, and ROI. It is built on the Session Tracing Data Model (STDM), which logs each event in a session.
- Agent Optimization inspects a session from the first user request through the agent’s resolution.
- Agent Health Monitoring detects silent failures such as spiking error rates or high latency in near-real time and notifies the org.
- Legacy Agentforce Analytics uses Data 360 dashboards and reports to review adoption and to adjust subagents and actions.
- Agentforce Session Tracing writes detailed interaction data to a unified model on Data 360 for dashboards, reports, and queries in sandbox or production.
- Monitor Agent Guardrails tracks instruction adherence and task resolution.
- Session log events are stored in the AI Agent Session Log data model object (DMO).

Primary source: https://developer.salesforce.com/docs/ai/agentforce/guide/get-started-agents.html

- Export Session Tracing Data produces a single JSON view of a full agent session trace.

### MCP, Gateway, multi-agent orchestration, and APIs

Primary source: https://help.salesforce.com/s/articleView?id=ai.agent_parent_extend.htm

- MCP for Agentforce registers third-party tools so agents can call them.
- Agentforce Gateway applies policies to connections to external APIs and MCP servers: access control, usage limits, and compliance.
- Multi-Agent Orchestration connects Agentforce agents in the same org so they collaborate on a task. A single agent can be deployed across channels with shared context.
- Invocable actions call an Agentforce Service agent, Agentforce Employee agent, or Agentforce (Default) from a flow or Apex class for background or event-driven work.
- Headless Agentforce development builds, deploys, and operates agents without Agentforce Builder or Setup, using AI coding assistants, Salesforce skills, and related tools.

Primary source: https://developer.salesforce.com/docs/ai/agentforce/guide/agent-api.html

- Agent API is a REST API for starting a session, sending and receiving messages, and ending a session. It can connect a website, a headless agent, another platform, or another agent.
- Access uses an external client app with the client credentials flow. Source: https://developer.salesforce.com/docs/ai/agentforce/guide/agent-api-get-started.html

Primary source: https://developer.salesforce.com/docs/ai/agentforce/guide/agent-dx.html

- Agents are Salesforce metadata. Agentforce DX adds CLI commands and a VS Code extension to create, preview, test, and move agent metadata among a DX project, scratch orgs, sandboxes, and production.
- A builder can switch between Agentforce Builder / Flow Builder in the org and VS Code / Salesforce CLI locally, then keep the DX project in sync.
- Agentforce DX can generate an authoring bundle that contains the Agent Script blueprint, preview in simulated or live mode, and publish the bundle to the org.
- Salesforce CLI and its core plugins, including Agentforce DX, release weekly.

Primary source: https://developer.salesforce.com/docs/ai/agentforce/guide/get-started-agents.html

- The Agentforce Python SDK creates, manages, and deploys agents programmatically.
- Custom Connections attach external chat clients to Agent API with structured response formats.

### Einstein Trust Layer, permissions, and compliance

Primary source: https://help.salesforce.com/s/articleView?id=ai.copilot_trust.htm

- Agentforce is integrated with the Einstein Trust Layer: zero data retention with third-party LLMs, dynamic grounding with secure data retrieval, prompt defense (system policies and prompt-injection detection), toxicity detection, and audit and feedback stored in Data 360.
- Pattern-based and field-based data masking in the Trust Layer is disabled for agents. Data accessed by agents, including PII, is protected in transit and is not stored or used for training by external LLM providers under the zero-retention policy.
- Ethical guardrails target hallucinations. Security guardrails target prompt injection and similar attacks. Subagent instructions set further boundaries. Instruction adherence shows how well the agent follows those instructions.
- Service agent templates use subagent instructions to decide when to escalate to a service rep. Lead Nurturing (SDR) uses admin-defined engagement rules for when the agent may work a lead and when it may send email.
- Agents honor licenses, permissions, field-level security, and sharing. Custom action access follows the Apex class, flow, or prompt template the action calls.
- Agentforce enforces the org’s trusted URL allowlist. Unapproved URLs in a response are replaced with `URL_Redacted`. The plan canvas shows an error when the agent tries to call or generate an unapproved URL. Citation source URLs still appear even if the domain is not allowlisted.
- Agentforce is a Covered Service in the Einstein Platform and Agentforce SOC 2 and SOC 3 reports. It is HIPAA eligible under the Salesforce Business Associate Addendum Restrictions and has ISO 27001, 27017, and 27018 certifications.

Primary source: https://developer.salesforce.com/docs/ai/agentforce/guide/trust.html

- Trust Layer protections listed for developers include CRM grounding, masking of sensitive data such as social security numbers (masking is disabled for agents in Help), toxicity detection, audit trail and feedback, and zero-retention agreements with third-party LLM partners including OpenAI.
- Salesforce’s documented generative-AI principles on that page are accuracy, safety, transparency, empowerment, and sustainability. The page states a human should check model responses before sharing them with end users in the majority of use cases.

Primary source: https://help.salesforce.com/s/articleView?id=ai.copilot_overview.htm

- Manage AI Agents grants org-wide rights to manage, activate, and deactivate agents, customize subagents and actions, and monitor activity. Help says to assign it only to users who need that access. Source: https://help.salesforce.com/s/articleView?id=ai.agent_setup_explore_types.htm

### Usage and billing

Primary source: https://help.salesforce.com/s/articleView?id=ai.generative_ai_usage.htm

- Salesforce documents three AI pricing models: consumption-based (prompts or actions), hybrid (per-user monthly license plus consumption, with Flex Credits when license conditions are not met), and business-metrics-based (examples: Agentforce Voice minutes and characters translated).
- Agentic usage is metered by actions. Prompt-based embedded AI is metered by prompts.
- Native units convert to Flex Credits through the Agentforce Rate Card. Other documented meters include Conversations and Einstein Requests.
- Metered usage is visible in the org’s Digital Wallet.
- Designing and building in Agentforce Builder is not metered. Previewing an agent in chat or voice is metered.
- Testing in Agentforce Builder, Agentforce Grid, Testing Center, and sandbox is metered, including voice and chat preview and batch tests.
- Production consumption covers live autonomous agent workflows and user-triggered prompts.
- Agentforce Employee agents require Flex Credits. Source: https://help.salesforce.com/s/articleView?id=ai.agent_setup_explore_types.htm

### Prompt Builder and models

Primary source: https://developer.salesforce.com/docs/ai/agentforce/guide/get-started-prompt-builder.html

- Prompt Builder creates prompt templates grounded in CRM merge fields (record fields, flows, related lists, and Apex). Templates can run on record pages or as Agentforce actions that generate summaries, descriptions, and other field values.
- Templates are callable from Connect REST API, Apex, invocable actions, Flow or Apex batch processing, and Metadata API (`GenAiPromptTemplate`).

Primary source: https://developer.salesforce.com/docs/ai/agentforce/guide/models-get-started.html

- Salesforce-managed models are enabled by default. AI Models configures and tests models. BYOLLM connects external OpenAI, Azure, Vertex, or Bedrock models. LLM Open Connector hosts custom models.
- Models API generates text, chat, and embeddings over Apex and REST. Calls go through the Einstein Trust Layer. Source: https://developer.salesforce.com/docs/ai/agentforce/guide/models-api.html

## Sources

- https://help.salesforce.com/s/articleView?id=ai.copilot_overview.htm
- https://help.salesforce.com/s/articleView?id=ai.copilot_building_blocks.htm
- https://help.salesforce.com/s/articleView?id=ai.agent_builder_reasoning_engine.htm
- https://help.salesforce.com/s/articleView?id=ai.agent_setup_explore_types.htm
- https://help.salesforce.com/s/articleView?id=ai.agent_parent_setup.htm
- https://help.salesforce.com/s/articleView?id=ai.agent_parent_configure.htm
- https://help.salesforce.com/s/articleView?id=ai.agent_parent_test.htm
- https://help.salesforce.com/s/articleView?id=ai.agent_parent_deploy.htm
- https://help.salesforce.com/s/articleView?id=ai.agent_parent_monitor.htm
- https://help.salesforce.com/s/articleView?id=ai.agent_parent_extend.htm
- https://help.salesforce.com/s/articleView?id=ai.copilot_trust.htm
- https://help.salesforce.com/s/articleView?id=ai.generative_ai_usage.htm
- https://help.salesforce.com/s/articleView?id=ai.agentforce_voice.htm
- https://help.salesforce.com/s/articleView?id=ai.agent_language_support.htm
- https://developer.salesforce.com/docs/ai/agentforce/overview
- https://developer.salesforce.com/docs/ai/agentforce/guide/agent-script.html
- https://developer.salesforce.com/docs/ai/agentforce/guide/ascript-ref-actions.html
- https://developer.salesforce.com/docs/ai/agentforce/guide/agent-dx.html
- https://developer.salesforce.com/docs/ai/agentforce/guide/get-started-agents.html
- https://developer.salesforce.com/docs/ai/agentforce/guide/agent-api.html
- https://developer.salesforce.com/docs/ai/agentforce/guide/agent-api-get-started.html
- https://developer.salesforce.com/docs/ai/agentforce/guide/adl.html
- https://developer.salesforce.com/docs/ai/agentforce/guide/trust.html
- https://developer.salesforce.com/docs/ai/agentforce/guide/get-started-prompt-builder.html
- https://developer.salesforce.com/docs/ai/agentforce/guide/models-get-started.html
- https://developer.salesforce.com/docs/ai/agentforce/guide/models-api.html
- https://www.salesforce.com/agentforce/
