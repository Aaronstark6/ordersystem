from dataclasses import dataclass, field
from typing import Any

from app.contracts.template_analysis_result import CellInfo, SheetInfo


CHECKBOX_MARKERS = {"□", "☐", "☑", "✓", "✔", "鈽�", "鉁�"}
RADIO_MARKERS = {"○", "●", "◯", "◉"}
YES_NO_OPTIONS = {"yes", "no"}
COMMON_BINARY_PAIRS = (
    ("male", "female"),
    ("domestic", "export"),
    ("sample", "production"),
)


@dataclass
class ChoiceOptionPattern:
    label: str
    value: str
    cell: CellInfo
    selected: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class ChoicePattern:
    label: str
    options: list[ChoiceOptionPattern]
    choice_mode: str
    allow_multiple: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)


def normalize_choice_text(value: object) -> str:
    return " ".join(str(value).strip().lower().split())


def make_choice_key(label: str, fallback: str) -> str:
    normalized = "".join(
        char.lower() if char.isalnum() else "_"
        for char in label.strip()
    ).strip("_")
    while "__" in normalized:
        normalized = normalized.replace("__", "_")
    return normalized or fallback


def marker_type(value: object) -> str | None:
    text = str(value).strip()
    if text in CHECKBOX_MARKERS:
        return "checkbox"
    if text in RADIO_MARKERS:
        return "radio"
    return None


def marker_selected(value: object) -> bool:
    return str(value).strip() in {"☑", "✓", "✔", "鉁�", "●", "◉"}


def split_inline_marker(value: object) -> tuple[str, str] | None:
    text = str(value).strip()
    if not text:
        return None
    for marker in CHECKBOX_MARKERS | RADIO_MARKERS:
        if text.startswith(marker):
            label = text[len(marker) :].strip()
            if label:
                return marker, label
    return None


def cell_map(sheet: SheetInfo) -> dict[tuple[int, int], CellInfo]:
    return {
        (cell.row, cell.column): cell
        for cell in sheet.cells
    }


def row_cells(sheet: SheetInfo) -> dict[int, list[CellInfo]]:
    rows: dict[int, list[CellInfo]] = {}
    for cell in sheet.cells:
        rows.setdefault(cell.row, []).append(cell)
    for cells in rows.values():
        cells.sort(key=lambda item: item.column)
    return rows


def nearest_label_above(sheet: SheetInfo, row: int, column: int) -> str:
    cells_by_position = cell_map(sheet)
    for search_row in range(row - 1, 0, -1):
        same_column = cells_by_position.get((search_row, column))
        if same_column and same_column.value:
            return str(same_column.value).strip()

        row_values = [
            cell
            for cell in cells_by_position.values()
            if cell.row == search_row and cell.value
        ]
        if row_values:
            return str(sorted(row_values, key=lambda item: item.column)[0].value).strip()
    return f"{sheet.sheet_name} row {row}"


def is_yes_no_pair(values: list[str]) -> bool:
    normalized = {normalize_choice_text(value) for value in values}
    return YES_NO_OPTIONS.issubset(normalized)


def common_binary_pair(values: list[str]) -> tuple[str, str] | None:
    normalized = {normalize_choice_text(value) for value in values}
    for pair in COMMON_BINARY_PAIRS:
        if set(pair).issubset(normalized):
            return pair
    return None
