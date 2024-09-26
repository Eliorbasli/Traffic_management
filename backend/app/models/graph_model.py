from typing import List, Dict, Tuple
from uuid import UUID, uuid4
from beanie import Document, Indexed ,before_event, Link, Replace , Insert
from datetime import datetime
from pydantic import BaseModel, Field

from .user_model import User
class Graph(Document):
    graph_id: UUID = Field(default_factory=uuid4, unique=True)
    name:str
    nodes: List[str]
    edges: List[List[str]]
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    owner : Link[User]

    def __repr__(self) -> str:
        return f"<Graph {self.graph_id}>"
    
    def __str__(self) -> str:
        return self.name
    
    def __hash__(self) -> int:
        return hash(self.name)
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Graph):
            return self.graph_id == other.graph_id
        return False


@before_event([Replace , Insert])
def update_update_at(self):
    self.updated_at = datetime.now()
    
class Collection:
    name = "graphs"
