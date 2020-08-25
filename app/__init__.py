import os
import yaml
import connexion

from dataclasses_jsonschema import SchemaType
from flask_migrate import Migrate

from .data_types import BaseType
from .config import configurations
from .models import db

BASE_PATH = os.path.dirname(os.path.abspath(__file__))


def load_api_spec(spec_file: str):
    with open(os.path.join(BASE_PATH, spec_file), "r") as f:
        spec = yaml.full_load(f.read())
        spec["components"]["schemas"].update(BaseType.all_json_schemas(schema_type=SchemaType.SWAGGER_V3))
    return spec


migrate = Migrate()


def create_app(testing: bool = False):
    app = connexion.FlaskApp(__name__, specification_dir="./", options={"swagger_ui": True})
    app.add_api(load_api_spec("my_api.yaml"))

    flask_app = app.app
    if testing:
        config_str = "test"
    else:
        config_str = "dev"
    flask_app.config.from_object(configurations[config_str])

    db.init_app(flask_app)
    migrate.init_app(flask_app, db)

    return flask_app
