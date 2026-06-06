from pathlib import Path
from typing import Any

from app.core.template_reader.excel_reader import read_excel_template
from app.core.template_reader.pdf_reader import read_pdf_template
from app.core.template_reader.word_reader import read_word_template


def read_template_file(file_path: str) -> Any:
    suffix = Path(file_path).suffix.lower()

    if suffix in {".xlsx", ".xlsm"}:
        return read_excel_template(file_path)
    if suffix == ".pdf":
        return read_pdf_template(file_path)
    if suffix in {".docx", ".doc"}:
        return read_word_template(file_path)

    raise ValueError(f"不支持的模板文件格式: {suffix or '无后缀'}")
