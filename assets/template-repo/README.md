# Claude Code Self-Improvement Loop

A practical repository template for documenting project memory, coding rules, and the feedback loop that makes Claude Code better over time.

## What this repo is

This repo explains and operationalizes three things:

1. `CLAUDE.md` as project memory
2. modular rules for domain-specific guidance
3. the self-improvement loop: error -> diagnosis -> rule -> better future runs

This is not a magical memory system. It is explicit system design.

## Why this exists

Claude Code is much more reliable when the project gives it concrete, reusable guidance:

- what matters in this codebase
- how to plan work
- what not to do
- how to verify work
- how to turn repeated mistakes into durable rules

Without that, each session repeats avoidable failures.

## Repository structure

```text
.
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

## How the self-improvement loop works

1. Claude produces output.
2. A mistake or weak pattern is noticed.
3. The root cause is identified.
4. A new rule, checklist, or example is written down.
5. Future sessions start with better guardrails.

That is the compounding effect.

## Quick start

1. Copy this repository into your project.
2. Edit `CLAUDE.md` with the 10 to 20 highest-value project rules.
3. Keep general rules in `.claude/rules/`.
4. Use `tasks/todo.example.md` for planning and review.
5. Add real mistakes to `learnings/examples.md`.
6. Prune weak or duplicate instructions every week.

## Design principles

- **Simplicity first**: remove complexity where possible.
- **No lazy fixes**: solve root causes, not symptoms.
- **Minimal impact**: change only what is necessary.
- **Verify before done**: the task is not complete until it is checked.

## What belongs in `CLAUDE.md`

Include:

- project-specific coding rules
- verification commands Claude will not infer reliably
- architecture constraints
- risky areas and repeated gotchas
- preferred workflow for planning and review

Do not include:

- generic coding advice
- basic language conventions already obvious from the repo
- long tutorials
- information that changes constantly

## How to keep this useful

Every time Claude repeats a mistake, ask:

- Was the rule missing?
- Was the rule too vague?
- Was the example missing?
- Was the verification loop weak?

Then update the system.

## Recommended next step

Replace the sample rules and examples with real failures from your own project. That is where the template becomes valuable.
