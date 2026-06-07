from app.confirmed.model import ConfirmedOrderObject


def validate_confirmed_order_object(confirmed_order: ConfirmedOrderObject) -> list[str]:
    errors: list[str] = []

    if not confirmed_order.confirmed_order_id:
        errors.append(
            "人工确认对象（ConfirmedOrderObject）缺少 confirmed_order_id"
        )

    if not confirmed_order.workspace_id:
        errors.append("人工确认对象（ConfirmedOrderObject）缺少 workspace_id")

    if not confirmed_order.document_id:
        errors.append("人工确认对象（ConfirmedOrderObject）缺少 document_id")

    if not confirmed_order.template_id:
        errors.append("人工确认对象（ConfirmedOrderObject）缺少 template_id")

    if not confirmed_order.confirmed_at:
        errors.append("人工确认对象（ConfirmedOrderObject）缺少 confirmed_at")

    if confirmed_order.total_object_count() == 0:
        errors.append("人工确认对象（ConfirmedOrderObject）没有可确认对象")

    return errors
