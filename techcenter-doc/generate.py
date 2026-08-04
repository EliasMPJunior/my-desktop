#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Callable, Dict, List, cast

try:
    import yaml
    from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape
    from markupsafe import Markup, escape
except ImportError as exc:
    missing = exc.name or "dependency"
    raise SystemExit(
        f"Missing {missing}. Install dependencies with: "
        "python -m pip install jinja2 pyyaml"
    ) from exc

from godfile import (
    ProjectInformationError,
    count_indexed_files,
    project_path_from_ontology,
)

ROOT = Path(__file__).resolve().parent
TEMPLATE_DIR = ROOT / "template"
VIEW_FILE = ROOT / "views" / "public.yaml"
OUTPUT_FILE = ROOT / "index.html"
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
        transformed_list: List[Any] = [transform_view_value(item) for item in raw_value]
        return transformed_list

    if isinstance(raw_value, dict):
        transformed_dict: Dict[str, Any] = {
            key: transform_view_value(value)
            for key, value in raw_value.items()
        }
        return transformed_dict

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


def inject_local_view_navigation(html: str) -> str:
    closing_body = "</body>"
    if closing_body not in html:
        raise ValueError("Rendered dashboard does not contain a closing body tag.")
    return html.replace(
        closing_body,
        local_view_navigation_script() + closing_body,
        1,
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
    html = inject_local_view_navigation(html)
    OUTPUT_FILE.write_text(html.rstrip() + "\n", encoding="utf-8")
    print(f"Generated {OUTPUT_FILE.relative_to(ROOT)} from {VIEW_FILE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
