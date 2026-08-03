import argparse
import os
from typing import List, Optional, Type

from ontobdc.cli.adapter.context import CliContextAdapter
from ontobdc.cli.domain.port.command import CliCommandPort
from ontobdc.cli.domain.request.command import CliCommandRequest

from ontobdc_dev.branch.plugin.command.base import DevBranchCommand
from ontobdc_dev.branch.plugin.command.changelog import DevBranchChangelogCommand
from ontobdc_dev.branch.plugin.command.checkout import DevBranchCheckoutCommand
from ontobdc_dev.branch.plugin.command.commit import DevCommitCommand
from ontobdc_dev.branch.plugin.command.create import DevBranchCreateCommand


def build_parser() -> argparse.ArgumentParser:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="ontobdc-dev",
        description="Developer CLI utilities for OntoBDC workspaces.",
    )
    parser.add_argument(
        "--root-dir",
        dest="root_dir",
        default=None,
        help="Workspace root directory. Defaults to the current OntoBDC project root.",
    )

    subparsers = parser.add_subparsers(dest="command")

    branch_parser: argparse.ArgumentParser = subparsers.add_parser(
        "branch",
        help="List branch status or run branch operations across repositories.",
    )
    branch_group = branch_parser.add_mutually_exclusive_group()
    branch_group.add_argument(
        "--create",
        dest="create_branch_name",
        metavar="BRANCH_NAME",
        help="Create a branch across repositories.",
    )
    branch_group.add_argument(
        "--checkout",
        dest="checkout_branch_name",
        metavar="BRANCH_NAME",
        help="Checkout a branch across repositories.",
    )
    branch_group.add_argument(
        "--pull",
        dest="pull_branch_name",
        nargs="?",
        const="",
        metavar="BRANCH_NAME",
        help="Fetch and pull a branch across repositories.",
    )
    branch_group.add_argument(
        "--changelog",
        dest="changelog_target",
        nargs="?",
        const="HEAD",
        metavar="TARGET_REF",
        help="Generate a changelog scaffold across repositories.",
    )

    commit_parser: argparse.ArgumentParser = subparsers.add_parser(
        "commit",
        help="Commit and push changes across repositories.",
    )
    commit_parser.add_argument(
        "message",
        help="Commit message to be used across repositories.",
    )

    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser: argparse.ArgumentParser = build_parser()
    args: argparse.Namespace = parser.parse_args(argv)

    if isinstance(args.root_dir, str) and args.root_dir.strip() != "":
        os.environ["ONTOBDC_PROJECT_ROOT"] = args.root_dir

    if args.command is None:
        parser.print_help()
        return 0

    if args.command == "branch":
        if args.create_branch_name is not None:
            return _run_command(
                command_class=DevBranchCreateCommand,
                command_args=["branch", "--create", args.create_branch_name],
            )

        if args.checkout_branch_name is not None:
            return _run_command(
                command_class=DevBranchCheckoutCommand,
                command_args=["branch", "--checkout", args.checkout_branch_name],
            )

        if args.changelog_target is not None:
            changelog_args: List[str] = ["branch", "--changelog"]
            if args.changelog_target != "":
                changelog_args.append(args.changelog_target)
            return _run_command(
                command_class=DevBranchChangelogCommand,
                command_args=changelog_args,
            )

        if args.pull_branch_name is not None:
            parser.error("The 'branch --pull' command is not ported yet.")

        return _run_command(
            command_class=DevBranchCommand,
            command_args=["branch"],
        )

    if args.command == "commit":
        return _run_command(
            command_class=DevCommitCommand,
            command_args=["commit", args.message],
        )

    parser.error(f"Unsupported command: {args.command}")


def _run_command(command_class: Type[CliCommandPort], command_args: List[str]) -> int:
    request: CliCommandRequest = CliCommandRequest(
        logical_component=command_class.METADATA.logical_component,
        component_action=command_class.METADATA.id,
        command_args=command_args,
        context=CliContextAdapter(command_args),
    )
    command: CliCommandPort = command_class(request)
    if not command.check():
        raise ValueError(f"Invalid command arguments: {command_args}")

    command.run()
    return 0
