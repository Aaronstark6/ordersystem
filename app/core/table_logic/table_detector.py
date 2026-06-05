from typing import List

from openpyxl.utils import get_column_letter

from app.contracts.template_analysis_result import SheetInfo, TableCandidate


def _text(value: object) -> str:
    if value is None:
        return ""
    return str(value).strip()


def detect_tables(sheets: List[SheetInfo]) -> List[TableCandidate]:
    tables: List[TableCandidate] = []

    for sheet in sheets:
        cells_by_row: dict[int, list] = {}
        for cell in sheet.cells:
            if _text(cell.value):
                cells_by_row.setdefault(cell.row, []).append(cell)

        for row_index, row_cells in cells_by_row.items():
            sorted_cells = sorted(row_cells, key=lambda item: item.column)
            text_cells = [cell for cell in sorted_cells if _text(cell.value)]

            if len(text_cells) < 3:
                continue

            columns = [cell.column for cell in text_cells]
            if max(columns) - min(columns) + 1 > len(columns) + 2:
                continue

            headers = [_text(cell.value) for cell in text_cells]
            min_col = min(columns)
            max_col = max(columns)
            min_row = row_index
            max_row = min(sheet.max_row, row_index + 10)
            range_ref = f"{get_column_letter(min_col)}{min_row}:{get_column_letter(max_col)}{max_row}"

            tables.append(
                TableCandidate(
                    sheet_name=sheet.sheet_name,
                    range_ref=range_ref,
                    header_row=row_index,
                    min_row=min_row,
                    max_row=max_row,
                    min_col=min_col,
                    max_col=max_col,
                    headers=headers,
                    confidence=0.65,
                    reason="同一行存在多个连续文本单元格，暂定为表头候选",
                )
            )

    return tables
