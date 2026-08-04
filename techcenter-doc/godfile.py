#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any, Iterable, Iterator
from urllib.parse import unquote, urlparse

METADATA_DIRECTORY = ".__ontobdc__"
RO_CRATE_FILENAME = "ro-crate-metadata.json"
CONTAINER_ONTOLOGY_FILENAME = "container.ttl"
PROJECT_ROOT_ENVIRONMENT_VARIABLE = "INFOBIM_PROJECT_ROOT"
PROV_AT_LOCATION_URI = "http://www.w3.org/ns/prov#atLocation"
IFC_REF_LATITUDE_LOCAL_NAME = "refLatitude_IfcSite"
IFC_REF_LONGITUDE_LOCAL_NAME = "refLongitude_IfcSite"

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


def project_coordinates_from_ifc(default_root: Path) -> dict[str, float] | None:
    """Resolve WGS84 coordinates from IfcSite.RefLatitude/RefLongitude."""
    project_root = resolve_project_root(default_root)
    ontology_files = tuple(_project_ontology_files(project_root))
    if not ontology_files:
        return None

    for ontology_file in ontology_files:
        coordinates = _coordinates_from_ifc_ontology(ontology_file)
        if coordinates is not None:
            return coordinates

    return None


def _project_ontology_files(project_root: Path) -> Iterator[Path]:
    for ontology_file in sorted(project_root.rglob("project.ttl")):
        if ontology_file.parent.name != "__infobim__":
            continue
        if ontology_file.parent.parent.name != METADATA_DIRECTORY:
            continue
        if ontology_file.is_file():
            yield ontology_file


def _coordinates_from_ifc_ontology(
    ontology_file: Path,
) -> dict[str, float] | None:
    try:
        from rdflib import Graph
    except ImportError as exc:
        raise ProjectInformationError(
            "rdflib é necessário para ler IfcSite.RefLatitude/RefLongitude."
        ) from exc

    graph = Graph()
    try:
        graph.parse(ontology_file, format="turtle")
    except Exception as exc:
        raise ProjectInformationError(
            f"Não foi possível ler as coordenadas IFC em {ontology_file}"
        ) from exc

    for site, latitude_node in _subject_objects_by_predicate_name(
        graph,
        IFC_REF_LATITUDE_LOCAL_NAME,
    ):
        longitude_node = _first_object_by_predicate_name(
            graph,
            site,
            IFC_REF_LONGITUDE_LOCAL_NAME,
        )
        if longitude_node is None:
            continue

        latitude = _compound_plane_angle_to_decimal(graph, latitude_node)
        longitude = _compound_plane_angle_to_decimal(graph, longitude_node)
        if latitude is None or longitude is None:
            continue
        if not -90 <= latitude <= 90:
            continue
        if not -180 <= longitude <= 180:
            continue

        return {
            "latitude": latitude,
            "longitude": longitude,
        }

    return None


def _subject_objects_by_predicate_name(
    graph: Any,
    predicate_name: str,
) -> Iterator[tuple[Any, Any]]:
    for subject, predicate, value in graph:
        if _local_name(predicate) == predicate_name:
            yield subject, value


def _first_object_by_predicate_name(
    graph: Any,
    subject: Any,
    predicate_name: str,
) -> Any | None:
    for predicate, value in graph.predicate_objects(subject):
        if _local_name(predicate) == predicate_name:
            return value
    return None


def _compound_plane_angle_to_decimal(graph: Any, node: Any) -> float | None:
    components = _compound_plane_angle_components(graph, node)
    if not components:
        return None
    if len(components) == 1:
        return components[0]

    degrees = components[0]
    sign = -1.0 if degrees < 0 else 1.0
    minutes = abs(components[1]) if len(components) > 1 else 0.0
    seconds = abs(components[2]) if len(components) > 2 else 0.0
    millionths = abs(components[3]) if len(components) > 3 else 0.0
    return sign * (
        abs(degrees)
        + minutes / 60.0
        + seconds / 3600.0
        + millionths / 3_600_000_000.0
    )


def _compound_plane_angle_components(graph: Any, node: Any) -> list[float]:
    direct_value = _numeric_value(graph, node)
    if direct_value is not None:
        return [direct_value]

    rdf_components = _rdf_collection_components(graph, node)
    if rdf_components:
        return rdf_components

    linked_components = _linked_list_components(graph, node)
    if linked_components:
        return linked_components

    return _numbers_from_lexical_value(str(node))


def _rdf_collection_components(graph: Any, node: Any) -> list[float]:
    try:
        from rdflib.namespace import RDF
    except ImportError:
        return []

    values: list[float] = []
    current = node
    visited: set[Any] = set()
    while current != RDF.nil and current not in visited:
        visited.add(current)
        item = graph.value(current, RDF.first)
        if item is None:
            return []
        numeric = _numeric_value(graph, item)
        if numeric is None:
            return []
        values.append(numeric)
        current = graph.value(current, RDF.rest)
        if current is None:
            return []
    return values


def _linked_list_components(graph: Any, node: Any) -> list[float]:
    values: list[float] = []
    current = node
    visited: set[Any] = set()
    while current is not None and current not in visited:
        visited.add(current)
        item = _first_object_by_predicate_name(graph, current, "hasContents")
        if item is None:
            break
        numeric = _numeric_value(graph, item)
        if numeric is None:
            return []
        values.append(numeric)
        current = _first_object_by_predicate_name(graph, current, "hasNext")
    return values


def _numeric_value(graph: Any, node: Any) -> float | None:
    try:
        from rdflib import Literal
    except ImportError:
        return None

    if isinstance(node, Literal):
        try:
            return float(node.toPython())
        except (TypeError, ValueError):
            numbers = _numbers_from_lexical_value(str(node))
            return numbers[0] if len(numbers) == 1 else None

    accepted_predicates = {
        "hasInteger",
        "hasDouble",
        "hasDecimal",
        "hasReal",
        "hasValue",
    }
    for predicate, value in graph.predicate_objects(node):
        if _local_name(predicate) not in accepted_predicates:
            continue
        numeric = _numeric_value(graph, value)
        if numeric is not None:
            return numeric
    return None


def _numbers_from_lexical_value(value: str) -> list[float]:
    matches = re.findall(r"[-+]?\d+(?:\.\d+)?", value)
    try:
        return [float(match) for match in matches]
    except ValueError:
        return []


def _local_name(value: Any) -> str:
    text = str(value)
    return text.rsplit("#", 1)[-1].rsplit("/", 1)[-1]


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
