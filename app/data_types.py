from dataclasses import dataclass
from dataclasses_jsonschema import JsonSchemaMixin
from typing import List, Optional


@dataclass
class BaseType(JsonSchemaMixin):
    pass


@dataclass
class Address(BaseType):
    address: str
    postcode: str


@dataclass
class User(BaseType):
    name: str
    email: str
    addresses: List[Address]
    id: Optional[int] = None
