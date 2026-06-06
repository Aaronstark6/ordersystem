from dataclasses import dataclass, field
from typing import Any, Dict

from app.document_model.coordinates import Coordinate


@dataclass
class VisualRegionCandidate:
    region_key: str
    label: str
    region_type: str
    coordinate: Coordinate
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class LayoutRegionCandidate:
    layout_key: str
    label: str
    coordinate: Coordinate
    metadata: Dict[str, Any] = field(default_factory=dict)


def build_visual_region_candidate(
    region_key: str,
    label: str,
    region_type: str,
    coordinate: Coordinate,
    metadata: Dict[str, Any] | None = None,
) -> VisualRegionCandidate:
    return VisualRegionCandidate(
        region_key=region_key,
        label=label,
        region_type=region_type,
        coordinate=coordinate,
        metadata=dict(metadata or {}),
    )


def build_layout_region_candidate(
    layout_key: str,
    label: str,
    coordinate: Coordinate,
    metadata: Dict[str, Any] | None = None,
) -> LayoutRegionCandidate:
    return LayoutRegionCandidate(
        layout_key=layout_key,
        label=label,
        coordinate=coordinate,
        metadata=dict(metadata or {}),
    )
