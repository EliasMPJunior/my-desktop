import os
from pathlib import Path
from typing import List, Optional


DEFAULT_REPOSITORY_DIRS: List[str] = [
    "ontobdc-wip",
    "ontobdc-core",
    "wip",
]


def resolve_workspace_root(start_path: Optional[str] = None) -> Path:
    current_path: Path = Path(start_path or os.getcwd()).resolve()
    search_path: Path = current_path if current_path.is_dir() else current_path.parent

    for candidate in [search_path] + list(search_path.parents):
        if (candidate / ".gitmodules").exists():
            return candidate

    for candidate in [search_path] + list(search_path.parents):
        if (candidate / ".git").exists():
            return candidate

    return search_path


def is_git_repository(path: Path) -> bool:
    return (path / ".git").is_dir() or (path / ".git").is_file()


def discover_repositories(root_dir: Path) -> List[Path]:
    repositories: List[Path] = []
    gitmodules_path: Path = root_dir / ".gitmodules"

    if gitmodules_path.exists():
        with gitmodules_path.open("r", encoding="utf-8") as file_handle:
            for line in file_handle:
                if "path =" not in line:
                    continue
                relative_path: str = line.split("=", 1)[1].strip()
                repositories.append(root_dir / relative_path)

    for directory_name in DEFAULT_REPOSITORY_DIRS:
        repositories.append(root_dir / directory_name)

    repositories.append(root_dir)

    unique_repositories: List[Path] = []
    seen_paths: List[str] = []
    for repository in repositories:
        normalized_path: str = str(repository.resolve())
        if normalized_path in seen_paths:
            continue
        seen_paths.append(normalized_path)
        if is_git_repository(repository):
            unique_repositories.append(repository)

    return unique_repositories
