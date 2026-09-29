---
name: Microsoft 365 Copilot
slug: microsoft-365-copilot
url: https://www.microsoft.com/microsoft-365-copilot
docs: https://learn.microsoft.com/en-us/microsoft-365/copilot/
kind: product
reviewed: 2026-09-28
---

# Microsoft 365 Copilot

## Product

Microsoft 365 Copilot is Microsoft’s work AI product for organizations. It sits inside Microsoft 365 and uses large language models with Microsoft Graph, Work IQ, and the Microsoft 365 apps. Microsoft Learn now also names the licensed work experience Microsoft Copilot and the included chat experience Microsoft Copilot Chat. The public product URL and this file keep the Microsoft 365 Copilot name.

It is an add-on plan on eligible Microsoft 365, Office 365, Teams, Exchange, SharePoint, OneDrive, Planner, Visio, and related subscriptions. Education and US government clouds have their own prerequisite lists. Microsoft 365 E7 includes Microsoft Copilot. Copilot Chat is included with eligible Microsoft 365 subscriptions. Microsoft 365 Copilot (Basic) is in-app Copilot without the add-on license. Microsoft 365 Copilot (Premium) is the full add-on: Graph and Work IQ grounding, Copilot Search, semantic indexing, SharePoint Advanced Management, Purview controls, agents on web and work data, usage reports, and Cowork on usage-based billing.

People sign in with a Microsoft Entra work or school account. They use it at https://m365copilot.com/, in the Microsoft Copilot app on web, Windows, macOS, Android, and iOS, and inside Word, Excel, PowerPoint, Outlook, OneNote, Teams, SharePoint, OneDrive, and related apps. Chat, Search, Create, Pages, Notebooks, agents, and Cowork are modules in that app. Admins assign licenses, set Copilot controls, and manage agents, connectors, spending, and security from the Microsoft 365 admin center.

Data access follows the signed-in user’s permissions. Prompts, responses, and Graph data are not used to train foundation LLMs. Enterprise Data Protection applies when users sign in with Entra accounts.

Out of scope here: Microsoft Security Copilot, GitHub Copilot, Microsoft Copilot Studio as a separately licensed maker product, and consumer Copilot signed in with a personal Microsoft account. Copilot Studio, Agent Builder, and the Microsoft 365 Agents Toolkit appear only as ways to extend this product.

## Features

### Licenses and access

Primary source: https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview

- Copilot Chat (Basic) is included with eligible Microsoft 365 licenses. It is enterprise chat grounded mainly in web data. Organizational content is used only when the user uploads or pastes it, works with open content in Outlook or Teams, or uses a pay-as-you-go agent.
- Microsoft 365 Copilot (Basic) is in-app Copilot in Word, Excel, PowerPoint, and OneNote without the add-on license. Access is subject to service capacity.
- Microsoft 365 Copilot (Premium) is the add-on license. It includes Basic in-app features plus priority access, Graph and Work IQ grounding, Copilot Search, semantic indexing, SharePoint Advanced Management, Purview classification and prompt review, agents on web and work data, usage reports, and Cowork via usage-based billing.
- Premium users reach Copilot at https://m365copilot.com/, in the Microsoft 365 desktop app, and in Word, Excel, PowerPoint, and OneNote.
- Work IQ can be turned on or off. When it is on, Premium responses use web, Graph, and Work IQ. When it is off, responses are not enriched with mail, files, meetings, calendars, teams, or organizational relationships.
- The Work IQ API is a separate usage-based offering for custom apps, agents, and integrations. It is not the Work IQ layer included with Premium.
- Admins manage pinning, image generation, agent creation, web search, and Chat access from Copilot controls. An AI Administrator role can manage Copilot without Global Administrator.
- The model selector offers Auto, Quick response, and Think deeper. Auto uses a real-time router. Anthropic subprocessors are opt-in and are not on for all users by default.
- Microsoft Copilot Chat usage reports cover standalone chat. Microsoft Copilot usage reports cover in-app use in Teams, Outlook, Word, Excel, and PowerPoint. Organizational messages can deliver in-app adoption guidance.
- Prerequisite add-on plans include Microsoft 365 Business, E3, E5, F1, F3, Apps, Office 365 E1/E3/E5/F3, Teams, Exchange, SharePoint, OneDrive, Planner, Visio, and Clipchamp, plus listed government and education SKUs. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-licensing
- Web-based Copilot Chat is included at no extra cost on eligible subscriptions. Work-based chat that uses the Entra account’s organizational data requires a Microsoft Copilot license. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-licensing

### Microsoft Copilot app

Primary source: https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-app-overview

- The Microsoft Copilot client runs in the browser at copilot.microsoft.com, as a Windows and macOS desktop app, and as Android and iOS apps.
- The same client hosts personal Microsoft account and Entra work or school sessions. A Work label and account switcher mark the work session. Data does not flow between the two account types.
- Work or school features depend on the assigned Microsoft 365 licenses. A Copilot license unlocks the full app.
- Admins can block personal-account use of the app with Tenant Restrictions.
- The service description lists Chat, Copilot Search, Copilot Notebooks, Pages, Create, Researcher, Analyst, Word/Excel/PowerPoint Agents, Prompt Gallery, and Scheduled Prompts as Microsoft Copilot app features, with cloud-environment differences. Source: https://learn.microsoft.com/en-us/office365/servicedescriptions/office-365-platform-service-description/microsoft-365-copilot
- Admins can show or hide Search, pin Chat, deploy or block agents, allow Pages and Notebooks through Cloud Policy, publish organization brand kits for Create, and map the Copilot key or Windows+C to the app. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-app-admin-settings
- Create is a built-in app module. Admins can publish organizational brand kits and Organizational Asset Library access for Create. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-app-admin-settings

### Copilot Chat

Primary source: https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview

- Copilot Chat (Basic) is available at https://m365copilot.com/, in Microsoft Edge, in Outlook and Teams, and at bing.com/chat, bing.com/copilotsearch, copilot.com, and copilot.ai.
- Edge Copilot Chat can summarize website content and some document types shown in Edge.
- Declarative agents grounded in instructions and public websites are included with Copilot Chat. Other custom agents are pay-as-you-go.
- Work or school users must sign in with Entra before using Copilot via the app, copilot.cloud.microsoft, Edge, or productivity apps.
- Side-by-side Copilot Chat in Word, Excel, PowerPoint, and OneNote needs a Microsoft 365 Copilot Basic or Premium label and a work or school sign-in. Source: https://support.microsoft.com/en-us/microsoft-365-copilot/how-copilot-chat-works-in-microsoft-365-apps
- All eligible subscribers can use Copilot Chat in Outlook. Without the add-on, prompts are limited to inbox, calendar, meetings, and other limited data. With the add-on, chat can use inbox, calendar, meetings, chats, and enterprise data. Source: https://support.microsoft.com/en-us/microsoft-365-copilot/how-copilot-chat-works-in-microsoft-365-apps

### Copilot in Word

Primary source: https://support.microsoft.com/en-us/office/welcome-to-copilot-in-word-2135e85f-a467-463b-b2f0-c51a46d625d1

- Copilot in Word drafts from a prompt, outline, notes, or a referenced file; rewrites selected text; adjusts tone; and summarizes or questions a document.
- It opens from the Copilot Dynamic Action Button into a chat pane with Edit mode on. Users can keep, discard, or refine generated content.
- In shared documents, Copilot previews suggested edits in chat. Nothing is written until the user approves.
- Users can type `/` to attach a document, email, or meeting. A model selector switches reasoning level or a provider such as OpenAI or Claude.
- An optional summary can appear at the top of a Word document, depending on settings and license.
- Word Copilot Chat can draft, summarize, rewrite, and answer questions about the open document. Source: https://support.microsoft.com/en-us/microsoft-365-copilot/how-copilot-chat-works-in-microsoft-365-apps

### Copilot in Excel

Primary source: https://support.microsoft.com/en-us/excel/copilot/get-started-with-copilot-in-excel

- Copilot in Excel edits workbooks with tables, charts, PivotTables, and formulas. Changes stay as ordinary Excel objects.
- It can add, rename, and delete sheets; edit cells and ranges; apply formatting, validation, borders, and styles; generate data and formulas; create charts, PivotTables, and shapes; highlight, sort, and filter; import from other workbooks; and use web search with citations.
- Edit, plan, and chat modes are available. Edit applies changes in the workbook. Plan produces a plan to confirm first. Chat keeps answers in the pane.
- Windows, Mac, and web support edit, chat, and plan. iPad supports chat and plan, with edit rolling out. iPhone and Android support chat, with iPhone edit rolling out.
- Licensed users can also open Agent Mode from Tools for multi-step workbook tasks. Source: https://support.microsoft.com/en-us/microsoft-365-copilot/how-copilot-chat-works-in-microsoft-365-apps

### Copilot in PowerPoint

Primary source: https://support.microsoft.com/en-us/microsoft-365-copilot/how-copilot-chat-works-in-microsoft-365-apps

- Copilot Chat in PowerPoint answers questions about a deck, summarizes slides, generates images, and suggests audience questions.
- Users can start a deck from a prompt or a referenced file, refine an outline in chat, then generate slides. Source: https://support.microsoft.com/en-us/powerpoint/copilot/create-a-new-presentation-with-copilot-in-powerpoint
- From the Microsoft Copilot app, Copilot can create a presentation in OneDrive and return a link to open it. Source: https://support.microsoft.com/en-us/powerpoint/copilot/create-a-new-presentation-with-copilot-in-powerpoint
- The Dynamic Action Button in Word, Excel, and PowerPoint opens the app agent in the right-hand chat pane. Outlook is unchanged. Source: https://support.microsoft.com/en-us/topic/the-copilot-dynamic-action-button-in-word-excel-and-powerpoint-40db4cef-3d59-474d-9dec-f649b5bfab8e

### Copilot in Outlook

Primary source: https://support.microsoft.com/en-us/Outlook/frequently-asked-questions-about-copilot-in-outlook

- Summary by Copilot extracts key points from a thread. Draft with Copilot writes a message from a prompt and thread context. Coaching by Copilot comments on tone, sentiment, and clarity and can apply suggestions.
- Prioritize my inbox assigns high, low, or normal priority and a reason. Users can set topic customizations for priority.
- Chat can triage mail (pin, flag, archive, delete), create or manage Outlook rules, and schedule meetings with up to two other people or add events such as focus time.
- Schedule with Copilot can create a meeting invitation from an email thread. Prepare for your meeting gathers related mail, chat, and pre-reads.
- Themes by Copilot generate appearance themes. Copilot voice reads and discusses mail and calendar.
- Features apply to the user’s primary Exchange Online mailbox only. They do not run on archive, group, shared, or delegate mailboxes, or on S/MIME or Double Key Encryption mail.
- Chat with Copilot in Outlook requires a work or school account and new Outlook for Windows or Outlook on the web.

### Copilot in Teams

Primary source: https://support.microsoft.com/en-us/teams/platform/frequently-asked-questions-about-copilot-in-microsoft-teams

- In chats and channels, Copilot summarizes conversations and surfaces open questions and decisions.
- Compose can rewrite a message, change tone and length, translate, or add context with Custom Tone.
- In meetings and calls, Copilot produces custom summaries, uses conversation and screen-share content, and lists unanswered questions during the meeting.
- During a meeting, Copilot needs to be running or a transcript must be started. After the meeting it uses the latest transcript. Without a transcript it is limited to meeting chat. The organizer can restrict Copilot and transcript access.
- Chat Copilot references the open chat and, unless told otherwise, messages from the last 30 days. It does not summarize images, Loop components, or files shared in the chat.
- The overview lists Teams summarization (up to 30 days), transcription, and action-item capture for Basic in-app Copilot. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview

### Copilot Notebooks and OneNote

Primary source: https://support.microsoft.com/en-us/microsoft-365-copilot/what-are-microsoft-365-copilot-notebooks-in-onenote

- Copilot Notebooks collect Copilot chats, Microsoft 365 files, OneNote pages, and links in one notebook. Copilot answers are grounded in that set.
- Users can generate summaries, action items, drafts, and an audio overview of notebook content.
- Notebooks are available to Microsoft Copilot and Copilot Chat licensed users. Creating a notebook also requires a SharePoint or OneDrive service plan.
- Copilot Chat in OneNote summarizes the current page, drafts to-do lists, and drafts plans from notes on that page. Source: https://support.microsoft.com/en-us/microsoft-365-copilot/how-copilot-chat-works-in-microsoft-365-apps
- Cloud Policy can allow or block creating and viewing Copilot Pages and Copilot Notebooks in the Copilot app. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-app-admin-settings

### Copilot in SharePoint

Primary source: https://learn.microsoft.com/en-us/sharepoint/copilot-in-sharepoint-get-started

- Copilot in SharePoint (public preview; general availability begins rolling out 30 September 2026) lets users ask questions, run workflows, and create sites, pages, reports, and Office files from SharePoint content.
- Everyday understand/create/organize work is included with a Microsoft 365 Copilot license. Advanced work at scale uses Copilot Credits and a spending policy that selects Advanced work in SharePoint.
- Included work covers questions, HTML/Word/Excel/PowerPoint files, pages, libraries, lists, simple rules and approvals, rename and share of individual files, skills, and Autofill metadata.
- Credit-metered work covers large-set synthesis and review, entire sites and solutions, scale edits, multistep AI workflows, real-time Autofill, image generation and edit, and site analytics.
- Site AI settings let owners pick which agent opens from the header, hide Copilot for visitors, and enable advanced document processing. Restricted Content Discovery hides Copilot and AI actions on a site.
- Every site has a ready-made agent scoped to that site. Users with edit permission and a Copilot license can create custom SharePoint agents from a site, library, list, or selected files and share them in Teams or Copilot Chat. Source: https://support.microsoft.com/en-US/SharePoint/copilot-in-sharepoint/get-started-with-agents-in-sharepoint
- SharePoint agents are also available through pay-as-you-go billing. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/pay-as-you-go/overview

### Copilot Cowork

Primary source: https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/

- Cowork carries out multi-step work across Microsoft 365. The user describes an outcome. Cowork drafts and sends mail, schedules meetings, creates Word/Excel/PowerPoint/PDF files, posts in Teams, searches the organization, manages OneDrive and SharePoint files, researches, prepares briefings, and can run scheduled or event-driven tasks.
- Cowork for work or school accounts is generally available. Cowork for personal accounts is in preview.
- Built-in skills include Word, Excel, PowerPoint, PDF, Email, Scheduling, Calendar Management, Meetings, Daily Briefing, Enterprise Search, Communications, Deep Research, Adaptive Cards, and App (Frontier). Users can add up to 50 custom `SKILL.md` files under OneDrive `/Documents/Cowork/skills/`.
- The App skill (Frontier preview) builds lightweight interactive apps from a description. Frontier enrollment is required.
- Plugins from the Microsoft 365 App Store add skills and connectors. Admins can deploy plugins tenant-wide.
- Users start Cowork at https://copilot.cloud.microsoft, in the Copilot desktop app, and in the iPhone and Android apps. They can attach work context, local files, or cloud files, and can dictate.
- Cowork asks before sensitive actions, with risk indicators and options to approve once, skip similar prompts in the session, approve all pending, or cancel. Users can pause, resume, or cancel.
- Cowork can edit an existing Word, Excel, or PowerPoint file in OneDrive or SharePoint in place, keeping version history. Outputs land in a session Output folder and in a OneDrive Cowork folder. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/use-cowork
- Access is granted only by a usage-based spending policy that selects Cowork. The Agents catalog Cowork entry no longer controls access. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance
- Browser use can complete web tasks in Microsoft Edge on the user’s device, inheriting Conditional Access, DLP, and Edge site policies. A Cowork Browsing tenant setting turns it on or off. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance
- Scheduled prompts and event-driven tasks (for example on mail or Teams messages) run as the creating user, with approval defaults, rate limits, loop protection, and unified audit logging. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance
- During a task, files are processed in a temporary isolated environment inside the Microsoft 365 service boundary and removed when the task ends. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance

### Agents

Primary source: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-overview

- Agents are specialized assistants that add knowledge, actions, and automation on top of Copilot. They can retrieve, summarize, and take actions such as sending mail or updating records.
- Declarative agents add instructions, knowledge (Teams, connectors, SharePoint, OneDrive), and API actions. They use Copilot’s orchestrator and models and run in Copilot and apps such as Teams, Word, Excel, and Outlook.
- Custom engine agents bring their own orchestration and models, need separate hosting, can start work without a user prompt, and can run in Copilot and in external apps. They support agent-to-agent delegation.
- Agent Builder in Microsoft 365 Copilot creates declarative agents from microsoft365.com/chat, office.com/chat, and Teams desktop or web. Knowledge can include SharePoint and Copilot connectors. It is not on mobile. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder
- Agent Store lists Microsoft, partner, and organization agents. Admins deploy prebuilt agents, approve Copilot Studio or packaged agents, and assign them to users or groups. Users install from Agent Store across Teams, Outlook, Word, Excel, and PowerPoint. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-agent-store
- The Agent 365 SDK can add Entra identity, managed MCP access to Microsoft 365 data, observability, and notifications in Teams, Outlook, and Word to agents built elsewhere. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-agent-store
- Microsoft preinstalls Researcher and Analyst for Copilot-licensed users. Admins can block them tenant-wide. Admins and users can install other agents under Integrated Apps policies. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-agent-install
- Word, Excel, and PowerPoint Agents are Premium-only file creators in the Copilot app. They use Anthropic models (admin must enable the provider), Work IQ for organizational context, and save output to OneDrive in the tenant. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/wordexcelppt-agents
- Researcher is a preinstalled agent for multi-step research across the web and the user’s files, mail, meetings, and chats. It returns cited, structured reports and can ask clarifying questions. It appears under Agents in Chat. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/researcher-agent

### Copilot Search

Primary source: https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search

- Copilot Search is a licensed, AI search module in the Microsoft Copilot app on desktop, web, and mobile. It appears automatically for eligible Copilot licenses.
- It searches Microsoft 365 and connected non-Microsoft sources, including catalog, custom, and ISV connectors, then can continue the query in chat.
- Natural-language and keyword queries are supported. Copilot Answers (from Copilot Chat) can appear at the top of results, grounded the same way as Chat, including optional web grounding.
- Admins can curate acronyms, bookmarks, and people answers.
- Compared with Microsoft Search, Copilot Search adds semantic search, connector content without extra vertical setup, and Chat integration.

### Microsoft 365 Copilot connectors

Primary source: https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/overview

- Synced tenant connectors index external data into Microsoft Graph for Copilot and Microsoft Search. Admins configure them. They honor source ACLs.
- Synced self-serve connectors let users authenticate and index a limited set of their own recent external content. Disconnecting removes that index.
- Federated connectors fetch live data over MCP without indexing. Docs mark write-back as arriving early October 2026; until then they are read-only.
- Microsoft lists more than 100 prebuilt connectors (for example Box, Google Drive, Salesforce, ServiceNow, Jira). Custom synced connectors use the Graph connectors API or Agents Toolkit. On-premises sources can use the Graph connector agent.
- People-data connectors sync profile data into Microsoft 365 while the source system stays authoritative.
- Connector content can appear in Copilot Chat answers with citations, in Copilot Search, and in Microsoft Search verticals.

### Work IQ

Primary source: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/

- Work IQ is a workplace intelligence layer that lets agents reason over organizational data, context, and tools with permission-aware governance.
- Work IQ API access is billed by usage and is independent of a Microsoft 365 Copilot license. Licensed Copilot users get Work IQ in Copilot experiences and agents; custom and third-party agents are usage-billed.
- The Work IQ MCP exposes ten generic tools (for example fetch, create, update) over mail, calendar, files, people, chat, and sites.
- Chat, A2A, and REST endpoints support conversational use, agent-to-agent delegation, and web apps.

### Personalization, memory, and prompts

Primary source: https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-personalization-memory

- Copilot memory (preview, Frontier) includes saved memories, details inferred from chat history, and custom instructions. Data is stored in a hidden Exchange mailbox folder.
- Enhanced personalization is on by default and can be turned off per user or tenant, including through Microsoft Graph `enhancedPersonalizationSetting`.
- Saved memories persist until the user deletes them. Chat-history details can be dropped as Copilot updates them; deleting the originating chats removes those details within seven days.
- Purview retention policies do not apply to Copilot memory. Admins can search and delete memory via eDiscovery and Graph (`IPM.Contact` in the CopilotMemory folder). Memory actions do not write Purview audit entries.
- Organizational prompts are admin-authored prompts (up to 1,000) shown in Copilot Chat, Edge, and Teams as suggestions, prompt-lab cards, and typeahead. AI Administrator or Search Editor can create, import, pin (up to four), and export them. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/organizational-prompts
- Scheduled prompts run Copilot on a schedule in Teams, Office.com chat, and Outlook. They require a Copilot license and connected experiences. Admins can inventory them in the Microsoft 365 Power Platform environment. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/scheduled-prompts

### People Skills

Primary source: https://learn.microsoft.com/en-us/microsoft-365/copilot/people-skills-overview

- People Skills builds skill profiles on a customizable taxonomy and feeds Copilot, agents, Microsoft 365, and Viva. It ships with Copilot or Viva licenses.
- Skills appear on the Microsoft 365 profile card, in people search, Org Explorer, People Companion, and, with a Copilot license, in Copilot people queries.
- AI inferencing is included for Copilot and listed Viva plans. E3/E5 tenants with Copilot can opt in other users.

### Billing

Primary source: https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-overview-copilot-credits

- Copilot Credits meter usage-based services. Billing methods include subscription licenses, Copilot Credit Pre-purchase Plan (P3), pay-as-you-go, prepaid capacity packs, and combinations.
- Cost management in the Microsoft 365 admin center sets spending policies, user and group access, limits, alerts, credit-request routing, and consumption views by policy, user, group, agent, and service.
- Cowork, apps built with Cowork, and the Work IQ API are managed in this Copilot Credits dashboard. Enabling or disabling Cowork also enables or disables Cowork app building by default.
- A separate pay-as-you-go service covers Copilot Chat, SharePoint agents, and Microsoft Copilot Retrieval API (preview), billed through an Azure subscription and billing policies. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/pay-as-you-go/overview
- Global, Billing, and AI administrators can manage pay-as-you-go. Global reader is read-only. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/pay-as-you-go/overview

### Admin and Copilot controls

Primary source: https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-controls/overview

- Copilot controls cover security and governance, management (licensing, metering, agent lifecycle, customization), and measurement (Copilot Analytics: readiness, adoption, productivity, ROI).
- Settings live in the Microsoft 365 admin center, Power Platform admin center, and Copilot Studio.
- Setup includes assigning licenses, update channels, SharePoint readiness, network allow lists, and the Copilot setup guide. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-licensing
- Copilot honors Conditional Access and MFA. Access is scoped to the signed-in user’s Graph permissions, including Restricted SharePoint Search and sensitivity labels. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-architecture
- Prompt and response history is stored as Copilot activity history. Users can delete it from the My Account portal. Admins can search it with Content search or Purview and set retention. Teams Export APIs cover Teams Copilot chats. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy

### Security, privacy, and compliance

Primary source: https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy

- Copilot, including Copilot Search, is covered by existing Microsoft 365 commercial privacy, security, and compliance commitments, including GDPR and the EU Data Boundary.
- Prompts, responses, and Graph data are not used to train foundation LLMs. Optional product feedback can be used to improve Copilot and is admin-controllable; it is not used to train foundation LLMs.
- Copilot applies content blocking, protected-material detection, and prompt-injection blocking.
- EU traffic stays in the EU Data Boundary for LLM processing. Anthropic subprocessors are excluded from EUDB. Advanced Data Residency and Multi-Geo include Copilot as of 1 March 2024.
- Sensitivity labels and IRM usage rights are honored. Semantic indexing stays inside the user’s access boundary.
- Enterprise Data Protection applies to Copilot Chat (Basic), Microsoft 365 Copilot (Basic), and Premium when users sign in with Entra. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
- The Copilot security dashboard in the Microsoft 365 admin center (Copilot > Overview > Security) covers DLP, oversharing, and compliance. Global Reader can view; AI Administrator can change. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/security-microsoft-365-copilot
- Microsoft Security Dashboard for AI (preview) at https://ai.security.microsoft.com aggregates Defender, Entra, and Purview signals across Copilot, Copilot Studio agents, Foundry, and third-party AI. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/security-microsoft-365-copilot
- SharePoint Advanced Management and restricted content discovery are included with Copilot licenses to reduce oversharing into Copilot results. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview

### Models

Primary source: https://learn.microsoft.com/en-us/microsoft-365/copilot/ai-models-overview

- Microsoft Online Services can use Microsoft-hosted models (under Microsoft DPA and Product Terms), AI subprocessors (third parties under Microsoft DPA), or independent processors (third-party terms; admin-enabled).
- Microsoft documents Anthropic, OpenAI, SpaceXAI, and Mistral as model options or subprocessors in the Copilot admin toc. Admins assign provider access to users and groups.
- Word, Excel, and PowerPoint Agents require Anthropic as a subprocessor. Anthropic models are excluded from EUDB and, where applicable, in-country processing. Source: https://learn.microsoft.com/en-us/microsoft-365/copilot/wordexcelppt-agents

## Sources

- https://learn.microsoft.com/en-us/microsoft-365/copilot/
- https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
- https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-licensing
- https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-app-overview
- https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-app-admin-settings
- https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-architecture
- https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy
- https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search
- https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-controls/overview
- https://learn.microsoft.com/en-us/microsoft-365/copilot/security-microsoft-365-copilot
- https://learn.microsoft.com/en-us/microsoft-365/copilot/ai-models-overview
- https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/
- https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/use-cowork
- https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance
- https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-overview
- https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder
- https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/
- https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/overview
- https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-agent-store
- https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-agent-install
- https://learn.microsoft.com/en-us/microsoft-365/copilot/wordexcelppt-agents
- https://learn.microsoft.com/en-us/microsoft-365/copilot/researcher-agent
- https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-personalization-memory
- https://learn.microsoft.com/en-us/microsoft-365/copilot/organizational-prompts
- https://learn.microsoft.com/en-us/microsoft-365/copilot/scheduled-prompts
- https://learn.microsoft.com/en-us/microsoft-365/copilot/people-skills-overview
- https://learn.microsoft.com/en-us/microsoft-365/copilot/pay-as-you-go/overview
- https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-overview-copilot-credits
- https://learn.microsoft.com/en-us/office365/servicedescriptions/office-365-platform-service-description/microsoft-365-copilot
- https://learn.microsoft.com/en-us/sharepoint/copilot-in-sharepoint-get-started
- https://support.microsoft.com/en-us/office/welcome-to-copilot-in-word-2135e85f-a467-463b-b2f0-c51a46d625d1
- https://support.microsoft.com/en-us/excel/copilot/get-started-with-copilot-in-excel
- https://support.microsoft.com/en-us/microsoft-365-copilot/how-copilot-chat-works-in-microsoft-365-apps
- https://support.microsoft.com/en-us/powerpoint/copilot/create-a-new-presentation-with-copilot-in-powerpoint
- https://support.microsoft.com/en-us/topic/the-copilot-dynamic-action-button-in-word-excel-and-powerpoint-40db4cef-3d59-474d-9dec-f649b5bfab8e
- https://support.microsoft.com/en-us/Outlook/frequently-asked-questions-about-copilot-in-outlook
- https://support.microsoft.com/en-us/teams/platform/frequently-asked-questions-about-copilot-in-microsoft-teams
- https://support.microsoft.com/en-us/microsoft-365-copilot/what-are-microsoft-365-copilot-notebooks-in-onenote
- https://support.microsoft.com/en-US/SharePoint/copilot-in-sharepoint/get-started-with-agents-in-sharepoint
- https://www.microsoft.com/microsoft-365-copilot
