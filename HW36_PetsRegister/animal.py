"""Implements classes related to animals"""

from enum import Enum
import datetime
class AnimalType(Enum):
    Dog = 1
    Cat = 2
    Fish = 3
    Parrot = 4


class Color(Enum):
    BLACK = 1
    WHITE = 2
    RED = 3
    SPOTTED = 4
    GRAY = 5
    GREEN = 6


class Animal:

    def __init__(self, year: int, type: AnimalType, color: Color):
        self.year = year
        self.type = type
        self.color = color

    @property
    def age(self):
        return f"{datetime.datetime.now().year - self.year} years"

    def get_type(self):
        return self.type

    def get_color(self):
        return self.color






