# Real Session Pattern

## Initial problem

Claude fixed a UI bug by renaming variables, moving files, and changing unrelated formatting.

## Diagnosis

The repo lacked a scoped-change rule and had no explicit bug-fix workflow.

## Correction

Added:

- `CLAUDE.md`: never modify unrelated files during a focused fix
- `.claude/workflows/bugfix.md`: reproduce -> isolate -> fix -> verify -> capture learning

## Result

Future bug fixes became smaller, easier to review, and less likely to create side effects.
