from dataclasses import dataclass, field
from typing import Any, Dict, List

from app.contracts.template_analysis_result import SheetInfo


@dataclass
class TableHeaderCandidate:
    sheet_name: str
    row: int
    min_col: int
    max_col: int
    headers: List[str] = field(default_factory=list)
    confidence: float = 0.0
    reason: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)


def detect_table_headers(sheets: List[SheetInfo]) -> List[TableHeaderCandidate]:
    candidates: List[TableHeaderCandidate] = []

    for sheet in sheets:
        text_cells_by_row: dict[int, list] = {}

        for cell in sheet.cells:
            if not isinstance(cell.value, str) or not cell.value.strip():
                continue
            text_cells_by_row.setdefault(cell.row, []).append(cell)

        for row_index, row_cells in text_cells_by_row.items():
            if len(row_cells) < 3:
                continue

            sorted_cells = sorted(row_cells, key=lambda item: item.column)
            columns = [cell.column for cell in sorted_cells]

            candidates.append(
                TableHeaderCandidate(
                    sheet_name=sheet.sheet_name,
                    row=row_index,
                    min_col=min(columns),
                    max_col=max(columns),
                    headers=[cell.value.strip() for cell in sorted_cells],
                    confidence=0.65,
                    reason="同一行存在三个以上非空文本单元格",
                )
            )

    return candidates
