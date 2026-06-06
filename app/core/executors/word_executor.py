from pathlib import Path
from xml.sax.saxutils import escape
from zipfile import ZIP_DEFLATED, ZipFile

from app.core.executors.result_model import (
    ExportExecutionResult,
    ExportOperationResult,
)
from app.export.model import ExportOperation, ExportStrategy


def _operation_result(operation: ExportOperation) -> ExportOperationResult:
    return ExportOperationResult(
        operation_id=operation.operation_id,
        operation_type=operation.operation_type,
        status="",
        message="",
        target=dict(operation.target),
        metadata=dict(operation.metadata),
    )


def execute_word_export(
    template_file_path: str,
    output_file_path: str,
    export_strategy: ExportStrategy,
) -> ExportExecutionResult:
    template_path = Path(template_file_path)
    output_path = Path(output_file_path)

    if not template_path.exists():
        raise FileNotFoundError(f"Word 模板文件不存在: {template_file_path}")
    if template_path.suffix.lower() != ".docx":
        raise ValueError("Word Executor 第一版只支持 .docx")
    if output_path.suffix.lower() != ".docx":
        raise ValueError("Word Executor 输出文件必须是 .docx")
    if template_path.resolve() == output_path.resolve():
        raise ValueError("Word 输出文件不能覆盖原模板")

    result = ExportExecutionResult(
        output_file_path=str(output_path),
        document_type="word",
    )

    with ZipFile(template_path, "r") as source_archive:
        try:
            document_xml = source_archive.read("word/document.xml").decode("utf-8")
        except KeyError:
            document_xml = None

        for operation in export_strategy.operations:
            operation_result = _operation_result(operation)

            if operation.operation_type != "write_value":
                operation_result.status = "skipped"
                operation_result.message = "Word Executor 第一版只支持 write_value"
                result.skipped_count += 1
            elif operation.target.get("bookmark"):
                operation_result.status = "skipped"
                operation_result.message = "Word bookmark 真实定位尚未实现"
                result.skipped_count += 1
            else:
                placeholder = operation.target.get("placeholder")
                if not placeholder:
                    operation_result.status = "failed"
                    operation_result.message = "导出目标缺少 placeholder"
                    result.failed_count += 1
                elif document_xml is None:
                    operation_result.status = "failed"
                    operation_result.message = "Word 模板缺少 word/document.xml"
                    result.failed_count += 1
                elif placeholder not in document_xml:
                    operation_result.status = "failed"
                    operation_result.message = f"Word placeholder 不存在: {placeholder}"
                    result.failed_count += 1
                else:
                    document_xml = document_xml.replace(
                        placeholder,
                        escape(str(operation.value)),
                    )
                    operation_result.status = "success"
                    operation_result.message = "Word placeholder 替换成功"
                    result.success_count += 1

            result.operation_results.append(operation_result)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        with ZipFile(output_path, "w", compression=ZIP_DEFLATED) as output_archive:
            for archive_item in source_archive.infolist():
                content = source_archive.read(archive_item.filename)
                if (
                    archive_item.filename == "word/document.xml"
                    and document_xml is not None
                ):
                    content = document_xml.encode("utf-8")
                output_archive.writestr(archive_item, content)

    return result
