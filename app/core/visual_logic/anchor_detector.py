from dataclasses import dataclass, field
from typing import Any, Dict

from app.document_model.coordinates import Coordinate


@dataclass
class AnchorCandidate:
    anchor_key: str
    label: str
    coordinate: Coordinate
    metadata: Dict[str, Any] = field(default_factory=dict)


def build_anchor_candidate(
    anchor_key: str,
    label: str,
    coordinate: Coordinate,
    metadata: Dict[str, Any] | None = None,
) -> AnchorCandidate:
    return AnchorCandidate(
        anchor_key=anchor_key,
        label=label,
        coordinate=coordinate,
        metadata=dict(metadata or {}),
    )
