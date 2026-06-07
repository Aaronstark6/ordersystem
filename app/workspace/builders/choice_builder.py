from dataclasses import asdict

from app.document_model.nodes import ChoiceNode
from app.workspace.model import WorkspaceChoice


def build_workspace_choice(choice_node: ChoiceNode) -> WorkspaceChoice:
    coordinate = (
        asdict(choice_node.coordinate)
        if choice_node.coordinate is not None
        else {}
    )
    return WorkspaceChoice(
        choice_key=choice_node.choice_key,
        label=choice_node.label,
        node_id=choice_node.node_id,
        options=list(choice_node.options),
        allow_multiple=choice_node.allow_multiple,
        default_option=choice_node.default_option,
        value=choice_node.default_option or "",
        coordinate=coordinate,
        metadata=dict(choice_node.metadata),
    )
