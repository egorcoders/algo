import json
import uuid
from typing import List
from uuid import UUID

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str
    balance: int


class UserUUID(BaseModel):
    id: UUID
    name: str
    email: str
    balance: int


class UserGroup(BaseModel):
    id: int
    name: str
    users: List[User]


with open('./data2.json', 'r') as json_data:
    users = [User(**d) for d in json.load(json_data)]

u1 = users[0]
u2 = users[1]

u_group = {
    "id": 2,
    "name": "Chloe Cooper",
    "users": [u1, u2]
}

user_data = {
    "id": uuid.uuid4(),
    "name": "John Doe St.",
    "email": "alice@example.com",
    "balance": 1000
}

u_uuid = UserUUID(**user_data)
print(u_uuid)

print(UserGroup(**u_group).model_dump_json())