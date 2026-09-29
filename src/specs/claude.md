---
name: Claude
slug: claude
url: https://claude.ai/
docs: https://support.claude.com/en/
kind: product
reviewed: 2026-09-28
---

# Claude

## Product

Claude is Anthropic's conversational assistant. A person signs in at [claude.ai](https://claude.ai/), in Claude Desktop, or in the Claude iOS or Android app, types a prompt, and continues a thread. Claude is also the model family Anthropic sells; this dossier is the chat product people use, not a model card.

Access is limited to supported locations. Users must be at least 18 years old. Sign-in is email or Google. The model in use appears below the input on web and desktop, or at the top of the screen on mobile. A person can switch models, set effort, and turn thinking on or off from that control. The `+` button or `/` opens extra options and commands.

Plans are Free, Pro, Max 5x, Max 20x, Team, and Enterprise. Free usage is session-based and resets every five hours. Paid individual plans add usage, priority access, and other product surfaces on the same subscription. Team and Enterprise add organization administration, identity controls, and shared projects. Team describes itself as a paid plan for the Claude chat experience. Enterprise seats include Claude on web, desktop, and mobile, plus Claude Code and Cowork; usage on usage-based Enterprise is billed at API rates on top of the seat fee.

Claude Code and Claude Cowork are separate products. Code is specified in `claude-code`. Cowork is specified in `claude-cowork`. The desktop app has a Code tab and a Cowork surface. Anthropic is rolling out a merged chat and Cowork experience on Pro and Max, on web, desktop, and mobile, in which a person does not pick a mode first. Until an account has that experience, the message box still shows Chat and Cowork as separate options. This file covers the chat assistant. Cowork-only local computer use, local folders, scheduled Cowork tasks, and the Cowork built-in browser stay in `claude-cowork`. Source: https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude

The Help Center is the documentation host for the product. Developer API and Console docs live on a separate host and are out of scope here.

## Features

### Chat

Primary source: https://support.claude.com/en/articles/8114491-get-started-with-claude

- Claude is available on the web at claude.ai, in Claude Desktop for Mac or Windows, and in Claude for iOS or Android.
- A person types a prompt into the chat interface and submits it to start or continue a conversation.
- The `+` button in the lower left or `/` opens additional options and commands.
- The current model is shown below the text input on web and desktop, or at the top of the screen on mobile. Clicking it opens the model selector.
- Claude is trained extensively in English and works in many other common languages. A language can be selected in settings.
- Conversation history cannot be imported from another AI provider. Free, Pro, and Max users can import memory from other providers.

### Claude Desktop

Primary source: https://support.claude.com/en/articles/10065433-install-claude-desktop

- Claude Desktop runs on macOS 11 or higher, Windows 10 or higher, and Linux (beta) on Ubuntu 22.04 LTS+ or Debian 12+, x64 or arm64.
- Chat is available on Free, Pro, Max, Team, and Enterprise. Claude Code and Claude Cowork are listed as desktop features on paid plans.
- Downloads are at the Claude downloads page. Linux can install from Anthropic's apt repository so updates arrive with system package updates.
- Desktop extensions install from Settings > Extensions. They connect Claude to local apps and data, including filesystem access, with code signing and encrypted storage for secrets.
- Desktop extensions run locally and are available in Claude Desktop and Claude Code, not on web or mobile.
- Linux desktop currently does not include computer use or dictation. Quick Entry works on X11; on native Wayland it uses the desktop's GlobalShortcuts portal.

### Claude Mobile apps

Primary source: https://support.claude.com/en/articles/11139144-use-claude-for-education-at-your-university

- Claude for iOS requires iOS 18.0 or later. Claude for Android requires Android 8.0 Oreo or later.
- Conversations sync across web, desktop, and mobile on the same account.
- Mobile apps include photo analysis and voice dictation.
- File creation is supported on iOS and Android. Tapping Download opens the file in a system preview or another app. Source: https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude
- On mobile, a person can ask for a design, deck, or doc in any chat and view it in the Artifacts tab. Starting from a template, editing, or changing sharing settings requires web or desktop. Source: https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them

### Claude in Chrome

Primary source: https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome

- Claude in Chrome is a Google Chrome extension for paid plans (Pro, Max, Team, Enterprise). It is not supported on other Chromium browsers or mobile.
- It is available in Claude Cowork and Claude Code, and in beta in the Chrome side panel. Claude can read, click, type, navigate, and fill forms on websites.
- On Max and Team, the side panel runs as a Claude Cowork session. That rollout is reaching Pro. On Enterprise it becomes a Cowork session after an admin enables Cowork in the cloud; until then it uses the classic side panel.
- A Cowork side-panel session is saved to history, can be continued on web, desktop, or mobile, and uses the same skills, plugins, and connectors as Cowork on desktop.
- The side panel starts in Automatically approve mode. A person can switch back to the classic side panel. Recorded workflows exist only in the classic side panel.
- From Claude Desktop, Claude in Chrome can be added as a connector and enabled per conversation so a chat can drive Chrome.
- Team and Enterprise admins can enable or disable the extension and restrict sites with allowlists and blocklists.
- Scheduled recurring browser tasks, multi-tab groups, shortcuts, 1Password sign-in (beta on macOS), and console-log reading are documented for the extension.

### Conversations

Primary source: https://support.claude.com/en/articles/10593882-share-and-unshare-chats

- Chats are private by default. Share creates a snapshot link of messages sent before sharing, including artifacts. Later messages stay private until the chat is unshared and shared again.
- Attached files and raw MCP tool-call data are not included in a shared snapshot.
- Team and Enterprise users can share chats only with members of the same organization, not publicly.
- Free, Pro, and Max users manage shared chats from Settings > Privacy.
- Incognito chats are available on all plans outside projects. They are not saved to chat history or memory, are not used for training, and are not included in monthly recap. Source: https://support.claude.com/en/articles/12260368-use-incognito-chats
- On Team and Enterprise, incognito chats still appear in owner data exports and, on Enterprise, in the Compliance API. They are retained at least 30 days, or longer under a custom retention policy.
- In the merged Claude experience, incognito chats open in the previous chat experience, so Claude cannot create files or run code in them.

### Projects

Primary source: https://support.claude.com/en/articles/9517075-what-are-projects

- Projects are self-contained workspaces with their own chat histories and knowledge bases. They are available on all plans. Free users can create at most five projects.
- A person uploads documents, text, code, or other files to the project knowledge base. Claude uses that material as context for chats in the project.
- Each project can have project instructions that apply to every chat in that project. Context is not shared across chats unless it is in the knowledge base.
- On Pro, Max, Team, and Enterprise, projects switch to RAG when knowledge approaches context limits, expanding capacity by up to 10x.
- Team and Enterprise projects can be shared with view or edit permission, to specific people, in bulk, or organization-wide. Owners can disable public or shared projects.
- A new projects version is in beta, starting with Claude Code for select Pro and Max users at claude.ai/code and in the desktop Code tab. Existing chat and Cowork projects keep working as they do today.

### Artifacts

Primary source: https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them

- An artifact is a design, deck, document, dashboard, or small interactive tool that opens beside the conversation. A person can edit it, return to it, and share it.
- Artifacts are available on Free, Pro, Max, Team, and Enterprise. They require Cloud code execution and file creation in Settings > Capabilities (or Organization settings > Capabilities on Team and Enterprise).
- Templates (Claude Design, Claude Slides, and Claude Docs) are in beta on paid plans. They are on by default on Pro, Max, and Team, and off on Enterprise until an owner turns each one on.
- Web and desktop can create, edit, and share artifacts and start from a template. Mobile can ask for a design, deck, or doc and view it in the Artifacts tab.
- Claude Slides builds presentations from notes, reports, or chat work. A person can edit slides, present in Claude, and export to PowerPoint or PDF.
- Legacy artifacts made before 16 September 2026 still work and can be published, but new legacy artifacts cannot be created.
- Artifacts that call Claude run on Anthropic's infrastructure. People using them sign in with their own Claude account. Usage counts against each person's plan.
- On Pro, Max, Team, and Enterprise, artifacts on web and desktop can connect to apps the person has connected, after approval, and can store up to 20 MB of text per artifact in personal or shared storage.

### Claude Docs

Primary source: https://support.claude.com/en/articles/16923645-get-started-with-claude-docs

- Claude Docs is in beta on Pro, Max, Team, and Enterprise. It is on by default on Pro, Max, and Team, and off on Enterprise until an owner turns it on in Organization settings > Artifacts.
- It is not available yet for organizations that use CMEK, zero data retention, or a HIPAA-ready configuration.
- A doc is a rich-text document in the person's Claude account. It can have headings, tables, formatting, and multiple tabs. Docs are saved in the Artifacts tab.
- Claude can draw on files, memory, projects, skills, and connected apps when drafting. A person can start with `/docs` or Output > Docs.
- People with edit access can edit the same doc at the same time. Claude acts with the permissions of the person who asked.
- Export formats are Word, PDF, Markdown, and Google Docs. A doc can be turned into a presentation with Claude Slides.
- On Team and Enterprise, docs cannot be shared outside the organization. Opening a shared doc requires a Claude account.

### Claude Design

Primary source: https://support.claude.com/en/articles/14604416-get-started-with-claude-design

- Claude Design is in beta on Pro, Max, Team, and Enterprise. It is on by default on Pro, Max, and Team, and off on Enterprise until an owner turns it on. A standalone experience remains at claude.ai/design.
- A person asks for a design in a conversation, picks a Design template in the Artifacts tab, or uses Output > Design. Claude generates a working design on a canvas beside the chat.
- A person can refine through chat, inline comments, or direct canvas edits (drag, resize, align).
- Export options include .zip, PDF, PPTX, standalone HTML, and send-to-tool destinations listed on the page. Google Slides export is available only at claude.ai/design.
- Designs can use an organization design system. Design-system sync and handoff to Claude Code are documented as a path into `claude-code`.
- Design activity counts toward the same usage pool as the rest of Claude, including Claude Code.

### Files and code execution

Primary source: https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude

- Code execution and file creation is available on all plans on web, desktop, and mobile. Claude runs code in a private sandboxed environment on claude.ai.
- Claude can create Excel (.xlsx), PowerPoint (.pptx), Word (.docx), and PDF files. Files can be downloaded or saved to Google Drive. Maximum size is 30 MB per file for uploads and downloads.
- Claude can write and run Python or JavaScript, create PNG visualizations, process CSV and TSV files, and build analyses from uploaded data.
- Free, Pro, and Max enable the capability in Settings > Capabilities. Team and Enterprise owners control it in Organization settings > Capabilities, including network egress (off, package managers only, allowlisted domains, or all domains except Anthropic's legal blocklist).
- Chat uploads accept PDF, DOCX, CSV, TXT, HTML, ODT, RTF, EPUB, JSON, and XLSX (XLSX needs code execution). Images: JPEG, PNG, GIF, WebP. Chat limits include 500 MB per file and 20 files per chat. Source: https://support.claude.com/en/articles/8241126-upload-files-to-claude
- PDFs of 100 pages or fewer are analyzed as text and visuals. PDFs of 101–1000 pages are text only. Source: https://support.claude.com/en/articles/8241126-upload-files-to-claude
- With code execution enabled, Claude summarizes earlier messages when a conversation approaches the context window so the thread can continue. Source: https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work

### Web search

Primary source: https://support.claude.com/en/articles/10684626-enable-and-use-web-search

- Web search is documented for Opus 5.5, Fable 5.1, Opus 5, Sonnet 5, Fable 5, Opus 4.8, Opus 4.7, Sonnet 4.6, Opus 4.6, and Haiku 4.5.
- On Team and Enterprise, an Owner or Primary Owner must enable web search in Organization settings > Capabilities before members can use it.
- In the classic experience, a person turns web search on from `+` > Web search. In the new Claude experience there is no toggle; Claude searches when it helps.
- Responses include citations and source links. With search on, web fetch can retrieve the full content of a URL the person provides.
- Image results from Bing can appear in the conversation with source links. Interactive search content is documented separately under visual content.
- Web search and web fetch count toward usage limits. Claude may use a location inferred from IP for localized results.

### Research

Primary source: https://support.claude.com/en/articles/11088861-use-research-on-claude

- Research is available on Pro, Max, Team, and Enterprise on web, desktop, and mobile. Web search must be on.
- A person enables it from `+` > Research. Claude runs multiple searches that build on each other across the web and connected internal sources such as Gmail, Google Calendar, and Google Docs.
- Research uses the same usage limits as ordinary chats and typically consumes them faster.

### Custom visuals

Primary source: https://support.claude.com/en/articles/13979539-custom-visuals-in-chat-and-cowork

- Custom visuals are in beta for all Claude users on web and desktop, in chat and Cowork. They do not render on iOS or Android.
- Claude does not generate photos or illustrations. It builds diagrams, charts, and interactive visuals with HTML and SVG. Source: https://support.claude.com/en/articles/9002504-can-claude-produce-images
- Visuals appear inline. A person can interact with them, ask follow-ups, copy as an image, download as .svg or .html, or save as an artifact.
- Shared-chat visuals render for the recipient on web and desktop only, and the recipient must be logged in.

### Memory

Primary source: https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context

- Past-chat search is available on Pro, Max, Team, and Enterprise on web, desktop, and mobile. Claude searches with RAG and shows the search as a tool call. It can search all chats outside projects, or chats inside one project.
- Search can be turned off in Settings > Memory. It is unavailable if the organization uses customer-managed encryption keys, because conversation content is encrypted.
- Memory is on by default for Free, Pro, and Max. On Team and Enterprise it is off until an owner enables it. Memory is not available to organizations with HIPAA, public-sector, or custom data retention agreements.
- Claude saves memory as topics while chatting. Each project has its own memory and project summary. A person can view, edit, or delete topics in Settings > Memory.
- Memory is shared between chat and Cowork when Cowork runs in the cloud. Local Cowork sessions do not use memory.
- Sensitive topics are off by default. Some information is never saved, including government ID numbers, criminal history, financial account numbers, and immigration status.
- Memory import and export is available for Free, Pro, Max, and Team on web and desktop. Source: https://support.claude.com/en/articles/12123587-import-and-export-your-memory-from-claude

### Skills

Primary source: https://support.claude.com/en/articles/12512176-what-are-skills

- Skills are folders of instructions, scripts, and resources that Claude loads when a task matches. They require code execution. They are available on Free, Pro, Max, Team, and Enterprise.
- Anthropic skills (for example Excel, Word, PowerPoint, and PDF creation) are available to all users and are invoked automatically when relevant.
- People and organizations can create custom skills in Markdown and can attach scripts. Partner skills in the Skills Directory are built to work with matching MCP connectors.
- Team and Enterprise owners can provision skills for all members, enabled or disabled by default. Enterprise can turn on skill and plugin scanning.
- Skills are discovered under Customize > Skills and Browse skills.

### Plugins

Primary source: https://support.claude.com/en/articles/13837440-use-plugins-in-claude

- Plugins are available on Pro, Max, Team, and Enterprise. Each plugin bundles skills, connectors, and sub-agents.
- A person can add and use plugins in chat on the web, in the Chat tab of Claude Desktop, and in Cowork. Skills and commands from a plugin work in chat. Hooks and sub-agents run in Cowork and Claude Code, not in chat.
- Plugins added on web or desktop are saved to the account and sync to Claude Code when the person signs in with the same Claude account (Claude Code v2.1.273 or later).
- Anthropic ships marketplaces such as Knowledge Work (default), Life Sciences, Financial Services, and Legal. A marketplace can also be added from a GitHub, GitLab, or Bitbucket repository.
- Team and Enterprise owners can turn on skill and plugin sharing, publishing to an organization library, default or required plugins, and Enterprise group assignment.
- Salesforce in Claude is a beta plugin on paid plans for organizations Salesforce approves. It works in chat and Cowork, bundles 37 sales skills plus Salesforce and Slack connectors, and asks the person to approve writes. Source: https://support.claude.com/en/articles/16952186-use-salesforce-in-claude

### Connectors

Primary source: https://support.claude.com/en/articles/11176164-use-claude-cowork

- Connectors let Claude access apps and services, retrieve data, and take actions within the person's permissions in the source system.
- Web connectors are available on Claude, Cowork, Claude Desktop, and Claude Mobile. Desktop extensions are available on Claude Desktop.
- Directory connectors are browsed from `+` > Connectors or Customize > Connectors. Some connectors render live interfaces in the conversation and show an Interactive badge.
- Custom remote MCP connectors are available on Free, Pro, Max, Team, and Enterprise on Claude, Cowork, and Claude Desktop. Free is limited to one custom connector. Custom servers are reached from Anthropic's cloud and must be on the public internet.
- Team and Enterprise owners enable connectors for the organization. Each person still authenticates unless Enterprise-managed auth (beta) authorizes the connector once for the organization.
- Owners can set tool categories or individual tools to Always allow, Needs approval, or Blocked. Restrictions never grant more access than the source system.
- Remote connectors work across web, mobile, Cowork, Desktop, and Claude Code. Desktop extensions are for local tools and OS-level access. Source: https://support.claude.com/en/articles/11725091-when-to-use-desktop-and-web-connectors
- Connector data transfers are encrypted. Third-party services process data on their own infrastructure. Chats with synced content cannot be shared. On Team and Enterprise, connectors are only available in private projects.

### Personalization and settings

Primary source: https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features

- Instructions for Claude are account-wide preferences applied to every conversation. They live in Settings.
- Project instructions apply only to chats inside one project.
- The model menu next to send sets the model, effort (Low, Medium, High, Extra high / xhigh, Max), and thinking. Effort is available on Opus 5.5, Fable 5.1, Opus 5, Sonnet 5, Fable 5, Opus 4.7, Opus 4.6, and Sonnet 4.6. Source: https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings
- Thinking shows an expandable section above the response. It cannot be turned off for Opus 5.5, Fable 5.1, or Opus 5 in Claude.
- Enterprise admins can hide models or effort levels for a role and can set a default model and effort for new chats.

### Plans and usage

Primary source: https://support.claude.com/en/articles/8325606-what-is-the-pro-plan

- Free access is available at claude.ai in supported locations. Free usage resets every five hours and varies with demand. Source: https://support.claude.com/en/articles/8114491-get-started-with-claude
- Pro is $20 per month (US), with annual billing available. It includes more usage than Free, priority access, early features, Claude Code access, and longer multi-step tasks. It does not include Claude API usage through the Console.
- Max 5x is $100 per month and Max 20x is $200 per month (web prices). Max includes 5x or 20x Pro per-session usage, a weekly limit across models, priority access to new models and features, and Claude Code. Source: https://support.claude.com/en/articles/11049741-what-is-the-max-plan
- Usage limits apply across claude.ai, Claude Code, and Claude Desktop. They depend on conversation length, features, model, and effort. Source: https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work
- On paid plans, the newest models support up to a 1M token context window; others support 500K or 200K. A portion of the window is reserved for the response.
- Pro, Max, Team, and seat-based Enterprise can buy usage credits after included limits. Usage-based Enterprise has no included token allowance and bills consumption at API rates.

### Team and Enterprise

Primary source: https://support.claude.com/en/articles/9266767-what-is-the-team-plan

- Team requires at least two members and supports up to 150 seats. Standard seats are $25 per member per month monthly, or $20 billed annually (US). Premium seats are $125 monthly or $100 annually (US).
- Team Standard seats include 1.25x Pro per-session usage. Premium seats include 6.25x. Limits are per member. Team includes SSO, domain capture, JIT, role-based permissions, spend controls, enterprise search, workplace connectors, projects, a 200k context window, Claude Code, and Cowork.
- Enterprise search is a dedicated search project provisioned for all members, with instructions for searching Slack, Microsoft 365, and custom connectors.
- Enterprise includes Team features plus audit logs, SCIM, custom data retention, Compliance API, Analytics API, customer-managed encryption keys, US-only inference, usage-based pricing, and HIPAA-ready configuration with a BAA for eligible organizations. Source: https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan
- Usage-based Enterprise seats are billed annually. The seat covers Claude on web, desktop, and mobile, plus Claude Code and Cowork. Usage is billed at API rates. Admins can set organization and user spend limits.
- Self-serve Enterprise has a 20-seat minimum at claude.ai/create/enterprise. Sales-assisted Enterprise has a 50-seat minimum. Enterprise is also available through AWS Marketplace.
- Some existing Enterprise orgs still have Chat vs Chat + Claude Code seats, or Standard vs Premium seats, until the next contract renewal.

### Claude for Education

Primary source: https://support.claude.com/en/articles/11139144-use-claude-for-education-at-your-university

- A university-sponsored Claude for Education account includes an enhanced context window, current models, projects, higher usage than individual plans, priority access, and file uploads.
- Students sign in at claude.ai with a university email, or use Desktop or mobile with the same account. SSO is managed by the university's Owner or Primary Owner.
- The university Primary Owner manages the account and data. Data exports, audit log, and thumbs feedback are off by default until the Primary Owner requests them from Anthropic. Source: https://support.claude.com/en/articles/11732894-who-owns-and-manages-the-data-of-my-claude-for-education-account
- Claude for Teachers is a free Team-like plan for verified educators, with a DPA, no training on chats and files, and several Team admin features turned off. A district-managed setup places teachers in a Claude Enterprise organization with SSO and admin controls. Source: https://support.claude.com/en/articles/15926041-claude-for-teachers-your-data-and-our-terms

### Claude Science

Primary source: https://support.claude.com/en/articles/16563838-get-started-with-claude-science

- Claude Science is a separate desktop app for scientific research, in beta on Pro, Max, Team, and Enterprise. Team and Enterprise owners turn it on in Organization settings > Claude Science.
- It runs on macOS 13 or later and Linux x64. Claude writes and runs code in a sandbox, reads folders the person grants, uses scientific-database connectors, can connect to compute clusters, and saves versioned artifacts with provenance.
- Installation, admin controls, and the changelog are documented on a separate Claude Science docs page linked from this article.

### Claude Security

Primary source: https://support.claude.com/en/articles/14661296-use-claude-security

- Claude Security is in public beta on Enterprise. An owner enables it in Organization settings > Claude Security.
- It scans GitHub.com or GitHub Enterprise Server repositories, verifies findings, and opens suggested patches in Claude Code on the web. The product lives at claude.ai/security.
- Scans run on Claude Mythos 5. Users see findings without direct model access. Scans are billed at token cost with no extra platform fee.
- Findings can be copied, downloaded as CSV or Markdown, or sent through per-project webhooks.

## Sources

- https://support.claude.com/en/
- https://support.claude.com/en/articles/8114491-get-started-with-claude
- https://support.claude.com/en/articles/10065433-install-claude-desktop
- https://support.claude.com/en/articles/11139144-use-claude-for-education-at-your-university
- https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude
- https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them
- https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome
- https://support.claude.com/en/articles/10593882-share-and-unshare-chats
- https://support.claude.com/en/articles/12260368-use-incognito-chats
- https://support.claude.com/en/articles/9517075-what-are-projects
- https://support.claude.com/en/articles/16923645-get-started-with-claude-docs
- https://support.claude.com/en/articles/14604416-get-started-with-claude-design
- https://support.claude.com/en/articles/8241126-upload-files-to-claude
- https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work
- https://support.claude.com/en/articles/10684626-enable-and-use-web-search
- https://support.claude.com/en/articles/11088861-use-research-on-claude
- https://support.claude.com/en/articles/13979539-custom-visuals-in-chat-and-cowork
- https://support.claude.com/en/articles/9002504-can-claude-produce-images
- https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context
- https://support.claude.com/en/articles/12123587-import-and-export-your-memory-from-claude
- https://support.claude.com/en/articles/12512176-what-are-skills
- https://support.claude.com/en/articles/13837440-use-plugins-in-claude
- https://support.claude.com/en/articles/16952186-use-salesforce-in-claude
- https://support.claude.com/en/articles/11176164-use-claude-cowork
- https://support.claude.com/en/articles/11725091-when-to-use-desktop-and-web-connectors
- https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features
- https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings
- https://support.claude.com/en/articles/8325606-what-is-the-pro-plan
- https://support.claude.com/en/articles/11049741-what-is-the-max-plan
- https://support.claude.com/en/articles/9266767-what-is-the-team-plan
- https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan
- https://support.claude.com/en/articles/11732894-who-owns-and-manages-the-data-of-my-claude-for-education-account
- https://support.claude.com/en/articles/15926041-claude-for-teachers-your-data-and-our-terms
- https://support.claude.com/en/articles/16563838-get-started-with-claude-science
- https://support.claude.com/en/articles/14661296-use-claude-security
- https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude
- https://claude.ai/
- https://claude.ai/design
- https://claude.ai/security
- https://claude.ai/create/enterprise
