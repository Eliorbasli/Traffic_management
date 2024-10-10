import pytest
from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app)

mock_graph = {
    "name": "Test Graph",
    "nodes": ["A", "B", "C"],
    "edges": {
        "A": [["B", 1], ["C", 2]],
        "B": [["C", 3]],
        "C": [["A", 4]]
    }
}

@pytest.fixture
def clear_test_data():
    """
    Fixture to clear test data after each test run.
    (Optional: depends on how you want to clean your database or mock objects)
    """
    yield


def test_create_graph(clear_test_data):
    response = client.post("/api/v1/graph/create", json=mock_graph)
    
    assert response.status_code == 201
    
    data = response.json()
    assert "graph_id" in data
    assert data["name"] == mock_graph["name"]
    assert data["nodes"] == mock_graph["nodes"]
    assert data["edges"] == mock_graph["edges"]

def test_get_graph_by_id(clear_test_data):
    create_response = client.post("/api/v1/graph/create" , json=mock_graph)
    graph_id = create_response.json()["graph_id"]
    
    get_response = client.post(f"/api/v1/graph/{graph_id}")
    
    assert get_response.status_code == 200
    
    data = get_response.json()
    assert data["graph_id"] == graph_id
    assert data["name"] == mock_graph["name"]
    assert data["nodes"] == mock_graph["nodes"]
    assert data["edges"] == mock_graph["edges"]
    

def test_create_graph_missing_fields(clear_test_data):
    incomplete_graph = {
        "name" : "Incomplete Graph",
        "edges": {
            "A" :[["B" , 1] , ["C" , 2]]
        }
    }
    
    response = client.post("/api/v1/graph/create", json=incomplete_graph)
    
    assert response.status_code == 422
    
    data = response.json()
    assert data["detail"][0]["msg"] == "field required"
    
    # Missing name field
    incomplete_graph = {
        "nodes" : ["A" , "B"],
        "edges": {
            "A" :[["B" , 1] , ["C" , 2]]
        }
    }
    
    response = client.post("/api/v1/graph/create", json=incomplete_graph)
    
    assert response.status_code == 422
    
    data = response.json()
    assert data["detail"][0]["msg"] == "field required"
    
    
def test_duplication_graph_creation(clear_test_data):
    pass