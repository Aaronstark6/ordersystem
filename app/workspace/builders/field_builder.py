from dataclasses import asdict

from app.document_model.nodes import FieldNode
from app.workspace.model import WorkspaceField


def build_workspace_field(field_node: FieldNode) -> WorkspaceField:
    coordinate = (
        asdict(field_node.coordinate)
        if field_node.coordinate is not None
        else {}
    )
    return WorkspaceField(
        field_key=field_node.field_key,
        label=field_node.label,
        node_id=field_node.node_id,
        value="",
        required=field_node.required,
        editable=True,
        coordinate=coordinate,
        metadata={
            **dict(field_node.metadata),
            "normalized_name": field_node.normalized_name,
            "value_type": field_node.value_type,
        },
    )
