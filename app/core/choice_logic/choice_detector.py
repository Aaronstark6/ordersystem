from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

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
