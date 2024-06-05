from pet import Pet
import random


class PetsRegistrator:
    __pets_registry = {}

    @staticmethod
    def register_new_pet(pet: Pet):
        pet_id = random.randint(1000, 9999)
        if pet._info in PetsRegistrator.__pets_registry.values():
            print("Pet is already registered")
        else:
            PetsRegistrator.__pets_registry[pet_id] =pet._info

    @staticmethod
    def show_pet_info(pet_name):
        for k, v in PetsRegistrator.__pets_registry.items():
            if pet_name in v:
                return k, v
            else:
                return "The pet hasn't been registered"

    @staticmethod
    def show_registered_animals():
        for i in PetsRegistrator.__pets_registry.items():
            print(i)
