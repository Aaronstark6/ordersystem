from pathlib import Path
from typing import Optional

from app.contracts.template_analysis_result import TemplateAnalysisResult, VisualRegionCandidate
from app.core.choice_logic.choice_detector import detect_choices
from app.core.field_logic.field_detector import detect_field_labels
from app.core.table_logic.table_detector import detect_tables
from app.core.template_reader.excel_reader import read_excel_template


def _build_basic_visual_regions(result: TemplateAnalysisResult) -> None:
    for sheet in result.sheets:
        if sheet.max_row <= 0 or sheet.max_column <= 0:
            continue

        result.visual_regions.append(
            VisualRegionCandidate(
                sheet_name=sheet.sheet_name,
                region_key=f"{sheet.sheet_name}:full_sheet",
                min_row=1,
                max_row=sheet.max_row,
                min_col=1,
                max_col=sheet.max_column,
                region_type="sheet",
                title=sheet.sheet_name,
                confidence=0.5,
            )
        )


def analyze_excel_template(file_path: str, template_id: Optional[str] = None) -> TemplateAnalysisResult:
    path = Path(file_path)

    result = TemplateAnalysisResult(
        template_id=template_id or path.stem,
        document_type="excel",
    )

    try:
        result.sheets = read_excel_template(file_path)
        result.field_labels = detect_field_labels(result.sheets)
        result.choices = detect_choices(result.sheets)
        result.tables = detect_tables(result.sheets)
        _build_basic_visual_regions(result)

        result.metadata["file_name"] = path.name
        result.metadata["sheet_count"] = len(result.sheets)
        result.metadata["field_label_count"] = len(result.field_labels)
        result.metadata["choice_count"] = len(result.choices)
        result.metadata["table_count"] = len(result.tables)
        result.metadata["visual_region_count"] = len(result.visual_regions)

        if not result.sheets:
            result.warnings.append("Excel 模板没有读取到任何工作表")

    except Exception as exc:
        result.errors.append(f"Excel 模板分析失败: {exc}")

    return result
