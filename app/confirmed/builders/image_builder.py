from app.confirmed.model import ConfirmedImage
from app.workspace.model import WorkspaceImage


def build_confirmed_image(workspace_image: WorkspaceImage) -> ConfirmedImage:
    return ConfirmedImage(
        image_key=workspace_image.image_key,
        label=workspace_image.label,
        node_id=workspace_image.node_id,
        image_role=workspace_image.image_role,
        confirmed=True,
        coordinate=dict(workspace_image.coordinate),
        metadata=dict(workspace_image.metadata),
    )
