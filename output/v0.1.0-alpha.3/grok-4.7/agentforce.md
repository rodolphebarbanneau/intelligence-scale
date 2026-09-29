## Intelligence Scale type

I'll follow the evaluation skill and rate only the product in the spec.

The skill and Agentforce brief are long, so I’ll finish both before scoring.

I’ll verify the Type II claims in the cited Salesforce docs before scoring.

Help pages didn’t return body text. I’ll try the developer docs and raw HTML.

Agent API shows an agent-assigned user. I’ll confirm identity, triggers, and multi-agent behavior in the cited docs.

**Intelligence Scale capability: 1.9 / 3.0**

Approaching Type II. Evaluated 2026-09-28, strongest current configuration: Agentforce Service, Lead Nurturing, and custom agents on Enterprise, Performance, Unlimited, or Developer with Foundations or Agentforce 1, built in Agentforce Builder with Agent Script. Retired Agentforce (Default) is excluded.

People can hand a service case or lead-engagement mandate to a persistent agent. Omni-Channel, messaging, email, and voice deliver each case; Atlas and Agent Script run the steps and tools; humans set guardrails and take escalations. That is delegated execution for those processes, not only chat assistance. It stops short of Type II because documented starts are inbound events, queues, and Flow or Apex invocable calls. A native schedule that starts runs is not documented.

| Criterion | Grade | Evidence | Source |
| --- | ---: | --- | --- |
| I.1 | 1.00 | Agents sit in Lightning, mobile, Slack, messaging, email, and voice as normal work surfaces. | https://help.salesforce.com/s/articleView?id=ai.agent_parent_deploy.htm |
| I.2 | 1.00 | CRM grounding, data libraries, web search, files, and Flow, Apex, and prompt actions are first-class. | https://developer.salesforce.com/docs/ai/agentforce/guide/adl.html |
| I.3 | 1.00 | Atlas selects a subagent, chains actions, and loops up to seven times inside a bounded request. | https://help.salesforce.com/s/articleView?id=ai.agent_builder_reasoning_engine.htm |
| I.4 | 1.00 | Builders test, activate, and direct agents; users continue chats; escalation returns work to a person. | https://help.salesforce.com/s/articleView?id=ai.agent_parent_test.htm |
| I.5 | 1.00 | Activated, versioned agents are org metadata with licenses and permissions, not one-off demos. | https://help.salesforce.com/s/articleView?id=ai.agent_setup_explore_types.htm |
| II.1 | 1.00 | Service and Lead Nurturing agents take queued conversations or rule-eligible leads through reply, meeting, or escalation, then repeat. Humans set the mandate. | https://help.salesforce.com/s/articleView?id=ai.agent_parent_deploy.htm |
| II.2 | 1.00 | After a run starts, scripted transitions, action chaining, and the reasoning loop proceed without a person between steps. Escalation is the exception path. | https://developer.salesforce.com/docs/ai/agentforce/guide/agent-script.html |
| II.3 | 1.00 | During a run the agent chooses granted Salesforce actions, knowledge, and utilities. Setup-time grants do not lower this. | https://developer.salesforce.com/docs/ai/agentforce/guide/ascript-ref-actions.html |
| II.4 | 1.00 | A durable agent has an agent-assigned user, permissions, Agent Memory across conversations, and CRM plus session state. | https://developer.salesforce.com/docs/ai/agentforce/guide/agent-api-get-started.html |
| II.5 | 1.00 | Analytics, session tracing, health alerts, Trust Layer audit, deactivation, and escalation let people supervise exceptions. | https://help.salesforce.com/s/articleView?id=ai.agent_parent_monitor.htm |
| II.6 | 0.75 | Inbound channels, Omni-Channel queues, and event-driven invocable calls start background runs. A native agent schedule is not documented. | https://help.salesforce.com/s/articleView?id=ai.agent_parent_extend.htm |
| III.1 | 0.75 | Routine service and lead work can run without a person. Other operations stay human-executed unless custom agents are built. | https://help.salesforce.com/s/articleView?id=ai.agent_setup_explore_types.htm |
| III.2 | 0.25 | The agent picks the next subagent or action inside a designed script. It does not decide or allocate the organization's next work. | https://help.salesforce.com/s/articleView?id=ai.agent_builder_reasoning_engine.htm |
| III.3 | 0.50 | Multi-agent orchestration, agent-to-agent API calls, and routing to another agent are primitives people connect. | https://developer.salesforce.com/docs/ai/agentforce/guide/agent-api.html |
| III.4 | 0.50 | Memory carries conversation details into later replies. Outcome evaluation and agent changes stay with people using analytics. | https://help.salesforce.com/s/articleView?id=ai.agent_parent_setup.htm |
| III.5 | 0.25 | Branches and tool choice follow a human-authored script. The builder assistant does not rewrite live orchestration. | https://developer.salesforce.com/docs/ai/agentforce/guide/agent-script.html |
| III.6 | 1.00 | Permissions, Trust Layer, escalation rules, audit, and activation let humans govern rather than execute routine service runs. | https://help.salesforce.com/s/articleView?id=ai.copilot_trust.htm |

* **Completed floor:** 1
* **Next Type raw progress:** 0.96
* **Weakest criterion:** 0.75 (II.6)
* **Weakest-link penalty:** 0.06
* **Adjusted progress:** 0.90
* **Final score:** **1.9**

### What prevents the next Type?

II.6. Event, queue, and invocable triggers start runs, and work continues in the background, but a first-class schedule that starts process runs is not a documented native capability. Until II.6 is 1.00, the Type II gate fails and the score cannot reach 2.0.

## Execution coverage

I'll follow the evaluation skill and rate only the product in the spec.

The spec is large, so I’ll read it in sections and only use its cited sources.

I’ll check the cited Salesforce docs for span, sharing, reach, catalog, surfaces, and ready-made jobs.

Help pages didn’t render. I’ll pull the developer docs that did, and check how suite products are graded.

**Execution coverage: 0.59 / 1.00**

Agentforce, evaluated 29 September 2026, is Salesforce’s hosted agent platform in its current supported configuration: Employee, Service, Lead Nurturing, Sales Coach, and Service Assistant on Enterprise, Performance, Unlimited, or Developer Edition with Foundations or Agentforce 1. Retired Agentforce (Default) is out of scope. An organization can put sales, service, employee, and admin work on it inside the Salesforce suite. Agents update CRM records, answer from knowledge, reply on Service Email, and hand a conversation to a person. They run in Lightning and the mobile app, in Slack, on customer chat, email, and voice, and through the Agent API. Work outside that suite has no native path unless a builder wires custom actions or MCP.

| Criterion | Grade | Evidence | Source |
| --------- | ----: | -------- | ------ |
| E.1 | 0.75 | Sales (Lead Nurturing, Sales Coach), service (Service Agent, Service Assistant), employee cross-department work, and admin Setup ship today. The chassis is the Salesforce suite, not a general company surface. | https://help.salesforce.com/s/articleView?id=ai.agent_setup_explore_types.htm |
| E.2 | 0.75 | An org agent, a Slack connection so the team works with the agent, and Omni-Channel escalation that transfers the conversation and history. Live multiplayer of several people plus the operator in one thread is not fully specified. Supervisors monitor voice calls. | https://help.salesforce.com/s/articleView?id=ai.agent_parent_deploy.htm |
| E.3 | 0.50 | Shipped read/write is one suite’s objects: Salesforce records, knowledge and files, and Service Email. External mail, calendar, and files are not documented as shipped jobs. MCP and Apex/Flow are buyer-wired. | https://help.salesforce.com/s/articleView?id=ai.copilot_building_blocks.htm |
| E.4 | 0.50 | Official templates and standard subagents cover more than one job. There is no marketplace the vendor, third parties, and customers publish into. The next job is a custom action or MCP the builder assembles. | https://help.salesforce.com/s/articleView?id=ai.agent_parent_configure.htm |
| E.5 | 1.00 | Lightning panel and Salesforce mobile, Slack, customer messaging, Service Email, and voice, plus Agent API and chat/mobile embed SDKs. | https://help.salesforce.com/s/articleView?id=ai.agent_parent_deploy.htm |
| E.6 | 0.75 | Documented Setup, Manage AI Agents, and Studio in the App Launcher. Adoption needs Foundations or Agentforce 1, Flex Credits for Employee Agent, and an admin to activate. | https://help.salesforce.com/s/articleView?id=ai.agent_parent_setup.htm |
| E.7 | 0.75 | Out-of-the-box agents and templates span several functions. A builder still connects channels, actions, and flows. Describing behavior can generate script; AI Assistance in the builder is beta. | https://developer.salesforce.com/docs/ai/agentforce/guide/agent-script.html |

* **Raw mean:** 0.71 (5.00/7 = 0.7143)
* **Weakest criterion:** 0.50
* **Weakest-link penalty:** 0.125
* **Uncapped score:** 0.59 (0.7143 − 0.125 = 0.5893, half down)
* **Span cap:** none
* **Final score:** **0.59**

### What most limits coverage?

System reach and the catalog, both 0.50. Native read/write stops at Salesforce objects. There is no documented shipped read/write of independent mail, calendar, or file systems, and MCP does not count as shipped reach. Coverage grows through templates, not a directory third parties and customer organizations can publish into. The next job still needs a builder to assemble actions, flows, Apex, or MCP.
