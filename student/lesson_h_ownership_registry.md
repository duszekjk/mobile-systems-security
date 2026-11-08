# Lesson H Ownership Registry

Purpose: stop duplicate edits on the BSM L08 lesson by making file ownership explicit.

## Canonical lesson artifacts

- Notebook: `student/labs/BSM_L08_AI_Mobile_Security_Assessment.ipynb`
- Shared lesson plan: `student/BSM_AI_Mobile_Security_Lesson_Multi_Agent_Plan.md`
- Lesson research notes: `research/2026-lecture-ai-vuln/lesson_h_practical_notes.md`
- App bundle: `student/apps/lesson_h_ai_security/`

## Agent ownership

### Agent 1 - Lesson Architect

Owned paths:
- `student/labs/BSM_L08_AI_Mobile_Security_Assessment.ipynb`

Do not edit:
- alternate notebook variants under `student/labs/BSM_L08_*`

### Agent 2 - Security Tool Research

Owned paths:
- `research/2026-lecture-ai-vuln/lesson_h_practical_notes.md`

Do not edit:
- the broader research corpus unless specifically assigned

### Agent 3 - Android Application

Owned paths:
- `student/apps/lesson_h_ai_security/README.md`
- `student/apps/lesson_h_ai_security/apps_manifest.yaml`
- `student/apps/lesson_h_ai_security/vulnerability_catalog.md`
- `student/apps/lesson_h_ai_security/InsecureNotes/`
- `student/apps/lesson_h_ai_security/FakeBankLite/`
- `student/apps/lesson_h_ai_security/SecurePatchTarget_v1/`
- `student/apps/lesson_h_ai_security/SecurePatchTarget_v2/`

Do not edit:
- legacy lesson-H roots outside `student/apps/lesson_h_ai_security/`

### Agent 4 - Assessment and Grading

Owned paths:
- `student/grading_rules.yaml`
- `student/answer_string_dictionary.md`

Do not edit:
- any app source or notebook content

### Agent 5 - Synchronization and QA

Owned paths:
- `project_manifest.yaml`
- `agent_status.yaml`
- `communication_log.yaml`
- `synchronization_report.md`
- `release_checklist.md`

Do not edit:
- lesson content unless a coordination fix is required

## Current duplication hotspots

These paths already exist in multiple variants and should be treated as read-only until the team agrees on cleanup:

- `student/labs/BSM_L08_AI_Assisted_Mobile_Security_Assessment.ipynb`
- `student/labs/BSM_L08_AI_assisted_mobile_application_security_assessment.ipynb`
- `student/labs/BSM_L08_AI_mobile_application_security_assessment.ipynb`
- `student/labs/BSM_L08_AI_wspomagana_ocena_bezpieczenstwa_aplikacji_mobilnych.ipynb`
- `student/apps/lesson_h_insecurenotes/`
- `student/apps/lesson_h_fakebanklite/`
- `student/apps/lesson_h_securepatchtarget_v1/`
- `student/apps/lesson_h_securepatchtarget_v2/`

## Working rule

Before editing any lesson file:

1. check `git status`
2. confirm the path is owned by the current agent
3. stop if another agent already touched that file
4. avoid broad add or broad refactors

