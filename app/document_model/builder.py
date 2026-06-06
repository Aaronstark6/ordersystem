from uuid import uuid4

from app.contracts.template_analysis_result import (
    FieldLabelCandidate,
    TableCandidate,
    TemplateAnalysisResult,
    VisualRegionCandidate,
)
from app.document_model.coordinates import Coordinate
from app.document_model.model import DocumentModel
from app.document_model.nodes import (
    ChoiceNode,
    ConditionNode,
    FieldNode,
    ImageNode,
    SectionNode,
    TableNode,
)


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


def _candidate_coordinate(candidate: object, document_type: str) -> Coordinate:
    coordinate = getattr(candidate, "coordinate", None)
    if coordinate is not None:
        return coordinate

    return Coordinate(
        document_type=document_type,
        sheet_name=getattr(candidate, "sheet_name", ""),
        cell=getattr(candidate, "cell", ""),
        row=getattr(candidate, "row", None),
        column=getattr(candidate, "column", None),
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

    for index, candidate in enumerate(analysis_result.images, start=1):
        node_id = f"image:{index}"
        image_key = getattr(candidate, "image_key", node_id)
        label = getattr(candidate, "label", image_key)
        document_model.images[node_id] = ImageNode(
            node_id=node_id,
            node_type="image",
            label=label,
            coordinate=_candidate_coordinate(
                candidate,
                analysis_result.document_type,
            ),
            image_key=image_key,
            image_role=getattr(candidate, "image_role", "attachment"),
            metadata={
                "source_candidate": type(candidate).__name__,
            },
        )

    for index, candidate in enumerate(analysis_result.conditions, start=1):
        node_id = f"condition:{index}"
        condition_key = getattr(candidate, "condition_key", node_id)
        operator = getattr(candidate, "operator", "")
        source_field = getattr(candidate, "source_field", "")
        expected_value = getattr(candidate, "expected_value", "")
        expression = f"{source_field} {operator} {expected_value}".strip()
        document_model.conditions[node_id] = ConditionNode(
            node_id=node_id,
            node_type="condition",
            label=getattr(candidate, "label", condition_key),
            condition_key=condition_key,
            expression=expression,
            controls_node_ids=list(
                getattr(candidate, "controlled_nodes", [])
            ),
            metadata={
                "source_field": source_field,
                "operator": operator,
                "expected_value": expected_value,
                "source_candidate": type(candidate).__name__,
            },
        )

    for index, candidate in enumerate(analysis_result.choices, start=1):
        node_id = f"choice:{index}"
        choice_key = getattr(candidate, "choice_key", node_id)
        options = []
        for option in getattr(candidate, "options", []):
            option_value = getattr(option, "value", option)
            options.append(str(option_value))

        document_model.choices[node_id] = ChoiceNode(
            node_id=node_id,
            node_type="choice",
            label=getattr(candidate, "label", choice_key),
            choice_key=choice_key,
            options=options,
            allow_multiple=bool(
                getattr(candidate, "allow_multiple", False)
            ),
            default_option=getattr(candidate, "default_option", None),
            metadata={
                "source_candidate": type(candidate).__name__,
            },
        )

    if document_model.node_count() == 0:
        raise ValueError("TemplateAnalysisResult did not produce any DocumentModel nodes")

    return document_model
