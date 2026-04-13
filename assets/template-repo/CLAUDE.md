# Core Principles

- Always identify the root cause before changing code.
- Prefer deleting code over adding complexity.
- Never modify unrelated files during a focused fix.
- Keep changes easy to review.

# Planning

- For any task with more than 3 steps, start with a short written plan.
- Track progress in `tasks/todo.example.md` or a task-specific copy.
- When a task changes shape, update the plan instead of improvising silently.

# Implementation

- Touch the minimum number of files needed.
- Preserve existing conventions unless there is a clear reason to improve them.
- Flag ambiguity early and make assumptions explicit.

# Verification

- A task is not done until the relevant checks have been run.
- Record the commands used for verification when they are not obvious.
- If no verification is possible, state that clearly.

# Self-Improvement Loop

When Claude makes a mistake or produces a weak result:

1. Write down the failure pattern.
2. Identify why it happened.
3. Add a rule, workflow step, example, or checklist item.
4. Store the lesson in `learnings/examples.md`.

# Repository Conventions

- Put short, high-value project memory here.
- Put topic-specific rules in `.claude/rules/`.
- Put procedures in `.claude/workflows/`.
- Keep this file under 200 lines.
