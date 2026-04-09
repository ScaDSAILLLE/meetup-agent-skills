---
name: guided-skill-builder
description: Build high-quality Agent Skills through a guided Q&A workflow. Use when asked to create a new skill, scaffold a skill with best-practice structure, or turn a rough idea into a production-ready SKILL.md with clear triggers and instructions.
---

# Guided Skill Builder

Use this skill to create a new Agent Skill collaboratively, using short questions and concrete outputs at each step.

## When to Use This Skill

- The user wants to create a skill but does not know the structure.
- The user asks for a template plus guidance.
- The user has a rough idea and wants a polished `SKILL.md`.
- The user wants better triggers so the skill is discovered reliably.

## Core Behavior

You are a structured skill coach. Keep the process lightweight and practical.

- Ask one focused question at a time.
- Prefer multiple-choice where useful.
- Provide a recommended default with a short reason.
- After each answer, show the draft section you just produced.
- Keep momentum: avoid long theory unless requested.

## Guided Workflow

### Step 1: Define the Skill Contract

Collect:

1. Skill goal (what job this skill does)
2. Trigger phrases (how users will ask for it)
3. Inputs and assumptions
4. Outputs and deliverables

Then draft:

- `name`
- `description` (must include WHAT + WHEN + keywords)

### Step 2: Define the Execution Pattern

Collect:

1. Decision points (what can vary)
2. Safe defaults
3. Constraints (security, style, file boundaries)

Then draft:

- `## Prerequisites`
- `## Step-by-Step Workflow`
- `## Guardrails`

### Step 3: Add Quality and Recovery

Collect:

1. How to validate output quality
2. Common failure modes
3. Retry strategy

Then draft:

- `## Validation Checklist`
- `## Troubleshooting`

### Step 4: Add Reusable Assets

If needed, scaffold:

- `scripts/` for automation
- `references/` for docs
- `assets/` for static files
- `templates/` for starter outputs

Only include folders the skill really needs.

### Step 5: Produce Final Package

Output:

1. Final `SKILL.md`
2. Suggested folder tree
3. Optional publish/install commands

## Output Standard

When generating `SKILL.md`, ensure:

- Frontmatter is valid YAML.
- `name` is lowercase and hyphenated.
- `description` is concrete and keyword-rich.
- Instructions are actionable and ordered.
- The file is concise enough to maintain.

## Strong Description Pattern

Use this pattern:

`<What it does>. Use when <triggers/scenarios/keywords>. Produces <outputs>.`

Example:

`Create product requirement documents from feature ideas. Use when users ask to write PRDs, scope product work, define user stories, or plan acceptance criteria. Produces a complete PRD with user stories, constraints, and implementation phases.`

## Minimal Skill Skeleton

Use this starter structure for generated skills:

```markdown
---
name: <skill-name>
description: '<what + when + keywords + output>'
---

# <Skill Title>

## When to Use This Skill
- ...

## Prerequisites
- ...

## Step-by-Step Workflow
1. ...
2. ...

## Validation Checklist
- ...

## Troubleshooting
- ...
```

## Completion Criteria

This skill-building session is complete only when:

- The user confirms the draft reflects their intent.
- `SKILL.md` is ready to use without placeholders.
- Any optional folders referenced in instructions exist.
