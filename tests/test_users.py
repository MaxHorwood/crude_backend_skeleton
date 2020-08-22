from http import HTTPStatus
from app.data_types import User, Address


def test_create_user(client):
    # Create a User and POST a User.
    user = User(5, "Max", "max@max.com", Address("A Road", "XX1 1XX"))

    res = client.post("/users", json=user.to_dict())
    assert res.status_code == HTTPStatus.CREATED

    user_res = User.from_dict(res.json)
    assert user_res == user


def test_get_user(client):
    res = client.get("/users")
    assert res.status_code == HTTPStatus.OK

    users = [User.from_dict(user) for user in res.json]
    assert len(users) == 3  # TODO: Don't carry over from the other test

    res = client.get("/user/1")
    assert res.status_code == HTTPStatus.OK
    user = User.from_dict(res.json)
    assert user.id == 1


def test_delete_user(client):
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
