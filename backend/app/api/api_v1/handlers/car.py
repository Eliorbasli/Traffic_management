from fastapi import APIRouter, HTTPException
from app.models.car_model import Car
from app.models.graph_model import Graph
import heapq

car_router = APIRouter()

@car_router.post("/find_shortest_path")
async def find_shortest_path(car: Car , grap_id: str):
    graph = await Graph.get(grap_id)
    if not graph:
        return HTTPException(status_code=404 , detail="Graph not found")
    
    # Dijkstra's algo to find the shortest path
    def dijkstra(start, end):
        distances = {node: float('infinity') for node in graph.nodes}
        distances[start] = 0 
        priority_queue = [(0,start)]
        path = {start: []}
        
        while priority_queue:
            current_distnace , current_node = heapq.heappop(priority_queue)
            
            if current_distnace > distances[current_node]:
                continue
            
            for neighbor , distance in graph.edegs.get(current_node , []):
                new_distnace = current_node + distance
                
                if new_distnace < distances[neighbor]:
                    distances[neighbor] = new_distnace
                    heapq.heappush(priority_queue , (new_distnace , neighbor))
                    path[neighbor] = path[current_node] + [neighbor]
                    
        return path.get(end , [])

    find_shortest_path = dijkstra(car.start_point, car.end_point)
    return { "path" : find_shortest_path}
