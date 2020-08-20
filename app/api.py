from http import HTTPStatus
from typing import Dict

from .data_types import User, Address
from .server_responses import bad_request_error, server_error

USERS = [
    User(0, "User 1", "User@user.com", Address("1 Something Road", "OX11 1ES")),
    User(1, "User 2", "User2@user.com", Address("2 Something Road", "OX11 1ES")),
]


def find_user(id: int) -> User:
    for user in USERS:
        if user.id == id:
            return user
    return None


def add_user(user: User):
    USERS.append(user)


def remove_user(user_id: int):
    for user in USERS:
        if user.id == user_id:
            USERS.remove(user)
            return True
    return False


def get_users():
    return [user.to_dict() for user in USERS], HTTPStatus.OK


def get_user(id: int):
    user = find_user(id)
    if not user:
        return {"message": f"User with id `{id}` not found"}, 404
    return user.to_dict(), HTTPStatus.OK


def create_user(user_data: Dict):
    user = User.from_dict(user_data)
    if not user:
        return bad_request_error(f"Error adding user: {user_data}")
    add_user(user)
    return user.to_dict(), HTTPStatus.CREATED


def delete_user(id: int):
    if remove_user(id):
        return {"message": f"Deleted user `{id}`"}, HTTPStatus.OK
    return {"message": f"Failed to deleted user `{id}`"}, HTTPStatus.BAD_REQUES
