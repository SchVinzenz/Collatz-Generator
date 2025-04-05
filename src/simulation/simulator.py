class CollatzSequence:
    def __init__(self, start_value: int = None):
        self.start_value = start_value

    def generate_sequence(self) -> list:
        if self.start_value is None or self.start_value < 1:
            raise ValueError("Starting value must be a positive integer")
        sequence = []
        n = self.start_value
        while n != 1:
            sequence.append(n)
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
        sequence.append(1)
        return sequence

    # Neue Methode generate für Kompatibilität mit main.py und Tests
    def generate(self, start_value: int = None) -> list:
        if start_value is not None:
            self.start_value = start_value
        return self.generate_sequence()