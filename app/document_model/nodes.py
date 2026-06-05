from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from app.document_model.coordinates import Coordinate


@dataclass
class BaseNode:
    node_id: str
    node_type: str
    label: str
    coordinate: Optional[Coordinate] = None
    section_id: Optional[str] = None
    exportable: bool = True
    requires_confirmation: bool = True
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class FieldNode(BaseNode):
    field_key: str = ""
    normalized_name: str = ""
    value_type: str = "text"
    required: bool = False


@dataclass
class TableNode(BaseNode):
    table_key: str = ""
    headers: List[str] = field(default_factory=list)
    row_count: Optional[int] = None
    column_count: Optional[int] = None


@dataclass
class ImageNode(BaseNode):
    image_key: str = ""
    image_role: str = "attachment"


@dataclass
class ChoiceNode(BaseNode):
    choice_key: str = ""
    options: List[str] = field(default_factory=list)
    allow_multiple: bool = False
    default_option: Optional[str] = None


@dataclass
class ConditionNode(BaseNode):
    condition_key: str = ""
    expression: str = ""
    controls_node_ids: List[str] = field(default_factory=list)


@dataclass
class SectionNode(BaseNode):
    section_key: str = ""
    child_node_ids: List[str] = field(default_factory=list)
