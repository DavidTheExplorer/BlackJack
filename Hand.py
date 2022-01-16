from constants import PICTURE_NUMBERS


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    @classmethod
    def from_deck(cls, deck):
        hand = cls()

        # draw 2 cards from the deck
        for _ in range(2):
            deck.draw_card_to(hand)

        return hand

    def add_card(self, card):
        self.cards.append(card)
        self.value += self.get_card_value(card)

    def is_blackjack(self):
        return self.value == 21

    def is_bust(self):
        return self.value > 21

    def get_card_value(self, card):
        number = card.number

        if number.isdigit():
            return int(number)

        if number in PICTURE_NUMBERS:
            return 10

        if number == 'A':
            return 11 if self.value <= 10 else 1

        raise ValueError(f'The specified card number({number}) is not a part of Blackjack!')

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        cards_str = ', '.join([str(card) for card in self.cards])

        return f'[{cards_str}] (worth {self.value})'
