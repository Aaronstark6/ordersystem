from dataclasses import dataclass
from typing import Optional


@dataclass
class Relationship:
    source_node_id: str
    target_node_id: str
    relationship_type: str
    description: Optional[str] = None
