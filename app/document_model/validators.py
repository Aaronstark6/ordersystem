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

    for choice_node in document_model.choices.values():
        if not choice_node.choice_mode:
            issues.append(
                ValidationIssue(
                    level="error",
                    code="missing_choice_mode",
                    message=f"ChoiceNode 缺少 choice_mode: {choice_node.node_id}",
                )
            )

        if not isinstance(choice_node.option_details, list):
            issues.append(
                ValidationIssue(
                    level="error",
                    code="invalid_choice_option_details",
                    message=(
                        f"ChoiceNode option_details 必须是 list: "
                        f"{choice_node.node_id}"
                    ),
                )
            )

    return issues
