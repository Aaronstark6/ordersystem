from dataclasses import asdict

from app.document_model.model import DocumentModel


def document_model_to_dict(document_model: DocumentModel) -> dict:
    return asdict(document_model)
