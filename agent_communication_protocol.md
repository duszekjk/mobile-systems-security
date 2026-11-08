# Agent Communication Protocol

## Purpose

This document defines how multiple agents must communicate and cooperate while working on the same project.

It is not a project plan. It does not describe the lesson content. It only defines the communication, coordination, waiting, interruption, review, and escalation mechanisms that agents must use to avoid chaos.

Every agent must read this document before doing any work.

---

# Core Rule

Agents are not independent freelancers.

They are members of one coordinated team.

No agent may begin implementation work until it knows:

1. what task it owns,
2. what files or resources it is allowed to modify,
3. what other agents it depends on,
4. who must review its work,
5. what output it must publish when finished.

If any of these are unclear, the agent must stop and ask for clarification.

---

# Shared Communication Space

All agents communicate through a shared `communication_log.md` file or equivalent shared channel.

Every message must be written in this format:

```md
## MESSAGE_ID: MSG-0001

from: Agent_Name
to: Agent_Name | ALL
type: STATUS | QUESTION | ANSWER | RESULT | REVIEW | WARNING | BLOCKER | INTERRUPT | WAITING | RESUME | DONE
priority: LOW | NORMAL | HIGH | URGENT
related_task: TASK-ID
related_file: optional-file-name
requires_response: YES | NO

message:
...
```

Agents must not rely only on final summaries. They must actively send questions, warnings, comments, partial results, and objections while work is in progress.

---

# Required Agent States

Each agent must keep its current state visible.

Allowed states:

- `IDLE`
- `WORKING`
- `WAITING_SHORT`
- `WAITING_LONG`
- `BLOCKED`
- `REVIEWING`
- `NEEDS_REWORK`
- `DONE`

Each state update must be published as a `STATUS` message.

Example:

```md
## MESSAGE_ID: MSG-0012

from: App_Agent
to: ALL
type: STATUS
priority: NORMAL
related_task: APP-01
requires_response: NO

message:
State changed to WORKING.
I am implementing InsecureNotes only.
I will not touch FakeBankLite or notebook files.
```

---

# Task Ownership

Before starting work, every agent must publish what it owns.

Example:

```md
## MESSAGE_ID: MSG-0020

from: App_Agent
to: ALL
type: STATUS
priority: HIGH
related_task: APP-01
requires_response: NO

message:
I own the implementation of InsecureNotes.
Locked resources:
- apps/InsecureNotes/
- apps_manifest.yaml section: InsecureNotes

No other agent should modify these files until I release the lock.
```

An agent may not edit files owned or locked by another agent.

If another agent needs a change, it must send a `QUESTION`, `REVIEW`, `WARNING`, or `INTERRUPT` message.

---

# File and Resource Locks

Agents must use explicit locks before editing shared resources.

Lock message:

```md
## MESSAGE_ID: MSG-0030

from: Grading_Agent
to: ALL
type: STATUS
priority: HIGH
related_task: GRADING-02
related_file: grading_rules.yaml
requires_response: NO

message:
LOCK ACQUIRED: grading_rules.yaml
Reason: adding canonical answers for Exercise 2.
Expected duration: short.
```

Unlock message:

```md
## MESSAGE_ID: MSG-0031

from: Grading_Agent
to: ALL
type: DONE
priority: NORMAL
related_task: GRADING-02
related_file: grading_rules.yaml
requires_response: NO

message:
LOCK RELEASED: grading_rules.yaml
Changes completed.
Summary:
- added CLEARTEXT_TRAFFIC
- added DEBUGGABLE_ENABLED
- added BACKUP_ALLOWED
```

If a lock is expected to last too long, the agent must explain why.

---

# Waiting Mechanism

Agents must not guess missing information.

If an agent needs another agent's result, it must wait.

There are two waiting modes.

---

## Short Wait

Use `WAITING_SHORT` when the dependency is expected to finish soon.

The agent may pause and periodically check the communication log.

Example:

```md
## MESSAGE_ID: MSG-0040

from: Grading_Agent
to: App_Agent
type: WAITING
priority: NORMAL
related_task: GRADING-01
requires_response: YES

message:
State changed to WAITING_SHORT.
I need the final vulnerability list for InsecureNotes before I can define canonical answers.
I will wait for your APP-01 result.
```

When the dependency appears, the waiting agent must publish:

```md
## MESSAGE_ID: MSG-0041

from: Grading_Agent
to: ALL
type: RESUME
priority: NORMAL
related_task: GRADING-01
requires_response: NO

message:
State changed from WAITING_SHORT to WORKING.
I received the InsecureNotes vulnerability list and continue grading design.
```

---

## Long Wait

Use `WAITING_LONG` when the dependency may take too long.

In this mode the agent must stop work and wait until the user or coordinator tells it to continue.

Example:

```md
## MESSAGE_ID: MSG-0045

from: Notebook_Agent
to: User_or_Coordinator
type: WAITING
priority: HIGH
related_task: NOTEBOOK-01
requires_response: YES

message:
State changed to WAITING_LONG.
I cannot build the notebook structure because the final exercise list is not ready.
This dependency may take longer.
I will stop here and wait until I am explicitly asked to continue.
```

Agents must not fill missing long-wait dependencies with guesses.

---

# Interrupt Mechanism

Agents may interrupt another agent if they see a serious problem.

Interrupts are used when continuing work would waste time or create incorrect output.

Valid reasons for interrupting:

- two agents are working on the same file or app,
- an agent is working outside its assigned scope,
- an app vulnerability cannot be detected by the planned tools,
- grading would not be deterministic,
- a proposed tool is not free or not reproducible,
- the work contradicts the project constraints,
- a security or safety issue appears.

Interrupt message:

```md
## MESSAGE_ID: MSG-0050

from: Grading_Agent
to: App_Agent
type: INTERRUPT
priority: URGENT
related_task: APP-02
requires_response: YES

message:
Please pause work on FakeBankLite.
Reason:
The current planned vulnerability requires students to write free-form text, which cannot be graded by exact string matching.
Suggested fix:
Replace it with a vulnerability that maps to one canonical answer, for example CLEARTEXT_TRAFFIC.
```

The interrupted agent must respond before continuing.

Allowed responses:

- accept and change work,
- explain why the interruption is incorrect,
- request coordinator decision,
- stop and mark itself blocked.

Response example:

```md
## MESSAGE_ID: MSG-0051

from: App_Agent
to: Grading_Agent
 type: ANSWER
priority: HIGH
related_task: APP-02
requires_response: NO

message:
Accepted.
I paused FakeBankLite changes.
I will replace the ambiguous issue with CLEARTEXT_TRAFFIC and update apps_manifest.yaml.
```

---

# Blocking Problems

If an agent cannot continue, it must publish a `BLOCKER` message.

Example:

```md
## MESSAGE_ID: MSG-0060

from: Tool_Research_Agent
to: ALL
type: BLOCKER
priority: HIGH
related_task: TOOLS-01
requires_response: YES

message:
I cannot recommend SecureBERT as a required tool yet.
Problem:
The model output is not stable enough for deterministic grading.
Impact:
Exercises depending on exact model labels may fail.
Suggested resolution:
Use the AI model only for discussion, and grade students on fixed labels chosen from a list.
```

Blockers must be resolved before dependent work continues.

---

# Result Messages

Every completed work item must publish a `RESULT` message before the agent marks itself as `DONE`.

A result message must include:

- what was done,
- what files changed,
- what assumptions were made,
- what still needs review,
- what other agents should use.

Example:

```md
## MESSAGE_ID: MSG-0070

from: App_Agent
to: ALL
type: RESULT
priority: NORMAL
related_task: APP-01
requires_response: YES

message:
Completed first version of InsecureNotes.

Files changed:
- apps/InsecureNotes/
- apps_manifest.yaml

Intentional vulnerabilities:
- HARDCODED_SECRET
- INSECURE_SHARED_PREFERENCES
- SENSITIVE_LOGGING
- WEAK_CRYPTO

Assumptions:
- These findings must be detectable by Semgrep or mobsfscan.

Needs review from:
- Tool_Research_Agent: confirm detectability
- Grading_Agent: confirm deterministic answer names
```

---

# Review Messages

Agents must review artifacts that affect their own work.

Example:

```md
## MESSAGE_ID: MSG-0080

from: Grading_Agent
to: App_Agent
type: REVIEW
priority: NORMAL
related_task: APP-01
requires_response: YES

message:
Review of InsecureNotes vulnerability list:

Approved:
- HARDCODED_SECRET
- SENSITIVE_LOGGING

Needs change:
- WEAK_CRYPTO is too broad.

Reason:
The answer could be AES_ECB, WEAK_CRYPTO, INSECURE_CRYPTO, or PREDICTABLE_IV.

Recommendation:
Use one exact canonical answer: AES_ECB_MODE.
```

The owner of the reviewed artifact must answer.

---

# Commenting on Work in Progress

Agents do not need to wait until final review to comment.

If an agent notices a smaller issue while another agent is working, it should send a `WARNING` or `COMMENT`-style `REVIEW` message.

Example:

```md
## MESSAGE_ID: MSG-0090

from: Tool_Research_Agent
to: App_Agent
type: WARNING
priority: NORMAL
related_task: APP-02
requires_response: NO

message:
Small warning while you work on FakeBankLite:
MobSF often reports network configuration issues with different wording depending on version.
For grading, avoid raw MobSF wording.
Use canonical answer CLEARTEXT_TRAFFIC instead.
```

Warnings are non-blocking unless marked as `URGENT`.

---

# Questions and Answers

Agents must ask direct questions instead of making assumptions.

Question example:

```md
## MESSAGE_ID: MSG-0100

from: Notebook_Agent
to: Grading_Agent
type: QUESTION
priority: NORMAL
related_task: NOTEBOOK-02
requires_response: YES

message:
For Exercise 3, should the answer field accept only one canonical string or several alternatives?
I need this before writing the Colab form.
```

Answer example:

```md
## MESSAGE_ID: MSG-0101

from: Grading_Agent
to: Notebook_Agent
type: ANSWER
priority: NORMAL
related_task: NOTEBOOK-02
requires_response: NO

message:
Use one primary canonical string in the notebook instructions.
The grading file may include alternatives, but students should be shown only one preferred answer format.
```

---

# Daily or Periodic Summaries

When agents work for a longer time, each agent must publish a short progress summary.

Example:

```md
## MESSAGE_ID: MSG-0110

from: Tool_Research_Agent
to: ALL
type: STATUS
priority: LOW
related_task: TOOLS-01
requires_response: NO

message:
Progress summary:
- MobSF checked
- mobsfscan checked
- Semgrep checked
- AI model research still in progress
Current risk:
AI model labels may not be stable enough for exact grading.
```

Summaries must not replace direct communication.

---

# Coordinator Role

If a coordinator exists, agents must route conflicts through the coordinator.

The coordinator decides:

- task assignment,
- ownership conflicts,
- unresolved objections,
- whether to continue after long waiting,
- final approval for release.

If no coordinator exists, unresolved conflicts must be sent to the user.

---

# Handoff Protocol

When one agent finishes work that another agent needs, it must send a handoff message.

Example:

```md
## MESSAGE_ID: MSG-0120

from: Tool_Research_Agent
to: App_Agent
type: RESULT
priority: HIGH
related_task: TOOLS-01
requires_response: YES

message:
Handoff to App_Agent:
Recommended detectable vulnerabilities for source-code exercises:
- hardcoded secret
- insecure logging
- exported activity
- cleartext traffic config

Avoid:
- vague cryptography issues unless the exact pattern is AES/ECB.

You may now design app vulnerabilities using this list.
```

The receiving agent must acknowledge:

```md
## MESSAGE_ID: MSG-0121

from: App_Agent
to: Tool_Research_Agent
type: ANSWER
priority: NORMAL
related_task: APP-01
requires_response: NO

message:
Handoff acknowledged.
I will use only detectable vulnerabilities from your list.
```

---

# Dependency Gates

Some work must not start before earlier work is complete.

Default gates:

## Gate 1: Tool Research Ready

Before app implementation begins:

- tool matrix must exist,
- recommended tools must be known,
- unsupported tools must be excluded.

## Gate 2: App Vulnerability List Ready

Before grading begins:

- app names must be fixed,
- vulnerability identifiers must be fixed,
- detection method must be known.

## Gate 3: Grading Rules Ready

Before notebook writing begins:

- canonical answers must be fixed,
- accepted alternatives must be known,
- answer format must be known.

## Gate 4: QA Review Ready

Before final release:

- all artifacts must be consistent,
- all locks released,
- all blockers resolved,
- all agents marked done.

If a gate is not satisfied, dependent agents must enter `WAITING_SHORT`, `WAITING_LONG`, or `BLOCKED`.

---

# Stop Rules

An agent must stop immediately when:

- it is editing a resource owned by another agent,
- another agent sends an urgent interrupt,
- its work depends on missing information,
- it notices that the current approach breaks deterministic grading,
- it notices that the work requires a paid or unavailable tool,
- it is about to invent missing project requirements.

Stopping is not failure. It is required coordination.

---

# Continue Rules

An agent may continue only when:

- its dependency has published a `RESULT`,
- required questions are answered,
- blockers are resolved,
- no urgent interrupt is pending,
- it owns or has permission to edit the required files.

---

# Final Completion Message

When an agent finishes all assigned work, it must send:

```md
## MESSAGE_ID: MSG-0999

from: Agent_Name
to: ALL
type: DONE
priority: NORMAL
related_task: TASK-ID
requires_response: NO

message:
State changed to DONE.
Completed work:
- ...

Artifacts produced:
- ...

Open risks:
- none / list risks

Needs further action from:
- none / specific agent
```

---

# Minimum Communication Requirements

Each agent must send at least these messages:

1. `STATUS` when starting.
2. `STATUS` when taking ownership of files or resources.
3. `QUESTION` if any required input is missing.
4. `WAITING` if blocked by another process.
5. `INTERRUPT` if another agent is causing conflict or waste.
6. `RESULT` after completing a meaningful unit of work.
7. `REVIEW` when another agent's work affects its own task.
8. `DONE` when fully finished.

---

# Practical Rule for Human Use

If agents cannot truly monitor each other automatically, the user or coordinator should periodically paste the latest communication log into each active agent.

Each agent must then:

1. read new messages,
2. respond to messages addressed to it,
3. update its state,
4. continue, wait, or stop.

This prevents agents from silently diverging.

---

# Summary

Good communication means agents must be able to:

- talk during work,
- ask questions,
- wait for dependencies,
- stop when waiting may take too long,
- interrupt incorrect work,
- comment on partial results,
- publish structured outputs,
- acknowledge handoffs,
- review each other's work,
- declare completion.

The goal is not only to summarize finished work, but to coordinate active work while it is happening.
