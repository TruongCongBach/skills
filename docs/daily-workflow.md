# Daily Workflow

Use this workflow to keep the skills from overlapping during normal ticket work.

## Sequence

1. `ticket-analysis`
   Use when the ticket is still being understood.
   Output: issue summary, expected vs actual behavior, ambiguities, likely root causes, readiness decision.

2. `ticket-planner`
   Use after the problem is clear enough to compare implementation directions.
   Output: recommended approach, affected areas, risks, edge cases, suggested tests.

3. `clean-code-agent`
   Use when writing or refactoring code.
   Output: implementation discipline and verification expectations.

4. `ticket-review`
   Use after code exists and needs review against Jira, UX, and quality expectations.
   Output: review findings, missing states, test gaps, required changes, QA checklist, ready vs needs revision.

5. `ticket-commit`
   Use after the implementation is approved and you need a clean, issue-scoped commit.
   Output: changed-file review, recommended files to stage, excluded files, commit title, safe to commit vs review needed.

6. `ticket-summary`
   Use after the implementation is effectively done and you need a clear engineering and QA-facing summary.
   Output: root cause, fix approach, what changed, affected areas, regression risks, QA focus, short summaries.

7. `ticket-close`
   Use only after the work is approved and the next step is final Jira communication.
   Output: final ticket comment, QA closure note, closure summary, concise status update.

## Boundary Rules

- `ticket-analysis` decides whether the ticket is ready to build.
- `ticket-planner` decides how the work should likely be built.
- `ticket-review` decides whether the built work is actually acceptable.
- `ticket-commit` decides what is safe to include in the issue commit.
- `ticket-summary` explains the completed change for humans.
- `ticket-close` writes the final Jira closure message.

## Practical Prompting

When several skills could plausibly match, invoke the skill by name:

- `Use ticket-analysis for this Jira bug.`
- `Use ticket-planner to compare implementation approaches.`
- `Use ticket-review to review this completed work.`
- `Use ticket-commit to prepare a clean commit for this issue.`
- `Use ticket-summary to write the engineering handoff.`
- `Use ticket-close to draft the final Jira closure comment.`
