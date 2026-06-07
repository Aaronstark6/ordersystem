from app.confirmed.model import ConfirmedTable
from app.workspace.model import WorkspaceTable


def build_confirmed_table(workspace_table: WorkspaceTable) -> ConfirmedTable:
    return ConfirmedTable(
        table_key=workspace_table.table_key,
        label=workspace_table.label,
        node_id=workspace_table.node_id,
        headers=list(workspace_table.headers),
        row_count=workspace_table.row_count,
        column_count=workspace_table.column_count,
        confirmed=True,
        coordinate=dict(workspace_table.coordinate),
        metadata=dict(workspace_table.metadata),
    )
