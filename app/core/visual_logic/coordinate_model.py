from app.document_model.coordinates import Coordinate


def excel_cell_to_coordinate(sheet_name: str, cell: str, row: int, column: int) -> Coordinate:
    return Coordinate(
        document_type="excel",
        sheet_name=sheet_name,
        cell=cell,
        row=row,
        column=column,
    )
