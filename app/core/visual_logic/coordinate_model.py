from dataclasses import dataclass, field
from typing import Any, Dict, List

from app.document_model.coordinates import Coordinate


@dataclass
class CoordinateGroup:
    group_key: str
    coordinates: List[Coordinate] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


def excel_cell_to_coordinate(sheet_name: str, cell: str, row: int, column: int) -> Coordinate:
    return Coordinate(
        document_type="excel",
        sheet_name=sheet_name,
        cell=cell,
        row=row,
        column=column,
    )
