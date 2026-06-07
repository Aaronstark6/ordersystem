from uuid import uuid4

from app.confirmed.model import (
    ConfirmedChoice,
    ConfirmedCondition,
    ConfirmedField,
    ConfirmedImage,
    ConfirmedOrderObject,
    ConfirmedSection,
    ConfirmedTable,
    utc_now_iso,
)
from app.workspace.model import (
    WorkspaceChoice,
    WorkspaceCondition,
    WorkspaceField,
    WorkspaceImage,
    WorkspaceSection,
    WorkspaceSnapshot,
    WorkspaceTable,
)


def _build_confirmed_field(
    workspace_field: WorkspaceField,
    user_values: dict[str, object],
) -> ConfirmedField:
    user_value = user_values.get(workspace_field.field_key, workspace_field.value)
    final_value = user_value

    return ConfirmedField(
        field_key=workspace_field.field_key,
        label=workspace_field.label,
        node_id=workspace_field.node_id,
        original_value=workspace_field.value,
        user_value=user_value,
        final_value=final_value,
        confirmed=True,
        coordinate=workspace_field.coordinate,
        metadata=workspace_field.metadata,
    )


def _build_confirmed_table(workspace_table: WorkspaceTable) -> ConfirmedTable:
    return ConfirmedTable(
        table_key=workspace_table.table_key,
        label=workspace_table.label,
        node_id=workspace_table.node_id,
        headers=list(workspace_table.headers),
        row_count=workspace_table.row_count,
        column_count=workspace_table.column_count,
        confirmed=True,
        coordinate=dict(workspace_table.coordinate),
        metadata=dict(workspace_table.metadata),
    )


def _build_confirmed_image(workspace_image: WorkspaceImage) -> ConfirmedImage:
    return ConfirmedImage(
        image_key=workspace_image.image_key,
        label=workspace_image.label,
        node_id=workspace_image.node_id,
        image_role=workspace_image.image_role,
        confirmed=True,
        coordinate=dict(workspace_image.coordinate),
        metadata=dict(workspace_image.metadata),
    )


def _build_confirmed_choice(
    workspace_choice: WorkspaceChoice,
    user_values: dict[str, object],
) -> ConfirmedChoice:
    user_value = user_values.get(
        workspace_choice.choice_key,
        workspace_choice.value,
    )
    return ConfirmedChoice(
        choice_key=workspace_choice.choice_key,
        label=workspace_choice.label,
        node_id=workspace_choice.node_id,
        options=list(workspace_choice.options),
        allow_multiple=workspace_choice.allow_multiple,
        default_option=workspace_choice.default_option,
        original_value=workspace_choice.value,
        user_value=user_value,
        final_value=user_value,
        confirmed=True,
        coordinate=dict(workspace_choice.coordinate),
        metadata=dict(workspace_choice.metadata),
    )


def _build_confirmed_condition(
    workspace_condition: WorkspaceCondition,
) -> ConfirmedCondition:
    return ConfirmedCondition(
        condition_key=workspace_condition.condition_key,
        label=workspace_condition.label,
        node_id=workspace_condition.node_id,
        expression=workspace_condition.expression,
        controls_node_ids=list(workspace_condition.controls_node_ids),
        confirmed=True,
        metadata=dict(workspace_condition.metadata),
    )


def _build_confirmed_section(
    workspace_section: WorkspaceSection,
    user_values: dict[str, object],
) -> ConfirmedSection:
    section = ConfirmedSection(
        section_key=workspace_section.section_key,
        title=workspace_section.title,
        node_id=workspace_section.node_id,
        metadata=workspace_section.metadata,
    )

    for workspace_field in workspace_section.fields:
        section.fields.append(_build_confirmed_field(workspace_field, user_values))

    for workspace_table in workspace_section.tables:
        section.tables.append(_build_confirmed_table(workspace_table))

    for workspace_image in workspace_section.images:
        section.images.append(_build_confirmed_image(workspace_image))

    for workspace_choice in workspace_section.choices:
        section.choices.append(
            _build_confirmed_choice(workspace_choice, user_values)
        )

    for workspace_condition in workspace_section.conditions:
        section.conditions.append(
            _build_confirmed_condition(workspace_condition)
        )

    return section


def build_confirmed_order_object(
    workspace: WorkspaceSnapshot,
    user_values: dict[str, object] | None = None,
) -> ConfirmedOrderObject:
    values = user_values or {}

    confirmed_order = ConfirmedOrderObject(
        confirmed_order_id=str(uuid4()),
        workspace_id=workspace.workspace_id,
        document_id=workspace.document_id,
        template_id=workspace.template_id,
        confirmed_at=utc_now_iso(),
    )

    for workspace_section in workspace.sections:
        confirmed_order.sections.append(
            _build_confirmed_section(workspace_section, values)
        )

    for workspace_field in workspace.unsectioned_fields:
        confirmed_order.unsectioned_fields.append(
            _build_confirmed_field(workspace_field, values)
        )

    for workspace_table in workspace.unsectioned_tables:
        confirmed_order.unsectioned_tables.append(
            _build_confirmed_table(workspace_table)
        )

    for workspace_image in workspace.unsectioned_images:
        confirmed_order.unsectioned_images.append(
            _build_confirmed_image(workspace_image)
        )

    for workspace_choice in workspace.unsectioned_choices:
        confirmed_order.unsectioned_choices.append(
            _build_confirmed_choice(workspace_choice, values)
        )

    for workspace_condition in workspace.conditions:
        confirmed_order.conditions.append(
            _build_confirmed_condition(workspace_condition)
        )

    if confirmed_order.total_object_count() == 0:
        confirmed_order.warnings.append(
            "人工确认对象（ConfirmedOrderObject）没有任何可确认对象"
        )

    return confirmed_order
