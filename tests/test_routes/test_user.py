def test_create_user(client):
    data = {"name":"testuser","password":"testing123","email":"testuser@nofoobar.com"}
    response = client.post("/users",json=data)
    assert response.status_code == 201
    assert response.json()["email"] == "testuser@nofoobar.com"