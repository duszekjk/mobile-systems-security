# BSM lesson plan: AI-assisted mobile application security assessment

## 1. Purpose of this document

This document describes the preparation plan for **one BSM laboratory lesson**, not a sequence of separate lessons. The lesson will be implemented as one Google Colab notebook supported by several Android Studio applications prepared specifically for the class.

The lesson theme is:

> **AI-assisted assessment of Android application security using security-focused tools and intentionally vulnerable mobile apps.**

The document is intended for a five-agent implementation team. It defines the lesson goals, expected Android applications, security tools, grading model, shared artifacts, communication workflow, synchronization rules and release criteria.

---

## 2. Context from previous notebooks

The new notebook should follow the style of the existing BSM notebook, especially `BSM_L07_Pochodzenie_Aplikacji_Integrity_Backup.ipynb`.

Observed BSM style:

- clear lesson title at the top,
- initial `Dane studenta` / student-data cell,
- numbered tasks using lesson prefix, for example `G01`, `G02`, `G03`,
- short theory section before each task,
- exact step-by-step instructions,
- Android Studio project path included in the task description,
- answer form cells using Colab parameters,
- submission through `zapisz_i_wyslij("G02", final_answer)` or equivalent,
- simple text answers submitted from Colab.

The computer-vision notebook shows a different but useful pattern:

- many small tasks,
- each task has an expected result stored under a task identifier,
- final answer is submitted through one dedicated cell per task.

For this BSM lesson, the **BSM L07 structure should be the primary template**. The computer-vision notebook is useful only as an example of repeated task/result organization.

---

## 3. Main lesson assumptions

1. This is **one BSM lesson**.
2. The lesson contains several exercises inside one notebook.
3. The lesson uses several Android applications, but they are all part of the same lesson.
4. Students do not use general-purpose LLMs such as normal ChatGPT.
5. Students use security-focused tools only.
6. Some tools may be used outside Colab.
7. The notebook explains what to do and provides fields for final answers.
8. Answers are graded using exact string comparison.
9. Therefore, students should not paste arbitrary scanner text.
10. Students should submit canonical answer strings prepared by the teacher.

---

## 4. Security and ethics boundaries

The lesson must be defensive and educational.

Allowed:

- analyzing intentionally vulnerable lab applications,
- static source-code analysis,
- APK analysis,
- comparing scanner results,
- classifying vulnerabilities,
- identifying false positives,
- proposing secure fixes,
- verifying that fixes reduce findings.


---

## 5. Tool research baseline

Before final implementation, Agent 2 must do fresh research and confirm current versions and availability. The following baseline is proposed.

Shared lesson-specific interpretation notes live here:

```text
research/2026-lecture-ai-vuln/lesson_h_practical_notes.md
```

All agents should use that file when translating papers into lesson design decisions, task wording, or grading constraints. It is the lesson-specific bridge between the broader research corpus and the mobile lab artifacts.

### 5.1 OWASP MASVS / MASTG / MASWE

Use OWASP MASVS, MASTG and MASWE as the conceptual and classification backbone for the lesson. Every intentionally introduced vulnerability should map to a mobile security category.

Use cases in this lesson:

- explaining vulnerability classes,
- mapping findings to mobile-security concepts,
- making the lesson defensible and standard-based,
- giving students professional vocabulary.

### 5.2 MobSF

MobSF should be considered the primary APK-level mobile security assessment tool.

Use cases:

- static APK analysis,
- manifest analysis,
- network security configuration review,
- backup/debuggable/exported component findings,
- optional dynamic analysis if the teaching environment supports it.

Preferred role in lesson:

- used for one or two tasks where students upload a prepared APK and identify a canonical vulnerability code.

### 5.3 mobsfscan

mobsfscan should be considered for source-code scanning.

Use cases:

- Kotlin source-code analysis,
- Java source-code analysis,
- Android XML analysis,
- finding insecure code patterns using MobSF rules and Semgrep/libsast.

Preferred role in lesson:

- source-code scan of a prepared Android Studio project.

### 5.4 Semgrep

Semgrep can be used as an additional or fallback source-code scanner.

Use cases:

- Java/Kotlin static analysis,
- Android security rules,
- custom rules for lesson-specific vulnerabilities.

Preferred role in lesson:

- either used directly by students or used by the teacher to validate that vulnerabilities are detectable.

### 5.5 SecureBERT2 / security-specific vulnerability models

Security-specific vulnerability-detection models should be used instead of general-purpose LLMs.

Candidate:

- `cisco-ai/SecureBERT2.0-code-vuln-detection`

Use cases:

- classify selected code snippets as vulnerable or not vulnerable,
- compare model output with deterministic scanner output,
- discuss why AI output requires verification.

Important limitation:

- output labels or confidence scores may vary by model version, environment or preprocessing. Therefore, grading should not depend directly on raw model output unless the notebook freezes the exact input and expected label.

### 5.6 garak / CyberSecEval-style tools

These tools may be considered for an optional section about testing security AI tools themselves.

Use cases:

- demonstrate that AI security assistants can be misled,
- show why deterministic scanners and human validation remain necessary.

Preferred role in lesson:

- optional advanced discussion, not core grading.

---

## 6. Proposed single-lesson structure

Suggested lesson title:

> **BSM L08 — AI-assisted mobile application security assessment**

Suggested Android project path:

```text
student/apps/lesson_h_ai_security/
```

Suggested task identifiers:

- `H01`
- `H02`
- `H03`
- `H04`
- `H05`

The exact letter can be adjusted to fit the existing BSM sequence.

---

## 7. Proposed exercises

### H01 — Source-code vulnerability scan

#### Goal

Students use a security scanner or security-specific AI model to inspect source code and identify a prepared vulnerability.

#### App

`InsecureNotes`

#### Prepared vulnerabilities

- hardcoded fake API key,
- sensitive data written to logs,
- plaintext token stored in `SharedPreferences`,
- weak cryptography example.

#### Recommended tools

- mobsfscan,
- Semgrep,
- optionally SecureBERT2-based snippet classifier.

#### Student action

1. Open `student/apps/lesson_h_ai_security/InsecureNotes` in Android Studio.
2. Locate the indicated Kotlin file.
3. Run the selected tool or inspect the prepared tool output.
4. Identify the vulnerability class.
5. Submit the canonical answer.

#### Example canonical answers

```text
HARDCODED_SECRET
SENSITIVE_LOGGING
PLAINTEXT_SHARED_PREFERENCES
WEAK_CRYPTO
```

#### Grading design

The notebook must not ask students to paste the scanner description. It should ask for a short code from a controlled list.

Example accepted answers for one variant:

```yaml
H01:
  accepted_answers:
    - HARDCODED_SECRET
    - HARDCODED_API_KEY
```

---

### H02 — APK security analysis

#### Goal

Students analyze a prepared APK and identify a vulnerability visible in APK-level analysis.

#### App

`FakeBankLite.apk`

#### Prepared vulnerabilities

- cleartext traffic enabled,
- insecure backup allowed,
- debuggable build flag,
- exported component.

#### Recommended tool

- MobSF

#### Student action

1. Build or download `FakeBankLite.apk`.
2. Upload it to MobSF.
3. Review manifest and security findings.
4. Identify the requested finding.
5. Submit the canonical answer.

#### Example canonical answers

```text
CLEARTEXT_TRAFFIC
BACKUP_ENABLED
DEBUGGABLE_TRUE
EXPORTED_COMPONENT
```

#### Grading design

The task should specify which part of the MobSF report students should inspect, for example:

> In the Manifest Analysis section, identify the network-security problem.

Expected answer:

```text
CLEARTEXT_TRAFFIC
```

---

### H03 — Security-specific AI model classification

#### Goal

Students use a security-specific vulnerability classifier on a fixed code snippet and interpret the result.

#### App

`InsecureNotes`

#### Prepared material

The notebook provides a short Kotlin snippet copied from the app.

#### Recommended tool

- SecureBERT2-style code vulnerability detection model,
- or another security-specific vulnerability classifier selected by Agent 2.

#### Student action

1. Copy the provided snippet.
2. Run it through the selected security-specific model.
3. Compare the model label with the expected vulnerability class.
4. Submit the canonical conclusion.

#### Example canonical answers

```text
MODEL_DETECTED_VULNERABLE
MODEL_MISSED_VULNERABILITY
MODEL_RESULT_UNCLEAR
```

#### Grading design

Because model outputs may vary, the task should be designed carefully.

Preferred approach:

- use a fixed snippet,
- use a frozen model version,
- define accepted answers based on the expected lesson result,
- allow two or three accepted strings if the model output changes slightly.

---

### H04 — Scanner vs AI disagreement

#### Goal

Students learn that AI-based security results require verification.

#### App

`FakeBankLite` or `InsecureNotes`

#### Prepared situation

One finding is intentionally chosen where:

- scanner finds the issue clearly,
- AI model either misses it or gives low confidence,
- or AI marks a safe snippet as suspicious.

#### Student action

1. Compare scanner output and AI output.
2. Decide which result should be trusted.
3. Submit the canonical answer.

#### Example canonical answers

```text
SCANNER_TRUE_POSITIVE
AI_FALSE_NEGATIVE
AI_FALSE_POSITIVE
NEEDS_HUMAN_REVIEW
```

#### Grading design

The task must clearly state what the student is evaluating.

Example question:

> The scanner reports `android:usesCleartextTraffic="true"`. The AI model says the code is safe. Which conclusion is correct?

Expected answer:

```text
AI_FALSE_NEGATIVE
```

---

### H05 — Patch verification

#### Goal

Students compare vulnerable and fixed app versions.

#### App

`SecurePatchTarget`

#### Prepared versions

- `SecurePatchTarget_v1` — vulnerable,
- `SecurePatchTarget_v2` — patched.

#### Student action

1. Analyze version 1.
2. Analyze version 2.
3. Identify which vulnerability disappeared.
4. Submit the canonical answer.

#### Example canonical answers

```text
ISSUE_FIXED
HARDCODED_SECRET_REMOVED
CLEARTEXT_TRAFFIC_FIXED
BACKUP_DISABLED
```

#### Grading design

The answer must be a deterministic string, not a written explanation.

---

## 8. Android applications to prepare

### 8.1 InsecureNotes

Purpose:

- source-code analysis,
- AI vulnerability classification,
- comparison between scanner and AI.

Suggested package:

```text
pl.edu.bsm.insecurenotes
```

Suggested vulnerable files:

```text
MainActivity.kt
SecretStore.kt
CryptoHelper.kt
LoggingHelper.kt
```

Vulnerabilities:

| ID | Vulnerability | Example canonical answer |
|---|---|---|
| V01 | fake API key hardcoded in Kotlin | `HARDCODED_SECRET` |
| V02 | token saved in plaintext SharedPreferences | `PLAINTEXT_SHARED_PREFERENCES` |
| V03 | sensitive value printed to Logcat | `SENSITIVE_LOGGING` |
| V04 | weak cryptographic mode or predictable IV | `WEAK_CRYPTO` |

Notes:

- All secrets must be fake.
- The app should be simple enough for students to understand quickly.
- The vulnerabilities should be obvious enough for tools to detect.

---

### 8.2 FakeBankLite

Purpose:

- APK-level analysis,
- manifest analysis,
- MobSF task.

Suggested package:

```text
pl.edu.bsm.fakebanklite
```

Vulnerabilities:

| ID | Vulnerability | Example canonical answer |
|---|---|---|
| V05 | cleartext traffic enabled | `CLEARTEXT_TRAFFIC` |
| V06 | backup enabled for sensitive app | `BACKUP_ENABLED` |
| V07 | debuggable build | `DEBUGGABLE_TRUE` |
| V08 | exported activity/service without protection | `EXPORTED_COMPONENT` |

Notes:

- The app must not connect to any real banking endpoint.
- Fake screens and fake data are enough.
- The app name should make the security context intuitive, but it must be clearly marked as a lab app.

---

### 8.3 SecurePatchTarget

Purpose:

- before/after comparison,
- remediation verification.

Suggested package:

```text
pl.edu.bsm.securepatchtarget
```

Versions:

```text
SecurePatchTarget_v1
SecurePatchTarget_v2
```

Vulnerabilities in v1:

- at least two issues copied from `InsecureNotes` or `FakeBankLite`.

Fixes in v2:

- remove hardcoded secret,
- disable cleartext traffic,
- disable backup,
- remove sensitive logging,
- use safer storage or encrypted preferences.

Example canonical answers:

```text
HARDCODED_SECRET_REMOVED
CLEARTEXT_TRAFFIC_FIXED
BACKUP_DISABLED
SENSITIVE_LOGGING_REMOVED
```

---

## 9. Grading model

The grading system compares submitted strings with teacher-provided accepted strings.

This means every task must have deterministic answer options.

### 9.1 Forbidden grading style

Do not ask:

```text
Paste the vulnerability description from MobSF.
```

This is fragile because tools may produce different wording between versions.

### 9.2 Required grading style

Ask:

```text
Enter the canonical vulnerability code.
```

Example:

```text
CLEARTEXT_TRAFFIC
```

### 9.3 Recommended answer fields

For each task, the notebook should use a simple form cell:

```python
# @title H02 — Formularz odpowiedzi {"run":"auto","vertical-output":true,"single-column":true,"display-mode":"form"}
code_h02 = ""  #@param {type:"string"}

final_answer = prepare_answer(code_h02.strip())
print(final_answer)
zapisz_i_wyslij("H02", final_answer)
```

### 9.4 Alternative accepted answers

Because students may reasonably use slightly different canonical names, the grading backend should support several exact accepted strings.

Example:

```yaml
H02:
  accepted_answers:
    - CLEARTEXT_TRAFFIC
    - CLEARTEXT_ENABLED
```

The notebook should still recommend one preferred answer.

---

## 10. Five-agent project structure

The project uses five cooperating agents.

The agents work on the same lesson, not on separate lessons.

---

# Agent 1 — Lesson Architect

## Responsibilities

- Design the single BSM lesson structure.
- Keep the notebook consistent with previous BSM lessons.
- Define task order and learning outcomes.
- Decide how much theory each section needs.
- Ensure the notebook is understandable for students.

## Owns

```text
lesson_structure.md
exercise_specifications.yaml
notebook_outline.md
```

## Inputs

- tool recommendations from Agent 2,
- app manifest from Agent 3,
- grading rules from Agent 4,
- QA reports from Agent 5.

## Completion criteria

Agent 1 can declare completion only when:

- every task has a goal,
- every task has a tool,
- every task has an Android app or snippet,
- every task has a deterministic answer field,
- the whole lesson fits into one BSM notebook.

---

# Agent 2 — Security Tool Research Agent

## Responsibilities

- Research current security tools.
- Confirm latest usable versions.
- Select tools that are security-focused, not general-purpose LLMs.
- Check whether tools run in Colab, locally, Docker, or Android Studio.
- Document risks caused by tool version changes.

## Owns

```text
tool_matrix.md
tool_recommendations.yaml
tool_risks.md
```

## Must research

- MobSF,
- mobsfscan,
- Semgrep Android/Kotlin support,
- SecureBERT2 or similar cybersecurity-specific vulnerability models,
- optional garak/CyberSecEval-style tooling.

## Completion criteria

Agent 2 can declare completion only when:

- each proposed tool has a purpose,
- each proposed tool has execution instructions,
- each proposed tool has known limitations,
- each proposed tool is mapped to at least one exercise or rejected with reason.

---

# Agent 3 — Android Application Agent

## Responsibilities

- Create the vulnerable Android applications.
- Ensure each app contains the expected vulnerabilities.
- Ensure vulnerabilities are detectable by selected tools.
- Keep all examples safe and educational.

## Owns

```text
apps_manifest.yaml
vulnerability_catalog.md
android_project_structure.md
```

## Must prepare

```text
InsecureNotes
FakeBankLite
SecurePatchTarget_v1
SecurePatchTarget_v2
```

## Completion criteria

Agent 3 can declare completion only when:

- each app builds,
- each app has the expected package name,
- each app contains the expected vulnerabilities,
- no app contains real secrets,
- no app performs harmful behavior,
- every vulnerability is documented in `vulnerability_catalog.md`.

---

# Agent 4 — Assessment and Grading Agent

## Responsibilities

- Design deterministic answer strings.
- Define accepted answers for every exercise.
- Reject tasks that cannot be graded by exact string comparison.
- Keep grading compatible with the existing BSM submission system.

## Owns

```text
grading_rules.yaml
grading_reference.md
answer_string_dictionary.md
```

## Veto power

Agent 4 may block an exercise if:

- scanner output is too variable,
- AI model output is too unstable,
- multiple interpretations are equally valid,
- the expected answer cannot be represented as one or a few exact strings.

## Completion criteria

Agent 4 can declare completion only when:

- every task has accepted answers,
- every accepted answer is deterministic,
- every answer string is documented,
- every answer string is visible to the teacher,
- the notebook asks for canonical codes rather than free-form explanations.

---

# Agent 5 — Synchronization and QA Agent

## Responsibilities

- Keep all artifacts synchronized.
- Track agent states.
- Track dependencies.
- Receive completion events.
- Allow agents to wait for each other.
- Collect comments and objections.
- Approve final release.

## Owns

```text
project_manifest.yaml
agent_status.yaml
communication_log.yaml
synchronization_report.md
release_checklist.md
```

## Completion criteria

Agent 5 can declare completion only when:

- all agents are completed,
- no blocking objections remain,
- every exercise references an existing app,
- every accepted answer maps to a real vulnerability,
- every tool mentioned in notebook exists in tool matrix,
- all release checklist items pass.

---

## 11. Agent communication system

Agents need more than shared files. They must be able to:

- say when they started,
- say when they finished,
- wait for another agent,
- comment on another agent's artifact,
- request changes,
- object to unsafe or ungradable designs,
- approve work,
- publish opinions,
- summarize findings.

This should be implemented as a structured project workflow.

---

## 12. Agent states

Each agent must always have one state in `agent_status.yaml`.

Allowed states:

```text
NOT_STARTED
WORKING
WAITING
REVIEWING
BLOCKED
COMPLETED
```

Example:

```yaml
Agent_3:
  state: WAITING
  waiting_for: Agent_2
  required_artifact: tool_recommendations.yaml
  reason: needs final scanner selection before app vulnerabilities are frozen
```

---

## 13. Communication events

All communication should be stored in `communication_log.yaml`.

### 13.1 Work started

```yaml
- event: WORK_STARTED
  agent: Agent_2
  timestamp: 2026-06-15T10:00:00
  message: "Starting current tool research."
```

### 13.2 Work completed

```yaml
- event: WORK_COMPLETED
  agent: Agent_2
  timestamp: 2026-06-15T12:00:00
  artifacts:
    - tool_matrix.md
    - tool_recommendations.yaml
  message: "Tool research completed and ready for review."
```

### 13.3 Waiting for dependency

```yaml
- event: WAITING_FOR_DEPENDENCY
  agent: Agent_4
  waiting_for: Agent_3
  required_artifact: apps_manifest.yaml
  message: "Cannot define accepted answers until vulnerability list is frozen."
```

### 13.4 Review requested

```yaml
- event: REVIEW_REQUESTED
  from: Agent_3
  to: Agent_4
  artifact: apps_manifest.yaml
  message: "Please verify that all proposed vulnerabilities can produce deterministic answer strings."
```

### 13.5 Review comment

```yaml
- event: REVIEW_COMMENT
  from: Agent_4
  to: Agent_3
  artifact: apps_manifest.yaml
  severity: MAJOR
  comment: "The AI-only classification task may not be deterministic. Add canonical answer choices or replace with scanner-confirmed vulnerability."
```

### 13.6 Change requested

```yaml
- event: CHANGE_REQUESTED
  from: Agent_5
  to: Agent_1
  artifact: exercise_specifications.yaml
  reason: "H03 mentions SecureBERT2 but tool_matrix.md does not yet approve it for student use."
```

### 13.7 Opinion published

```yaml
- event: OPINION_PUBLISHED
  from: Agent_2
  artifact: tool_matrix.md
  priority: MEDIUM
  opinion: "MobSF should be used for APK analysis, but not for exact wording-based grading. Use canonical answer strings instead."
```

### 13.8 Objection raised

```yaml
- event: OBJECTION_RAISED
  from: Agent_4
  artifact: exercise_specifications.yaml
  blocking: true
  reason: "H04 has too many valid answers and cannot be graded by exact string comparison."
```

### 13.9 Objection resolved

```yaml
- event: OBJECTION_RESOLVED
  by: Agent_1
  artifact: exercise_specifications.yaml
  resolution: "H04 changed to a fixed multiple-choice-style canonical answer: AI_FALSE_NEGATIVE."
```

### 13.10 Approval

```yaml
- event: REVIEW_APPROVED
  from: Agent_4
  artifact: grading_rules.yaml
  message: "All answer strings are deterministic and compatible with exact string matching."
```

---

## 14. How agents wait for each other

Agents do not wait informally. They update their state.

Example:

```yaml
Agent_1:
  state: WAITING
  waiting_for:
    - Agent_2
    - Agent_3
    - Agent_4
  required_artifacts:
    - tool_recommendations.yaml
    - apps_manifest.yaml
    - grading_rules.yaml
```

When the required agents publish `WORK_COMPLETED`, Agent 5 updates the dependency status and notifies the waiting agent through the communication log.

Example:

```yaml
- event: DEPENDENCY_READY
  to: Agent_1
  artifacts:
    - tool_recommendations.yaml
    - apps_manifest.yaml
    - grading_rules.yaml
  message: "All required inputs are available. Agent_1 may continue."
```

---

## 15. How agents comment on each other's work

Agents comment through review events, not by editing someone else's artifact directly.

Example:

```yaml
- event: REVIEW_COMMENT
  from: Agent_2
  to: Agent_1
  artifact: lesson_structure.md
  severity: MINOR
  comment: "The notebook says Semgrep detects all Kotlin issues, but Kotlin rule coverage depends on selected rules. Please soften the wording."
```

The artifact owner must either:

1. accept the comment and update the artifact,
2. reject the comment and explain why,
3. escalate to Agent 5.

---

## 16. How agents share gathered information

Each agent publishes gathered information in its owned artifact.

Examples:

- Agent 2 publishes tool research in `tool_matrix.md`.
- Agent 3 publishes app vulnerability details in `vulnerability_catalog.md`.
- Agent 4 publishes canonical answer strings in `grading_reference.md`.
- Agent 5 summarizes integration state in `synchronization_report.md`.

Agents may also publish short findings in the communication log.

Example:

```yaml
- event: FINDING_PUBLISHED
  from: Agent_2
  topic: "MobSF output stability"
  finding: "MobSF wording can vary between versions, so grading must not depend on exact MobSF report text."
  affects:
    - Agent_1
    - Agent_4
```

---

## 17. How agents say they finished

An agent declares completion only through `WORK_COMPLETED`.

Example:

```yaml
- event: WORK_COMPLETED
  agent: Agent_3
  artifacts:
    - apps_manifest.yaml
    - vulnerability_catalog.md
    - android_project_structure.md
  completion_statement: "All planned Android applications are specified and all vulnerabilities are mapped to exercises and grading identifiers."
```

Agent 5 then verifies the artifacts. If verification passes, Agent 5 marks the agent as completed.

Example:

```yaml
Agent_3:
  state: COMPLETED
  verified_by: Agent_5
```

---

## 18. Shared repository structure

```text
project/
├── README.md
├── lesson_structure.md
├── notebook_outline.md
├── exercise_specifications.yaml
├── tool_matrix.md
├── tool_recommendations.yaml
├── tool_risks.md
├── apps_manifest.yaml
├── vulnerability_catalog.md
├── android_project_structure.md
├── grading_rules.yaml
├── grading_reference.md
├── answer_string_dictionary.md
├── project_manifest.yaml
├── agent_status.yaml
├── communication_log.yaml
├── synchronization_report.md
├── release_checklist.md
└── decisions/
    ├── ADR-001-tool-selection.md
    ├── ADR-002-grading-style.md
    └── ADR-003-app-scope.md
```

---

## 19. Source-of-truth manifest

Agent 5 maintains `project_manifest.yaml`.

Example:

```yaml
lesson:
  id: BSM_L08
  title: AI-assisted mobile application security assessment
  type: single_lesson

exercises:
  H01:
    app: InsecureNotes
    tool: mobsfscan
    vulnerability: HARDCODED_SECRET
    accepted_answers:
      - HARDCODED_SECRET
      - HARDCODED_API_KEY

  H02:
    app: FakeBankLite.apk
    tool: MobSF
    vulnerability: CLEARTEXT_TRAFFIC
    accepted_answers:
      - CLEARTEXT_TRAFFIC
      - CLEARTEXT_ENABLED

  H03:
    app: InsecureNotes
    tool: SecureBERT2-code-vuln-detection
    vulnerability: PLAINTEXT_SHARED_PREFERENCES
    accepted_answers:
      - MODEL_DETECTED_VULNERABLE

  H04:
    app: FakeBankLite
    tool: MobSF + security model
    vulnerability: AI_FALSE_NEGATIVE
    accepted_answers:
      - AI_FALSE_NEGATIVE

  H05:
    app: SecurePatchTarget_v1_v2
    tool: MobSF or mobsfscan
    vulnerability: CLEARTEXT_TRAFFIC_FIXED
    accepted_answers:
      - CLEARTEXT_TRAFFIC_FIXED
```

---

## 20. Decision records

Important decisions must be stored as ADR files.

Example:

```text
decisions/ADR-002-grading-style.md
```

Template:

```md
# ADR-002 — Grading uses canonical answer strings

## Decision

Students submit canonical vulnerability identifiers instead of raw scanner output.

## Reason

The grading backend compares exact strings. Scanner and AI output may vary between versions.

## Consequences

Every exercise must include one or more accepted answer strings.
Free-form explanations may appear as learning activities but cannot be graded automatically.
```

---

## 21. Synchronization workflow

### Stage 1 — Tool research

Lead: Agent 2

Output:

- `tool_matrix.md`
- `tool_recommendations.yaml`

Agent 2 then publishes `WORK_COMPLETED`.

Agents 1, 3 and 4 review.

---

### Stage 2 — Android app design

Lead: Agent 3

Input:

- Agent 2 tool recommendations

Output:

- `apps_manifest.yaml`
- `vulnerability_catalog.md`

Agent 3 then requests review from Agent 4.

---

### Stage 3 — Grading design

Lead: Agent 4

Input:

- Agent 3 app manifest
- Agent 1 exercise goals

Output:

- `grading_rules.yaml`
- `grading_reference.md`

Agent 4 may block any exercise that is not deterministic.

---

### Stage 4 — Lesson structure

Lead: Agent 1

Input:

- tool recommendations,
- app manifest,
- grading rules.

Output:

- `lesson_structure.md`
- `notebook_outline.md`
- `exercise_specifications.yaml`

---

### Stage 5 — Integration and QA

Lead: Agent 5

Input:

- all artifacts

Output:

- `project_manifest.yaml`
- `synchronization_report.md`
- `release_checklist.md`

Agent 5 verifies consistency and either approves release or requests changes.

---

## 22. QA checklist

Before the lesson is approved:

- [ ] Notebook is one lesson, not several lessons.
- [ ] Every exercise has one task identifier.
- [ ] Every exercise references a real prepared app or snippet.
- [ ] Every Android app builds.
- [ ] Every vulnerability is intentional.
- [ ] Every vulnerability is safe for a teaching lab.
- [ ] Every vulnerability has a canonical answer string.
- [ ] Every canonical answer appears in `grading_rules.yaml`.
- [ ] No task requires normal ChatGPT.
- [ ] All AI tools are security-specific.
- [ ] Scanner output wording is not used directly for grading.
- [ ] Tool versions are documented.
- [ ] The notebook follows the BSM L07 style.
- [ ] Agent 5 has approved the final manifest.

---

## 23. Final implementation recommendation

The first implementation of the lesson should use five graded exercises:

| Task | App | Tool | Expected answer style |
|---|---|---|---|
| H01 | InsecureNotes | mobsfscan or Semgrep | vulnerability code |
| H02 | FakeBankLite.apk | MobSF | vulnerability code |
| H03 | InsecureNotes snippet | SecureBERT2-style model | model conclusion code |
| H04 | FakeBankLite / snippet | scanner + AI comparison | disagreement code |
| H05 | SecurePatchTarget v1/v2 | MobSF or mobsfscan | fixed issue code |

The lesson should prioritize reliability over tool complexity. If a tool produces unstable output, it may still be shown, but it should not determine grading.

---

## 24. Final release condition

The lesson is ready for notebook implementation only when:

```yaml
Agent_1: COMPLETED
Agent_2: COMPLETED
Agent_3: COMPLETED
Agent_4: COMPLETED
Agent_5: COMPLETED
open_objections: 0
release_checklist: PASSED
```

Only after this condition is met should the actual Colab notebook and Android Studio projects be generated.
