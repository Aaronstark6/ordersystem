from app.confirmed.model import ConfirmedChoice
from app.workspace.model import WorkspaceChoice


def build_confirmed_choice(
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
