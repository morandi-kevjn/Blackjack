# blackjack

import random

cards = []
suits = ['spades', 'clubs', 'hearts', 'diamonds']
# ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
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

"""
suit = 'hearts'
rank = 'K'
value = 10
"""

# print('Your card is: ' + rank + ' of ' + suit)

# suits.append('snakes')

# this will create the cards in order
for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])

# this will shuffle cards and we will create a function of this
def shuffle():
    random.shuffle(cards)

# def deal()
def deal(number):
    cards_dealt = []
    for x in range(number):
        card = cards.pop()
        cards_dealt.append(card)

    return cards_dealt

# print(cards)

# how to have one card
# card = cards.pop()
# print(card)

shuffle()
# print(cards)

"""
cards_dealt = deal(2)
card = cards_dealt[0]
rank = card[1]

print(card)

if rank == 'A':
    value = 11
elif rank == 'J' or rank == 'Q' or rank == 'K':
    value = 10
else:
    value = rank

rank_dict = {'rank': rank, 'value': value}

print(rank_dict['rank'], rank_dict['value'])
"""

card = deal(1)[0]

# print(card)
print(card[1]['value'])
