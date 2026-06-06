from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class ChoiceOption:
    option_key: str
    label: str
    value: Any
    selected: bool = False
    metadata: Dict[str, Any] = field(default_factory=dict)


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


def build_choice_option(
    option_key: str,
    label: str,
    value: Any,
    selected: bool = False,
    metadata: Dict[str, Any] | None = None,
) -> ChoiceOption:
    return ChoiceOption(
        option_key=option_key,
        label=label,
        value=value,
        selected=selected,
        metadata=metadata or {},
    )


def build_choice_candidate(
    choice_key: str,
    label: str,
    options: List[ChoiceOption],
    allow_multiple: bool = False,
    default_option: Optional[str] = None,
    metadata: Dict[str, Any] | None = None,
) -> ChoiceCandidate:
    return ChoiceCandidate(
        choice_key=choice_key,
        label=label,
        options=options,
        allow_multiple=allow_multiple,
        default_option=default_option,
        metadata=metadata or {},
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
