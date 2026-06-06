from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class ExportOperation:
    operation_id: str
    operation_type: str
    source_node_id: str
    field_key: str
    label: str
    value: Any
    target: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ExportStrategy:
    export_strategy_id: str
    confirmed_order_id: str
    document_id: str
    template_id: str
    document_type: str = "excel"
    operations: List[ExportOperation] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)

    def operation_count(self) -> int:
        return len(self.operations)
