from typing import Iterable


def build_order_parse_prompt(
    raw_text: str,
    expected_fields: Iterable[str] | None = None,
) -> str:
    fields = list(expected_fields or [])

    field_block = ""
    if fields:
        field_block = "\n需要优先提取的字段：\n" + "\n".join(
            f"- {field}" for field in fields
        )

    return (
        "你是订单解析助手。\n"
        "请从客户订单文本中提取结构化订单字段。\n"
        "输出必须是 JSON 对象。\n"
        f"{field_block}\n\n"
        "客户订单文本：\n"
        f"{raw_text}"
    )
