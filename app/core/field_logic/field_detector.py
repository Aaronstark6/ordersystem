from dataclasses import dataclass, field
from typing import Any, Dict, List

from app.contracts.template_analysis_result import FieldLabelCandidate, SheetInfo
from app.document_model.coordinates import Coordinate


@dataclass
class FieldCandidate:
    field_key: str
    label: str
    normalized_name: str
    source: str
    confidence: float
    coordinate: Coordinate
    metadata: Dict[str, Any] = field(default_factory=dict)


def build_field_candidate(
    field_key: str,
    label: str,
    normalized_name: str,
    source: str,
    confidence: float,
    coordinate: Coordinate,
    metadata: Dict[str, Any] | None = None,
) -> FieldCandidate:
    return FieldCandidate(
        field_key=field_key,
        label=label,
        normalized_name=normalized_name,
        source=source,
        confidence=confidence,
        coordinate=coordinate,
        metadata=dict(metadata or {}),
    )


_LABEL_HINTS = (
    "客户",
    "公司",
    "联系人",
    "电话",
    "邮箱",
    "地址",
    "产品",
    "品名",
    "规格",
    "数量",
    "单价",
    "金额",
    "日期",
    "订单",
    "备注",
    "要求",
    "包装",
    "成分",
    "含量",
    "批号",
)


def _looks_like_label(value: object) -> bool:
    if value is None:
        return False

    text = str(value).strip()
    if not text:
        return False

    if len(text) > 40:
        return False

    if text.endswith(":") or text.endswith("："):
        return True

    return any(hint in text for hint in _LABEL_HINTS)


def detect_field_labels(sheets: List[SheetInfo]) -> List[FieldLabelCandidate]:
    candidates: List[FieldLabelCandidate] = []

    for sheet in sheets:
        for cell in sheet.cells:
            if not _looks_like_label(cell.value):
                continue

            label = str(cell.value).strip().rstrip(":：")
            confidence = 0.7

            if str(cell.value).strip().endswith((":", "：")):
                confidence += 0.15

            if cell.is_merged:
                confidence -= 0.05

            candidates.append(
                FieldLabelCandidate(
                    sheet_name=sheet.sheet_name,
                    cell=cell.cell,
                    row=cell.row,
                    column=cell.column,
                    label=label,
                    confidence=min(confidence, 0.95),
                    reason="匹配字段标签关键词或冒号格式",
                )
            )

    return candidates
