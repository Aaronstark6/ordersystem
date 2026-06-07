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
class WorkspaceTable:
    table_key: str
    label: str
    node_id: str
    headers: List[str] = field(default_factory=list)
    row_count: int | None = None
    column_count: int | None = None
    coordinate: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class WorkspaceImage:
    image_key: str
    label: str
    node_id: str
    image_role: str = "attachment"
    coordinate: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class WorkspaceChoice:
    choice_key: str
    label: str
    node_id: str
    options: List[str] = field(default_factory=list)
    allow_multiple: bool = False
    default_option: str | None = None
    value: Any = ""
    coordinate: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class WorkspaceCondition:
    condition_key: str
    label: str
    node_id: str
    expression: str = ""
    controls_node_ids: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class WorkspaceSection:
    section_key: str
    title: str
    node_id: str
    fields: List[WorkspaceField] = field(default_factory=list)
    tables: List[WorkspaceTable] = field(default_factory=list)
    images: List[WorkspaceImage] = field(default_factory=list)
    choices: List[WorkspaceChoice] = field(default_factory=list)
    conditions: List[WorkspaceCondition] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class WorkspaceSnapshot:
    workspace_id: str
    document_id: str
    template_id: str
    sections: List[WorkspaceSection] = field(default_factory=list)
    unsectioned_fields: List[WorkspaceField] = field(default_factory=list)
    unsectioned_tables: List[WorkspaceTable] = field(default_factory=list)
    unsectioned_images: List[WorkspaceImage] = field(default_factory=list)
    unsectioned_choices: List[WorkspaceChoice] = field(default_factory=list)
    conditions: List[WorkspaceCondition] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)

    def field_count(self) -> int:
        section_field_count = sum(len(section.fields) for section in self.sections)
        return section_field_count + len(self.unsectioned_fields)
