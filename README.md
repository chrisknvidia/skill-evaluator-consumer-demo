# SkillEvaluator CI consumer demonstration

This repository demonstrates a separate repository consuming a reusable
SkillEvaluator CI integration.

## How the customer uses it

Open [the customer workflow](.github/workflows/skill-checks.yml). Its single job
calls a reusable workflow from the
[personal SkillEvaluator fork](https://github.com/chrisknvidia/SkillEvaluator-ci-demo),
sets `paths: skills`, and leaves `llm: false`. The workflow and image are pinned
so the recorded result identifies the code that actually ran.

On each push to `main`, pull-request change, or manual **Skill checks** start,
GitHub pulls the already-built image and scans the configured skills. The
consumer does not build the evaluator, install scanners, or need a registry
password.

## Find the results

Open [Actions](https://github.com/chrisknvidia/skill-evaluator-consumer-demo/actions)
and select a **Skill checks** run.

1. **Read the run summary** for each skill's status, actual quality score and
   grade, errors/warnings, and validator evidence. A score is a recorded
   quality assessment, not a percentage of security checks passed.
2. **Open the Tier 1 scan job** for per-skill and per-check diagnostics. Failed
   checks show their recorded reason and suggested fix; GitHub annotations
   highlight actionable failures. Download the **skill-evaluator-tier1**
   artifact for full JSON, HTML, Markdown, SARIF, and stdout/stderr logs.
3. **Open the hosted report** from the summary or PR comment once publication
   completes. Its **Needs attention** section explains failures near the top;
   the skill list links to SkillEvaluator's native HTML report for each skill.
   Searchable findings retain exact source locations and suggested fixes.
   Quality dimensions, N/A checks, and incomplete diagnostics remain distinct.
   The reports support mobile, keyboard navigation, dark mode, offline use,
   print, and downloads of the original JSON evidence.

The configured [report history](https://chrisknvidia.github.io/skill-evaluator-consumer-demo/)
retains each published run and attempt. The
[latest main report](https://chrisknvidia.github.io/skill-evaluator-consumer-demo/main/latest/)
is a stable entry point; `pr/<number>/` is the corresponding stable link for
an eligible same-repository pull request. Permanent run reports live under
`runs/<run-id>/<attempt>/`. Older run reports remain available in history.
The publisher checks the current commit before advancing a main or PR link,
so a delayed old run cannot replace the current result.

Eligible PR runs automatically create or update one bot comment with the
skill scores, failure reasons, and direct report/run links. Publishing is
separate from scanning: the report labels the **CI run conclusion** and
**Tier 1 scan result** independently. A report-publication problem does not
turn a failed scan into a pass.

Hosted reports and automatic PR feedback have been exercised in real GitHub
Actions runs, including the deliberately failing [PR #1](https://github.com/chrisknvidia/skill-evaluator-consumer-demo/pull/1).
Publishing follows scan completion and may take another minute. While it is
pending, read the run summary or download the artifact and open `index.html`
locally. The publisher rebuilds its site from validated JSON; it does not execute
pull-request code or trust artifact-supplied HTML.
Fork-PR report publication and bot comments are not enabled in this example.

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
does not pass this secret. Real credentialed LLM success has not been tested
in this demonstration.
A missing-key test proves configuration rejection, not successful model-backed
analysis; that success needs its own live verification.

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
is excluded from `skills/`. Its malformed name, which does not match its
directory, causes the structural rejection. Its short description also falls
below the recommended level of detail. Negative-test jobs should target that fixture
explicitly and expect validation to fail. Do not include it in the normal
passing collection.

Repository content is available under the MIT license in `LICENSE`.
