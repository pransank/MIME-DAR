"""
Temperature conversion utilities.
"""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert a temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius: float) -> float:
    """Convert a temperature from Celsius to Kelvin."""
    return celsius + 273.15


if __name__ == "__main__":
    print(celsius_to_fahrenheit(100))
    print(fahrenheit_to_celsius(212))
