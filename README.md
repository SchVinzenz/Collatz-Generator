# Collatz-Generator
An interactive Python program for exploring the Collatz Conjecture. The tool enables you to analyze and simulate Collatz sequences, and to experiment with symbolic methods using sympy. It features an intuitive graphical user interface.

## Overview

The Collatz Tool allows users to:
- **Analyze:** Generate and visualize the Collatz sequence for a chosen starting value. The interactive window supports zoom and pan functionalities.
- **Simulate:** Display the Collatz sequence as text in a dialog box.
- **Proof:** Perform a simple hypothesis test (e.g., verifying n == 1) and present the sequence in a designated results window.
- **Alternative Approaches:** Use sympy to present a symbolic expression of the Collatz mapping (experimental and not a full proof).
- **Settings:** Adjust the UI language (based on a selection of the world’s 10 most-spoken languages), choose a background color, and modify the font size.

## System Requirements

- Python 3.6 or higher
- Dependencies:
  - `tkinter` (typically included with Python; may need installation on some systems)
  - `matplotlib`
  - `sympy`
  - Other standard packages (like `threading`)

## Installation and Usage

1. **Clone the Repository** or download the project folder.
2. **Install Dependencies:**  
   Run:
   ```bash
   pip install matplotlib sympy
   ```
3. **Run the Program:**  
   In your terminal, navigate to the project folder and execute:
   ```bash
   python3 src/main.py
   ```
   The GUI will open with options for analysis, simulation, proof, and exit.
4. **Adjust Settings:**  
   Use the gear icon in the bottom left to open the settings window to change language, color, and font size. The question mark icon in the bottom right shows the alternative symbolic proof approach.

## Packaging as a macOS App

To package the program as a native macOS application (a .app), you can use [py2app](https://py2app.readthedocs.io/):
1. Install `py2app`:
   ```bash
   pip install py2app
   ```
2. Create a `setup.py` file (see example code in the project).
3. Run the following command in the project folder:
   ```bash
   python setup.py py2app
   ```
4. The resulting .app will be located in the `dist` folder.

## Project Structure

- **src/main.py:** The main program (GUI) with options for analysis, simulation, proof, alternative approaches, and settings.
- **src/analysis/analyzer.py:** Contains the `CollatzAnalyzer` class that generates, analyzes, and visualizes the Collatz sequence (including zoom/pan functionality via Matplotlib).
- **src/proofs/prover.py:** Provides simple proof functions to perform the hypothesis test (e.g., verifying that n == 1).
- **setup.py:** The packaging script for py2app to create a macOS application.
- **README.md:** This documentation.

## Additional Notes

- The translation of the user interface is provided as an example. For a complete language switch, all UI text should be dynamically adapted to the chosen language.
- The color selection is now handled via a color chooser, eliminating the need to manually enter hex codes.
- Experimental approaches (such as the alternative proof using sympy) demonstrate how Python can be used for symbolic computation—even though a full mathematical proof requires more advanced systems.

## Summary

This repository serves as a lightweight and educational platform for experimenting with the Collatz Conjecture, combining visualization, simulation, and customizable interface features.