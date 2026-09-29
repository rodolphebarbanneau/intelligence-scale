---
name: Grok
slug: grok
url: https://grok.com/
docs: https://docs.x.ai/grok/overview
kind: product
reviewed: 2026-09-28
---

# Grok

## Product

Grok is xAI's assistant. It runs on the web at grok.com and in the iOS and Android apps. Sign in once and conversations, settings, and subscription stay in sync across those platforms.

A person opens a thread, asks a question, and continues in the same conversation. The docs describe chat, Grok Imagine for images and video, hands-free voice, file upload for analysis and summarization, and connectors that reach email, files, and calendar from inside a chat. The product page also lists live web and X search, step-by-step reasoning, code in the thread, memory across chats, custom instructions, a writing canvas, and shareable threads.

Grok is free to start. Paid SuperGrok plans raise limits and unlock more across Grok products from one weekly usage allowance. The pricing page lists Free, SuperGrok Lite, SuperGrok, SuperGrok Plus, SuperGrok Heavy, Business, and Enterprise. SuperGrok is $30 per month. SuperGrok Plus is $100 per month and adds higher usage, 1080p video, and priority access. Grok Business is $30 per month for teams, with workspaces, licenses, and sharing controls in the xAI console. Grok Enterprise adds organization-level SSO, SCIM, and further security controls through sales.

This file is the Grok assistant only. Grok Bot (`grok-bot`) is a separate product: durable AI teammates on a persistent cloud computer. Grok Build (`grok-build`) is the coding agent; the FAQ says Grok Studio is no longer supported and to use Grok Build instead. xAI also sells a developer API and offers Grok on the X platform, which X operates under X's terms.

## Features

### Welcome to Grok

Primary source: https://docs.x.ai/grok/overview

- Grok is xAI's assistant on grok.com and in the iOS and Android apps.
- Sign in once and conversations, settings, and subscription stay in sync across every platform.
- Chat is a back-and-forth for questions, brainstorming, writing, and working through problems.
- Grok Imagine creates images and video.
- Voice talks to Grok hands-free.
- File uploads cover PDFs, images, spreadsheets, code, audio, and more for analysis, extraction, and summarization.
- Connectors let Grok reach email, files, and calendar inside a chat.
- Grok is free to start. Paid SuperGrok plans raise limits and unlock more across every product from a single weekly usage allowance.

### Chat, search, and reasoning

Primary source: https://x.ai/grok

- The product page describes Grok as chat, search, reason, and create in one place.
- Answers can show reasoning step by step.
- The same thread can generate images, video, and code.
- Voice conversations are described as natural back-and-forth with low latency.
- Multi-agent mode runs several agents in parallel on sub-problems and merges one cited answer. Each agent's reasoning is visible.
- Search uses the live web and X, with citations from primary sources.
- Follow-up questions continue the topic in the same thread.
- Code generation writes, debugs, and explains code in the thread.
- Memory across chats remembers preferences and past conversations.
- Canvas is long-form editing with inline suggestions.
- Custom instructions tailor responses to style and needs.
- Conversations can be shared with a public link.
- The page lists 30+ languages for speaking and writing.
- Vision analyzes screenshots, photos, and diagrams.
- Sign-in uses an X or email account.
- SuperGrok is listed for higher limits, priority access, and multi-agent.

### Image & Video Generation

Primary source: https://docs.x.ai/grok/faq

- Grok Imagine generates images and video from text prompts or reference photos, and can restyle, edit, and iterate in the conversation. Source: https://x.ai/grok
- The product page states image generation up to 2K resolution and text-to-video up to 15 seconds. Source: https://x.ai/grok
- The product page also lists video generation up to 15 seconds at 720p. Source: https://x.ai/grok
- SuperGrok Plus lists 1080p video creation. Source: https://x.ai/pricing
- Generated images and videos include a Grok watermark. There is no setting to remove it. Removing, altering, or obscuring the watermark or other provenance signals is prohibited under the Acceptable Use Policy.
- 720p videos fall back to 480p once the 720p cap for the tier is reached.

### Files & Data

Primary source: https://docs.x.ai/grok/faq

- Upload files in chats on web, iOS, and Android from the + control next to the message input, or drag-and-drop on the web.
- Multiple files can attach to one message. Web allows up to about 100 files. Android allows up to 20. iOS supports multiple files.
- Document and data types include PDF, DOCX, TXT, CSV, XLSX, PPTX, HTML, XML, JSON, Markdown, LaTeX, ODT, RTF, and code files such as `.py`, `.cpp`, `.java`, `.html`, and `.css`.
- Image types include JPEG, JPG, PNG, WebP, HEIC, and BMP. GIF and SVG support varies by platform.
- Audio types include MP3, WAV, M4A, OGG, FLAC, and AAC. Video types include MP4 and MOV.
- Most files can be up to 150 MB each. Limits can vary by platform or subscription.
- Grok extracts and processes content from uploads: text from documents, visual reasoning from images and PDFs, and related analysis. Very long files may be summarized or handled in sections.
- Documented file work includes synthesis across files, transformation and summarization, extraction of tables and quotes, analysis of images and charts, code debugging, audio and video transcription, and multimodal reasoning across text, images, and code.
- Embedded images inside non-PDF files may not be processed visually. Some audio and video files upload but have variable transcription quality.
- On the web, grok.com/files deletes content and frees space. Profile → Settings → Data Controls has further data controls.
- Deleted chats and files are removed within standard retention windows unless retained longer for legal, compliance, or safety purposes.

### Connectors

Primary source: https://docs.x.ai/grok/connectors

- Connectors are available to all Grok users and let Grok access external tools and data sources inside a conversation.
- On Grok Business and Enterprise, a team admin must provision a connector in the cloud console before members can use it.
- There are three kinds: built-in connectors, a catalog of pre-configured OAuth connectors, and custom MCP connectors.
- Built-in connectors are maintained by xAI, authenticate with OAuth, and need no setup beyond the initial sign-in.
- Built-in connectors listed in the docs are Gmail & Google Calendar, Google Drive, OneDrive, Outlook Mail & Calendar, Microsoft Teams, SharePoint, and Salesforce.
- Add a built-in connector at grok.com/connectors with New Connector, then complete OAuth. Grok requests only the permissions it needs.
- After connect, Grok can use the connector's tools automatically when a question relates to that service.
- The catalog of additional OAuth connectors is at grok.com/connectors.
- A custom MCP connector can expose an internal API, database, or SaaS tool, with custom tool schemas and authentication on the operator's infrastructure.
- Add a custom MCP connector at grok.com/connectors with New Connector → Custom, then enter the MCP server URL and complete authentication.
- Grok discovers tools the MCP server exposes and makes them available in conversations.
- The MCP server must be reachable on the public internet. Local servers need a tunnel.

### Google Drive

Primary source: https://docs.x.ai/grok/connectors/google-drive

- Search files by content or title across Docs, Sheets, Slides, and other Drive types.
- Read file contents in the conversation to summarize or analyze them.
- Create and write files, including new Google Docs.
- Create folders, list folder contents, and trash files.
- Upload artifacts Grok generates to any folder in Drive.
- Filter by starred files, shared files, files modified after a date, or files in a specific folder.
- OAuth scopes include Drive metadata, read, optional write (`drive`), and `userinfo.email`. Grok can only access files the signed-in Google account can access.
- Connect at grok.com/connectors by selecting Google Drive and signing in with Google.
- xAI does not use Google Drive data for model training. The docs say Drive content is accessed in real time and is not stored on xAI servers afterward.
- Disconnect at grok.com/connectors, or revoke the app at myaccount.google.com/permissions.

### Gmail & Google Calendar

Primary source: https://docs.x.ai/grok/connectors/gmail-google-calendar

- Gmail and Google Calendar are separate connectors, each with its own OAuth sign-in and permissions.
- Gmail can search with Gmail operators, read full messages including attachments, compose and manage drafts, send, reply, and forward when write permissions are enabled, and organize mail with labels, trash, and delete.
- Gmail starts read-only. Write, send, and label tools are enabled progressively by organization administrators.
- Google Calendar can search events, view attendees, location, and description, check free/busy availability, create, update, and delete events when write is enabled, RSVP, and list accessible calendars.
- Connect each at grok.com/connectors by selecting Gmail or Google Calendar and signing in with Google.
- xAI does not use Gmail or Calendar data for model training. The docs say that data is accessed in real time and is not stored on xAI servers afterward.
- Disconnect at grok.com/connectors, or revoke the app at myaccount.google.com/permissions.

### Outlook Mail & Calendar

Primary source: https://docs.x.ai/grok/connectors/outlook

- Outlook Mail and Outlook Calendar are separate connectors, each with its own OAuth sign-in and permissions.
- Outlook Mail can search the mailbox, read messages including attachments, compose drafts with To, Cc, Bcc, and HTML, send, reply-all, and forward, move mail between folders, create folders, run batch operations, and attach Grok-generated artifacts to a draft.
- Outlook Calendar can search events, view attendees, location, and body, check availability across attendees, create and update events with recurrence and reminders, and RSVP with optional comments.
- Mail uses delegated `Mail.ReadWrite` and `Mail.Send`. Calendar uses delegated `Calendars.ReadWrite`. Grok can only access the signed-in user's mailbox and calendar.
- Connect at grok.com/connectors by selecting Outlook or Outlook Calendar and signing in with a Microsoft work or school account.
- Some organizations require an Azure AD admin to grant consent for the xAI Grok application before users can sign in.
- xAI does not use Outlook data for model training. The docs say that data is accessed in real time and is not stored on xAI servers afterward.
- Disconnect at grok.com/connectors, or revoke the app at myapps.microsoft.com.

### SharePoint

Primary source: https://docs.x.ai/grok/connectors/sharepoint

- SharePoint is available on Grok Business and Enterprise plans only.
- Grok can search documents, read files from document libraries, browse folders and drives, and, if write access is enabled, upload generated artifacts to a SharePoint drive.
- A team admin must add the connector in the console, choose delegated `Sites.Read.All` or application-level `Sites.Selected` access, enter the Azure AD tenant ID, and complete Microsoft 365 admin consent.
- Application-level mode uses a site allow list. Delegated mode is bounded by the connecting account's SharePoint access.
- Optional write access uses a separate Entra application and `Files.ReadWrite.All`, and is not on by default for team members even after the admin approves it.
- A background sync indexes SharePoint content. Every search or file request is access-checked against the querying user's Microsoft permissions.
- Team members connect their own Microsoft work or school account at grok.com/connectors after admin setup.
- xAI does not use SharePoint data for model training. Disconnecting a user deletes indexed data only they could access. Removing the connector deletes all indexed data for the organization.

### OneDrive

Primary source: https://docs.x.ai/grok/connectors/onedrive

- OneDrive is available on Grok Business and Enterprise plans only.
- Grok can browse files and folders in the signed-in user's personal OneDrive and upload generated artifacts there.
- Full-text search across OneDrive for Business files is documented through the SharePoint connector, because those files sit on SharePoint infrastructure.
- A team admin must add the connector, provide the Azure AD tenant ID, and complete Microsoft 365 admin consent.
- Permissions are delegated (`Files.ReadWrite`, `User.Read`, `offline_access`) and scoped to the signed-in user's own OneDrive.
- Team members connect at grok.com/connectors with a Microsoft work or school account.
- xAI does not use OneDrive data for model training. Disconnecting deletes indexed data for that account. Removing the connector deletes indexed data for the organization.

### Microsoft Teams

Primary source: https://docs.x.ai/grok/connectors/microsoft-teams

- Search messages across channels and chats by keyword.
- Read channel messages including threaded replies, reactions, and @mentions, and read one-on-one and group chats.
- Send channel messages, reply to threads, send chat messages, and create new one-on-one or group chats.
- Browse teams and channels, and view team and channel members including roles.
- Permissions are delegated. Grok can only access teams, channels, and chats the signed-in user already belongs to.
- Connect at grok.com/connectors by selecting Microsoft Teams and signing in with a Microsoft work or school account.
- Some organizations require Azure AD admin consent for the xAI Grok application.
- xAI does not use Teams data for model training. The docs say Teams data is accessed in real time and is not stored on xAI servers afterward.
- Disconnect at grok.com/connectors, or revoke the app at myapps.microsoft.com.

### Salesforce

Primary source: https://docs.x.ai/grok/connectors/salesforce

- Explore standard and custom objects in the connected Salesforce org.
- Search across objects, retrieve recently viewed or modified records, and filter, sort, and summarize records across parent-child relationships.
- Create records such as Leads, Opportunities, Accounts, Cases, or custom objects from chat, and update fields on existing records by ID or context.
- Actions follow the connected Salesforce user's profile, role, sharing rules, and field-level security.
- A company admin adds the connector in the xAI console under Grok Enterprise → Connectors and provides OAuth client credentials. Setup also references installing and configuring the Salesforce DX MCP Server (Beta).
- Team members then connect at grok.com/connectors with Salesforce credentials.
- Only one Salesforce org or instance is supported per team.
- xAI does not use Salesforce data for model training. The docs say Grok queries Salesforce in real time and does not copy or store records on xAI servers.

### Custom MCP Tunneling

Primary source: https://docs.x.ai/grok/connectors/custom-mcp-tunneling

- Grok's servers must reach a custom MCP server over the public internet. Localhost and private-network URLs are rejected.
- A tunnel exposes a local MCP server through a public URL. The MCP server code does not need to change.
- The docs show ngrok and Cloudflare Tunnel as example tunnel providers. They are third-party services and are not affiliated with xAI or Grok.
- Cloudflare quick tunnels do not support Server-Sent Events. The docs say to use ngrok for SSE, and that Streamable HTTP works with Cloudflare.
- Free-tier tunnel URLs often change on restart. After a restart, remove the old connector and add a new one with the new URL.
- Grok calls the MCP server on demand during conversations. If the tunnel or local server is stopped, tool calls fail.
- OAuth or API-key authentication still happens in Grok after the tunnel URL is provided.

### Billing & Subscriptions

Primary source: https://docs.x.ai/grok/faq

- Manage a web SuperGrok subscription at grok.com/?_s=billing while logged in: change plan, update payment, or cancel. Settings → Billing on grok.com is the same path.
- Apple App Store subscriptions are canceled and refunded through Apple.
- Google Play subscriptions are canceled in Google Play. Refunds for web and Google Play go through the xAI Refund Request form. Approved refunds typically return to the original payment method in 5–10 business days.
- X Premium refunds, when required by law, are handled by X, not xAI.
- xAI API credits are not refundable.
- Large unexpected invoices are often a SuperGrok Heavy yearly subscription rather than API usage.
- A subscription is tied to the account used at purchase. Web and app access can look missing if the sign-in method differs. X Premium+ access applies to the account linked to X.

### Usage & Limits

Primary source: https://docs.x.ai/grok/faq

- Paid users share one weekly usage pool across Grok products instead of separate daily limits per product. The FAQ dates this change as rolling out in June 2026.
- The pool can be spent on a single product or across products. Different products cost different amounts of the pool. A chat message uses little compute; a high-quality video or a long coding task uses more.
- Settings → Usage on web and mobile shows percent used, a breakdown by product (API, Build, Chat, Imagine, Voice), the weekly reset time, and Extra Usage Credits.
- When the weekly limit is met, paid features pause until reset. Free-tier Chat and Voice limits remain and reset on their own schedule.
- Extra Usage Credits continue paid features after the included weekly allowance. They can currently be purchased only on the web, from as little as $5 on the Usage tab, and expire one year after purchase unless otherwise stated.
- Extra Usage Credits are priced at standard rates, which the FAQ says is a higher cost per action than included weekly usage.
- Auto Top Up adds credits when the balance is low, with a chosen amount and monthly cap.
- The FAQ says upgrading a plan gives more weekly usage at a lower cost per action than repeated Extra Usage Credits.

### Accounts & Login

Primary source: https://docs.x.ai/grok/faq

- Link an X account on grok.com under Settings → Account with Connect your X Account. xAI can then read X subscription status and grant related benefits.
- Sign-in methods are managed at accounts.x.ai.
- A subscription created with Apple Hide My Email is recognized when signing in with Apple, not when using the relay address through Google or email.
- Change or add a sign-in email at accounts.x.ai. Apple subscriptions stay tied to the Apple ID.
- Delete the xAI account from xAI Accounts. If the same account is used for the API, API access is removed. The account can be restored within 30 days by logging in again and confirming restoration.
- Report issues from the product (or reply to a billing receipt). Include account email, platform, browser or OS, invoice number for billing, and a screenshot or conversation share link.
- xAI provides Grok in the X apps but does not operate X. X issues go to X's Help Center.

### Products & Models

Primary source: https://docs.x.ai/grok/faq

- Grok Bot is not the same product as Grok on grok.com or the Grok mobile apps. The FAQ describes Grok Bot as durable AI teammates on a persistent cloud computer.
- Grok Studio is no longer supported. The FAQ says to use Grok Build instead.
- Companions are available on the iOS app only. The FAQ says there are no plans to bring them to the web or Android.
- The documented web address for the app is grok.com in a standard Chrome or Chromium browser. The FAQ says some users on grok.x.ai or other hosts miss features such as Projects.

### Data controls and privacy

Primary source: https://x.ai/legal/faq

- Grok is available as a standalone chatbot on iOS, Android, and grok.com. Grok on X is a separate path under X's terms and privacy policy.
- Users must confirm they are at least 13. Ages 13–17 need parent or guardian permission.
- Conversation history is available in the apps and on grok.com.
- Share a conversation with a public share link from grok.com or the apps. Anyone with the link can open it, and public posts of the link may be indexed.
- Revoke share links at grok.com/share-links.
- Private Chat (ghost icon) hides history from the user and deletes the conversation from xAI systems within 30 days. Private Chat content is not used for model training.
- The consumer FAQ says users own inputs and outputs, including generated images, and may use outputs commercially, subject to xAI's Consumer Terms and brand attribution.
- Logged-in users can opt in or out of model training: Settings → Data Controls → Improve the model on mobile, or Settings → Data → Improve the Model on grok.com.
- The consumer FAQ says xAI does not use business and enterprise customer content to improve models.
- Personalize Grok using X is a toggle under Data Controls on mobile and Settings → Data on grok.com.
- Delete a conversation, all conversations, or the account from history and Settings / Data Controls. Deletion from xAI systems can take up to 30 days.
- The consumer FAQ says xAI does not sell data or share it with third parties for marketing or advertising.
- Data subject requests can go through in-product Data Controls or https://x.ai/privacy-portal/.
- Consumer support email listed on that page is support@x.ai.

### Plans

Primary source: https://x.ai/pricing

- Free is $0 per month and lists real-time web and X search, voice mode, SOC 2 Type I and Type II, and connectors.
- SuperGrok is $30 per month and lists the Grok 4.6 model, Grok Bot access, connectors, higher rate limits, Expert, SOC 2 Type I and Type II, and image and video generation.
- SuperGrok Plus is $100 per month and includes SuperGrok plus 1080p video, higher usage across Chat, Imagine, Voice, and Build, priority access at peak times, and early access to new features. The card also lists lightning-fast replies.
- The comparison table also names SuperGrok Lite, SuperGrok Heavy, Business, and Enterprise.
- The Team tab lists Business at $30 per month with all Grok models including Grok 4.6, Grok Build access, team seat management, consolidated billing, SOC 2 Type I and Type II, role-based access control, domain verification, user analytics, and custom data retention.
- Enterprise is listed as custom. The Team card adds custom SSO, SCIM, custom RBAC, advanced user and access management, dedicated onboarding and support, customer-managed encryption keys, and a dedicated data plane.
- Sales can discuss custom rate limits, dedicated infrastructure, SSO, compliance, data residency, and volume pricing. The page lists sales@x.ai.

### Grok.com User Guide

Primary source: https://docs.x.ai/grok/user-guide

- Grok Business provides personal and team workspaces with privacy and sharing controls under business plan terms.
- A team workspace includes privacy terms, SuperGrok or SuperGrok Heavy benefits depending on the license, and conversation sharing limited to active team members.
- Personal Workspace is for individual use unless the organization disables it. Team Workspace is for the team and requires an active license.
- Switch workspaces with the workspace selector in the bottom-left navigation on grok.com.
- Enterprise licenses can disable personal workspaces. Enabling or disabling that setting goes through xAI sales on an Enterprise plan.
- Team-workspace share links open only for licensed team members. Links sent to people outside the team or without a license do not open.
- Share from a team-workspace conversation with the share button, then select team members and generate a link.
- Shared conversations appear at https://grok.com/history?tab=shared-with-me.
- Activate a license from the Grok Business overview at console.x.ai with Assign license. The team workspace then appears on grok.com.
- The user guide states enterprise-grade privacy protections under xAI's terms, including data handling and, for the Enterprise tier, custom retention policies.

### License & User Management

Primary source: https://docs.x.ai/grok/management

- The Grok Business overview at console.x.ai is the hub for licenses and invitations.
- License types are SuperGrok (standard business access with enhanced quotas and features) and SuperGrok Heavy (upgraded performance for demanding workloads).
- Admins buy licenses from the overview by type and quantity. Purchased licenses go into a pool for assignment.
- Invite users by email from Invite users to Grok Business. An invitation can auto-provision a license on acceptance. Invitees get team workspace access and basic team read permissions for sharing conversations.
- Assign a license from the team list to activate access immediately. Unassign License returns the seat to the pool and removes team-workspace access. Personal workspace remains.
- Cancel unused licenses from the overview. Cancellation may take a few days. Eligible refunds go to the billing method.
- Sharing policy is set in console.x.ai under Sharing & Retention → Product Sharing for conversations, projects, and skills.
- Policy levels are Private, Team, Organization, and Public. Members can share more narrowly than the ceiling, not more broadly.
- Public links apply to conversations only. Projects and skills cap at Organization. Defaults: conversations and projects can be shared organization-wide; skills start at Private.
- Tightening a policy applies immediately to new shares and restricts existing shares that exceed the new ceiling.
- Billing Read-Write is required to purchase or cancel licenses. Team Read-Write is required to invite users or assign and revoke licenses. Admins set these on the overview role settings.

### Connector Management

Primary source: https://docs.x.ai/grok/connector-management

- On Business and Enterprise, a team admin must add a connector in the console before members can connect it.
- Open console.x.ai, select the team, then Grok Business → Connectors.
- Admins can provision catalog connectors or a custom MCP server (Other, then the server URL).
- Some connectors need extra setup, such as admin consent for Microsoft services. Dedicated guides exist for SharePoint, OneDrive, and Salesforce.
- After provisioning, members connect their own accounts at grok.com/connectors.
- Configure adjusts access controls, allowed sites, or other service-specific options. Remove deletes the connector for the team and may delete indexed data.
- Adding and removing connectors requires Team Read-Write permissions.

### Organization Management

Primary source: https://docs.x.ai/grok/organization

- Organizations are exclusive to the Enterprise tier. The dashboard is at console.x.ai/organization and is limited to organization admins.
- An organization groups multiple console teams under one IT control plane.
- Domain association links the organization to an email domain. Users who sign up or log in with that domain are associated automatically.
- Organization admins can see all associated users and teams, including affiliations, access status, and high-level usage metrics.
- The structure supports independent Grok Business or API teams with centralized access controls and auditing.
- SSO setup is self-guided for listed identity providers, including Okta, Azure AD, and Google Workspace, with metadata exchange and attribute mapping.
- After SSO is on, users must log in through SSO. A domain email entered on Log in with email redirects to the IdP. Non-domain emails keep standard login.
- SCIM provisions and deprovisions users from the IdP. Admins create roles with name, slug, and description, order them by priority, and map IdP groups to roles at sso.x.ai.
- Each role maps to console teams, ACLs, and a product license such as Grok Business. A Member role is always last as the default.
- SCIM activation shows a preview first. The docs warn that SCIM can change access and that the organization should be notified before activation.
- After activation, roles are managed on the Provisioning tab: create roles, reorder priority, and update teams, permissions, and licenses.
- Organization, SSO, and Enterprise help is directed to x.ai/grok/business/enquire.

## Sources

- https://docs.x.ai/grok/overview
- https://docs.x.ai/grok/faq
- https://docs.x.ai/grok/connectors
- https://docs.x.ai/grok/connectors/google-drive
- https://docs.x.ai/grok/connectors/gmail-google-calendar
- https://docs.x.ai/grok/connectors/outlook
- https://docs.x.ai/grok/connectors/sharepoint
- https://docs.x.ai/grok/connectors/onedrive
- https://docs.x.ai/grok/connectors/microsoft-teams
- https://docs.x.ai/grok/connectors/salesforce
- https://docs.x.ai/grok/connectors/custom-mcp-tunneling
- https://docs.x.ai/grok/user-guide
- https://docs.x.ai/grok/management
- https://docs.x.ai/grok/connector-management
- https://docs.x.ai/grok/organization
- https://x.ai/legal/faq
- https://x.ai/pricing
- https://x.ai/grok
