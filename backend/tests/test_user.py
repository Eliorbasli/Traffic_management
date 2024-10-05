import pytest
from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app)

mock_user ={
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "testpassword123",
}

@pytest.fixture
def clear_data():
    """
    Fixture to clear test data after each test run.
    (Optional: depends on how you want to clean your database or mock objects)
    """
    yield
    
def test_create_user(clear_test_data):
    response = client.post('/api/v1/auth/create', json=mock_user)
    
    assert response.status_code == 201
    
    data = response.json()
    assert "user_id" in data
    assert data["username"] == mock_user["username"]
    assert data["email"] == mock_user["email"]
    assert "user_id" in data
    