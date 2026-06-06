from typing import Any, List

from app.core.choice_logic.choice_detector import ChoiceGroup, ChoiceOption


class ChoiceResolveError(Exception):
    pass


def resolve_choice(
    choice_group: ChoiceGroup,
    selected_values: List[Any],
) -> ChoiceGroup:
    if not choice_group.allow_multiple and len(selected_values) > 1:
        raise ChoiceResolveError(
            f"选择组（ChoiceGroup）不允许多选: {choice_group.choice_key}"
        )

    valid_values = {option.value for option in choice_group.options}

    for value in selected_values:
        if value not in valid_values:
            raise ChoiceResolveError(
                f"选择值不属于选择组（ChoiceGroup）: "
                f"{choice_group.choice_key} -> {value}"
            )

    resolved_options: list[ChoiceOption] = []

    for option in choice_group.options:
        resolved_options.append(
            ChoiceOption(
                option_key=option.option_key,
                label=option.label,
                value=option.value,
                selected=option.value in selected_values,
                metadata=option.metadata,
            )
        )

    return ChoiceGroup(
        choice_key=choice_group.choice_key,
        label=choice_group.label,
        options=resolved_options,
        allow_multiple=choice_group.allow_multiple,
        default_option=choice_group.default_option,
        metadata=choice_group.metadata,
    )
