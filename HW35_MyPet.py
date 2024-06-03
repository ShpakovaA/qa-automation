
"""
    Tamagotchi: can create pets that have favourite food and toy, feed, pat them and play fetch

"""
class MyPet:

    def __init__(self, animal, name, favourite_toy: str, favourite_food: str, energetic=True):
        self.animal = animal
        self.name = name
        self.favourite_toy = favourite_toy
        self.favourite_food = favourite_food
        self.energetic = energetic

    def feed(self, food: str):
        """
        Feeds pet
        :param food: food to feed
        :return: pet's impression of the food
        """
        if food.lower() == self.favourite_food.lower():
            print("Mmmm...Yum")
        else:
            print("yucks....")

    def play_fetch(self):
        """
        Pet fetches favourite toy
        makes animal tired, pet doesn't play if tired
        """
        if self.energetic:
            print(f"{self.name} goes after the {self.favourite_toy}")
            self._change_energy_level()
        else:
            print("Tired! Let's sleep")

    def sleep(self):
        """
        Puts pet to sleep, makes pet energetic
        """
        print("shhh! Your pet is sleeping")
        self._change_energy_level()

    def buy_new_toy(self, new_toy):
        self.favourite_toy = new_toy

    def _change_energy_level(self):
        if self.energetic:
            self.energetic = False
        else:
            self.energetic = True
    @staticmethod
    def pat_the_pet():
        print("Pet is happy!!!")


lota = MyPet("Dog", "Lota", "ball", "cheese")
lota.feed("Lemon")
lota.play_fetch()
lota.buy_new_toy("Teddy Bear")
lota.play_fetch()
lota.sleep()
lota.play_fetch()
lota.pat_the_pet()




