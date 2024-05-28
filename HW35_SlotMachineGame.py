import random

"""
  Slot machine game
"""
class SlotMachineGame:

    def __init__(self, balance: int, is_member=None, free_game=True):
        self.balance = balance
        self.is_member = is_member
        self.__free_game = free_game

    WIN = 1000000
    GAME_FEE = 50

    def _spin(self):
        """
                Game fee deducts from balance,
                if two random numbers match it's a win, balance increases with the WIN amount
        """
        self.balance -= SlotMachineGame.GAME_FEE
        if random.random() == random.random():
            self.balance += SlotMachineGame.WIN
            print(f"You won {SlotMachineGame.WIN}!!! Your budget now is {self.balance}!!!")
        else:
            print("You lost! Try again!")

    def play(self):
        """
        If balance amount is sufficient game starts, if not - top up is required
        Members are allowed to play once for free if broke
        """
        if self.balance >= SlotMachineGame.GAME_FEE:
            self._spin()

        else:
            if self.is_member and self.__free_game:
                print("You are broke! But members get one game free")
                self._spin()
                self.__free_game = False

            else:
                print("Please, top up")

    def top_up(self, amount: int):
        self.balance += amount

    @classmethod
    def change_game_fee(cls, new_fee):
        cls.GAME_FEE = new_fee


play = SlotMachineGame(20, True)
play.play()
play.play()

play2 = SlotMachineGame(20)
play2.play()
play2.top_up(100)
play2.play()


