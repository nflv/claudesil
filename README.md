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

## Template repository contents

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
