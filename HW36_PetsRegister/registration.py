from __future__ import annotations

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
        result = {}
        for k, v in PetsRegistrator.__pets_registry.items():
            if pet_name in v:
                result[k] = v
        if result:
            return result
        else:
            return "The pet hasn't been registered"

    @staticmethod
    def delete_pet_record(pet_name, owner_name):
        for k, v in PetsRegistrator.__pets_registry.items():
            if pet_name in v and str(v).find(owner_name):
                del PetsRegistrator.__pets_registry[k]
                break


    @staticmethod
    def show_registered_animals():
        result = {}
        for k, v in PetsRegistrator.__pets_registry.items():
            result[k] = v
        return result

    @staticmethod
    def show_registered_animals_number():
        return len(PetsRegistrator.__pets_registry)

    @staticmethod
    def update_pet_info(pet: Pet):
        PetsRegistrator.delete_pet_record(pet.name, str(pet.owner))
        PetsRegistrator.register_new_pet(pet)


