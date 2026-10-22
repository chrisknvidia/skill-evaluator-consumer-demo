---
name: acceptance-checklist
description: Converts a stated feature requirement into observable acceptance checks. Use when a small change needs reviewable completion criteria.
license: MIT
metadata:
  author: SkillEvaluator CI Demo Authors <ci-demo@example.com>
  version: 1.0.0
  tags:
    - demonstration
    - text-assistance
---

# Acceptance Checklist

## Purpose
Translate a supplied requirement into concrete checks that a reviewer can observe.

## Prerequisites
Provide a requirement, its intended user, and any known constraints as text.
No repository access or execution environment is required.

## Instructions
1. Identify the outcome the requirement explicitly promises.
2. List the normal user flow using observable inputs and outputs.
3. Add checks for empty input, invalid input, and one relevant boundary value.
4. Include option interactions only when the requirement names those options.
5. Separate assumptions from confirmed requirements.
6. Validate that each check can produce a clear pass or fail result.
7. Record missing details as questions without inventing product behavior.

## Output
Return a checklist grouped into Normal behavior, Edge cases, and Open questions.
Each acceptance check states its starting condition, action, and expected result.
Keep implementation suggestions separate from acceptance criteria.

## Examples
Input:
```text
A search field filters a supplied list by a case-insensitive name match.
```
Output:
```text
- Given names Oak and Pine, searching oak returns Oak.
- Given names Oak and Pine, searching MAPLE returns an empty result.
- Open question: Does an empty query show all names or no names?
```
The empty-query behavior remains unresolved until the requirement defines it.

## Limitations
A written checklist is a proposed verification aid, not evidence that a feature passed.
This skill does not infer deployment, performance, or accessibility guarantees.

## Troubleshooting
If the requirement conflicts with a constraint, flag the conflict before generating dependent checks.
If a result cannot be observed, explain the validation problem and ask for a measurable outcome.
