from dataclasses import dataclass
from dataclasses_jsonschema import JsonSchemaMixin, FieldEncoder
from typing import List, Optional, NewType

Postcode = NewType("Postcode", str)
Email = NewType("Email", str)


class PostcodeField(FieldEncoder):
    @property
    def json_schema(self):
        return {"type": "string", "pattern": r"[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][A-Z]{2}"}


class EmailField(FieldEncoder):
    @property
    def json_schema(self):
        return {"type": "string", "pattern": r"[^@]+@[^@]+\.[^@]+"}


JsonSchemaMixin.register_field_encoders({Postcode: PostcodeField(), Email: EmailField()})


@dataclass
class BaseType(JsonSchemaMixin):
    pass


@dataclass
class Address(BaseType):
    address: str
    postcode: Postcode


@dataclass
class User(BaseType):
    name: str
    email: Email
    addresses: List[Address]
    id: Optional[int] = None
