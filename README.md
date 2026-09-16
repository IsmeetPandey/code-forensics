# Code Forensics 🧬

A repository archaeology tool that studies how a codebase evolved through Git history and identifies change hotspots.

## Product thesis

A current codebase hides its history. Git contains evidence about which files change repeatedly, when architecture shifts happened, and where maintenance effort concentrates.

## Planned analysis

```text
Git history → commit/file metrics → hotspots → timeline → explainable report
```

Initial signals include:

- commit frequency by file
- lines added/removed over time
- churn hotspots
- bug-fix / refactor keyword signals
- contributor concentration
- files whose size and change frequency both rise
- architectural milestones inferred from file-tree changes

The tool must label these as **signals**, not proof of defects or developer quality.

## Build phases

- **Phase 1:** repository parser + baseline statistics
- **Phase 2:** file churn and hotspot analysis
- **Phase 3:** interactive repository timeline
- **Phase 4:** AST-aware analysis and exportable reports

## Intended stack

Python + GitPython + standard-library AST parsing + FastAPI + React + D3.js.
