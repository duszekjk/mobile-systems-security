# Lesson H Ownership Map

Purpose: strict path ownership for the BSM L08 lesson.  
Rule: if a path is already touched by another agent, stop and report instead of editing.

## Current Lesson-H Ownership

| Path | Owner | Allowed Actions | Blocked Actions | Status |
|---|---|---|---|---|
| `student/labs/BSM_L08_AI_Assisted_Mobile_Security_Assessment.ipynb` | Agent 1 | Review and coordinate notebook structure | Edit alternate notebook variants | Active, canonical notebook target |
| `student/labs/BSM_L08_AI_mobile_application_security_assessment.ipynb` | Unassigned, conflict path | Review only | Any edits until ownership is resolved | Conflict / do not touch |
| `student/apps/lesson_h_ai_security/README.md` | Agent 3 | Metadata and suite description updates | Notebook edits | Active |
| `student/apps/lesson_h_ai_security/apps_manifest.yaml` | Agent 3 | App-path manifest updates | Notebook edits | Active |
| `student/apps/lesson_h_ai_security/vulnerability_catalog.md` | Agent 4 | Grading-vocabulary mapping | App source edits | Active |
| `student/answer_string_dictionary.md` | Agent 4 | Canonical answer matrix | Notebook and app source edits | Locked for answer-matrix centralization |
| `student/grading_rules.yaml` | Agent 4 | Canonical answer matrix rules | Notebook and app source edits | Locked for answer-matrix centralization |
| `student/apps/lesson_h_ai_security/InsecureNotes/` | Agent 3 | App source and build files | Duplicate nested copy edits | Active |
| `student/apps/lesson_h_ai_security/FakeBankLite/` | Agent 3 | App source and build files | Duplicate nested copy edits | Active |
| `student/apps/lesson_h_ai_security/SecurePatchTarget_v1/` | Agent 3 | App source and build files | Duplicate nested copy edits | Active |
| `student/apps/lesson_h_ai_security/SecurePatchTarget_v2/` | Agent 3 | App source and build files | Duplicate nested copy edits | Active |
| `student/lesson_h_ownership_registry.md` | Agent 5 | Coordination reference only | Lesson content edits | Reference |
| `student/lesson_h_communication_log.md` | All agents | Append status updates only | Overwrite or delete existing entries | Active coordination log |

## Duplicate / Collision Paths

- `student/labs/BSM_L08_AI_Assisted_Mobile_Security_Assessment.ipynb`
- `student/labs/BSM_L08_AI_mobile_application_security_assessment.ipynb`
- `student/apps/lesson_h_ai_security/InsecureNotes/lesson_h_insecurenotes/`
- `student/apps/lesson_h_ai_security/FakeBankLite/lesson_h_insecurenotes/`
- `student/apps/lesson_h_ai_security/SecurePatchTarget_v1/lesson_h_insecurenotes/`
- `student/apps/lesson_h_ai_security/SecurePatchTarget_v2/lesson_h_insecurenotes/`

## Agent 5 Reconciliation

- Canonical notebook remains [`student/labs/BSM_L08_AI_Assisted_Mobile_Security_Assessment.ipynb`](/Volumes/Macintosh%20HD2/Downloads/autotasks/bsm/student/labs/BSM_L08_AI_Assisted_Mobile_Security_Assessment.ipynb).
- Canonical app sources are the top-level roots:
  - [`student/apps/lesson_h_ai_security/InsecureNotes/`](/Volumes/Macintosh%20HD2/Downloads/autotasks/bsm/student/apps/lesson_h_ai_security/InsecureNotes/)
  - [`student/apps/lesson_h_ai_security/FakeBankLite/`](/Volumes/Macintosh%20HD2/Downloads/autotasks/bsm/student/apps/lesson_h_ai_security/FakeBankLite/)
  - [`student/apps/lesson_h_ai_security/SecurePatchTarget_v1/`](/Volumes/Macintosh%20HD2/Downloads/autotasks/bsm/student/apps/lesson_h_ai_security/SecurePatchTarget_v1/)
  - [`student/apps/lesson_h_ai_security/SecurePatchTarget_v2/`](/Volumes/Macintosh%20HD2/Downloads/autotasks/bsm/student/apps/lesson_h_ai_security/SecurePatchTarget_v2/)
- Remaining nested `lesson_h_insecurenotes` collision paths are now cleanup targets and may be reconciled by the owning app agent.
- Duplicate notebook variants are now coordination-only references, not edit targets.
- Tool-execution recipes are frozen; only Agent 5 may reopen them through a coordination update.

## Hard Rules

1. Check `git status` before every patch.
2. Stop if a path is already touched by another agent.
3. Do not edit outside the assigned paths.
4. Do not use broad `git add` or repo-wide refactors.
5. Post coordination updates only in `student/lesson_h_communication_log.md`.
