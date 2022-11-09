def eat_ghost(power_pellet: bool, touching_ghost: bool) -> bool:
    """Takes 2 arguments to determine if Pac-Man can eat a ghost.

    Args:
        power_pellet (bool): True if Power Pellet is active, else False.
        touching_ghost (bool): True if Pac-Man is touching a ghost, else False.

    Returns:
        bool: Returns a True if power_pellet AND touching_ghost are True, else returns False.
    """
    return power_pellet and touching_ghost


def score(touching_power_pellet: bool, touching_dot: bool) -> bool:
    """Takes 2 arguments and determines if Pac-Man earned a score point.

    Args:
        touching_power_pellet (bool): True if Pac-Man is touching a Power Pellet, else False.
        touching_dot (bool): True if Pac-Man is touching a dot, else False.

    Returns:
        bool: Returns True power_pellet AND/OR touching dot is True, else returns False.
    """
    return touching_power_pellet or touching_dot


def lose(power_pellet: bool, touching_ghost: bool) -> bool:
    """Takes 2 arguments and determines if Pac-Man loses or not.

    Args:
        power_pellet (bool): True if Power Pellet is active, else False.
        touching_ghost (bool): True if Pac-Man is touching a ghost, else False.

    Returns:
        bool: Returns True if Pac-Man touches a ghost but Power Pellet is False, else returns False.
    """
    return not power_pellet and touching_ghost


def win(eaten_all_dots: bool, power_pellet: bool, touching_ghost: bool) -> bool:
    """Takes 3 arguments and determines if Pac-Man wins or not.

    Args:
        eaten_all_dots (bool): True if Pac-Man has eaten all the dots, else False.
        power_pellet (bool): True if Power Pellet is active, else False.
        touching_ghost (bool): True if Pac-Man is touching a ghost, else False.

    Returns:
        bool: Returns True if eaten_all_dots is True and touching_ghost is False, else returns False.
        If power_pellet is True while touching_ghost is True, then return True.
    """
    return eaten_all_dots and not lose(power_pellet, touching_ghost)
