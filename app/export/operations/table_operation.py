from uuid import uuid4

from openpyxl.utils import get_column_letter

from app.confirmed.model import ConfirmedTable
from app.export.model import ExportOperation


def _resolve_start_cell(table: ConfirmedTable) -> str:
    cell = table.coordinate.get("cell")
    if cell:
        return str(cell)

    row = table.coordinate.get("row")
    column = table.coordinate.get("column")
    if row is None or column is None:
        return ""

    return f"{get_column_letter(int(column))}{int(row)}"


def _build_table_rows(table: ConfirmedTable) -> list[list[object]]:
    headers = list(table.headers)
    if not headers:
        return []

    rows: list[list[object]] = [headers]
    data_row_count = max((table.row_count or 1) - 1, 0)
    for _ in range(data_row_count):
        rows.append(["" for _ in headers])
    return rows


def build_table_operation(table: ConfirmedTable) -> ExportOperation:
    target = dict(table.coordinate)
    target["start_cell"] = _resolve_start_cell(table)

    return ExportOperation(
        operation_id=str(uuid4()),
        operation_type="write_table",
        source_node_id=table.node_id,
        field_key=table.table_key,
        label=table.label,
        value=_build_table_rows(table),
        target=target,
        metadata={
            "confirmed": table.confirmed,
            "headers": list(table.headers),
            "row_count": table.row_count,
            "column_count": table.column_count,
            "contract": "excel_write_table_v1",
        },
    )
