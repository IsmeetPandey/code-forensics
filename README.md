# Code Forensics 🧬

A repository archaeology tool that studies how a codebase evolved through Git history and highlights change hotspots.

## Run locally

```bash
python forensics.py path/to/repository
```

The command emits structured JSON so the analysis can later feed a web dashboard or report generator.

## Current MVP

- Git commit count and recent commit metadata
- Contributor list
- File change-frequency hotspots
- Python AST function/class counts
- JSON output suitable for further visualization

## Design principle

A hotspot is a **signal**, not proof of a bug or poor engineering. The tool reports evidence and leaves interpretation to the developer.

Future versions: line churn, refactor/bug-fix signals, architecture milestones, interactive timelines, and exportable reports.
