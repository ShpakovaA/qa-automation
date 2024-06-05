"""Example of PetRegister usage"""

from owner import Owner
from pet import Pet
from animal import Color, AnimalType
from registration import PetsRegistrator

# creating owners
owner1 = Owner("Sam Adams")
owner2 = Owner("Jeck Brown")
owner3 = Owner("Oliver Smith")

# creating pets
pet1 = Pet(2022, type=AnimalType.Dog, color=Color.WHITE, name="Lota", owner=owner1)
pet2 = Pet(2019, type=AnimalType.Cat, color=Color.SPOTTED, name="Nolla", owner=owner3)
pet3 = Pet(2020, type=AnimalType.Parrot, color=Color.GREEN, name="Rio", owner=owner1)
pet4 = Pet(2017, type=AnimalType.Fish, color=Color.RED, name="Dorry", owner=owner2)

#registration flow

#show empty registry
print(PetsRegistrator.show_registered_animals())
print()

#register pets
PetsRegistrator.register_new_pet(pet1)
PetsRegistrator.register_new_pet(pet2)
PetsRegistrator.register_new_pet(pet3)
PetsRegistrator.register_new_pet(pet4)
print(PetsRegistrator.show_registered_animals())
print()

#try to register already existing pet
PetsRegistrator.register_new_pet(pet2)
print()

#show info about registered pet
print(PetsRegistrator.show_pet_info("Rio"))
print(PetsRegistrator.show_pet_info("Lota"))
print(PetsRegistrator.show_pet_info("Pop"))

