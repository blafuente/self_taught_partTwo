from random import shuffle
from card import Card

class Deck:
    def __init__(self):
        # Creates card objects representing all the cards in the 52 card deck
        self.cards = []
        for i in range(2,15): # Picks value of card
            for j in range(4): # Picks suit of card
                self.cards.append(Card(i,j))
            shuffle(self.cards)
    # Removes and returns a card from the cards list or returns none
    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

# deck = Deck()
# for card in deck.cards:
#     print(card)