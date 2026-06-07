from app.confirmed.model import ConfirmedCondition
from app.workspace.model import WorkspaceCondition


def build_confirmed_condition(
    workspace_condition: WorkspaceCondition,
) -> ConfirmedCondition:
    return ConfirmedCondition(
        condition_key=workspace_condition.condition_key,
        label=workspace_condition.label,
        node_id=workspace_condition.node_id,
        expression=workspace_condition.expression,
        controls_node_ids=list(workspace_condition.controls_node_ids),
        confirmed=True,
        metadata=dict(workspace_condition.metadata),
    )
