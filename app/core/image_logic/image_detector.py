from dataclasses import dataclass, field
from typing import Any, Dict, List

from app.contracts.template_analysis_result import CellInfo, SheetInfo
from app.core.image_logic.image_patterns import (
    contains_image_keyword,
    infer_image_role,
    normalize_image_text,
)
from app.document_model.coordinates import Coordinate


@dataclass
class ImageAreaCandidate:
    area_key: str
    coordinate: Coordinate
    image_role: str = "placeholder"
    label: str = ""
    confidence: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)

    @property
    def image_key(self) -> str:
        return self.area_key


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


def _image_area_key(cell: CellInfo, index: int) -> str:
    label_key = "".join(
        char.lower() if char.isalnum() else "_"
        for char in str(cell.value or "").strip()
    ).strip("_")
    while "__" in label_key:
        label_key = label_key.replace("__", "_")
    return label_key or f"image_area_{index}"


def _cell_coordinate(cell: CellInfo) -> Coordinate:
    return Coordinate(
        document_type="excel",
        sheet_name=cell.sheet_name,
        cell=cell.cell,
        row=cell.row,
        column=cell.column,
    )


def _detect_image_cell(cell: CellInfo, index: int) -> ImageAreaCandidate | None:
    if cell.value is None or not contains_image_keyword(cell.value):
        return None

    label = str(cell.value).strip()
    return build_image_area_candidate(
        area_key=_image_area_key(cell, index),
        coordinate=_cell_coordinate(cell),
        image_role=infer_image_role(label),
        label=label,
        confidence=0.7,
        metadata={
            "source": "image_placeholder_text",
            "matched_text": normalize_image_text(label),
        },
    )


def detect_images(sheets: List[SheetInfo]) -> List[ImageAreaCandidate]:
    candidates: list[ImageAreaCandidate] = []

    for sheet in sheets:
        for cell in sheet.cells:
            candidate = _detect_image_cell(cell, len(candidates) + 1)
            if candidate is not None:
                candidates.append(candidate)

    return candidates
