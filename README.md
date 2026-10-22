# SkillEvaluator CI consumer demonstration

This repository demonstrates a separate repository consuming a reusable
SkillEvaluator CI integration.

## How the customer uses it

Open [the customer workflow](.github/workflows/skill-checks.yml). Its single job
calls a reusable workflow from the
[personal SkillEvaluator fork](https://github.com/chrisknvidia/SkillEvaluator-ci-demo),
sets `paths: skills`, and leaves `llm: false`. The workflow and image are pinned
so the recorded result identifies the code that actually ran.

On each push to `main` or pull request, GitHub pulls the already-built image,
scans all five skills, and publishes a check plus downloadable reports. The
consumer does not build the evaluator, install scanners, or need a registry
password. Inspect [Actions](../../actions) and open a **Skill checks** run; its
summary lists each skill and its **skill-evaluator-tier1** artifact contains
JSON, HTML, Markdown, SARIF, and logs.

The scan includes all applicable Tier 1 checks, including SkillSpector. No
Tier 2 or Tier 3 evaluation runs. A green check means the requested Tier 1
checks completed and passed; it does not prove real agent performance.

## Try the failure cases

**Verify CI failure handling** is a manually started workflow with three cases:

- `mixed-valid-and-invalid`: scan the five valid skills and the invalid fixture;
  retain all six results, and fail the job.
- `missing-path`: fail clearly when no configured directory exists.
- `missing-llm-key`: request LLM mode without a secret and fail configuration.

Those workflows should be red. They deliberately demonstrate that errors do
not produce a misleading green result. Normal **Skill checks** scans only
`skills/` and excludes the invalid fixture.

## Optional LLM mode

Create an Actions repository secret named `LLM_API_KEY`, then manually start
**Skill checks with LLM** and choose its provider and optional model. This adds
LLM security analysis, finding verification, and rubric evaluation. It makes
billable calls to your selected provider. The normal pull-request workflow
does not pass this secret. Credentialed LLM success must be verified separately
from the static example; a missing-key test is not that verification.

GitHub branch rules can separately require the **Tier 1 scan** check before
merging. This repository demonstrates the check and does not enforce a merge rule.

## Sample content and provenance

The five skills in `skills/` are original synthetic demonstration content,
authored with Codex specifically for this repository. They are not copied
from an external skill catalog and do not represent production-certified
skills. All examples are invented. The `example.com` author address is a
reserved demonstration address, not a contact inbox.

| Skill | Purpose |
| --- | --- |
| `meeting-action-list` | Extract explicit commitments from supplied notes. |
| `acceptance-checklist` | Draft observable checks from a supplied requirement. |
| `release-summary` | Draft release notes from supplied completed changes. |
| `glossary-builder` | Explain terms using only supplied source text. |
| `evidence-table` | Separate supported claims from remaining proof gaps. |

Four skills are text-only. `meeting-action-list` includes an optional Python
standard-library helper that reads one explicitly supplied local CSV and prints
JSON. None require external services or secrets. A pinned `requirements.txt`
in that skill supplies a dependency-audit demonstration inventory; the helper
itself does not need that dependency. CI dependency checks may contact a public
package advisory service. A static validation run assesses their
structure and applicable quality checks; it does not prove their usefulness
in a live agent evaluation.

The intentionally invalid skill at `tests/fixtures/invalid-skill/SKILL.md`
is excluded from `skills/`. It safely demonstrates a structural rejection:
its name is malformed and does not match its directory, and its description
is below the required length. Negative-test jobs should target that fixture
explicitly and expect validation to fail. Do not include it in the normal
passing collection.

Repository content is available under the MIT license in `LICENSE`.
