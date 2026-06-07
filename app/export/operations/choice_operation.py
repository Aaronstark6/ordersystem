from uuid import uuid4

from app.confirmed.model import ConfirmedChoice
from app.export.model import ExportOperation


def build_choice_operation(choice: ConfirmedChoice) -> ExportOperation:
    return ExportOperation(
        operation_id=str(uuid4()),
        operation_type="set_choice",
        source_node_id=choice.node_id,
        field_key=choice.choice_key,
        label=choice.label,
        value={
            "choice_mode": choice.choice_mode,
            "final_value": choice.final_value,
            "final_selected_values": list(choice.final_selected_values),
            "options": list(choice.options),
            "option_details": [
                dict(option_detail)
                for option_detail in choice.option_details
            ],
        },
        target=dict(choice.coordinate),
        metadata={
            "confirmed": choice.confirmed,
            "default_option": choice.default_option,
            "allow_multiple": choice.allow_multiple,
        },
    )
