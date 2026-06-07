from app.confirmed.model import ConfirmedField
from app.workspace.model import WorkspaceField


def build_confirmed_field(
    workspace_field: WorkspaceField,
    user_values: dict[str, object],
) -> ConfirmedField:
    user_value = user_values.get(workspace_field.field_key, workspace_field.value)
    return ConfirmedField(
        field_key=workspace_field.field_key,
        label=workspace_field.label,
        node_id=workspace_field.node_id,
        original_value=workspace_field.value,
        user_value=user_value,
        final_value=user_value,
        confirmed=True,
        coordinate=workspace_field.coordinate,
        metadata=workspace_field.metadata,
    )
