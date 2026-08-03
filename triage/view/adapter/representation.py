from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any

from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF


VISUAL = Namespace(
    "http://datacenter.app.br/ontology/productivity/entity/"
    "visual_representation_type/type.ttl#"
)
SCHEMA = Namespace("https://schema.org/")


class VisualRepresentationContractError(ValueError):
    """Raised when the packaged visual ontology is incomplete or invalid."""


def _required_object(graph: Graph, subject: URIRef, predicate: URIRef) -> URIRef:
    value = graph.value(subject, predicate)
    if not isinstance(value, URIRef):
        raise VisualRepresentationContractError(
            f"Missing URI value for {predicate} on {subject}."
        )
    return value


def _identifier(graph: Graph, resource: URIRef) -> str:
    value = graph.value(resource, SCHEMA.identifier)
    if not isinstance(value, Literal) or not str(value).strip():
        raise VisualRepresentationContractError(
            f"Missing schema:identifier on {resource}."
        )
    return str(value).strip()


def _optional_literal(
    graph: Graph,
    subject: URIRef,
    predicate: URIRef,
) -> str | None:
    value = graph.value(subject, predicate)
    if value is None:
        return None
    if not isinstance(value, Literal):
        raise VisualRepresentationContractError(
            f"Expected literal value for {predicate} on {subject}."
        )
    normalized = str(value).strip()
    return normalized or None


def _rule_map(
    graph: Graph,
    profile: URIRef,
    relation: URIRef,
    applies_to: URIRef,
    value_predicate: URIRef,
) -> dict[str, str]:
    values: dict[str, str] = {}
    for rule in graph.objects(profile, relation):
        if not isinstance(rule, URIRef):
            raise VisualRepresentationContractError(
                f"Expected URI rule for {relation} on {profile}."
            )
        target = _required_object(graph, rule, applies_to)
        value = _optional_literal(graph, rule, value_predicate)
        if value is None:
            raise VisualRepresentationContractError(
                f"Missing rule value for {value_predicate} on {rule}."
            )
        values[str(target)] = value
    return dict(sorted(values.items()))


@dataclass(frozen=True)
class VisualRepresentationContract:
    """Renderer-neutral visual profiles extracted from the packaged ontology."""

    profiles: dict[str, dict[str, Any]]
    schema_version: int = 1

    @classmethod
    def from_file(cls, ontology_file: Path) -> "VisualRepresentationContract":
        graph = Graph()
        graph.parse(str(ontology_file), format="turtle")

        profiles: dict[str, dict[str, Any]] = {}
        for category, profile in graph.subject_objects(
            VISUAL.hasVisualRepresentationType
        ):
            if not isinstance(category, URIRef) or not isinstance(profile, URIRef):
                continue
            if (profile, RDF.type, VISUAL.VisualRepresentationType) not in graph:
                raise VisualRepresentationContractError(
                    f"{profile} is not a VisualRepresentationType."
                )

            profiles[str(category)] = {
                "id": _identifier(graph, profile),
                "shape": _identifier(
                    graph,
                    _required_object(graph, profile, VISUAL.visualShape),
                ),
                "borderStyle": _identifier(
                    graph,
                    _required_object(graph, profile, VISUAL.borderStyle),
                ),
                "borderTone": _identifier(
                    graph,
                    _required_object(graph, profile, VISUAL.borderTone),
                ),
                "fillStyle": _identifier(
                    graph,
                    _required_object(graph, profile, VISUAL.fillStyle),
                ),
                "colorAuthority": _identifier(
                    graph,
                    _required_object(graph, profile, VISUAL.colorAuthority),
                ),
                "recommendedColorRole": _optional_literal(
                    graph,
                    profile,
                    VISUAL.recommendedColorRole,
                ),
                "issueStatusColors": _rule_map(
                    graph,
                    profile,
                    VISUAL.issueStatusColorRule,
                    VISUAL.appliesToIssueStatus,
                    VISUAL.issueStatusColorRole,
                ),
                "iconAuthority": _identifier(
                    graph,
                    _required_object(graph, profile, VISUAL.iconAuthority),
                ),
                "fixedIconName": _optional_literal(
                    graph,
                    profile,
                    VISUAL.fixedIconName,
                ),
                "recordKindIcons": _rule_map(
                    graph,
                    profile,
                    VISUAL.recordKindIconRule,
                    VISUAL.appliesToRecordKind,
                    VISUAL.recordKindIconName,
                ),
            }

        if not profiles:
            raise VisualRepresentationContractError(
                "The visual ontology contains no annotation profile bindings."
            )
        return cls(profiles=dict(sorted(profiles.items())))

    @classmethod
    def packaged(cls) -> "VisualRepresentationContract":
        ontology_file = (
            Path(__file__).resolve().parents[1]
            / "plugin"
            / "ontology"
            / "visual_representation_type.ttl"
        )
        return cls.from_file(ontology_file)

    def as_payload(self) -> dict[str, Any]:
        return {
            "schemaVersion": self.schema_version,
            "profiles": self.profiles,
        }


@lru_cache(maxsize=1)
def packaged_visual_representation_contract() -> VisualRepresentationContract:
    """Return the immutable packaged contract, parsed once per process."""

    return VisualRepresentationContract.packaged()
