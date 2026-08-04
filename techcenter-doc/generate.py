#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Callable, Dict, cast

try:
    import yaml
    from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape
    from markupsafe import Markup, escape
except ImportError as exc:
    missing = exc.name or "dependency"
    raise SystemExit(
        f"Missing {missing}. Install dependencies with: "
        "python -m pip install jinja2 pyyaml rdflib"
    ) from exc

from godfile import (
    ProjectInformationError,
    count_indexed_files,
    project_coordinates_from_ifc,
    project_path_from_ontology,
)

ROOT = Path(__file__).resolve().parent
TEMPLATE_DIR = ROOT / "template"
VIEW_FILE = ROOT / "views" / "public.yaml"
OUTPUT_FILE = ROOT / "index.html"
PROJECT_RUNTIME_DATA_FILE = (
    ROOT
    / ".__ontobdc__"
    / "asset"
    / "infobim-view"
    / "js"
    / "project_runtime_data.js"
)
WORKSTREAM_JSONLD_FILE = ROOT / "payload" / "triple" / "work_stream.jsonld"
INLINE_STRONG_PATTERN = re.compile(r"(\*\*|__)(.+?)\1")
LOCAL_VIEW_ACTION_PREFIXES = ("view/", "./view/")
MONTHS_PT_BR = (
    "",
    "janeiro",
    "fevereiro",
    "março",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro",
)


def render_inline_markup(raw_text: str) -> Markup:
    escaped_text: str = str(escape(raw_text))
    formatted_text: str = INLINE_STRONG_PATTERN.sub(r"<strong>\2</strong>", escaped_text)
    formatted_text = formatted_text.replace("\n", "<br>\n")
    return Markup(formatted_text)


def transform_view_value(raw_value: Any) -> Any:
    if isinstance(raw_value, str):
        return render_inline_markup(raw_value)
    if isinstance(raw_value, list):
        return [transform_view_value(item) for item in raw_value]
    if isinstance(raw_value, dict):
        return {
            key: transform_view_value(value)
            for key, value in raw_value.items()
        }
    return raw_value


def prepare_view_data(raw_data: Dict[str, Any]) -> Dict[str, Any]:
    return cast(Dict[str, Any], transform_view_value(raw_data))


def generation_date() -> str:
    current = datetime.now().astimezone()
    return f"{current.day} de {MONTHS_PT_BR[current.month]} de {current.year}"


def generated_project_value(
    label: str,
    resolver: Callable[[Path], Any],
) -> Any:
    try:
        return resolver(ROOT)
    except ProjectInformationError as exc:
        print(f"Warning: {label}: {exc}", file=sys.stderr)
        return "Não disponível"


def generated_project_coordinates() -> dict[str, float] | None:
    try:
        return project_coordinates_from_ifc(ROOT)
    except ProjectInformationError as exc:
        print(f"Warning: project coordinates: {exc}", file=sys.stderr)
        return None


def enrich_project_information(raw_data: Dict[str, Any]) -> None:
    project = raw_data.setdefault("project", {})
    raw_fields = project.setdefault("fields", [])
    if not isinstance(raw_fields, list):
        raise TypeError("project.fields must be a list")

    generated_labels = {"Path", "Arquivos indexados"}
    fields = [
        field
        for field in raw_fields
        if not (
            isinstance(field, dict)
            and field.get("label") in generated_labels
        )
    ]

    project_path = generated_project_value(
        "project path",
        project_path_from_ontology,
    )
    indexed_files = generated_project_value(
        "indexed files",
        count_indexed_files,
    )

    fields.extend(
        [
            {"label": "Path", "value": project_path},
            {"label": "Arquivos indexados", "value": indexed_files},
        ]
    )
    project["fields"] = fields
    project["path"] = project_path
    project["location"] = generated_project_coordinates()


def local_view_navigation_script() -> str:
    prefixes = ", ".join(repr(prefix) for prefix in LOCAL_VIEW_ACTION_PREFIXES)
    return f"""  <script>
    (function () {{
      const prefixes = [{prefixes}];
      document.querySelectorAll('.menubar-item[data-action]').forEach((button) => {{
        button.addEventListener('click', () => {{
          const action = String(button.dataset.action || '').trim();
          if (prefixes.some((prefix) => action.startsWith(prefix))) {{
            window.location.href = action;
          }}
        }});
      }});
    }}());
  </script>
"""


def inject_before_closing_body(html: str, fragment: str) -> str:
    closing_body = "</body>"
    if closing_body not in html:
        raise ValueError("Rendered dashboard does not contain a closing body tag.")
    return html.replace(closing_body, fragment + closing_body, 1)


def inject_local_view_navigation(html: str) -> str:
    return inject_before_closing_body(html, local_view_navigation_script())


def serialize_runtime_script(variable_name: str, payload: Any) -> str:
    return (
        f"window.{variable_name} = "
        + json.dumps(payload, ensure_ascii=False, indent=2)
        + ";\n"
    )


def write_runtime_script(path: Path, variable_name: str, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        serialize_runtime_script(variable_name, payload),
        encoding="utf-8",
    )


def write_project_runtime_data(location: dict[str, float] | None) -> None:
    payload = {
        "location": location,
        "locationSource": "IfcSite.RefLatitude/RefLongitude",
    }
    write_runtime_script(
        PROJECT_RUNTIME_DATA_FILE,
        "infoBimProjectRuntimeData",
        payload,
    )


def load_workstream_jsonld() -> dict[str, Any] | None:
    if not WORKSTREAM_JSONLD_FILE.is_file():
        print(
            f"Warning: workstream JSON-LD not found: {WORKSTREAM_JSONLD_FILE}",
            file=sys.stderr,
        )
        return None

    raw_value = json.loads(WORKSTREAM_JSONLD_FILE.read_text(encoding="utf-8"))
    if not isinstance(raw_value, dict):
        raise TypeError("work_stream.jsonld must contain a JSON object")
    return cast(dict[str, Any], raw_value)


def serialize_embedded_jsonld(payload: dict[str, Any] | None) -> str:
    serialized = json.dumps(payload, ensure_ascii=False, indent=2)
    return serialized.replace("</", "<\\/")


def workstream_jsonld_fragment(payload: dict[str, Any] | None) -> str:
    return (
        '  <script id="work-stream-jsonld" type="application/ld+json">\n'
        + serialize_embedded_jsonld(payload)
        + "\n  </script>\n"
        + "  <script>\n"
        + "    window.infoBimWorkStreamData = JSON.parse(\n"
        + "      document.getElementById('work-stream-jsonld').textContent\n"
        + "    );\n"
        + "  </script>\n"
    )


def inject_workstream_jsonld(
    html: str,
    payload: dict[str, Any] | None,
) -> str:
    return inject_before_closing_body(
        html,
        workstream_jsonld_fragment(payload),
    )


def main() -> int:
    if not VIEW_FILE.is_file():
        print(f"View not found: {VIEW_FILE}", file=sys.stderr)
        return 1

    raw_data: Dict[str, Any] = cast(
        Dict[str, Any],
        yaml.safe_load(VIEW_FILE.read_text(encoding="utf-8")) or {},
    )
    enrich_project_information(raw_data)
    raw_data["generation"] = {"date": generation_date()}
    data: Dict[str, Any] = prepare_view_data(raw_data)

    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        autoescape=select_autoescape(("html", "xml")),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    html = env.get_template("index.html.jinja").render(**data)
    workstream_payload = load_workstream_jsonld()
    html = inject_workstream_jsonld(html, workstream_payload)
    html = inject_local_view_navigation(html)
    OUTPUT_FILE.write_text(html.rstrip() + "\n", encoding="utf-8")

    write_project_runtime_data(raw_data["project"].get("location"))

    print(f"Generated {OUTPUT_FILE.relative_to(ROOT)} from {VIEW_FILE.relative_to(ROOT)}")
    print(
        "Embedded "
        f"{WORKSTREAM_JSONLD_FILE.relative_to(ROOT)} in {OUTPUT_FILE.relative_to(ROOT)}"
    )
    print(f"Generated {PROJECT_RUNTIME_DATA_FILE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
