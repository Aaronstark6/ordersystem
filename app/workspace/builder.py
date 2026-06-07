from dataclasses import asdict
from uuid import uuid4

from app.document_model.model import DocumentModel
from app.document_model.nodes import SectionNode
from app.workspace.builders.choice_builder import build_workspace_choice
from app.workspace.builders.condition_builder import build_workspace_condition
from app.workspace.builders.field_builder import build_workspace_field
from app.workspace.builders.image_builder import build_workspace_image
from app.workspace.builders.table_builder import build_workspace_table
from app.workspace.model import (
    WorkspaceSection,
    WorkspaceSnapshot,
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
            section.fields.append(build_workspace_field(field_node))
            continue

        table_node = document_model.tables.get(child_node_id)
        if table_node is not None:
            section.tables.append(build_workspace_table(table_node))
            continue

        image_node = document_model.images.get(child_node_id)
        if image_node is not None:
            section.images.append(build_workspace_image(image_node))
            continue

        choice_node = document_model.choices.get(child_node_id)
        if choice_node is not None:
            section.choices.append(build_workspace_choice(choice_node))

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
        workspace.unsectioned_fields.append(build_workspace_field(field_node))

    for table_node in document_model.tables.values():
        if table_node.node_id in assigned_table_ids:
            continue
        workspace.unsectioned_tables.append(build_workspace_table(table_node))

    for image_node in document_model.images.values():
        if image_node.node_id in assigned_image_ids:
            continue
        workspace.unsectioned_images.append(build_workspace_image(image_node))

    for choice_node in document_model.choices.values():
        if choice_node.node_id in assigned_choice_ids:
            continue
        workspace.unsectioned_choices.append(build_workspace_choice(choice_node))

    for condition_node in document_model.conditions.values():
        workspace.conditions.append(
            build_workspace_condition(condition_node)
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
