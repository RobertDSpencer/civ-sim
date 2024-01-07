class Biome:
    def __init__(self, name="empty") -> None:
        self.name = name
        if self.name == "empty":
            self.symbol = "X"
        else:
            self.symbol = ""