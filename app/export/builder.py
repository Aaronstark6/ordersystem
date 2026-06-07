from uuid import uuid4

from app.confirmed.model import ConfirmedOrderObject
from app.export.model import ExportStrategy
from app.export.operations.table_operation import build_table_operation
from app.export.operations.value_operation import build_value_operation


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
            strategy.operations.append(build_value_operation(field))
        for table in section.tables:
            strategy.operations.append(build_table_operation(table))

    for field in confirmed_order.unsectioned_fields:
        strategy.operations.append(build_value_operation(field))

    for table in confirmed_order.unsectioned_tables:
        strategy.operations.append(build_table_operation(table))

    if strategy.operation_count() == 0:
        strategy.warnings.append(
            "导出策略（ExportStrategy）没有生成任何导出操作（ExportOperation）"
        )

    return strategy
