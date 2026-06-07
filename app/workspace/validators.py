from app.workspace.model import WorkspaceSnapshot


def validate_workspace_snapshot(workspace: WorkspaceSnapshot) -> list[str]:
    errors: list[str] = []

    if not workspace.workspace_id:
        errors.append("工作区快照（WorkspaceSnapshot）缺少 workspace_id")

    if not workspace.document_id:
        errors.append("工作区快照（WorkspaceSnapshot）缺少 document_id")

    if not workspace.template_id:
        errors.append("工作区快照（WorkspaceSnapshot）缺少 template_id")

    content_count = (
        workspace.field_count()
        + sum(len(section.tables) for section in workspace.sections)
        + sum(len(section.images) for section in workspace.sections)
        + sum(len(section.choices) for section in workspace.sections)
        + sum(len(section.conditions) for section in workspace.sections)
        + len(workspace.unsectioned_tables)
        + len(workspace.unsectioned_images)
        + len(workspace.unsectioned_choices)
        + len(workspace.conditions)
    )
    if content_count == 0:
        errors.append("工作区快照（WorkspaceSnapshot）没有可确认内容")

    workspace_choices = [
        choice
        for section in workspace.sections
        for choice in section.choices
    ]
    workspace_choices.extend(workspace.unsectioned_choices)

    for choice in workspace_choices:
        if not choice.choice_mode:
            errors.append(
                f"工作区选择（WorkspaceChoice）缺少 choice_mode: {choice.node_id}"
            )

        if not isinstance(choice.selected_values, list):
            errors.append(
                "工作区选择（WorkspaceChoice）selected_values 必须是 list: "
                f"{choice.node_id}"
            )

    return errors
