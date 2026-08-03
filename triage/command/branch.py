from pathlib import Path
from typing import Dict, List, Optional

from ontobdc_dev.git import git_run, git_stdout, git_succeeds
from ontobdc_dev.workspace import discover_repositories


def run_branch_command(
    root_dir: Path,
    create_branch_name: Optional[str] = None,
    checkout_branch_name: Optional[str] = None,
    pull_branch_name: Optional[str] = None,
    changelog_target: Optional[str] = None,
) -> int:
    repositories: List[Path] = discover_repositories(root_dir)

    if create_branch_name is not None:
        return _run_branch_create(repositories, create_branch_name)
    if checkout_branch_name is not None:
        return _run_branch_checkout(repositories, checkout_branch_name)
    if pull_branch_name is not None:
        return _run_branch_pull(repositories, pull_branch_name)
    if changelog_target is not None:
        return _run_branch_changelog(repositories, changelog_target)
    return _run_branch_status(repositories, root_dir)


def _run_branch_status(repositories: List[Path], root_dir: Path) -> int:
    for repository in repositories:
        repository_name: str = repository.name
        branch_name: str = _get_current_branch(repository)
        files: List[Dict[str, str]] = _list_status_files(repository, root_dir)

        print("")
        print("> {0} ({1})".format(repository_name, branch_name))
        if not files:
            print("  - clean")
            continue

        for file_data in files:
            print("  - [{0}] {1}".format(file_data["state"], file_data["file"]))

    return 0


def _run_branch_create(repositories: List[Path], branch_name: str) -> int:
    has_error: bool = False

    for repository in repositories:
        repository_name: str = repository.name
        print("")
        print("> Processing {0}".format(repository_name))

        branch_exists: bool = git_succeeds(
            repository,
            ["show-ref", "--verify", "--quiet", "refs/heads/{0}".format(branch_name)],
        )
        if branch_exists:
            print("  - branch '{0}' already exists".format(branch_name))
            continue

        create_result = git_run(repository, ["checkout", "-b", branch_name])
        if create_result.returncode != 0:
            print("  - failed to create branch")
            has_error = True
            continue

        print("  - created local branch")

        remotes_output: str = git_stdout(repository, ["remote"])
        if remotes_output == "":
            print("  - no remote repository found")
            continue

        push_result = git_run(repository, ["push", "--set-upstream", "origin", branch_name])
        if push_result.returncode != 0:
            print("  - failed to push upstream")
            has_error = True
            continue

        print("  - pushed upstream")

    return 1 if has_error else 0


def _run_branch_checkout(repositories: List[Path], branch_name: str) -> int:
    has_error: bool = False

    for repository in repositories:
        repository_name: str = repository.name
        print("")
        print("> Processing {0}".format(repository_name))

        has_local_branch: bool = git_succeeds(
            repository,
            ["show-ref", "--verify", "--quiet", "refs/heads/{0}".format(branch_name)],
        )
        has_remote_branch: bool = git_succeeds(
            repository,
            ["show-ref", "--verify", "--quiet", "refs/remotes/origin/{0}".format(branch_name)],
        )

        if not has_local_branch and not has_remote_branch:
            print("  - branch '{0}' does not exist in this repository".format(branch_name))
            continue

        checkout_result = git_run(repository, ["checkout", branch_name])
        if checkout_result.returncode != 0:
            print("  - failed to checkout branch")
            has_error = True
            continue

        print("  - checked out")

    return 1 if has_error else 0


def _run_branch_pull(repositories: List[Path], branch_name: Optional[str]) -> int:
    has_error: bool = False

    print("")
    print("Fetching repositories...")
    for repository in repositories:
        repository_name: str = repository.name
        print("")
        print("> Fetching {0}".format(repository_name))

        fetch_result = git_run(repository, ["fetch", "--all"])
        if fetch_result.returncode != 0:
            print("  - failed to fetch repository")
            has_error = True
            continue

        print("  - fetched successfully")

    print("")
    print("Pulling repositories...")
    for repository in repositories:
        repository_name: str = repository.name
        target_branch_name: str = branch_name or _get_current_branch(repository)
        print("")
        print("> Pulling {0}".format(repository_name))

        if target_branch_name == "unknown":
            print("  - failed to resolve current branch")
            has_error = True
            continue

        remotes_output: str = git_stdout(repository, ["remote"])
        if remotes_output == "":
            print("  - no remote repository found")
            has_error = True
            continue

        print("  - target branch: {0}".format(target_branch_name))

        pull_result = git_run(repository, ["pull", "origin", target_branch_name])
        if pull_result.returncode != 0:
            print("  - failed to pull branch '{0}'".format(target_branch_name))
            has_error = True
            continue

        print("  - pulled successfully")

    return 1 if has_error else 0


def _run_branch_changelog(repositories: List[Path], target_ref: Optional[str]) -> int:
    normalized_target_ref: str = target_ref or "HEAD"

    for repository in repositories:
        repository_name: str = repository.name
        print("")
        print("> Processing {0}".format(repository_name))
        print(
            "  - changelog feature is not ported yet for target '{0}'".format(
                normalized_target_ref
            )
        )

    return 0


def _get_current_branch(repository: Path) -> str:
    branch_name: str = git_stdout(repository, ["branch", "--show-current"])
    if branch_name != "":
        return branch_name

    branch_name = git_stdout(repository, ["rev-parse", "--abbrev-ref", "HEAD"])
    if branch_name != "":
        return branch_name

    return "unknown"


def _list_status_files(repository: Path, root_dir: Path) -> List[Dict[str, str]]:
    status_result = git_run(repository, ["status", "--porcelain=v1"])
    files: List[Dict[str, str]] = []

    for line in status_result.stdout.splitlines():
        if line == "":
            continue

        status_code: str = line[:2]
        file_path: str = line[3:]

        if repository == root_dir and file_path in ["ontobdc-wip", "ontobdc-core", "wip"]:
            continue

        files.append(
            {
                "file": file_path,
                "state": _detect_file_state(status_code),
            }
        )

    return files


def _detect_file_state(status_code: str) -> str:
    if "??" in status_code:
        return "untracked"
    if "A" in status_code:
        return "added"
    if "D" in status_code:
        return "deleted"
    return "modified"
