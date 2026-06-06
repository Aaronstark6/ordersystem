from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class OrderField:
    field_key: str
    label: str
    value: Any
    confidence: float = 0.0
    source_text: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class MissingField:
    field_key: str
    label: str
    reason: str = ""


@dataclass
class OrderObject:
    order_id: str
    fields: Dict[str, OrderField] = field(default_factory=dict)
    missing_fields: List[MissingField] = field(default_factory=list)
    raw_text: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)

    def field_count(self) -> int:
        return len(self.fields)


@dataclass
class ParseResult:
    order_object: OrderObject
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)

    def has_errors(self) -> bool:
        return bool(self.errors)
