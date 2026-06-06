from pathlib import Path
from typing import Any

from openpyxl import load_workbook

from app.export.model import ExportStrategy


class ExcelExecutionError(Exception):
    pass


def _get_target_value(target: dict[str, Any], key: str) -> Any:
    value = target.get(key)
    if value is None or value == "":
        raise ExcelExecutionError(f"导出目标缺少 {key}")
    return value


def execute_excel_export(
    template_file_path: str,
    output_file_path: str,
    export_strategy: ExportStrategy,
) -> str:
    template_path = Path(template_file_path)
    output_path = Path(output_file_path)

    if not template_path.exists():
        raise FileNotFoundError(f"Excel 模板文件不存在: {template_file_path}")

    workbook = load_workbook(filename=template_path)

    for operation in export_strategy.operations:
        if operation.operation_type != "write_value":
            continue

        sheet_name = _get_target_value(operation.target, "sheet_name")
        cell = _get_target_value(operation.target, "cell")

        if sheet_name not in workbook.sheetnames:
            raise ExcelExecutionError(f"工作表不存在: {sheet_name}")

        worksheet = workbook[sheet_name]
        worksheet[cell] = operation.value

    output_path.parent.mkdir(parents=True, exist_ok=True)
    workbook.save(output_path)

    return str(output_path)
