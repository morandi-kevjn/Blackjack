# blackjack

import random

class Deck:

    def __init__(self):
        # self. makes variable cards accessible in the class
        self.cards = []
        suits = ['spades', 'clubs', 'hearts', 'diamonds']
        ranks = [
            {'rank': 'A', 'value': 11},
            {'rank': '2', 'value': 2},
            {'rank': '3', 'value': 3},
            {'rank': '4', 'value': 4},
            {'rank': '5', 'value': 5},
            {'rank': '6', 'value': 6},
            {'rank': '7', 'value': 7},
            {'rank': '8', 'value': 8},
            {'rank': '9', 'value': 9},
            {'rank': '10', 'value': 10},
            {'rank': 'J', 'value': 10},
            {'rank': 'Q', 'value': 10},
            {'rank': 'K', 'value': 10}
        ]

        # this will create the cards in order
        for suit in suits:
            for rank in ranks:
                self.cards.append([suit, rank])

    # this will shuffle cards, and we will create a function of this
    def shuffle(self):
        # shuffle only if cards is greater than one
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    # def deal()
    def deal(self, number):
        cards_dealt = []
        for x in range(number):
            # remove a card only if there is at least one card in the deck
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)

        return cards_dealt


deck1 = Deck()
deck2 = Deck()
deck2.shuffle()

print(deck1.cards)
print(deck2.cards)
