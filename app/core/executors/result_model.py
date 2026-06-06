from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class ExportOperationResult:
    operation_id: str
    operation_type: str
    status: str
    message: str
    target: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ExportExecutionResult:
    output_file_path: str
    document_type: str
    success_count: int = 0
    skipped_count: int = 0
    failed_count: int = 0
    operation_results: List[ExportOperationResult] = field(default_factory=list)
