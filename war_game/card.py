# Class modeling playing cards
class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]
    # class variables
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "king", "Ace"]
    # The values list has none at index zero and one so that the numbers in the list match their index
    def __init__(self, v, s):
        """ suit + value are ints """
        self.value = v
        self.suit = s
    
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        else:
            return False
    
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        else:
            return False
    
    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v