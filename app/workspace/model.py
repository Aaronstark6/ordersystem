from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class WorkspaceField:
    field_key: str
    label: str
    node_id: str
    value: Any = ""
    required: bool = False
    editable: bool = True
    coordinate: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class WorkspaceSection:
    section_key: str
    title: str
    node_id: str
    fields: List[WorkspaceField] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class WorkspaceSnapshot:
    workspace_id: str
    document_id: str
    template_id: str
    sections: List[WorkspaceSection] = field(default_factory=list)
    unsectioned_fields: List[WorkspaceField] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)

    def field_count(self) -> int:
        section_field_count = sum(len(section.fields) for section in self.sections)
        return section_field_count + len(self.unsectioned_fields)
