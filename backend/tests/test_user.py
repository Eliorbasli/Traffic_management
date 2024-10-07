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
    
    
# Test User Login Endpoint
def test_login_user(clear_test_data):
    client.post("/api/v1/auth/create", json=mock_user)
    
    login_data = {
        "username": mock_user["username"],
        "password": mock_user["password"]
    }
    
    response = client.post("/api/v1/auth/login", json=login_data)
    
    assert response.status_code == 200
    
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data

def test_invalied_login(clear_data):
    # Attempt login with incorrect password
    login_data = {
        "username": mock_user["username"],
        "password": mock_user["password"]
    }
    
    response = client.post("/api/v1/auth/login", json=login_data)
    
    assert response.status_code == 401
    
    data = response.json()
    assert data["detail"] == "Incorrect username or password"
    
def test_duplicate_user_creation(clear_test_data):
    client.post("/api/v1/auth/create" , json=mock_user)

    response = client.post("/api/v1/auth/create", json=mock_user)
    
    assert response.status_code == 400
    
    data = response.json()
    assert data["detail"] == "User with this username or email alreay exists"
    
    
def test_missing_fields_user_creation(clear_data):
    incomplete_user = {
        "username": "newuser",
        "email": "newuser@example.com"
        # Missing "password"
    }
    
    response = client.get("/api/v1/auth/create" , json=incomplete_user)
    
    assert response.status_code == 422
    
    data = response.json()
    assert data["detail"][0]["msg"] == "field required"
    
    incomplete_user = {
        "username": "newuser",
        "password": "newpassword123"
        # Missing "email"
    }
    
    response = client.post("/api/v1/auth/create", json=incomplete_user)
    
    assert response.status_code == 422, f"Expected 422, got {response.status_code}"
    
    data = response.json()
    assert data["detail"][0]["msg"] == "field required", "Error message for missing email field does not match"

    incomplete_user = {
        "email": "newuser@example.com",
        "password": "newpassword123"
        # Missing "username"
    }
    
    response = client.post("/api/v1/auth/create", json=incomplete_user)
    
    assert response.status_code == 422, f"Expected 422, got {response.status_code}"
    
    data = response.json()
    assert data["detail"][0]["msg"] == "field required", "Error message for missing username field does not match"

