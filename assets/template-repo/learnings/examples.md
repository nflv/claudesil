# Learnings Log

## Learning template

- Mistake:
- Why it happened:
- Correct behavior:
- New rule:
- Rule location:

## Example 1

- Mistake: Claude edited unrelated files while fixing a small bug.
- Why it happened: There was no explicit rule limiting change scope.
- Correct behavior: Keep a focused fix inside the smallest relevant surface area.
- New rule: Never modify unrelated files during a focused fix.
- Rule location: `CLAUDE.md`

## Example 2

- Mistake: Claude marked a task done without verification.
- Why it happened: The workflow implied verification but did not require it.
- Correct behavior: A task is not complete until checks are run or the absence of checks is stated explicitly.
- New rule: Always verify before done.
- Rule location: `.claude/rules/testing.md`
