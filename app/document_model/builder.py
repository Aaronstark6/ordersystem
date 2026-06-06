from uuid import uuid4

from app.contracts.template_analysis_result import (
    FieldLabelCandidate,
    TableCandidate,
    TemplateAnalysisResult,
    VisualRegionCandidate,
)
from app.document_model.coordinates import Coordinate
from app.document_model.model import DocumentModel
from app.document_model.nodes import FieldNode, SectionNode, TableNode


def _field_coordinate(candidate: FieldLabelCandidate, document_type: str) -> Coordinate:
    return Coordinate(
        document_type=document_type,
        sheet_name=candidate.sheet_name,
        cell=candidate.cell,
        row=candidate.row,
        column=candidate.column,
    )


def _table_coordinate(candidate: TableCandidate, document_type: str) -> Coordinate:
    return Coordinate(
        document_type=document_type,
        sheet_name=candidate.sheet_name,
        row=candidate.min_row,
        column=candidate.min_col,
        width=float(candidate.max_col - candidate.min_col + 1),
        height=float(candidate.max_row - candidate.min_row + 1),
    )


def _section_coordinate(candidate: VisualRegionCandidate, document_type: str) -> Coordinate:
    return Coordinate(
        document_type=document_type,
        sheet_name=candidate.sheet_name,
        row=candidate.min_row,
        column=candidate.min_col,
        width=float(candidate.max_col - candidate.min_col + 1),
        height=float(candidate.max_row - candidate.min_row + 1),
    )


def build_document_model(analysis_result: TemplateAnalysisResult) -> DocumentModel:
    document_model = DocumentModel(
        document_id=str(uuid4()),
        template_id=analysis_result.template_id,
        document_type=analysis_result.document_type,
    )

    for index, candidate in enumerate(analysis_result.field_labels, start=1):
        node_id = f"field:{index}"
        document_model.fields[node_id] = FieldNode(
            node_id=node_id,
            node_type="field",
            label=candidate.label,
            coordinate=_field_coordinate(candidate, analysis_result.document_type),
            field_key=node_id,
            normalized_name=candidate.label,
            metadata={
                "confidence": candidate.confidence,
                "reason": candidate.reason,
            },
        )

    for index, candidate in enumerate(analysis_result.tables, start=1):
        node_id = f"table:{index}"
        document_model.tables[node_id] = TableNode(
            node_id=node_id,
            node_type="table",
            label=" / ".join(candidate.headers) or node_id,
            coordinate=_table_coordinate(candidate, analysis_result.document_type),
            table_key=node_id,
            headers=list(candidate.headers),
            row_count=candidate.max_row - candidate.min_row + 1,
            column_count=candidate.max_col - candidate.min_col + 1,
            metadata={
                "confidence": candidate.confidence,
                "reason": candidate.reason,
            },
        )

    for index, candidate in enumerate(analysis_result.visual_regions, start=1):
        node_id = f"section:{index}"
        document_model.sections[node_id] = SectionNode(
            node_id=node_id,
            node_type="section",
            label=candidate.title or candidate.region_key,
            coordinate=_section_coordinate(candidate, analysis_result.document_type),
            section_key=candidate.region_key,
            metadata={
                "confidence": candidate.confidence,
                "region_type": candidate.region_type,
            },
        )

    if document_model.node_count() == 0:
        raise ValueError("TemplateAnalysisResult did not produce any DocumentModel nodes")

    return document_model
