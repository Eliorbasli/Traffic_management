from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document, Indexed
from pydantic import Field, EmailStr
from typing import Dict, List, Tuple

class Graph(Document):
    graph_id: UUID = Field(default_factory=uuid4 , unique=True)
    nodes: List[str]
    edegs: Dict[str, List[Tuple[str, int]]] # Each edge connects to a node with a distance
    
    class Settings:
        collection = "graphs"
    