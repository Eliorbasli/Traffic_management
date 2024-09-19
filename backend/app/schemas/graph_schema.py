from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field

class GraphCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Name of the graph")
    description: Optional[str] = Field(None, max_length=500, description="Description of the graph")
    nodes: list[str] = Field(..., description="List of nodes in the graph")
    edges: list[tuple[str, str]] = Field(..., description="List of edges in the graph")

class GraphUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100, description="Name of the graph")
    description: Optional[str] = Field(None, max_length=500, description="Description of the graph")
    nodes: Optional[list[str]] = Field(None, description="List of nodes in the graph")
    edges: Optional[list[tuple[str, str]]] = Field(None, description="List of edges in the graph")

class GraphOut(BaseModel):
    graph_id: UUID
    name: str
    description: Optional[str]
    nodes: list[str]
    edges: list[tuple[str, str]]
    created_at : datetime
    updated_at : datetime
