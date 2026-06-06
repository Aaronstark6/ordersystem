from dataclasses import dataclass, field
from typing import Any, Dict

from app.document_model.coordinates import Coordinate


@dataclass
class ImageAnchorCandidate:
    anchor_key: str
    coordinate: Coordinate
    anchor_type: str = "cell"
    image_area_key: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)


def build_image_anchor_candidate(
    anchor_key: str,
    coordinate: Coordinate,
    anchor_type: str = "cell",
    image_area_key: str = "",
    metadata: Dict[str, Any] | None = None,
) -> ImageAnchorCandidate:
    return ImageAnchorCandidate(
        anchor_key=anchor_key,
        coordinate=coordinate,
        anchor_type=anchor_type,
        image_area_key=image_area_key,
        metadata=dict(metadata or {}),
    )
