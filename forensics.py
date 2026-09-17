from __future__ import annotations

import argparse
import ast
import json
import subprocess
from collections import Counter
from pathlib import Path


def run(repo: Path, *args: str) -> str:
    try:
        process = subprocess.run(
            ['git', '-C', str(repo), *args],
            capture_output=True,
            text=True,
            timeout=20,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise RuntimeError(f'git command failed: {exc}') from exc
    if process.returncode:
        raise RuntimeError(process.stderr.strip() or 'git command failed')
    return process.stdout


def python_metrics(path: Path) -> tuple[int, int, int]:
    try:
        tree = ast.parse(path.read_text(encoding='utf-8'))
    except (OSError, SyntaxError, UnicodeDecodeError):
        return (0, 0, 0)
    return (
        sum(isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) for node in ast.walk(tree)),
        sum(isinstance(node, ast.ClassDef) for node in ast.walk(tree)),
        len(tree.body),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description='Inspect how a Git repository evolved.')
    parser.add_argument('repo', type=Path)
    args = parser.parse_args()
    repo = args.repo.expanduser().resolve()
    if not (repo / '.git').is_dir():
        raise SystemExit(f'Not a Git repository: {repo}')

    commits = run(repo, 'rev-list', '--count', 'HEAD').strip()
    log = run(repo, 'log', '--format=%H%x09%an%x09%ad%x09%s', '--date=short').splitlines()
    churn = Counter()
    for line in run(repo, 'log', '--name-only', '--format=').splitlines():
        name = line.strip()
        if name:
            churn[name] += 1

    py = []
    for path in repo.rglob('*.py'):
        if '.git' in path.parts:
            continue
        functions, classes, _ = python_metrics(path)
        py.append({'file': str(path.relative_to(repo)), 'functions': functions, 'classes': classes})

    result = {
        'repository': str(repo),
        'commit_count': int(commits or 0),
        'authors': sorted({parts[1] for line in log if len(parts := line.split('\t', 3)) > 1}),
        'recent_commits': [line.split('\t', 3) for line in log[:20]],
        'hotspots': churn.most_common(20),
        'python_ast': py[:100],
    }
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
