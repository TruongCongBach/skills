# Daily Workflow

Use this workflow to keep the skills from overlapping during normal ticket work.

Security risk assessment is a required layer across the workflow, not a separate stage. Surface it early in `ticket-analysis`, turn it into mitigation in `ticket-planner`, validate it in `ticket-review`, and preserve only the necessary context in `ticket-summary` and `ticket-close`.

## Sequence

1. `ticket-analysis`
   Use when the ticket is still being understood.
   Output: issue summary, expected vs actual behavior, ambiguities, likely root causes, security considerations, readiness decision, and parsed design context when images matter.

2. `ticket-planner`
   Use after the problem is clear enough to compare implementation directions.
   Output: recommended approach, affected areas, risks, security mitigations, edge cases, suggested tests, using parsed design context when UI direction depends on screenshots.

3. `clean-code-agent`
   Use when writing or refactoring code.
   Output: implementation discipline and verification expectations.

4. `ticket-review`
   Use after code exists and needs review against Jira, UX, and quality expectations.
   Output: review findings, missing states, security findings, test gaps, required changes, QA checklist, ready vs needs revision, optionally anchored to parsed design context.

5. `ticket-commit`
   Use after the implementation is approved and you need a clean, issue-scoped commit.
   Output: changed-file review, recommended files to stage, excluded files, commit title, safe to commit vs review needed.

6. `ticket-summary`
   Use after the implementation is effectively done and you need a clear engineering and QA-facing summary.
   Output: root cause, fix approach, what changed, affected areas, regression risks, security note if relevant, QA focus, short summaries.

7. `ticket-close`
   Use only after the work is approved and the next step is final Jira communication.
   Output: final ticket comment, QA closure note, security note if relevant, closure summary, concise status update.

## Boundary Rules

- `ticket-analysis` decides whether the ticket is ready to build.
- `ticket-planner` decides how the work should likely be built.
- `ticket-review` decides whether the built work is actually acceptable.
- `ticket-commit` decides what is safe to include in the issue commit.
- `ticket-summary` explains the completed change for humans.
- `ticket-close` writes the final Jira closure message.
- Security-sensitive tickets should be able to point to a clear owner, risk level, and mitigation before approval.

## Practical Prompting

When several skills could plausibly match, invoke the skill by name:

- `Use ticket-analysis for this Jira bug.`
- `Use ticket-planner to compare implementation approaches.`
- `Use ticket-review to review this completed work.`
- `Use ticket-commit to prepare a clean commit for this issue.`
- `Use ticket-summary to write the engineering handoff.`
- `Use ticket-close to draft the final Jira closure comment.`
