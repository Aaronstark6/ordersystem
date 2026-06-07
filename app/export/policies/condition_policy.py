from dataclasses import dataclass, field
from typing import Any, Iterable, Mapping

from app.confirmed.model import ConfirmedCondition


@dataclass
class ConditionPolicy:
    skipped_node_ids: set[str] = field(default_factory=set)
    allowed_node_ids: set[str] = field(default_factory=set)
    warnings: list[str] = field(default_factory=list)

    def should_skip_export(self, node_id: str) -> bool:
        return node_id in self.skipped_node_ids

    def allows_export(self, node_id: str) -> bool:
        return not self.should_skip_export(node_id)


def _is_empty(value: Any) -> bool:
    return value is None or value == "" or value == [] or value == {}


def _evaluate_condition(
    operator: str,
    actual_value: Any,
    expected_value: Any,
) -> bool:
    if operator == "equals":
        return actual_value == expected_value
    if operator == "not_equals":
        return actual_value != expected_value
    if operator == "is_empty":
        return _is_empty(actual_value)
    if operator == "not_empty":
        return not _is_empty(actual_value)
    if operator == "contains":
        try:
            return expected_value in actual_value
        except TypeError:
            return False
    raise ValueError(f"不支持的 ConditionPolicy operator: {operator}")


def _condition_result(
    condition: ConfirmedCondition,
    values: Mapping[str, Any],
) -> tuple[bool | None, str]:
    metadata = condition.metadata
    precomputed_result = metadata.get("condition_result")
    if isinstance(precomputed_result, bool):
        return precomputed_result, ""

    operator = str(metadata.get("operator", "")).strip()
    if not operator:
        return None, "缺少 operator"

    actual_value_key = next(
        (
            key
            for key in ("actual_value", "source_value", "value")
            if key in metadata
        ),
        None,
    )
    if actual_value_key is not None:
        actual_value = metadata[actual_value_key]
    else:
        source_field = str(metadata.get("source_field", "")).strip()
        if not source_field or source_field not in values:
            return None, "缺少可解析的条件实际值"
        actual_value = values[source_field]

    try:
        return (
            _evaluate_condition(
                operator=operator,
                actual_value=actual_value,
                expected_value=metadata.get("expected_value"),
            ),
            "",
        )
    except ValueError as exc:
        return None, str(exc)


def build_condition_policy(
    conditions: Iterable[ConfirmedCondition],
    values: Mapping[str, Any] | None = None,
) -> ConditionPolicy:
    policy = ConditionPolicy()
    resolved_values = values or {}

    for condition in conditions:
        controlled_node_ids = list(condition.controls_node_ids)
        if not controlled_node_ids:
            continue

        action = str(condition.metadata.get("action", "skip_export")).strip()
        result, error = _condition_result(condition, resolved_values)

        if result is None:
            policy.skipped_node_ids.update(controlled_node_ids)
            policy.warnings.append(
                f"ConditionPolicy 无法判断 {condition.condition_key}: "
                f"{error}；已保守跳过受控节点"
            )
            continue

        if action == "skip_export":
            if result:
                policy.skipped_node_ids.update(controlled_node_ids)
            continue

        if action == "export":
            if result:
                policy.allowed_node_ids.update(controlled_node_ids)
            else:
                policy.skipped_node_ids.update(controlled_node_ids)
            continue

        policy.skipped_node_ids.update(controlled_node_ids)
        policy.warnings.append(
            f"ConditionPolicy 不支持 action: {action}；已保守跳过受控节点"
        )

    return policy
