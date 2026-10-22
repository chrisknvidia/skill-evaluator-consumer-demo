# SkillEvaluator evaluation report

**Tier 1 scan result: FAILED**

6 skills · 5 passed · 1 failed · 0 incomplete

Errors: 2 · Warnings: 28

## Evaluation scope

Tier 1: executed for 6/6 skills with validator evidence; result FAILED\. Tier 2: Not run\. Tier 3: Not run\.

Recorded LLM stages: skipped\. LLM checks disabled by \-\-no\-llm\.

Static scanner outcomes do not establish behavioral usefulness. Not run tiers are not passes.

[Open full report](https://chrisknvidia.github.io/skill-evaluator-consumer-demo/runs/39844380707/1/index.html) · [Workflow run and logs](https://github.com/chrisknvidia/skill-evaluator-consumer-demo/actions/runs/39844380707)

**CI run conclusion:** failure

| Skill | Status | Quality / 100 | Errors | Warnings |
| --- | --- | --- | --- | --- |
| skills/acceptance\-checklist | PASS | 98.2 / A | 0 | 3 |
| skills/evidence\-table | PASS | 98.2 / A | 0 | 3 |
| skills/glossary\-builder | PASS | 98.2 / A | 0 | 3 |
| skills/invalid\-skill | FAIL | 71.8 / C | 2 | 12 |
| skills/meeting\-action\-list | PASS | 98.2 / A | 0 | 4 |
| skills/release\-summary | PASS | 98.2 / A | 0 | 3 |

**skills/invalid\-skill / Schema &amp; Repository Governance:** Field 'name': Value error, Skill name 'INVALID NAME' must be in kebab\-case format \(lowercase letters, numbers, and hyphens only, starting with a letter\)

Location: /workspace/skills/invalid\-skill/SKILL\.md. Suggested fix: Fix the 'name' field in frontmatter according to schema requirements

**skills/invalid\-skill / QUALITY:** Invalid name format: 'INVALID NAME' \(lowercase/numbers/hyphens only\)

Location: /workspace/skills/invalid\-skill/SKILL\.md. Suggested fix: Use only lowercase letters, numbers, and hyphens

[Open full report](https://chrisknvidia.github.io/skill-evaluator-consumer-demo/runs/39844380707/1/index.html) · [Workflow run and logs](https://github.com/chrisknvidia/skill-evaluator-consumer-demo/actions/runs/39844380707)
