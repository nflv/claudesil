````md

<img width="1536" height="1024" alt="crab transparent" src="https://github.com/user-attachments/assets/dde8f855-5ea8-4ab6-a3f4-a4d48538ac52" />

# Claude Self-Improvement Repo

A practical, publish-ready system for making Claude Code more reliable by turning repeated mistakes into explicit rules, workflows, and reusable project memory.

<p align="left">
  <img alt="GitHub stars" src="https://img.shields.io/github/stars/yourname/claude-self-improvement-repo?style=flat-square">
  <img alt="GitHub forks" src="https://img.shields.io/github/forks/yourname/claude-self-improvement-repo?style=flat-square">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-blue?style=flat-square">
  <img alt="Claude Code" src="https://img.shields.io/badge/built%20for-Claude%20Code-6b46c1?style=flat-square">
</p>

---

## What this repo is

This repository does two jobs:

1. **ChatGPT Skill**  
   Helps generate a clean Claude Code workflow with `CLAUDE.md`, modular rules, task tracking, examples, and diagrams.

2. **Template Repository**  
   Gives you a documented starter repo you can publish directly or adapt to your own projects.

> The core idea is simple: every repeated mistake should become a rule, checklist item, example, or workflow so it does not happen again.

That is the self-improvement loop.

---

## Why this exists

Claude does **not** improve automatically.

It becomes more reliable only when you build a feedback system around it:

- detect repeated mistakes
- convert them into explicit instructions
- verify outcomes
- keep the rules short, specific, and updated

This repo turns that process into something concrete and reusable.

---

## The self-improvement loop

<p align="center">
  <img src="https://github.com/user-attachments/assets/44043487-3405-439b-a1ed-6a5fb0fe016a" alt="Self-improvement loop diagram" width="520">
</p>

**Loop:**

1. Claude makes a mistake or produces a weak result  
2. You identify the failure pattern  
3. You convert the pattern into a rule, checklist, or example  
4. Future sessions start with better guardrails  

---

## Who this is for

Use this repo if you want to:

- publish a polished GitHub repo explaining `CLAUDE.md`
- build a reliable Claude Code workflow for yourself or your team
- replace vague prompting with repeatable systems
- teach others how project memory, rules, and workflows should actually work
- turn trial-and-error into accumulated operational knowledge

---

## What’s included

```text
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
````

---

## Repository structure

| Path                      | Purpose                                                  |
| ------------------------- | -------------------------------------------------------- |
| `README.md`               | Fast explanation of the repo, concept, and quick start   |
| `guide.md`                | Deeper explanation of the full system                    |
| `CLAUDE.md`               | Main operational rules Claude should follow in this repo |
| `CLAUDE.local.example.md` | Example private override file                            |
| `.claude/rules/`          | Modular rules split by topic                             |
| `.claude/workflows/`      | Playbooks for recurring work types                       |
| `tasks/`                  | Planning, progress tracking, and review notes            |
| `learnings/`              | Captured mistakes and the rules created from them        |
| `diagrams/`               | Visual explanations of the system                        |
| `examples/`               | Before/after examples and realistic sessions             |

---

## How Claude memory actually works

Claude Code does not “remember everything forever” like a human.

It reads the memory files you provide at the start of work and uses those files as instructions and context for the current session.

### Memory layers

* **Global memory** → your personal preferences across all projects
* **Project memory** → rules for a specific repository
* **Local memory** → your private notes for one project
* **Modular rules** → additional files loaded by topic

<p align="center">
  <img src="https://github.com/user-attachments/assets/cb2ee08d-cc5c-45c3-9b66-fa31f937cbc3" alt="How Claude reads memory" width="420">
</p>

### Priority order

If two rules conflict, the more specific one wins:

```text
CLAUDE.local.md
CLAUDE.md (project)
~/.claude/CLAUDE.md
```

That means:

* your private local override beats the team default
* the project rule beats your general preference
* the global file is the weakest layer

### Memory hierarchy diagram

<p align="center">
  <img src="https://github.com/user-attachments/assets/98b2f9fb-aeec-4c74-abed-b7afd761b7bd" alt="Memory hierarchy diagram" width="700">
</p>

### What each file is for

#### `~/.claude/CLAUDE.md`

Use this for preferences you want in **every project**.

Examples:

* preferred coding style
* default explanation style
* general planning behavior
* formatting preferences

#### `./CLAUDE.md`

Use this for rules the **whole repository** should follow.

Examples:

* architecture rules
* test commands
* branch naming
* code review expectations
* project-specific constraints

This file should usually be committed to Git.

#### `./CLAUDE.local.md`

Use this for **private notes** that should not be committed.

Examples:

* local machine setup
* temporary reminders
* personal shortcuts
* one-off workflow preferences

This file should usually be in `.gitignore`.

#### `.claude/rules/*.md`

Use these to split large rules into smaller topic-specific files.

Examples:

* `coding.md`
* `testing.md`
* `debugging.md`
* `api-routes.md`

This keeps the main `CLAUDE.md` short and high-signal.

---

## Quick start

### 1. Create a project `CLAUDE.md`

At the root of your repo, add a `CLAUDE.md`.

Start small. Do not write a giant manifesto.

```md
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
```

---

### 2. Add modular rules

Create `.claude/rules/` and split rules by topic.

```text
.claude/
  rules/
    coding.md
    testing.md
    git.md
    debugging.md
```

This avoids one huge file and makes maintenance easier.

---

### 3. Use task tracking

Create a task file such as `tasks/todo.md`.

For every non-trivial task:

* write the plan
* track progress
* add a short review at the end

```md
# Task: Fix broken auth redirect

## Plan
- [ ] Reproduce the bug
- [ ] Find the root cause
- [ ] Implement the fix
- [ ] Run tests
- [ ] Document the lesson

## Review
- Root cause was wrong callback path
- Added regression test
- Added rule to avoid hardcoded redirect paths
```

---

### 4. Verify before calling it done

Do not stop at “the code changed.”

Done means **verified**.

Examples:

* UI → open and test it
* backend → run tests
* infrastructure → check logs
* bugfix → reproduce before and after

If there is no verification step, the workflow is weak.

---

### 5. Turn repeated mistakes into rules

Whenever Claude makes a mistake twice, convert that mistake into a rule.

```md
## New learning
- Mistake: Changed unrelated files during a refactor
- Cause: Scope was too broad
- Rule: Only modify files directly required for the task unless explicitly asked
```

That is how the system compounds over time.

---

## Good rules vs bad rules

Most teams write rules like this:

```md
- Write clean code
- Test your changes
- Keep files organized
- Use best practices
```

These sound fine, but they are weak because they are:

* vague
* not testable
* not project-specific
* already obvious to the model

Better rules look like this:

```md
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
```

---

## Why this works

This system improves Claude output because it adds:

### 1. Real constraints

Claude now knows:

* where things belong
* how to verify changes
* what failure patterns to avoid
* what “done” actually means

### 2. Consistency across sessions

Different sessions produce more similar outputs because the repo contains stable instructions.

### 3. Fewer repeated mistakes

Failures are captured and turned into guardrails.

<p align="center">
  <img src="https://github.com/user-attachments/assets/d7b2f1da-3f03-475b-ba7d-5ec72ec1c497" alt="Feedback loop diagram" width="520">
</p>

---

## File hierarchy

<p align="center">
  <img src="https://github.com/user-attachments/assets/428fa84b-437f-4a57-a479-6011f2258431" alt="File hierarchy diagram" width="520">
</p>

---

## Full system breakdown

The README should give fast understanding.

For the full explanation, put the deeper content in `guide.md`.

That guide should cover:

* what `CLAUDE.md` is
* where each memory file belongs
* what to include and what to avoid
* how imports work
* how modular rules work
* workflow patterns
* how to evolve the system over time
* common mistakes when writing memory files

### Rule of thumb

* `README.md` → fast understanding
* `guide.md` → full explanation
* `CLAUDE.md` → operational rules
* `.claude/rules/` → modular extensions
* `tasks/` → execution tracking
* `learnings/` → institutional memory

---

## Suggested publishing flow

1. Copy `assets/template-repo/` into a new GitHub repository
2. Tailor `CLAUDE.md` to your own project
3. Replace the example learnings with real failures from actual use
4. Keep the core file short and move detailed rules into `.claude/rules/`
5. Publish the repo as both a guide and a starter kit

---

## Why this is a strong skill

Most skill ideas fail because they are abstract.

This one is concrete:

* **clear inputs** → pasted context and uploaded files
* **clear outputs** → repo skeleton, docs, diagrams, reusable rules
* **clear workflow** → diagnose, codify, verify, iterate

That makes it usable, teachable, and repeatable.

---

## Principles

* Keep `CLAUDE.md` compact
* Prefer examples over theory
* Prefer checklists over vague advice
* Prefer specific rules over motivational language
* Treat repeated corrections as missing system design

---

## Summary

The shortest honest description of this repo is:

> A practical system for making Claude Code more reliable by turning repeated mistakes into explicit rules, workflows, and reusable project memory.

If you only do five things:

1. create `CLAUDE.md`
2. add a few repo-specific rules
3. create `.claude/rules/`
4. track tasks in `tasks/todo.md`
5. update rules whenever mistakes repeat

That is the system.

---

## License

MIT

---

## Contributing

Contributions are welcome.

Useful contributions include:

* clearer templates
* better examples
* improved workflows
* stronger diagrams
* real-world lessons from repeated Claude failures

If you find a repeated failure pattern, turn it into a rule and open a PR.

```
