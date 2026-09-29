---
name: Grok Bot
slug: grok-bot
url: https://x.ai/bot
docs: https://docs.x.ai/grok-bot/overview
kind: product
reviewed: 2026-09-28
---

# Grok Bot

## Product

Grok Bot is xAI's product for named AI teammates called Bots. In the docs and the app, a Bot is one persistent named agent: it has a name, a job, its own conversation, and working context that develops over time. A person works with a Bot by messaging it. They type, dictate, or start a voice chat, give a task plus context and tool access, and review results, questions, and approval requests in the same conversation. The apps are thin clients for chat, review, and approvals. The work itself runs on a persistent cloud computer in Cursor's cloud, with a browser, filesystem, and terminal. Closing the app, laptop, or phone does not stop a background turn or a routine.

All of one user's Bots share that computer's files, browser sessions, and app logins. The computer belongs to the Cursor user account, not to an individual Bot. Each Bot gets its own screen on the shared computer and can run one computer-use task on that screen at a time. Between users, each person gets a dedicated Firecracker microVM. Cursor manages model selection; there is no model picker in the app.

The desktop app runs on macOS (Apple silicon and Intel), Windows (x64 and Arm64), and Linux (x64 and Arm64 as a `.deb`, `.rpm`, or AppImage). The mobile app runs on iPhone and iPad (iOS or iPadOS 18 or later) and Android 9 or later. Sign-in uses a Cursor account, including organization SSO when the organization requires it. Grok Bot requires cloud data storage, so Cursor Legacy Privacy Mode is not supported.

Access is included with every paid individual Cursor plan and with the Cursor Teams plan, or by linking an individual SuperGrok, SuperGrok Plus, SuperGrok Heavy, or X Premium+ subscription to the Cursor account. Paid access includes weekly usage that resets weekly. Eligible accounts can continue with on-demand usage billed through Cursor. A separate Grok Bot subscription is not required.

Grok Bot is the product chassis. The Grok assistant at grok.com (`grok`) and Grok Build (`grok-build`) are separate products and are out of scope.

## Features

### Grok Bot

Primary source: https://docs.x.ai/grok-bot/overview

- A Bot is a named teammate with a job and context that compounds over time.
- Setup is a message: create a Bot, describe the job, and grant access as the Bot asks. There is no workflow builder.
- Bots use connectors where available and computer use for other apps and websites.
- Bots can run in parallel, message each other, share context in group chats, and pass ownership of a task.
- A person can walk a Bot through a multi-step path once, save it as a skill, and rerun it on a schedule.
- A named Bot keeps memory, files, browser sessions, and preferences across sessions.
- Memory covers stable preferences, role context, and summaries of prior work. Conversations and learned context stay separate per Bot.
- Bots can use many browser-based tools, including services without a connector. A site can still block automation, expire a session, or require a human step; the Bot hands those steps back rather than working around them.

### Get started

Primary source: https://docs.x.ai/grok-bot/get-started

- Eligible access is every paid individual Cursor plan, the Cursor Teams plan, or an individual SuperGrok, SuperGrok Plus, or SuperGrok Heavy subscription linked to the Cursor account.
- Download the desktop app from the Grok Bot downloads page on x.ai/bot. Linux builds are under More downloads.
- On first use, Grok Bot introduces Bots, the shared computer, and routines, then asks which tools the person uses. Those answers shape teammate suggestions and do not connect the tools by themselves.
- Create a first Bot from Meet a future teammate, or choose Create your own and set a short name, one primary job, and a description of how it should work.
- Add more Bots later with New → Create new Bot.
- The composer supports typing, Start voice input (`Cmd/Ctrl+D` on desktop; Start dictation on iPhone and Android), and Start voice chat for a live conversation.
- When a Bot reaches an app that needs authentication, the person opens Agent Computer, takes over, completes the password, passkey, two-factor code, or CAPTCHA, and returns control.
- For supported services, install a plugin from Marketplace in the sidebar and authenticate it in the browser.

### Use cases

Primary source: https://docs.x.ai/grok-bot/use-cases

- Documented starter roles are Sales Outbound, Talent Scout, Paid Media, Expense Manager, Product Performance, Bug Reproduction, Account Health, and Chief of Staff.
- The page tells people to start with read-and-prepare work, review the result, then add approved actions or a routine.
- Each role page section names suggested source systems and a starter prompt that stops at a reviewable draft.

### Grok Bot for Mobile

Primary source: https://docs.x.ai/grok-bot/mobile

- The iPhone and Android apps connect to the same Bots, conversations, routines, connectors, and shared cloud computer as the desktop app.
- Download is from the App Store on iPhone and Google Play on Android.
- New users can complete the first-run tour, choose a first Bot, and wait while the shared computer is set up. Existing users go to their synced Bot list.
- From a conversation, send text, dictate, start a voice chat, play a voice memo, take or attach a photo, choose an image or file, mention another Bot or `@everyone` in a group, reply in a thread, and react to a message.
- Drafts are saved per conversation when the person navigates away.
- On iPhone, the system share sheet can send a photo, file, link, or text into a Grok Bot chat. On Android, the share sheet currently accepts text.
- Email and Slack drafts appear as New Email or New Slack Message cards with Send Email, Send Message, or Discard.
- The + control creates a New Bot or New Group Chat. The person can edit a Bot profile, manage group members, pin or hide a conversation, and delete a Bot.
- Open the computer from a conversation to watch work, take over for a password, two-factor code, or CAPTCHA, inspect the screen, and return control.
- A Bot profile lists routines, next run, instruction, and Run history. Active pauses or resumes a routine. Editing the schedule or instruction and testing a routine currently require the desktop app.
- Home-screen search covers Messages, Bots, Group Chats, Files, Routines, or All.
- Settings cover account, plugins, Bot settings, Auto Review when available, appearance, Language (System follows the device; the list is shorter than desktop), usage or an eligible App Store or Google Play subscription, sign out, and delete account.
- Some advanced desktop controls and teach-by-demonstration workflows are not available on mobile.
- Push delivery is still rolling out. In-app attention states remain available when push is not enabled.

### Create and manage Bots

Primary source: https://docs.x.ai/grok-bot/bots

- Create a Bot with New in the sidebar or `Cmd/Ctrl+N`, then Create new Bot, or type a name and choose Create “name” Bot.
- Edit Profile sets name, label, description, and avatar.
- Existing Bots can suggest or create a focused Bot when a job should have a long-lived owner.
- Pin keeps a Bot at the top of the sidebar. Hide from sidebar removes it from the main list without deleting work. Hiding does not pause the Bot or its routines.
- Duplicate copies the profile, settings, enabled skills, routines, and avatar. It does not copy conversation history, learned memory, or chat attachments.
- Share creates a template link as Public link or Team-only. Enterprise accounts default to Team-only. The recipient previews the template on x.ai and adds a copy. They do not get the sharer's computer, logins, or conversation history.
- A public link shows the Bot's shared configuration, including identity, description, skills, and routines. Adding a shared Bot accepts the third-party bot terms.
- Deleting a Bot removes its active profile, conversation, and routines. Shared computer files and sign-ins may remain. Backend retention follows the applicable Cursor terms.

### Message and collaborate

Primary source: https://docs.x.ai/grok-bot/chat-and-collaboration

- A message can include pasted text, links, and images; local file attachments; dictation; a voice chat; a `/` skill reference; an `@` mention of a Bot, group, routine, or connector; a reply to a specific message; and a reaction.
- The transcript shows tool activity, computer use, created files, questions, approval requests, and voice memos.
- A Bot can reply with a voice memo. Play voice memo, Pause voice memo, and expand the memo to read the transcript.
- Start voice chat begins a live conversation when the composer is empty. After the call ends, the conversation can include a Voice chat card.
- Email and Slack drafts appear as editable cards with Send email or Send message, or Discard.
- A direct message from the person takes priority over background work and can redirect the current turn. A direct “Stop now” message ends work immediately and does not undo completed actions.
- A group chat holds two to six Bots with a shared outcome. Membership can be edited later.
- Write normally to let participating Bots decide who should respond, `@` a Bot to assign a request, mention several Bots, or use `@everyone` for a group-wide update.
- Bot-to-group handoff messages are currently text-only. A Bot should send an image directly to another Bot when that teammate must inspect it.
- A Bot can send an asynchronous message to another Bot. The receiving Bot wakes, handles the request, and can reply later. The handoff is visible in the conversation.
- Reply in a thread for feedback on one result or approval request. Use reactions for acknowledgement; a reaction alone should not carry a safety-critical decision.
- Search or the command palette finds Bots, groups, messages, files, links, and routines. Search availability can vary during rollout.
- Desktop shortcuts include `Cmd/Ctrl+K` for the search palette, `Cmd/Ctrl+Shift+F` to search Bots, `Cmd/Ctrl+N` for a new Bot or chat, `Cmd/Ctrl+D` to dictate, and `Cmd/Ctrl+,` for Settings. Start voice chat has no keybinding.

### Files and results

Primary source: https://docs.x.ai/grok-bot/files-and-results

- Attach files with the attachment control or by dragging into the composer. Images and links can be pasted.
- Supported inputs include images, audio, and video; PDF and plain-text documents; Word, Excel, and PowerPoint; CSV, JSON, YAML, and source-code files; HTML and email files; and Jupyter notebooks.
- The desktop composer accepts up to six attachments at a time. Documents, images, and audio can be up to 25 MB each; videos can be up to 200 MB.
- Large, encrypted, damaged, or unusual files may not be readable.
- Links in messages and results open in the system browser. Hovering a link card shows a preview first.
- Files, images, links, and tool results appear as cards. Open a card to preview supported formats, save the file, open the source link, or continue with feedback.
- Bots can read files other Bots save in `/workspace`.

### Use the computer and apps

Primary source: https://docs.x.ai/grok-bot/computer-and-apps

- Every Bot on the account uses the same persistent cloud computer. Browser cookies, signed-in sessions, files, and command-line credentials are shared.
- Open Agent Computer from a conversation to watch clicks, typing, navigation, and current status. Leaving the preview does not stop cloud work.
- The Bot may ask the person to take over for a password or passkey, two-factor authentication, a CAPTCHA, a payment or identity check, or a site that requires a human.
- For a supported connection that presents a secure secret request, enter the value there. The value is masked and is not added to the conversation.
- Connectors are installed as plugins from Marketplace. Choose Add, complete authentication in the browser if requested, then type `@` to attach the connector or `/` to reference a saved skill.
- Installed connectors are account-wide and are not isolated to one Bot.
- Durable project files belong in the shared workspace at `/workspace`. Temporary directories, manually installed packages, and uncommitted application state are replaceable.
- Recover computer is offered from the unreachable-computer error state. Settings → Updates has Update (keeps files) and Reset (rebuilds from the last saved snapshot).
- The Grok Bot cloud computer is separate from the local Mac or Windows computer. A Bot runs commands on the local computer only when that capability is enabled and approved.

### Skills and routines

Primary source: https://docs.x.ai/grok-bot/skills-routines-and-automations

- A skill is a reusable set of instructions for how to do a task. A routine tells one Bot when to run a workflow, on a schedule or, where supported, after an event.
- A skill captures steps, decision rules, expected output, and safety boundaries. Skills are available across the person's Bots if the Bot has the relevant connector or login.
- Marketplace installs supported connectors and packaged skills. Private skills are one library shared by all of the person's Bots.
- When Teach a task is available, record one browser workflow from the computer view for up to ten minutes. It does not record microphone audio. The Bot creates a draft skill to review and test. The rollout may be gradual.
- Ask the owning Bot to create a routine with a schedule, time zone, input source, expected result, approval boundary, and missing-source behavior.
- Cursor account integrations can start a routine from an event such as a Slack message or a GitHub notification. They are separate from Slack or GitHub plugins and may require their own connection flow.
- Test run performs real work after creating or editing a routine.
- View conversation details → Routines lists a Bot's routines and recent runs. A person can enable or pause a routine, run a test, edit schedule or instructions, inspect history, or delete it.
- A Bot can own up to 50 routines. The app keeps the 20 most recent run records for each routine. Deleting a routine is immediate and has no undo.
- After a long period away, Grok Bot may ask whether to keep routines running and pause them if there is no response.

### Settings and notifications

Primary source: https://docs.x.ai/grok-bot/settings-and-notifications

- Open Settings from the account menu or with `Cmd/Ctrl+,`. Some options appear based on account and rollout.
- The account menu shows About, the installed version, Get Grok Bot for mobile, Switch account, and Add account. Inactive accounts can be removed.
- Appearance is Follow System, Light, or Dark. Language is Follow System or one of more than 20 app languages, including English, Spanish, French, German, Japanese, Korean, Simplified Chinese, and Traditional Chinese.
- Bot settings include Timezone for routine schedules and Execution on Local Computer.
- Auto-review manages personal rules plus any team rules the admin requires. Personal rules save to the account and apply on every desktop the person signs in to. When rules conflict, Ask first wins.
- Route egress through this desktop sends the Grok Bot computer's web traffic through the current desktop. If an Enterprise admin turns off Allow Local Egress, the toggle locks and any active route stops within five minutes.
- Marketplace → Your plugins lists Installed plugins and Private skills. Individual plugin tools can be enabled or disabled. On Teams and Enterprise, team-provided plugins may be required or restricted.
- Usage & Billing shows weekly included usage and on-demand usage for eligible accounts. The account menu can show Weekly usage at a glance.
- Settings → Updates updates the desktop app and, separately, Grok Bot's Computer (Update or Reset).
- View conversation details → Bot settings edits one Bot's name, optional label, description, avatar, and notifications preference.
- Sidebar attention states are Needs attention, Unread activity, and Working or typing status.
- Notifications on a Bot send an operating-system or mobile notification when that Bot finishes or needs input. Group chats do not have the same per-Bot switch. Notifications are normally suppressed while Grok Bot is focused.
- In-app errors appear above the composer under Notifications. Some notices include Copy request ID for support.

### Approvals, security, and privacy

Primary source: https://docs.x.ai/grok-bot/approvals-security-and-privacy

- An approval request shows the proposed operation and its inputs. On desktop, Allow once, Deny, and Always allow (save a matching rule) are available. On iPhone and Android, the Auto-review sheet offers Allow, Deny, and Always allow when a rule is proposed.
- An approval controls the proposed action. It does not reverse work already completed.
- Auto Review evaluates tool calls and computer actions before they run. Ask first rules always stop matching actions. Allow automatically rules proceed only when the automated review does not identify another reason to stop.
- Passwords, passkeys, two-factor codes, CAPTCHAs, and payment confirmations use a computer takeover. Do not send those values in ordinary chat.
- A supported secure secret request masks the entered value, excludes it from the transcript, and does not show it to the model.
- A Bot can show a one-step form in chat so the person can type a login, checkout address, or phone number that the Bot then fills into the page.
- Use hardware security keys under Settings → General → Security Key lets the Bot's browser use a key plugged into the desktop. The setting is on by default on macOS and Windows, is not yet supported on Linux, and asks for approval on every use.
- Execution on Local Computer is Ask every time, Always allow, or Never allow. The default is Ask every time. After computers are registered, the choice moves to Settings → Computer → Computers per computer. A team admin can cap the setting.
- Grok Bot uses Cursor authentication and account data settings. Training opt-out follows the applicable Cursor account and privacy settings.
- Sharing a Bot template is not a security boundary. A public link copies configuration only.
- Cleanup is pause or delete routines, sign out of websites on the computer, uninstall connectors and revoke them in the source service, remove sensitive files from `/workspace`, and hide or delete Bots. Deleting a Bot does not remove shared-computer files or browser sessions.

### Grok Bot for teams and enterprises

Primary source: https://docs.x.ai/grok-bot/teams-and-enterprises

- On Teams, Grok Bot is enabled by default for every member. It stays off for teams on Privacy Mode (Legacy) or a legacy request-based plan. There is no switch to turn it off.
- On Enterprise, an admin enables Grok Bot from the Grok Bot page in the Cursor dashboard and can give access to all members or limit it with Manage Group Access. Turning it off blocks every member without deleting their computers.
- Invite Team on the Grok Bot page emails existing Cursor users a download link, or invites new users to the Cursor team. Teams that manage membership through SCIM see only the existing-users option.
- Each user's work runs in a dedicated Firecracker microVM. A Bot can use only the accounts and plugins the user or team grants.
- Team Rules, Cloud Agent delegation, public template sharing, and the local-execution ceiling are available to team admins on Teams and Enterprise.
- Enterprise-only dashboard controls include the organization-wide enable switch, Network Controls, Team Setup, Allow Local Egress, Action Recording, Enforce Auto-review, Auto-review rules, computer management for organization admins, audit logs, OpenTelemetry Export, the MCP allowlist, and SCIM.
- Cloud Agents on the Grok Bot page allows or blocks Bots delegating coding tasks to Cursor Cloud Agents. The switch is on by default. Delegated work runs on separate computers under existing Cloud Agent controls.
- Public template sharing controls whether members can publish Bot templates outside the team. Enterprise teams start with public sharing off.
- Grok Bot inherits the team's Cursor connector policy. Connectors appear as plugins. Pushing connectors to members as mandatory or default-on is not available. A blocked connector shows as Disabled by team admin.
- Execution on Local Computer on the Grok Bot page caps local work as Always allow, Ask every time, or Never allow. Always allow leaves the choice to each member.
- Team Rules added from the Grok Bot page can apply to Cursor, Grok Bot, or both. Rules applied to Grok Bot are always required.
- Enforce Auto-review (Enterprise, off by default) prevents members from turning Auto-review off. Team Auto-review rules then apply to every member's Bots as locked rows.
- Network Controls (Enterprise) sets Grok Bot Network Access to No Policy (Allow All), Allow All Network Access, Defaults + Team Allowlist, or Team Allowlist Only. Directory groups can carry Group Network Access. Teams without a policy default to allow-all.
- Team Setup (Enterprise) runs admin-managed install-script manifests on every team computer at start and on a periodic refresh.
- Action Recording (Enterprise, off by default) records connector tool calls, shell commands, browser navigations, and computer-use sessions after sanitization. Events do not appear on the Audit Log page. OpenTelemetry Export delivers them tagged `cursor.surface=grok_bot`.
- Audit logs (Enterprise) cover admin, security, and authentication events plus Grok Bot control-plane events such as Bot creation, member access changes, Team Setup manifests, MCP authentication, Slack account links, and routines.
- Admins can enable Grok Bot and manage capabilities, Enforce Auto-review, group access, network policy, team rules, and setup scripts through the Admin API.
- On Enterprise teams where it has rolled out, Conversation Insights on the Analytics dashboard has a Grok Bot source that groups conversations by Type of Work and Level of Automation.
- A separate Grok Bot spend cap is not available. Account-level on-demand controls apply.

### Configure identity and access

Primary source: https://docs.x.ai/grok-bot/identity-and-access

- Grok Bot uses the existing Cursor SSO app. There is no separate Grok Bot application in Okta or Entra ID.
- Cursor SSO is SAML 2.0 and works with Okta, Microsoft Entra, Google Workspace, and OneLogin.
- SCIM 2.0 provisioning and deprovisioning is available on the Enterprise plan. Removing the user in the identity provider removes them from Cursor.
- Assign the existing Cursor app (and the SCIM app if used) to every group that should get Grok Bot.
- Members sign in to IdP-provisioned apps from the Bot's computer in the browser. The computer runs Linux and is not enrolled in MDM. Device-trust agents such as Okta FastPass do not run on it.
- Plugin authentication does not go through the computer, so computer-browser authentication rules do not apply to plugins.
- Requiring managed devices for Grok Bot sign-in still works, because Grok Bot uses Cursor SSO on the member's device.
- Revoking the user in the identity provider ends in-computer application sessions.

### Connect to private networks

Primary source: https://docs.x.ai/grok-bot/private-networks

- Hosted computers reach the internet through shared static egress IP addresses. Dedicated per-customer egress IPs are not available.
- A member can turn on Route egress through this desktop so destinations see that device's IP address and the Bot can reach networks available from that device.
- Enterprise Team Setup can install a networking client on every team computer. Cursor does not operate or monitor the client. Tailscale and Cloudflare Tunnel are the worked examples; other Linux clients follow the same pattern.
- Each Team Setup manifest holds script entries with an ID, a Setup Script, and an optional Check Script. Scripts run as the computer user with `sudo` available, at start and on a roughly daily refresh, with a 30-minute timeout per script.
- Setup scripts must not include secrets. Authenticate computers interactively in the computer's browser, or use a vendor mechanism that keeps long-lived credentials out of the script.
- If Grok Bot delegates work to Cloud Agents, those agents run under Cloud Agent network settings, not the Grok Bot computer's network client.

### Configure TLS-inspecting proxies

Primary source: https://docs.x.ai/grok-bot/proxies

- The desktop app connects to Cursor's API at `*.cursor.sh` for chat, sign-in, and approvals, and to the hosted computer at a nested `*.*.cursorvm.com` hostname.
- Gateways must allow `*.cursor.sh`, `*.cursor-cdn.com`, `*.cursorapi.com`, `*.cursorvm.com`, `*.*.cursorvm.com`, `cursor.com`, and `downloads.cursor.com`.
- The same domains need a TLS-inspection bypass and no response buffering. The nested `*.*.cursorvm.com` pattern is required; `*.cursorvm.com` alone is not enough.
- Exceptions must apply to every location and off-network profile. This page covers the path from the member device to Cursor, not the hosted computer's destination policy.

### Manage Grok Bot computers

Primary source: https://docs.x.ai/grok-bot/computers

- Grok Bot Computers on the Cursor dashboard is Enterprise only and appears only for organization admins.
- Recreate builds a replacement computer on the latest image, runs Team Setup, and keeps synced Bots, files, and logins. A Bot mid-turn is asked to pause; if it cannot pause in time, that member's recreate fails and the current computer stays.
- Terminate deletes the current computer. The member's next session starts a fresh computer on the same durable disk. Running work stops. Terminating does not remove access.
- Both actions remove apps and packages members installed themselves. Team Setup installs return on the new computer.
- Network policy changes reach computers without a recreate.

### Grok Bot security

Primary source: https://docs.x.ai/grok-bot/security

- Network policy destinations cover web domains and IP ranges with ports. Running computers apply changes within about a minute. Sleeping computers apply them when they next wake.
- Blocking a plugin does not block that service's website. Closing both paths takes the connector policy and Network Controls.
- Shared static egress ranges identify Grok Bot traffic, not one team. Current ranges come from the account team.
- Auto Review covers shell commands, plugin calls, computer use, automation writes (changes to routines and event triggers), and delegation such as Cloud Agent and subagent launches. It can allow, require approval, or deny. It does not review every side effect, such as memory writes and most settings changes.
- A Bot has no identity of its own and cannot hold more access than the signed-in member, except team-managed connectors that may use team or service-account credentials.
- Connector tokens stay on Cursor's backend. Bots invoke tools without receiving OAuth tokens, and tokens are not stored on the computer.
- Idle computers hibernate automatically. Image updates recreate computers on a fresh image with member files preserved.
- Under the Data Processing Agreement, data is deleted or returned within 30 days of written direction after the service ends. Daily encrypted backups cover the production control plane.
- A per-organization retention policy and customer-managed point-in-time restore of an individual computer are not available.
- Grok Bot computers run in the United States today. Cursor's US-only data residency program does not apply to Grok Bot by default.
- The team model allowlist is Enterprise only, and enforcement is not guaranteed. Onboarding presents an acknowledgement that Grok Bot may not follow the list.
- With Privacy Mode enabled, customer data is not used for training. Zero Data Retention follows Cursor's existing provider agreements.
- Grok Bot runs only on Cursor-hosted cloud computers. On-premises, in-perimeter, and bring-your-own-image deployment are not supported.
- Outside content is marked as untrusted data when presented to the model.
- Anysphere holds ISO/IEC 27001 and ISO/IEC 42001 certifications issued by Schellman, and Grok Bot is included in the current ISO scope. Certificates and reports are at trust.cursor.com. Source: https://docs.x.ai/grok-bot/security-faq

### Plans and billing

Primary source: https://cursor.com/help/grok-bot/plans

- Access is included on Cursor Pro, Pro+, Ultra, and self-serve Cursor Teams. Enterprise enablement is managed by the admin or account team.
- Individual SuperGrok, SuperGrok Plus, SuperGrok Heavy, and X Premium+ can grant usage on a Cursor account. SuperGrok Lite, SuperGrok Team, and SuperGrok Enterprise cannot link.
- Linking SuperGrok or X Premium+ is a usage grant, not a Cursor plan. The link is permanent and cannot be unlinked or moved to another Cursor account. Source: https://cursor.com/help/grok-bot/supergrok
- A Cursor plan and a SuperGrok or X Premium+ link do not stack. They do not add extra Grok Bot usage on top of each other.
- Weekly usage is included usage and resets weekly. On-demand usage is extra usage billed through Cursor after the weekly grant runs out, capped by the on-demand monthly limit.
- If on-demand is off, Grok Bot stops when weekly usage runs out.
- A run already in progress can finish past the monthly limit. After that, on-demand stops until the limit is raised or the billing cycle resets.
- macOS and iOS share one usage bucket on the signed-in Cursor account.
- The Grok Bot free trial is a usage credit with a 7-day window. Used trial credit is not restored. Cancel Trial on a free-plan account ends the trial immediately and cannot be claimed again.
- Request-based Teams plans and Enterprise seats do not take a personal SuperGrok link.
- On-demand usage already consumed and mid-cycle downgrades with usage are not refundable through Cursor. Store purchases follow Apple or Google Play refund paths. SuperGrok and X Premium+ are billed by xAI or X.

### Troubleshooting

Primary source: https://docs.x.ai/grok-bot/troubleshooting

- An error about Legacy Privacy Mode means the account data setting does not permit Grok Bot's required storage.
- Recover computer and Update preserve durable files and logins. Reset restores the last saved snapshot and can lose recent or unsynced work.
- On iPhone and Android, Update Computer and Reset Computer live under Settings → Bot → Bot Computer.
- A computer-use task already active on a Bot's screen may need to finish or be redirected before another one can start.
- If usage is exhausted or an on-demand spending limit is reached, review Usage & Billing or the account access page.
- Support intake asks for Grok Bot version, OS, the exact error, Bot or routine name, time and time zone, and the full request ID or conversation ID when shown.

## Sources

- https://docs.x.ai/grok-bot/overview
- https://docs.x.ai/grok-bot/get-started
- https://docs.x.ai/grok-bot/use-cases
- https://docs.x.ai/grok-bot/mobile
- https://docs.x.ai/grok-bot/bots
- https://docs.x.ai/grok-bot/chat-and-collaboration
- https://docs.x.ai/grok-bot/files-and-results
- https://docs.x.ai/grok-bot/computer-and-apps
- https://docs.x.ai/grok-bot/skills-routines-and-automations
- https://docs.x.ai/grok-bot/settings-and-notifications
- https://docs.x.ai/grok-bot/approvals-security-and-privacy
- https://docs.x.ai/grok-bot/teams-and-enterprises
- https://docs.x.ai/grok-bot/identity-and-access
- https://docs.x.ai/grok-bot/private-networks
- https://docs.x.ai/grok-bot/proxies
- https://docs.x.ai/grok-bot/computers
- https://docs.x.ai/grok-bot/security
- https://docs.x.ai/grok-bot/security-faq
- https://docs.x.ai/grok-bot/troubleshooting
- https://cursor.com/help/grok-bot/plans
- https://cursor.com/help/grok-bot/supergrok
- https://x.ai/bot
