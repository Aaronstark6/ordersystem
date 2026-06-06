from dataclasses import asdict

from app.workspace.model import WorkspaceSnapshot


def workspace_snapshot_to_dict(workspace: WorkspaceSnapshot) -> dict:
    return asdict(workspace)
