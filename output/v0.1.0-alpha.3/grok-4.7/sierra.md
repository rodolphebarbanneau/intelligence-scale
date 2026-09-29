## Intelligence Scale type

I'll follow the evaluation skill and rate only the product in the spec.

The skill and Sierra spec are large, so I'll read them in sections and follow the skill exactly.

The spec is the brief. I'll verify the cited product pages that decide Type II and Type III before scoring.

**Intelligence Scale capability: 2.6 / 3.0**

Type II with partial Type III capabilities.

Evaluated 2026-09-29. Subject is Sierra Agent OS, the enterprise chassis for one customer-facing agent (Studio, SDK, Ghostwriter, Horizon, Context Engine/ADP, Insights). Public docs at docs.sierra.ai are gated; grades use the spec and cited product pages and official blogs. Marketing language was not treated as extra capability.

The agent can own customer processes: each case arrives on a channel or Horizon signal, is carried to an outcome, and repeats. People set journeys, policy, and guardrails and handle exceptions. It does not yet orchestrate the operating system. Work selection stays inside human playbooks, actors do not delegate to each other, and process changes do not ship without a person.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| I.1 | 1.00 | Production agent on voice, chat, email, SMS, messaging, and ChatGPT, plus Live Assist in care work. Not an isolated API. | https://sierra.ai/product, https://sierra.ai/product/channels, https://sierra.ai/blog/agent-os-2-0 |
| I.2 | 1.00 | Knowledge, 40+ integrations, systems of record, and ADP memory across conversations, CRM, billing, and transactions. | https://sierra.ai/product/agent-studio, https://sierra.ai/blog/agent-data-platform, https://sierra.ai/blog/agent-studio-2-0 |
| I.3 | 1.00 | Multi-step journeys complete returns, order updates, claims, warranties, and on-call card/ACH payments. | https://sierra.ai/product, https://sierra.ai/product/voice, https://sierra.ai/uk/blog/sierra-achieves-aiuc-1-certification |
| I.4 | 1.00 | Review-before-ship, traces, QA to production with rollback, Live Assist continuation, and audit of reasoning and systems used. | https://sierra.ai/product/ghostwriter, https://sierra.ai/blog/agent-studio-2-0, https://sierra.ai/blog/your-agent-laid-bare-and-why-it-matters |
| I.5 | 1.00 | Versioned releases, always-on monitors, and outcome-priced handling across ongoing deployments. | https://sierra.ai/product, https://sierra.ai/blog/outcome-based-pricing-for-ai-agents, https://sierra.ai/blog/agent-monitoring |
| II.1 | 1.00 | One persistent agent takes each case from a channel or signal to a billed outcome (resolve, save, return, claim, renewal) across runs. People set the mandate and take escalations. | https://sierra.ai/product/horizon, https://sierra.ai/blog/outcome-based-pricing-for-ai-agents, https://sierra.ai/blog/serving-customer-experience-and-engineering-teams-all-from-one-platform |
| II.2 | 1.00 | After start, the agent moves through steps, tools, and branches. Human sign-off is a configured guardrail, not a required step between actions. | https://sierra.ai/product/agent-sdk, https://sierra.ai/product/horizon, https://sierra.ai/blog/agent-studio-2-0 |
| II.3 | 1.00 | During a run it uses granted knowledge, CRM, orders, payments, and handoff. No person coordinates each call. Setup binding does not lower this. | https://sierra.ai/product/agent-studio, https://sierra.ai/blog/agent-studio-2-0, https://sierra.ai/product/voice |
| II.4 | 1.00 | Durable named agent: cross-run ADP memory, guardrail permissions, integration credentials, and Horizon state over days or weeks. | https://sierra.ai/product/context-engine, https://sierra.ai/blog/agent-data-platform, https://sierra.ai/blog/agent-studio-2-0 |
| II.5 | 1.00 | Traces, monitors, Explorer, live correct/block/escalate, handoff, audit, and rollback. People supervise exceptions rather than routine steps. | https://sierra.ai/product/insights, https://sierra.ai/blog/agent-monitoring, https://sierra.ai/uk/blog/sierra-achieves-aiuc-1-certification |
| II.6 | 1.00 | Inbound channels and Horizon signals start work. Jobs continue in the background across days or weeks, including outbound. | https://sierra.ai/product/horizon, https://sierra.ai/product/context-engine, https://sierra.ai/blog/agent-data-platform |
| III.1 | 1.00 | Routine customer operations run 24/7 without a person in each case. Escalation is the exception path. Domain breadth is not scored here. | https://sierra.ai/product, https://sierra.ai/blog/outcome-based-pricing-for-ai-agents, https://sierra.ai/product/live-assist |
| III.2 | 0.75 | Horizon/ADP choose the next customer action from signals inside a human strategy. They do not allocate work across operators. One kind of work. | https://sierra.ai/product/horizon, https://sierra.ai/product/context-engine, https://sierra.ai/blog/agent-data-platform |
| III.3 | 0.25 | No persistent actors delegate operational work to each other. Supervisors are a response guardrail. Explorer to Ghostwriter is human-gated. API/MCP to other agents is buyer-wired. | https://sierra.ai/product/trust-and-reliability, https://sierra.ai/product/explorer, https://sierra.ai/blog/your-agent-laid-bare-and-why-it-matters |
| III.4 | 0.75 | Signals, action, and memory change the next customer decision. Experiment results do not change production until a person promotes them. | https://sierra.ai/product/context-engine, https://sierra.ai/blog/agent-data-platform, https://sierra.ai/blog/let-your-customers-shape-your-agents |
| III.5 | 0.50 | Next-best-action stays inside human journeys and playbooks. Ghostwriter can edit the process but cannot ship without approval. Not new operational paths or reallocated responsibilities. | https://sierra.ai/product/horizon, https://sierra.ai/product/ghostwriter, https://sierra.ai/blog/agent-studio-2-0 |
| III.6 | 1.00 | Policy, guardrails, audit, release control, and exception alerts let people govern while routine cases run unattended. | https://sierra.ai/product/trust-and-reliability, https://sierra.ai/blog/your-agent-laid-bare-and-why-it-matters, https://sierra.ai/product/horizon |

* **Completed floor:** 2
* **Next Type raw progress:** 0.71
* **Weakest criterion:** 0.25 (III.3)
* **Weakest-link penalty:** 0.13
* **Adjusted progress:** 0.58
* **Final score:** **2.6**

### What prevents the next Type?

Type III needs every III criterion at 1.00. Four are short:

* **III.3** — Persistent actors do not delegate or collaborate on operational work without a person.
* **III.5** — The agent does not change how work is organized. Process edits stay human-approved.
* **III.2** — Next-work choice is limited to customer playbooks, not allocation across actors.
* **III.4** — Outcome evaluation does not autonomously change production processes.

## Execution coverage

I'll follow the evaluation skill and rate only the product in the spec.

The spec is too large to read at once. I'll load it in sections and use only its cited sources.

The spec is a customer-agent platform with gated docs. I'll verify the cited product pages before scoring.

The product pages are thin in markdown. I'll pull the raw pages and the blog posts the spec cites.

Agent Studio 2.0 confirms a no-code library and private workspaces. I'll check the remaining cited posts for reach, sharing, and adoption.

**Execution coverage: 0.59 / 1.00**

Sierra Agent OS, the hosted enterprise platform as of 29 September 2026, carries customer-facing agent work: support conversations, contact-center assist, and long-running customer journeys on voice, chat, email, SMS, messaging, and ChatGPT. The rest of the company has no native path. Docs at `docs.sierra.ai` are gated; this rating uses the spec and the cited product pages and official posts.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| E.1 | 0.50 | One business function: customer-facing agents that answer, act, and hand off. Claims, mortgages, returns, and upsells are tasks of that same agent, not separate departmental surfaces. Engineering, HR, finance, and legal have no native path. | https://sierra.ai/product |
| E.2 | 0.75 | Shared org agent, roles, and Live Assist: the agent guides a representative in the live conversation and handoff carries context. Agent Studio workspaces are private; collaboration is GitHub-style snapshots, not several people plus the operator in one thread. | https://sierra.ai/blog/agent-studio-2-0 ; https://sierra.ai/blog/agent-os-2-0 ; https://sierra.ai/blog/your-agent-laid-bare-and-why-it-matters |
| E.3 | 0.75 | Integration Library: pick a connector, add credentials and endpoints, publish tools that can process a return, update an order, or read account data. CRM, billing, orders, and contact centers are categories. Named systems of record are not documented as shipped read/write jobs, so this is not 1.00. | https://sierra.ai/blog/agent-studio-2-0 ; https://sierra.ai/product/agent-studio |
| E.4 | 0.75 | First-party Integration Library, mostly connectors, one job family, not open to third-party publishing. Custom entries are Agent SDK work, not a marketplace of agents. | https://sierra.ai/blog/agent-studio-2-0 |
| E.5 | 1.00 | Agent Studio plus customer channels (voice, chat, email, SMS, WhatsApp, ChatGPT) plus API/embed (Headless API; other agents call Sierra through APIs). | https://sierra.ai/product/channels ; https://sierra.ai/blog/agent-os-2-0 ; https://sierra.ai/blog/agent-data-platform ; https://sierra.ai/blog/your-agent-laid-bare-and-why-it-matters |
| E.6 | 0.75 | Sign-in, roles, environments, and versioned releases exist, on one enterprise path with gated docs. Start is a Sierra engagement and a forward-deployed team, not a public trial. | https://sierra.ai/product ; https://sierra.ai/blog/serving-customer-experience-and-engineering-teams-all-from-one-platform ; https://docs.sierra.ai/ |
| E.7 | 0.50 | Ghostwriter builds or updates the customer agent from a prompt or uploaded SOPs, then a person reviews and ships. That generated path is one function, not several. | https://sierra.ai/product/ghostwriter |

* **Raw mean:** 0.71
* **Weakest criterion:** 0.50
* **Weakest-link penalty:** 0.13
* **Uncapped score:** 0.59
* **Span cap:** none
* **Final score:** **0.59**

### What most limits coverage?

E.1 and E.7. The product is a customer-experience agent, not a surface for other functions, and Ghostwriter only generates that one kind of job. There is no public catalog of named systems of record with documented read/write jobs, and no self-serve trial; those limits sit on E.3 and E.6 and are not the floor.
