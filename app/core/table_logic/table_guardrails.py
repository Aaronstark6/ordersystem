from __future__ import annotations

from typing import Iterable

from app.contracts.template_analysis_result import CellInfo


CHOICE_MARKERS = {
    "□",
    "☐",
    "☑",
    "✓",
    "✔",
    "○",
    "●",
    "◯",
    "◉",
}

FIELD_LABEL_HINTS = {
    "customer name",
    "customer",
    "order no",
    "order number",
    "product name",
    "product",
    "quantity",
    "qty",
    "destination",
    "rush order",
    "private label",
    "notes",
    "field",
}

IMAGE_KEYWORDS = {
    "image",
    "product image",
    "label image",
    "package image",
    "packaging image",
    "logo",
    "stamp",
    "signature",
    "图片",
    "产品图片",
    "标签图片",
    "包装图片",
    "商标",
    "印章",
    "签名",
}

OBJECT_MAP_FIRST_VALUES = {
    "field",
    "choice",
    "condition",
    "table",
    "image",
}


def normalize_table_text(value: object) -> str:
    return " ".join(str(value or "").strip().lower().split())


def row_texts(cells: Iterable[CellInfo]) -> list[str]:
    return [
        str(cell.value).strip()
        for cell in sorted(cells, key=lambda item: item.column)
        if str(cell.value or "").strip()
    ]


def _normalized_row_texts(cells: Iterable[CellInfo]) -> list[str]:
    return [normalize_table_text(text) for text in row_texts(cells)]


def is_choice_like_row(cells: Iterable[CellInfo]) -> bool:
    texts = row_texts(cells)
    normalized = [normalize_table_text(text) for text in texts]
    joined = " ".join(normalized)
    if any(text in CHOICE_MARKERS for text in texts):
        return True
    if "set_choice" in joined:
        return True
    return bool(normalized and normalized[0] == "choice")


def is_field_like_row(cells: Iterable[CellInfo]) -> bool:
    normalized = _normalized_row_texts(cells)
    if not normalized:
        return False
    if normalized[0] == "field" or "write_value" in normalized:
        return True
    return len(normalized) < 5 and sum(
        text in FIELD_LABEL_HINTS
        for text in normalized
    ) >= 2


def is_image_like_row(cells: Iterable[CellInfo]) -> bool:
    normalized = _normalized_row_texts(cells)
    if not normalized:
        return False
    joined = " ".join(normalized)
    if normalized[0] == "image" or "insert_image" in joined:
        return True
    return any(keyword in joined for keyword in IMAGE_KEYWORDS)


def is_control_mapping_header(cells: Iterable[CellInfo]) -> bool:
    normalized = set(_normalized_row_texts(cells))
    return {
        "object type",
        "key",
        "target cell",
        "expected operation",
    }.issubset(normalized)


def is_object_mapping_detail_row(cells: Iterable[CellInfo]) -> bool:
    normalized = _normalized_row_texts(cells)
    return bool(normalized and normalized[0] in OBJECT_MAP_FIRST_VALUES)


def is_non_table_layout_row(cells: Iterable[CellInfo]) -> bool:
    return (
        is_control_mapping_header(cells)
        or is_object_mapping_detail_row(cells)
        or is_field_like_row(cells)
        or is_choice_like_row(cells)
        or is_image_like_row(cells)
    )
