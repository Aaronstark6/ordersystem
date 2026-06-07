from uuid import uuid4

from app.confirmed.model import ConfirmedTable
from app.export.model import ExportOperation


def build_table_operation(table: ConfirmedTable) -> ExportOperation:
    return ExportOperation(
        operation_id=str(uuid4()),
        operation_type="write_table",
        source_node_id=table.node_id,
        field_key=table.table_key,
        label=table.label,
        value={
            "headers": list(table.headers),
            "row_count": table.row_count,
            "column_count": table.column_count,
        },
        target=dict(table.coordinate),
        metadata={
            "confirmed": table.confirmed,
        },
    )
