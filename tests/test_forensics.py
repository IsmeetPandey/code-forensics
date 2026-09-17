import subprocess
from pathlib import Path

from forensics import python_metrics, run


def test_python_metrics_counts_async_functions(tmp_path: Path):
    source = tmp_path / 'sample.py'
    source.write_text('class A:\n    async def go(self):\n        pass\n\ndef f():\n    pass\n', encoding='utf-8')
    assert python_metrics(source) == (2, 1, 2)


def test_run_reports_git_errors(tmp_path: Path):
    try:
        run(tmp_path, 'status')
    except RuntimeError as exc:
        assert 'git command failed' in str(exc)
    else:
        raise AssertionError('expected git failure')
