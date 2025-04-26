

def test_get_users(auth_client):
    client = auth_client["client"]
    token = auth_client["token"]

    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/api/users/", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json()["data"], list)

def test_create_and_get_user(auth_client):
    client = auth_client["client"]
    token = auth_client["token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Create another user
    response = client.post("/api/register", json={
        "name": "New User",
        "email": "newuser@example.com",
        "password": "password123"
    })
    assert response.status_code == 201

    # Get users
    response = client.get("/api/users/", headers=headers)
    assert response.status_code == 200
    data = response.json()["data"]
    assert any(user["email"] == "newuser@example.com" for user in data)

def test_update_user(auth_client):
    client = auth_client["client"]
    token = auth_client["token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Get my user_id first
    response = client.get("/api/users/", headers=headers)
    user_id = response.json()["data"][0]["id"]

    # Update
    response = client.put(f"/api/users/{user_id}", headers=headers, json={
        "name": "Updated Name"
    })
    assert response.status_code == 200
    assert response.json()["data"]["name"] == "Updated Name"

def test_delete_user(auth_client):
    client = auth_client["client"]
    token = auth_client["token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Create user to delete
    response = client.post("/api/register", json={
        "name": "Delete Me",
        "email": "deleteme@example.com",
        "password": "deleteme"
    })
    response = client.get("/api/users/", headers=headers)
    users = response.json()["data"]
    user_id = next(u["id"] for u in users if u["email"] == "deleteme@example.com")

    # Delete
    response = client.delete(f"/api/users/{user_id}", headers=headers)
    assert response.status_code == 200
    assert response.json()["data"]["id"] == user_id
