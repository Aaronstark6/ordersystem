from uuid import uuid4

from app.core.ai_parser.order_object import OrderObject
from app.core.matching.confidence_scorer import score_field_match
from app.core.matching.match_result import CandidateFillField, CandidateFillObject
from app.document_model.model import DocumentModel


def build_candidate_fill_object(
    order_object: OrderObject,
    document_model: DocumentModel,
    minimum_score: float = 0.7,
) -> CandidateFillObject:
    candidate = CandidateFillObject(
        candidate_fill_id=str(uuid4()),
        order_id=order_object.order_id,
        document_id=document_model.document_id,
        template_id=document_model.template_id,
    )

    for node_id, field_node in document_model.fields.items():
        best_score = 0.0
        best_order_field = None

        for order_field_key, order_field in order_object.fields.items():
            score = score_field_match(order_field_key, field_node.field_key)
            if score > best_score:
                best_score = score
                best_order_field = order_field

        if best_order_field is None or best_score < minimum_score:
            candidate.missing_fields.append(field_node.field_key)
            continue

        candidate.fields[field_node.field_key] = CandidateFillField(
            field_key=field_node.field_key,
            node_id=node_id,
            label=field_node.label,
            value=best_order_field.value,
            score=best_score,
            source_order_field_key=best_order_field.field_key,
            reason="字段 key 简单匹配",
            metadata={
                "order_label": best_order_field.label,
                "order_confidence": best_order_field.confidence,
            },
        )

    if candidate.field_count() == 0:
        candidate.warnings.append(
            "候选填充值对象（CandidateFillObject）没有生成任何字段"
        )

    return candidate
