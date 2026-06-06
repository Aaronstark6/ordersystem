from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List

from openpyxl import load_workbook
from openpyxl.utils.cell import coordinate_from_string, column_index_from_string

from app.export.model import ExportStrategy


class ExcelExecutionError(Exception):
    pass


@dataclass
class ExportOperationResult:
    operation_id: str
    operation_type: str
    status: str
    message: str
    target: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ExcelExportResult:
    output_file_path: str
    success_count: int = 0
    skipped_count: int = 0
    failed_count: int = 0
    operation_results: List[ExportOperationResult] = field(default_factory=list)


def _get_target_value(target: dict[str, Any], key: str) -> Any:
    value = target.get(key)
    if value is None or value == "":
        raise ExcelExecutionError(f"导出目标缺少 {key}")
    return value


def _get_worksheet(workbook: Any, sheet_name: str) -> Any:
    if sheet_name not in workbook.sheetnames:
        raise ExcelExecutionError(f"工作表不存在: {sheet_name}")
    return workbook[sheet_name]


def _write_value(workbook: Any, target: Dict[str, Any], value: Any) -> None:
    sheet_name = _get_target_value(target, "sheet_name")
    cell = _get_target_value(target, "cell")
    worksheet = _get_worksheet(workbook, sheet_name)
    worksheet[cell] = value


def _write_table(workbook: Any, target: Dict[str, Any], value: Any) -> None:
    sheet_name = _get_target_value(target, "sheet_name")
    start_cell = _get_target_value(target, "start_cell")
    if not isinstance(value, list):
        raise ExcelExecutionError("write_table 的 value 必须是 list")

    worksheet = _get_worksheet(workbook, sheet_name)
    column_letters, start_row = coordinate_from_string(start_cell)
    start_column = column_index_from_string(column_letters)

    for row_offset, row_values in enumerate(value):
        values = row_values if isinstance(row_values, (list, tuple)) else [row_values]
        for column_offset, cell_value in enumerate(values):
            worksheet.cell(
                row=start_row + row_offset,
                column=start_column + column_offset,
                value=cell_value,
            )


def _validate_insert_image(
    workbook: Any,
    target: Dict[str, Any],
    value: Any,
) -> None:
    sheet_name = _get_target_value(target, "sheet_name")
    _get_target_value(target, "cell")
    _get_worksheet(workbook, sheet_name)
    if value is None or value == "":
        raise ExcelExecutionError("insert_image 缺少图片值")


def execute_excel_export(
    template_file_path: str,
    output_file_path: str,
    export_strategy: ExportStrategy,
) -> ExcelExportResult:
    template_path = Path(template_file_path)
    output_path = Path(output_file_path)

    if not template_path.exists():
        raise FileNotFoundError(f"Excel 模板文件不存在: {template_file_path}")

    workbook = load_workbook(filename=template_path)
    result = ExcelExportResult(output_file_path=str(output_path))

    for operation in export_strategy.operations:
        operation_result = ExportOperationResult(
            operation_id=operation.operation_id,
            operation_type=operation.operation_type,
            status="",
            message="",
            target=dict(operation.target),
            metadata=dict(operation.metadata),
        )

        try:
            if operation.operation_type == "write_value":
                _write_value(workbook, operation.target, operation.value)
                operation_result.status = "success"
                operation_result.message = "单元格值写入成功"
                result.success_count += 1
            elif operation.operation_type == "write_table":
                _write_table(workbook, operation.target, operation.value)
                operation_result.status = "success"
                operation_result.message = "表格值写入成功"
                result.success_count += 1
            elif operation.operation_type == "insert_image":
                _validate_insert_image(
                    workbook,
                    operation.target,
                    operation.value,
                )
                operation_result.status = "skipped"
                operation_result.message = "图片插入尚未实现，已完成占位校验"
                result.skipped_count += 1
            else:
                operation_result.status = "skipped"
                operation_result.message = (
                    f"暂不支持导出操作: {operation.operation_type}"
                )
                result.skipped_count += 1
        except Exception as exc:
            operation_result.status = "failed"
            operation_result.message = str(exc)
            result.failed_count += 1

        result.operation_results.append(operation_result)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    workbook.save(output_path)

    return result
