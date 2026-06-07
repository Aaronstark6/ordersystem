from dataclasses import asdict

from app.document_model.nodes import ImageNode
from app.workspace.model import WorkspaceImage


def build_workspace_image(image_node: ImageNode) -> WorkspaceImage:
    coordinate = (
        asdict(image_node.coordinate)
        if image_node.coordinate is not None
        else {}
    )
    return WorkspaceImage(
        image_key=image_node.image_key,
        label=image_node.label,
        node_id=image_node.node_id,
        image_role=image_node.image_role,
        coordinate=coordinate,
        metadata=dict(image_node.metadata),
    )
