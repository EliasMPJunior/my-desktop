from pathlib import Path
from typing import List

from ontobdc_dev.git import git_run, git_stdout
from ontobdc_dev.workspace import discover_repositories


def run_commit_command(root_dir: Path, message: str) -> int:
    repositories: List[Path] = discover_repositories(root_dir)
    has_error: bool = False

    print("")
    print("Starting commit process...")
    print("Root Directory: {0}".format(str(root_dir)))
    print("Message: \"{0}\"".format(message))

    for repository in repositories:
        repository_name: str = repository.name
        branch_name: str = _get_current_branch(repository)

        print("")
        print("> Processing {0} ({1})".format(repository_name, branch_name))

        add_result = git_run(repository, ["add", "."])
        if add_result.returncode != 0:
            print("  - failed to add changes")
            has_error = True
            continue

        print("  - added all changes")

        has_changes: bool = _has_repository_changes(repository)
        if not has_changes:
            print("  - no changes to commit")
            continue

        commit_result = git_run(repository, ["commit", "-m", message])
        if commit_result.returncode != 0:
            print("  - failed to commit changes")
            has_error = True
            continue

        print("  - committed changes")

        remotes_output: str = git_stdout(repository, ["remote"])
        if remotes_output == "":
            print("  - no remote repository found")
            continue

        push_result = git_run(repository, ["push"])
        if push_result.returncode == 0:
            print("  - pushed to remote")
            continue

        upstream_result = git_run(
            repository,
            ["push", "--set-upstream", "origin", branch_name],
        )
        if upstream_result.returncode != 0:
            print("  - failed to push changes")
            has_error = True
            continue

        print("  - pushed to remote with upstream")

    print("")
    print("Commit process finished.")

    return 1 if has_error else 0


def _get_current_branch(repository: Path) -> str:
    branch_name: str = git_stdout(repository, ["branch", "--show-current"])
    if branch_name != "":
        return branch_name

    branch_name = git_stdout(repository, ["rev-parse", "--abbrev-ref", "HEAD"])
    if branch_name != "":
        return branch_name

    return "unknown"


def _has_repository_changes(repository: Path) -> bool:
    status_result = git_run(repository, ["status", "--porcelain=v1"])
    return status_result.stdout.strip() != ""
