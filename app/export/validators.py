from app.export.model import ExportStrategy


def validate_export_strategy(strategy: ExportStrategy) -> list[str]:
    errors: list[str] = []

    if not strategy.export_strategy_id:
        errors.append("导出策略（ExportStrategy）缺少 export_strategy_id")

    if not strategy.confirmed_order_id:
        errors.append("导出策略（ExportStrategy）缺少 confirmed_order_id")

    if not strategy.document_id:
        errors.append("导出策略（ExportStrategy）缺少 document_id")

    if not strategy.template_id:
        errors.append("导出策略（ExportStrategy）缺少 template_id")

    for operation in strategy.operations:
        if not operation.operation_id:
            errors.append("导出操作（ExportOperation）缺少 operation_id")

        if not operation.operation_type:
            errors.append("导出操作（ExportOperation）缺少 operation_type")

        if not operation.source_node_id:
            errors.append("导出操作（ExportOperation）缺少 source_node_id")

        if not operation.target:
            errors.append(
                f"导出操作（ExportOperation）缺少 target: {operation.field_key}"
            )

    return errors
