
from dataclasses import dataclass
from typing import ClassVar, Dict
from urllib.parse import quote


@dataclass(frozen=True)
class WorkStreamContext:
    """Build the portable identity contract for a WorkStream view."""

    work_stream_id: str

    _NAMESPACE: ClassVar[str] = "urn:ontobdc:workstream"

    def __post_init__(self) -> None:
        normalized = str(self.work_stream_id).strip()
        if not normalized:
            raise ValueError("work_stream_id must not be empty")
        object.__setattr__(self, "work_stream_id", normalized)

    @property
    def encoded_id(self) -> str:
        return quote(self.work_stream_id, safe="")

    @property
    def work_stream_uri(self) -> str:
        return f"{self._NAMESPACE}/{self.encoded_id}"

    @property
    def dimension_base_uri(self) -> str:
        return f"{self.work_stream_uri}/dimension"

    @property
    def resource_relationship_namespace(self) -> str:
        return "urn:ontobdc:linkset:workstream-resource"

    def dimension_uri(self, dimension: str) -> str:
        normalized = str(dimension).strip().lower().replace("_", "-")
        if not normalized:
            raise ValueError("dimension must not be empty")
        return f"{self.dimension_base_uri}/{quote(normalized, safe='-')}"

    def as_payload(self) -> Dict[str, object]:
        return {
            "workStreamId": self.work_stream_id,
            "workStreamUri": self.work_stream_uri,
            "dimensionBaseUri": self.dimension_base_uri,
            "resourceRelationshipNamespace": (
                self.resource_relationship_namespace
            ),
        }
