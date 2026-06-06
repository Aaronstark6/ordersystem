from dataclasses import dataclass
from pathlib import Path


@dataclass
class PdfTemplateInfo:
    file_path: str
    file_name: str
    document_type: str = "pdf"


def read_pdf_template(file_path: str) -> PdfTemplateInfo:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"PDF 模板文件不存在: {file_path}")
    if path.suffix.lower() != ".pdf":
        raise ValueError(f"不是 PDF 模板文件: {file_path}")

    return PdfTemplateInfo(
        file_path=str(path),
        file_name=path.name,
    )
