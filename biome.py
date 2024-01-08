from colorama import Fore
class Biome:
    def __init__(self, name="empty") -> None:
        self.name = name
        # the effects of a biome are Type, Fertility, and Hostility
        # Type is a string (e.g. arid, forested, aquatic)
        # Fertility is a decimal number that will change the growth rate multiplicitavely (e.g. 0.5, 1.5, 2.0)
        # Hostility is a number that will decrease the population linearly (e.g. 50, 10, 5)
        if self.name == "empty":
            self.symbol = "X"
            self.fertility = 0
            self.hostility = 0
        elif self.name == "plain":
            self.symbol = Fore.GREEN + "#"
            self.fertility = 1
            self.hostility = 0
        else:
            self.symbol = ""
            self.fertility = 0
            self.hostility = 0
    
    def __str__(self) -> str:
        return self.symbol