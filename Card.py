from dataclasses import dataclass


@dataclass  # equivalent to lombok @Data in Java
class Card:
    number: int
    symbol: str

    def __repr__(self):
        return f'{self.number}{self.symbol}'
