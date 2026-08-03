import argparse
from typing import List, Optional

from ontobdc_dev.commands import (
    run_branch_command,
    run_commit_command,
    run_render_command,
)
from ontobdc_dev.workspace import resolve_workspace_root


def build_parser() -> argparse.ArgumentParser:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="ontobdc-dev",
        description="Developer CLI utilities for OntoBDC workspaces.",
    )
    parser.add_argument(
        "--root-dir",
        dest="root_dir",
        default=None,
        help="Workspace root directory. Defaults to the closest git workspace from the current directory.",
    )

    subparsers = parser.add_subparsers(dest="command")
    subparsers.required = True

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
        help="Fetch and pull a branch across repositories. Defaults to the current branch when omitted.",
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

    render_parser: argparse.ArgumentParser = subparsers.add_parser(
        "render",
        help="Run renderer development tests against the OntoBDC workspace.",
    )
    render_parser.add_argument(
        "--test",
        dest="render_test_name",
        required=True,
        choices=["rich"],
        metavar="TEST_NAME",
        help="Select the renderer test to run.",
    )
    render_parser.add_argument(
        "--class",
        dest="response_class_name",
        default=None,
        metavar="CLASS_NAME",
        help="Limit the render test to one response, adapter, or scenario class name.",
    )

    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser: argparse.ArgumentParser = build_parser()
    args: argparse.Namespace = parser.parse_args(argv)
    root_dir = resolve_workspace_root(args.root_dir)

    if args.command == "branch":
        return run_branch_command(
            root_dir=root_dir,
            create_branch_name=args.create_branch_name,
            checkout_branch_name=args.checkout_branch_name,
            pull_branch_name=args.pull_branch_name,
            changelog_target=args.changelog_target,
        )

    if args.command == "commit":
        return run_commit_command(
            root_dir=root_dir,
            message=args.message,
        )

    if args.command == "render":
        return run_render_command(
            root_dir=root_dir,
            test_name=args.render_test_name,
            response_class_name=args.response_class_name,
        )

    parser.error("Unsupported command.")
