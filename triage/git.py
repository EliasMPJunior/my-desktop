import subprocess
from pathlib import Path
from typing import List


def git_stdout(cwd: Path, args: List[str]) -> str:
    result: subprocess.CompletedProcess[str] = subprocess.run(
        ["git"] + args,
        cwd=str(cwd),
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return ""
    return result.stdout.strip()


def git_succeeds(cwd: Path, args: List[str]) -> bool:
    result: subprocess.CompletedProcess[str] = subprocess.run(
        ["git"] + args,
        cwd=str(cwd),
        capture_output=True,
        text=True,
        check=False,
    )
    return result.returncode == 0


def git_run(cwd: Path, args: List[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git"] + args,
        cwd=str(cwd),
        capture_output=True,
        text=True,
        check=False,
    )
