from app.document_model.nodes import ConditionNode
from app.workspace.model import WorkspaceCondition


def build_workspace_condition(
    condition_node: ConditionNode,
) -> WorkspaceCondition:
    return WorkspaceCondition(
        condition_key=condition_node.condition_key,
        label=condition_node.label,
        node_id=condition_node.node_id,
        expression=condition_node.expression,
        controls_node_ids=list(condition_node.controls_node_ids),
        metadata=dict(condition_node.metadata),
    )
