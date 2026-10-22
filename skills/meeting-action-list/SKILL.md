---
name: meeting-action-list
description: Extracts explicit commitments from meeting notes. Use when a meeting needs a concise action list with owners and due dates.
license: MIT
metadata:
  author: SkillEvaluator CI Demo Authors <ci-demo@example.com>
  version: "1.0.0"
  tags:
    - demonstration
    - text-assistance
---

# Meeting Action List

## Purpose
Turn supplied meeting notes into a faithful list of commitments that participants can review.

## Prerequisites
Provide the meeting notes as text. No external services or credentials are required. The optional CSV helper requires Python 3.12 or later.

## Instructions
1. Read the complete notes and identify statements that commit to future work.
2. Separate decisions and background discussion from actions.
3. Record the stated owner and due date for each action; use “Unspecified” when either is absent.
4. Preserve relative dates exactly unless the meeting date is provided.
5. Combine duplicate actions only when their owner, scope, and deadline agree.
6. Validate every action against the notes before returning the result.

## Output
Return a Markdown table with Action, Owner, Due date, and Supporting note columns.
After the table, list unresolved ambiguities in one short paragraph.
If no commitments are present, return “No explicit action items found.”

## Examples
Input:
```text
The draft is ready. Design team will review the diagram by Friday.
A launch date was discussed but no date was agreed.
```
Output:
```text
Action: Review the diagram
Owner: Design team
Due date: Friday
Supporting note: Design team will review the diagram by Friday.
```
The launch discussion creates no action because nobody committed to a next step.

## Available Scripts
| Script | Purpose | Arguments |
| --- | --- | --- |
| `scripts/summarize_actions.py` | Count actions and missing owner/date values in a local CSV | Explicit CSV path |

For a supplied CSV, run the helper from this skill directory:
```bash
python3 scripts/summarize_actions.py /path/to/actions.csv
```
A host with a `run_script` tool can invoke the same script with the same path argument.
CSV headers must include `action,owner,due_date`; extra named columns are allowed.
The script reads only the supplied file and prints JSON. A header-only CSV returns zero counts.
Blank or “Unspecified” owners and dates are counted as missing. Dates are not interpreted.
Malformed rows and unreadable files produce an error on stderr and exit code 2.
The skill's `requirements.txt` supplies a pinned dependency inventory for demonstrating
CI dependency auditing; the standard-library CSV helper does not import that package.

## Limitations
This skill extracts stated commitments; it does not assign work or contact participants.
An absent owner is an information gap, not permission to infer a responsible person.

## Troubleshooting
If notes contradict each other, retain both statements and flag the conflict.
If input is empty or unreadable, explain the validation error and request readable notes.
