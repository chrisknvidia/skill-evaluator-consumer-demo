# SkillEvaluator evaluation report

**Tier 1 scan result: FAILED**

6 skills · 5 passed · 1 failed · 0 incomplete

Errors: 2 · Warnings: 28

## Evaluation scope

Tier 1: executed for 6/6 skills with validator evidence; result FAILED\. Tier 2: Not run\. Tier 3: Not run\.

Recorded LLM stages: skipped\. LLM checks disabled by \-\-no\-llm\.

Static scanner outcomes do not establish behavioral usefulness. Not run tiers are not passes.

[Open full report](https://chrisknvidia.github.io/skill-evaluator-consumer-demo/runs/39710576857/1/index.html) · [Workflow run and logs](https://github.com/chrisknvidia/skill-evaluator-consumer-demo/actions/runs/39710576857)

**CI run conclusion:** failure

**Commit:** 36fcb979cc309141ca74f8796386fde1040d6974

**Runtime image:** 

## Needs attention

**skills/invalid\-skill / Schema &amp; Repository Governance (FAIL):** Field &\#x27;name&\#x27;: Value error, Skill name &\#x27;INVALID NAME&\#x27; must be in kebab\-case format \(lowercase letters, numbers, and hyphens only, starting with a letter\)

**skills/invalid\-skill / QUALITY (FAIL):** Invalid name format: &\#x27;INVALID NAME&\#x27; \(lowercase/numbers/hyphens only\)

## Skills and scores

| Skill | Tier 1 | Quality / 100 | Grade | Errors | Warnings |

| --- | --- | --- | --- | --- | --- |

| skills/acceptance\-checklist | PASS | 98.2 | A | 0 | 3 |

| skills/evidence\-table | PASS | 98.2 | A | 0 | 3 |

| skills/glossary\-builder | PASS | 98.2 | A | 0 | 3 |

| skills/invalid\-skill | FAIL | 71.8 | C | 2 | 12 |

| skills/meeting\-action\-list | PASS | 98.2 | A | 0 | 4 |

| skills/release\-summary | PASS | 98.2 | A | 0 | 3 |

## skills/acceptance\-checklist

[JSON](https://chrisknvidia.github.io/skill-evaluator-consumer-demo/runs/39710576857/1/skill-001/skillevaluator-tier1.json)

### Recorded quality dimensions

| Dimension | Score / 100 | Weight | Issues |

| --- | --- | --- | --- |

| correctness | 95 | 0\.35 | 1 |

| discoverability | 100 | 0\.25 | 0 |

| reliability | 100 | 0\.25 | 0 |

| efficiency | 100 | 0\.15 | 0 |

### Validator outcomes

| Validator | Outcome | Checks recorded | Errors | Warnings |

| --- | --- | --- | --- | --- |

| Schema &amp; Repository Governance | PASS | 11 | 0 | 1 |

| Semantic Version Validation | PASS | 1 | 0 | 0 |

| Security Scan | PASS | 1 | 0 | 0 |

| PII Scan | PASS | 2 | 0 | 0 |

| License Compliance | PASS | 1 | 0 | 0 |

| Code Risk Analysis | NOT APPLICABLE | 1 | 0 | 0 |

| Secrets Detection | PASS | 1 | 0 | 0 |

| Code Integrity &amp; Hygiene | PASS | 4 | 0 | 1 |

| Dependency Vulnerability Audit | NOT APPLICABLE | 1 | 0 | 0 |

| Unicode Smuggling Detection | PASS | 1 | 0 | 0 |

| QUALITY | PASS | 1 | 0 | 1 |

| SCRIPT\_LINT | NOT APPLICABLE | 1 | 0 | 0 |

### Schema &amp; Repository Governance — evidence

**Evidence: manifest\_exists:** Found skill manifest: SKILL\.md

**Evidence metadata:** \{&quot;file\_path&quot;: &quot;/workspace/skills/acceptance\-checklist/SKILL\.md&quot;\}

**Evidence: frontmatter\_valid:** Valid frontmatter for skill &\#x27;acceptance\-checklist&\#x27;

**Evidence metadata:** \{&quot;description\_length&quot;: 134\}

**Evidence: folder\_hierarchy:** Valid general skill structure: skills/acceptance\-checklist/

**Evidence: naming\_convention:** Folder name &\#x27;acceptance\-checklist&\#x27; follows kebab\-case convention

**Evidence metadata:** \{&quot;name\_length&quot;: 20\}

**Evidence: line\_count:** SKILL\.md within line limit \(55/500\)

**Evidence metadata:** \{&quot;limit&quot;: 500, &quot;line\_count&quot;: 55\}

**Evidence: body\_heading:** Body contains a top\-level heading

**Evidence: body\_recommended\_section:** Found recommended section: &\#x27;\#\# Instructions&\#x27; \(or &\#x27;\#\# Usage&\#x27;\)

**Evidence: body\_recommended\_section:** Found recommended section: &\#x27;\#\# Examples&\#x27;

**Evidence: optional\_files:** Skill directory contains only expected files

**Evidence: name\_consistency:** Directory name matches frontmatter: &\#x27;acceptance\-checklist&\#x27;

**Evidence: author\_format:** Valid author format: SkillEvaluator CI Demo Authors &lt;ci\-demo@​example\.com&gt;

**Warning:** Workflow scope: llm skipped\. LLM checks disabled by \-\-no\-llm\.

**Scanner message:** \[OK\] manifest\_exists: Found skill manifest: SKILL\.md

**Scanner message:** \[OK\] frontmatter\_valid: Valid frontmatter for skill &\#x27;acceptance\-checklist&\#x27;

**Scanner message:** \[OK\] folder\_hierarchy: Valid general skill structure: skills/acceptance\-checklist/

**Scanner message:** \[OK\] naming\_convention: Folder name &\#x27;acceptance\-checklist&\#x27; follows kebab\-case convention

**Scanner message:** \[OK\] line\_count: SKILL\.md within line limit \(55/500\)

**Scanner message:** \[OK\] body\_heading: Body contains a top\-level heading

**Scanner message:** \[OK\] body\_recommended\_section: Found recommended section: &\#x27;\#\# Instructions&\#x27; \(or &\#x27;\#\# Usage&\#x27;\)

**Scanner message:** \[OK\] body\_recommended\_section: Found recommended section: &\#x27;\#\# Examples&\#x27;

**Scanner message:** \[OK\] optional\_files: Skill directory contains only expected files

**Scanner message:** \[OK\] name\_consistency: Directory name matches frontmatter: &\#x27;acceptance\-checklist&\#x27;

**Scanner message:** \[OK\] author\_format: Valid author format: SkillEvaluator CI Demo Authors &lt;ci\-demo@​example\.com&gt;

### Semantic Version Validation — evidence

**Evidence: version\_semver:** Valid semantic version: 1\.0\.0

**Evidence metadata:** \{&quot;previous\_version&quot;: null, &quot;version&quot;: &quot;1\.0\.0&quot;\}

**Scanner message:** \[OK\] version\_semver: Valid semantic version: 1\.0\.0

### Security Scan — evidence

**Evidence: skillspector:** No security vulnerabilities detected \(secrets, API keys, credentials\)

**Scanner message:** \[OK\] skillspector: No security vulnerabilities detected \(secrets, API keys, credentials\)

### PII Scan — evidence

**Evidence: pii\_scan\_start:** Scanning 1 files for PII

**Evidence metadata:** \{&quot;file\_count&quot;: 1\}

**Evidence: pii\_detection:** No PII detected in 1 files \(emails, SSNs, phone numbers, paths\)

**Evidence metadata:** \{&quot;files\_scanned&quot;: 1\}

**Scanner message:** \[OK\] pii\_scan\_start: Scanning 1 files for PII

**Scanner message:** \[OK\] pii\_detection: No PII detected in 1 files \(emails, SSNs, phone numbers, paths\)

### License Compliance — evidence

**Evidence: license\_compliance:** License compliance scan completed \(allowed\)

**Evidence metadata:** \{&quot;license\_status&quot;: &quot;allowed&quot;\}

**Scanner message:** Tier 1: Found license declaration in frontmatter \(SKILL\.md\)

**Scanner message:** License: MIT \(ALLOWED \- permissive\)

**Scanner message:** \[OK\] license\_compliance: License compliance scan completed \(allowed\)

### Code Risk Analysis — evidence

**Evidence: code\_file\_discovery:** No code files found \- code risk analysis is not applicable

**Evidence metadata:** \{&quot;file\_counts&quot;: \{&quot;js&quot;: 0, &quot;py&quot;: 0, &quot;sh&quot;: 0\}\}

**Scanner message:** \[OK\] code\_file\_discovery: No code files found \- code risk analysis is not applicable

### Secrets Detection — evidence

**Evidence: gitleaks:** No secrets detected by Gitleaks

**Scanner message:** \[OK\] gitleaks: No secrets detected by Gitleaks

### Code Integrity &amp; Hygiene — evidence

**Evidence: dead\_links\_scan:** Checking 1 markdown files for dead links

**Evidence metadata:** \{&quot;file\_count&quot;: 1\}

**Evidence: dead\_links:** All relative links valid in 1 markdown file\(s\)

**Evidence metadata:** \{&quot;files\_checked&quot;: 1\}

**Evidence: dependencies:** No dependency files found \(requirements\.txt, pyproject\.toml\)

**Evidence: test\_discovery:** No standard Python test\-file candidates found; target tests were not executed and coverage was not measured\. Consider adding tests\.

**Evidence metadata:** \{&quot;coverage\_measured&quot;: false, &quot;execution\_performed&quot;: false, &quot;patterns&quot;: \[&quot;test\_\*\.py&quot;, &quot;\*\_test\.py&quot;\], &quot;test\_count&quot;: 0\}

**Warning:** No standard Python test\-file candidates found; consider adding tests

**Scanner message:** \[OK\] dead\_links\_scan: Checking 1 markdown files for dead links

**Scanner message:** \[OK\] dead\_links: All relative links valid in 1 markdown file\(s\)

**Scanner message:** \[OK\] dependencies: No dependency files found \(requirements\.txt, pyproject\.toml\)

**Scanner message:** \[OK\] test\_discovery: No standard Python test\-file candidates found; target tests were not executed and coverage was not measured\. Consider adding tests\.

### Dependency Vulnerability Audit — evidence

**Evidence: dependency\_file\_discovery:** No dependency files found \- vulnerability audit is not applicable

**Scanner message:** \[OK\] dependency\_file\_discovery: No dependency files found \- vulnerability audit is not applicable

### Unicode Smuggling Detection — evidence

**Evidence: unicode\_scan:** No invisible Unicode characters detected in 1 file\(s\)

**Evidence metadata:** \{&quot;files\_scanned&quot;: 1\}

**Scanner message:** \[OK\] unicode\_scan: No invisible Unicode characters detected in 1 file\(s\)

### QUALITY — evidence

**Evidence: quality\_score:** Score: 98\.2/100 \(Grade: A\)

**Evidence metadata:** \{&quot;grade&quot;: &quot;A&quot;, &quot;overall\_score&quot;: 98\.2, &quot;skill\_type&quot;: &quot;guide\-only&quot;\}

**Finding: quality\_correctness \(medium\):** SKILL\_SPEC recommended field missing: &\#x27;version&\#x27;

**File:** /workspace/skills/acceptance\-checklist/SKILL\.md

**Suggested fix:** Add &\#x27;version&\#x27; to frontmatter — Semantic version \(e\.g\., &quot;1\.0\.0&quot;\)

**Finding metadata:** \{&quot;deduction&quot;: 5, &quot;dimension&quot;: &quot;correctness&quot;\}

**Warning:** \[QUALITY\-MEDIUM\] SKILL\_SPEC recommended field missing: &\#x27;version&\#x27; in /workspace/skills/acceptance\-checklist/SKILL\.md

**Scanner message:** \[OK\] quality\_score: Score: 98\.2/100 \(Grade: A\)

### SCRIPT\_LINT — evidence

**Evidence: lint:** No scripts/ or tools/ directory found

**Scanner message:** \[OK\] lint: No scripts/ or tools/ directory found

## skills/evidence\-table

[JSON](https://chrisknvidia.github.io/skill-evaluator-consumer-demo/runs/39710576857/1/skill-002/skillevaluator-tier1.json)

### Recorded quality dimensions

| Dimension | Score / 100 | Weight | Issues |

| --- | --- | --- | --- |

| correctness | 95 | 0\.35 | 1 |

| discoverability | 100 | 0\.25 | 0 |

| reliability | 100 | 0\.25 | 0 |

| efficiency | 100 | 0\.15 | 0 |

### Validator outcomes

| Validator | Outcome | Checks recorded | Errors | Warnings |

| --- | --- | --- | --- | --- |

| Schema &amp; Repository Governance | PASS | 11 | 0 | 1 |

| Semantic Version Validation | PASS | 1 | 0 | 0 |

| Security Scan | PASS | 1 | 0 | 0 |

| PII Scan | PASS | 2 | 0 | 0 |

| License Compliance | PASS | 1 | 0 | 0 |

| Code Risk Analysis | NOT APPLICABLE | 1 | 0 | 0 |

| Secrets Detection | PASS | 1 | 0 | 0 |

| Code Integrity &amp; Hygiene | PASS | 4 | 0 | 1 |

| Dependency Vulnerability Audit | NOT APPLICABLE | 1 | 0 | 0 |

| Unicode Smuggling Detection | PASS | 1 | 0 | 0 |

| QUALITY | PASS | 1 | 0 | 1 |

| SCRIPT\_LINT | NOT APPLICABLE | 1 | 0 | 0 |

### Schema &amp; Repository Governance — evidence

**Evidence: manifest\_exists:** Found skill manifest: SKILL\.md

**Evidence metadata:** \{&quot;file\_path&quot;: &quot;/workspace/skills/evidence\-table/SKILL\.md&quot;\}

**Evidence: frontmatter\_valid:** Valid frontmatter for skill &\#x27;evidence\-table&\#x27;

**Evidence metadata:** \{&quot;description\_length&quot;: 142\}

**Evidence: folder\_hierarchy:** Valid general skill structure: skills/evidence\-table/

**Evidence: naming\_convention:** Folder name &\#x27;evidence\-table&\#x27; follows kebab\-case convention

**Evidence metadata:** \{&quot;name\_length&quot;: 14\}

**Evidence: line\_count:** SKILL\.md within line limit \(57/500\)

**Evidence metadata:** \{&quot;limit&quot;: 500, &quot;line\_count&quot;: 57\}

**Evidence: body\_heading:** Body contains a top\-level heading

**Evidence: body\_recommended\_section:** Found recommended section: &\#x27;\#\# Instructions&\#x27; \(or &\#x27;\#\# Usage&\#x27;\)

**Evidence: body\_recommended\_section:** Found recommended section: &\#x27;\#\# Examples&\#x27;

**Evidence: optional\_files:** Skill directory contains only expected files

**Evidence: name\_consistency:** Directory name matches frontmatter: &\#x27;evidence\-table&\#x27;

**Evidence: author\_format:** Valid author format: SkillEvaluator CI Demo Authors &lt;ci\-demo@​example\.com&gt;

**Warning:** Workflow scope: llm skipped\. LLM checks disabled by \-\-no\-llm\.

**Scanner message:** \[OK\] manifest\_exists: Found skill manifest: SKILL\.md

**Scanner message:** \[OK\] frontmatter\_valid: Valid frontmatter for skill &\#x27;evidence\-table&\#x27;

**Scanner message:** \[OK\] folder\_hierarchy: Valid general skill structure: skills/evidence\-table/

**Scanner message:** \[OK\] naming\_convention: Folder name &\#x27;evidence\-table&\#x27; follows kebab\-case convention

**Scanner message:** \[OK\] line\_count: SKILL\.md within line limit \(57/500\)

**Scanner message:** \[OK\] body\_heading: Body contains a top\-level heading

**Scanner message:** \[OK\] body\_recommended\_section: Found recommended section: &\#x27;\#\# Instructions&\#x27; \(or &\#x27;\#\# Usage&\#x27;\)

**Scanner message:** \[OK\] body\_recommended\_section: Found recommended section: &\#x27;\#\# Examples&\#x27;

**Scanner message:** \[OK\] optional\_files: Skill directory contains only expected files

**Scanner message:** \[OK\] name\_consistency: Directory name matches frontmatter: &\#x27;evidence\-table&\#x27;

**Scanner message:** \[OK\] author\_format: Valid author format: SkillEvaluator CI Demo Authors &lt;ci\-demo@​example\.com&gt;

### Semantic Version Validation — evidence

**Evidence: version\_semver:** Valid semantic version: 1\.0\.0

**Evidence metadata:** \{&quot;previous\_version&quot;: null, &quot;version&quot;: &quot;1\.0\.0&quot;\}

**Scanner message:** \[OK\] version\_semver: Valid semantic version: 1\.0\.0

### Security Scan — evidence

**Evidence: skillspector:** No security vulnerabilities detected \(secrets, API keys, credentials\)

**Scanner message:** \[OK\] skillspector: No security vulnerabilities detected \(secrets, API keys, credentials\)

### PII Scan — evidence

**Evidence: pii\_scan\_start:** Scanning 1 files for PII

**Evidence metadata:** \{&quot;file\_count&quot;: 1\}

**Evidence: pii\_detection:** No PII detected in 1 files \(emails, SSNs, phone numbers, paths\)

**Evidence metadata:** \{&quot;files\_scanned&quot;: 1\}

**Scanner message:** \[OK\] pii\_scan\_start: Scanning 1 files for PII

**Scanner message:** \[OK\] pii\_detection: No PII detected in 1 files \(emails, SSNs, phone numbers, paths\)

### License Compliance — evidence

**Evidence: license\_compliance:** License compliance scan completed \(allowed\)

**Evidence metadata:** \{&quot;license\_status&quot;: &quot;allowed&quot;\}

**Scanner message:** Tier 1: Found license declaration in frontmatter \(SKILL\.md\)

**Scanner message:** License: MIT \(ALLOWED \- permissive\)

**Scanner message:** \[OK\] license\_compliance: License compliance scan completed \(allowed\)

### Code Risk Analysis — evidence

**Evidence: code\_file\_discovery:** No code files found \- code risk analysis is not applicable

**Evidence metadata:** \{&quot;file\_counts&quot;: \{&quot;js&quot;: 0, &quot;py&quot;: 0, &quot;sh&quot;: 0\}\}

**Scanner message:** \[OK\] code\_file\_discovery: No code files found \- code risk analysis is not applicable

### Secrets Detection — evidence

**Evidence: gitleaks:** No secrets detected by Gitleaks

**Scanner message:** \[OK\] gitleaks: No secrets detected by Gitleaks

### Code Integrity &amp; Hygiene — evidence

**Evidence: dead\_links\_scan:** Checking 1 markdown files for dead links

**Evidence metadata:** \{&quot;file\_count&quot;: 1\}

**Evidence: dead\_links:** All relative links valid in 1 markdown file\(s\)

**Evidence metadata:** \{&quot;files\_checked&quot;: 1\}

**Evidence: dependencies:** No dependency files found \(requirements\.txt, pyproject\.toml\)

**Evidence: test\_discovery:** No standard Python test\-file candidates found; target tests were not executed and coverage was not measured\. Consider adding tests\.

**Evidence metadata:** \{&quot;coverage\_measured&quot;: false, &quot;execution\_performed&quot;: false, &quot;patterns&quot;: \[&quot;test\_\*\.py&quot;, &quot;\*\_test\.py&quot;\], &quot;test\_count&quot;: 0\}

**Warning:** No standard Python test\-file candidates found; consider adding tests

**Scanner message:** \[OK\] dead\_links\_scan: Checking 1 markdown files for dead links

**Scanner message:** \[OK\] dead\_links: All relative links valid in 1 markdown file\(s\)

**Scanner message:** \[OK\] dependencies: No dependency files found \(requirements\.txt, pyproject\.toml\)

**Scanner message:** \[OK\] test\_discovery: No standard Python test\-file candidates found; target tests were not executed and coverage was not measured\. Consider adding tests\.

### Dependency Vulnerability Audit — evidence

**Evidence: dependency\_file\_discovery:** No dependency files found \- vulnerability audit is not applicable

**Scanner message:** \[OK\] dependency\_file\_discovery: No dependency files found \- vulnerability audit is not applicable

### Unicode Smuggling Detection — evidence

**Evidence: unicode\_scan:** No invisible Unicode characters detected in 1 file\(s\)

**Evidence metadata:** \{&quot;files\_scanned&quot;: 1\}

**Scanner message:** \[OK\] unicode\_scan: No invisible Unicode characters detected in 1 file\(s\)

### QUALITY — evidence

**Evidence: quality\_score:** Score: 98\.2/100 \(Grade: A\)

**Evidence metadata:** \{&quot;grade&quot;: &quot;A&quot;, &quot;overall\_score&quot;: 98\.2, &quot;skill\_type&quot;: &quot;guide\-only&quot;\}

**Finding: quality\_correctness \(medium\):** SKILL\_SPEC recommended field missing: &\#x27;version&\#x27;

**File:** /workspace/skills/evidence\-table/SKILL\.md

**Suggested fix:** Add &\#x27;version&\#x27; to frontmatter — Semantic version \(e\.g\., &quot;1\.0\.0&quot;\)

**Finding metadata:** \{&quot;deduction&quot;: 5, &quot;dimension&quot;: &quot;correctness&quot;\}

**Warning:** \[QUALITY\-MEDIUM\] SKILL\_SPEC recommended field missing: &\#x27;version&\#x27; in /workspace/skills/evidence\-table/SKILL\.md

**Scanner message:** \[OK\] quality\_score: Score: 98\.2/100 \(Grade: A\)

### SCRIPT\_LINT — evidence

**Evidence: lint:** No scripts/ or tools/ directory found

**Scanner message:** \[OK\] lint: No scripts/ or tools/ directory found

## skills/glossary\-builder

[JSON](https://chrisknvidia.github.io/skill-evaluator-consumer-demo/runs/39710576857/1/skill-003/skillevaluator-tier1.json)

### Recorded quality dimensions

| Dimension | Score / 100 | Weight | Issues |

| --- | --- | --- | --- |

| correctness | 95 | 0\.35 | 1 |

| discoverability | 100 | 0\.25 | 0 |

| reliability | 100 | 0\.25 | 0 |

| efficiency | 100 | 0\.15 | 0 |

### Validator outcomes

| Validator | Outcome | Checks recorded | Errors | Warnings |

| --- | --- | --- | --- | --- |

| Schema &amp; Repository Governance | PASS | 11 | 0 | 1 |

| Semantic Version Validation | PASS | 1 | 0 | 0 |

| Security Scan | PASS | 1 | 0 | 0 |

| PII Scan | PASS | 2 | 0 | 0 |

| License Compliance | PASS | 1 | 0 | 0 |

| Code Risk Analysis | NOT APPLICABLE | 1 | 0 | 0 |

| Secrets Detection | PASS | 1 | 0 | 0 |

| Code Integrity &amp; Hygiene | PASS | 4 | 0 | 1 |

| Dependency Vulnerability Audit | NOT APPLICABLE | 1 | 0 | 0 |

| Unicode Smuggling Detection | PASS | 1 | 0 | 0 |

| QUALITY | PASS | 1 | 0 | 1 |

| SCRIPT\_LINT | NOT APPLICABLE | 1 | 0 | 0 |

### Schema &amp; Repository Governance — evidence

**Evidence: manifest\_exists:** Found skill manifest: SKILL\.md

**Evidence metadata:** \{&quot;file\_path&quot;: &quot;/workspace/skills/glossary\-builder/SKILL\.md&quot;\}

**Evidence: frontmatter\_valid:** Valid frontmatter for skill &\#x27;glossary\-builder&\#x27;

**Evidence metadata:** \{&quot;description\_length&quot;: 133\}

**Evidence: folder\_hierarchy:** Valid general skill structure: skills/glossary\-builder/

**Evidence: naming\_convention:** Folder name &\#x27;glossary\-builder&\#x27; follows kebab\-case convention

**Evidence metadata:** \{&quot;name\_length&quot;: 16\}

**Evidence: line\_count:** SKILL\.md within line limit \(55/500\)

**Evidence metadata:** \{&quot;limit&quot;: 500, &quot;line\_count&quot;: 55\}

**Evidence: body\_heading:** Body contains a top\-level heading

**Evidence: body\_recommended\_section:** Found recommended section: &\#x27;\#\# Instructions&\#x27; \(or &\#x27;\#\# Usage&\#x27;\)

**Evidence: body\_recommended\_section:** Found recommended section: &\#x27;\#\# Examples&\#x27;

**Evidence: optional\_files:** Skill directory contains only expected files

**Evidence: name\_consistency:** Directory name matches frontmatter: &\#x27;glossary\-builder&\#x27;

**Evidence: author\_format:** Valid author format: SkillEvaluator CI Demo Authors &lt;ci\-demo@​example\.com&gt;

**Warning:** Workflow scope: llm skipped\. LLM checks disabled by \-\-no\-llm\.

**Scanner message:** \[OK\] manifest\_exists: Found skill manifest: SKILL\.md

**Scanner message:** \[OK\] frontmatter\_valid: Valid frontmatter for skill &\#x27;glossary\-builder&\#x27;

**Scanner message:** \[OK\] folder\_hierarchy: Valid general skill structure: skills/glossary\-builder/

**Scanner message:** \[OK\] naming\_convention: Folder name &\#x27;glossary\-builder&\#x27; follows kebab\-case convention

**Scanner message:** \[OK\] line\_count: SKILL\.md within line limit \(55/500\)

**Scanner message:** \[OK\] body\_heading: Body contains a top\-level heading

**Scanner message:** \[OK\] body\_recommended\_section: Found recommended section: &\#x27;\#\# Instructions&\#x27; \(or &\#x27;\#\# Usage&\#x27;\)

**Scanner message:** \[OK\] body\_recommended\_section: Found recommended section: &\#x27;\#\# Examples&\#x27;

**Scanner message:** \[OK\] optional\_files: Skill directory contains only expected files

**Scanner message:** \[OK\] name\_consistency: Directory name matches frontmatter: &\#x27;glossary\-builder&\#x27;

**Scanner message:** \[OK\] author\_format: Valid author format: SkillEvaluator CI Demo Authors &lt;ci\-demo@​example\.com&gt;

### Semantic Version Validation — evidence

**Evidence: version\_semver:** Valid semantic version: 1\.0\.0

**Evidence metadata:** \{&quot;previous\_version&quot;: null, &quot;version&quot;: &quot;1\.0\.0&quot;\}

**Scanner message:** \[OK\] version\_semver: Valid semantic version: 1\.0\.0

### Security Scan — evidence

**Evidence: skillspector:** No security vulnerabilities detected \(secrets, API keys, credentials\)

**Scanner message:** \[OK\] skillspector: No security vulnerabilities detected \(secrets, API keys, credentials\)

### PII Scan — evidence

**Evidence: pii\_scan\_start:** Scanning 1 files for PII

**Evidence metadata:** \{&quot;file\_count&quot;: 1\}

**Evidence: pii\_detection:** No PII detected in 1 files \(emails, SSNs, phone numbers, paths\)

**Evidence metadata:** \{&quot;files\_scanned&quot;: 1\}

**Scanner message:** \[OK\] pii\_scan\_start: Scanning 1 files for PII

**Scanner message:** \[OK\] pii\_detection: No PII detected in 1 files \(emails, SSNs, phone numbers, paths\)

### License Compliance — evidence

**Evidence: license\_compliance:** License compliance scan completed \(allowed\)

**Evidence metadata:** \{&quot;license\_status&quot;: &quot;allowed&quot;\}

**Scanner message:** Tier 1: Found license declaration in frontmatter \(SKILL\.md\)

**Scanner message:** License: MIT \(ALLOWED \- permissive\)

**Scanner message:** \[OK\] license\_compliance: License compliance scan completed \(allowed\)

### Code Risk Analysis — evidence

**Evidence: code\_file\_discovery:** No code files found \- code risk analysis is not applicable

**Evidence metadata:** \{&quot;file\_counts&quot;: \{&quot;js&quot;: 0, &quot;py&quot;: 0, &quot;sh&quot;: 0\}\}

**Scanner message:** \[OK\] code\_file\_discovery: No code files found \- code risk analysis is not applicable

### Secrets Detection — evidence

**Evidence: gitleaks:** No secrets detected by Gitleaks

**Scanner message:** \[OK\] gitleaks: No secrets detected by Gitleaks

### Code Integrity &amp; Hygiene — evidence

**Evidence: dead\_links\_scan:** Checking 1 markdown files for dead links

**Evidence metadata:** \{&quot;file\_count&quot;: 1\}

**Evidence: dead\_links:** All relative links valid in 1 markdown file\(s\)

**Evidence metadata:** \{&quot;files\_checked&quot;: 1\}

**Evidence: dependencies:** No dependency files found \(requirements\.txt, pyproject\.toml\)

**Evidence: test\_discovery:** No standard Python test\-file candidates found; target tests were not executed and coverage was not measured\. Consider adding tests\.

**Evidence metadata:** \{&quot;coverage\_measured&quot;: false, &quot;execution\_performed&quot;: false, &quot;patterns&quot;: \[&quot;test\_\*\.py&quot;, &quot;\*\_test\.py&quot;\], &quot;test\_count&quot;: 0\}

**Warning:** No standard Python test\-file candidates found; consider adding tests

**Scanner message:** \[OK\] dead\_links\_scan: Checking 1 markdown files for dead links

**Scanner message:** \[OK\] dead\_links: All relative links valid in 1 markdown file\(s\)

**Scanner message:** \[OK\] dependencies: No dependency files found \(requirements\.txt, pyproject\.toml\)

**Scanner message:** \[OK\] test\_discovery: No standard Python test\-file candidates found; target tests were not executed and coverage was not measured\. Consider adding tests\.

### Dependency Vulnerability Audit — evidence

**Evidence: dependency\_file\_discovery:** No dependency files found \- vulnerability audit is not applicable

**Scanner message:** \[OK\] dependency\_file\_discovery: No dependency files found \- vulnerability audit is not applicable

### Unicode Smuggling Detection — evidence

**Evidence: unicode\_scan:** No invisible Unicode characters detected in 1 file\(s\)

**Evidence metadata:** \{&quot;files\_scanned&quot;: 1\}

**Scanner message:** \[OK\] unicode\_scan: No invisible Unicode characters detected in 1 file\(s\)

### QUALITY — evidence

**Evidence: quality\_score:** Score: 98\.2/100 \(Grade: A\)

**Evidence metadata:** \{&quot;grade&quot;: &quot;A&quot;, &quot;overall\_score&quot;: 98\.2, &quot;skill\_type&quot;: &quot;guide\-only&quot;\}

**Finding: quality\_correctness \(medium\):** SKILL\_SPEC recommended field missing: &\#x27;version&\#x27;

**File:** /workspace/skills/glossary\-builder/SKILL\.md

**Suggested fix:** Add &\#x27;version&\#x27; to frontmatter — Semantic version \(e\.g\., &quot;1\.0\.0&quot;\)

**Finding metadata:** \{&quot;deduction&quot;: 5, &quot;dimension&quot;: &quot;correctness&quot;\}

**Warning:** \[QUALITY\-MEDIUM\] SKILL\_SPEC recommended field missing: &\#x27;version&\#x27; in /workspace/skills/glossary\-builder/SKILL\.md

**Scanner message:** \[OK\] quality\_score: Score: 98\.2/100 \(Grade: A\)

### SCRIPT\_LINT — evidence

**Evidence: lint:** No scripts/ or tools/ directory found

**Scanner message:** \[OK\] lint: No scripts/ or tools/ directory found

## skills/invalid\-skill

[JSON](https://chrisknvidia.github.io/skill-evaluator-consumer-demo/runs/39710576857/1/skill-004/skillevaluator-tier1.json)

### Recorded quality dimensions

| Dimension | Score / 100 | Weight | Issues |

| --- | --- | --- | --- |

| correctness | 55 | 0\.35 | 5 |

| discoverability | 65 | 0\.25 | 3 |

| reliability | 85 | 0\.25 | 3 |

| efficiency | 100 | 0\.15 | 0 |

### Validator outcomes

| Validator | Outcome | Checks recorded | Errors | Warnings |

| --- | --- | --- | --- | --- |

| Schema &amp; Repository Governance | FAIL | 1 | 1 | 1 |

| Semantic Version Validation | NOT APPLICABLE | 1 | 0 | 0 |

| Security Scan | PASS | 1 | 0 | 0 |

| PII Scan | PASS | 2 | 0 | 0 |

| License Compliance | PASS | 1 | 0 | 0 |

| Code Risk Analysis | NOT APPLICABLE | 1 | 0 | 0 |

| Secrets Detection | PASS | 1 | 0 | 0 |

| Code Integrity &amp; Hygiene | PASS | 4 | 0 | 1 |

| Dependency Vulnerability Audit | NOT APPLICABLE | 1 | 0 | 0 |

| Unicode Smuggling Detection | PASS | 1 | 0 | 0 |

| QUALITY | FAIL | 1 | 1 | 10 |

| SCRIPT\_LINT | NOT APPLICABLE | 1 | 0 | 0 |

### Schema &amp; Repository Governance — evidence

**Evidence: manifest\_exists:** Found skill manifest: SKILL\.md

**Evidence metadata:** \{&quot;file\_path&quot;: &quot;/workspace/skills/invalid\-skill/SKILL\.md&quot;\}

**Finding: frontmatter\_field \(high\):** Field &\#x27;name&\#x27;: Value error, Skill name &\#x27;INVALID NAME&\#x27; must be in kebab\-case format \(lowercase letters, numbers, and hyphens only, starting with a letter\)

**File:** /workspace/skills/invalid\-skill/SKILL\.md

**Suggested fix:** Fix the &\#x27;name&\#x27; field in frontmatter according to schema requirements

**Finding metadata:** \{&quot;error\_type&quot;: &quot;value\_error&quot;, &quot;field&quot;: &quot;name&quot;\}

**Error:** \[SCHEMA\-HIGH\] Field &\#x27;name&\#x27;: Value error, Skill name &\#x27;INVALID NAME&\#x27; must be in kebab\-case format \(lowercase letters, numbers, and hyphens only, starting with a letter\) in /workspace/skills/invalid\-skill/SKILL\.md

**Warning:** Workflow scope: llm skipped\. LLM checks disabled by \-\-no\-llm\.

**Scanner message:** \[OK\] manifest\_exists: Found skill manifest: SKILL\.md

### Semantic Version Validation — evidence

**Evidence: version\_optional:** No semantic version label present; resource will use commit\-hash history

**Evidence metadata:** \{&quot;previous\_version&quot;: null\}

**Scanner message:** \[OK\] version\_optional: No semantic version label present; resource will use commit\-hash history

### Security Scan — evidence

**Evidence: skillspector:** No security vulnerabilities detected \(secrets, API keys, credentials\)

**Scanner message:** \[OK\] skillspector: No security vulnerabilities detected \(secrets, API keys, credentials\)

### PII Scan — evidence

**Evidence: pii\_scan\_start:** Scanning 1 files for PII

**Evidence metadata:** \{&quot;file\_count&quot;: 1\}

**Evidence: pii\_detection:** No PII detected in 1 files \(emails, SSNs, phone numbers, paths\)

**Evidence metadata:** \{&quot;files\_scanned&quot;: 1\}

**Scanner message:** \[OK\] pii\_scan\_start: Scanning 1 files for PII

**Scanner message:** \[OK\] pii\_detection: No PII detected in 1 files \(emails, SSNs, phone numbers, paths\)

### License Compliance — evidence

**Evidence: license\_compliance:** License compliance scan completed \(allowed\)

**Evidence metadata:** \{&quot;license\_status&quot;: &quot;allowed&quot;\}

**Scanner message:** Tier 1: Found license declaration in frontmatter \(SKILL\.md\)

**Scanner message:** License: MIT \(ALLOWED \- permissive\)

**Scanner message:** \[OK\] license\_compliance: License compliance scan completed \(allowed\)

### Code Risk Analysis — evidence

**Evidence: code\_file\_discovery:** No code files found \- code risk analysis is not applicable

**Evidence metadata:** \{&quot;file\_counts&quot;: \{&quot;js&quot;: 0, &quot;py&quot;: 0, &quot;sh&quot;: 0\}\}

**Scanner message:** \[OK\] code\_file\_discovery: No code files found \- code risk analysis is not applicable

### Secrets Detection — evidence

**Evidence: gitleaks:** No secrets detected by Gitleaks

**Scanner message:** \[OK\] gitleaks: No secrets detected by Gitleaks

### Code Integrity &amp; Hygiene — evidence

**Evidence: dead\_links\_scan:** Checking 1 markdown files for dead links

**Evidence metadata:** \{&quot;file\_count&quot;: 1\}

**Evidence: dead\_links:** All relative links valid in 1 markdown file\(s\)

**Evidence metadata:** \{&quot;files\_checked&quot;: 1\}

**Evidence: dependencies:** No dependency files found \(requirements\.txt, pyproject\.toml\)

**Evidence: test\_discovery:** No standard Python test\-file candidates found; target tests were not executed and coverage was not measured\. Consider adding tests\.

**Evidence metadata:** \{&quot;coverage\_measured&quot;: false, &quot;execution\_performed&quot;: false, &quot;patterns&quot;: \[&quot;test\_\*\.py&quot;, &quot;\*\_test\.py&quot;\], &quot;test\_count&quot;: 0\}

**Warning:** No standard Python test\-file candidates found; consider adding tests

**Scanner message:** \[OK\] dead\_links\_scan: Checking 1 markdown files for dead links

**Scanner message:** \[OK\] dead\_links: All relative links valid in 1 markdown file\(s\)

**Scanner message:** \[OK\] dependencies: No dependency files found \(requirements\.txt, pyproject\.toml\)

**Scanner message:** \[OK\] test\_discovery: No standard Python test\-file candidates found; target tests were not executed and coverage was not measured\. Consider adding tests\.

### Dependency Vulnerability Audit — evidence

**Evidence: dependency\_file\_discovery:** No dependency files found \- vulnerability audit is not applicable

**Scanner message:** \[OK\] dependency\_file\_discovery: No dependency files found \- vulnerability audit is not applicable

### Unicode Smuggling Detection — evidence

**Evidence: unicode\_scan:** No invisible Unicode characters detected in 1 file\(s\)

**Evidence metadata:** \{&quot;files\_scanned&quot;: 1\}

**Scanner message:** \[OK\] unicode\_scan: No invisible Unicode characters detected in 1 file\(s\)

### QUALITY — evidence

**Evidence: quality\_score:** Score: 71\.8/100 \(Grade: C\)

**Evidence metadata:** \{&quot;grade&quot;: &quot;C&quot;, &quot;overall\_score&quot;: 71\.8, &quot;skill\_type&quot;: &quot;guide\-only&quot;\}

**Finding: quality\_correctness \(high\):** Invalid name format: &\#x27;INVALID NAME&\#x27; \(lowercase/numbers/hyphens only\)

**File:** /workspace/skills/invalid\-skill/SKILL\.md

**Suggested fix:** Use only lowercase letters, numbers, and hyphens

**Finding metadata:** \{&quot;deduction&quot;: 15, &quot;dimension&quot;: &quot;correctness&quot;\}

**Finding: quality\_correctness \(medium\):** Guide\-only skill has very little content \(10 lines\)

**File:** /workspace/skills/invalid\-skill/SKILL\.md

**Suggested fix:** Guide skills should have detailed instructions since they have no code

**Finding metadata:** \{&quot;deduction&quot;: 15, &quot;dimension&quot;: &quot;correctness&quot;\}

**Finding: quality\_correctness \(low\):** No examples provided

**File:** /workspace/skills/invalid\-skill/SKILL\.md

**Suggested fix:** Add example usage with code blocks

**Finding metadata:** \{&quot;deduction&quot;: 5, &quot;dimension&quot;: &quot;correctness&quot;\}

**Finding: quality\_correctness \(medium\):** SKILL\_SPEC recommended field missing: &\#x27;version&\#x27;

**File:** /workspace/skills/invalid\-skill/SKILL\.md

**Suggested fix:** Add &\#x27;version&\#x27; to frontmatter — Semantic version \(e\.g\., &quot;1\.0\.0&quot;\)

**Finding metadata:** \{&quot;deduction&quot;: 5, &quot;dimension&quot;: &quot;correctness&quot;\}

**Finding: quality\_correctness \(medium\):** SKILL\_SPEC recommended field missing: &\#x27;metadata\.tags&\#x27;

**File:** /workspace/skills/invalid\-skill/SKILL\.md

**Suggested fix:** Add &\#x27;tags&\#x27; under metadata: — Categorization tags \(under metadata:, list of 1\-5 items\)

**Finding metadata:** \{&quot;deduction&quot;: 5, &quot;dimension&quot;: &quot;correctness&quot;\}

**Finding: quality\_discoverability \(medium\):** Description too short \(3 chars, recommend 50\-150\)

**File:** /workspace/skills/invalid\-skill/SKILL\.md

**Suggested fix:** Add more context: what tasks does this skill handle?

**Finding metadata:** \{&quot;deduction&quot;: 20, &quot;dimension&quot;: &quot;discoverability&quot;\}

**Finding: quality\_discoverability \(low\):** Description doesn&\#x27;t mention WHEN to use this skill

**File:** /workspace/skills/invalid\-skill/SKILL\.md

**Suggested fix:** Add trigger context: &\#x27;Use for\.\.\.&\#x27;, &\#x27;When you need to\.\.\.&\#x27;

**Finding metadata:** \{&quot;deduction&quot;: 10, &quot;dimension&quot;: &quot;discoverability&quot;\}

**Finding: quality\_discoverability \(low\):** No &\#x27;\#\# Purpose&\#x27; section

**File:** /workspace/skills/invalid\-skill/SKILL\.md

**Suggested fix:** Add purpose section to clarify use cases

**Finding metadata:** \{&quot;deduction&quot;: 5, &quot;dimension&quot;: &quot;discoverability&quot;\}

**Finding: quality\_reliability \(low\):** No prerequisites/requirements documented

**File:** /workspace/skills/invalid\-skill/SKILL\.md

**Suggested fix:** Document dependencies, API keys, or setup needed

**Finding metadata:** \{&quot;deduction&quot;: 5, &quot;dimension&quot;: &quot;reliability&quot;\}

**Finding: quality\_reliability \(low\):** No limitations documented

**File:** /workspace/skills/invalid\-skill/SKILL\.md

**Suggested fix:** Add &\#x27;\#\# Limitations&\#x27; section with known issues/constraints

**Finding metadata:** \{&quot;deduction&quot;: 5, &quot;dimension&quot;: &quot;reliability&quot;\}

**Finding: quality\_reliability \(low\):** No troubleshooting section documented

**File:** /workspace/skills/invalid\-skill/SKILL\.md

**Suggested fix:** Add &\#x27;\#\# Troubleshooting&\#x27; with Error/Cause/Solution patterns

**Finding metadata:** \{&quot;deduction&quot;: 5, &quot;dimension&quot;: &quot;reliability&quot;\}

**Error:** \[QUALITY\-HIGH\] Invalid name format: &\#x27;INVALID NAME&\#x27; \(lowercase/numbers/hyphens only\) in /workspace/skills/invalid\-skill/SKILL\.md

**Warning:** \[QUALITY\-MEDIUM\] Guide\-only skill has very little content \(10 lines\) in /workspace/skills/invalid\-skill/SKILL\.md

**Warning:** \[QUALITY\-LOW\] No examples provided in /workspace/skills/invalid\-skill/SKILL\.md

**Warning:** \[QUALITY\-MEDIUM\] SKILL\_SPEC recommended field missing: &\#x27;version&\#x27; in /workspace/skills/invalid\-skill/SKILL\.md

**Warning:** \[QUALITY\-MEDIUM\] SKILL\_SPEC recommended field missing: &\#x27;metadata\.tags&\#x27; in /workspace/skills/invalid\-skill/SKILL\.md

**Warning:** \[QUALITY\-MEDIUM\] Description too short \(3 chars, recommend 50\-150\) in /workspace/skills/invalid\-skill/SKILL\.md

**Warning:** \[QUALITY\-LOW\] Description doesn&\#x27;t mention WHEN to use this skill in /workspace/skills/invalid\-skill/SKILL\.md

**Warning:** \[QUALITY\-LOW\] No &\#x27;\#\# Purpose&\#x27; section in /workspace/skills/invalid\-skill/SKILL\.md

**Warning:** \[QUALITY\-LOW\] No prerequisites/requirements documented in /workspace/skills/invalid\-skill/SKILL\.md

**Warning:** \[QUALITY\-LOW\] No limitations documented in /workspace/skills/invalid\-skill/SKILL\.md

**Warning:** \[QUALITY\-LOW\] No troubleshooting section documented in /workspace/skills/invalid\-skill/SKILL\.md

**Scanner message:** \[OK\] quality\_score: Score: 71\.8/100 \(Grade: C\)

### SCRIPT\_LINT — evidence

**Evidence: lint:** No scripts/ or tools/ directory found

**Scanner message:** \[OK\] lint: No scripts/ or tools/ directory found

## skills/meeting\-action\-list

[JSON](https://chrisknvidia.github.io/skill-evaluator-consumer-demo/runs/39710576857/1/skill-005/skillevaluator-tier1.json)

### Recorded quality dimensions

| Dimension | Score / 100 | Weight | Issues |

| --- | --- | --- | --- |

| correctness | 95 | 0\.35 | 1 |

| discoverability | 100 | 0\.25 | 0 |

| reliability | 100 | 0\.25 | 0 |

| efficiency | 100 | 0\.15 | 0 |

### Validator outcomes

| Validator | Outcome | Checks recorded | Errors | Warnings |

| --- | --- | --- | --- | --- |

| Schema &amp; Repository Governance | PASS | 11 | 0 | 2 |

| Semantic Version Validation | PASS | 1 | 0 | 0 |

| Security Scan | PASS | 1 | 0 | 0 |

| PII Scan | PASS | 2 | 0 | 0 |

| License Compliance | PASS | 1 | 0 | 0 |

| Code Risk Analysis | PASS | 2 | 0 | 0 |

| Secrets Detection | PASS | 1 | 0 | 0 |

| Code Integrity &amp; Hygiene | PASS | 5 | 0 | 1 |

| Dependency Vulnerability Audit | PASS | 1 | 0 | 0 |

| Unicode Smuggling Detection | PASS | 1 | 0 | 0 |

| QUALITY | PASS | 1 | 0 | 1 |

| SCRIPT\_LINT | PASS | 1 | 0 | 0 |

### Schema &amp; Repository Governance — evidence

**Evidence: manifest\_exists:** Found skill manifest: SKILL\.md

**Evidence metadata:** \{&quot;file\_path&quot;: &quot;/workspace/skills/meeting\-action\-list/SKILL\.md&quot;\}

**Evidence: frontmatter\_valid:** Valid frontmatter for skill &\#x27;meeting\-action\-list&\#x27;

**Evidence metadata:** \{&quot;description\_length&quot;: 123\}

**Evidence: folder\_hierarchy:** Valid general skill structure: skills/meeting\-action\-list/

**Evidence: naming\_convention:** Folder name &\#x27;meeting\-action\-list&\#x27; follows kebab\-case convention

**Evidence metadata:** \{&quot;name\_length&quot;: 19\}

**Evidence: line\_count:** SKILL\.md within line limit \(72/500\)

**Evidence metadata:** \{&quot;limit&quot;: 500, &quot;line\_count&quot;: 72\}

**Evidence: body\_heading:** Body contains a top\-level heading

**Evidence: body\_recommended\_section:** Found recommended section: &\#x27;\#\# Instructions&\#x27; \(or &\#x27;\#\# Usage&\#x27;\)

**Evidence: body\_recommended\_section:** Found recommended section: &\#x27;\#\# Examples&\#x27;

**Evidence: optional\_files:** Found optional supporting files: scripts

**Evidence metadata:** \{&quot;files\_found&quot;: \[&quot;scripts&quot;\]\}

**Evidence: name\_consistency:** Directory name matches frontmatter: &\#x27;meeting\-action\-list&\#x27;

**Evidence: author\_format:** Valid author format: SkillEvaluator CI Demo Authors &lt;ci\-demo@​example\.com&gt;

**Finding: unexpected\_file \(low\):** Unexpected &\#x27;requirements\.txt&\#x27; in skill root

**File:** /workspace/skills/meeting\-action\-list/requirements\.txt

**Suggested fix:** Consider moving to one of: agents/, assets/, config/, evals/, references/, scripts/, tests/, tools/\. To allow additional directories, set $SKILLEVALUATOR\_SCHEMA\_ALLOWED\_DIRS\.

**Warning:** \[SCHEMA\-LOW\] Unexpected &\#x27;requirements\.txt&\#x27; in skill root in /workspace/skills/meeting\-action\-list/requirements\.txt

**Warning:** Workflow scope: llm skipped\. LLM checks disabled by \-\-no\-llm\.

**Scanner message:** \[OK\] manifest\_exists: Found skill manifest: SKILL\.md

**Scanner message:** \[OK\] frontmatter\_valid: Valid frontmatter for skill &\#x27;meeting\-action\-list&\#x27;

**Scanner message:** \[OK\] folder\_hierarchy: Valid general skill structure: skills/meeting\-action\-list/

**Scanner message:** \[OK\] naming\_convention: Folder name &\#x27;meeting\-action\-list&\#x27; follows kebab\-case convention

**Scanner message:** \[OK\] line\_count: SKILL\.md within line limit \(72/500\)

**Scanner message:** \[OK\] body\_heading: Body contains a top\-level heading

**Scanner message:** \[OK\] body\_recommended\_section: Found recommended section: &\#x27;\#\# Instructions&\#x27; \(or &\#x27;\#\# Usage&\#x27;\)

**Scanner message:** \[OK\] body\_recommended\_section: Found recommended section: &\#x27;\#\# Examples&\#x27;

**Scanner message:** \[OK\] optional\_files: Found optional supporting files: scripts

**Scanner message:** \[OK\] name\_consistency: Directory name matches frontmatter: &\#x27;meeting\-action\-list&\#x27;

**Scanner message:** \[OK\] author\_format: Valid author format: SkillEvaluator CI Demo Authors &lt;ci\-demo@​example\.com&gt;

### Semantic Version Validation — evidence

**Evidence: version\_semver:** Valid semantic version: 1\.0\.0

**Evidence metadata:** \{&quot;previous\_version&quot;: null, &quot;version&quot;: &quot;1\.0\.0&quot;\}

**Scanner message:** \[OK\] version\_semver: Valid semantic version: 1\.0\.0

### Security Scan — evidence

**Evidence: skillspector:** No security vulnerabilities detected \(secrets, API keys, credentials\)

**Scanner message:** \[OK\] skillspector: No security vulnerabilities detected \(secrets, API keys, credentials\)

### PII Scan — evidence

**Evidence: pii\_scan\_start:** Scanning 3 files for PII

**Evidence metadata:** \{&quot;file\_count&quot;: 3\}

**Evidence: pii\_detection:** No PII detected in 3 files \(emails, SSNs, phone numbers, paths\)

**Evidence metadata:** \{&quot;files\_scanned&quot;: 3\}

**Scanner message:** \[OK\] pii\_scan\_start: Scanning 3 files for PII

**Scanner message:** \[OK\] pii\_detection: No PII detected in 3 files \(emails, SSNs, phone numbers, paths\)

### License Compliance — evidence

**Evidence: license\_compliance:** License compliance scan completed \(allowed\)

**Evidence metadata:** \{&quot;license\_status&quot;: &quot;allowed&quot;\}

**Scanner message:** Tier 1: Found license declaration in frontmatter \(SKILL\.md\)

**Scanner message:** License: MIT \(ALLOWED \- permissive\)

**Scanner message:** \[OK\] license\_compliance: License compliance scan completed \(allowed\)

### Code Risk Analysis — evidence

**Evidence: bandit:** Bandit: No security issues found

**Evidence: semgrep:** Semgrep: No security issues found

**Scanner message:** Found 1 Python, 0 Shell, 0 JavaScript/TypeScript files

**Scanner message:** \[OK\] bandit: Bandit: No security issues found

**Scanner message:** \[OK\] semgrep: Semgrep: No security issues found

### Secrets Detection — evidence

**Evidence: gitleaks:** No secrets detected by Gitleaks

**Scanner message:** \[OK\] gitleaks: No secrets detected by Gitleaks

### Code Integrity &amp; Hygiene — evidence

**Evidence: dead\_links\_scan:** Checking 1 markdown files for dead links

**Evidence metadata:** \{&quot;file\_count&quot;: 1\}

**Evidence: dead\_links:** All relative links valid in 1 markdown file\(s\)

**Evidence metadata:** \{&quot;files\_checked&quot;: 1\}

**Evidence: dependency\_audit:** Auditing requirements\.txt

**Evidence: dependency\_audit:** requirements\.txt passed dependency audit

**Evidence: test\_discovery:** No standard Python test\-file candidates found; target tests were not executed and coverage was not measured\. Consider adding tests\.

**Evidence metadata:** \{&quot;coverage\_measured&quot;: false, &quot;execution\_performed&quot;: false, &quot;patterns&quot;: \[&quot;test\_\*\.py&quot;, &quot;\*\_test\.py&quot;\], &quot;test\_count&quot;: 0\}

**Warning:** No standard Python test\-file candidates found; consider adding tests

**Scanner message:** \[OK\] dead\_links\_scan: Checking 1 markdown files for dead links

**Scanner message:** \[OK\] dead\_links: All relative links valid in 1 markdown file\(s\)

**Scanner message:** \[OK\] dependency\_audit: Auditing requirements\.txt

**Scanner message:** \[OK\] dependency\_audit: requirements\.txt passed dependency audit

**Scanner message:** \[OK\] test\_discovery: No standard Python test\-file candidates found; target tests were not executed and coverage was not measured\. Consider adding tests\.

### Dependency Vulnerability Audit — evidence

**Evidence: pip\_audit:** requirements\.txt: No vulnerabilities found \(pip\-audit\)

**Evidence metadata:** \{&quot;source&quot;: &quot;requirements\.txt&quot;, &quot;vulnerability\_count&quot;: 0\}

**Scanner message:** Auditing requirements\.txt

**Scanner message:** \[OK\] pip\_audit: requirements\.txt: No vulnerabilities found \(pip\-audit\)

### Unicode Smuggling Detection — evidence

**Evidence: unicode\_scan:** No invisible Unicode characters detected in 3 file\(s\)

**Evidence metadata:** \{&quot;files\_scanned&quot;: 3\}

**Scanner message:** \[OK\] unicode\_scan: No invisible Unicode characters detected in 3 file\(s\)

### QUALITY — evidence

**Evidence: quality\_score:** Score: 98\.2/100 \(Grade: A\)

**Evidence metadata:** \{&quot;grade&quot;: &quot;A&quot;, &quot;overall\_score&quot;: 98\.2, &quot;skill\_type&quot;: &quot;script\-based&quot;\}

**Finding: quality\_correctness \(medium\):** SKILL\_SPEC recommended field missing: &\#x27;version&\#x27;

**File:** /workspace/skills/meeting\-action\-list/SKILL\.md

**Suggested fix:** Add &\#x27;version&\#x27; to frontmatter — Semantic version \(e\.g\., &quot;1\.0\.0&quot;\)

**Finding metadata:** \{&quot;deduction&quot;: 5, &quot;dimension&quot;: &quot;correctness&quot;\}

**Warning:** \[QUALITY\-MEDIUM\] SKILL\_SPEC recommended field missing: &\#x27;version&\#x27; in /workspace/skills/meeting\-action\-list/SKILL\.md

**Scanner message:** \[OK\] quality\_score: Score: 98\.2/100 \(Grade: A\)

### SCRIPT\_LINT — evidence

**Evidence: lint:** All 1 script\(s\) passed lint checks

**Scanner message:** \[OK\] lint: All 1 script\(s\) passed lint checks

## skills/release\-summary

[JSON](https://chrisknvidia.github.io/skill-evaluator-consumer-demo/runs/39710576857/1/skill-006/skillevaluator-tier1.json)

### Recorded quality dimensions

| Dimension | Score / 100 | Weight | Issues |

| --- | --- | --- | --- |

| correctness | 95 | 0\.35 | 1 |

| discoverability | 100 | 0\.25 | 0 |

| reliability | 100 | 0\.25 | 0 |

| efficiency | 100 | 0\.15 | 0 |

### Validator outcomes

| Validator | Outcome | Checks recorded | Errors | Warnings |

| --- | --- | --- | --- | --- |

| Schema &amp; Repository Governance | PASS | 11 | 0 | 1 |

| Semantic Version Validation | PASS | 1 | 0 | 0 |

| Security Scan | PASS | 1 | 0 | 0 |

| PII Scan | PASS | 2 | 0 | 0 |

| License Compliance | PASS | 1 | 0 | 0 |

| Code Risk Analysis | NOT APPLICABLE | 1 | 0 | 0 |

| Secrets Detection | PASS | 1 | 0 | 0 |

| Code Integrity &amp; Hygiene | PASS | 4 | 0 | 1 |

| Dependency Vulnerability Audit | NOT APPLICABLE | 1 | 0 | 0 |

| Unicode Smuggling Detection | PASS | 1 | 0 | 0 |

| QUALITY | PASS | 1 | 0 | 1 |

| SCRIPT\_LINT | NOT APPLICABLE | 1 | 0 | 0 |

### Schema &amp; Repository Governance — evidence

**Evidence: manifest\_exists:** Found skill manifest: SKILL\.md

**Evidence metadata:** \{&quot;file\_path&quot;: &quot;/workspace/skills/release\-summary/SKILL\.md&quot;\}

**Evidence: frontmatter\_valid:** Valid frontmatter for skill &\#x27;release\-summary&\#x27;

**Evidence metadata:** \{&quot;description\_length&quot;: 129\}

**Evidence: folder\_hierarchy:** Valid general skill structure: skills/release\-summary/

**Evidence: naming\_convention:** Folder name &\#x27;release\-summary&\#x27; follows kebab\-case convention

**Evidence metadata:** \{&quot;name\_length&quot;: 15\}

**Evidence: line\_count:** SKILL\.md within line limit \(56/500\)

**Evidence metadata:** \{&quot;limit&quot;: 500, &quot;line\_count&quot;: 56\}

**Evidence: body\_heading:** Body contains a top\-level heading

**Evidence: body\_recommended\_section:** Found recommended section: &\#x27;\#\# Instructions&\#x27; \(or &\#x27;\#\# Usage&\#x27;\)

**Evidence: body\_recommended\_section:** Found recommended section: &\#x27;\#\# Examples&\#x27;

**Evidence: optional\_files:** Skill directory contains only expected files

**Evidence: name\_consistency:** Directory name matches frontmatter: &\#x27;release\-summary&\#x27;

**Evidence: author\_format:** Valid author format: SkillEvaluator CI Demo Authors &lt;ci\-demo@​example\.com&gt;

**Warning:** Workflow scope: llm skipped\. LLM checks disabled by \-\-no\-llm\.

**Scanner message:** \[OK\] manifest\_exists: Found skill manifest: SKILL\.md

**Scanner message:** \[OK\] frontmatter\_valid: Valid frontmatter for skill &\#x27;release\-summary&\#x27;

**Scanner message:** \[OK\] folder\_hierarchy: Valid general skill structure: skills/release\-summary/

**Scanner message:** \[OK\] naming\_convention: Folder name &\#x27;release\-summary&\#x27; follows kebab\-case convention

**Scanner message:** \[OK\] line\_count: SKILL\.md within line limit \(56/500\)

**Scanner message:** \[OK\] body\_heading: Body contains a top\-level heading

**Scanner message:** \[OK\] body\_recommended\_section: Found recommended section: &\#x27;\#\# Instructions&\#x27; \(or &\#x27;\#\# Usage&\#x27;\)

**Scanner message:** \[OK\] body\_recommended\_section: Found recommended section: &\#x27;\#\# Examples&\#x27;

**Scanner message:** \[OK\] optional\_files: Skill directory contains only expected files

**Scanner message:** \[OK\] name\_consistency: Directory name matches frontmatter: &\#x27;release\-summary&\#x27;

**Scanner message:** \[OK\] author\_format: Valid author format: SkillEvaluator CI Demo Authors &lt;ci\-demo@​example\.com&gt;

### Semantic Version Validation — evidence

**Evidence: version\_semver:** Valid semantic version: 1\.0\.0

**Evidence metadata:** \{&quot;previous\_version&quot;: null, &quot;version&quot;: &quot;1\.0\.0&quot;\}

**Scanner message:** \[OK\] version\_semver: Valid semantic version: 1\.0\.0

### Security Scan — evidence

**Evidence: skillspector:** No security vulnerabilities detected \(secrets, API keys, credentials\)

**Scanner message:** \[OK\] skillspector: No security vulnerabilities detected \(secrets, API keys, credentials\)

### PII Scan — evidence

**Evidence: pii\_scan\_start:** Scanning 1 files for PII

**Evidence metadata:** \{&quot;file\_count&quot;: 1\}

**Evidence: pii\_detection:** No PII detected in 1 files \(emails, SSNs, phone numbers, paths\)

**Evidence metadata:** \{&quot;files\_scanned&quot;: 1\}

**Scanner message:** \[OK\] pii\_scan\_start: Scanning 1 files for PII

**Scanner message:** \[OK\] pii\_detection: No PII detected in 1 files \(emails, SSNs, phone numbers, paths\)

### License Compliance — evidence

**Evidence: license\_compliance:** License compliance scan completed \(allowed\)

**Evidence metadata:** \{&quot;license\_status&quot;: &quot;allowed&quot;\}

**Scanner message:** Tier 1: Found license declaration in frontmatter \(SKILL\.md\)

**Scanner message:** License: MIT \(ALLOWED \- permissive\)

**Scanner message:** \[OK\] license\_compliance: License compliance scan completed \(allowed\)

### Code Risk Analysis — evidence

**Evidence: code\_file\_discovery:** No code files found \- code risk analysis is not applicable

**Evidence metadata:** \{&quot;file\_counts&quot;: \{&quot;js&quot;: 0, &quot;py&quot;: 0, &quot;sh&quot;: 0\}\}

**Scanner message:** \[OK\] code\_file\_discovery: No code files found \- code risk analysis is not applicable

### Secrets Detection — evidence

**Evidence: gitleaks:** No secrets detected by Gitleaks

**Scanner message:** \[OK\] gitleaks: No secrets detected by Gitleaks

### Code Integrity &amp; Hygiene — evidence

**Evidence: dead\_links\_scan:** Checking 1 markdown files for dead links

**Evidence metadata:** \{&quot;file\_count&quot;: 1\}

**Evidence: dead\_links:** All relative links valid in 1 markdown file\(s\)

**Evidence metadata:** \{&quot;files\_checked&quot;: 1\}

**Evidence: dependencies:** No dependency files found \(requirements\.txt, pyproject\.toml\)

**Evidence: test\_discovery:** No standard Python test\-file candidates found; target tests were not executed and coverage was not measured\. Consider adding tests\.

**Evidence metadata:** \{&quot;coverage\_measured&quot;: false, &quot;execution\_performed&quot;: false, &quot;patterns&quot;: \[&quot;test\_\*\.py&quot;, &quot;\*\_test\.py&quot;\], &quot;test\_count&quot;: 0\}

**Warning:** No standard Python test\-file candidates found; consider adding tests

**Scanner message:** \[OK\] dead\_links\_scan: Checking 1 markdown files for dead links

**Scanner message:** \[OK\] dead\_links: All relative links valid in 1 markdown file\(s\)

**Scanner message:** \[OK\] dependencies: No dependency files found \(requirements\.txt, pyproject\.toml\)

**Scanner message:** \[OK\] test\_discovery: No standard Python test\-file candidates found; target tests were not executed and coverage was not measured\. Consider adding tests\.

### Dependency Vulnerability Audit — evidence

**Evidence: dependency\_file\_discovery:** No dependency files found \- vulnerability audit is not applicable

**Scanner message:** \[OK\] dependency\_file\_discovery: No dependency files found \- vulnerability audit is not applicable

### Unicode Smuggling Detection — evidence

**Evidence: unicode\_scan:** No invisible Unicode characters detected in 1 file\(s\)

**Evidence metadata:** \{&quot;files\_scanned&quot;: 1\}

**Scanner message:** \[OK\] unicode\_scan: No invisible Unicode characters detected in 1 file\(s\)

### QUALITY — evidence

**Evidence: quality\_score:** Score: 98\.2/100 \(Grade: A\)

**Evidence metadata:** \{&quot;grade&quot;: &quot;A&quot;, &quot;overall\_score&quot;: 98\.2, &quot;skill\_type&quot;: &quot;guide\-only&quot;\}

**Finding: quality\_correctness \(medium\):** SKILL\_SPEC recommended field missing: &\#x27;version&\#x27;

**File:** /workspace/skills/release\-summary/SKILL\.md

**Suggested fix:** Add &\#x27;version&\#x27; to frontmatter — Semantic version \(e\.g\., &quot;1\.0\.0&quot;\)

**Finding metadata:** \{&quot;deduction&quot;: 5, &quot;dimension&quot;: &quot;correctness&quot;\}

**Warning:** \[QUALITY\-MEDIUM\] SKILL\_SPEC recommended field missing: &\#x27;version&\#x27; in /workspace/skills/release\-summary/SKILL\.md

**Scanner message:** \[OK\] quality\_score: Score: 98\.2/100 \(Grade: A\)

### SCRIPT\_LINT — evidence

**Evidence: lint:** No scripts/ or tools/ directory found

**Scanner message:** \[OK\] lint: No scripts/ or tools/ directory found

[Open full report](https://chrisknvidia.github.io/skill-evaluator-consumer-demo/runs/39710576857/1/index.html) · [Workflow run and logs](https://github.com/chrisknvidia/skill-evaluator-consumer-demo/actions/runs/39710576857)
