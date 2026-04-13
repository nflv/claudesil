# Example Patterns

## Strong examples

A strong example shows:

- the original weak behavior
- the problem with it
- the corrected rule
- the resulting improved behavior

## Weak example

"Claude was bad at coding, so we made a better file."

This teaches nothing.

## Strong example

Mistake:
Claude made broad edits across unrelated files while fixing a narrow bug.

Root cause:
There was no explicit rule limiting scope.

Rule added:
"Never modify unrelated files when addressing a single reported bug."

Impact:
Future fixes stay localized and review gets easier.

## Good repo writing pattern

Use this structure for explanatory sections:

- what it is
- why it exists
- when to use it
- common failure mode
- best practice
