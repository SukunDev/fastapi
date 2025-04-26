

def test_get_user_not_found(auth_client):
    client = auth_client["client"]
    token = auth_client["token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.get("/api/users/9999", headers=headers)
    assert response.status_code == 404
    assert response.json()["status"] is True
    assert response.json()["error"] == "User not found"

def test_update_user_not_found(auth_client):
    client = auth_client["client"]
    token = auth_client["token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.put("/api/users/9999", headers=headers, json={
        "name": "Ghost User"
    })
    assert response.status_code == 404
    assert response.json()["status"] is True
    assert response.json()["error"] == "User not found"

def test_delete_user_not_found(auth_client):
    client = auth_client["client"]
    token = auth_client["token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.delete("/api/users/9999", headers=headers)
    assert response.status_code == 404
    assert response.json()["status"] is True
    assert response.json()["error"] == "User not found"
