from dataclasses import dataclass, field
from typing import Dict, List

from app.document_model.nodes import (
    ChoiceNode,
    ConditionNode,
    FieldNode,
    ImageNode,
    SectionNode,
    TableNode,
)
from app.document_model.relationships import Relationship


@dataclass
class ValidationIssue:
    level: str
    code: str
    message: str
    node_id: str = ""


@dataclass
class DocumentModel:
    document_id: str
    template_id: str
    document_type: str
    fields: Dict[str, FieldNode] = field(default_factory=dict)
    tables: Dict[str, TableNode] = field(default_factory=dict)
    images: Dict[str, ImageNode] = field(default_factory=dict)
    choices: Dict[str, ChoiceNode] = field(default_factory=dict)
    conditions: Dict[str, ConditionNode] = field(default_factory=dict)
    sections: Dict[str, SectionNode] = field(default_factory=dict)
    relationships: List[Relationship] = field(default_factory=list)
    validation_issues: List[ValidationIssue] = field(default_factory=list)

    def node_count(self) -> int:
        return (
            len(self.fields)
            + len(self.tables)
            + len(self.images)
            + len(self.choices)
            + len(self.conditions)
            + len(self.sections)
        )
