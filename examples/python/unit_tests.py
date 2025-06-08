import pytest
from fastapi.testclient import TestClient
from main import app, users

client = TestClient(app)

def test_get_all_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert len(response.json()) == len(users)
    assert response.json()[0]["name"] == "Alice"
    assert response.json()[1]["name"] == "Bob"

def test_get_user_exists():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Alice"
    assert response.json()["email"] == "alice@example.com"

def test_get_user_not_found():
    response = client.get("/users/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

def test_create_user():
    new_user = {"name": "Charlie", "email": "charlie@example.com"}
    response = client.post("/users", json=new_user)
    assert response.status_code == 201
    assert response.json()["name"] == new_user["name"]
    assert response.json()["email"] == new_user["email"]
    assert "id" in response.json()

def test_create_user_invalid_data():
    # Missing required email field
    new_user = {"name": "David"}
    response = client.post("/users", json=new_user)
    assert response.status_code == 422  # Validation error

def test_update_user_complete():
    update_data = {"name": "Alice Smith", "email": "alice.smith@example.com"}
    response = client.put("/users/1", json=update_data)
    assert response.status_code == 200
    assert response.json()["name"] == update_data["name"]
    assert response.json()["email"] == update_data["email"]
    assert response.json()["id"] == 1

def test_update_user_not_found():
    update_data = {"name": "Nobody", "email": "nobody@example.com"}
    response = client.put("/users/999", json=update_data)
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

def test_partial_update_user():
    # Only update email
    update_data = {"email": "bob.new@example.com"}
    response = client.patch("/users/2", json=update_data)
    assert response.status_code == 200
    assert response.json()["email"] == update_data["email"]
    assert response.json()["name"] == "Bob"  # Name should remain unchanged
    assert response.json()["id"] == 2

def test_partial_update_user_not_found():
    update_data = {"name": "Nobody"}
    response = client.patch("/users/999", json=update_data)
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

def test_delete_user():
    # First make sure the user exists
    get_response = client.get("/users/1")
    assert get_response.status_code == 200
    
    # Then delete the user
    response = client.delete("/users/1")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "deleted successfully" in response.json()["message"]
    
    # Verify the user is gone
    get_response_after = client.get("/users/1")
    assert get_response_after.status_code == 404

def test_delete_user_not_found():
    response = client.delete("/users/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"