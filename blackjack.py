from time import sleep

from Deck import Deck
from Hand import Hand

# TODO: create a player class that will have a deck, and a money variable
deck = Deck.random_deck()
player_hand = Hand.from_deck(deck)
dealer_hand = Hand.from_deck(deck)


def main():
    print(f'Your starting hand is: {player_hand}')
    print(f"The dealer's hand is: [{dealer_hand.cards[0]}, ?]")
    print()

    if player_hand.is_blackjack() or dealer_hand.is_blackjack():
        print_who_won()
        return

    # handle the player's actions
    while not player_hand.is_bust() and not player_hand.is_blackjack():

        match input('Hit or Stand?').lower():
            case 'hit' | 'h':
                new_card = deck.draw_card_to(player_hand)

                print(f'Drawn a {new_card}!')
                print(f'Your new hand: {player_hand}')
                print()

            case _:
                print()
                break

    if player_hand.is_bust() or player_hand.is_blackjack():
        print_who_won()
        return

    # the dealer draws cards until his hand's worth >= 17
    while dealer_hand.value < 17:
        print(f"The dealer's hand is worth {dealer_hand.value}, drawing a card..")
        deck.draw_card_to(dealer_hand)
        sleep(1.2)

    print(f"The dealer's hand is: {dealer_hand}")
    print()
    print_who_won()


def print_who_won():
    if player_hand.is_blackjack():
        print('You got a Blackjack and WON!')

    elif player_hand.is_bust():
        print(f'You lost because your hand is worth {player_hand.value}.')

    elif dealer_hand.is_blackjack():
        print(f'You lost because the dealer got a BlackJack! {dealer_hand}.')

    elif dealer_hand.is_bust():
        print(f'You won because the dealer busted!')

    elif dealer_hand.value == player_hand.value:
        print(f'Draw! Both you and the dealer are worth {player_hand.value}!')

    elif dealer_hand.value > player_hand.value:
        print(f"You lost because your hand is worth {player_hand.value} and the dealer's worth {dealer_hand.value}.")

    elif player_hand.value > dealer_hand.value:
        print(f'You won because you had more points({player_hand.value}) than the dealer({dealer_hand.value}).')


if __name__ == '__main__':
    main()
