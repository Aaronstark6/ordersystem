from app.document_model.model import DocumentModel, ValidationIssue


def validate_document_model(document_model: DocumentModel) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []

    if not document_model.document_id:
        issues.append(
            ValidationIssue(
                level="error",
                code="missing_document_id",
                message="DocumentModel 缺少 document_id",
            )
        )

    if not document_model.template_id:
        issues.append(
            ValidationIssue(
                level="error",
                code="missing_template_id",
                message="DocumentModel 缺少 template_id",
            )
        )

    if not document_model.document_type:
        issues.append(
            ValidationIssue(
                level="error",
                code="missing_document_type",
                message="DocumentModel 缺少 document_type",
            )
        )

    return issues
