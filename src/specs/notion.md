---
name: Notion AI
slug: notion
url: https://www.notion.com/product/ai
docs: https://www.notion.com/help
kind: product
reviewed: 2026-09-28
---

# Notion AI

## Product

Notion AI is Notion's built-in AI product inside a Notion workspace. It lives in the same pages, databases, and sidebar as the rest of Notion. People use it to search, write, transcribe meetings, and run agents on workspace content and connected apps.

Notion documents Notion AI on Business and Enterprise plans. Free and Plus workspaces get a limited number of complimentary AI responses. Custom Agents, Notion credits, Notion AI Connectors (except the personal Gmail connector), Research Mode, image generation, MCP connections, and Workers require Business or Enterprise. Notion Agent, AI Meeting Notes, and Enterprise Search are included on those plans. Custom Agents and premium models spend Notion credits.

The product runs in the Notion web app, the desktop app, and the mobile apps. Custom Agents are built and used on desktop or web. Notion Agent can connect MCP servers on web and desktop, not on mobile. Calendar event create and cancel from Notion Agent is web and desktop only. AI Meeting Notes works in the desktop app, browser, and mobile app, with different audio capture limits on each.

Someone opens Notion Agent from the face in the bottom corner, from `Notion AI` in the sidebar, or with a keyboard shortcut. They chat, attach files, pick sources, and switch models. For recurring team work they open `Agents` in the sidebar and create a Custom Agent with instructions, triggers, access, and a model. Workspace owners manage connectors, models, credits, web search, meeting notes, and who can create agents in `Settings` → `Notion AI`.

This dossier is Notion AI. There are no sibling specs in this repository. Notion Calendar and Notion Mail are separate Notion products that agents can connect to. The Developer Platform (Workers, Admin API, Notion MCP) is documented where it powers or governs this product. Claude, Cursor, and ChatGPT are other vendors' products; Notion documents Claude agents and Cursor agents as External Agents inside Notion, and Notion MCP as a way those apps can read and write Notion content.

## Features

### Notion Agent

Primary source: https://www.notion.com/help/notion-agent

- Notion Agent is an on-demand AI teammate inside Notion. It creates and edits pages and databases using the current page, the workspace, and connected apps.
- It has the same permissions as the person using it. If that person cannot view or edit content, the agent cannot either.
- Open it from the face at the bottom of Notion. The chat can suggest actions based on the current page, such as generating action items or making content more concise.
- By default it uses the page you are on. Selected blocks become the focus. `@` adds a page or person. `All sources` limits which workspace, connector, and MCP sources it uses.
- Attach a file with the paperclip. Upload PDF, CSV, Excel/XLSX, Word/DOCX, PowerPoint/PPTX, or ZIP. The agent can answer questions about the file or turn it into pages or databases.
- Switch models from `Auto`. Documented models include Claude Fable 5.1 (Business and Enterprise only), Claude Sonnet 5, the newest GPT models, Gemini, and Grok. Some models look only at the web and not the workspace. Premium models spend Notion credits and stay off until an admin turns them on in `Settings` → `Notion AI`.
- It can search the workspace and connected apps, query databases and properties, read comments, and search version history.
- After you connect your Slack account, it can look up people, search channels you are in (including private channels and DMs), read recent messages, open shared files, post messages, reply in threads, edit messages it posted, and add or remove reactions. Posts appear as you. Source: https://www.notion.com/help/notion-ai-connectors-for-slack
- Connect MCP servers so the agent can look up information and take actions in those apps from chat.
- It can create and edit pages; create and edit database views including maps and forms; and create or edit properties including relations. It cannot create database automations, database templates, database page layouts, or advanced properties such as formulas, rollups, or buttons.
- Results that are tabular appear as an interactive table in the chat.
- It can use a secure workspace to calculate, run simple code, and create downloadable spreadsheets, slide decks, PDFs, or documents.
- It can read, group, and archive Inbox notifications, and it can be opened from the Agent icon in the inbox panel.
- After you connect Gmail in `Settings` → `Notion AI` → `AI connectors`, it can search mail, draft and send emails, archive or trash messages, manage labels, and unsubscribe. Write actions ask for confirmation before they run.
- After you connect Calendar in the same settings, it can find time with teammates, show ranked suggestions on an interactive grid, prep for meetings, reshuffle the schedule, time-block tasks, and create or edit external scheduling links. It cannot edit or cancel an event if you are not the organizer. Scheduling and canceling events is not available on mobile.
- Personalize the agent with a name, accessories, and an instructions page (an existing page, a template, or a new private `My Notion AI` page). Instructions can set tone, notes about your role, and pages or channels to look at first. You can tell the agent to update those instructions while you work.
- Chat mode can be `Sidebar` or `Floating`. Pin a chat to keep it at the top of the Chat tab (not on mobile). Open chat history from the clock icon next to `Notion AI` in the sidebar.
- Thumbs up and thumbs down send feedback to Notion. The help article says this feedback is not used to train the agent.
- The help article lists things Notion Agent cannot do: answer from a non-PDF embed such as a video transcript; create or edit comments; share pages or change permission levels; start AI Meeting Notes; create reminders; manage workspace settings such as member roles, billing, or security; or connect new MCP servers on mobile.

### Skills

Primary source: https://www.notion.com/help/create-and-manage-skills

- Skills are reusable instructions written as Notion pages. Mark a page as a skill and run it with Notion Agent, or let the agent pick it when it fits.
- Built-in skills in the text selection menu include Improve Writing, Proofread, Explain, and Reformat. Custom skills can replace or supplement those.
- Create a skill from `Library` → `Skills` → `New skill`, from `Settings` → `Notion AI` → `Skills`, from `•••` → `Use as a skill` on a page, or by asking Notion Agent to mark a page as a skill.
- Run a skill by highlighting text, hovering a block and choosing `Skills`, typing `/skill` next to content, or typing `/` plus the skill name in Notion Agent chat.
- Automatic use is on by default for skills that live in a skills database and have a description. Turn off `Use automatically` to require an explicit call.
- A skills database makes every new page a skill and adds a `Description` property that Notion Agent reads. You can create a Skills database or turn an existing database into one.
- Share a skill like any other page. People with access can run it. People who can edit the page change the skill for everyone. Shared skills appear in Library `Discover`; select `Enable for me` to add them to your menu.
- Download a skill to a local agent such as Claude Code, Codex, Cursor, Gemini, or Grok as a `SKILL.md` file plus approved attachments. When the Notion skill changes, the download is badged.
- A Custom Agent can use a skill if you add the skill page under `Tools and access`.

### Custom Agents

Primary source: https://www.notion.com/help/custom-agents

- Custom Agents are shared workflows that run in the background on triggers and schedules. Unlike Notion Agent, they do not wait for each prompt.
- After setup they can read granted Notion pages and databases and certain connected apps; run on recurring triggers and workspace events; take actions such as posting reports, filing bugs, updating records, or sending messages; and hand part of a job to other Custom Agents they are allowed to call.
- They require the Business or Enterprise plan. Build, edit, view, or interact on desktop or web.
- Create from the `Agents` sidebar `+` control: create with AI chat, create from a template, or create a blank agent. Review generated instructions, triggers, and access, then save.
- Combine trigger types on one agent. Filters can limit runs to pages, messages, property values, keywords, or a database view.
- Recurring triggers support every day, week, month, or year, with a time and timezone. The settings show the next scheduled run.
- Notion triggers include a comment on a page, a page added to a database, a property updated, a page removed from a database, and a finished AI Meeting Note.
- Slack triggers can watch a message posted, an emoji reaction, or a mention of the Custom Agent in public or private channels. An admin must connect Slack first. Mentions require Slack user groups to be allowed. Thread replies and keyword filters are optional. Saved or Later Slack messages are not supported. A Slack typing indicator (“Working on it…”) can be turned off.
- Access is explicit. An agent does not get the whole workspace by default. Grant specific pages and databases, or `Pages shared with everyone in Notion`. Linking a page in instructions does not add it to Tools and access.
- Web access is a toggle. On lets the agent retrieve information from the internet. Off keeps it on Notion and configured apps.
- A primary agent can call other Custom Agents you add under Tools and access. Instructions say which jobs to hand off and what to return. Sub-agent work spends Notion credits.
- Models include Claude Fable 5 (Business and Enterprise only), Claude Sonnet 5, the newest GPT models, Gemini, and Grok. Auto is the documented default. Admins limit models under `Settings` → `Notion AI` → `General` → `Allowed models for Custom Agents`. Claude Fable 5 stays off until an admin turns it on because Anthropic may store prompts and responses for that model.
- Share an agent like a page. Permission levels are `Full Access`, `Can Edit`, and `Can View and Interact`. Users without access may still trigger an agent that responds to Slack events in a channel they can see.
- Embed a Custom Agent by pasting its link and choosing `Embed`. Embedding does not grant access. The agent cannot read the host page unless that page is in Tools and access.
- Each agent page has `Chat`, `Activity`, and `Settings`. Activity (Full Access) logs the trigger, actions, and errors. Version history can restore a past configuration.
- Duplicate copies name, model, instructions, and accessible pages, databases, and triggers. Tool connections, Workers, run history, and credit limits do not carry over. The duplicate is private by default.
- Full Access users can export Insights chats as CSV (up to 300 chats for a selected period) on Business and Enterprise.

### Custom Agent connections

Primary source: https://www.notion.com/help/mcp-connections-for-custom-agents

- Slack is a native integration. After an admin connects the Slack AI connector, a Custom Agent can read selected public and private channels, post to selected channels, and react to threads. Source: https://www.notion.com/help/custom-agents
- Mail connections work with Gmail, Notion Mail, or Outlook and do not require Notion Mail. The agent can search, archive, star or flag, trash, manage labels, unsubscribe, block senders, draft, send, and manage filters. Notion Mail adds status, reminders, and saving emails as synced blocks. Source: https://www.notion.com/help/connect-mail-to-custom-agents
- Mail triggers include new email received, new email sent, received or sent, and label applied. Filters can match From, To, Subject, Body, or Domain. Permissions are Modify inbox, Draft, Send, and Require confirmation. Sharing the agent lets anyone with access view emails in the connected inbox. Source: https://www.notion.com/help/connect-mail-to-custom-agents
- Calendar connections work with Notion Calendar, Google Calendar, Apple Calendar, and Microsoft Outlook / M365. The agent can read, create, update, cancel, invite, find time, add or remove attendees, and RSVP. Outlook can add a Teams link, see shared calendars, work with recurring meetings, and book a room (some Outlook features are documented as rolling out). Source: https://www.notion.com/help/connect-calendar-to-custom-agents
- Calendar triggers include event created, event updated, and event cancelled, with filters on title, description, location, owner, or all-day status. Permissions are Read, Read and write, Require confirmation, and a default calendar. Source: https://www.notion.com/help/connect-calendar-to-custom-agents
- MCP connections are Business and Enterprise only. They work with scheduled, Notion, Slack, and manual runs. They have read and write access but no trigger capability. Native integrations such as Slack can trigger. Source: https://www.notion.com/help/mcp-connections-for-custom-agents
- Pre-configured MCP servers listed in help are Amplitude, Attio, Box, ClickHouse, Figma, GitHub, HubSpot, Intercom, Linear, Mercury, Miro, Mixpanel, n8n, Ramp, Stripe, Sentry, and Wiz. Custom servers use a public URL after an admin enables custom MCP and sets install policy (`Approved & recommended` or `Approved only`). Source: https://www.notion.com/help/mcp-connections-for-custom-agents
- Each MCP connection is unique to one agent and uses the authenticator's credentials. Write tools default to Always ask. Options are Run automatically, Always ask, and Always allow. Only the person who authenticated can change that connection's tool settings. Source: https://www.notion.com/help/mcp-connections-for-custom-agents
- Notion Agent MCP connections are separate. Connecting an MCP server for Notion Agent does not give Custom Agents that connection. Source: https://www.notion.com/help/connect-mcp-servers-to-your-notion-agent

### Custom Agent sharing and admin

Primary source: https://www.notion.com/help/custom-agents-sharing-and-permissions

- Custom Agents act as specialized team members with their own permissions. Notion Agent acts as you. Sharing an agent gives users the agent's access, including content they cannot open directly.
- Grant pages and databases at Can view, Can comment, or Can edit. You can also add an agent from a page's `Share` menu. There is no inherited access from the creator or the user. Database row permissions follow the agent's access.
- `Can view and interact` can run the agent and read settings. `Can edit` can change instructions and Notion access (not third-party connections others enabled) and view all chats. `Full access` can share and delete the agent.
- Guests and restricted members can see agent output on shared pages and can trigger configured agents by editing those pages. They cannot create agents or ask the agent questions unless given edit permission.
- The Agent Directory lives at `Settings` → `Notion AI` → `Agents`. Admins can search agents, see creators and last activity, and disable editing, chatting, and triggers. Enterprise admins can change permissions and delete any agent.
- Creation policy can be all members (default), workspace owners only, or owners plus added groups. Enterprise admins set this under `Settings` → `Notion AI` → `Agents` → `Control who can create agents`. Source: https://www.notion.com/help/custom-agents
- Content search can filter pages shared with a Custom Agent. A page or database owner can remove an agent from `Share` without access to the agent itself.
- Enterprise audit log records Custom Agent actions and can filter by agent. Instruction updates, permission changes, and integration additions are recorded. Source: https://www.notion.com/help/custom-agents
- `Settings` → `Analytics` → `AI` shows most-used and unused agents.
- After a member leaves, private agents appear in content re-provisioning after 7 days without an owner the agent stops. Ownership transfer is also supported via the Public API.
- Enterprise org admins can use the Admin API with an org-owned admin token to list agents, update sharing, track and limit credits, set creation policy, pause all agents, turn an agent off or on, and delete an agent (setup is kept for recovery). Source: https://www.notion.com/help/manage-custom-agents-with-the-admin-api

### Autofill and databases

Primary source: https://www.notion.com/help/autofill

- Notion AI can create a database from a page (`Build with AI`) or from Home `Build` mode. Creating a database this way is included on Business and Enterprise. The help article says this flow cannot edit existing databases and cannot create pages, automations, forms, charts, or page templates.
- Basic Autofill fills a property from the content of that row or page (summaries, key info, translation, tagging). It is included on Business and Enterprise and does not use Notion credits. It does not browse the web or other pages. Runs can be manual, on page create, or on page edits.
- Custom Agent Autofill can use workspace search, web search (when enabled), conditional logic, and multi-property updates. It spends Notion credits. Runs can be manual, on page create, on page edits, or on a schedule.
- Notion Agent can write or edit formulas in databases and automations. Source: https://www.notion.com/help/notion-ai-faqs

### Enterprise Search

Primary source: https://www.notion.com/help/enterprise-search

- Enterprise Search is a Notion AI feature on Business and Enterprise. Open `Home` and enter a question in the search window. Answers cite sources.
- It searches the workspace, apps connected through Notion AI Connectors, and the web. `All sources` can turn off web search or apps, or limit the search to one source, page, or teamspace.
- You can add context with `Add context` or `@`-mention pages, teamspaces, and people. The article says it can look at database views, relations, and properties.
- Switch models from `Auto` among OpenAI GPT, Anthropic Claude, and Google Gemini. Some models look only at the web.

### Notion AI Connectors

Primary source: https://www.notion.com/help/notion-ai-connectors

- Connectors let questions pull information from third-party apps with citations. Third-party connectors require Business or Enterprise. The Gmail AI Connector (personal) is free on all plans.
- Documented apps are Slack and Microsoft Teams (chat); Google Drive and Microsoft SharePoint & OneDrive (knowledge); Jira (beta), GitHub, and Linear (projects); Gmail, Microsoft Outlook, and Google Calendar (email and calendars).
- Search connected apps from Notion Agent chat, `Notion AI` in the sidebar, and `Search` in the sidebar. For some apps, Notion Agent can take action, not only search.
- Workspace owners with admin rights in the other app set up connectors under `Settings` → `Notion AI`. Initial ingest can take up to 36 hours. New content can take up to 3 hours to index. Access generally goes back one year from setup.
- Permissions follow the mapping between the connected app and Notion. Embeddings of third-party content are stored in a Turbopuffer vector database. Disconnecting makes content unsearchable (up to one hour for some connectors) and deletes the data within a day.
- The connector stays if the installing workspace owner leaves, except Google Drive, which Notion reassigns to another owner with the right permissions.

### Research Mode

Primary source: https://www.notion.com/help/research-mode

- Research Mode is on Business and Enterprise. Open `Home`, select `Research` at the bottom of the search window, and enter a query. The FAQs also describe toggling Research Mode from `Notion AI` in the sidebar. Source: https://www.notion.com/help/notion-ai-faqs
- It searches the workspace, connected apps, uploaded files such as PDFs, and the web. `All sources` can turn off web search or limit sources. Documented connector examples include Slack, Google Drive, Microsoft Teams, Jira, Zendesk, Asana, and GitHub.
- It can find pages in databases, query a page that is part of a database, and filter or sort by properties.
- A run can take up to 10 minutes. You can copy the report or `Save as page`. The article says Notion AI generates answers using LLMs such as GPT-5 and Claude.

### AI Meeting Notes

Primary source: https://www.notion.com/help/ai-meeting-notes

- AI Meeting Notes is in beta. It transcribes a meeting and produces a summary with key points and action items. It requires Business or Enterprise (or an eligible mobile subscription that includes Notion AI). Daily cap is 10 hours per user. Source: https://www.notion.com/help/category/notion-ai
- Desktop app version 4.7.0 or later is required. Mac needs macOS 13 or later. The desktop app can capture system audio and microphone. The browser captures microphone only and does not capture conferencing audio through headphones. Mobile records the phone microphone and is documented for in-person meetings.
- Start with `/meet`, from the `Upcoming events` tile in Home, or from the `Meetings` sidebar after Calendar is connected. Start transcribing confirms consent. At least one minute of audio (about 300 transcribed characters) is required for a summary.
- Upload AAC, M4A, MP3, or WAV into a Meeting Notes block. MOV, MP4, and Loom uploads are not supported.
- Desktop can add speaker labels, best for virtual one-on-ones with system audio. Speaker labeling is English only. Summaries include transcript citations. Source: https://www.notion.com/help/category/notion-ai
- Summary instructions can be Auto, a built-in meeting type, or a custom instructions page. Custom instructions are private by default. You can set a default instruction.
- Consent options include copyable text, a spoken message, and workspace-enforced auto-play (`Settings` → `Notion AI` → `AI Meeting Notes`).
- Notes are private by default. `Auto-share with internal calendar event participants` shares notes created from a Notion calendar event with workspace members on the event. Set a default meetings database under `Settings` → `Notion AI`.
- Workspace owners can turn the feature off with `Workspace availability` and can enable `Store audio locally`. Audio for a block is stored on the recorder's device. Source: https://www.notion.com/help/category/notion-ai
- Languages listed for AI Meeting Notes are English, Chinese, Spanish, French, German, Japanese, Korean, Portuguese, Russian, Thai, Vietnamese, Danish, Finnish, Norwegian, Dutch, and Swedish. Offline use is not supported. Source: https://www.notion.com/help/category/notion-ai
- A finished AI Meeting Note can trigger a Custom Agent. Source: https://www.notion.com/help/custom-agents
- Notion Agent cannot start AI Meeting Notes. Source: https://www.notion.com/help/notion-agent

### Inline AI, AI blocks, and translation

Primary source: https://www.notion.com/help/notion-ai-faqs

- Highlight text or press space on a page to edit with Notion AI: summarize, translate, fix grammar, change length or tone, draft an outline, email, or table, or brainstorm. Accept, discard, or try again.
- Type `/AI Block` to generate a custom output, a page summary, or key points. Set specified context and search sources, then `Generate`. The same block can regenerate later.
- Translate a page from `•••` → `Translate`, or ask Notion Agent to translate the page.
- The default keyboard shortcut is `shift` + `cmd/ctrl` + `J`, including when you are not in Notion. Change it in `Settings` → `Preferences`.
- On iOS you can open Notion AI from Siri, Spotlight, the Shortcuts app, or (iPhone 15 Pro) the Action button.

### Image generation

Primary source: https://www.notion.com/help/create-and-edit-images-with-notion-ai

- Image generation is on Business and Enterprise. Workspace owners and admins can turn it off. Custom Agents cannot generate images.
- Generate a new image in an image block, edit an existing image, or ask Notion Agent to make or edit an image using the current page.
- The FAQs label image generation as beta and list per-user limits of 10 generations or edits per 24 hours and 30 per 30 days while in beta. Source: https://www.notion.com/help/notion-ai-faqs
- Image generation is covered by the Notion AI usage allowance for in-product billing. Account-team workspaces use the rolling 10/24-hour and 30/30-day limits.

### Workers

Primary source: https://www.notion.com/help/run-custom-code-with-workers

- Workers are in beta on the Developer Platform. They run custom code on Notion's infrastructure for database sync, tools for Custom Agents, and webhook triggers. They are available on Business and Enterprise.
- Workspace owners can keep creation to owners, allow specific members or groups, or turn Workers off. Developer Mode lists Workers and shows Overview, Logs, Environment Variables, and Settings. Deploy and code changes use the Notion CLI or a coding tool.
- Database sync keeps an external source (examples: Zendesk, Salesforce, an internal tool) in a Notion database under normal sharing permissions.
- Agent tools extend Custom Agents beyond built-in actions and MCP (examples: query a warehouse, generate assets, act in an app without MCP).
- Webhook triggers start a Notion or connected-system workflow from an external event.
- By default only the creator can modify a Worker or add it as a connection. Share it so teammates can attach it to a Custom Agent. Duplicating a Custom Agent does not copy Workers. Source: https://www.notion.com/help/custom-agents
- Workers use Notion credits, not the Notion Agent usage allowance. Source: https://www.notion.com/help/manage-your-usage-allowance-for-notion-ai

### External Agents

Primary source: https://www.notion.com/help/use-claude-agents-in-notion

- Claude agents in Notion are in beta on Business and Enterprise. They are hosted by Notion on Anthropic infrastructure. No Anthropic account is used. They spend Notion credits per run, priced like Custom Agents.
- Create from `Agents` → `New Agent` → `Claude`, from a template (some connect to GitHub with a personal access token) or from scratch with instructions, triggers, and connections.
- They can chat, work from shared docs and task boards, and create or update content if they have edit access. They cannot browse the web or call other agents in a session.
- Permissions match Custom Agents and are set per agent. Enterprise, HIPAA, and model-restricted workspaces leave Claude agents off until a workspace owner turns them on in `Settings` → `Notion AI` → `Agents` → `Manage external agents`.
- Notion zero data retention does not apply. The article says Claude agents use Claude Managed Agents, which are stateful and not eligible for zero data retention.
- Cursor agents in Notion are in beta on Business and Enterprise for people who have a Cursor account and user API keys. They run on Cursor's infrastructure, desktop only, and are billed by Cursor, not Notion credits. Source: https://www.notion.com/help/connect-cursor-to-notion
- Create a Cursor agent from `Agents` → `New Agent` → `Cursor`, enter a Cursor API key, and set instructions, triggers, and connections. Cursor can find workspace information, create and update pages, and answer questions about work. Admins can turn Cursor agents off under Manage external agents. Source: https://www.notion.com/help/connect-cursor-to-notion
- Notion MCP lets MCP-client apps such as Claude, Cursor, and ChatGPT Pro read and write Notion content from those apps. That is the inverse of Claude or Cursor agents inside Notion. Enterprise admins can restrict AI apps to an approved list under `Settings` → `Connections` → `Permissions`. Source: https://www.notion.com/help/notion-mcp

### Notion credits and usage allowance

Primary source: https://www.notion.com/help/buy-and-track-notion-credits-for-custom-agents

- Custom Agents spend shared workspace Notion credits on each run. Usage rises with more reading, more steps, more frequent runs, and advanced models. Auto is the documented default for matching a model to the task.
- Help estimates cost per run for example workflows (Q&A, task routing, status update, mail triage, daily brief) and states 1,000 credits cost $10. Actual usage is shown after each run.
- If credits run out, Custom Agents and premium models pause until credits reset or an admin adds more. Admins get in-app and email notices at 80% and 100% usage.
- Credits are a Business and Enterprise add-on. They cannot be bought on an App Store or Google Play subscription. Downgrading to Free or Plus switches Custom Agents off without deleting them.
- Mid-period credit increases apply immediately; decreases apply at the next service period. There is no documented cap on how many credits a workspace can buy.
- Basic Autofill does not use credits. Custom Agent Autofill does.
- The credits dashboard is at `Settings` → `Access & billing` → `Notion credits`. Admins see workspace usage. Creators see workspace pacing and their own agents. Source: https://www.notion.com/help/track-usage-in-the-notion-credits-dashboard
- Business and Enterprise include a usage allowance for some features, measured in a six-hour window and a monthly window. It applies to personal Notion Agent (including chat), image generation, and page translation. It does not apply to Custom Agents or Workers. AI Meeting Notes has its own 10-hour daily cap. Source: https://www.notion.com/help/manage-your-usage-allowance-for-notion-ai
- When the allowance is reached, those features pause until the window refreshes, or workspace owners can let the team keep going with Notion credits. Source: https://www.notion.com/help/manage-your-usage-allowance-for-notion-ai
- The product page states Custom Agents are priced under the credit system at $10 per 1,000 credits after the free trial period. Source: https://www.notion.com/product/ai

### Security and privacy

Primary source: https://www.notion.com/help/notion-ai-security-practices

- Notion AI honors existing permissions. Models cannot use content the user cannot access.
- Workspace content is embedded with an OpenAI zero-retention embeddings API and stored in a Turbopuffer vector database (SOC 2 Type 2). Embeddings are treated as Customer Data. They are deleted within 60 days after a page or workspace is deleted.
- Customer Data sent to subprocessors is encrypted in transit with TLS 1.2 or greater. Notion and its AI subprocessors do not use Customer Data to train models by default. Input and output are Customer Data; Notion does not claim ownership.
- Enterprise workspaces use zero data retention at LLM providers by default. Non-Enterprise providers retain Customer Data for 30 days or fewer. Features that need data-retaining LLMs stay off until an admin turns them on. External Agents have different retention.
- Notion AI is in Notion's SOC 2 Type 2 and ISO 27001 scope. HIPAA for Enterprise uses zero-retention LLM APIs. The product page also lists GDPR, CCPA, and encryption in transit. Source: https://www.notion.com/product/ai
- Workspace owners can enable or disable web search and require confirmation before web requests. Business and Enterprise owners can allow members to spend credits past the usage allowance.
- Enterprise customers can trigger DLP alerts on AI prompts and generated content through third-party integration partners.
- Notion AI Supplementary Terms and the Content & Use Policy apply to AI input and output.
- Enterprise Search security documents OAuth 2.0 for Microsoft, Atlassian, and Slack; TLS 1.2 or greater; zero-retention connector API calls; permission checks at query time; and permission updates within about one hour. Source: https://www.notion.com/help/enterprise-search-security-and-privacy-practices
- Enterprise data retention settings apply to deleted AI chats as well as pages (default 30 days, customizable from one day to 10 years). AI chats skip Trash. Source: https://www.notion.com/help/custom-data-retention-settings
- Workspace owners can opt in to share workspace data to improve Notion AI, set model controls, set per-member credit limits, and configure AI Meeting Notes, connectors, and personalization under `Settings` → `Notion AI`. Source: https://www.notion.com/help/notion-ai-faqs

## Sources

- https://www.notion.com/help
- https://www.notion.com/help/notion-ai-faqs
- https://www.notion.com/help/notion-agent
- https://www.notion.com/help/create-and-manage-skills
- https://www.notion.com/help/custom-agents
- https://www.notion.com/help/custom-agents-sharing-and-permissions
- https://www.notion.com/help/mcp-connections-for-custom-agents
- https://www.notion.com/help/connect-mail-to-custom-agents
- https://www.notion.com/help/connect-calendar-to-custom-agents
- https://www.notion.com/help/connect-mcp-servers-to-your-notion-agent
- https://www.notion.com/help/manage-custom-agents-with-the-admin-api
- https://www.notion.com/help/autofill
- https://www.notion.com/help/enterprise-search
- https://www.notion.com/help/notion-ai-connectors
- https://www.notion.com/help/notion-ai-connectors-for-slack
- https://www.notion.com/help/research-mode
- https://www.notion.com/help/ai-meeting-notes
- https://www.notion.com/help/category/notion-ai
- https://www.notion.com/help/create-and-edit-images-with-notion-ai
- https://www.notion.com/help/run-custom-code-with-workers
- https://www.notion.com/help/use-claude-agents-in-notion
- https://www.notion.com/help/connect-cursor-to-notion
- https://www.notion.com/help/notion-mcp
- https://www.notion.com/help/buy-and-track-notion-credits-for-custom-agents
- https://www.notion.com/help/track-usage-in-the-notion-credits-dashboard
- https://www.notion.com/help/manage-your-usage-allowance-for-notion-ai
- https://www.notion.com/help/notion-ai-security-practices
- https://www.notion.com/help/enterprise-search-security-and-privacy-practices
- https://www.notion.com/help/custom-data-retention-settings
- https://www.notion.com/product/ai
