"""This module contains class Pet that inherits Animal class"""

from animal import Animal
from animal import AnimalType
from animal import Color
from owner import Owner


class Pet(Animal):
    def __init__(self, year: int, type: AnimalType, color: Color, name: str, owner: Owner):
        super().__init__(year, type, color)
        self.name = name
        self._owner = owner
    @property
    def _info(self):
        return self.name, self.age,  self.type, self.color, self.owner.owner_info

    @property
    def owner(self):
        return self._owner


    def change_owner(self, owner: Owner):
        self._owner = owner


