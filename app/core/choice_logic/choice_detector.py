from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from app.contracts.template_analysis_result import CellInfo, SheetInfo
from app.core.choice_logic.choice_patterns import (
    ChoiceOptionPattern,
    ChoicePattern,
    common_binary_pair,
    is_yes_no_pair,
    make_choice_key,
    marker_selected,
    marker_type,
    nearest_label_above,
    row_cells,
    split_inline_marker,
)
from app.document_model.coordinates import Coordinate


@dataclass
class ChoiceOption:
    option_key: str
    label: str
    value: Any
    selected: bool = False
    metadata: Dict[str, Any] = field(default_factory=dict)
    coordinate: Optional[Coordinate] = None


@dataclass
class ChoiceGroup:
    choice_key: str
    label: str
    options: List[ChoiceOption] = field(default_factory=list)
    allow_multiple: bool = False
    default_option: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ChoiceCandidate:
    choice_key: str
    label: str
    options: List[ChoiceOption] = field(default_factory=list)
    allow_multiple: bool = False
    default_option: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    choice_mode: str = "value"


def build_choice_option(
    option_key: str,
    label: str,
    value: Any,
    selected: bool = False,
    metadata: Dict[str, Any] | None = None,
    coordinate: Optional[Coordinate] = None,
) -> ChoiceOption:
    return ChoiceOption(
        option_key=option_key,
        label=label,
        value=value,
        selected=selected,
        metadata=metadata or {},
        coordinate=coordinate,
    )


def build_choice_candidate(
    choice_key: str,
    label: str,
    options: List[ChoiceOption],
    allow_multiple: bool = False,
    default_option: Optional[str] = None,
    metadata: Dict[str, Any] | None = None,
    choice_mode: str = "value",
) -> ChoiceCandidate:
    return ChoiceCandidate(
        choice_key=choice_key,
        label=label,
        options=options,
        allow_multiple=allow_multiple,
        default_option=default_option,
        metadata=metadata or {},
        choice_mode=choice_mode,
    )


def choice_candidate_to_group(candidate: ChoiceCandidate) -> ChoiceGroup:
    return ChoiceGroup(
        choice_key=candidate.choice_key,
        label=candidate.label,
        options=candidate.options,
        allow_multiple=candidate.allow_multiple,
        default_option=candidate.default_option,
        metadata=candidate.metadata,
    )


def _option_coordinate(cell: CellInfo) -> Coordinate:
    return Coordinate(
        document_type="excel",
        sheet_name=cell.sheet_name,
        cell=cell.cell,
        row=cell.row,
        column=cell.column,
    )


def _option_value(label: str) -> str:
    return make_choice_key(label, "option")


def _build_candidate(pattern: ChoicePattern, index: int) -> ChoiceCandidate:
    fallback_key = f"choice_{index}"
    choice_key = make_choice_key(pattern.label, fallback_key)
    options = [
        build_choice_option(
            option_key=f"{choice_key}:{_option_value(option.label)}",
            label=option.label,
            value=_option_value(option.label),
            selected=option.selected,
            metadata=dict(option.metadata),
            coordinate=_option_coordinate(option.cell),
        )
        for option in pattern.options
    ]

    return build_choice_candidate(
        choice_key=choice_key,
        label=pattern.label,
        options=options,
        allow_multiple=pattern.allow_multiple,
        metadata=dict(pattern.metadata),
        choice_mode=pattern.choice_mode,
    )


def _marker_options_from_row(sheet: SheetInfo, cells: list[CellInfo]) -> ChoicePattern | None:
    options: list[ChoiceOptionPattern] = []
    mode: str | None = None
    cells_by_column = {cell.column: cell for cell in cells}

    for cell in cells:
        current_mode = marker_type(cell.value)
        if current_mode is None:
            continue

        label_cell = cells_by_column.get(cell.column + 1)
        if label_cell is None or label_cell.value is None:
            continue
        label = str(label_cell.value).strip()
        if not label:
            continue

        mode = mode or current_mode
        if mode != current_mode:
            continue

        options.append(
            ChoiceOptionPattern(
                label=label,
                value=_option_value(label),
                cell=cell,
                selected=marker_selected(cell.value),
                metadata={"source": "split_marker_label"},
            )
        )

    if len(options) < 2 or mode is None:
        return None

    return ChoicePattern(
        label=nearest_label_above(sheet, options[0].cell.row, options[0].cell.column),
        options=options,
        choice_mode="checkbox_group" if mode == "checkbox" else "radio_group",
        allow_multiple=mode == "checkbox",
        metadata={"source": "marker_row"},
    )


def _inline_marker_options(sheet: SheetInfo, cells: list[CellInfo]) -> ChoicePattern | None:
    options: list[ChoiceOptionPattern] = []
    mode: str | None = None

    for cell in cells:
        split = split_inline_marker(cell.value)
        if split is None:
            continue
        marker, label = split
        current_mode = marker_type(marker)
        if current_mode is None:
            continue

        mode = mode or current_mode
        if mode != current_mode:
            continue

        options.append(
            ChoiceOptionPattern(
                label=label,
                value=_option_value(label),
                cell=cell,
                selected=marker_selected(marker),
                metadata={"source": "inline_marker"},
            )
        )

    if len(options) < 2 or mode is None:
        return None

    return ChoicePattern(
        label=nearest_label_above(sheet, options[0].cell.row, options[0].cell.column),
        options=options,
        choice_mode="checkbox_group" if mode == "checkbox" else "radio_group",
        allow_multiple=mode == "checkbox",
        metadata={"source": "inline_marker_row"},
    )


def _binary_options(sheet: SheetInfo, cells: list[CellInfo]) -> ChoicePattern | None:
    if any(marker_type(cell.value) or split_inline_marker(cell.value) for cell in cells):
        return None

    text_cells = [
        cell
        for cell in cells
        if cell.value is not None and str(cell.value).strip()
    ]
    values = [str(cell.value).strip() for cell in text_cells]
    if len(values) == 1 and "/" in values[0]:
        parts = [
            part.strip()
            for part in values[0].split("/")
            if part.strip()
        ]
        if is_yes_no_pair(parts):
            source = "yes_no_inline"
        elif common_binary_pair(parts) is not None:
            source = "common_binary_pair_inline"
        else:
            return None

        cell = text_cells[0]
        options = [
            ChoiceOptionPattern(
                label=part,
                value=_option_value(part),
                cell=cell,
                metadata={"source": source},
            )
            for part in parts
        ]
        return ChoicePattern(
            label=nearest_label_above(sheet, cell.row, cell.column),
            options=options,
            choice_mode="radio_group",
            allow_multiple=False,
            metadata={"source": source},
        )

    if len(values) < 2:
        return None

    if is_yes_no_pair(values):
        pair_values = {"yes", "no"}
        source = "yes_no"
    else:
        pair = common_binary_pair(values)
        if pair is None:
            return None
        pair_values = set(pair)
        source = "common_binary_pair"

    options = [
        ChoiceOptionPattern(
            label=str(cell.value).strip(),
            value=_option_value(str(cell.value).strip()),
            cell=cell,
            metadata={"source": source},
        )
        for cell in text_cells
        if make_choice_key(str(cell.value), "") in pair_values
    ]
    if len(options) < 2:
        return None

    return ChoicePattern(
        label=nearest_label_above(sheet, options[0].cell.row, options[0].cell.column),
        options=options,
        choice_mode="radio_group",
        allow_multiple=False,
        metadata={"source": source},
    )


def _dedupe_patterns(patterns: list[ChoicePattern]) -> list[ChoicePattern]:
    seen: set[tuple[str, tuple[str, ...]]] = set()
    unique: list[ChoicePattern] = []
    for pattern in patterns:
        key = (
            pattern.choice_mode,
            tuple(option.cell.cell for option in pattern.options),
        )
        if key in seen:
            continue
        seen.add(key)
        unique.append(pattern)
    return unique


def detect_choices(sheets: List[SheetInfo]) -> List[ChoiceCandidate]:
    patterns: list[ChoicePattern] = []

    for sheet in sheets:
        for cells in row_cells(sheet).values():
            for detector in (
                _marker_options_from_row,
                _inline_marker_options,
                _binary_options,
            ):
                pattern = detector(sheet, cells)
                if pattern is not None:
                    patterns.append(pattern)

    return [
        _build_candidate(pattern, index)
        for index, pattern in enumerate(_dedupe_patterns(patterns), start=1)
    ]
