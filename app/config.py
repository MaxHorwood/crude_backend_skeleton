import os


class BaseConfig(object):
    DEBUG: bool = False
    TESTING: bool = False
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

    # Override and set any variables that are in the environment
    # TODO: Any issues with actually do this? (Loading vars that we don't want)
    def __init__(self):
        for attr in dir(self):
            if attr.startswith("__"):
                continue
            value = os.environ.get(attr)
            if value:
                setattr(self, attr, value)
            else:
                setattr(self, attr, getattr(self, attr))


class DevelopmentConfig(BaseConfig):
    DEBUG: bool = True
    TESTING: bool = True
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = True
    SQLALCHEMY_DATABASE_URI: str = "postgres://postgres:max@localhost/dev_db"


class TestingConfig(BaseConfig):
    TESTING: bool = True
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///:memory:"


class ProdConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI: str = ""


configurations = {
    "dev": DevelopmentConfig,
    "test": TestingConfig,
    "prod": ProdConfig,
}
