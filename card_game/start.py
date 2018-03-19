import random

NUMBER_OF_PLAYERS = 2
POINTS_PER_TURN = 2


def create_deck():
    """ This is a simple deck without suits
    so i choose to use only fourteen cards.
    """
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    random.shuffle(deck)
    return deck


def deal_out(deck, cards_to_deal=None):
    # if not cards_to_deal:
    #     cards_to_deal = int(len(deck) / 2)

    return deck[cards_to_deal:], deck[:cards_to_deal]


def player_turn_over(hand):
    hand.sort()
    return hand.pop()


def first_player_win(first_player_card, second_player_card):
    return first_player_card > second_player_card


def second_player_win(first_player_card, second_player_card):
    return first_player_card < second_player_card


def is_game_over(first_player_hand, second_player_hand):
    return (
        len(first_player_hand) == 0 and
        len(second_player_hand) == 0
    )


def get_winner(first_player_score, second_player_score):
    if first_player_score > second_player_score:
        return 'first'

    elif first_player_score < second_player_score:
        return 'second'

    return 'draw game'


def run():
    print('Starting a new game')
    game_is_running = True
    first_player_score = 0
    second_player_score = 0
    deck = create_deck()

    cards_to_deal = int(len(deck) / NUMBER_OF_PLAYERS)
    first_player_hand, second_player_hand = deal_out(
        deck=deck,
        cards_to_deal=cards_to_deal
    )

    while game_is_running:
        first_player_higher_card = player_turn_over(hand=first_player_hand)
        second_player_higher_card = player_turn_over(hand=second_player_hand)

        if first_player_win(
            first_player_card=first_player_higher_card,
            second_player_card=second_player_higher_card
        ):
            first_player_score += POINTS_PER_TURN

        elif second_player_win(
            first_player_card=first_player_higher_card,
            second_player_card=second_player_higher_card
        ):
            second_player_score += POINTS_PER_TURN

        if is_game_over(
            first_player_hand=first_player_hand,
            second_player_hand=second_player_hand
        ):
            game_is_running = False

    print(
        'The winner is: {winner}'.format(
            winner=get_winner(first_player_score, second_player_score)
        )
    )


if __name__ == '__main__':
    run()
