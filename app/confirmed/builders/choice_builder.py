from app.confirmed.model import ConfirmedChoice
from app.workspace.model import WorkspaceChoice


def build_confirmed_choice(
    workspace_choice: WorkspaceChoice,
    user_values: dict[str, object],
) -> ConfirmedChoice:
    has_user_value = workspace_choice.choice_key in user_values
    user_value = user_values.get(
        workspace_choice.choice_key,
        workspace_choice.value,
    )
    positional_choice_modes = {
        "checkbox_group",
        "radio_group",
        "multiselect",
    }
    final_selected_values = list(workspace_choice.selected_values)
    if (
        has_user_value
        and workspace_choice.choice_mode in positional_choice_modes
        and isinstance(user_value, list)
    ):
        final_selected_values = list(user_value)

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
        choice_mode=workspace_choice.choice_mode or "value",
        option_details=[
            dict(option_detail)
            for option_detail in workspace_choice.option_details
        ],
        selected_values=list(workspace_choice.selected_values),
        final_selected_values=final_selected_values,
    )
