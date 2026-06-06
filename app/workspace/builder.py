from dataclasses import asdict
from uuid import uuid4

from app.document_model.model import DocumentModel
from app.document_model.nodes import FieldNode, SectionNode
from app.workspace.model import WorkspaceField, WorkspaceSection, WorkspaceSnapshot


def _coordinate_to_dict(field_node: FieldNode) -> dict:
    if field_node.coordinate is None:
        return {}
    return asdict(field_node.coordinate)


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
        if field_node is None:
            continue
        section.fields.append(_build_workspace_field(field_node))

    return section


def build_workspace_snapshot(document_model: DocumentModel) -> WorkspaceSnapshot:
    workspace = WorkspaceSnapshot(
        workspace_id=str(uuid4()),
        document_id=document_model.document_id,
        template_id=document_model.template_id,
    )

    assigned_field_ids: set[str] = set()

    for section_node in document_model.sections.values():
        section = _build_workspace_section(section_node, document_model)
        for field in section.fields:
            assigned_field_ids.add(field.node_id)
        workspace.sections.append(section)

    for field_node in document_model.fields.values():
        if field_node.node_id in assigned_field_ids:
            continue
        workspace.unsectioned_fields.append(_build_workspace_field(field_node))

    if workspace.field_count() == 0:
        workspace.warnings.append("工作区没有生成任何字段")

    return workspace
