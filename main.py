# blackjack

import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank["rank"]} of {self.suit}'
        # return self.rank['rank'] + ' of ' + self.suit


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
                self.cards.append(Card(suit, rank))

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


card1 = Card('hearts', {'rank': 'J', 'value': 10})
print(card1)
