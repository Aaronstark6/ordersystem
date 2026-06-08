from dataclasses import dataclass, field
from typing import Any, Dict, List

from app.contracts.template_analysis_result import SheetInfo
from app.core.condition_logic.condition_patterns import (
    extract_controlled_nodes,
    infer_action,
    make_condition_key,
    parse_condition_text,
)

@dataclass
class ConditionCandidate:
    condition_key: str
    label: str
    source_field: str
    operator: str
    expected_value: Any
    action: str = "skip_export"
    controlled_nodes: list[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


def build_condition_candidate(
    condition_key: str,
    label: str,
    source_field: str,
    operator: str,
    expected_value: Any,
    action: str = "skip_export",
    controlled_nodes: list[str] | None = None,
    metadata: Dict[str, Any] | None = None,
) -> ConditionCandidate:
    return ConditionCandidate(
        condition_key=condition_key,
        label=label,
        source_field=source_field,
        operator=operator,
        expected_value=expected_value,
        action=action,
        controlled_nodes=list(controlled_nodes or []),
        metadata=dict(metadata or {}),
    )


def _row_texts(sheet: SheetInfo) -> dict[int, list[str]]:
    rows: dict[int, list[str]] = {}
    for cell in sheet.cells:
        text = str(cell.value or "").strip()
        if text:
            rows.setdefault(cell.row, []).append(text)
    return rows


def _row_controlled_nodes(texts: list[str]) -> list[str]:
    nodes: list[str] = []
    for text in texts:
        for node in extract_controlled_nodes(text):
            if node not in nodes:
                nodes.append(node)
    return nodes


def _row_action(texts: list[str]) -> str:
    joined = " ".join(texts)
    return infer_action(joined)


def detect_conditions(sheets: List[SheetInfo]) -> List[ConditionCandidate]:
    candidates: list[ConditionCandidate] = []

    for sheet in sheets:
        for row_index, texts in _row_texts(sheet).items():
            controlled_nodes = _row_controlled_nodes(texts)
            action = _row_action(texts)
            for text in texts:
                pattern = parse_condition_text(
                    text,
                    fallback_key=f"{sheet.sheet_name}_{row_index}",
                )
                if pattern is None:
                    continue

                candidates.append(
                    build_condition_candidate(
                        condition_key=make_condition_key(
                            pattern.condition_key,
                            f"condition_{len(candidates) + 1}",
                        ),
                        label=pattern.label,
                        source_field=pattern.source_field,
                        operator=pattern.operator,
                        expected_value=pattern.expected_value,
                        action=action or pattern.action,
                        controlled_nodes=controlled_nodes or pattern.controlled_nodes,
                        metadata={
                            **pattern.metadata,
                            "sheet_name": sheet.sheet_name,
                            "row": row_index,
                            "action": action or pattern.action,
                            "controlled_nodes": controlled_nodes,
                        },
                    )
                )

    return candidates
