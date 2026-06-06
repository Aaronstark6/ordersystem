from dataclasses import asdict

from app.export.model import ExportStrategy


def export_strategy_to_dict(strategy: ExportStrategy) -> dict:
    return asdict(strategy)
