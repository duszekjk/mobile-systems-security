# Lesson H practical notes

## Scope

This note is for the BSM L08 lab:

- `student/labs/BSM_L08_AI_Mobile_Security_Assessment.ipynb`
- `student/apps/lesson_h_ai_security`

It is intentionally narrower than the broader research bundle in `research/2026-lecture-ai-vuln/`. The goal here is to translate the literature into practical teaching choices for this lesson, not to summarize the full paper set.

## Coordination

Before any further lesson-H edit, read `student/lesson_h_communication_log.md` and post a short update there if the coordination file is owned by your role.

## Agent 2 working order

Use this file as the lesson-facing bridge from literature to task design.

When translating papers into lesson decisions:

1. prefer the practical notes here over the broader research bundle
2. keep H01-H05 deterministic and canonical-answer based
3. avoid depending on raw vendor wording from scanners or models
4. treat Android/mobile examples as the lesson target, not the general paper topic

What this file is not:

- a full paper summary
- a grading key
- a substitute for the communication log

## What the lesson actually needs

The lab has five concrete student actions:

1. source-code scan of `InsecureNotes`
2. APK / manifest analysis of `FakeBankLite`
3. AI-assisted classification of a fixed code snippet
4. disagreement handling between scanner and model output
5. patch verification between `SecurePatchTarget_v1` and `SecurePatchTarget_v2`

So the literature has to support:

- why a code scanner is useful
- why model-based classification is useful but unstable
- why mobile APK analysis still needs deterministic inspection
- why exact-answer grading should use canonical codes instead of prose

## Papers that matter most for this lab

### `codebert.pdf`

Practical use:

- background for code representation models used in code understanding and vulnerability classification
- helps justify the H03 setup where a snippet is classified by a model instead of only by a rule-based scanner

Lesson takeaway:

- the model can be used as a pre-screening signal, not as final authority

### `graphcodebert.pdf`

Practical use:

- supports the idea that code structure and dataflow matter for vulnerability detection
- useful when explaining why a model may behave differently from a simple regex or keyword scanner

Lesson takeaway:

- model output is not guaranteed to match the exact vulnerability wording a student expects

### `devign.pdf`

Practical use:

- useful as a classical vulnerability-detection baseline that motivates learning-based detection
- good for a short theory note that "machine learning can detect patterns, but not every logical bug"

Lesson takeaway:

- ML detectors can be right for the wrong reason, or miss an issue entirely

### `vuldeepecker.pdf`

Practical use:

- supports function-level vulnerability detection as a precursor to later vulnerability classifiers
- helpful for explaining why local code snippets are a reasonable teaching unit

Lesson takeaway:

- snippet-level classification is teachable, but the lab must freeze the input and the accepted outputs

### `ivdetect.pdf`

Practical use:

- reinforces that vulnerability detection depends on feature extraction and model framing
- good for the "scanner vs AI" comparison in H04

Lesson takeaway:

- disagreement between tools is normal and should trigger human review

### `linevd.pdf`

Practical use:

- useful for explaining why line-level localization matters in practice
- helps justify giving students a concrete file and line to inspect in H01/H03

Lesson takeaway:

- students should identify the canonical issue code, not paste a long tool report

### `cvefixes.pdf`

Practical use:

- useful as background for fix verification
- supports H05, where students compare vulnerable and patched variants

Lesson takeaway:

- remediation verification is a separate skill from finding the original issue

### `diversevul.pdf`

Practical use:

- useful for explaining dataset diversity and why detectors generalize unevenly
- supports the lesson design choice to use multiple small tasks instead of one giant open-ended assessment

Lesson takeaway:

- detector performance varies by codebase, language, and feature distribution

## Papers that matter for the AI caution layer

### `finetuning_large_language_models_for_vulnerability_detection.pdf`

Practical use:

- supports the claim that fine-tuning can improve vulnerability detection
- useful background for H03

Lesson takeaway:

- fine-tuned models still need frozen inputs and controlled grading outputs

### `understanding_the_effectiveness_of_large_language_models_in_detecting_security_vulnerabilities.pdf`

Practical use:

- useful for discussing the limits of general-purpose LLMs in security work
- helps explain why the lesson prefers security-specific models or deterministic scanners

Lesson takeaway:

- "AI says safe" is not enough for a mobile security decision

### `code_vulnerability_detection_a_comparative_analysis_of_emerging_large_language_models.pdf`

Practical use:

- good support for the scanner-vs-model comparison task
- useful when describing that multiple models can disagree on the same code

Lesson takeaway:

- the lesson should teach verification, not blind trust

### `llbezpeky_leveraging_large_language_models_for_vulnerability_detection.pdf`

Practical use:

- useful as a broader examples paper for LLM-assisted vulnerability detection
- supports the lesson's "AI-assisted" framing

Lesson takeaway:

- AI assistance is helpful, but result normalization is required for assessment

### `lprotector_an_llm-driven_vulnerability_detection_system.pdf`

Practical use:

- shows how an LLM-driven detection workflow can be framed as a system
- useful for a teacher note on why this lesson mixes tools instead of relying on one model

Lesson takeaway:

- system design matters as much as the model

### `vuldetectbench_evaluating_the_deep_capability_of_vulnerability_detection_with_large_language_models.pdf`

Practical use:

- helpful for motivating that benchmarking matters
- relevant to the lesson's need for deterministic answer strings

Lesson takeaway:

- benchmarkability and grading stability are part of the lesson design

### `gpt4_technical_report.pdf`

Practical use:

- background for model capability discussions
- not a primary source for the lab exercises themselves

Lesson takeaway:

- general model capability does not remove the need for security-specific validation

## Mobile-specific translation

The papers are mostly about code vulnerability detection in general, not Android-specific issues. For this lesson, the translation is:

- source-code detectors justify H01
- APK/manifest inspection justifies H02
- model classification and disagreement handling justify H03 and H04
- patch comparison and remediation checks justify H05

The mobile side of the lesson is supplied by the apps:

- `InsecureNotes`
- `FakeBankLite`
- `SecurePatchTarget_v1`
- `SecurePatchTarget_v2`

## Practical teaching constraints

1. Do not ask students to reproduce raw model labels from a live model unless the input is frozen and the accepted outputs are narrow.
2. Do not grade on MobSF wording.
3. Use canonical answer codes.
4. Keep scanner and AI roles separate:
   - scanner for deterministic finding
   - model for interpretation or comparison
5. Keep the lesson mobile-focused by anchoring every task to a specific app or APK.

## Frozen execution recipes

These are the lesson-level execution paths to keep stable for all agents.

### H01 source scan

- Target: `student/apps/lesson_h_ai_security/InsecureNotes`
- Tool path: `mobsfscan` or Semgrep on the app source tree
- Output to grade: one canonical code from the predefined list
- Do not grade: tool prose, line numbers, or warning counts

### H02 APK analysis

- Target: `student/apps/lesson_h_ai_security/FakeBankLite`
- Tool path: MobSF static analysis of the prepared APK
- Output to grade: one canonical code from the predefined list
- Do not grade: raw MobSF wording or section titles

### H03 model classification

- Target: one frozen Kotlin snippet from `InsecureNotes`
- Tool path: a security-specific code-vulnerability classifier such as `cisco-ai/SecureBERT2.0-code-vuln-detection`
- Output to grade: one canonical conclusion string, not a full model dump
- Do not grade: confidence scores or unbounded label text

### H04 disagreement handling

- Target: the same frozen source material used in H01/H03
- Tool path: compare deterministic scanner output against model output
- Output to grade: one canonical disagreement code
- Do not grade: a free-form explanation of the disagreement

### H05 patch verification

- Target: `student/apps/lesson_h_ai_security/SecurePatchTarget_v1` and `SecurePatchTarget_v2`
- Tool path: source or APK comparison that proves the fix
- Output to grade: one canonical fix code
- Do not grade: a prose explanation of the remediation

## Remaining lesson-design gaps

1. The canonical answer matrix still needs to be centralized in one grading-owned file.
2. The exact frozen Kotlin snippet for H03 still needs to be pinned down by the notebook owner.
3. The H02 APK build/download path still needs one student-facing recipe so everyone uses the same artifact.
4. The duplicate lesson-H roots still need cleanup under the canonical-source decision.
5. The notebook smoke test still needs to be run after app consolidation.

## Suggested lesson phrasing

- H01: "Find the issue in the source code"
- H02: "Find the manifest-level problem in the APK"
- H03: "Classify the snippet, then record the canonical result"
- H04: "Resolve scanner vs AI disagreement"
- H05: "Confirm that the patch removed the issue"

## Bottom line

For this lesson, the research should be treated as supporting evidence for a small, practical workflow:

- deterministic source scan
- APK inspection
- model-assisted comparison
- human verification
- patch validation

That is the useful overlap. The rest of the broader paper set is background, not lesson-critical material.

## Status

- Owned file updated: `research/2026-lecture-ai-vuln/lesson_h_practical_notes.md`
- Current state: lesson-specific practical guidance is in place and ready for other agents to consume
