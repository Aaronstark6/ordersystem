from dataclasses import dataclass, field
from typing import Any, Dict

from app.document_model.coordinates import Coordinate


@dataclass
class ImageAreaCandidate:
    area_key: str
    coordinate: Coordinate
    image_role: str = "placeholder"
    label: str = ""
    confidence: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)


def build_image_area_candidate(
    area_key: str,
    coordinate: Coordinate,
    image_role: str = "placeholder",
    label: str = "",
    confidence: float = 0.0,
    metadata: Dict[str, Any] | None = None,
) -> ImageAreaCandidate:
    return ImageAreaCandidate(
        area_key=area_key,
        coordinate=coordinate,
        image_role=image_role,
        label=label,
        confidence=confidence,
        metadata=dict(metadata or {}),
    )
