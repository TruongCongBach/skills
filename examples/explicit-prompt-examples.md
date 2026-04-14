# Explicit Prompt Examples

Use explicit skill names when this repo coexists with other skills on the same machine.

## Ticket Triage

```text
Use ticket-analysis to triage Jira ticket ML-39 before implementation.
Read the ticket first, inspect the attached HAR file, and tell me whether this is ready to build.
```

## Implementation Planning

```text
Use ticket-planner for this approved analysis.
Compare two implementation approaches for the bug and tell me which one you recommend before coding starts.
```

## Post-Implementation Review

```text
Use ticket-review to review this completed implementation against Jira ticket ML-39 and the attached screenshot.
Tell me what is still missing before I approve it.
```

## Scoped Commit

```text
Use ticket-commit for Jira ticket ML-39.
Inspect the current git changes, recommend only the files that clearly belong to this issue, and prepare the commit title without including uncertain files automatically.
```

## Engineering Handoff Summary

```text
Use ticket-summary to summarize the completed fix for QA and future engineers.
Explain the root cause, what changed, regression risks, and what QA should focus on.
```

## Final Jira Closure

```text
Use ticket-close to draft the final Jira closure comment for ML-39.
Keep it concise and include a QA handoff note plus a short closure summary.
```
