def is_criticality_balanced(temperature: int, neutrons: int) -> bool:
    """Takes 2 parameters and returns a boolean for if the reactor is in criticality or not.

    Args:
        temperature (int): The temperature of the nuclear reactor in Kelvin.
        neutrons (int): Number of neutrons emitted per second.

    Returns:
        bool: Returns True if:
        1. Temperature is less than 800,
        2. Number of neutrons emitted is greater than 500,
        3. Product of temperature and neutrons is less than 500,000.
        Else return False.
    """
    return temperature < 800 and neutrons > 500 and (temperature * neutrons) < 500000


def reactor_efficiency(voltage: int, current: int, theory_max_power: int) -> str:
    """Takes 3 parameters and determines the power efficiency of the reactor.

    Args:
        voltage (int): Voltage output from the reactor.
        current (int): The current of the electricity.
        theory_max_power (int): Theoretical max power output the reactor can achieve.

    Returns:
        str: "Green", "Orange", "Red" or "Black" depending on the power efficiency.
    """
    efficiency = ((voltage * current) / theory_max_power) * 100
    if efficiency > 80:
        return "Green"
    if efficiency >= 60:
        return "Orange"
    return "Red" if efficiency >= 30 else "Black"


def fail_safe(temperature: int, neutrons: int, threshold: int) -> str:
    """Takes 3 parameters and determines the status of the reactor.

    Args:
        temperature (int): The temperature of the nuclear reactor in Kelvin.
        neutrons (int): Number of neutrons emitted per second.
        threshold (int): The threshold of the reactor.

    Returns:
        str: "LOW", "NORMAL", or "DANGER" depending on the status.
    """
    output_ratio = (temperature * neutrons)/threshold
    if output_ratio < 0.9:
        return "LOW"
    return "NORMAL" if output_ratio <= 1.1 else "DANGER"
    