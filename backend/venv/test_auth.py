from integration_test import client



def test_signup_success(client):
    response = client.post("/signup", json={
        "username": "user1",
        "password": "pass1"
    })
    assert response.status_code == 200

def test_login_success(client):
    client.post("/signup", json={
        "username": "user1",
        "password": "pass1"
    })
    response = client.post("/login", json={"username":"user1", "password":"pass1"})

    assert response.status_code == 200
    assert "access_token" in response.json()