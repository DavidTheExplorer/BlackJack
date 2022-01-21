import random

from Card import Card, NUMBERS, SYMBOLS


class Deck:

    def __init__(self):
        self.cards = list(Card(number, symbol) for symbol in SYMBOLS for number in NUMBERS)

    @classmethod
    def random_deck(cls):
        deck = cls()
        deck.shuffle()

        return deck

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card_to(self, hand):
        card = self.cards.pop()
        hand.add_card(card)
        return card

