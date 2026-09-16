# Interpreting Results

Code Forensics turns Git history into evidence about how a repository changed.

## Signals

- **Commit history** shows when activity happened and how frequently the repository changed.
- **Contributor data** shows who authored visible changes in the analyzed history.
- **Hotspots** identify files that changed often.
- **AST counts** provide a lightweight view of Python functions and classes.

## What a hotspot means

A frequently changed file is a signal for attention, not proof of a defect. A central module, an actively developed feature, or a file undergoing a planned refactor can all create high change frequency.

## Use context

Compare hotspots with commit messages, the surrounding timeline, and the repository's architecture. The tool should help a developer ask better questions rather than label code as good or bad automatically.

## Future signals

Line churn, refactor-versus-fix classification, architecture milestones, and interactive timelines can add context while keeping the evidence-first approach.
