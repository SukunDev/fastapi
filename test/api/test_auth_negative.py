
def test_register_duplicate_email(client):
    client.post("/api/register", json={
        "name": "John Doe",
        "email": "duplicate@example.com",
        "password": "123456"
    })

    response = client.post("/api/register", json={
        "name": "John Clone",
        "email": "duplicate@example.com",
        "password": "654321"
    })
    assert response.status_code == 400
    assert response.json()["status"] is True
    assert response.json()["error"] == "Email is already registered"

def test_login_nonexistent_email(client):
    response = client.post("/api/login", json={
        "email": "nonexistent@example.com",
        "password": "password123"
    })
    assert response.status_code == 401
    assert response.json()["status"] is True
    assert response.json()["error"] == "Invalid credentials"

def test_login_wrong_password(client):
    client.post("/api/register", json={
        "name": "Jane Doe",
        "email": "janedoe@example.com",
        "password": "correctpassword"
    })

    response = client.post("/api/login", json={
        "email": "janedoe@example.com",
        "password": "wrongpassword"
    })
    assert response.status_code == 401
    assert response.json()["status"] is True
    assert response.json()["error"] == "Invalid credentials"
