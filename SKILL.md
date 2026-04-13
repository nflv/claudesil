---
name: claude-self-improvement-repo
description: build a documented repository skeleton for claude code memory and project rules, with a strong guide to claude.md, modular rules, task workflows, examples, and diagrams. use when the user wants to create or improve a github-ready repo, starter kit, guide, or reusable template that explains and operationalizes the self-improvement loop, project memory, coding conventions, review checklists, or claude code working patterns from pasted context or uploaded files.
---

# Claude Self Improvement Repo

Build a clean, publishable repository that teaches and operationalizes `CLAUDE.md` and the self-improvement loop.

## Outcome

Produce a repo that does two things well:

1. Explain what `CLAUDE.md`, modular rules, and the self-improvement loop are.
2. Give users a usable starter kit they can publish, copy, or adapt.

Default outputs:

- repository skeleton
- root `README.md`
- core `CLAUDE.md`
- modular `.claude/` rules and workflows
- examples and diagrams
- task tracking template
- learnings log

## Operating rules

- Start from the user's actual context, not generic AI advice.
- Keep the core `CLAUDE.md` short and opinionated.
- Prefer concrete instructions, templates, and examples over explanation.
- Treat repeated mistakes as missing system design.
- Separate global rules, project rules, and local overrides.
- Make the repository understandable to a new user in under five minutes.

## Workflow

1. Identify the target repo type.
   - **Generic educational template**: use the bundled template repo in `assets/template-repo/` as the base.
   - **Project-specific repo**: adapt naming, workflows, examples, and rules from the user's pasted context or uploaded files.

2. Build the core operating files.
   - `README.md`
   - `CLAUDE.md`
   - `.claude/rules/*.md`
   - `.claude/workflows/*.md`

3. Add proof and teaching material.
   - `examples/bad_vs_good.md`
   - `examples/real_session.md`
   - `learnings/examples.md`
   - Mermaid diagrams from `assets/template-repo/diagrams/`

4. Verify quality.
   - Check that the repo explains the self-improvement loop clearly.
   - Check that each rule is concrete and enforceable.
   - Check that examples show failure, diagnosis, and codified learning.
   - Remove filler and duplicated theory.

5. Deliver a GitHub-ready structure.
   - Preserve directory clarity.
   - Keep names readable.
   - Prefer copy-paste-ready files.

## Default repo pattern

Use this structure unless the user's project clearly needs a variant:

```text
repo/
├── README.md
├── CLAUDE.md
├── CLAUDE.local.example.md
├── .claude/
│   ├── rules/
│   └── workflows/
├── tasks/
├── learnings/
├── diagrams/
└── examples/
```

## What to write in each file

### README.md

Explain:

- what the repo is
- why `CLAUDE.md` matters
- how the self-improvement loop works
- how to install or copy the template
- how to keep the system useful over time

### CLAUDE.md

Include only high-value instructions Claude would not reliably infer from code alone:

- repository-specific conventions
- testing and verification commands
- architecture constraints
- change-scope rules
- repeated failure patterns turned into guardrails

Do not fill it with generic advice.

### .claude/rules/

Use these for topic-specific rules such as:

- coding conventions
- debugging
- testing
- git and PR discipline

### .claude/workflows/

Use these for repeatable multi-step procedures such as:

- plan mode
- bug fixing
- refactoring
- adding a new learning after failure

### examples/

Show before/after transformations. The value is in demonstrating how a vague habit becomes a reliable workflow.

### learnings/

Store failure patterns in this form:

- mistake
- why it happened
- correct behavior
- new rule
- where the rule now lives

## Use bundled resources

When building a repo, consult these references directly:

- `references/guide.md` for the teaching narrative
- `references/repo-map.md` for file-by-file intent
- `references/workflow.md` for the self-improvement loop and adoption model
- `references/examples.md` for example content patterns

Use `assets/template-repo/` as the starting point for file content and layout.

## Quality bar

A strong result has these properties:

- a newcomer can understand the repo quickly
- the repo is useful without extra explanation
- the self-improvement loop is operational, not philosophical
- each included file has a job
- the repo can be pushed to GitHub immediately with minimal editing

## Avoid these failure modes

- turning the repo into a long essay
- writing vague rules such as “write clean code”
- duplicating the same guidance in three files
- hiding the actual starter files behind too much documentation
- claiming the system learns automatically instead of showing how rules are updated
