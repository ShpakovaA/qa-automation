"""This module contains base class Owner for Pets Registry System"""
import random


class Owner:

    def __init__(self, name):
        self.name = name
        self.id = random.randint(1000, 9999)

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    @property
    def owner_info(self):
        return f"Owner info: {self.name}, id: {self.id}"


