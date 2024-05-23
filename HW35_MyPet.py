
"""
    Tamagotchi: can create pets that have favourite food and toy, feed them and play fetch

"""
class MyPet:

    FAVOURITE_TOY = "ball"
    FAVOURITE_FOOD = "cheese"
    ENERGETIC = True
    def __init__(self, animal, name):
        self.animal = animal
        self.name = name

    def feed(self, food: str):
        """
        Feeds pet
        :param food: food to feed
        :return: pet's impression of the food
        """
        if food.lower() == MyPet.FAVOURITE_FOOD:
            print("Mmmm...Yum")
        else:
            print("yucks....")

    def play_fetch(self):
        """
        Pet fetches favourite toy
        :return: makes animal tired, pet doesn't play if tired
        """
        if MyPet.ENERGETIC:
            print(f"{self.name} goes after the {MyPet.FAVOURITE_TOY}")
            MyPet._change_energy_level()
        else:
            print("Tired! Let's sleep")

    @staticmethod
    def sleep():
        """
        Puts pet to sleep
        :return: make pet energetic
        """
        print("shhh! Your pet is sleeping")
        MyPet._change_energy_level()

    @classmethod
    def change_favourite_toy(cls, new_favourite_toy):
        MyPet.FAVOURITE_TOY = new_favourite_toy

    @classmethod
    def _change_energy_level(cls):
        if MyPet.ENERGETIC:
            MyPet.ENERGETIC = False
        else:
            MyPet.ENERGETIC = True


lota = MyPet("Dog", "Lota")
lota.feed("Lemon")
lota.play_fetch()
MyPet.change_favourite_toy("Teddy Bear")
lota.play_fetch()
lota.sleep()
lota.play_fetch()





