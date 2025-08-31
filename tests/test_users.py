from app import schemas
from .database import client, session

    
def test_root(client):
    response = client.get("/")
    print(response.json().get("message"))
    assert response.status_code == 200
    assert response.json().get("message") == "Hello Sam!!!!!!!"
    assert response.status_code == 200

def test_create_user(client):
    response = client.post("/users/", json={"email": "sam11223@gmail.com", "password": "password"})
    new_user =schemas.UserOut(**response.json())
    assert new_user.email == "sam11223@gmail.com"
    assert response.status_code == 201
    # assert response.json().get)