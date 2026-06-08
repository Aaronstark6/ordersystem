from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any


TRIGGER_WORDS = ("if", "如果", "满足", "当")
EQUALS_TOKENS = ("==", "=", "equals", "等于")
CONTAINS_TOKENS = ("contains", "包含关键词", "包含")
SKIP_EXPORT_TOKENS = ("skip export", "skip_export", "隐藏")
EXPORT_TOKENS = ("export", "显示")


@dataclass
class ConditionPattern:
    condition_key: str
    label: str
    source_field: str
    operator: str
    expected_value: Any
    action: str = "skip_export"
    controlled_nodes: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


def normalize_condition_text(value: object) -> str:
    return " ".join(str(value or "").strip().lower().split())


def make_condition_key(label: str, fallback: str) -> str:
    normalized = "".join(
        char.lower() if char.isalnum() else "_"
        for char in label.strip()
    ).strip("_")
    while "__" in normalized:
        normalized = normalized.replace("__", "_")
    return normalized or fallback


def infer_action(text: object) -> str:
    normalized = normalize_condition_text(text)
    if any(token in normalized for token in SKIP_EXPORT_TOKENS):
        return "skip_export"
    if any(token in normalized for token in EXPORT_TOKENS):
        return "export"
    return "skip_export"


def clean_expected_value(value: str) -> str:
    cleaned = value.strip()
    for token in SKIP_EXPORT_TOKENS + EXPORT_TOKENS:
        pattern = re.compile(rf"\b{re.escape(token)}\b", flags=re.IGNORECASE)
        cleaned = pattern.sub("", cleaned).strip()
    return cleaned


def is_valid_source_field(value: str) -> bool:
    normalized = normalize_condition_text(value)
    if not normalized:
        return False
    if "should be" in normalized:
        return False
    return len(normalized.split()) <= 5


def extract_controlled_nodes(text: object) -> list[str]:
    normalized = normalize_condition_text(text)
    if "controls" not in normalized and "控制" not in normalized:
        return []
    if "controls" in normalized:
        tail = normalized.split("controls", 1)[1]
    else:
        tail = normalized.split("控制", 1)[1]
    return [
        part.strip()
        for part in re.split(r"[/,;，；、\s]+", tail)
        if part.strip()
    ]


def parse_condition_text(text: object, fallback_key: str) -> ConditionPattern | None:
    raw = str(text or "").strip()
    normalized = normalize_condition_text(raw)
    if not normalized:
        return None

    expression = raw
    for trigger in TRIGGER_WORDS:
        if normalized.startswith(trigger):
            expression = raw[len(trigger) :].strip()
            break

    operator = ""
    source_field = ""
    expected_value = ""

    contains_pattern = re.search(
        r"(.+?)\s*(?:contains|包含关键词|包含)\s*(.+)",
        expression,
        flags=re.IGNORECASE,
    )
    if contains_pattern:
        operator = "contains"
        source_field = contains_pattern.group(1).strip()
        expected_value = clean_expected_value(contains_pattern.group(2))
    else:
        equals_pattern = re.search(
            r"(.+?)\s*(?:==|=|equals|等于)\s*(.+)",
            expression,
            flags=re.IGNORECASE,
        )
        if equals_pattern:
            operator = "equals"
            source_field = equals_pattern.group(1).strip()
            expected_value = clean_expected_value(equals_pattern.group(2))

    if not source_field or not operator or not is_valid_source_field(source_field):
        return None

    label = raw
    condition_key = make_condition_key(source_field, fallback_key)
    return ConditionPattern(
        condition_key=f"{condition_key}_condition",
        label=label,
        source_field=make_condition_key(source_field, source_field),
        operator=operator,
        expected_value=expected_value,
        action=infer_action(raw),
        metadata={
            "source": "condition_text",
            "raw_text": raw,
        },
    )
