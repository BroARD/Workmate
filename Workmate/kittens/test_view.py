import requests

BASE_URL = "http://localhost:8000/api"


def test_get_breeds():
    response = requests.get(f"{BASE_URL}/breeds")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_kittens():
    response = requests.get(f"{BASE_URL}/kittens")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_kittens_by_breed():
    breed = "Майн-Кун"
    response = requests.get(f"{BASE_URL}/kittens?breed={breed}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_kitten_details():
    kitten_id = 1
    response = requests.get(f"{BASE_URL}/kittens/{kitten_id}")
    assert response.status_code == 200
    assert "color" in response.json()
    assert "age" in response.json()
    assert "description" in response.json()


def test_add_kitten():
    data = {
        "color": "black",
        "age": 3,
        "description": "Cute black kitten"
    }
    response = requests.post(f"{BASE_URL}/kittens", json=data)
    assert response.status_code == 201
    assert response.json()["color"] == data["color"]


def test_update_kitten():
    kitten_id = 1
    data = {
        "color": "white",
        "age": 4,
        "description": "Updated description"
    }
    response = requests.put(f"{BASE_URL}/kittens/{kitten_id}", json=data)
    assert response.status_code == 200
    assert response.json()["color"] == data["color"]


def test_delete_kitten():
    kitten_id = 1
    response = requests.delete(f"{BASE_URL}/kittens/{kitten_id}")
    assert response.status_code == 204


def test_jwt_authorization():
    credentials = {
        "username": "admin",
        "password": "admin"
    }
    # Получение токена
    token_response = requests.post(f"{BASE_URL}/token", json=credentials)
    assert token_response.status_code == 200
