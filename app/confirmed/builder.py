from uuid import uuid4

from app.confirmed.builders.choice_builder import build_confirmed_choice
from app.confirmed.builders.condition_builder import build_confirmed_condition
from app.confirmed.builders.field_builder import build_confirmed_field
from app.confirmed.builders.image_builder import build_confirmed_image
from app.confirmed.builders.table_builder import build_confirmed_table
from app.confirmed.model import (
    ConfirmedOrderObject,
    ConfirmedSection,
    utc_now_iso,
)
from app.workspace.model import (
    WorkspaceSection,
    WorkspaceSnapshot,
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
        section.fields.append(build_confirmed_field(workspace_field, user_values))

    for workspace_table in workspace_section.tables:
        section.tables.append(build_confirmed_table(workspace_table))

    for workspace_image in workspace_section.images:
        section.images.append(build_confirmed_image(workspace_image))

    for workspace_choice in workspace_section.choices:
        section.choices.append(
            build_confirmed_choice(workspace_choice, user_values)
        )

    for workspace_condition in workspace_section.conditions:
        section.conditions.append(
            build_confirmed_condition(workspace_condition)
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
            build_confirmed_field(workspace_field, values)
        )

    for workspace_table in workspace.unsectioned_tables:
        confirmed_order.unsectioned_tables.append(
            build_confirmed_table(workspace_table)
        )

    for workspace_image in workspace.unsectioned_images:
        confirmed_order.unsectioned_images.append(
            build_confirmed_image(workspace_image)
        )

    for workspace_choice in workspace.unsectioned_choices:
        confirmed_order.unsectioned_choices.append(
            build_confirmed_choice(workspace_choice, values)
        )

    for workspace_condition in workspace.conditions:
        confirmed_order.conditions.append(
            build_confirmed_condition(workspace_condition)
        )

    if confirmed_order.total_object_count() == 0:
        confirmed_order.warnings.append(
            "人工确认对象（ConfirmedOrderObject）没有任何可确认对象"
        )

    return confirmed_order
