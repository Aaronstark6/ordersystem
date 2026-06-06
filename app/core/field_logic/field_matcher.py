from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class FieldMatchCandidate:
    source_field_key: str
    target_field_key: str
    score: float
    reason: str
    metadata: Dict[str, Any] = field(default_factory=dict)


def build_field_match_candidate(
    source_field_key: str,
    target_field_key: str,
    score: float,
    reason: str,
    metadata: Dict[str, Any] | None = None,
) -> FieldMatchCandidate:
    return FieldMatchCandidate(
        source_field_key=source_field_key,
        target_field_key=target_field_key,
        score=score,
        reason=reason,
        metadata=dict(metadata or {}),
    )


def simple_field_match(
    source_key: str,
    target_key: str,
) -> FieldMatchCandidate:
    if source_key == target_key:
        return build_field_match_candidate(
            source_field_key=source_key,
            target_field_key=target_key,
            score=1.0,
            reason="字段 key 完全相等",
        )

    if source_key in target_key or target_key in source_key:
        return build_field_match_candidate(
            source_field_key=source_key,
            target_field_key=target_key,
            score=0.7,
            reason="一方字段 key 包含另一方",
        )

    return build_field_match_candidate(
        source_field_key=source_key,
        target_field_key=target_key,
        score=0.0,
        reason="字段 key 不匹配",
    )
