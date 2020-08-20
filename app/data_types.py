from dataclasses import dataclass
from dataclasses_jsonschema import JsonSchemaMixin


@dataclass
class BaseType(JsonSchemaMixin):
    pass


@dataclass
class Address(BaseType):
    address: str
    postcode: str


@dataclass
class User(BaseType):
    id: int
    name: str
    email: str
    address: Address
