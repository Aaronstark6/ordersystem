from dataclasses import dataclass
from typing import Optional


@dataclass
class Coordinate:
    document_type: str
    page_index: Optional[int] = None
    sheet_name: Optional[str] = None
    cell: Optional[str] = None
    row: Optional[int] = None
    column: Optional[int] = None
    x: Optional[float] = None
    y: Optional[float] = None
    width: Optional[float] = None
    height: Optional[float] = None
