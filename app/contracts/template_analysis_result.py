from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class CellInfo:
    sheet_name: str
    cell: str
    row: int
    column: int
    value: Any = None
    data_type: str = ""
    is_merged: bool = False
    merged_range: Optional[str] = None
    has_style: bool = False
    number_format: Optional[str] = None


@dataclass
class MergedRangeInfo:
    sheet_name: str
    range_ref: str
    min_row: int
    min_col: int
    max_row: int
    max_col: int


@dataclass
class SheetInfo:
    sheet_name: str
    max_row: int
    max_column: int
    cells: List[CellInfo] = field(default_factory=list)
    merged_ranges: List[MergedRangeInfo] = field(default_factory=list)
    row_heights: Dict[int, float] = field(default_factory=dict)
    column_widths: Dict[str, float] = field(default_factory=dict)


@dataclass
class FieldLabelCandidate:
    sheet_name: str
    cell: str
    row: int
    column: int
    label: str
    confidence: float
    reason: str = ""


@dataclass
class TableCandidate:
    sheet_name: str
    range_ref: str
    header_row: int
    min_row: int
    max_row: int
    min_col: int
    max_col: int
    headers: List[str] = field(default_factory=list)
    confidence: float = 0.0
    reason: str = ""


@dataclass
class VisualRegionCandidate:
    sheet_name: str
    region_key: str
    min_row: int
    max_row: int
    min_col: int
    max_col: int
    region_type: str
    title: str = ""
    confidence: float = 0.0


@dataclass
class TemplateAnalysisResult:
    template_id: str
    document_type: str
    sheets: List[SheetInfo] = field(default_factory=list)
    field_labels: List[FieldLabelCandidate] = field(default_factory=list)
    tables: List[TableCandidate] = field(default_factory=list)
    visual_regions: List[VisualRegionCandidate] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    images: List[Any] = field(default_factory=list)
    conditions: List[Any] = field(default_factory=list)
    choices: List[Any] = field(default_factory=list)

    def has_errors(self) -> bool:
        return bool(self.errors)
