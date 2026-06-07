from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ConfirmedField:
    field_key: str
    label: str
    node_id: str
    original_value: Any = ""
    user_value: Any = ""
    final_value: Any = ""
    confirmed: bool = True
    coordinate: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ConfirmedTable:
    table_key: str
    label: str
    node_id: str
    headers: List[str] = field(default_factory=list)
    row_count: int | None = None
    column_count: int | None = None
    confirmed: bool = True
    coordinate: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ConfirmedImage:
    image_key: str
    label: str
    node_id: str
    image_role: str = "attachment"
    confirmed: bool = True
    coordinate: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ConfirmedChoice:
    choice_key: str
    label: str
    node_id: str
    options: List[str] = field(default_factory=list)
    allow_multiple: bool = False
    default_option: str | None = None
    original_value: Any = ""
    user_value: Any = ""
    final_value: Any = ""
    confirmed: bool = True
    coordinate: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)
    choice_mode: str = "value"
    option_details: List[Dict[str, Any]] = field(default_factory=list)
    selected_values: List[Any] = field(default_factory=list)
    final_selected_values: List[Any] = field(default_factory=list)


@dataclass
class ConfirmedCondition:
    condition_key: str
    label: str
    node_id: str
    expression: str = ""
    controls_node_ids: List[str] = field(default_factory=list)
    confirmed: bool = True
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ConfirmedSection:
    section_key: str
    title: str
    node_id: str
    fields: List[ConfirmedField] = field(default_factory=list)
    tables: List[ConfirmedTable] = field(default_factory=list)
    images: List[ConfirmedImage] = field(default_factory=list)
    choices: List[ConfirmedChoice] = field(default_factory=list)
    conditions: List[ConfirmedCondition] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ConfirmedOrderObject:
    confirmed_order_id: str
    workspace_id: str
    document_id: str
    template_id: str
    confirmed_at: str
    sections: List[ConfirmedSection] = field(default_factory=list)
    unsectioned_fields: List[ConfirmedField] = field(default_factory=list)
    unsectioned_tables: List[ConfirmedTable] = field(default_factory=list)
    unsectioned_images: List[ConfirmedImage] = field(default_factory=list)
    unsectioned_choices: List[ConfirmedChoice] = field(default_factory=list)
    conditions: List[ConfirmedCondition] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)

    def field_count(self) -> int:
        section_field_count = sum(len(section.fields) for section in self.sections)
        return section_field_count + len(self.unsectioned_fields)

    def total_object_count(self) -> int:
        section_object_count = sum(
            len(section.fields)
            + len(section.tables)
            + len(section.images)
            + len(section.choices)
            + len(section.conditions)
            for section in self.sections
        )
        return (
            section_object_count
            + len(self.unsectioned_fields)
            + len(self.unsectioned_tables)
            + len(self.unsectioned_images)
            + len(self.unsectioned_choices)
            + len(self.conditions)
        )


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()
