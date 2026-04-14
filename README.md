# Skills

Personal Codex skills repository for daily ticket work in React Native and Next.js projects. Each skill is a self-contained folder with a `SKILL.md` file, optional `references/`, and optional helper scripts.

## Available Skills

| Skill | Purpose |
|-------|---------|
| [clean-code-agent](./skills/clean-code-agent/) | Foundational coding discipline for implementation work |
| [ticket-analyzer](./skills/ticket-analyzer/) | Triage a Jira ticket before coding and decide if it is ready for implementation |
| [fix-planner](./skills/fix-planner/) | Propose implementation approaches after analysis and before coding |
| [implementation-reviewer](./skills/implementation-reviewer/) | Review completed implementation against Jira, UX, and engineering quality |
| [change-summarizer](./skills/change-summarizer/) | Summarize the completed change for engineers and QA handoff |
| [ticket-closure-helper](./skills/ticket-closure-helper/) | Prepare the final Jira closure comment and QA closure note after approval |

## Recommended Workflow

Use the skills in this order for the cleanest handoff chain:

1. `ticket-analyzer`
2. `fix-planner`
3. `clean-code-agent`
4. `implementation-reviewer`
5. `change-summarizer`
6. `ticket-closure-helper`

Load the workflow guide in [docs/daily-workflow.md](./docs/daily-workflow.md) for stage-by-stage intent and handoff boundaries.

## Avoiding Skill Confusion

Some skills are intentionally close together, so explicit invocation is the safest way to avoid the wrong one triggering when this repo coexists with other skills on another machine.

Use prompts like:

- `Use ticket-analyzer to triage this Jira bug before coding.`
- `Use fix-planner to compare implementation approaches for this ticket.`
- `Use implementation-reviewer to review this completed PR against the ticket.`
- `Use change-summarizer to write the engineering and QA handoff summary.`
- `Use ticket-closure-helper to draft the final Jira closure comment.`

Prompt examples live in [examples/explicit-prompt-examples.md](./examples/explicit-prompt-examples.md).

## Repo Structure

```text
skills/
└── skill-name/
    ├── SKILL.md
    ├── references/
    ├── scripts/
    └── evals/
```

## Installation On Other Machines

Recommended approach: install this repo as a reusable skill source and keep it updated through Git.

### Option 1: Install Directly From GitHub

If your skills CLI supports GitHub sources, install the whole repo with:

```bash
npx skills add https://github.com/TruongCongBach/skills
```

Install a single skill from the repo with:

```bash
npx skills add https://github.com/TruongCongBach/skills --skill ticket-analyzer
```

Examples:

```bash
npx skills add https://github.com/TruongCongBach/skills --skill fix-planner
npx skills add https://github.com/TruongCongBach/skills --skill implementation-reviewer
npx skills add https://github.com/TruongCongBach/skills --skill change-summarizer
npx skills add https://github.com/TruongCongBach/skills --skill ticket-closure-helper
```

Use the repo root URL, not a GitHub subfolder URL for an individual skill.

### Option 2: Clone The Repo And Register The Local Path

1. Clone the repo:

```bash
git clone https://github.com/TruongCongBach/skills.git ~/my-codex-skills
```

2. Register the repo as a skills source if your client supports skill-source registration:

```text
/skills add /absolute/path/to/my-codex-skills
```

3. Update later with:

```bash
cd ~/my-codex-skills
git pull
```

If your Codex setup does not support GitHub installation or `/skills add`, use the cloned repo as the source of truth and copy or symlink individual folders from `skills/<skill-name>/` into the local skills directory that your client reads.

## Installing Only One Skill

If you want to avoid loading the whole repo on another machine, install one skill explicitly:

```bash
npx skills add https://github.com/TruongCongBach/skills --skill ticket-analyzer
```

When the machine already has many other skills, explicit installation plus explicit prompting is the safest setup.

Prompt examples:

- `Use ticket-analyzer to triage this Jira bug before coding.`
- `Use fix-planner to compare implementation approaches.`
- `Use implementation-reviewer to review this completed work.`
- `Use change-summarizer to write the engineering handoff.`
- `Use ticket-closure-helper to draft the final Jira closure comment.`

## Packaging

The root `skill.zip` file is treated as a local build artifact and is ignored. To generate distributable archives, run:

```bash
python3 scripts/package_skills.py
```

This creates:

- `dist/<skill-name>.zip` for each skill
- `dist/skills-bundle.zip` containing the whole `skills/` directory

## Creating A New Skill

Use the [template](./template/SKILL.md) as a starting point or follow the patterns in the existing workflow-oriented skills.
