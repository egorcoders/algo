from enum import Enum, auto
from datetime import datetime


class LowerEnum(Enum):
    def __str__(self):
        return self.name.capitalize()


class Weekdays(LowerEnum):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()


for day in Weekdays:
    if datetime.now().isoweekday() == day.value:
        print('That is your day!')
    else:
        print(f'Today is {day}')


