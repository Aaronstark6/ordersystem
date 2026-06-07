from uuid import uuid4

from app.confirmed.model import ConfirmedImage
from app.export.model import ExportOperation


def build_image_operation(image: ConfirmedImage) -> ExportOperation:
    return ExportOperation(
        operation_id=str(uuid4()),
        operation_type="insert_image",
        source_node_id=image.node_id,
        field_key=image.image_key,
        label=image.label,
        value={
            "image_key": image.image_key,
            "image_role": image.image_role,
        },
        target=image.coordinate,
        metadata={
            "confirmed": image.confirmed,
            "image_role": image.image_role,
        },
    )
