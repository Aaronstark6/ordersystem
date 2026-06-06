from dataclasses import dataclass, field
from typing import Any, Dict, List

from app.contracts.template_analysis_result import SheetInfo


@dataclass
class MergedCellCandidate:
    sheet_name: str
    range_ref: str
    min_row: int
    max_row: int
    min_col: int
    max_col: int
    metadata: Dict[str, Any] = field(default_factory=dict)


def detect_merged_cells(sheets: List[SheetInfo]) -> List[MergedCellCandidate]:
    candidates: List[MergedCellCandidate] = []

    for sheet in sheets:
        for merged_range in sheet.merged_ranges:
            candidates.append(
                MergedCellCandidate(
                    sheet_name=merged_range.sheet_name,
                    range_ref=merged_range.range_ref,
                    min_row=merged_range.min_row,
                    max_row=merged_range.max_row,
                    min_col=merged_range.min_col,
                    max_col=merged_range.max_col,
                )
            )

    return candidates
