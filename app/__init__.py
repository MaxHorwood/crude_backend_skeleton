import os
import yaml
import connexion

from http import HTTPStatus
from dataclasses_jsonschema import SchemaType

from .data_types import BaseType


BASE_PATH = os.path.dirname(os.path.abspath(__file__))


def load_api_spec(spec_file: str):
    with open(os.path.join(BASE_PATH, spec_file), "r") as f:
        spec = yaml.full_load(f.read())
        spec["components"]["schemas"].update(BaseType.all_json_schemas(schema_type=SchemaType.SWAGGER_V3))
    return spec


def create_app():
    app = connexion.FlaskApp(__name__, specification_dir="./", options={"swagger_ui": True})
    app.add_api(load_api_spec("my_api.yaml"))
    app.add_error_handler(HTTPStatus.BAD_REQUEST, lambda x: {"message": f"Bad Request {x}"})

    return app.app
