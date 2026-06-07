from uuid import uuid4

from app.confirmed.model import ConfirmedField, ConfirmedOrderObject, ConfirmedTable
from app.export.model import ExportOperation, ExportStrategy


def _build_export_operation(field: ConfirmedField) -> ExportOperation:
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
        },
    )


def _build_table_export_operation(table: ConfirmedTable) -> ExportOperation:
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


def build_export_strategy(
    confirmed_order: ConfirmedOrderObject,
    document_type: str = "excel",
) -> ExportStrategy:
    strategy = ExportStrategy(
        export_strategy_id=str(uuid4()),
        confirmed_order_id=confirmed_order.confirmed_order_id,
        document_id=confirmed_order.document_id,
        template_id=confirmed_order.template_id,
        document_type=document_type,
    )

    for section in confirmed_order.sections:
        for field in section.fields:
            strategy.operations.append(_build_export_operation(field))
        for table in section.tables:
            strategy.operations.append(
                _build_table_export_operation(table)
            )

    for field in confirmed_order.unsectioned_fields:
        strategy.operations.append(_build_export_operation(field))

    for table in confirmed_order.unsectioned_tables:
        strategy.operations.append(_build_table_export_operation(table))

    if strategy.operation_count() == 0:
        strategy.warnings.append(
            "导出策略（ExportStrategy）没有生成任何导出操作（ExportOperation）"
        )

    return strategy
