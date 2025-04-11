# Collatz-Generator 🚀
Ein interaktives Python-Programm zur Erforschung der Collatz-Vermutung. Das Tool ermöglicht es dir, Collatz-Sequenzen zu analysieren, zu simulieren und mit symbolischen Methoden (mithilfe von sympy) zu experimentieren. Es bietet eine intuitive grafische Benutzeroberfläche. 🎨

## Überblick 🌟

Das Collatz-Tool erlaubt dir:
- **Analyse:** Generiere und visualisiere die Collatz-Sequenz für einen gewählten Startwert. Das interaktive Fenster unterstützt Zoom- und Schwenkfunktionen. 🔍
- **Simulation:** Zeige die Collatz-Sequenz als Text in einem Dialogfenster an. 📝
- **Beweis:** Führe einen einfachen Hypothesentest durch (z. B. Überprüfung, ob n == 1) und präsentiere die Sequenz in einem speziellen Ergebnisfenster. ✅
- **Alternative Ansätze:** Nutze sympy, um einen symbolischen Ausdruck der Collatz-Abbildung darzustellen (experimentell und kein vollständiger Beweis). 🧪
- **Einstellungen:** Passe die Sprache der Benutzeroberfläche an (basierend auf einer Auswahl der 10 meistgesprochenen Sprachen weltweit), wähle eine Hintergrundfarbe und ändere die Schriftgröße. 🌈

## Systemanforderungen 🖥️

- Python 3.6 oder höher
- Abhängigkeiten:
  - `tkinter` (normalerweise in Python enthalten; muss auf einigen Systemen installiert werden)
  - `matplotlib`
  - `sympy`
  - Weitere Standardpakete (wie `threading`)

## Installation und Nutzung 📥

1. **Repository klonen** oder den Projektordner herunterladen.
2. **Abhängigkeiten installieren:**  
   Führe aus:
   ```bash
   pip install matplotlib sympy
   ```
3. **Programm ausführen:**  
   Navigiere im Terminal zum Projektordner und führe aus:
   ```bash
   python3 src/main.py
   ```
   Die GUI öffnet sich mit Optionen für Analyse, Simulation, Beweis und Beenden. 🖱️
4. **Einstellungen anpassen:**  
   Nutze das Zahnrad-Symbol unten links, um das Einstellungsfenster zu öffnen und Sprache, Farbe und Schriftgröße zu ändern. Das Fragezeichen-Symbol unten rechts zeigt den alternativen symbolischen Beweisansatz an. ⚙️❓

## Verpackung als macOS-App 🍎

Um das Programm als native macOS-Anwendung (.app) zu verpacken, kannst du [py2app](https://py2app.readthedocs.io/) verwenden:
1. Installiere `py2app`:
   ```bash
   pip install py2app
   ```
2. Erstelle eine `setup.py`-Datei (siehe Beispielcode im Projekt).
3. Führe den folgenden Befehl im Projektordner aus:
   ```bash
   python setup.py py2app
   ```
4. Die resultierende .app befindet sich im `dist`-Ordner. 📂

## Projektstruktur 📂

- **src/main.py:** Das Hauptprogramm (GUI) mit Optionen für Analyse, Simulation, Beweis, alternative Ansätze und Einstellungen.
- **src/analysis/analyzer.py:** Enthält die Klasse `CollatzAnalyzer`, die die Collatz-Sequenz generiert, analysiert und visualisiert (einschließlich Zoom-/Schwenkfunktionalität über Matplotlib).
- **src/proofs/prover.py:** Bietet einfache Beweisfunktionen, um den Hypothesentest durchzuführen (z. B. Überprüfung, ob n == 1).
- **setup.py:** Das Verpackungsskript für py2app, um eine macOS-Anwendung zu erstellen.
- **README.md:** Diese Dokumentation. 📖

## Zusätzliche Hinweise 📝

- Die Übersetzung der Benutzeroberfläche wird als Beispiel bereitgestellt. Für einen vollständigen Sprachwechsel sollten alle UI-Texte dynamisch an die gewählte Sprache angepasst werden. 🌍
- Die Farbauswahl wird jetzt über einen Farbwähler gehandhabt, sodass keine Hex-Codes manuell eingegeben werden müssen. 🎨
- Experimentelle Ansätze (wie der alternative Beweis mit sympy) zeigen, wie Python für symbolische Berechnungen verwendet werden kann – auch wenn ein vollständiger mathematischer Beweis fortgeschrittenere Systeme erfordert. 🧠

## Zusammenfassung 🏁

Dieses Repository dient als leichtgewichtige und lehrreiche Plattform, um mit der Collatz-Vermutung zu experimentieren. Es kombiniert Visualisierung, Simulation und anpassbare Schnittstellenfunktionen. Viel Spaß beim Erkunden! 🎉