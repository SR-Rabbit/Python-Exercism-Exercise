"""Functions to help you cook and bake a gorgeous lasagna"""

EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculates the remaining time left (in minutes) to bake the lasagna.

    Args:
        elapsed_bake_time (int): The time that the lasagna has been in the oven.

    Returns:
        int: Time remaining (in minutes) to finish baking the lasagna.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers:int) -> int:
    """Calculates the time it would take (in minutes) to make a lasagna of N layers.

    Args:
        number_of_layers (int): The number of layers desired for the lasagna.

    Returns:
        int: Total preparation time (in minutes) to make a lasagna of N layers.
    """
    return number_of_layers * 2


def elapsed_time_in_minutes(number_of_layers:int, elapsed_bake_time: int) -> int:
    """Calculates the total number of minute's spent preparing and cooking the lasagna.

    Args:
        number_of_layers (int): Number of layers the lasagna has.
        elapsed_bake_time (int): How long (in minute) the lasagna has been baking for in the oven.

    Returns:
        int: Total elapsed time spent cooking the lasagna.
    """
    return bake_time_remaining(elapsed_bake_time) + preparation_time_in_minutes(number_of_layers)
