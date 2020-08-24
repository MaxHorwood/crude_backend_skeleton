from http import HTTPStatus


DUMMY_USER = {
    "name": "Max",
    "email": "max@max.com",
    "addresses": [{"address": "A Road", "postcode": "XX1 1XX"}],
}


def test_create_user(client):
    # Create a User and POST a User.
    res = client.post("/users", json=DUMMY_USER)
    assert res.status_code == HTTPStatus.CREATED

    user = res.json
    assert user["id"] == 1
    assert user["name"] == DUMMY_USER["name"]
    assert user["email"] == DUMMY_USER["email"]
    assert user["addresses"] == DUMMY_USER["addresses"]


def test_get_user(client):
    res = client.post("/users", json=DUMMY_USER)
    assert res.status_code == HTTPStatus.CREATED

    res = client.get("/users")
    assert res.status_code == HTTPStatus.OK
    assert len(res.json) == 1

    res = client.get("/user/1")
    assert res.status_code == HTTPStatus.OK
    assert res.json["id"] == 1


def test_delete_user(client):
    res = client.post("/users", json=DUMMY_USER)
    assert res.status_code == HTTPStatus.CREATED

    res = client.get("/user/1")
    assert res.status_code == HTTPStatus.OK

    res = client.delete("/user/1")
    assert res.status_code == HTTPStatus.OK

    # Try and delete again
    res = client.delete("/user/1")
    assert res.status_code == HTTPStatus.BAD_REQUEST

    # Try and get the deleted user
    res = client.get("/user/1")
    assert res.status_code == HTTPStatus.NOT_FOUND
