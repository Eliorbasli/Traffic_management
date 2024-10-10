from typing import List
from app.models.user_model import User
from app.models.graph_model import Graph
from app.schemas.graph_schema import GraphCreate
from beanie import PydanticObjectId

class GraphService:
    @staticmethod
    async def list_graphs(user: User):
        user_object_id = PydanticObjectId(user.id)
        graphs = await Graph.find(Graph.owner.id == user_object_id).to_list()
        return graphs


    @staticmethod
    async def create_graph(user: User , data: GraphCreate) -> Graph:
        graph_data = data.model_dump()
        
        edges = graph_data.get("edges")
        if not all(isinstance(edge, list) and len(edge) == 2 for edge in edges):
            raise ValueError("Each edge must be a list of two node names.")
        graph = Graph(**data.model_dump() , owner=user)
        
        return await graph.insert()
    
    @staticmethod
    async def get_graph_by_name(name: str) -> List[Graph]:
        graphs = await Graph.find({"name": name}).to_list()
        
        return graphs
    
    @staticmethod
    async def get_graph_by_id(graph_id: str) -> List[Graph]:
        graphs = await Graph.find({"graph_id": graph_id}).to_list()
        
        return graphs
