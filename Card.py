from dataclasses import dataclass

PICTURE_NUMBERS = ['J', 'Q', 'K']
NUMBERS = [str(n) for n in range(2, 11)] + PICTURE_NUMBERS + ['A']
SYMBOLS = ['♣', '♦', '♥', '♠']


@dataclass
class Card:
    number: str
    symbol: str

    def __repr__(self):
        return f'{self.number}{self.symbol}'
