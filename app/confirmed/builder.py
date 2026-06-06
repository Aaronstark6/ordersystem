from uuid import uuid4

from app.confirmed.model import (
    ConfirmedField,
    ConfirmedOrderObject,
    ConfirmedSection,
    utc_now_iso,
)
from app.workspace.model import WorkspaceField, WorkspaceSection, WorkspaceSnapshot


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

    if confirmed_order.field_count() == 0:
        confirmed_order.warnings.append(
            "人工确认对象（ConfirmedOrderObject）没有任何字段"
        )

    return confirmed_order
