from uuid import uuid4

from app.confirmed.model import ConfirmedField
from app.export.model import ExportOperation


def build_value_operation(field: ConfirmedField) -> ExportOperation:
    return ExportOperation(
        operation_id=str(uuid4()),
        operation_type="write_value",
        source_node_id=field.node_id,
        field_key=field.field_key,
        label=field.label,
        value=field.final_value,
        target=field.coordinate,
        metadata={
            "confirmed": field.confirmed,
            "original_value": field.original_value,
            "user_value": field.user_value,
            "field_metadata": dict(field.metadata),
        },
    )
