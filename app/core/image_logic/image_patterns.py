from __future__ import annotations


IMAGE_KEYWORDS = (
    "product image",
    "label image",
    "package image",
    "packaging image",
    "image",
    "logo",
    "stamp",
    "signature",
    "产品图片",
    "标签图片",
    "包装图片",
    "图片",
    "商标",
    "印章",
    "签名",
)


def normalize_image_text(text: object) -> str:
    return " ".join(str(text).strip().lower().split())


def contains_image_keyword(text: object) -> bool:
    normalized = normalize_image_text(text)
    if not normalized:
        return False
    return any(keyword in normalized for keyword in IMAGE_KEYWORDS)


def infer_image_role(text: object) -> str:
    normalized = normalize_image_text(text)

    if "logo" in normalized or "商标" in normalized:
        return "logo"
    if "product image" in normalized or "产品图片" in normalized:
        return "product_image"
    if "label image" in normalized or "标签图片" in normalized:
        return "label_image"
    if (
        "package image" in normalized
        or "packaging image" in normalized
        or "包装图片" in normalized
    ):
        return "package_image"
    if "stamp" in normalized or "印章" in normalized:
        return "stamp"
    if "signature" in normalized or "签名" in normalized:
        return "signature"
    return "generic_image"
