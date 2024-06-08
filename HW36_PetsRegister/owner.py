"""This module contains base class Owner for Pets Registry System"""
import random


class Owner:
    def __init__(self, name):
        self.name = name
        self._id = random.randint(1000, 9999)

    @property
    def id(self):
        return self._id

    def get_name(self):
        return self.name

    @property
    def owner_info(self):
        return f"Owner info: {self.name}, id: {self._id}"


