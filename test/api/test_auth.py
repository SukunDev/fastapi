

def test_register_success(client):
    response = client.post("/api/register", json={
        "name": "John Doe",
        "email": "john@example.com",
        "password": "123456"
    })
    assert response.status_code == 201
    assert response.json()["status"] is True
    assert response.json()["data"]["email"] == "john@example.com"

def test_login_success(client):
    # Register first
    client.post("/api/register", json={
        "name": "Jane Doe",
        "email": "jane@example.com",
        "password": "654321"
    })
    # Login
    response = client.post("/api/login", json={
        "email": "jane@example.com",
        "password": "654321"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()["data"]
