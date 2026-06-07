from dataclasses import asdict

from app.document_model.nodes import TableNode
from app.workspace.model import WorkspaceTable


def build_workspace_table(table_node: TableNode) -> WorkspaceTable:
    coordinate = (
        asdict(table_node.coordinate)
        if table_node.coordinate is not None
        else {}
    )
    return WorkspaceTable(
        table_key=table_node.table_key,
        label=table_node.label,
        node_id=table_node.node_id,
        headers=list(table_node.headers),
        row_count=table_node.row_count,
        column_count=table_node.column_count,
        coordinate=coordinate,
        metadata=dict(table_node.metadata),
    )
