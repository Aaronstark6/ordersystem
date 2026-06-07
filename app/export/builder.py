from uuid import uuid4

from app.confirmed.model import ConfirmedOrderObject
from app.export.model import ExportStrategy
from app.export.operations.choice_operation import build_choice_operation
from app.export.operations.image_operation import build_image_operation
from app.export.operations.table_operation import build_table_operation
from app.export.operations.value_operation import build_value_operation
from app.export.policies.condition_policy import build_condition_policy


def _build_condition_values(
    confirmed_order: ConfirmedOrderObject,
) -> dict[str, object]:
    values: dict[str, object] = {}

    fields = list(confirmed_order.unsectioned_fields)
    choices = list(confirmed_order.unsectioned_choices)
    for section in confirmed_order.sections:
        fields.extend(section.fields)
        choices.extend(section.choices)

    for field in fields:
        values[field.field_key] = field.final_value
        values[field.node_id] = field.final_value

    for choice in choices:
        choice_value: object = choice.final_value
        if choice.choice_mode in {
            "checkbox_group",
            "radio_group",
            "multiselect",
        }:
            choice_value = list(choice.final_selected_values)
        values[choice.choice_key] = choice_value
        values[choice.node_id] = choice_value

    return values


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

    conditions = list(confirmed_order.conditions)
    for section in confirmed_order.sections:
        conditions.extend(section.conditions)
    condition_policy = build_condition_policy(
        conditions,
        values=_build_condition_values(confirmed_order),
    )
    strategy.warnings.extend(condition_policy.warnings)

    for section in confirmed_order.sections:
        if condition_policy.should_skip_export(section.node_id):
            continue
        for field in section.fields:
            if not condition_policy.should_skip_export(field.node_id):
                strategy.operations.append(build_value_operation(field))
        for table in section.tables:
            if not condition_policy.should_skip_export(table.node_id):
                strategy.operations.append(build_table_operation(table))
        for image in section.images:
            if not condition_policy.should_skip_export(image.node_id):
                strategy.operations.append(build_image_operation(image))
        for choice in section.choices:
            if not condition_policy.should_skip_export(choice.node_id):
                strategy.operations.append(build_choice_operation(choice))

    for field in confirmed_order.unsectioned_fields:
        if not condition_policy.should_skip_export(field.node_id):
            strategy.operations.append(build_value_operation(field))

    for table in confirmed_order.unsectioned_tables:
        if not condition_policy.should_skip_export(table.node_id):
            strategy.operations.append(build_table_operation(table))

    for image in confirmed_order.unsectioned_images:
        if not condition_policy.should_skip_export(image.node_id):
            strategy.operations.append(build_image_operation(image))

    for choice in confirmed_order.unsectioned_choices:
        if not condition_policy.should_skip_export(choice.node_id):
            strategy.operations.append(build_choice_operation(choice))

    if strategy.operation_count() == 0:
        strategy.warnings.append(
            "导出策略（ExportStrategy）没有生成任何导出操作（ExportOperation）"
        )

    return strategy
