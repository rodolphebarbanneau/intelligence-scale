"""One-model mock run. Rates every dossier at criterion level and writes a rating partial under a test- id.

The grades are a fixture. The shared scorer in cli/rating/ applies the cross-criterion caps, gates, and formulas.
The calibration anchors in src/config/reference.json come from this fixture.
"""

from __future__ import annotations

import json
from decimal import Decimal

from cli.errors import ScaleError
from cli.paths import REFERENCE_PATH, partial_path, relative
from cli.rating.rubric import load_rubric
from cli.rating.scoring import apply_cross_caps, exec_score, interpret, type_score
from cli.rating.specs import load_specs

RUN_ID = "test-2026-09-28"
MODEL = "grok-4.7"
DATE = "28 September 2026"
ANCHORS = ("agentforce", "cursor", "notion", "sierra", "t3code")

TYPE_RUBRIC = load_rubric("type")
EXEC_RUBRIC = load_rubric("exec")
TYPE_KEYS = TYPE_RUBRIC.keys
EXEC_KEYS = EXEC_RUBRIC.keys
ALLOWED = {Decimal(x) for x in ("0", "0.25", "0.50", "0.75", "1")}


def D(text: str) -> Decimal:
    return Decimal(text)


def num(value: Decimal, places: int) -> float:
    return float(f"{value:.{places}f}")


def row(grade: str, evidence: str, source: str) -> tuple:
    value = D(grade)
    if value not in ALLOWED:
        raise ScaleError(f"bad grade {grade}")
    return value, evidence, source


def zeros(source: str, evidence: str = "The cited pages do not establish this.") -> dict:
    return {key: row("0.00", evidence, source) for key in ("III.1", "III.2", "III.3", "III.4", "III.5", "III.6")}


def pack(items: dict) -> dict:
    missing = [key for key in TYPE_KEYS if key not in items]
    if missing:
        raise ScaleError(f"missing type keys {missing}")
    return items


# Primary sources, short enough for a table cell. Every URL must appear in that spec.
S = {
    "agentforce": "https://help.salesforce.com/s/articleView?id=ai.copilot_overview.htm",
    "agentforce-types": "https://help.salesforce.com/s/articleView?id=ai.agent_setup_explore_types.htm",
    "chatgpt": "https://help.openai.com/en/articles/12677804-what-is-chatgpt-faq",
    "chatgpt-apps": "https://help.openai.com/en/articles/11487775-connected-apps-in-chatgpt",
    "chatgpt-use": "https://learn.chatgpt.com/docs/use-chatgpt.md",
    "chatgpt-work": "https://help.openai.com/en/articles/20001143/",
    "claude": "https://support.claude.com/en/articles/8114491-get-started-with-claude",
    "claude-plugins": "https://support.claude.com/en/articles/13837440-use-plugins-in-claude",
    "claude-code": "https://code.claude.com/docs/en/overview",
    "claude-cowork": "https://claude.com/docs/cowork/overview",
    "codex": "https://developers.openai.com/codex/",
    "cursor": "https://cursor.com/docs/cloud-agent",
    "cursor-agent": "https://cursor.com/docs/agent/overview",
    "devin": "https://docs.devin.ai/get-started/devin-intro",
    "dust": "https://dust.tt/",
    "dust-intro": "https://docs.dust.tt/docs/user-documentation/getting-started/intro-to-dust",
    "dust-admin": "https://docs.dust.tt/docs/user-documentation/admins/admin-governance/workspace-governance-roles-groups-and-permissions",
    "dust-triggers": "https://docs.dust.tt/docs/user-documentation/agents/triggers/schedules",
    "dust-sidekick": "https://docs.dust.tt/docs/user-documentation/agents/default-agents/agent-builder-sidekick",
    "gemini": "https://gemini.google.com/",
    "github-copilot": "https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent",
    "glean": "https://docs.glean.com/agents/how-agents-work",
    "glean-auto": "https://docs.glean.com/agents/auto-mode-agent",
    "glean-lib": "https://docs.glean.com/agents/concepts/agent-library",
    "grok": "https://docs.x.ai/grok/overview",
    "grok-bot": "https://docs.x.ai/grok-bot/overview",
    "grok-bot-use": "https://docs.x.ai/grok-bot/use-cases",
    "grok-build": "https://docs.x.ai/build/overview",
    "m365": "https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview",
    "m365-cowork": "https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/",
    "notion": "https://www.notion.com/help/custom-agents",
    "notion-agent": "https://www.notion.com/help/notion-agent",
    "replit": "https://docs.replit.com/features/agent/overview",
    "sierra": "https://sierra.ai/product",
    "sierra-horizon": "https://sierra.ai/product/horizon",
    "sierra-live": "https://sierra.ai/product/live-assist",
    "sierra-studio": "https://sierra.ai/product/agent-studio",
    "sierra-aiuc": "https://sierra.ai/uk/blog/sierra-achieves-aiuc-1-certification",
    "t3code": "https://github.com/pingdotgg/t3code/blob/main/README.md",
    "t3code-composer": "https://github.com/pingdotgg/t3code/blob/main/docs/user/composer.md",
    "t3code-perm": "https://github.com/pingdotgg/t3code/blob/main/docs/user/permission-modes.md",
    "t3code-threads": "https://github.com/pingdotgg/t3code/blob/main/docs/user/thread-sidebar.md",
    "t3code-bg": "https://github.com/pingdotgg/t3code/blob/main/docs/user/background-service.md",
    "t3code-git": "https://github.com/pingdotgg/t3code/blob/main/docs/user/source-control.md",
    "t3code-remote": "https://github.com/pingdotgg/t3code/blob/main/docs/user/remote-access.md",
    "plateforme": "src/specs/plateforme.md",
}


def T(slug: str, grades: dict, summary: str, gap: str) -> dict:
    return {"rows": pack({**grades, **OVERRIDES.get(slug, {})}), "summary": summary, "gap": gap}


def E(grades: dict, summary: str, gap: str) -> dict:
    missing = [key for key in EXEC_KEYS if key not in grades]
    if missing:
        raise ScaleError(f"missing exec keys {missing}")
    return {"rows": grades, "summary": summary, "gap": gap}


def coding_iii(source: str, coordination: tuple | None = None) -> dict:
    base = zeros(source, "The cited pages do not show the agent running the company, allocating its work, or leaving people in governance.")
    if coordination:
        base["III.3"] = coordination
    return base


# Rows regraded against src/type.yaml: II.7 for every product, II.1 where a trigger rule repeats the same job,
# II.4 where a durable named actor has product-managed memory, and the redefined III.1 and III.6.
OVERRIDES = {
    "cursor": {
        "II.1": row("0.50", "Automations start Cloud Agents on cron, GitHub, Slack, and Linear events, so the same coding job repeats without a person handing over each run. No named actor is assigned a process or takes cases from its own intake.", S["cursor"]),
        "II.7": row("0.50", "A Cloud Agent builds, tests, and opens a pull request with no person between those stages. Merging and shipping the change stay with people.", S["cursor"]),
    },
    "codex": {
        "II.1": row("0.50", "Scheduled tasks, GitHub auto-review, and Linear assignment start the same coding work repeatedly. No named actor owns a process.", S["codex"]),
        "II.7": row("0.50", "A cloud run edits, tests, and returns a diff or pull request with no person between stages. Merging stays with people.", S["codex"]),
    },
    "claude-code": {
        "II.1": row("0.50", "Desktop scheduled tasks rerun a coding session on a cadence, and Routines are research preview. No named actor owns a process.", S["claude-code"]),
        "II.7": row("0.50", "A session gathers context, edits, and verifies without per-step prompting. The change still lands as a commit or pull request a person merges.", S["claude-code"]),
    },
    "devin": {
        "II.1": row("0.50", "Automations start sessions from Slack, GitHub, Linear, cron, or webhooks. Each session is still one coding task, with no named actor owning a process.", S["devin"]),
        "II.7": row("0.50", "A session codes, tests, and opens a pull request without a person orchestrating each command. Merging stays with people.", S["devin"]),
    },
    "github-copilot": {
        "II.1": row("0.50", "Automations start cloud agent on schedules or issue events. The owned unit is still one task ending in one pull request.", S["github-copilot"]),
        "II.7": row("0.50", "The agent edits and tests in Actions, then opens a pull request. People review and merge it.", S["github-copilot"]),
    },
    "replit": {
        "II.1": row("0.50", "Routines rerun work hourly, daily, or weekly from a chat. They are personal, and no named actor owns a process.", S["replit"]),
        "II.7": row("0.50", "Agent implements and runs App Testing without a person between steps. Routines cannot schedule publishing, so shipping stays with people.", S["replit"]),
    },
    "grok-build": {
        "II.7": row("0.50", "Always-approve runs and workflows edit files and run commands through a coding task. The spec does not show the change delivered without a person.", S["grok-build"]),
    },
    "t3code": {
        "II.7": row("0.50", "A thread progresses a coding task in its worktree, and source control can commit and push. A person still starts each thread and lands the change.", S["t3code-git"]),
    },
    "grok-bot": {
        "II.7": row("0.50", "Routines and computer-use turns run their steps with the app closed. Many writes land as Send cards a person confirms, and starter guidance has people review drafts.", S["grok-bot"]),
    },
    "chatgpt": {
        "II.1": row("0.50", "Scheduled tasks rerun a saved prompt in the background. Chat itself is person-steered, and no actor owns a process.", S["chatgpt-use"]),
        "II.7": row("0.25", "A chat turn or scheduled task returns a finished answer or file. A person moves the work to its next stage.", S["chatgpt-use"]),
    },
    "claude": {
        "II.1": row("0.25", "A person can hand Claude a request or a Research task and get a finished result. Nothing repeats without a person.", S["claude"]),
        "II.7": row("0.25", "A chat or Research run returns a finished answer or artifact. A person carries it further.", S["claude"]),
    },
    "gemini": {
        "II.1": row("0.50", "Scheduled actions rerun a prompt on a schedule. Gemini Apps is otherwise person-steered, and Spark is experimental.", S["gemini"]),
        "II.7": row("0.25", "A chat, Deep Research, or scheduled action returns a finished answer or report. A person moves the work on.", S["gemini"]),
    },
    "grok": {
        "II.1": row("0.25", "A person can hand the assistant a request and get a finished answer. No schedules or triggers are specified.", S["grok"]),
        "II.7": row("0.25", "A conversation returns a finished answer. A person moves the work on.", S["grok"]),
    },
    "chatgpt-work": {
        "II.7": row("0.50", "A published agent runs its configured steps without anyone typing each one. The spec does not show routine cases delivered to their final outcome in a system of record.", S["chatgpt-work"]),
    },
    "claude-cowork": {
        "II.1": row("0.50", "Scheduled tasks rerun Cowork work on a cadence while the computer sleeps. Each run is its own session, not a named actor owning a process.", S["claude-cowork"]),
        "II.7": row("0.50", "Inside a task Claude progresses through several steps with no person between them. The spec does not show routine outcomes delivered without a person.", S["claude-cowork"]),
    },
    "microsoft-365-copilot": {
        "II.1": row("0.50", "Scheduled prompts and Cowork scheduled or event-driven tasks rerun work without a person starting each run. No named actor owns a process.", S["m365"]),
        "II.7": row("0.50", "Cowork progresses a multi-step plan across mail, files, and meetings, asking before sensitive actions. The spec does not show routine outcomes closed without a person.", S["m365-cowork"]),
    },
    "notion": {
        "II.7": row("0.50", "A Custom Agent runs its trigger's steps across pages, databases, and mail. The spec does not show routine cases carried to their final outcome.", S["notion"]),
    },
    "dust": {
        "II.7": row("0.50", "A triggered run progresses through its tool calls with no person between steps. The spec does not show routine cases delivered to their final outcome.", S["dust-triggers"]),
    },
    "glean": {
        "II.7": row("0.50", "Auto mode and workflow mode run their steps toward an outcome. Web write actions wait for confirmation unless admins allow unattended writes.", S["glean"]),
    },
    "agentforce": {
        "II.7": row("0.50", "A Service agent answers common inquiries and runs record actions inside the conversation, escalating complex ones. The spec does not state that routine cases close with the outcome recorded without a person.", S["agentforce"]),
    },
    "sierra": {
        "II.4": row("0.75", "The brand agent persists across conversations and channels, with Context Engine memory the product manages. It is not its own principal with its own credentials.", S["sierra-horizon"]),
        "II.7": row("0.75", "Journeys such as a claim or renewal are carried to an outcome, and escalation handles exceptions. The spec does not show that across every routine case type.", S["sierra-horizon"]),
    },
    "plateforme": {
        "II.7": row("0.50", "An Action moves a released workflow from queued to completed across agents, operators, and applications. The spec does not state that routine cases end with the business outcome recorded in the system of record.", S["plateforme"]),
        "III.1": row("0.25", "Operators and Actions start on triggers and run without anyone typing. The spec does not show a whole process running unattended to its final outcome.", S["plateforme"]),
        "III.6": row("0.75", "Budgets, caps, permissions, and grants are enforced on operators, and the audit log records activity. The spec does not show irreversible actions gated apart from routine ones, or audits of AI decisions against policy.", S["plateforme"]),
    },
}


RATINGS = {
    "cursor": {
        "type": T(
            "cursor",
            {
                "I.1": row("1.00", "Agent, Tab, and inline edit sit in the normal editor loop.", S["cursor-agent"]),
                "I.2": row("1.00", "Agent tools include search, files, shell, browser control, and MCP.", S["cursor-agent"]),
                "I.3": row("1.00", "Cloud Agents build, test, use a desktop and browser, and open pull requests without the laptop staying online.", S["cursor"]),
                "I.4": row("1.00", "Plan Mode waits for approval. Run modes, checkpoints, and spend limits keep the person in charge.", S["cursor-agent"]),
                "I.5": row("1.00", "Team rules, shared Cloud Agents, automations, and SSO make the same coding workflow repeatable.", S["cursor"]),
                "II.1": row("0.25", "Automations and Cloud Agents run coding jobs. The spec does not show a persistent actor that owns a business process.", S["cursor"]),
                "II.2": row("1.00", "Once started, a Cloud Agent builds, tests, and opens a pull request with no person between steps. Plan Mode approval is optional.", S["cursor"]),
                "II.3": row("1.00", "The agent selects files, shell, browser, MCP, and built-in subagents during a run.", S["cursor-agent"]),
                "II.4": row("0.50", "Each Cloud Agent run is a dedicated microVM that ends. Automations persist a job config, not a durable worker.", S["cursor"]),
                "II.5": row("1.00", "Plan Mode, run modes, Agent Review, checkpoints, and Enterprise audit logs let people inspect and stop work.", S["cursor"]),
                "II.6": row("1.00", "Automations start Cloud Agents on cron, GitHub, Slack, Linear, and other events.", S["cursor"]),
                **coding_iii(S["cursor"], row("0.25", "Subagents run inside one human-started coding task.", S["cursor-agent"])),
            },
            "Cursor natively augments software work: people stay in charge while Agent and Cloud Agents complete bounded coding tasks. Automations can start those tasks. Nothing in the spec gives a persistent actor ownership of a business process.",
            "Type II is blocked by II.1: each run is one coding task, with no persistent actor that owns a process. II.4 is an ephemeral VM, not a durable principal.",
        ),
        "exec": E(
            {
                "E.1": row("0.25", "Cursor is a coding agent for codebases, features, bugs, and reviews. Only that craft uses it.", S["cursor-agent"]),
                "E.2": row("0.75", "Teammates with repo access can open a Cloud Agent run read-only and send follow-ups. Live side-by-side work is limited.", S["cursor"]),
                "E.3": row("0.25", "Native write-back is the repository and pull requests. Other systems are MCP the buyer wires.", S["cursor"]),
                "E.4": row("0.25", "The Cursor Marketplace installs plugins, skills, and MCPs for coding work.", S["cursor-agent"]),
                "E.5": row("0.75", "Runs start from the desktop app, CLI, web, iOS, Slack, GitHub comments, Linear, and an API.", S["cursor"]),
                "E.6": row("1.00", "Individuals download the app and sign in. Teams and Enterprise have documented setup, SSO, and admin.", S["cursor"]),
                "E.7": row("0.25", "Ready-made jobs such as Agent, Bugbot, and PR review stay inside software delivery.", S["cursor"]),
            },
            "An engineering team can put repository work on Cursor across the editor, cloud, and chat start points. The catalog and the jobs stay inside software engineering.",
            "E.1, E.3, E.4, and E.7 are specialist-craft 0.25, so the published score cannot reach 0.50.",
        ),
    },
    "codex": {
        "type": T(
            "codex",
            {
                "I.1": row("1.00", "Codex is the coding loop in the CLI, IDE, ChatGPT desktop app, cloud, and Remote.", S["codex"]),
                "I.2": row("1.00", "Sessions inspect files, edit the repo, run tools, and can use MCP, skills, and plugins.", S["codex"]),
                "I.3": row("1.00", "A local turn loops on tool output until the task finishes. Cloud runs isolated containers the person can leave.", S["codex"]),
                "I.4": row("1.00", "An approval policy and sandbox decide when Codex must stop and ask.", S["codex"]),
                "I.5": row("1.00", "AGENTS.md, skills, plugins, scheduled tasks, and managed configuration support repeatable team use.", S["codex"]),
                "II.1": row("0.25", "Cloud chats, review, and scheduled tasks complete coding jobs, not a business process.", S["codex"]),
                "II.2": row("1.00", "A cloud run loops on tool output until the task finishes, with no human at each step. The approval policy is the organization's choice.", S["codex"]),
                "II.3": row("1.00", "Codex uses subagents and MCP or plugin tools during the run without the person coordinating each call.", S["codex"]),
                "II.4": row("0.50", "Cloud containers and threads resume. There is no durable named worker principal.", S["codex"]),
                "II.5": row("1.00", "Sandbox modes, approval policies, review, and Enterprise logs support supervision of coding work.", S["codex"]),
                "II.6": row("1.00", "Scheduled tasks, GitHub auto-review, and Linear assignment can start coding work without a fresh prompt.", S["codex"]),
                **coding_iii(S["codex"], row("0.25", "Subagents run inside one session when the person or a skill asks.", S["codex"])),
            },
            "Codex natively augments software development across CLI, IDE, and cloud, with sandbox approvals and repeatable project setup. Scheduled review can start coding work. The product still executes tasks people or ticket events dispatch.",
            "Type II is blocked by II.1: runs are coding tasks people or events dispatch. II.4 stays a cloud chat, not a persistent principal.",
        ),
        "exec": E(
            {
                "E.1": row("0.25", "Codex is OpenAI's coding agent for project files, commands, and reviews. Only that craft uses it.", S["codex"]),
                "E.2": row("0.50", "Business and Enterprise workspaces exist. Slack and share links hand off a thread after the fact, not a live operator run.", S["codex"]),
                "E.3": row("0.25", "Native artifacts are the repository and PR diffs. Other systems are MCP the buyer adds.", S["codex"]),
                "E.4": row("0.25", "ChatGPT and Codex share a plugin directory for coding plugins.", S["codex"]),
                "E.5": row("0.75", "Surfaces include CLI, IDE, desktop, cloud web, Slack, GitHub, and Linear.", S["codex"]),
                "E.6": row("1.00", "Codex ships on ChatGPT plans and via API-key local use, with documented install and Enterprise admin.", S["codex"]),
                "E.7": row("0.25", "Shipped jobs are coding, review, and security scans inside one craft.", S["codex"]),
            },
            "A development team can turn on Codex from a ChatGPT plan and run it locally and in the cloud. Shared work is mostly snapshots and pull requests.",
            "E.1, E.3, E.4, and E.7 stay at specialist-craft 0.25, so the score cannot reach 0.50.",
        ),
    },
    "claude-code": {
        "type": T(
            "claude-code",
            {
                "I.1": row("1.00", "The same engine runs in the terminal, VS Code, JetBrains, desktop, claude.ai/code, and mobile.", S["claude-code"]),
                "I.2": row("1.00", "Built-in tools cover files, search, shell, and web. MCP, CLAUDE.md, and skills attach extra context.", S["claude-code"]),
                "I.3": row("1.00", "A session loops gather context, take action, and verify. Cloud sessions keep running after the laptop closes.", S["claude-code"]),
                "I.4": row("1.00", "Permission modes include Manual, Accept edits, Plan, and Auto. People interrupt and restore checkpoints.", S["claude-code"]),
                "I.5": row("1.00", "CLAUDE.md, skills, hooks, plugins, and Team or Enterprise managed settings support repeatable use.", S["claude-code"]),
                "II.1": row("0.25", "Documented work is tests, features, PRs, and scheduled coding sessions, not a business process.", S["claude-code"]),
                "II.2": row("1.00", "Cloud sessions gather context, act, and verify without per-step prompting. Auto mode leaves approvals to the organization.", S["claude-code"]),
                "II.3": row("1.00", "Built-in tools include Agent, Skill, Workflow, and subagents the session can select.", S["claude-code"]),
                "II.4": row("0.50", "Sessions save and resume. Cloud VMs are reclaimed after inactivity. Routines are a research preview.", S["claude-code"]),
                "II.5": row("1.00", "Allow, ask, and deny rules, sandbox, Plan mode, hooks, and cloud audit logs are native.", S["claude-code"]),
                "II.6": row("0.75", "Desktop scheduled tasks run while the app is open. Routines and managed Code Review are research preview.", S["claude-code"]),
                **coding_iii(S["claude-code"], row("0.25", "Subagents return a summary to the parent. Agent teams are experimental and off by default.", S["claude-code"])),
            },
            "Claude Code is a native Type I coding agent: people direct sessions while the model edits, runs commands, and continues in the cloud. The strongest event and schedule products are preview. No actor owns a business process.",
            "Type II is blocked by II.1: sessions are coding tasks. II.6 cannot reach 1.00 while Routines are preview. II.4 lacks a durable principal.",
        ),
        "exec": E(
            {
                "E.1": row("0.25", "Claude Code reads a codebase, edits files, and runs commands. Only that craft uses it.", S["claude-code"]),
                "E.2": row("0.50", "Team cloud sessions can be Private or Team. Slack can start a session. The coding work stays in one session.", S["claude-code"]),
                "E.3": row("0.25", "Cloud clone and PR creation require GitHub. Other systems appear as MCP the buyer connects.", S["claude-code"]),
                "E.4": row("0.25", "The plugin marketplace bundles skills, agents, hooks, and MCP for the coding agent.", S["claude-code"]),
                "E.5": row("0.75", "Surfaces include CLI, VS Code, JetBrains, desktop, web, mobile, Slack, and GitHub.", S["claude-code"]),
                "E.6": row("1.00", "Native installers and IDE plugins are documented. Team and Enterprise add managed settings and SSO.", S["claude-code"]),
                "E.7": row("0.25", "Bundled skills and jobs stay inside coding. The buyer designs every other job.", S["claude-code"]),
            },
            "A software team can install Claude Code and run it in the terminal, IDE, desktop, browser, and Slack. Ready-made work stays in the coding craft.",
            "E.1, E.3, E.4, and E.7 are specialist-craft 0.25, so the score cannot reach 0.50.",
        ),
    },
    "devin": {
        "type": T(
            "devin",
            {
                "I.1": row("1.00", "Devin is Cognition's AI software engineer. People start work from the web app, Slack, Teams, CLI, Desktop, or API.", S["devin"]),
                "I.2": row("1.00", "Cloud sessions run in a VM with repos, a shell, an IDE, a browser, secrets, and Computer Use.", S["devin"]),
                "I.3": row("1.00", "Agent mode writes code, runs commands, browses, and can open a pull request and watch CI.", S["devin"]),
                "I.4": row("1.00", "People watch Progress and can take over the IDE or browser. Auto-approve for child sessions can be turned off.", S["devin"]),
                "I.5": row("1.00", "Plans, playbooks, skills, automations, and org membership make the same workflow repeatable.", S["devin"]),
                "II.1": row("0.25", "Documented work is a software task. The intro's rule of thumb is a long coding task, not a business process.", S["devin"]),
                "II.2": row("1.00", "Once started, a session progresses through the coding task without a person orchestrating each command.", S["devin"]),
                "II.3": row("1.00", "The session selects the shell, editor, browser, git, and Computer Use during the run. Enabling Computer Use is admin setup.", S["devin"]),
                "II.4": row("0.25", "Each session boots an ephemeral VM. Auto-triage spawns child sessions, not a durable worker principal.", S["devin"]),
                "II.5": row("0.75", "Session Insights, IDE takeover, Devin Review, and enterprise audit logs let people inspect a run.", S["devin"]),
                "II.6": row("1.00", "Automations start sessions from Slack, GitHub, Linear, cron, or webhooks with no person starting each run.", S["devin"]),
                **coding_iii(S["devin"], row("0.25", "A parent session can launch child sessions inside one human-started coding run.", S["devin"])),
            },
            "Devin natively augments software engineering: a person hands it a ticket, and the agent codes, tests, and opens a pull request. Triggers make long coding tasks less manual. People still decide which work exists and review each result.",
            "Type II is blocked by II.1 and II.4: no business-process ownership and no persistent AI principal.",
        ),
        "exec": E(
            {
                "E.1": row("0.25", "The product is aimed at engineering teams. Documented jobs are tickets, features, bugs, migrations, and reviews.", S["devin"]),
                "E.2": row("0.75", "Teams share an org machine. Slack can start a session in-thread. Several people sharing one run as first-class multiplayer is not documented.", S["devin"]),
                "E.3": row("0.50", "Native write-back is source control. Linear, Jira, and PagerDuty mainly trigger sessions.", S["devin"]),
                "E.4": row("0.25", "The plugin marketplace installs skills, MCP, hooks, and rules for coding sessions.", S["devin"]),
                "E.5": row("0.75", "Work runs in the web app, Slack, Teams, CLI, Desktop, GitHub comments, and the API.", S["devin"]),
                "E.6": row("1.00", "Self-serve signup covers Free through Teams. Membership, roles, and Enterprise SSO are documented.", S["devin"]),
                "E.7": row("0.25", "Ready-made jobs such as Review and Code Scans stay inside software engineering.", S["devin"]),
            },
            "An engineering team can sign up, connect repos, and run coding sessions from the web or Slack. Coverage does not leave software work.",
            "E.1, E.4, and E.7 stay at specialist-craft 0.25, so the score cannot reach 0.50.",
        ),
    },
    "github-copilot": {
        "type": T(
            "github-copilot",
            {
                "I.1": row("1.00", "Copilot is GitHub's assistant for writing and shipping software in IDEs, github.com, Mobile, CLI, and the Copilot app.", S["github-copilot"]),
                "I.2": row("1.00", "Cloud agent uses the repository, issues, historic pull requests, instructions, MCP, hooks, and skills.", S["github-copilot"]),
                "I.3": row("1.00", "Cloud agent researches a repository, edits a branch, and opens a pull request. A session has a 59-minute cap.", S["github-copilot"]),
                "I.4": row("1.00", "A person assigns the task and reviews the diff. Business and Enterprise need an admin policy.", S["github-copilot"]),
                "I.5": row("1.00", "Paid plans include cloud agent. Automations run on a schedule or repository event.", S["github-copilot"]),
                "II.1": row("0.25", "The owned unit is one coding task in one repository, ending in one pull request.", S["github-copilot"]),
                "II.2": row("1.00", "After start, the Actions environment edits and tests without the developer sitting in an IDE.", S["github-copilot"]),
                "II.3": row("0.75", "The agent uses the repo and MCP. It can change only the specified repository, one branch, and one pull request.", S["github-copilot"]),
                "II.4": row("0.25", "Work runs in an ephemeral GitHub Actions environment. Copilot Memory is public preview.", S["github-copilot"]),
                "II.5": row("0.75", "People review the diff. Code review and automation confidence holds exist.", S["github-copilot"]),
                "II.6": row("1.00", "Automations start cloud agent on schedules or issue events with no person starting each run.", S["github-copilot"]),
                **coding_iii(S["github-copilot"]),
            },
            "Copilot natively assists software work: completions in the editor and a cloud agent that returns a pull request. Schedules and issue events can start a run. The process owned is still one repository change.",
            "Type II is blocked by II.1 and II.4: one coding task in an ephemeral Actions session.",
        ),
        "exec": E(
            {
                "E.1": row("0.25", "Copilot is GitHub's assistant for writing and shipping software. Documented jobs stay in the repository workflow.", S["github-copilot"]),
                "E.2": row("0.50", "Business and Enterprise seats exist. Sharing is a pull request. Slack and Teams planning are public preview.", S["github-copilot"]),
                "E.3": row("0.50", "Cloud agent works with GitHub-hosted repositories and writes one pull request.", S["github-copilot"]),
                "E.4": row("0.25", "Plugins, skills, and the MCP Registry are a coding catalog.", S["github-copilot"]),
                "E.5": row("0.75", "Surfaces include many IDEs, github.com, Mobile, CLI, Slack, and Teams.", S["github-copilot"]),
                "E.6": row("1.00", "Copilot Free through Enterprise have documented seats, AI Controls, and an onboarding path.", S["github-copilot"]),
                "E.7": row("0.25", "Shipped jobs are completions, chat, cloud agent, and code review.", S["github-copilot"]),
            },
            "A GitHub team can turn Copilot on and run coding work from the IDE or github.com. Span, catalog, and ready-made jobs stay inside software development.",
            "E.1, E.4, and E.7 are specialist-craft 0.25, so the score cannot reach 0.50.",
        ),
    },
    "replit": {
        "type": T(
            "replit",
            {
                "I.1": row("1.00", "Replit Agent is the documented partner in Chat and the Project Editor that sets up a project and writes code.", S["replit"]),
                "I.2": row("1.00", "Agent works inside a Project and can use connectors, MCP servers, skills, and web search.", S["replit"]),
                "I.3": row("1.00", "Agent writes code, sets up infrastructure, tests in a browser, and can produce apps.", S["replit"]),
                "I.4": row("1.00", "The person reviews the plan, applies or dismisses a Ready task, and can roll back to a checkpoint.", S["replit"]),
                "I.5": row("1.00", "Starter through Enterprise workspaces, Team seats, and published apps make the same build path repeatable.", S["replit"]),
                "II.1": row("0.25", "The owned work is the Project being built. That is not ownership of a business process.", S["replit"]),
                "II.2": row("1.00", "After plan approval, Agent implements in the current session or as a background task without a person between steps.", S["replit"]),
                "II.3": row("1.00", "During a build Agent selects code, infrastructure, connectors, and App Testing.", S["replit"]),
                "II.4": row("0.25", "Memories and checkpoints snapshot a Project. There is no durable worker identity.", S["replit"]),
                "II.5": row("0.75", "Plan approval, apply or dismiss, checkpoints, and App Testing takeover are the controls.", S["replit"]),
                "II.6": row("0.75", "Routines schedule hourly, daily, or weekly work from a chat. They are personal and cannot schedule publishing.", S["replit"]),
                **coding_iii(S["replit"]),
            },
            "Replit Agent natively turns a prompt into a Project: it plans, codes, tests, and publishes while the person approves the plan. The owned unit is still a build, not a business process.",
            "Type II is blocked by II.1 and II.4: a project build and no persistent AI principal.",
        ),
        "exec": E(
            {
                "E.1": row("0.25", "Replit Agent builds and changes Replit Projects. That is specialist creation and coding craft.", S["replit"]),
                "E.2": row("0.75", "Paid Team Workspaces share projects. Chats stay private to the owner.", S["replit"]),
                "E.3": row("0.50", "The product primarily reads and writes its own Project. Connectors are sign-in integrations.", S["replit"]),
                "E.4": row("0.25", "The skills directory and MCP picker add builder skills for the same app-building craft.", S["replit"]),
                "E.5": row("0.75", "Work runs on replit.com, Desktop, Mobile, Slack, ChatGPT, and Claude.", S["replit"]),
                "E.6": row("1.00", "Starter includes daily Agent credits. Core, Pro, and Enterprise have documented seats and billing.", S["replit"]),
                "E.7": row("0.25", "Agent is a general builder. SEO and Security agents stay inside creating a Replit Project.", S["replit"]),
            },
            "A team can sign up, share a Workspace, and ask Agent to build and publish a Project. Named skills do not move coverage off the app-building craft.",
            "E.1, E.4, and E.7 stay at specialist-craft 0.25, so the score cannot reach 0.50.",
        ),
    },
    "grok-build": {
        "type": T(
            "grok-build",
            {
                "I.1": row("1.00", "Grok Build is used as an interactive TUI in a project directory, or headlessly in scripts and CI.", S["grok-build"]),
                "I.2": row("1.00", "Prompts attach project files. grok inspect reports rules, skills, plugins, hooks, and MCP servers.", S["grok-build"]),
                "I.3": row("1.00", "The agent edits files, runs bash, uses MCP tools, and can orchestrate background subagents via workflows.", S["grok-build"]),
                "I.4": row("1.00", "Plan mode drafts a plan that must be approved before edits. Ask mode prompts for unallowed tools.", S["grok-build"]),
                "I.5": row("1.00", "Conversations persist and can be resumed. Enterprise OIDC and managed policy files pin org use.", S["grok-build"]),
                "II.1": row("0.25", "Workflows and coding sessions complete software jobs. The spec does not show a persistent actor that owns a business process.", S["grok-build"]),
                "II.2": row("1.00", "Always-approve runs and workflows progress a coding task without a human at each tool call.", S["grok-build"]),
                "II.3": row("1.00", "The agent selects built-in tools, MCP servers, and background subagents during a coding turn.", S["grok-build"]),
                "II.4": row("0.50", "Conversations persist on disk and can be resumed. There is no durable named worker principal.", S["grok-build"]),
                "II.5": row("1.00", "Plan mode, Ask mode, and permission policies let people inspect and approve tool calls.", S["grok-build"]),
                "II.6": row("0.50", "/loop repeats a prompt on an interval after a person starts it. There are no schedules or event triggers.", S["grok-build"]),
                **coding_iii(S["grok-build"], row("0.25", "Subagents are child sessions that return a summary to a parent.", S["grok-build"])),
            },
            "Grok Build natively augments software work: people stay in charge while the local agent edits, runs tools, and resumes sessions. Workflows and /loop are still long coding tasks a person starts. Nothing in the spec gives a persistent actor ownership of a business process.",
            "Type II is blocked by II.1: runs are coding tasks a person starts. II.6 is a person-started loop, not event initiation.",
        ),
        "exec": E(
            {
                "E.1": row("0.25", "Grok Build is xAI's coding agent used in a project directory through a local TUI and CLI.", S["grok-build"]),
                "E.2": row("0.25", "/share and remote session sync are listed. Several people and an operator in the same work are not described.", S["grok-build"]),
                "E.3": row("0.25", "The agent reads and writes the local repo and shell. Other systems need MCP the buyer adds.", S["grok-build"]),
                "E.4": row("0.25", "The Marketplace tab installs plugins that add skills, agents, hooks, and MCP for coding.", S["grok-build"]),
                "E.5": row("0.50", "Work happens in the interactive TUI and through headless grok -p or ACP.", S["grok-build"]),
                "E.6": row("1.00", "Documented curl, PowerShell, and npm install, plus enterprise OIDC and managed policy files.", S["grok-build"]),
                "E.7": row("0.25", "Skills and plugins stay inside coding. The buyer writes every other job.", S["grok-build"]),
            },
            "An organization can put software-engineering work on a local grok CLI with a real install path. Coverage does not leave the coding craft.",
            "E.1, E.2, E.3, E.4, and E.7 sit at 0.25. Specialist span caps the published score at 0.49.",
        ),
    },
    "t3code": {
        "type": T(
            "t3code",
            {
                "I.1": row("1.00", "T3 Code starts and steers installed coding-agent CLIs from one desktop, web, or mobile interface.", S["t3code"]),
                "I.2": row("1.00", "The composer attaches files, terminal excerpts, review comments, and pull requests as context.", S["t3code"]),
                "I.3": row("1.00", "A turn runs the provider's agent loop: it decides each step from what the previous one returned and chains tool calls until it ends the turn. With Full access it edits and runs commands without approvals, and each tool call shows in the thread.", S["t3code-composer"]),
                "I.4": row("1.00", "Stop halts a running turn, Steer sends messages into it, permission modes gate commands and edits, and Edit from here rewinds and continues.", S["t3code-composer"]),
                "I.5": row("0.50", "Threads, project settings, and t3.json scripts persist on the server. The spec does not show that configuration shared with a team or managed by an admin.", S["t3code"]),
                "II.1": row("0.25", "The strongest supported wrap still completes coding jobs a person starts. That is not a persistent actor that owns a business process.", S["t3code"]),
                "II.2": row("0.50", "With Full access, the default, a thread runs a coding task to the end with no prompt between tool calls. The spec does not show a run moving work across stages of a process.", S["t3code-threads"]),
                "II.3": row("0.75", "During a run the wrapped agent uses shell, file, subagent, browser preview, and device tools. The spec does not say it alone chooses which to call and in what order.", S["t3code-threads"]),
                "II.4": row("0.50", "Threads persist on the T3 server and can continue after a restart. The durable actor is still the provider process, not a named worker principal.", S["t3code-threads"]),
                "II.5": row("1.00", "Per-thread Supervised, Auto-accept, Auto, and Full access modes, plus the question panel and mobile alerts, let people supervise the wrap.", S["t3code-perm"]),
                "II.6": row("0.50", "A person starts each thread, which then keeps running on a background server that survives logout, and can resume after a crash or restart. T3 does not ship schedules or event starts, and it does not surface the providers' own cloud triggers.", S["t3code-bg"]),
                **coding_iii(S["t3code"], row("0.25", "T3 groups subagent activity from the wrapped provider inside one human-started thread.", S["t3code-threads"])),
            },
            "T3 Code lets people steer provider coding agents from desktop, web, or mobile, with worktrees, permission modes, stop, and live steering. Each turn runs the provider's self-directed agent loop. Configuration stays with one person's environments, so the Type I floor is incomplete. T3 does not start work on a schedule.",
            "I.5 blocks the Type I floor: threads, settings, and scripts persist and can be reused, but the spec does not show them shared with a team or managed by an organization admin. Type II is further blocked by II.1 and II.6. Do not copy a sibling provider's grades; this score is what T3 exposes and adds.",
        ),
        "exec": E(
            {
                "E.1": row("0.25", "T3 wraps coding agents. Several providers do not widen span beyond that craft.", S["t3code"]),
                "E.2": row("0.00", "Remote pairing and mobile notifications reach the same person's other devices. The spec shows no notification or link to another person.", S["t3code-remote"]),
                "E.3": row("0.25", "Native write-back is the workspace and Git hosts. Other company systems are not shipped jobs.", S["t3code-git"]),
                "E.4": row("0.00", "Extensibility is more coding-agent providers. T3 itself ships no plugins, extensions, or MCP servers.", S["t3code"]),
                "E.5": row("0.50", "Shipped surfaces are the desktop app, app.t3.codes, iOS, Android, and the t3 CLI. There is no workplace-chat surface.", S["t3code-remote"]),
                "E.6": row("0.50", "Installers and a welcome wizard let an individual start. T3 sells no plan and org admin is pairing links.", S["t3code"]),
                "E.7": row("0.25", "T3 does not ship ready-made jobs. The wrap's coding jobs stay that provider's catalog.", S["t3code"]),
            },
            "A developer can install T3 Code and steer a first-class coding wrap from desktop, web, or mobile. Coverage stays the coding craft. The wrap does not import a sibling provider's company-admin path or ready-made jobs.",
            "E.2 and E.4 are zero: nothing reaches another person, and T3 ships no extensions of its own. E.1, E.3, and E.7 stay at 0.25. Wrapping several coding agents does not raise span, and specialist span caps the score at 0.49.",
        ),
    },
    "grok-bot": {
        "type": T(
            "grok-bot",
            {
                "I.1": row("1.00", "A person works with a named Bot by messaging it in the desktop or mobile app.", S["grok-bot"]),
                "I.2": row("1.00", "Bots use marketplace connectors where available and computer use for other apps, plus files and per-Bot memory.", S["grok-bot"]),
                "I.3": row("1.00", "A Bot runs multi-step work on a persistent cloud computer. Closing the app does not stop a background turn or a routine.", S["grok-bot"]),
                "I.4": row("1.00", "Approval requests offer Allow once, Deny, or Always allow. Email and Slack drafts wait for Send or Discard.", S["grok-bot"]),
                "I.5": row("1.00", "Named Bots keep memory, files, and preferences. Teams enables Grok Bot by default.", S["grok-bot"]),
                "II.1": row("0.50", "A named Bot persists and runs routines on a schedule or event. Each routine is still a delegated task, not a process the Bot is put in charge of.", S["grok-bot-use"]),
                "II.2": row("1.00", "Computer-use turns and routines run their steps with the app closed. Always allow leaves approvals to the person.", S["grok-bot"]),
                "II.3": row("0.75", "During a turn the Bot uses connectors, computer use, and optional Cloud Agent delegation. Many writes land as human Send cards.", S["grok-bot"]),
                "II.4": row("0.75", "Each Bot is a named teammate with memory on a durable cloud computer, but it cannot hold more access than the signed-in member.", S["grok-bot"]),
                "II.5": row("0.75", "Approvals, Auto Review, and Enterprise audit are native. Starter guidance still has people review drafts.", S["grok-bot"]),
                "II.6": row("0.75", "A routine runs one Bot on a schedule or, where supported, after a Slack or GitHub event.", S["grok-bot"]),
                **{
                    **zeros(S["grok-bot"], "The overview does not establish a closed loop that changes how the company is run, or a human role limited to governance."),
                    "III.1": row("0.25", "Routines and background turns can run with the app closed. Org-wide operations still need human grants and reviews.", S["grok-bot"]),
                    "III.2": row("0.25", "In a group chat, Bots can decide who should respond. They do not determine the organization's operational work.", S["grok-bot"]),
                    "III.3": row("0.75", "Bots message each other, share group-chat context, and can pass task ownership. A group is two to six Bots.", S["grok-bot"]),
                },
            },
            "Grok Bot is a Type I teammate product with real Type II primitives: a named durable Bot, supervision, scheduled or event routines, and bot-to-bot handoff. Each routine is still a delegated task, and many writes stop at a Send card.",
            "Type II is blocked by II.1: routines are delegated tasks, not a process the Bot owns. II.3 through II.6 are limited by draft writes, member-scoped access, and triggers only where supported.",
        ),
        "exec": E(
            {
                "E.1": row("1.00", "Starter roles include sales, talent, paid media, expenses, product, bugs, accounts, and chief of staff. People across functions can put work on a Bot.", S["grok-bot-use"]),
                "E.2": row("0.75", "A group chat holds a person plus two to six Bots with shared context and bot-to-bot handoff. Sharing a Bot is a template copy.", S["grok-bot"]),
                "E.3": row("0.75", "Marketplace connectors plus computer use can operate many apps. Email and Slack writes are often draft cards awaiting Send.", S["grok-bot"]),
                "E.4": row("0.75", "Marketplace installs connectors and packaged skills. The person still describes the job.", S["grok-bot"]),
                "E.5": row("0.50", "Work happens in the desktop app and the iPhone and Android apps. Slack and email are outbound draft cards.", S["grok-bot"]),
                "E.6": row("1.00", "Eligible Cursor or SuperGrok accounts download the app and create a Bot. Teams is on by default.", S["grok-bot"]),
                "E.7": row("0.75", "Starter roles for several functions ship a suggested source list and a starter prompt. A person still connects sources and sets routines.", S["grok-bot-use"]),
            },
            "People across several functions can put work on a named Bot today, with a real install path, a marketplace of connectors, and starter roles. Write-back is often a draft.",
            "E.5 is the lowest at 0.50: work happens in the Grok apps, with Slack and email only as outbound draft cards.",
        ),
    },
    "chatgpt": {
        "type": T(
            "chatgpt",
            {
                "I.1": row("1.00", "People open ChatGPT, type in the message box, and use it for writing, studying, planning, math, coding, and file analysis.", S["chatgpt"]),
                "I.2": row("1.00", "Chat can use uploaded files, web search, projects, plugins, and connected apps such as Drive, Slack, Outlook, and SharePoint.", S["chatgpt-apps"]),
                "I.3": row("1.00", "Scheduled tasks run in the background from Chat. ChatGPT can also run code on spreadsheets. Workspace Agents and Codex are out of scope.", S["chatgpt-use"]),
                "I.4": row("1.00", "A person starts the chat, reviews the result, and can approve app reads or actions before they complete.", S["chatgpt-use"]),
                "I.5": row("1.00", "Projects, custom instructions, memory, plugins, and Business or Enterprise workspaces support repeatable use.", S["chatgpt"]),
                "II.1": row("0.00", "Chat is a person-steered thread. No persistent actor owns an end-to-end business process.", S["chatgpt-use"]),
                "II.2": row("0.25", "The person orchestrates each step by prompting. A scheduled run replays a saved prompt.", S["chatgpt-use"]),
                "II.3": row("0.50", "Chat picks web search, files, and connected apps inside a turn. A person moves the work between turns.", S["chatgpt-use"]),
                "II.4": row("0.50", "Memory, projects, and GPTs persist preferences or a config. There is no durable worker principal.", S["chatgpt-use"]),
                "II.5": row("0.25", "Humans routinely execute the work by chatting.", S["chatgpt-use"]),
                "II.6": row("0.75", "Scheduled tasks run a saved prompt in the background on a schedule. There are no event triggers.", S["chatgpt-use"]),
                **zeros(S["chatgpt-use"], "Organization-level orchestration is not established for the chat product."),
            },
            "The assistant is a person-steered Type I conversation. Scheduled tasks and connected apps assist inside that chat. Workspace Agents and Codex are other products.",
            "II.1 is 0.00: Chat has no actor that owns a process. II.2 and II.5 stay low because a person executes each step by prompting.",
        ),
        "exec": E(
            {
                "E.1": row("1.00", "Anyone can put writing, study, planning, coding, or analysis on Chat. It is a general work surface, not one suite.", S["chatgpt"]),
                "E.2": row("0.75", "Shared projects give invitees edit or chat access to the same chats, files, and instructions. Ordinary chats stay private.", S["chatgpt"]),
                "E.3": row("0.75", "Connected apps can read and take supported actions in Drive, Slack, Outlook, SharePoint, and similar systems, with per-app approval.", S["chatgpt-apps"]),
                "E.4": row("0.75", "A plugin directory and GPTs exist across uses. Many plugins are connectors, and new personal GPT publishing is closed.", S["chatgpt-use"]),
                "E.5": row("0.75", "Work happens on web, desktop, iOS, Android, and Voice.", S["chatgpt-use"]),
                "E.6": row("1.00", "Free, Plus, Business, Edu, and Enterprise paths are documented, including self-serve Business workspaces.", S["chatgpt"]),
                "E.7": row("0.25", "Chat is a blank-canvas assistant. The person writes the job each time; nothing installs or generates a running job.", S["chatgpt-use"]),
            },
            "Anyone can put work on ChatGPT. Shared projects and connectors make it a general company chat surface. It is still a blank canvas, not a path to finished jobs.",
            "E.7 is a blank canvas: no job ships, installs, or is generated ready to run.",
        ),
    },
    "claude": {
        "type": T(
            "claude",
            {
                "I.1": row("1.00", "A person signs in at claude.ai, Desktop, or mobile, types a prompt, and continues a thread.", S["claude"]),
                "I.2": row("1.00", "Chat can use uploads, project knowledge, web search, Research, connectors, skills, and memory.", S["claude"]),
                "I.3": row("0.75", "Research runs multiple searches and code execution can create files in a sandbox. Chat has no scheduled tasks; those sit in Cowork and Code.", S["claude"]),
                "I.4": row("1.00", "The person starts and continues the chat, reviews artifacts, and can require connector approval.", S["claude"]),
                "I.5": row("1.00", "Projects, skills, account instructions, and Team or Enterprise admin support repeatable use.", S["claude"]),
                "II.1": row("0.00", "Chat is person-steered. Plugin sub-agents do not run in chat.", S["claude-plugins"]),
                "II.2": row("0.25", "The person orchestrates each chat. No process-level execution is specified for Chat.", S["claude"]),
                "II.3": row("0.50", "Connectors, skills, and Research are used inside a turn. A person moves the work between turns.", S["claude"]),
                "II.4": row("0.50", "Memory and projects store context. There is no durable Chat worker principal.", S["claude"]),
                "II.5": row("0.25", "Humans execute by chatting.", S["claude"]),
                "II.6": row("0.25", "A person starts every chat. Scheduled Cowork tasks are out of scope for this Chat spec.", S["claude"]),
                **zeros(S["claude"], "The chat sources do not establish organizational orchestration."),
            },
            "Claude chat is a signed-in Type I conversation. Research and sandboxed files run inside that thread. Scheduled tasks, computer use, and sub-agents belong to Cowork or Code.",
            "I.3 is limited once Cowork and Code are excluded. Crossing Type I still needs native background or scheduled autonomy on Chat. Type II is entirely unmet.",
        ),
        "exec": E(
            {
                "E.1": row("1.00", "Claude chat is a general assistant for anyone who can prompt. It is a general work surface, not one suite.", S["claude"]),
                "E.2": row("0.75", "Team and Enterprise projects share with view or edit. Chat shares are snapshots.", S["claude"]),
                "E.3": row("0.75", "Connectors retrieve data and take actions in source systems. Salesforce in Claude is beta.", S["claude"]),
                "E.4": row("0.75", "Anthropic ships plugin marketplaces named Knowledge Work, Life Sciences, Financial Services, and Legal. In chat, only skills and commands run.", S["claude-plugins"]),
                "E.5": row("0.75", "Chat is on web, Desktop, iOS, and Android.", S["claude"]),
                "E.6": row("1.00", "Free signup, Pro, Max, and documented Team and Enterprise admin and SSO are available.", S["claude"]),
                "E.7": row("0.25", "Chat is a blank-canvas assistant. Built-in skills and plugin commands are helpers a person invokes, not running jobs.", S["claude"]),
            },
            "Anyone can put a question on Claude chat. Shared projects and named marketplaces raise coverage. Chat still does not get a team to a running job.",
            "E.7 is a blank canvas. Chat cannot run marketplace sub-agents.",
        ),
    },
    "gemini": {
        "type": T(
            "gemini",
            {
                "I.1": row("1.00", "People open gemini.google.com or the mobile app, enter a prompt, and use Gemini to brainstorm, summarize, and draft.", S["gemini"]),
                "I.2": row("1.00", "Signed-in users can attach files, run Deep Research, and use Connected Apps including Google Workspace.", S["gemini"]),
                "I.3": row("1.00", "Deep Research builds a plan and then a report. Ordinary chats also support recurring scheduled actions.", S["gemini"]),
                "I.4": row("1.00", "Users edit prompts, regenerate, review reports, and must confirm custom MCP writes.", S["gemini"]),
                "I.5": row("1.00", "Gems, notebooks, scheduled actions, and Workspace-admin Gemini Apps access support repeatable use.", S["gemini"]),
                "II.1": row("0.00", "Gemini Apps is a person-steered chat. Spark is an experimental personal task agent, not a process owner.", S["gemini"]),
                "II.2": row("0.25", "The person dispatches each chat or research run.", S["gemini"]),
                "II.3": row("0.50", "Connected Apps and Deep Research are used inside a request. A person moves the work between requests.", S["gemini"]),
                "II.4": row("0.50", "Memory and Gems persist instructions. There is no durable worker principal.", S["gemini"]),
                "II.5": row("0.25", "Humans routinely prompt. Spark explicitly requires user supervision and is experimental.", S["gemini"]),
                "II.6": row("0.75", "Scheduled actions rerun a prompt on a schedule. There are no event triggers.", S["gemini"]),
                **zeros(S["gemini"], "The Gemini Apps pages do not establish organizational orchestration. Workspace and Cloud are other products."),
            },
            "Gemini Apps is a Type I assistant: people steer chat, Deep Research, and scheduled actions. Spark is experimental and was not used to raise Type II.",
            "II.1 is 0.00: Gemini Apps has no actor that owns a process. II.2 and II.5 stay low because a person prompts each step.",
        ),
        "exec": E(
            {
                "E.1": row("1.00", "Gemini Apps is a general assistant for drafting, research, and files. It is a general work surface.", S["gemini"]),
                "E.2": row("0.50", "Work or school accounts exist. Sharing is a Canvas or chat link, a Gem, or an export.", S["gemini"]),
                "E.3": row("0.75", "Workspace can read Gmail, Calendar, Drive, Docs, and Sheets and can create calendar events, Keep notes, and Tasks.", S["gemini"]),
                "E.4": row("0.25", "Gems are user-saved instructions. Custom apps are MCP the buyer wires.", S["gemini"]),
                "E.5": row("0.75", "Surfaces include web, mobile, Gemini in Chrome, and Gemini in Google Messages.", S["gemini"]),
                "E.6": row("1.00", "Personal Google accounts can start free. Work and school use is a documented Workspace-admin path.", S["gemini"]),
                "E.7": row("0.25", "Gemini Apps is a blank-canvas assistant. Deep Research and Gems are not turn-on jobs for several functions.", S["gemini"]),
            },
            "Anyone can chat with Gemini or run Deep Research. Coverage is still a blank canvas with Google-suite reach, not a catalog of company jobs.",
            "E.4 and E.7 are 0.25: no business-function catalog or ready-made jobs. E.2 is single-player sharing.",
        ),
    },
    "grok": {
        "type": T(
            "grok",
            {
                "I.1": row("1.00", "Grok is a back-and-forth assistant on grok.com and iOS or Android for questions, writing, and problems.", S["grok"]),
                "I.2": row("1.00", "Chat can upload files and use built-in connectors for Gmail, Calendar, Drive, Outlook, Teams, and Salesforce, plus live web and X search.", S["grok"]),
                "I.3": row("0.75", "Multi-agent mode and connector actions can run inside one human-started thread. This spec has no scheduled tasks for the assistant.", S["grok"]),
                "I.4": row("1.00", "The person starts and continues the thread and can set custom instructions.", S["grok"]),
                "I.5": row("1.00", "Memory, custom instructions, conversation history, and Business or Enterprise workspaces support repeatable use.", S["grok"]),
                "II.1": row("0.00", "The assistant is a person-steered chat. Durable teammates are Grok Bot, which is out of scope.", S["grok"]),
                "II.2": row("0.25", "The person orchestrates each conversation.", S["grok"]),
                "II.3": row("0.50", "Connectors run when a chat question relates to a service. A person moves the work between turns.", S["grok"]),
                "II.4": row("0.50", "Memory persists preferences. The persistent cloud-computer worker is Grok Bot, out of scope.", S["grok"]),
                "II.5": row("0.25", "Humans routinely prompt.", S["grok"]),
                "II.6": row("0.25", "No schedules or background process continuity are specified for the Grok assistant.", S["grok"]),
                **zeros(S["grok"], "The assistant pages do not establish organizational orchestration. Grok Bot is a different spec."),
            },
            "Grok the assistant can search, write, and use connectors in a thread the person steers. Multi-agent mode answers a hard question. It does not run a process, and Grok Bot must not be borrowed to raise this score.",
            "I.3 is turn-bound once Bot and Build are excluded. Type II is entirely unmet.",
        ),
        "exec": E(
            {
                "E.1": row("1.00", "Grok is a general assistant for chat, search, writing, and files. It is a general work surface.", S["grok"]),
                "E.2": row("0.50", "Business and Enterprise team workspaces exist. Sharing is a member-restricted link after the fact.", S["grok"]),
                "E.3": row("0.75", "Built-in connectors document read and write for Gmail, Calendar, Drive, Outlook, Teams, and Salesforce.", S["grok"]),
                "E.4": row("0.25", "Coverage grows through a connector catalog and custom MCP, which the buyer wires into a blank chat.", S["grok"]),
                "E.5": row("0.50", "Surfaces are grok.com plus iOS and Android. No desktop app or workplace-chat surface is specified for this assistant.", S["grok"]),
                "E.6": row("1.00", "Free start is documented. Business license assign and Enterprise SSO are documented in the console.", S["grok"]),
                "E.7": row("0.25", "The assistant is a blank canvas. The buyer writes every job in chat.", S["grok"]),
            },
            "Anyone can put writing or research on Grok. Connectors can reach mail and Salesforce. It is still a single-player blank canvas.",
            "E.4 and E.7 are 0.25. E.5 is web and mobile only.",
        ),
    },
    "chatgpt-work": {
        "type": T(
            "chatgpt-work",
            {
                "I.1": row("1.00", "People open Agents in the ChatGPT sidebar and run a published agent with @ or from Agents.", S["chatgpt-work"]),
                "I.2": row("1.00", "The builder adds tools, apps such as Calendar, Drive, Slack, and SharePoint, custom MCP servers, skills, and files.", S["chatgpt-work"]),
                "I.3": row("1.00", "A published agent runs its configured task in ChatGPT, in Slack, on a schedule, or from an API trigger.", S["chatgpt-work"]),
                "I.4": row("1.00", "Builders preview before create and set write-action approvals that default to Always ask.", S["chatgpt-work"]),
                "I.5": row("1.00", "Agents can be shared, listed in the organization directory, scheduled, and deployed to Slack.", S["chatgpt-work"]),
                "II.1": row("0.50", "A published agent runs a designed task on schedules, in Slack, or from an API trigger. There is no persistent actor put in charge of a process.", S["chatgpt-work"]),
                "II.2": row("1.00", "A published agent finishes its configured steps without anyone typing each one. Write approvals can be set to Never ask.", S["chatgpt-work"]),
                "II.3": row("1.00", "During a run the agent selects the apps, MCP servers, skills, and files it was given.", S["chatgpt-work"]),
                "II.4": row("0.50", "A published agent keeps instructions, tools, files, and optional memory. Agent-owned app accounts exist, but there is no agent principal.", S["chatgpt-work"]),
                "II.5": row("0.75", "Write approvals, RBAC, admin review of activity, and compliance export govern task runs.", S["chatgpt-work"]),
                "II.6": row("1.00", "A published agent starts from a ChatGPT schedule, a Slack schedule, or an API trigger with no person starting each run.", S["chatgpt-work"]),
                **zeros(S["chatgpt-work"], "The article does not establish organization-level orchestration or a governance-only human role."),
            },
            "Workspace Agents run a task a builder configured, on a schedule or from an API, with tools and approvals and no person at each step. There is still no persistent actor that owns a process.",
            "II.1 and II.4 block Type II: a scheduled agent runs tasks, and it has no principal of its own.",
        ),
        "exec": E(
            {
                "E.1": row("1.00", "Workspace agents are a general ChatGPT work surface for Business, Enterprise, and Edu teams across functions.", S["chatgpt-work"]),
                "E.2": row("0.75", "The owner shares Can chat or Can edit, lists the agent in the team directory, and can put it in a Slack channel.", S["chatgpt-work"]),
                "E.3": row("0.75", "Connected apps include Calendar, Drive, Slack, and SharePoint, with write actions that default to Always ask.", S["chatgpt-work"]),
                "E.4": row("0.50", "Creation can start from a template. The team directory holds organization-built agents, not a first-party job marketplace.", S["chatgpt-work"]),
                "E.5": row("0.75", "Surfaces are ChatGPT, Slack, and an API trigger.", S["chatgpt-work"]),
                "E.6": row("0.75", "Admins get RBAC for use, build, publish, and Slack. The path is limited to Business, Enterprise, and Edu.", S["chatgpt-work"]),
                "E.7": row("0.75", "A prompt becomes a draft plan and then an agent, and templates start other jobs. Apps still need connecting and the builder refines the draft.", S["chatgpt-work"]),
            },
            "A workspace can generate agents from a prompt or a template and share them across ChatGPT and Slack. Coverage grows as far as the workspace builds.",
            "E.4 is the lowest at 0.50: templates and an organization directory, not a marketplace.",
        ),
    },
    "claude-cowork": {
        "type": T(
            "claude-cowork",
            {
                "I.1": row("1.00", "On desktop, the person selects Cowork, describes the task, reviews the plan, and lets it run. Cowork is on Pro, Max, Team, and Enterprise.", S["claude-cowork"]),
                "I.2": row("1.00", "Cowork reads and writes local files, loads connectors, skills, and plugins, and can use the built-in browser when the desktop app is open.", S["claude-cowork"]),
                "I.3": row("1.00", "Claude splits complex work into smaller tasks with parallel workstreams and returns finished files.", S["claude-cowork"]),
                "I.4": row("1.00", "The person starts, steers, and reviews tasks, with Manual, Auto, or Skip approval modes.", S["claude-cowork"]),
                "I.5": row("1.00", "Projects keep folders, instructions, and memory. Scheduled tasks run on all paid plans.", S["claude-cowork"]),
                "II.1": row("0.25", "The unit of work is a session or a scheduled prompt, one task per run, with no persistent actor owning a process.", S["claude-cowork"]),
                "II.2": row("1.00", "Inside a task, Claude progresses through steps with no person between them. Auto mode leaves approvals to the person.", S["claude-cowork"]),
                "II.3": row("0.75", "Claude tries connectors first, then the browser, then computer use. Computer use is beta and is not on Team or Enterprise.", S["claude-cowork"]),
                "II.4": row("0.25", "Each cloud sandbox is created at start and destroyed at end. A cowork session is not a process actor.", S["claude-cowork"]),
                "II.5": row("0.75", "Approval modes, forwarded permission prompts, and phone notifications let a person supervise a task.", S["claude-cowork"]),
                "II.6": row("0.75", "Scheduled tasks run remotely on a cadence when the computer is asleep. Each run is its own Cowork session.", S["claude-cowork"]),
                **zeros(S["claude-cowork"], "The cited pages do not establish organizational orchestration. Claude Code's schedules are a different product."),
            },
            "A person describes an outcome; Cowork plans and runs a multi-step session, then returns files. Scheduled tasks make that repeatable. A session is not a persistent AI actor that owns a business process. Dispatch is limited beta.",
            "II.1 and II.4: a cowork session or scheduled prompt is not a persistent actor that owns a process.",
        ),
        "exec": E(
            {
                "E.1": row("1.00", "Cowork produces documents, spreadsheets, presentations, and research for people on paid plans, across functions. It is not tied to one suite.", S["claude-cowork"]),
                "E.2": row("0.50", "Team and Enterprise exist. Sessions cannot be shared; artifacts can. Work stays single-player.", S["claude-cowork"]),
                "E.3": row("0.75", "Connectors can retrieve data and take actions. Cowork reads and writes local files. Computer use is beta and omitted on Team and Enterprise.", S["claude-cowork"]),
                "E.4": row("0.75", "There is a Connectors Directory, a Skills catalog, and a plugins marketplace. Shipped Anthropic skills stay in the office-document family.", S["claude-cowork"]),
                "E.5": row("0.75", "Desktop is the full surface. Web and mobile also run Cowork and are beta.", S["claude-cowork"]),
                "E.6": row("0.75", "Cowork is on by default on paid plans, with Team and Enterprise owner toggles. Enterprise cloud sessions start off.", S["claude-cowork"]),
                "E.7": row("0.25", "The person describes an outcome in a blank Cowork session. Anthropic skills help with office file types.", S["claude-cowork"]),
            },
            "Paid Claude users can put knowledge work on Cowork from the desktop app, with connectors, skills, and plugins. Sessions cannot be shared. The product is a general assistant, not a set of finished jobs.",
            "E.7 is a blank canvas. E.2 stays at team-account sharing because sessions are not multiplayer.",
        ),
    },
    "microsoft-365-copilot": {
        "type": T(
            "microsoft-365-copilot",
            {
                "I.1": row("1.00", "People use Copilot at m365copilot.com, in the Copilot app, and inside Word, Excel, PowerPoint, Outlook, Teams, and related apps.", S["m365"]),
                "I.2": row("1.00", "Premium grounds responses in Microsoft Graph and Work IQ within the signed-in user's permissions.", S["m365"]),
                "I.3": row("1.00", "Cowork for work or school is generally available and carries out multi-step work such as drafting mail and creating Office files.", S["m365-cowork"]),
                "I.4": row("1.00", "In Word, suggested edits are not written until the user approves. Cowork asks before sensitive actions.", S["m365-cowork"]),
                "I.5": row("1.00", "Scheduled prompts run in Teams, Office.com chat, and Outlook. Admins deploy agents from Agent Store.", S["m365"]),
                "II.1": row("0.25", "Cowork, Researcher, and declarative agents complete one task per run, started by a person, a schedule, or an event. No persistent actor owns a process.", S["m365"]),
                "II.2": row("1.00", "Cowork progresses a multi-step plan across mail, files, and meetings, asking only before sensitive actions.", S["m365-cowork"]),
                "II.3": row("0.75", "Cowork ships skills for Word, Excel, PowerPoint, Email, Scheduling, Meetings, and Teams. Federated connector write-back is not yet available.", S["m365-cowork"]),
                "II.4": row("0.25", "Cowork processes files in a temporary isolated environment removed when the task ends. Memory is preview.", S["m365-cowork"]),
                "II.5": row("0.75", "Cowork approvals, Purview, Conditional Access, and unified audit logging are native.", S["m365-cowork"]),
                "II.6": row("1.00", "Scheduled prompts and Cowork scheduled or event-driven tasks start with no person starting each run.", S["m365-cowork"]),
                **zeros(S["m365"], "The dossier does not establish organization-level orchestration, and custom engine A2A needs separate hosting."),
            },
            "Copilot is embedded in Microsoft 365 apps. Cowork can run scheduled or event-driven tasks. Those are human-designed tasks inside the suite, not a persistent actor that owns a business process.",
            "II.1 and II.4: scheduled Cowork and store agents are not a persistent actor that owns a process.",
        ),
        "exec": E(
            {
                "E.1": row("0.75", "Copilot sits in Word, Excel, PowerPoint, Outlook, Teams, SharePoint, OneDrive, and OneNote. That is several functions with a real limit: one suite.", S["m365"]),
                "E.2": row("0.75", "Copilot works in Teams chats, channels, and meetings. Admins assign Agent Store agents to users or groups.", S["m365"]),
                "E.3": row("0.75", "Cowork reads and writes Microsoft 365 mail, calendar, files, and Teams. Synced connectors index many external sources; federated write-back is not yet available.", S["m365-cowork"]),
                "E.4": row("0.75", "Agent Store lists Microsoft, partner, and organization agents. Researcher and Analyst are preinstalled. The catalog is limited to the Microsoft 365 family.", S["m365"]),
                "E.5": row("0.75", "Surfaces include the Copilot app on web, Windows, macOS, iOS, and Android, plus Word, Excel, Outlook, and Teams.", S["m365"]),
                "E.6": row("1.00", "Admins assign licenses, use Copilot controls, and deploy or block agents from the Microsoft 365 admin center.", S["m365"]),
                "E.7": row("0.75", "Ready-made jobs include in-app draft and summarize, Outlook triage, Teams meeting summaries, Researcher, Analyst, and Cowork skills. That is one suite.", S["m365-cowork"]),
            },
            "An eligible Microsoft 365 tenant can put mail, documents, meetings, and Teams work on Copilot as it ships, with Agent Store and admin controls. Coverage stays inside one suite.",
            "E.1, E.3, E.4, E.5, and E.7 are capped by one suite. Preview SharePoint Copilot and unreadied federated write-back cannot lift those grades to 1.00.",
        ),
    },
    "notion": {
        "type": T(
            "notion",
            {
                "I.1": row("1.00", "Notion Agent opens from the face, sidebar, or shortcut and works on the current page, workspace, and connected apps.", S["notion-agent"]),
                "I.2": row("1.00", "It searches the workspace and connectors such as Slack, Drive, SharePoint, GitHub, Linear, Gmail, Outlook, and Calendar.", S["notion-agent"]),
                "I.3": row("0.50", "Notion Agent edits pages and databases and can act in Slack, Gmail, and Calendar in one task. The spec does not say it picks each next step from the last result and continues until done.", S["notion-agent"]),
                "I.4": row("0.25", "A person starts Notion Agent and sees the result, and Gmail writes ask for confirmation. The spec documents no way to stop a running task, which blocks the higher checks.", S["notion-agent"]),
                "I.5": row("1.00", "Custom Agents run on recurring schedules and Notion, Slack, mail, and calendar events after they are saved.", S["notion"]),
                "II.1": row("0.50", "Custom Agents are shared workflows that run on triggers. The spec does not show one put in charge of a process and carrying each case to an outcome.", S["notion"]),
                "II.2": row("1.00", "After setup they run in the background on the saved triggers, with no person between steps.", S["notion"]),
                "II.3": row("1.00", "During a run the agent uses the pages, databases, Slack, mail, calendar, MCP, and other Custom Agents it was granted.", S["notion"]),
                "II.4": row("0.75", "Custom Agents have their own Notion permissions. MCP and mail connections use the authenticator's credentials.", S["notion"]),
                "II.5": row("0.75", "Activity, version history, confirmation settings, and Enterprise audit logs exist.", S["notion"]),
                "II.6": row("1.00", "Recurring schedules plus Notion, Slack, mail, and calendar triggers start runs without a person starting each one.", S["notion"]),
                **zeros(S["notion"], "The article does not show agents allocating work that was not triggered, or a governance-only human role."),
            },
            "Custom Agents run a workflow on their own when a schedule or an event fires, with their own Notion permissions. The spec does not document stopping a running task or a self-directed task loop, so the Type I floor is incomplete.",
            "I.3 and I.4 block the Type I floor: no documented stop control and no stated self-directed loop. Beyond that, II.1 blocks Type II because triggered workflows are not shown owning a process, and II.4 is not a full principal because connections use the authenticator's credentials.",
        ),
        "exec": E(
            {
                "E.1": row("0.75", "Notion AI runs inside one Notion workspace on pages, databases, and connected apps. Several functions can use that suite.", S["notion-agent"]),
                "E.2": row("0.75", "Pages and Custom Agents are shared like Notion pages. Notion Agent acts as the signed-in user.", S["notion"]),
                "E.3": row("0.75", "Native write is Notion pages and databases. Slack, Gmail, and Calendar can write after connect. Many connectors are search.", S["notion-agent"]),
                "E.4": row("0.50", "Skills and Custom Agent templates exist. The company still builds the agents.", S["notion"]),
                "E.5": row("0.75", "Work is in Notion web, desktop, and mobile, with Slack posts and triggers.", S["notion-agent"]),
                "E.6": row("1.00", "Business and Enterprise document Settings, creation policy, credits, and onboarding.", S["notion"]),
                "E.7": row("0.75", "Create with AI chat generates a Custom Agent's instructions, triggers, and access for review, and templates start others. Coverage stays inside the Notion workspace.", S["notion"]),
            },
            "A Business or Enterprise workspace can generate Custom Agents from chat or templates and share them on Notion pages and Slack. Coverage stays inside that workspace suite.",
            "E.4 is the lowest at 0.50: templates and skills, not a marketplace.",
        ),
    },
    "dust": {
        "type": T(
            "dust",
            {
                "I.1": row("1.00", "Members talk to agents in the workspace with @, or unmentioned messages go to the workspace default agent.", S["dust-intro"]),
                "I.2": row("1.00", "Managed connections include Google Drive, Notion, Confluence, Slack, Salesforce, and Zendesk. Tools can search and write in those apps.", S["dust-intro"]),
                "I.3": row("1.00", "Agents are a first-class object people talk to. Triggers can start a conversation, and an agent can answer and take action.", S["dust-intro"]),
                "I.4": row("1.00", "A person can inspect live tool calls, send a message while the agent runs, or stop it. Governance settings control who publishes agents.", S["dust-admin"]),
                "I.5": row("1.00", "Published agents, skills, schedules, webhooks, Slack auto-reply, and automation platforms are documented repeatable paths.", S["dust-triggers"]),
                "II.1": row("0.50", "Schedules and webhooks start a designed agent run. No persistent actor is put in charge of a process.", S["dust-intro"]),
                "II.2": row("1.00", "A triggered run progresses through its tool calls with no person between steps.", S["dust-triggers"]),
                "II.3": row("1.00", "An agent with several capabilities selects and combines its tools during the run.", S["dust-intro"]),
                "II.4": row("0.50", "Agent Memory is per-user for that agent. Wake-ups run with the authentication of the user whose message created them.", S["dust-admin"]),
                "II.5": row("0.75", "Live action inspection, stop, email Accept or Reject, and Enterprise audit logs exist.", S["dust-admin"]),
                "II.6": row("1.00", "Agent Builder schedules and webhook triggers start runs with no person starting each one.", S["dust-triggers"]),
                **zeros(S["dust-intro"], "The cited pages do not show agents determining work, coordinating without a person, or closing an operational loop."),
            },
            "Dust lets a company build and run agents on its tools, with triggers and admin control. The documented actor is still an agent a person dispatches or a trigger starts. It is not shown owning a business process.",
            "II.1 and II.4 block Type II: triggered agents run tasks, and memory and credentials stay with the user who created the run.",
        ),
        "exec": E(
            {
                "E.1": row("1.00", "Dust is a company workspace for custom agents on shared knowledge and many vendors' tools. Several functions can put work on it.", S["dust"]),
                "E.2": row("0.75", "A Pod is a shared workspace for conversations, tasks, and files. Slack and Teams threads call @dust.", S["dust-intro"]),
                "E.3": row("0.75", "Connections index many systems. Tools can write Notion, Slack, GitHub, and draft Gmail or Zendesk.", S["dust"]),
                "E.4": row("0.50", "Templates and default skills exist. The company still builds the agents.", S["dust-intro"]),
                "E.5": row("1.00", "Work runs in the web app, Slack, Teams, email, Zendesk, and the Dust API.", S["dust"]),
                "E.6": row("1.00", "Business is self-serve. Admins, SSO, and roles are documented.", S["dust-admin"]),
                "E.7": row("0.75", "Sidekick drafts instructions and a working configuration and recommends tools, skills, and models. Templates and Convert to agent start other jobs. Sidekick cannot set triggers.", S["dust-sidekick"]),
            },
            "A company can generate Dust agents with Sidekick, share them in Pods and Slack, and reach connected systems. Coverage depends on the agents the workspace builds.",
            "E.4 is the lowest at 0.50: templates and default skills, not a marketplace.",
        ),
    },
    "glean": {
        "type": T(
            "glean",
            {
                "I.1": row("1.00", "Anyone with a work account uses Chat as the default surface. Search and the Agent Library sit beside it.", S["glean"]),
                "I.2": row("1.00", "Connectors index company apps with permission mirroring. Tools can create tickets, post comments, and update fields.", S["glean"]),
                "I.3": row("1.00", "Auto mode agents run research, analysis, summarization, and drafting. Chat has an agentic planner and Deep Research.", S["glean-auto"]),
                "I.4": row("1.00", "Write actions in the web app pause for approval by default. Builders preview and debug before publish.", S["glean"]),
                "I.5": row("1.00", "The Agent Library lists runnable agents. Schedule and content triggers start repeats after an admin enables them.", S["glean-lib"]),
                "II.1": row("0.50", "Agents are reusable solutions a builder publishes from a goal and tools. That is not a documented owned business process.", S["glean"]),
                "II.2": row("1.00", "Auto mode selects tools and progresses toward the outcome, and workflow mode runs its steps, with no person between steps.", S["glean-auto"]),
                "II.3": row("1.00", "Auto mode selects tools and can use the Task tool for sub-agents during the run.", S["glean-auto"]),
                "II.4": row("0.75", "Independent Agents are in beta. They have a dedicated profile and can use admin-approved service credentials.", S["glean"]),
                "II.5": row("0.75", "Web write actions wait for confirmation. Admins can allow unattended writes. Scheduled agents can be paused.", S["glean"]),
                "II.6": row("1.00", "Schedule and content triggers start runs with no person starting each one. Admins enable them, and some content-trigger sources are experimental.", S["glean"]),
                **zeros(S["glean"], "The docs do not show agents rewriting the operating model or limiting humans to governance."),
            },
            "Glean can run a designed agent on a schedule or a content trigger, and Auto mode can pick tools inside that request. Independent Agents add a system profile and are beta. The company still designs the work.",
            "II.1 blocks Type II: Independent Agents are beta and do not show a persistent actor owning an end-to-end business process. II.4 stays beta.",
        ),
        "exec": E(
            {
                "E.1": row("1.00", "Anyone on the tenant can search, chat, and run agents. Templates list Engineering, HR, IT, Marketing, Sales, and Support across many vendors' apps.", S["glean-lib"]),
                "E.2": row("0.75", "Users share chats and Projects. Slack Public Mode and Independent Agents can work in a shared channel. Independent Agents are beta.", S["glean"]),
                "E.3": row("0.75", "Native connectors cover mail, calendar, CRM, tickets, and files. Tools can write. Deep Research is read-only.", S["glean"]),
                "E.4": row("0.50", "The Agent Library and templates cover several job categories. Those are designed agents, not a marketplace you install without building.", S["glean-lib"]),
                "E.5": row("1.00", "Surfaces include the web app, desktop, mobile, Slack, Teams, Zendesk or ServiceNow, MCP, and the Web SDK.", S["glean"]),
                "E.6": row("1.00", "Sign-in is the company IdP. The Admin Console documents connectors, SSO, RBAC, and feature enablement.", S["glean"]),
                "E.7": row("0.75", "A person describes an outcome in Builder Assistant and reviews the generated agent. Templates by function supply prompts, tools, and logic. Admins still enable tools and triggers.", S["glean-auto"]),
            },
            "A Glean tenant can generate agents from a description or a function template and run them across connected apps and workplace chat.",
            "E.4 is the lowest at 0.50: a designed-agent directory, not a marketplace open to third parties.",
        ),
    },
    "agentforce": {
        "type": T(
            "agentforce",
            {
                "I.1": row("1.00", "Agents are a standard part of Salesforce in the Lightning Agentforce panel, the mobile app, and Slack, and they update records, not only answer.", S["agentforce"]),
                "I.2": row("1.00", "Agents use uploaded files, CRM data and Data Libraries, and actions in Salesforce, Slack, email, and MCP tools, and they honor licenses, permissions, field-level security, and sharing.", S["agentforce"]),
                "I.3": row("1.00", "After an action runs the agent decides whether to run another, ask again, or reply, up to seven loops, and it can update records without a person approving each step.", S["agentforce"]),
                "I.4": row("0.25", "A person starts a session and sees the reply. The spec documents no way to stop or interrupt a running agent, only escalation to a live agent.", S["agentforce"]),
                "I.5": row("1.00", "Agents are saved and versioned org metadata, shared across the org, and admins manage them with the Manage AI Agents permission.", S["agentforce"]),
                "II.1": row("1.00", "A Service agent is assigned messaging and email channels, takes each conversation from its inbound Omni-Channel flow, answers common inquiries, and escalates complex ones.", S["agentforce-types"]),
                "II.2": row("0.75", "Atlas routes, runs actions, and replies with no person between steps, and escalation hands off exceptions. Agents run with or without a human in the loop.", S["agentforce"]),
                "II.3": row("1.00", "During a conversation the agent chooses the actions the task needs across Salesforce actions, MCP tools, and other agents in the org.", S["agentforce"]),
                "II.4": row("0.75", "A named agent persists as org metadata with Agent Memory across conversations. It acts within the user's permissions and has no credentials of its own.", S["agentforce"]),
                "II.5": row("0.50", "Session tracing, analytics, and Omni Supervisor show sessions and active calls. Escalation transfers the conversation instead of resuming it after a person responds.", S["agentforce"]),
                "II.6": row("0.75", "Inbound flows route each conversation to the agent, and invocable actions run agents from Flow or Apex for background or event-driven work. Schedules are not documented.", S["agentforce"]),
                **zeros(S["agentforce"], "Multi-agent orchestration and guardrails are described. The spec does not show agents creating or allocating the org's work, or people in governance only."),
            },
            "Agentforce agents are standard Salesforce features that reason over CRM data and run record actions. A Service agent takes conversations from its own channels and escalates exceptions. The spec documents no way to stop a running agent, so the Type I floor is incomplete.",
            "I.4 blocks the Type I floor: the spec documents starting a session and escalation, but no stop or interrupt control. Type II is otherwise close; II.5 lacks an approval that resumes the same run.",
        ),
        "exec": E(
            {
                "E.1": row("0.75", "Help lists Employee, Lead Nurturing, Sales Coach, Service Agent, Service Assistant, and Setup agents. That is several functions inside one Salesforce suite.", S["agentforce-types"]),
                "E.2": row("0.50", "A Salesforce org is a team account. Slack and Omni-Channel escalation can hand a conversation to a person. The work itself is a single conversation.", S["agentforce"]),
                "E.3": row("0.50", "Native read and write is Salesforce records, knowledge, files, and Service Email. Other systems need custom actions or MCP.", S["agentforce"]),
                "E.4": row("0.50", "Agents start from templates or standard subagents. There is no first-party marketplace in the spec.", S["agentforce-types"]),
                "E.5": row("1.00", "Employees work with agents in Lightning, the mobile app, and Slack. Customers reach Service agents on messaging, email, and voice. The Agent API and mobile SDKs embed agents in other software.", S["agentforce"]),
                "E.6": row("1.00", "A builder turns Agentforce on in Setup, creates an agent from a template, and activates it. Manage AI Agents and Studio permissions let an org roll it out without services. Required add-on licenses vary by type.", S["agentforce"]),
                "E.7": row("0.75", "Shipped types include Employee, Lead Nurturing, Sales Coach, Service Agent, Service Assistant, and Setup. That is one Salesforce family.", S["agentforce-types"]),
            },
            "A Salesforce org can turn on service, sales, and employee agents from Setup and reach them in Lightning, Slack, customer channels, and the API. Write-back, sharing, and the catalog stay inside the Salesforce suite.",
            "E.2, E.3, and E.4 stay partial: a conversation in one org, Salesforce records, and templates rather than a marketplace.",
        ),
    },
    "sierra": {
        "type": T(
            "sierra",
            {
                "I.1": row("1.00", "One agent handles customer conversations on voice, chat, email, and WhatsApp as the product's normal work.", S["sierra"]),
                "I.2": row("1.00", "The agent connects to knowledge and systems of record such as order management and CRM so it can complete customer tasks.", S["sierra"]),
                "I.3": row("1.00", "Product pages describe end-to-end customer jobs such as a claim, a return, or a mortgage, plus Horizon playbooks that run over weeks.", S["sierra"]),
                "I.4": row("1.00", "Supervisors can correct, block, or escalate live responses, and the conversation continues. Ghostwriter shows a build for review before it goes live.", S["sierra-aiuc"]),
                "I.5": row("1.00", "Agent Studio versions journeys, uses roles and environments, and moves snapshots from QA to production.", S["sierra-studio"]),
                "II.1": row("0.75", "One agent takes each customer conversation from its channels and carries journeys such as a claim or renewal to an outcome, with Horizon playbooks over weeks. It owns one kind of process.", S["sierra-horizon"]),
                "II.2": row("1.00", "A journey or Horizon playbook progresses without a person at each step. Escalation handles exceptions.", S["sierra-horizon"]),
                "II.3": row("1.00", "During a conversation the agent selects the integrations and tools it was configured with.", S["sierra-studio"]),
                "II.4": row("0.50", "Context Engine keeps permissioned customer memory across channels. That is a brand agent, not an employee principal with its own credentials.", S["sierra-horizon"]),
                "II.5": row("0.75", "Monitors, traces, and contact-center handoff let people observe conversations and take exceptions. The spec does not show a paused run resuming after a person approves.", S["sierra-live"]),
                "II.6": row("1.00", "Inbound conversations start runs, and Horizon signals start proactive engagement from customer behavior or milestones.", S["sierra-horizon"]),
                **zeros(S["sierra"], "The product pages do not show agents determining the company's operational work or leaving people in governance only."),
            },
            "Sierra natively runs customer conversations across channels, carrying designed journeys to an outcome with review, escalation, and long-running Horizon playbooks. It is close to owning the customer-conversation process.",
            "II.4 blocks Type II: Context Engine memory belongs to a brand agent, not a principal with its own credentials. II.1 is limited to one kind of process.",
        ),
        "exec": E(
            {
                "E.1": row("0.50", "Sierra is a customer-facing agent for voice, chat, email, SMS, messaging, and ChatGPT. Other company functions have no native path.", S["sierra"]),
                "E.2": row("0.50", "Live Assist puts the same agent next to a care representative. Contact-center handoff adds a person. The conversation itself is still one customer thread.", S["sierra-live"]),
                "E.3": row("0.75", "The site describes 40+ integrations for knowledge bases, systems of record, and contact centers, including completing a claim or a return.", S["sierra-studio"]),
                "E.4": row("0.25", "The Integration Library adds connectors for the same customer-conversation craft. There is no marketplace of jobs for other functions.", S["sierra-studio"]),
                "E.5": row("0.50", "Customer work runs on voice, chat, email, SMS, WhatsApp, and ChatGPT, and Live Assist serves care representatives. Employees do not work with the agent from Slack or Teams.", S["sierra"]),
                "E.6": row("0.75", "Sierra is obtained through an enterprise partnership, with documentation, training, and support, and Agent Studio has roles and environments. A forward-deployed team is part of the offer, so rollout without services is not shown.", S["sierra"]),
                "E.7": row("0.50", "The shipped job is customer conversation, including ready-made channel coverage. Other functions are not turn-on jobs.", S["sierra"]),
            },
            "A company can put customer conversations on Sierra across many channels, with integrations into CRM and order systems. Coverage stays that one function. Adoption is an enterprise engagement, not self-serve.",
            "E.4 is a support-craft integration library. E.1 and E.7 stay at one business function.",
        ),
    },
    "plateforme": {
        "type": T(
            "plateforme",
            {
                "I.1": row("1.00", "Chat is the work surface. Ask, Run, and Build sit in the normal loop for every member.", S["plateforme"]),
                "I.2": row("1.00", "Runs use skills, applications, web, documents, projects, files, operator memory, and the chat's computer.", S["plateforme"]),
                "I.3": row("1.00", "Run executes with tools and a computer. Build creates and releases agents, skills, and applications.", S["plateforme"]),
                "I.4": row("1.00", "People start, stop, and regenerate turns, approve mutating tools and Build tools, and resolve Issues.", S["plateforme"]),
                "I.5": row("1.00", "Released assets, projects, teams, the marketplace, and organization and enterprise admin support repeatable use.", S["plateforme"]),
                "II.1": row("1.00", "A licensed Operator is put in charge of work: its primary agent answers mentions, schedules, webhooks, and events in its chats, and Actions run released workflows end to end.", S["plateforme"]),
                "II.2": row("1.00", "An Action moves from queued to completed through its steps. Human approval steps are optional in the workflow.", S["plateforme"]),
                "II.3": row("1.00", "The operator uses bound applications, skills, scripts, its computer, and memory during a run. Workflows combine agents, operators, and applications.", S["plateforme"]),
                "II.4": row("1.00", "An Operator is its own principal with grants, operator-wide memory, write-only secrets and static credentials, repositories, and a persistent volume.", S["plateforme"]),
                "II.5": row("1.00", "Approvals, Issues, cancel, the runs list, attached chats, the feed, dashboards, and the audit log let people supervise.", S["plateforme"]),
                "II.6": row("1.00", "Mentions, schedules, signed webhooks, workspace events, automatic replies, and workflow triggers start work with no person starting each run.", S["plateforme"]),
                "III.1": row("0.50", "Operators and Actions run on triggers without anyone typing. People arrange which work runs that way.", S["plateforme"]),
                "III.2": row("0.25", "A workflow routes steps to operators, and an operator decides whether to auto-reply. The routing is a designed graph.", S["plateforme"]),
                "III.3": row("0.50", "Several operators can be granted on one channel, and workflow steps span operators. People arrange that coordination.", S["plateforme"]),
                "III.4": row("0.50", "Events trigger Actions, dashboards observe outcomes, and operator memory carries notes into later runs. People close the loop.", S["plateforme"]),
                "III.5": row("0.25", "Workflow conditions branch inside a designed graph. Changing the graph goes through a person's Build turn.", S["plateforme"]),
                "III.6": row("0.50", "Budgets, caps, permissions, the audit log, and the enterprise tenant support governance. The spec does not show routine supervision becoming exceptional.", S["plateforme"]),
            },
            "Plateforme natively supports Type II: a licensed Operator is a persistent principal with memory, credentials, a computer, and triggers, and Actions run released workflows end to end under human supervision. Type III has primitives: several operators per channel, event-driven Actions, dashboards, and memory. People still arrange them.",
            "III.2 and III.5 are lowest: operators do not decide which work happens next, and changing a workflow still goes through a person.",
        ),
        "exec": E(
            {
                "E.1": row("1.00", "Any team can put work on agents, operators, workflows, and dashboards in an organization workspace. It is not tied to one suite or craft.", S["plateforme"]),
                "E.2": row("1.00", "Channels hold several people and operators in one thread, with grants, projects, and chats attached to Actions.", S["plateforme"]),
                "E.3": row("0.75", "Applications, including Slack and mail, install from the marketplace as deployments over HTTP APIs and databases or as connections to remote tool servers, with approvals on writes. Reach comes through the catalog, not shipped jobs.", S["plateforme"]),
                "E.4": row("1.00", "A first-party marketplace lists agents, skills, applications, workflows, and reports. Verified and community publishers and any workspace can distribute into it.", S["plateforme"]),
                "E.5": row("0.75", "Work happens in the web product and through a public API that prompts agents directly. Slack and mail come through marketplace applications, not first-party channels.", S["plateforme"]),
                "E.6": row("1.00", "Free and Community start, a Team trial, roles, base permissions, teams, checkout, and enterprise administration are specified.", S["plateforme"]),
                "E.7": row("0.75", "Agents and workflows install from the marketplace with Install missing, Build generates agents, skills, and applications, and a chat can be promoted to a workflow. Secrets, bindings, and operators still need setting up.", S["plateforme"]),
            },
            "An organization can put work from any function on Plateforme, share it with people and operators in one thread, install or generate the next job, and prompt agents from the web product, the public API, or marketplace Slack and mail applications.",
            "E.3, E.5, and E.7 are the lowest at 0.75: reach and channels come through catalog applications rather than shipped jobs or first-party channels, and installed or generated jobs still need secrets, bindings, and operators.",
        ),
    },
}
def capped(rows: dict, rubric) -> dict:
    """Apply the rubric's cross-criterion caps to the fixture grades and say so in the evidence."""
    grades = {key: rows[key][0] for key in rubric.keys}
    notes = apply_cross_caps(rubric, grades)
    out = dict(rows)
    for key, items in notes.items():
        _grade, evidence, source = rows[key]
        out[key] = (grades[key], f"{evidence} Scorer: {' '.join(items)}", source)
    return out


def table(rows: dict, keys: list[str]) -> str:
    lines = ["| Criterion | Grade | Evidence | Source |", "| --------- | ----: | -------- | ------ |"]
    for key in keys:
        grade, evidence, source = rows[key]
        lines.append(f"| {key} | {grade:.2f} | {evidence} | {source} |")
    return "\n".join(lines)


def type_report(slug: str, spec: dict) -> tuple[dict, str]:
    rows = capped(spec["type"]["rows"], TYPE_RUBRIC)
    scored = type_score(TYPE_RUBRIC, {key: rows[key][0] for key in TYPE_KEYS})
    floor, score = scored.floor, scored.score
    criteria = {key: num(rows[key][0], 2) for key in TYPE_KEYS}
    body = f"""> **Intelligence Scale capability: {score:.1f} / 3.0**

{interpret(floor, score)}

{spec['type']['summary']}

Mock fixture for {DATE}, graded at criterion level from `src/specs/{slug}.md`. The shared scorer applies the cross-criterion caps and the formula.

{table(rows, TYPE_KEYS)}

* **Completed floor:** {floor}
* **Next Type raw progress:** {scored.raw:.2f}
* **Weakest criterion:** {scored.lowest:.2f} ({', '.join(scored.weakest) or 'none'})
* **Weakest-link penalty:** {scored.penalty:.2f}
* **Adjusted progress:** {scored.adjusted:.2f}
* **Final score:** **{score:.1f}**

### What prevents the next Type?

{spec['type']['gap']}
"""
    payload = {"axis": "type", "score": num(score, 1), "floor": floor, "criteria": criteria}
    return payload, body + "\n```json\n" + json.dumps(payload, indent=2) + "\n```\n"


def exec_report(slug: str, spec: dict) -> tuple[dict, str]:
    rows = spec["exec"]["rows"]
    scored = exec_score(EXEC_RUBRIC, {key: rows[key][0] for key in EXEC_KEYS})
    score = scored.score
    cap_line = "0.49, because E.1 is below 0.50" if scored.span_capped else "none"
    criteria = {key: num(rows[key][0], 2) for key in EXEC_KEYS}
    body = f"""> **Execution coverage: {score:.2f} / 1.00**

{spec['exec']['summary']}

Mock fixture for {DATE}, graded at criterion level from `src/specs/{slug}.md`.

{table(rows, EXEC_KEYS)}

* **Raw mean:** {scored.raw:.2f}
* **Weakest criterion:** {scored.lowest:.2f} ({', '.join(scored.weakest)})
* **Weakest-link penalty:** {scored.penalty:.2f}
* **Uncapped score:** {scored.uncapped:.2f}
* **Span cap:** {cap_line}
* **Final score:** **{score:.2f}**

### What most limits coverage?

{spec['exec']['gap']}
"""
    payload = {"axis": "exec", "score": num(score, 2), "criteria": criteria}
    return payload, body + "\n```json\n" + json.dumps(payload, indent=2) + "\n```\n"


def scored_criteria(payload: dict) -> dict:
    """Criteria that move the published score: Type I and II always, Type III only from the Type II floor."""
    if payload["axis"] == "exec" or payload["floor"] >= 2:
        return payload["criteria"]
    return {key: value for key, value in payload["criteria"].items() if not key.startswith("III.")}


def write_reference(evaluations: list[dict]) -> None:
    specs = {}
    for evaluation in evaluations:
        if evaluation["slug"] not in ANCHORS:
            continue
        specs[evaluation["slug"]] = {
            "type": {
                "floor": evaluation["type"]["floor"],
                "score": evaluation["type"]["score"],
                "criteria": scored_criteria({"axis": "type", **evaluation["type"]}),
            },
            "exec": {"score": evaluation["exec"]["score"], "criteria": evaluation["exec"]["criteria"]},
        }
    payload = {
        "note": "Expected grades for the calibration anchors, from `intelligence-scale mock`. Type III is left out below the Type II floor, where it does not move the score.",
        "tolerance": {"criterion": 0.25, "type": 0.3, "exec": 0.1},
        "alpha_min": 0.667,
        "specs": specs,
    }
    REFERENCE_PATH.parent.mkdir(parents=True, exist_ok=True)
    REFERENCE_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {relative(REFERENCE_PATH)}")


def write_mock(write_reference_file: bool = False) -> list[dict]:
    """Write the fixture partial to temp/<RUN_ID>/<MODEL>.json and return its evaluations."""
    specs = load_specs(include_drafts=True)
    slugs = [spec.slug for spec in specs]
    missing = [spec.slug for spec in specs if not spec.draft and spec.slug not in RATINGS]
    extra = [slug for slug in RATINGS if slug not in slugs]
    if missing or extra:
        raise ScaleError(f"spec mismatch missing={missing} extra={extra}")
    evaluations = []
    print(f"{'slug':<24} {'type':>5} {'exec':>5}")
    for spec_file in specs:
        slug = spec_file.slug
        if slug not in RATINGS:
            print(f"skipping draft spec {slug} (no mock rating)")
            continue
        spec = RATINGS[slug]
        for axis in ("type", "exec"):
            for _grade, _evidence, source in spec[axis]["rows"].values():
                if source.startswith("http") and source not in spec_file.text:
                    raise ScaleError(f"{slug} cites a URL that is not in the dossier: {source}")
        type_payload, type_text = type_report(slug, spec)
        exec_payload, exec_text = exec_report(slug, spec)
        evaluations.append(
            {
                "slug": slug,
                "name": spec_file.name,
                "url": spec_file.url,
                "type": {"score": type_payload["score"], "criteria": type_payload["criteria"], "floor": type_payload["floor"], "report": type_text},
                "exec": {"score": exec_payload["score"], "criteria": exec_payload["criteria"], "report": exec_text},
            }
        )
        print(f"{slug:<24} {type_payload['score']:5.1f} {exec_payload['score']:5.2f}")
    payload = {"model": MODEL, "created": "", "git": "", "evaluations": evaluations}
    path = partial_path(RUN_ID, MODEL)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {relative(path)}")
    if write_reference_file:
        write_reference(evaluations)
    return evaluations
