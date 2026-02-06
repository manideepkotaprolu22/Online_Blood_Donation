from integration_test import client


def test_register_donor_success(client):
    client.post("/signup", json={
        "username": "donor",
        "password": "pass"
    })

    login = client.post("/login", json={
        "username": "donor",
        "password": "pass"
    })

    token = login.json()["access_token"]

    response = client.post(
        "/donor/register",
        json={
            "name": "John",
            "age": 30,
            "gender": "Male",
            "blood_group": "O+",
            "city": "Dallas",
            "phone_number": 9999999999
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200


def test_get_donors(client):
    response = client.get("/donors")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
