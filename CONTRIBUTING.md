# Contributing to Code Forensics

Code Forensics examines repository history to produce explainable signals about how a codebase evolved.

## Development flow

1. Create a focused branch for one change.
2. Keep analysis deterministic and make assumptions explicit.
3. Add tests for parsing, metrics, edge cases, and report formatting when behavior changes.
4. Run the test suite locally before opening a pull request.
5. Document how the change was verified.

## Interpretation principle

Metrics such as commit frequency, churn, or file-change concentration are signals, not proof of a defect or a developer's quality. Prefer explainable evidence over unsupported conclusions.

## Pull requests

Useful contributions include parser robustness, additional tests, report improvements, documentation, and support for more Git history shapes. Keep each pull request focused and reviewable.
