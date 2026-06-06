from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class ConditionCandidate:
    condition_key: str
    label: str
    source_field: str
    operator: str
    expected_value: Any
    metadata: Dict[str, Any] = field(default_factory=dict)


def build_condition_candidate(
    condition_key: str,
    label: str,
    source_field: str,
    operator: str,
    expected_value: Any,
    metadata: Dict[str, Any] | None = None,
) -> ConditionCandidate:
    return ConditionCandidate(
        condition_key=condition_key,
        label=label,
        source_field=source_field,
        operator=operator,
        expected_value=expected_value,
        metadata=dict(metadata or {}),
    )
