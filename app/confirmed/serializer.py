from dataclasses import asdict

from app.confirmed.model import ConfirmedOrderObject


def confirmed_order_object_to_dict(confirmed_order: ConfirmedOrderObject) -> dict:
    return asdict(confirmed_order)
