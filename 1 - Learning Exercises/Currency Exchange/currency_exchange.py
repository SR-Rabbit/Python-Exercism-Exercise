def exchange_money(budget: float, exchange_rate: float) -> float:
    """Takes two parameters and returns the value of the exchanged currency.

    Args:
        budget (float): The amount planned to be exchanged.
        exchange_rate (float): The value of one currency equal to one unit of foreign currency.

    Returns:
        float: The value of the exchanged currency.
    """
    return budget / exchange_rate


def get_change(budget: float, exchanging_value: float) -> float:
    """Takes two parameters and returns the amount of money that is left from the budget.

    Args:
        budget (float): The amount of money before exchange.
        exchanging_value (float): The amount is that taken from the budget to be exchanged.

    Returns:
        float: The amount that is left from the budget.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """Takes two parameters and returns the total value of the bills received from the exchange.

    Args:
        denomination (int): The value of a single bill or unit.
        number_of_bills (int): The number of bills you received from the exchange.

    Returns:
        int: The total value of the bills received from the exchange.
    """
    return int(denomination * number_of_bills)


def get_number_of_bills(budget: float, denomination: int) -> int:
    """Takes two parameters and returns the number of bills that can be exchanged within the budget.

    Args:
        budget (float): The amount planned to be exchanged.
        denomination (int): The value of a single bill or unit.

    Returns:
        int: The number of bills that can be exchanged within the budget.
    """
    return int(budget // denomination)


def get_leftover_of_bills(budget: float, denomination: int) -> float:
    """Takes two parameters and returns the remainder or leftover amount that cannot be exchanged.

    Args:
        budget (float): The amount planned to be exchanged.
        denomination (int): The value of a single bill or unit.

    Returns:
        float: The amount or remainder that is leftover that cannot be exchanged from the budget.
    """
    return budget % denomination


def exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination: int) -> int:
    """Takes four parameters and returns maximum value received after exchange rate and spread.

    Args:
        budget (float): The amount planned to be exchanged.
        exchange_rate (float): The value of one currency equal to one unit of foreign currency.
        spread (int): Percentage taken as an exchange fee.
        denomination (int): The value of a single bill or unit.

    Returns:
        int: The maximum value after calculating the exchange rate and spread.
    """
    new_exchange_rate = exchange_rate + (exchange_rate * (spread / 100))
    budget_converted = budget / new_exchange_rate
    remainder_amount = budget_converted % denomination
    return int(budget_converted - remainder_amount)

    # [Alternatively in one line]
    # return int((budget / (exchange_rate + (exchange_rate * (spread / 100))) // denomination* denomination))
