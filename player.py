class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def __str__(self):
        return self.name
