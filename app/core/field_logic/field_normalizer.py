import re


_STANDARD_FIELD_KEYS = {
    "客户名称": "customer_name",
    "客户": "customer_name",
    "公司": "company_name",
    "产品名称": "product_name",
    "产品": "product_name",
    "数量": "quantity",
    "规格": "specification",
    "单价": "unit_price",
    "金额": "amount",
    "日期": "date",
    "备注": "remark",
    "包装": "packaging",
    "成分": "ingredients",
    "含量": "dosage",
}


def normalize_field_label(label: str) -> str:
    cleaned = label.strip().strip(":：").strip().lower()

    if cleaned in _STANDARD_FIELD_KEYS:
        return _STANDARD_FIELD_KEYS[cleaned]

    cleaned = re.sub(r"\s+", "_", cleaned)
    return f"field_{cleaned}"
