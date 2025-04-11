# Collatz-Generator 🚀
An interactive Python program for exploring the Collatz conjecture. This tool allows you to analyze, simulate, and experiment with Collatz sequences using symbolic methods (via sympy). It features an intuitive graphical user interface. 🎨

## Overview 🌟

The Collatz tool enables you to:
- **Analysis:** Generate and visualize the Collatz sequence for a chosen starting value. The interactive window supports zoom and pan functions. 🔍
- **Simulation:** Display the Collatz sequence as text in a dialog window. 📝
- **Proof:** Perform a simple hypothesis test (e.g., checking if n == 1) and present the sequence in a dedicated results window. ✅
- **Alternative Approaches:** Use sympy to represent a symbolic expression of the Collatz mapping (experimental and not a complete proof). 🧪
- **Settings:** Adjust the user interface language (based on a selection of the 10 most spoken languages worldwide), choose a background color, and change the font size. 🌈

## System Requirements 🖥️

- Python 3.6 or higher
- Dependencies:
  - `tkinter` (usually included with Python; may need to be installed on some systems)
  - `matplotlib`
  - `sympy`
  - Other standard packages (like `threading`)

## Installation and Usage 📥

1. **Clone the repository** or download the project folder.
2. **Install dependencies:**  
   Run:
   ```bash
   pip install matplotlib sympy
   ```
3. **Run the program:**  
   Navigate to the project folder in the terminal and run:
   ```bash
   python3 src/main.py
   ```
   The GUI will open with options for analysis, simulation, proof, and exit. 🖱️
4. **Adjust settings:**  
   Use the gear icon in the bottom left to open the settings window and change language, color, and font size. The question mark icon in the bottom right shows the alternative symbolic proof approach. ⚙️❓

## Packaging as a macOS App 🍎

To package the program as a native macOS application (.app), you can use [py2app](https://py2app.readthedocs.io/):
1. Install `py2app`:
   ```bash
   pip install py2app
   ```
2. Create a `setup.py` file (see example code in the project).
3. Run the following command in the project folder:
   ```bash
   python setup.py py2app
   ```
4. The resulting .app will be located in the `dist` folder. 📂

## Project Structure 📂

- **src/main.py:** The main program (GUI) with options for analysis, simulation, proof, alternative approaches, and settings.
- **src/analysis/analyzer.py:** Contains the `CollatzAnalyzer` class, which generates, analyzes, and visualizes the Collatz sequence (including zoom/pan functionality via Matplotlib).
- **src/proofs/prover.py:** Provides simple proof functions to perform hypothesis tests (e.g., checking if n == 1).
- **setup.py:** The packaging script for py2app to create a macOS application.
- **README.md:** This documentation. 📖

## Additional Notes 📝

- The user interface translation is provided as an example. For a complete language switch, all UI texts should be dynamically adjusted to the selected language. 🌍
- The color selection is now handled via a color picker, so no manual input of hex codes is required. 🎨
- Experimental approaches (like the alternative proof with sympy) demonstrate how Python can be used for symbolic computations – even though a complete mathematical proof requires more advanced systems. 🧠

## Summary 🏁

This repository serves as a lightweight and educational platform to experiment with the Collatz conjecture. It combines visualization, simulation, and customizable interface features. Have fun exploring! 🎉