from dataclasses import asdict
from typing import Any
from uuid import uuid4

from app.document_model.model import DocumentModel
from app.document_model.nodes import (
    ChoiceNode,
    ConditionNode,
    FieldNode,
    ImageNode,
    SectionNode,
    TableNode,
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


def _coordinate_to_dict(node: Any) -> dict:
    if node.coordinate is None:
        return {}
    return asdict(node.coordinate)


def _build_workspace_field(field_node: FieldNode) -> WorkspaceField:
    return WorkspaceField(
        field_key=field_node.field_key,
        label=field_node.label,
        node_id=field_node.node_id,
        value="",
        required=field_node.required,
        editable=True,
        coordinate=_coordinate_to_dict(field_node),
        metadata={
            "normalized_name": field_node.normalized_name,
            "value_type": field_node.value_type,
        },
    )


def _build_workspace_table(table_node: TableNode) -> WorkspaceTable:
    return WorkspaceTable(
        table_key=table_node.table_key,
        label=table_node.label,
        node_id=table_node.node_id,
        headers=list(table_node.headers),
        row_count=table_node.row_count,
        column_count=table_node.column_count,
        coordinate=_coordinate_to_dict(table_node),
        metadata=dict(table_node.metadata),
    )


def _build_workspace_image(image_node: ImageNode) -> WorkspaceImage:
    return WorkspaceImage(
        image_key=image_node.image_key,
        label=image_node.label,
        node_id=image_node.node_id,
        image_role=image_node.image_role,
        coordinate=_coordinate_to_dict(image_node),
        metadata=dict(image_node.metadata),
    )


def _build_workspace_choice(choice_node: ChoiceNode) -> WorkspaceChoice:
    return WorkspaceChoice(
        choice_key=choice_node.choice_key,
        label=choice_node.label,
        node_id=choice_node.node_id,
        options=list(choice_node.options),
        allow_multiple=choice_node.allow_multiple,
        default_option=choice_node.default_option,
        value=choice_node.default_option or "",
        coordinate=_coordinate_to_dict(choice_node),
        metadata=dict(choice_node.metadata),
    )


def _build_workspace_condition(
    condition_node: ConditionNode,
) -> WorkspaceCondition:
    return WorkspaceCondition(
        condition_key=condition_node.condition_key,
        label=condition_node.label,
        node_id=condition_node.node_id,
        expression=condition_node.expression,
        controls_node_ids=list(condition_node.controls_node_ids),
        metadata=dict(condition_node.metadata),
    )


def _build_workspace_section(
    section_node: SectionNode,
    document_model: DocumentModel,
) -> WorkspaceSection:
    section = WorkspaceSection(
        section_key=section_node.section_key,
        title=section_node.label,
        node_id=section_node.node_id,
        metadata={
            "coordinate": asdict(section_node.coordinate) if section_node.coordinate else {},
        },
    )

    for child_node_id in section_node.child_node_ids:
        field_node = document_model.fields.get(child_node_id)
        if field_node is not None:
            section.fields.append(_build_workspace_field(field_node))
            continue

        table_node = document_model.tables.get(child_node_id)
        if table_node is not None:
            section.tables.append(_build_workspace_table(table_node))
            continue

        image_node = document_model.images.get(child_node_id)
        if image_node is not None:
            section.images.append(_build_workspace_image(image_node))
            continue

        choice_node = document_model.choices.get(child_node_id)
        if choice_node is not None:
            section.choices.append(_build_workspace_choice(choice_node))

    return section


def build_workspace_snapshot(document_model: DocumentModel) -> WorkspaceSnapshot:
    workspace = WorkspaceSnapshot(
        workspace_id=str(uuid4()),
        document_id=document_model.document_id,
        template_id=document_model.template_id,
    )

    assigned_field_ids: set[str] = set()
    assigned_table_ids: set[str] = set()
    assigned_image_ids: set[str] = set()
    assigned_choice_ids: set[str] = set()

    for section_node in document_model.sections.values():
        section = _build_workspace_section(section_node, document_model)
        for field in section.fields:
            assigned_field_ids.add(field.node_id)
        for table in section.tables:
            assigned_table_ids.add(table.node_id)
        for image in section.images:
            assigned_image_ids.add(image.node_id)
        for choice in section.choices:
            assigned_choice_ids.add(choice.node_id)
        workspace.sections.append(section)

    for field_node in document_model.fields.values():
        if field_node.node_id in assigned_field_ids:
            continue
        workspace.unsectioned_fields.append(_build_workspace_field(field_node))

    for table_node in document_model.tables.values():
        if table_node.node_id in assigned_table_ids:
            continue
        workspace.unsectioned_tables.append(_build_workspace_table(table_node))

    for image_node in document_model.images.values():
        if image_node.node_id in assigned_image_ids:
            continue
        workspace.unsectioned_images.append(_build_workspace_image(image_node))

    for choice_node in document_model.choices.values():
        if choice_node.node_id in assigned_choice_ids:
            continue
        workspace.unsectioned_choices.append(_build_workspace_choice(choice_node))

    for condition_node in document_model.conditions.values():
        workspace.conditions.append(
            _build_workspace_condition(condition_node)
        )

    content_count = (
        workspace.field_count()
        + sum(len(section.tables) for section in workspace.sections)
        + sum(len(section.images) for section in workspace.sections)
        + sum(len(section.choices) for section in workspace.sections)
        + len(workspace.unsectioned_tables)
        + len(workspace.unsectioned_images)
        + len(workspace.unsectioned_choices)
        + len(workspace.conditions)
    )
    if content_count == 0:
        workspace.warnings.append("工作区没有生成任何可确认内容")

    return workspace
