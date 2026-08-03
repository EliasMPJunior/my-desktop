import sys
import traceback
from dataclasses import dataclass
from importlib import import_module
from pathlib import Path
from typing import Any, List, Optional, Tuple


@dataclass(frozen=True)
class RichRenderScenario:
    name: str
    response: Any


def run_render_command(
    root_dir: Path,
    test_name: str,
    response_class_name: Optional[str] = None,
) -> int:
    normalized_test_name: str = str(test_name or "").strip().lower()
    if normalized_test_name != "rich":
        print("Error: unsupported render test: {0}".format(test_name))
        print("Available tests:")
        print("  - rich")
        return 1

    return _run_rich_render_test(
        root_dir=root_dir,
        response_class_name=response_class_name,
    )


def _run_rich_render_test(
    root_dir: Path,
    response_class_name: Optional[str] = None,
) -> int:
    ontobdc_src_dir: Optional[Path] = _resolve_ontobdc_src_dir(root_dir)
    if ontobdc_src_dir is None:
        print("Error: could not locate the ontobdc/src directory from the provided workspace root.")
        return 1

    _ensure_python_path(ontobdc_src_dir)

    try:
        response_module = import_module("ontobdc.cli.domain.response.command")
        loader_module = import_module("ontobdc.view.adapter.loader")
        layout_module = import_module("ontobdc.view.plugin.render.rich.layout")
    except ModuleNotFoundError as exc:
        print("Error: failed to import ontobdc modules required for rich render testing.")
        print("Missing dependency: {0}".format(str(exc)))
        print("Run this command inside the same Python environment used by the ontobdc workspace.")
        return 1

    scenarios: List[RichRenderScenario] = _build_rich_scenarios(response_module)
    loader = loader_module.ResponseMessageBoxAdapterLoader()
    layout = layout_module.RichMessageBoxLayout()

    resolved_scenarios: List[Tuple[RichRenderScenario, Any]] = [
        (scenario, loader.get(scenario.response))
        for scenario in scenarios
    ]
    filtered_scenarios: List[Tuple[RichRenderScenario, Any]] = _filter_scenarios(
        resolved_scenarios=resolved_scenarios,
        response_class_name=response_class_name,
    )
    if not filtered_scenarios:
        print("Error: no rich render scenario matched the provided class name.")
        print("Available classes:")
        available_class_name: str
        for available_class_name in _list_available_class_names(resolved_scenarios):
            print("  - {0}".format(available_class_name))
        return 1

    print("")
    print("Running rich render test from: {0}".format(str(ontobdc_src_dir.parent)))

    scenario: RichRenderScenario
    adapter: Any
    for scenario, adapter in filtered_scenarios:
        response_type_name: str = type(scenario.response).__name__
        adapter_type_name: str = type(adapter).__name__

        print("")
        print("=" * 100)
        print("Scenario: {0}".format(scenario.name))
        print("Response: {0}".format(response_type_name))
        print("Adapter: {0}".format(adapter_type_name))
        print("=" * 100)
        print(adapter.render(scenario.response, layout))

    return 0


def _resolve_ontobdc_src_dir(root_dir: Path) -> Optional[Path]:
    normalized_root_dir: Path = root_dir.expanduser().resolve()
    candidates: List[Path] = [
        normalized_root_dir / "ontobdc" / "src",
        normalized_root_dir.parent / "ontobdc" / "src",
        normalized_root_dir / "src",
    ]

    candidate: Path
    for candidate in candidates:
        if (candidate / "ontobdc").is_dir():
            return candidate

    return None


def _ensure_python_path(ontobdc_src_dir: Path) -> None:
    resolved_path: str = str(ontobdc_src_dir.expanduser().resolve())
    if resolved_path not in sys.path:
        sys.path.insert(0, resolved_path)


def _build_rich_scenarios(response_module: Any) -> List[RichRenderScenario]:
    CommandResponse = response_module.CommandResponse
    HelpCommandResponse = response_module.HelpCommandResponse
    ExceptionCommandResponse = response_module.ExceptionCommandResponse
    ListCommandResponse = response_module.ListCommandResponse
    WelcomeCommandResponse = response_module.WelcomeCommandResponse

    return [
        RichRenderScenario(
            name="command_response_nested_content",
            response=CommandResponse(
                title="Container Metadata Ready",
                description="The container metadata was synchronized successfully.",
                content={
                    "container_id": "urn:ontobdc:storage/local/my-desktop/pregao",
                    "summary": {
                        "resource_count": 3,
                        "last_sync": "2026-07-31T10:22:00Z",
                        "health": "ok",
                    },
                    "resources": [
                        {
                            "name": "weblink.xlsx",
                            "path": "payload/document/weblink.xlsx",
                            "status": "ready",
                        },
                        {
                            "name": "datapackage.json",
                            "path": ".__ontobdc__/datapackage.json",
                            "status": "updated",
                        },
                    ],
                },
            ),
        ),
        RichRenderScenario(
            name="help_command_response",
            response=HelpCommandResponse(
                title="OntoBDC Help",
                description="Available commands for the current runtime.",
                content={
                    "init": {
                        "usage": "ontobdc init",
                        "description": "Initialize OntoBDC in the current directory.",
                    },
                    "context entity": {
                        "usage": "ontobdc context --container <container_id> --entity <entity>",
                        "description": "List entity instances in the selected container.",
                    },
                },
            ),
        ),
        RichRenderScenario(
            name="list_command_response",
            response=ListCommandResponse(
                title="Registered Containers",
                description="Containers available in the local workspace.",
                content=[
                    {
                        "repository": "pregao",
                        "id": "urn:ontobdc:storage/local/my-desktop/pregao",
                        "status": "ready",
                    },
                    {
                        "repository": "licitacao",
                        "id": "urn:ontobdc:storage/local/my-desktop/licitacao",
                        "status": "indexed",
                    },
                ],
            ),
        ),
        RichRenderScenario(
            name="welcome_command_response",
            response=WelcomeCommandResponse(
                title="InfoBIM Welcome",
                description="Display the welcome experience for the local engineering workspace.",
                content={
                    "project": "Pregao",
                    "workstreams": 4,
                    "latest_activity": "Indexed technical note TN-042.",
                },
            ),
        ),
        RichRenderScenario(
            name="exception_without_traceback",
            response=ExceptionCommandResponse(
                title="OntoBDC Run",
                description="Command execution failed.",
                content={
                    "error": "The selected container is missing a required datapackage resource.",
                },
            ),
        ),
        RichRenderScenario(
            name="exception_with_traceback",
            response=ExceptionCommandResponse(
                title="OntoBDC Run",
                description="Command execution failed.",
                content={
                    "error": "The selected container is missing a required datapackage resource.",
                    "traceback": _build_mock_traceback(),
                },
            ),
        ),
    ]


def _build_mock_traceback() -> str:
    try:
        _raise_mock_runtime_error()
    except RuntimeError:
        return traceback.format_exc().strip()

    return ""


def _raise_mock_runtime_error() -> None:
    raise RuntimeError("Mocked response trace for rich renderer validation.")


def _filter_scenarios(
    resolved_scenarios: List[Tuple[RichRenderScenario, Any]],
    response_class_name: Optional[str],
) -> List[Tuple[RichRenderScenario, Any]]:
    normalized_filter: str = str(response_class_name or "").strip().lower()
    if normalized_filter == "":
        return resolved_scenarios

    scenario: RichRenderScenario
    adapter: Any
    filtered_scenarios: List[Tuple[RichRenderScenario, Any]] = []
    for scenario, adapter in resolved_scenarios:
        response_type_name: str = type(scenario.response).__name__.lower()
        adapter_type_name: str = type(adapter).__name__.lower()
        scenario_name: str = scenario.name.lower()

        if normalized_filter in [response_type_name, adapter_type_name, scenario_name]:
            filtered_scenarios.append((scenario, adapter))

    return filtered_scenarios


def _list_available_class_names(
    resolved_scenarios: List[Tuple[RichRenderScenario, Any]],
) -> List[str]:
    class_names: List[str] = []
    scenario: RichRenderScenario
    adapter: Any

    for scenario, adapter in resolved_scenarios:
        candidate_class_name: str
        for candidate_class_name in [
            type(scenario.response).__name__,
            type(adapter).__name__,
            scenario.name,
        ]:
            if candidate_class_name in class_names:
                continue
            class_names.append(candidate_class_name)

    class_names.sort()
    return class_names
