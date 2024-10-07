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
