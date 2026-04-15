# Skills

Personal Codex skills repository for daily ticket work in React Native and Next.js projects. Each skill is a self-contained folder with a `SKILL.md` file, optional `references/`, and optional helper scripts.

The ticket workflow skills are written to mirror the user's current language automatically. If the conversation is in Vietnamese, the skill should respond in Vietnamese. If the conversation is in English, the skill should respond in English.

Security risk assessment is treated as a cross-cutting layer across the workflow rather than a separate skill. `ticket-analysis` flags security-sensitive impact, `ticket-planner` proposes mitigations, `ticket-review` checks security findings, and `ticket-summary` or `ticket-close` preserve only the security context that future readers still need.

Design-image handling is also integrated into the workflow. `ticket-analysis` and `ticket-planner` can turn screenshots or design images into structured Markdown through [scripts/extract_design_context.py](./scripts/extract_design_context.py), with OmniParser as the preferred engine and MarkItDown as the fallback.

No extra skill is required for design-image extraction on another machine. The existing ticket skills already know how to call the wrapper script. What the other machine may need is optional parser tooling such as OmniParser or MarkItDown.

## Available Skills

| Skill | Purpose |
|-------|---------|
| [clean-code-agent](./skills/clean-code-agent/) | Foundational coding discipline for implementation work |
| [ticket-analysis](./skills/ticket-analysis/) | Triage a Jira ticket before coding and decide if it is ready for implementation |
| [ticket-planner](./skills/ticket-planner/) | Propose implementation approaches after analysis and before coding |
| [ticket-review](./skills/ticket-review/) | Review completed implementation against Jira, UX, and engineering quality |
| [ticket-commit](./skills/ticket-commit/) | Prepare and optionally perform a safe Jira-scoped commit using only relevant files |
| [ticket-summary](./skills/ticket-summary/) | Summarize the completed change for engineers and QA handoff |
| [ticket-close](./skills/ticket-close/) | Prepare the final Jira closure comment and QA closure note after approval |

## Recommended Workflow

Use the skills in this order for the cleanest handoff chain:

1. `ticket-analysis`
2. `ticket-planner`
3. `clean-code-agent`
4. `ticket-review`
5. `ticket-commit`
6. `ticket-summary`
7. `ticket-close`

Load the workflow guide in [docs/daily-workflow.md](./docs/daily-workflow.md) for stage-by-stage intent and handoff boundaries.
Load the shared security references in [docs/security/](./docs/security/) when the ticket touches auth, permissions, tokens, storage, logging, uploads, deep links, WebViews, or server/client trust boundaries.

## Avoiding Skill Confusion

Some skills are intentionally close together, so explicit invocation is the safest way to avoid the wrong one triggering when this repo coexists with other skills on another machine.

Use prompts like:

- `Use ticket-analysis to triage this Jira bug before coding.`
- `Use ticket-planner to compare implementation approaches for this ticket.`
- `Use ticket-review to review this completed PR against the ticket.`
- `Use ticket-commit to prepare a safe commit for this Jira issue.`
- `Use ticket-summary to write the engineering and QA handoff summary.`
- `Use ticket-close to draft the final Jira closure comment.`

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
npx skills add https://github.com/TruongCongBach/skills --skill ticket-analysis
```

Examples:

```bash
npx skills add https://github.com/TruongCongBach/skills --skill ticket-planner
npx skills add https://github.com/TruongCongBach/skills --skill ticket-review
npx skills add https://github.com/TruongCongBach/skills --skill ticket-commit
npx skills add https://github.com/TruongCongBach/skills --skill ticket-summary
npx skills add https://github.com/TruongCongBach/skills --skill ticket-close
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

## Extra Setup For Design Images On Other Machines

You do **not** need to install another skill for screenshot or design-image parsing.

You only need:

1. This skills repo
2. Optional parser tooling on that machine if you want higher-quality design extraction

Recommended parser setup:

- Preferred: OmniParser
- Fallback: MarkItDown

Quick guidance:

- If the machine only uses normal ticket text and no design images, no extra setup is needed.
- If the machine needs image-to-Markdown support for UI work, configure OmniParser or install MarkItDown.

See:

- [docs/design/design-extraction-setup.md](./docs/design/design-extraction-setup.md)

Typical setup choices:

### Option A: Best Quality

Install or run OmniParser separately on that machine, then set one of:

```bash
export OMNIPARSER_URL="http://localhost:7860/process_image"
```

or

```bash
export OMNIPARSER_CMD="python /absolute/path/to/your_omniparser_wrapper.py --json"
```

### Option B: Easier Fallback

Install MarkItDown:

```bash
pip install 'markitdown[all]'
```

or ensure:

```bash
uvx markitdown path/to/file.png
```

### Test The Setup

After setup, verify with:

```bash
python3 scripts/extract_design_context.py path/to/image.png --include-raw
```

If the machine is configured correctly, the script will output a structured Markdown note the ticket skills can reuse.

## Installing Only One Skill

If you want to avoid loading the whole repo on another machine, install one skill explicitly:

```bash
npx skills add https://github.com/TruongCongBach/skills --skill ticket-analysis
```

When the machine already has many other skills, explicit installation plus explicit prompting is the safest setup.

Prompt examples:

- `Use ticket-analysis to triage this Jira bug before coding.`
- `Use ticket-planner to compare implementation approaches.`
- `Use ticket-review to review this completed work.`
- `Use ticket-commit to prepare the commit safely.`
- `Use ticket-summary to write the engineering handoff.`
- `Use ticket-close to draft the final Jira closure comment.`

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
