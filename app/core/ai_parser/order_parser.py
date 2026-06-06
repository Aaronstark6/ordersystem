from uuid import uuid4

from app.core.ai_parser.order_object import OrderField, OrderObject, ParseResult


def parse_order_text_stub(raw_text: str) -> ParseResult:
    order = OrderObject(
        order_id=str(uuid4()),
        raw_text=raw_text,
        metadata={"parser": "stub"},
    )

    if not raw_text or not raw_text.strip():
        return ParseResult(
            order_object=order,
            warnings=[],
            errors=["订单文本为空"],
        )

    for line in raw_text.splitlines():
        text = line.strip()
        if not text:
            continue

        if "：" in text:
            key, value = text.split("：", 1)
        elif ":" in text:
            key, value = text.split(":", 1)
        else:
            continue

        field_key = key.strip()
        field_value = value.strip()

        if not field_key:
            continue

        order.fields[field_key] = OrderField(
            field_key=field_key,
            label=field_key,
            value=field_value,
            confidence=0.5,
            source_text=text,
        )

    if order.field_count() == 0:
        return ParseResult(
            order_object=order,
            warnings=["未从订单文本中解析出字段"],
            errors=[],
        )

    return ParseResult(order_object=order)
