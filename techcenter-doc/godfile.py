#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import unquote, urlparse

METADATA_DIRECTORY = ".__ontobdc__"
RO_CRATE_FILENAME = "ro-crate-metadata.json"
CONTAINER_ONTOLOGY_FILENAME = "container.ttl"
PROJECT_ROOT_ENVIRONMENT_VARIABLE = "INFOBIM_PROJECT_ROOT"
PROV_AT_LOCATION_URI = "http://www.w3.org/ns/prov#atLocation"

_AT_LOCATION_PATTERN = re.compile(
    rf"(?:prov:atLocation|<{re.escape(PROV_AT_LOCATION_URI)}>)\s+"
    r"(?:<(?P<uri>[^>]+)>|\"(?P<literal>(?:\\.|[^\"])*)\")",
    re.IGNORECASE | re.MULTILINE,
)


class ProjectInformationError(RuntimeError):
    """Raised when generated project information cannot be resolved."""


def resolve_project_root(default_root: Path) -> Path:
    configured_root = os.environ.get(PROJECT_ROOT_ENVIRONMENT_VARIABLE)
    root = Path(configured_root).expanduser() if configured_root else default_root
    return root.resolve()


def count_indexed_files(default_root: Path) -> int:
    """Count file resources indexed by the project's RO-Crate metadata."""
    project_root = resolve_project_root(default_root)
    crate_file = _required_metadata_file(project_root, RO_CRATE_FILENAME)

    try:
        crate_data = json.loads(crate_file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ProjectInformationError(
            f"Não foi possível ler o RO-Crate: {crate_file}"
        ) from exc

    graph = crate_data.get("@graph")
    if not isinstance(graph, list):
        raise ProjectInformationError(
            f"RO-Crate sem @graph válido: {crate_file}"
        )

    entities = [entity for entity in graph if isinstance(entity, dict)]
    root_dataset = next(
        (entity for entity in entities if entity.get("@id") in {"./", "."}),
        None,
    )

    if root_dataset is not None:
        part_ids = set(_reference_ids(root_dataset.get("hasPart")))
        indexed_parts = {
            resource_id
            for resource_id in part_ids
            if _is_local_file_identifier(resource_id)
        }
        if indexed_parts:
            return len(indexed_parts)

    indexed_entities = {
        str(entity.get("@id", "")).strip()
        for entity in entities
        if _is_file_entity(entity)
    }
    return len(indexed_entities)


def project_path_from_ontology(default_root: Path) -> str:
    """Read the project path from prov:atLocation in container.ttl."""
    project_root = resolve_project_root(default_root)
    ontology_file = _required_metadata_file(
        project_root,
        CONTAINER_ONTOLOGY_FILENAME,
    )

    try:
        ontology_text = ontology_file.read_text(encoding="utf-8")
    except OSError as exc:
        raise ProjectInformationError(
            f"Não foi possível ler a ontologia: {ontology_file}"
        ) from exc

    match = _AT_LOCATION_PATTERN.search(ontology_text)
    if match is None:
        raise ProjectInformationError(
            f"prov:atLocation não encontrado em {ontology_file}"
        )

    raw_location = match.group("uri") or _decode_turtle_literal(
        match.group("literal") or ""
    )
    if not raw_location:
        raise ProjectInformationError(
            f"prov:atLocation vazio em {ontology_file}"
        )

    return _display_path(raw_location)


def _required_metadata_file(project_root: Path, filename: str) -> Path:
    metadata_file = project_root / METADATA_DIRECTORY / filename
    if metadata_file.is_file():
        return metadata_file

    raise ProjectInformationError(
        f"Metadado não encontrado: {metadata_file}. "
        f"Defina {PROJECT_ROOT_ENVIRONMENT_VARIABLE} para a raiz do projeto, "
        "quando necessário."
    )


def _reference_ids(raw_value: Any) -> Iterable[str]:
    values = raw_value if isinstance(raw_value, list) else [raw_value]
    for value in values:
        if isinstance(value, dict):
            resource_id = value.get("@id")
        else:
            resource_id = value
        if isinstance(resource_id, str) and resource_id.strip():
            yield resource_id.strip()


def _entity_types(entity: dict[str, Any]) -> set[str]:
    raw_types = entity.get("@type")
    values = raw_types if isinstance(raw_types, list) else [raw_types]
    return {
        str(value).rsplit("/", 1)[-1].rsplit("#", 1)[-1].lower()
        for value in values
        if value
    }


def _is_file_entity(entity: dict[str, Any]) -> bool:
    resource_id = str(entity.get("@id", "")).strip()
    if not _is_local_file_identifier(resource_id):
        return False

    entity_types = _entity_types(entity)
    file_types = {
        "file",
        "mediaobject",
        "digitaldocument",
        "textdigitaldocument",
        "spreadsheetdigitaldocument",
        "presentationdigitaldocument",
        "imageobject",
        "audioobject",
        "videoobject",
        "softwaresourcecode",
    }
    if entity_types.intersection(file_types):
        return True

    return bool(Path(urlparse(resource_id).path).suffix)


def _is_local_file_identifier(resource_id: str) -> bool:
    normalized = resource_id.strip()
    if normalized in {
        "",
        ".",
        "./",
        RO_CRATE_FILENAME,
        f"./{RO_CRATE_FILENAME}",
    }:
        return False
    if normalized.startswith("#") or normalized.endswith("/"):
        return False

    parsed = urlparse(normalized)
    if parsed.scheme in {"http", "https", "urn", "mailto"}:
        return False
    return True


def _decode_turtle_literal(value: str) -> str:
    return value.replace(r"\"", '"').replace(r"\\", "\\")


def _display_path(raw_location: str) -> str:
    parsed = urlparse(raw_location)
    if parsed.scheme.lower() != "file":
        return unquote(raw_location)

    decoded_path = unquote(parsed.path)
    if parsed.netloc:
        return f"//{parsed.netloc}{decoded_path}"

    if re.match(r"^/[A-Za-z]:/", decoded_path):
        return decoded_path[1:].replace("/", "\\")

    return decoded_path or raw_location
