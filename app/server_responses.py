from http import HTTPStatus
from connexion.problem import problem


def _mk_response(message: str, status_code: int):
    return {"message": message}, status_code


def bad_request_error(message: str):
    return problem(HTTPStatus.BAD_REQUEST, "BAD_REQUEST", message)


def server_error(message: str):
    return problem(500, "SERVER_ERROR", message)
