card_values = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 1,
}


def value_of_card(card: str) -> int:
    """Takes 1 argument, and returns the value of the card.

    Args:
        card (str): The card's number or face.

    Returns:
        int: The value assigned to the number or card face.
    """
    return card_values[card]


def higher_card(card_one: str, card_two: str) -> str or tuple:
    """Takes 2 arguments, and returns the card of higher value, or both if they have equal value.

    Args:
        card_one (str): Number or face of card one.
        card_two (str): Number or face of card two.

    Returns:
        str or tuple: The card of higher value, or both cards if they have equal value.
    """
    if card_values[card_one] == card_values[card_two]:
        return card_one, card_two
    return card_one if card_values[card_one] > card_values[card_two] else card_two


def value_of_ace(card_one: str, card_two: str) -> int:
    """Takes 2 arguments, and determines the value of the ace ("A") card.

    Args:
        card_one (str): Number or face of card one.
        card_two (str): Number or face of card two.

    Returns:
        int: The value of the ace ("A"), either 1 or 11.
    """
    if card_one == "A" or card_two == "A":
        return 11
    return 11 if (card_values[card_one] + card_values[card_two]) <= 10 else 1


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Takes 2 arguments, and determines if the first 2 cards dealt is a natural or blackjack.

    Args:
        card_one (str): Number or face of card one.
        card_two (str): Number or face of card two.

    Returns:
        bool: True if the first 2 cards adds up to 21, else False.
    """
    card_values["A"] = value_of_ace(card_one, card_two)
    return card_values[card_one] + card_values[card_two] == 21


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Takes 2 arguments, and determines if first 2 card can be split.

    Args:
        card_one (str): Number or face of card one.
        card_two (str): Number or face of card two.

    Returns:
        bool: True if first 2 cards have the same value, else False.
    """
    return card_values[card_one] == card_values[card_two]


def can_double_down(card_one: str, card_two: str) -> bool:
    """Takes 2 arguments, and determines if the player can "double down".

    Args:
        card_one (str): Number or face of card one.
        card_two (str): Number or face of card two.

    Returns:
        bool: True if the first 2 cards have a total value of 9, 10, or 11, else False.
    """
    return card_values[card_one] + card_values[card_two] in [9, 10, 11]
