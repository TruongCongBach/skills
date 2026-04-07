# Skills

Personal skills repository for Claude Code. Each skill is a self-contained folder with a `SKILL.md` file containing YAML frontmatter and instructions.

## Available Skills

| Skill | Description |
|-------|-------------|
| [clean-code-agent](./skills/clean-code-agent/) | Foundational coding discipline enforcing SOLID, GRASP, DDD, Clean Coder, Design Patterns and AVR Loop |

## Skill Structure

```
skills/
└── skill-name/
    ├── SKILL.md          # Required: frontmatter + instructions
    ├── references/       # Optional: detailed reference docs
    └── evals/            # Optional: evaluation test cases
```

## Creating a New Skill

Use the [template](./template/SKILL.md) as a starting point:

```markdown
---
name: my-skill-name
description: A clear description of what this skill does and when to use it
---

# My Skill Name

[Instructions here]
```

## Installation

Register this repo as a skill source in Claude Code:

```
/skills add /path/to/this/repo
```
