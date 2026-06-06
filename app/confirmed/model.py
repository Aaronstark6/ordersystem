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
class ConfirmedSection:
    section_key: str
    title: str
    node_id: str
    fields: List[ConfirmedField] = field(default_factory=list)
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
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)

    def field_count(self) -> int:
        section_field_count = sum(len(section.fields) for section in self.sections)
        return section_field_count + len(self.unsectioned_fields)


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()
