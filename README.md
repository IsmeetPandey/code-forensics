# Code Forensics 🧬

> Investigate how a codebase evolved through Git history.

Code Forensics is a repository archaeology tool that turns Git history into structured evidence: commit activity, contributors, change hotspots, and Python structure metrics.

## What it does

- Reports commit count and recent commit metadata
- Lists contributors
- Finds frequently changed file hotspots
- Counts Python functions and classes with the AST
- Emits structured JSON for later visualization or reporting

## Quick start

```bash
python forensics.py path/to/repository
```

The command emits JSON that can be consumed by a dashboard, report generator, or other analysis tooling.

## Engineering principle

A hotspot is a **signal, not proof** of a bug, poor engineering, or architectural weakness. The tool reports evidence and leaves interpretation to the developer.

## Quality & maintenance

- Dependency updates are managed with Dependabot.
- CI performs a Python compilation/smoke check on pushes and pull requests.
- Contributions are documented in `CONTRIBUTING.md`.
- Security reports should follow `SECURITY.md`.

## Roadmap

- [ ] Line-level churn analysis
- [ ] Refactor vs. bug-fix signals
- [ ] Architecture milestones
- [ ] Interactive timelines
- [ ] Exportable reports

## Scope

Run the analysis against repositories you are authorized to inspect. Treat generated findings as analytical signals that require human review.
