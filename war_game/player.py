# Now need a class to represent each player in the game to keep track of their cards and how many wins
class Player:
    def __init__(self, name):
        self.wins = 0 
        self.card = None
        self.name = name
