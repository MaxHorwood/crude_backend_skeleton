from http import HTTPStatus
from typing import Dict

import app.data_types as dt
from .server_responses import bad_request_error, make_response
from app.models import db, User, Address


def add_user(user: dt.User) -> User:
    user_model = User(name=user.name, email=user.email)
    db.session.add(user_model)
    db.session.flush()
    for address in user.addresses:
        address_model = Address(postcode=address.postcode, address=address.address, user_id=user_model.id)
        db.session.add(address_model)
    db.session.commit()
    return user_model


def get_users():
    users = db.session.query(User).all()
    return [dt.User.from_object(user) for user in users], HTTPStatus.OK


def get_user(id: int):
    user = db.session.query(User).filter(User.id == id).one_or_none()
    if not user:
        return make_response(f"User with id `{id}` not found", HTTPStatus.NOT_FOUND)
    return dt.User.from_object(user), HTTPStatus.OK


def create_user(user_data: Dict):
    user = dt.User.from_dict(user_data)
    if not user:
        return bad_request_error(f"Error adding user: {user_data}")
    user_model = add_user(user)
    return dt.User.from_object(user_model), HTTPStatus.CREATED


def delete_user(id: int):
    user = db.session.query(User).filter(User.id == id).one_or_none()
    if user:
        db.session.delete(user)
        db.session.commit()
        return make_response(f"Deleted user `{id}`", HTTPStatus.OK)
    return make_response(f"Failed to deleted user `{id}`", HTTPStatus.BAD_REQUEST)
