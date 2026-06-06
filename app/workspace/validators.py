from app.workspace.model import WorkspaceSnapshot


def validate_workspace_snapshot(workspace: WorkspaceSnapshot) -> list[str]:
    errors: list[str] = []

    if not workspace.workspace_id:
        errors.append("工作区快照（WorkspaceSnapshot）缺少 workspace_id")

    if not workspace.document_id:
        errors.append("工作区快照（WorkspaceSnapshot）缺少 document_id")

    if not workspace.template_id:
        errors.append("工作区快照（WorkspaceSnapshot）缺少 template_id")

    return errors
