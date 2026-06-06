from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class CandidateFillField:
    field_key: str
    node_id: str
    label: str
    value: Any
    score: float
    source_order_field_key: str = ""
    reason: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class CandidateFillObject:
    candidate_fill_id: str
    order_id: str
    document_id: str
    template_id: str
    fields: Dict[str, CandidateFillField] = field(default_factory=dict)
    missing_fields: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)

    def field_count(self) -> int:
        return len(self.fields)
