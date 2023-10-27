import json
import uuid
from enum import Enum, auto
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field, EmailStr


class Weekdays(Enum):
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"


class Event(BaseModel):
    day: Weekdays = Field()
    is_holiday: Optional[bool]


event1 = Event(**{'day': Weekdays.MONDAY, 'is_holiday': True})
event2 = Event(day=Weekdays.WEDNESDAY, is_holiday=False)
event3 = Event(day=Weekdays.FRIDAY, is_holiday=None)  # No holiday information

events = [event1, event2, event3]

print([e.model_dump_json(by_alias=True) for e in events])


class User(BaseModel):
    id: int
    name: str
    email: EmailStr
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