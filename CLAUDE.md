# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

Personal skills repository for Claude Code. This repo contains no build system, tests, or runtime — it is a collection of Markdown-based skill definitions consumed by Claude Code via `/skills add <path>`.

## Structure

- `skills/<skill-name>/SKILL.md` — required entry file with YAML frontmatter (`name`, `description`) followed by instructions.
- `skills/<skill-name>/references/` — optional deep-dive docs referenced from `SKILL.md` (kept out of the main file to preserve context).
- `skills/<skill-name>/evals/evals.json` — optional evaluation test cases.
- `template/SKILL.md` — starting point for new skills.

## Authoring Conventions

- The `description` field in frontmatter is the trigger signal: it must clearly state **what the skill does and when Claude should invoke it**. Claude picks skills based on this field, so be specific about triggering contexts.
- Keep `SKILL.md` focused on decision rules and principles; offload detailed examples, long tables, and reference material into `references/*.md` and link to them from `SKILL.md` (see `skills/clean-code-agent/SKILL.md` for the established pattern).
- When adding a new skill, update the "Available Skills" table in `README.md`.

## Existing Skills

- `clean-code-agent` — foundational coding discipline (SOLID, GRASP, DDD, Clean Coder, AVR Loop). Designed to trigger on *any* code-producing task. When editing it, preserve its "always-on" framing in the `description`.
