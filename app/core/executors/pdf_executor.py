from pathlib import Path
from shutil import copyfile

from app.core.executors.result_model import (
    ExportExecutionResult,
    ExportOperationResult,
)
from app.export.model import ExportStrategy


def execute_pdf_export(
    template_file_path: str,
    output_file_path: str,
    export_strategy: ExportStrategy,
) -> ExportExecutionResult:
    template_path = Path(template_file_path)
    output_path = Path(output_file_path)

    if not template_path.exists():
        raise FileNotFoundError(f"PDF 模板文件不存在: {template_file_path}")
    if template_path.suffix.lower() != ".pdf":
        raise ValueError("PDF Executor 只支持 .pdf")
    if output_path.suffix.lower() != ".pdf":
        raise ValueError("PDF Executor 输出文件必须是 .pdf")
    if template_path.resolve() == output_path.resolve():
        raise ValueError("PDF 输出文件不能覆盖原模板")

    result = ExportExecutionResult(
        output_file_path=str(output_path),
        document_type="pdf",
    )

    for operation in export_strategy.operations:
        result.operation_results.append(
            ExportOperationResult(
                operation_id=operation.operation_id,
                operation_type=operation.operation_type,
                status="skipped",
                message=(
                    "PDF Executor 第一版暂不执行真实写入，"
                    "需要后续支持 AcroForm 或坐标覆盖写入"
                ),
                target=dict(operation.target),
                metadata=dict(operation.metadata),
            )
        )
        result.skipped_count += 1

    output_path.parent.mkdir(parents=True, exist_ok=True)
    copyfile(template_path, output_path)

    return result
