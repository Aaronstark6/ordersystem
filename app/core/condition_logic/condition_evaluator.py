from dataclasses import dataclass
from typing import Any


@dataclass
class ConditionRule:
    condition_key: str
    source_field: str
    operator: str
    expected_value: Any


def evaluate_condition(rule: ConditionRule, values: dict[str, Any]) -> bool:
    actual_value = values.get(rule.source_field)

    if rule.operator == "equals":
        return actual_value == rule.expected_value

    if rule.operator == "not_equals":
        return actual_value != rule.expected_value

    raise ValueError(f"不支持的条件操作符: {rule.operator}")
