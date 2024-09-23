from fastapi import APIRouter, Depends ,HTTPException
from app.models.user_model import User
from app.api.deps.user_deps import get_current_user
from app.schemas.graph_schema import GraphCreate, GraphOut, GraphUpdate
from app.services.graph_service import GraphService
from app.models.graph_model import Graph
from typing import List
from uuid import UUID

graph_router = APIRouter()

@graph_router.get('/' , summary="Get all graphs of the user", response_model=GraphOut)
async def list(current_user: User = Depends(get_current_user)):
    return await GraphService.list_graphs(current_user)

@graph_router.post('/create' , summary="Create new Graph" , response_model=Graph)
async def create_graph(data: GraphCreate, current_user: User = Depends(get_current_user)):
    return await GraphService.create_graph(data=data, user=current_user)

@graph_router.get('/get_graphs', response_model=List[GraphOut])
async def get_graphs():
    graphs = await GraphService.get_graph_by_name("")
    if not graphs:
        raise HTTPException(status_code=404, detail="No graphs found")
    return graphs

@graph_router.get('/get_graph/{graph_id}', response_model=GraphOut)
async def get_graph(graph_id: UUID):
    graph = await GraphService.get_graph_by_id(str(graph_id))
    if not graph:
        raise HTTPException(status_code=404, detail="Graph not found")
    return graph

@graph_router.put('/update_graph/{graph_id}', response_model=GraphOut)
async def update_graph(graph_id: UUID, graph_update: GraphUpdate):
    updated_graph = await GraphService.update_graph(str(graph_id), graph_update)
    if not updated_graph:
        raise HTTPException(status_code=404, detail="Graph not found")
    return updated_graph

@graph_router.delete('/delete_graph/{graph_id}', response_model=dict)
async def delete_graph(graph_id: UUID):
    deleted = await GraphService.delete_graph(str(graph_id))
    if not deleted:
        raise HTTPException(status_code=404, detail="Graph not found")
    return {"message": "Graph deleted successfully"}
