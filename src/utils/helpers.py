def collatz_sequence(n):
    """Generates the Collatz sequence for a given starting number n."""
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def is_power_of_two(n):
    """Checks if a number is a power of two."""
    return (n > 0) and (n & (n - 1)) == 0

def format_sequence(sequence):
    """Formats the Collatz sequence into a readable string."""
    return ' -> '.join(map(str, sequence))

def display_intro() -> None:
    """
    Zeigt die Einführungsnachricht für das Collatz Tool an.
    """
    print("Willkommen zum Collatz Conjecture Research Tool!")

def some_helper_function(x: int) -> int:
    """
    Beispiel-Hilfsfunktion, die den übergebenen Wert quadriert.
    """
    return x * x