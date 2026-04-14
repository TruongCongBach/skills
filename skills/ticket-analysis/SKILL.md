---
name: ticket-analysis
description: Analyze Jira tickets before implementation. This skill should be used when a ticket needs triage, impact analysis, screenshot or design-image review, HAR or Charles or zipped-log inspection, fix-direction planning, or a readiness decision before coding begins. It is analysis-only and must not start implementation unless explicitly requested later.
progressive_disclosure:
  entry_point:
    summary: "Read the ticket first, inspect supporting artifacts, identify likely causes and risks, and decide whether the work is ready for implementation."
    when_to_use: "Use for Jira-first ticket triage, debugging intake, design discrepancy review from screenshots, HAR or Charles artifact review, and engineering planning before any code changes."
    quick_start: "1. Read Jira data 2. Structure expected vs actual behavior 3. Review images or logs if present 4. Form root-cause hypotheses 5. Propose fix directions and readiness decision 6. Stop before implementation"
  references:
    - references/analysis-workflow.md
    - references/ticket-analysis-template.md
    - references/screenshot-review-template.md
    - references/network-log-analysis-template.md
    - references/root-cause-hypothesis-template.md
    - references/readiness-checklist.md
    - references/title-format-guide.md
---

# Ticket Analysis

## Overview

Use this skill to triage a ticket before implementation starts. Read Jira ticket data through MCP, inspect screenshots or design images when present, inspect HAR or Charles or zipped logs when present, and produce a concise engineering analysis that helps decide whether the ticket is ready for coding.

Keep the workflow analysis-only. Propose likely causes, affected areas, and fix directions, but do not edit code or start implementation unless a later prompt explicitly asks for it.

Always respond in the user's current language. If the user writes in Vietnamese, reply in Vietnamese. If the user writes in English, reply in English. Keep technical terms in their original form when that is clearer.

## When to Use This Skill

Activate when:
- A Jira ticket needs a concise technical summary before coding
- A bug report needs expected vs actual behavior clarified
- A screenshot or design image needs UI-state or layout analysis
- HAR, Charles, zip, JSON, text, or log artifacts need inspection
- A ticket needs root-cause hypotheses and fix directions
- A ticket needs a readiness-for-implementation decision
- A team needs a reusable triage report other engineers can read later

Do not activate when:
- The user already approved implementation and wants code changes now
- The task is pure coding with no triage or investigation phase
- The request is only to rewrite text without technical analysis

## The Iron Law

Read the ticket first. Anchor every conclusion to evidence from Jira, images, or artifacts. Mark assumptions explicitly. Stop at analysis and planning unless implementation is explicitly requested later.

## Core Principles

1. **Ticket-first discipline**: Start from Jira summary, description, comments, attachments, issue type, and acceptance criteria.
2. **Evidence before inference**: Separate observed facts from hypotheses. State confidence and unknowns.
3. **Artifact-aware debugging**: Treat screenshots and logs as first-class inputs, not optional extras.
4. **Actionable planning**: Produce fix directions, risks, and affected areas that help a human decide whether to begin implementation.
5. **Readiness gating**: End with a concrete decision: ready to implement or not yet ready.

## Quick Start

1. Read the Jira issue via MCP and capture:
   - ticket ID
   - issue type
   - summary
   - description
   - comments
   - status
   - priority
   - labels or components
   - acceptance criteria if present
2. Normalize the ticket into the standard structure from [ticket-analysis-template](./references/ticket-analysis-template.md).
3. Review attached or supplied images with the screenshot workflow in [screenshot-review-template](./references/screenshot-review-template.md).
4. Inspect HAR, Charles, zip, JSON, or text logs with [network-log-analysis-template](./references/network-log-analysis-template.md).
   Execute `scripts/inspect_ticket_artifacts.py <path ...>` to summarize common network and log patterns.
5. Build 2-4 plausible root-cause hypotheses using [root-cause-hypothesis-template](./references/root-cause-hypothesis-template.md).
6. Map likely affected areas, fix directions, and implementation risks.
7. Apply [readiness-checklist](./references/readiness-checklist.md) and end with a recommendation.
8. Generate the standard title string with [title-format-guide](./references/title-format-guide.md) or `scripts/generate_ticket_title.py`.

## Workflow Rules

- Prefer Jira MCP as the system of record for ticket context.
- Pull exact ticket ID from Jira when available.
- Distinguish clearly between:
  - reported symptoms
  - observed evidence
  - inferred root causes
  - proposed fix directions
- For screenshots or design images, describe visible issues and likely state problems without claiming pixel-perfect certainty.
- For logs and traffic captures, summarize failed requests, slow requests, duplicate requests, suspicious payloads, and notable error patterns.
- For React Native and Next.js tickets, call out likely frontend, navigation, API, caching, auth, state, form, rendering, and environment boundaries when relevant.
- Keep the output concise enough for daily triage, but complete enough for handoff.

## Output Contract

Produce the final analysis in this order:
- Ticket summary
- Problem statement
- Expected vs actual behavior
- Acceptance criteria found
- Missing information / ambiguities
- Design/UI findings if image exists
- Network/log findings if logs exist
- Likely root causes
- Proposed fix directions
- Affected areas
- Risks / tradeoffs
- Questions to confirm before implementation
- Recommendation: ready to implement or not yet ready

When relevant, also include:
- Suggested title
- Suggested commit message
- Suggested ticket comment title

## Artifact Handling

### Jira

Use Jira MCP to load the issue and extract the smallest useful set of fields first. Expand only when the ticket is ambiguous or comments contain critical debugging detail.

### Screenshots or Design Images

Inspect the image directly when it is available in the conversation or as a local path. Focus on visible layout defects, component state, copy mismatches, loading or empty states, error states, spacing inconsistencies, and platform-specific clues. State assumptions explicitly.

### HAR, Charles, Zip, or Logs

Inspect file type before analysis. Unzip archives into a temporary workspace when needed. Normalize HAR and JSON where possible, and summarize traffic behavior in engineering terms rather than raw dumps.

Execute:

```bash
python3 scripts/inspect_ticket_artifacts.py path/to/file.har
python3 scripts/inspect_ticket_artifacts.py path/to/archive.zip --slow-ms 1500
```

Use the script output as input evidence, not as the final answer by itself.

## Navigation

- **[Analysis Workflow](./references/analysis-workflow.md)** - Load for the end-to-end triage sequence and evidence standards.
- **[Ticket Analysis Template](./references/ticket-analysis-template.md)** - Load for the main report structure and concise writing pattern.
- **[Screenshot Review Template](./references/screenshot-review-template.md)** - Load when a screenshot or design image is part of the ticket.
- **[Network / Log Analysis Template](./references/network-log-analysis-template.md)** - Load when HAR, Charles, zip, JSON, or text logs exist.
- **[Root Cause Hypothesis Template](./references/root-cause-hypothesis-template.md)** - Load when several explanations are plausible and tradeoffs need to be compared.
- **[Readiness Checklist](./references/readiness-checklist.md)** - Load before the final recommendation.
- **[Title Format Guide](./references/title-format-guide.md)** - Load to generate `type: TICKET-ID | summary` strings consistently.

## Key Reminders

- Read the ticket before forming a solution.
- Keep the analysis grounded in evidence.
- Mark missing information instead of filling gaps with certainty.
- Propose fix directions without writing code.
- Keep summaries concise and engineer-readable.
- Prefer `fix` for bug tickets and `feat` for feature tickets when type is uncertain.
- Always include the Jira ticket ID in the suggested title when available.
- End with a readiness decision, not a vague summary.

## Red Flags - STOP

Stop and correct course when:
- Starting to edit code or propose implementation details beyond planning
- Treating assumptions as confirmed facts
- Ignoring ticket comments or acceptance criteria
- Claiming exact design dimensions from a screenshot alone
- Dumping raw logs without extracting patterns
- Recommending implementation even though core behavior is still ambiguous
- Omitting the final readiness recommendation
- Generating a title that does not match `type: TICKET-ID | summary`

## Integration Notes

- Use with Jira MCP for ticket retrieval.
- Use image inspection tools when screenshots are supplied.
- Use terminal tools for archive extraction and script execution.
- Use follow-up implementation skills only after the user approves moving beyond analysis.
