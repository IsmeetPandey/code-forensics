from __future__ import annotations
import ast
import json
import subprocess
from collections import Counter
from pathlib import Path
import argparse

def run(repo: Path, *args: str) -> str:
    p = subprocess.run(['git','-C',str(repo),*args], capture_output=True, text=True)
    if p.returncode: raise RuntimeError(p.stderr.strip() or 'git command failed')
    return p.stdout

def python_metrics(path: Path) -> tuple[int,int,int]:
    try:
        tree=ast.parse(path.read_text(encoding='utf-8'))
    except (OSError,SyntaxError,UnicodeDecodeError): return (0,0,0)
    return (sum(isinstance(n, ast.FunctionDef) for n in ast.walk(tree)), sum(isinstance(n, ast.ClassDef) for n in ast.walk(tree)), len(tree.body))

def main() -> None:
    ap=argparse.ArgumentParser(description='Inspect how a Git repository evolved.')
    ap.add_argument('repo', type=Path)
    ns=ap.parse_args(); repo=ns.repo.resolve()
    if not (repo/'.git').exists(): raise SystemExit(f'Not a Git repository: {repo}')
    commits=run(repo,'rev-list','--count','HEAD').strip()
    log=run(repo,'log','--format=%H%x09%an%x09%ad%x09%s','--date=short').splitlines()
    churn=Counter()
    for line in run(repo,'log','--name-only','--format=').splitlines():
        name=line.strip()
        if name: churn[name]+=1
    py=[]
    for p in repo.rglob('*.py'):
        if '.git' not in p.parts:
            f,c,_=python_metrics(p); py.append({'file':str(p.relative_to(repo)),'functions':f,'classes':c})
    result={'repository':str(repo),'commit_count':int(commits or 0),'authors':sorted(set(x.split('\t')[1] for x in log if '\t' in x)),'recent_commits':[x.split('\t',3) for x in log[:20]],'hotspots':churn.most_common(20),'python_ast':py[:100]}
    print(json.dumps(result,indent=2))
if __name__=='__main__': main()
