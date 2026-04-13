# Claude Self Improvement Repo

A push-ready skill repository that teaches and scaffolds a well-documented GitHub repo for Claude Code workflows.

This package does two jobs:

1. It acts as a **ChatGPT Skill** that helps users create a clean repository with `CLAUDE.md`, modular rules, task tracking, diagrams, examples, and a documented self-improvement loop.
2. It includes a **template repository** that users can publish directly or adapt for their own project.

The central idea is simple:

> Every repeated mistake should become a rule, example, or checklist item so the model does not make the same mistake again.

That is the self-improvement loop.

## What this repository includes

- `SKILL.md` - the skill entrypoint and operating instructions
- `agents/openai.yaml` - ChatGPT skill metadata
- `references/` - the guide material the skill loads when needed
- `assets/template-repo/` - a complete template repository users can copy and publish
- `scripts/` - lightweight helper tooling for validation and adoption

## Who this is for

Use this if you want to:

- publish a polished GitHub repo explaining `CLAUDE.md`
- teach others how to structure project memory and rules for Claude Code
- demonstrate the self-improvement loop with examples and diagrams
- give teams a reusable starter kit instead of vague advice

## Core concept

The self-improvement loop is not “AI learns magically.”
It is a disciplined workflow:

1. Claude makes a mistake or produces a weak result.
2. You identify the failure pattern.
3. You convert that pattern into an explicit rule, checklist, example, or template.
4. Future sessions start with better guardrails.

This repository turns that loop into a concrete, reproducible system.

## Diagram

<img width="816" height="1475" alt="mermaid-diagram (1)" src="https://github.com/user-attachments/assets/44043487-3405-439b-a1ed-6a5fb0fe016a" />

# Claude Self-Improvement System

## 1. What this is
This is a system that makes Claude stop repeating mistakes.

## 2. The core idea
Claude does not learn automatically.
You must convert errors into rules.

## 3. The Loop

<img width="816" height="1475" alt="mermaid-diagram (1)" src="https://github.com/user-attachments/assets/fe2eea0c-0bb1-4994-a065-048f7887b78f" />


## 4. File hierarchy

<img width="816" height="1475" alt="mermaid-diagram (1)" src="https://github.com/user-attachments/assets/428fa84b-437f-4a57-a479-6011f2258431" />


## 5. How Claude actually reads your memory

<img width="621" height="2075" alt="mermaid-diagram (2)" src="https://github.com/user-attachments/assets/cb2ee08d-cc5c-45c3-9b66-fa31f937cbc3" />

Claude Code does not “remember everything forever” like a human.

It reads the memory files you give it at the start of work, then uses those files as instructions and context for the current session.

The idea is simple:

Global memory = your personal preferences across all projects
Project memory = rules for this specific repository
Local memory = your private notes for this project only
Modular rules = extra rules loaded when relevant

According to the hierarchy you shared, Claude Code supports these layers: global ~/.claude/CLAUDE.md, project ./CLAUDE.md or ./.claude/CLAUDE.md, and local ./CLAUDE.local.md, with more specific files taking priority over broader ones. Modular rules can live under .claude/rules/.

Memory Hierarchy:

<img width="2252" height="932" alt="mermaid-diagram (3)" src="https://github.com/user-attachments/assets/98b2f9fb-aeec-4c74-abed-b7afd761b7bd" />

Priority order

If two rules conflict, the more specific one wins:

CLAUDE.local.md
project CLAUDE.md
global ~/.claude/CLAUDE.md

That means:

your personal override for one repo beats the team default
the repo rule beats your general preference
the global file is the weakest layer
What each file is for
~/.claude/CLAUDE.md

Use this for things you want in every project.

Examples:

preferred coding style
how you like explanations
default behavior for planning
personal formatting preferences
./CLAUDE.md

Use this for rules the whole repository should follow.

Examples:

architecture rules
test commands
branch naming
code review expectations
important project quirks

This file should usually be committed to git so the whole team shares the same base context.

./CLAUDE.local.md

Use this for private notes that should not be committed.

Examples:

your own shortcuts
local machine setup
temporary project reminders
personal workflow preferences

This should usually be added to .gitignore.

.claude/rules/*.md

Use these to split large rules into smaller files.

Examples:

coding.md
testing.md
debugging.md
api-routes.md

This keeps the main CLAUDE.md short and easier to maintain.

Important truth

Claude does not become better just because the file exists.

It becomes better only when:

the rules are specific
the rules are short
the rules are based on real mistakes
the rules are updated over time

That is the whole self-improvement loop.


## 6. Quick start (5 steps)

Step 1 — Create a project CLAUDE.md

At the root of your repo, add a CLAUDE.md.

Start small. Do not write a giant manifesto.

Good first sections:

code style
architecture
workflow
testing
common mistakes

Example:

# Code Style
- Use TypeScript, not plain JavaScript
- Use ES modules
- Keep functions small and explicit

# Architecture
- API routes live in src/api/
- Database logic lives in src/db/
- Do not mix UI and server code

# Workflow
- For tasks with more than 3 steps, make a plan first
- Keep changes minimal
- Do not edit unrelated files

# Testing
- Run npm test before finishing
- Run npm run typecheck before commit
Step 2 — Add modular rules

Create .claude/rules/ and split rules by topic.

Example:

.claude/
  rules/
    coding.md
    testing.md
    git.md
    debugging.md

This helps avoid one huge file.

Step 3 — Use task tracking

Create a task file like tasks/todo.md.

For every non-trivial task:

write the plan
track progress
write a short review at the end

Example:

# Task: Fix broken auth redirect

## Plan
- [ ] Reproduce the bug
- [ ] Find root cause
- [ ] Implement fix
- [ ] Run tests
- [ ] Document lesson

## Review
- Root cause was wrong callback path
- Added regression test
- Added rule to avoid hardcoded redirect paths
Step 4 — Verify before calling it done

Do not let Claude stop at “I changed the code.”

Done means verified.

Examples:

UI: open and test it
backend: run tests
infra: check logs
bugfix: reproduce before and after

If there is no verification step, the workflow is weak.

Step 5 — Turn mistakes into rules

Whenever Claude makes a mistake twice, convert that mistake into a rule.

Simple format:

## New learning
- Mistake: Changed unrelated files during refactor
- Cause: Scope was too broad
- Rule: Only modify files directly needed for the task unless explicitly asked

That is how the system compounds over time.

## 7. Real example (before/after)

This section matters because theory alone is weak.

Before

The team uses vague rules like this:

# Rules
- Write clean code
- Test your changes
- Keep files organized
- Use best practices

This looks nice but it is mostly useless.

Why it fails:

too vague
not testable
no project context
Claude already knows generic advice
After

Now the team writes specific rules:

# Code Style
- Use ES modules only; do not use CommonJS
- Prefer named exports for shared utilities
- Keep API handlers under src/api/handlers/

# Testing
- Run npm run test:unit before completion
- Run npm run typecheck before commit
- For auth changes, also run npm run test:auth

# Workflow
- For tasks with more than 3 steps, write a plan in tasks/todo.md first
- Do not modify unrelated files
- If a fix is temporary, say so explicitly and explain the tradeoff

# Common Mistakes
- Do not hardcode environment-specific URLs
- Do not rename files during bugfixes unless required
- Do not skip regression tests for production bugs
What improved
1. Claude has real constraints

It now knows:

where things belong
how to verify changes
what errors to avoid
2. The repo becomes more consistent

Different sessions produce more similar results.

3. Repeated mistakes go down

Because the system captures failures and turns them into guardrails.

The deeper point

The improvement does not come from “better prompting.”

It comes from building a feedback loop:

<img width="849" height="1475" alt="mermaid-diagram (4)" src="https://github.com/user-attachments/assets/d7b2f1da-3f03-475b-ba7d-5ec72ec1c497" />

## 8. Full system breakdown (link to guide.md)

Full system breakdown

For the full explanation, see guide.md
.

That guide should cover:

what CLAUDE.md is
where to place each file
what to include and what to avoid
how @imports work
how modular rules work
the Boris Cherny workflow
how to evolve the system over time
common mistakes when writing memory files

In short:

README = fast understanding
guide.md = full explanation
CLAUDE.md = actual operational rules
.claude/rules/ = modular extensions
tasks/ = execution tracking
learnings/ = institutional memory
Template repository contents

Here is what each part of the template repo is for.

claude-self-improvement-repo/
├── README.md
├── guide.md
├── CLAUDE.md
├── CLAUDE.local.example.md
├── .claude/
│   ├── rules/
│   │   ├── coding.md
│   │   ├── testing.md
│   │   ├── git.md
│   │   └── debugging.md
│   └── workflows/
│       ├── plan-mode.md
│       ├── bugfix.md
│       └── refactor.md
├── tasks/
│   └── todo.example.md
├── learnings/
│   └── examples.md
├── diagrams/
│   ├── memory-hierarchy.mmd
│   ├── self-improvement-loop.mmd
│   └── workflow.mmd
└── examples/
    ├── bad-vs-good.md
    └── real-session.md
README.md

The front door.

Purpose:

explain what the repo is
show the core idea fast
include diagrams
help people start quickly

This should be simple and convincing.

guide.md

The deep explanation.

Purpose:

explain the full mental model
teach the hierarchy
explain the workflow in plain language
show best practices and anti-patterns

This is where you go broad and detailed.

CLAUDE.md

The operating file.

Purpose:

store the main rules Claude should follow in this repo
keep the high-signal instructions in one place

This is the most important file in the system.

CLAUDE.local.example.md

A personal override template.

Purpose:

show users how to create local personal instructions
keep private preferences out of git

This should be an example, not the real private file.

.claude/rules/

Modular rules.

Purpose:

split rules by topic
keep CLAUDE.md short
allow more focused maintenance

Examples:

coding rules
testing rules
git workflow
debugging habits
.claude/workflows/

Process playbooks.

Purpose:

explain how to handle recurring work types
reduce ambiguity for common tasks

Examples:

plan mode workflow
bugfix workflow
refactor workflow
tasks/

Execution tracking.

Purpose:

store plans
track progress
record review notes

This is where the process becomes operational instead of theoretical.

learnings/

Captured lessons.

Purpose:

store examples of mistakes and corrections
make the self-improvement loop visible

This is the memory of the system.

diagrams/

Visual explanations.

Purpose:

make the system easier to understand
show structure at a glance
help people learn faster

Important: do not leave diagrams only as source files. Also render them to PNG or SVG if you want the repo to feel polished.

examples/

Concrete demonstrations.

Purpose:

show bad vs good rules
show a realistic session
make the system believable

Without examples, the repo stays abstract.

## summary

If someone asks, “What is this repo?” the shortest honest answer is:

This repo is a practical system for making Claude Code more reliable by turning repeated mistakes into explicit rules, task workflows, and reusable project memory.

If someone asks, “What should I do first?”:

create CLAUDE.md
add a few repo-specific rules
create .claude/rules/
track tasks in tasks/todo.md
update rules whenever mistakes repeat

The bundled template repo contains:

- `README.md` with positioning, installation, and usage docs
- `CLAUDE.md` core memory and workflow rules
- `.claude/rules/` modular rules
- `.claude/workflows/` structured procedures
- `tasks/todo.example.md` for planning and review
- `learnings/examples.md` to store mistakes and the rule created from them
- `diagrams/` with Mermaid charts
- `examples/` with before/after examples

## Suggested publishing flow

1. Copy `assets/template-repo/` into a new GitHub repository.
2. Tailor `CLAUDE.md` to your project.
3. Replace the example learnings with real failures from your own usage.
4. Keep the core file short and move detailed rules into `.claude/rules/`.
5. Publish the repo as both a guide and a starter kit.

## Why this is a good skill

Most skill ideas fail because they are too abstract. This one is concrete:

- clear inputs: pasted context and uploaded files
- clear outputs: a repository skeleton, docs, diagrams, and reusable rules
- clear workflow: diagnose, codify, verify, iterate

## Notes

- Keep `CLAUDE.md` compact. Long files degrade adherence.
- Prefer examples, templates, and checklists over theory.
- Treat every repeated correction as missing system design.
