---
name: release-summary
description: Summarizes supplied merged changes into concise release notes. Use when a release needs user-facing changes with evidence limits.
license: MIT
metadata:
  author: SkillEvaluator CI Demo Authors <ci-demo@example.com>
  version: 1.0.0
  tags:
    - demonstration
    - text-assistance
---

# Release Summary

## Purpose
Create accurate release notes from a supplied list of completed changes.

## Prerequisites
Provide merged change descriptions and any known release version or date.
No browsing, publishing rights, or credentials are required.

## Instructions
1. Read the supplied changes and retain only behavior supported by that material.
2. Group related changes into additions, fixes, and behavior changes.
3. Explain the impact on a user before including technical detail.
4. Preserve explicitly stated compatibility changes and migration steps.
5. Keep planned or unmerged work in an excluded-items note.
6. Validate the version and date against the input; omit either when absent.
7. Identify missing evidence instead of claiming a fix was deployed or verified.

## Output
Return a short release heading and a bulleted list of changes.
Use an Upgrade notes section only when the source states a required user action.
End with unresolved source gaps when any remain.

## Examples
Input:
```text
Merged: export keeps the column order selected by the user.
Planned: add a chart preview.
```
Output:
```text
Fixes
- Exports now preserve the selected column order.
Source gap: release version and date were not supplied.
```
The planned chart preview is excluded from the release changes.

## Limitations
This skill writes a draft and does not publish releases or verify deployment state.
A merged change is evidence of source integration, not proof of production availability.

## Troubleshooting
If the input contains duplicate change descriptions, combine them without broadening the claim.
If two items disagree about compatibility, retain the discrepancy as a validation issue.
