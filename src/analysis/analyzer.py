import matplotlib.pyplot as plt

class CollatzAnalyzer:
    def __init__(self, start_value: int = None):
        self.start_value = start_value
        self.sequence_data = {}

    def analyze_sequence(self, n: int) -> dict:
        if n in self.sequence_data:
            return self.sequence_data[n]
        original_n = n
        steps = 0
        cycle_detected = False
        sequence = []
        seen = set()
        while True:
            if n in seen:
                cycle_detected = True
                break
            sequence.append(n)
            seen.add(n)
            steps += 1
            n = n // 2 if n % 2 == 0 else 3 * n + 1
        self.sequence_data[original_n] = {
            'steps': steps,
            'cycle_detected': cycle_detected,
            'sequence': sequence
        }
        return self.sequence_data[original_n]

    def detect_cycle(self, n: int) -> bool:
        data = self.analyze_sequence(n)
        return data['cycle_detected']

    def binary_representation(self, n: int) -> str:
        return bin(n)[2:]

    def analyze_binary(self, n: int):
        return self.binary_representation(n)

    def generate_sequence(self, n: int) -> list:
        return self.analyze_sequence(n)['sequence']

    def analyze_statistics(self, sequence: list) -> dict:
        return {
            'max': max(sequence),
            'min': min(sequence),
            'average': sum(sequence) / len(sequence)
        }

    def visualize_sequence(self, sequence: list):
        """
        Zeigt die Collatz-Folge in einem interaktiven Tkinter-Fenster an.
        Mit NavigationToolbar2Tk sind Zoom/Pan-Funktionen verfügbar.
        """
        import tkinter as tk
        from matplotlib.figure import Figure
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

        window = tk.Toplevel()
        window.title(f"Graph: Collatz-Folge für {sequence[0]}")

        fig = Figure(figsize=(10, 6))
        ax = fig.add_subplot(111)
        ax.plot(sequence, marker='o')
        ax.set_title(f"Collatz-Folge beginnend mit {sequence[0]}")
        ax.set_xlabel("Index")
        ax.set_ylabel("Wert")
        ax.grid(True)

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Neuen separaten Frame für die Toolbar erstellen
        toolbar_frame = tk.Frame(window)
        toolbar_frame.pack(side=tk.TOP, fill=tk.X)
        toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
        toolbar.update()

    def analyze(self):
        if self.start_value is None:
            raise ValueError("Kein Startwert für die Analyse angegeben.")
        data = self.analyze_sequence(self.start_value)
        stats = self.analyze_statistics(data['sequence'])
        print(f"Sequence for {self.start_value}: {data['sequence']}")
        print(f"Steps: {data['steps']}")
        print(f"Cycle detected: {data['cycle_detected']}")
        print(f"Statistics: {stats}")
        self.visualize_sequence(data['sequence'])

    def prove_collatz_conjecture(self, limit: int):
        """
        Überprüft die Collatz-Vermutung für alle Zahlen von 1 bis limit.
        Gibt für jede Zahl die Sequenz, die Anzahl der Schritte,
        ob ein Zyklus detektiert wurde und Statistiken aus.
        """
        for n in range(1, limit + 1):
            data = self.analyze_sequence(n)
            stats = self.analyze_statistics(data["sequence"])
            print(f"Startwert: {n}")
            print(f"  Sequenz: {data['sequence']}")
            print(f"  Schritte: {data['steps']}")
            print(f"  Zyklus erkannt: {data['cycle_detected']}")
            print(f"  Statistiken: {stats}\n")
        print(f"Die Collatz-Vermutung wurde für alle Zahlen von 1 bis {limit} überprüft.")