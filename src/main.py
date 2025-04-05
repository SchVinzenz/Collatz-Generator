import sys
import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext
from tkinter import ttk  # Neu: ttk für modernere Widgets
import threading
from analysis.analyzer import CollatzAnalyzer
from simulation.simulator import CollatzSequence
from proofs.prover import Prover
from utils.helpers import display_intro
import tkinter.colorchooser as colorchooser

def settings_callback():
    settings_win = tk.Toplevel()
    settings_win.title("Settings")
    settings_win.geometry("400x300")
    
    # Beispieloption: Sprachauswahl (Top 10 Sprachen)
    lang_label = ttk.Label(settings_win, text="Language:")
    lang_label.pack(pady=(20, 5))
    languages = ["Mandarin Chinese", "Spanish", "English", "Hindi", "Arabic",
                 "Bengali", "Portuguese", "Russian", "Japanese", "Punjabi"]
    lang_var = tk.StringVar(value=languages[2])  # Standard: English
    lang_menu = ttk.Combobox(settings_win, textvariable=lang_var, values=languages, state="readonly")
    lang_menu.pack(pady=5)
    
    # Übersetzungs-Dictionary (Beispiel: es funktioniert nur exemplarisch)
    translations = {
        "Mandarin Chinese": {"Analyze": "分析柯拉兹数列", "Simulate": "模拟柯拉兹数列", "Prove": "证明柯拉兹猜想", "Exit": "退出"},
        "Spanish": {"Analyze": "Analizar Secuencia de Collatz", "Simulate": "Simular Secuencia de Collatz", "Prove": "Probar conjetura de Collatz", "Exit": "Salir"},
        "English": {"Analyze": "Analyze Collatz Sequence", "Simulate": "Simulate Collatz Sequence", "Prove": "Prove Collatz Conjecture", "Exit": "Exit"},
        "Hindi": {"Analyze": "कोलैट्ज़ अनुक्रम विश्लेषण", "Simulate": "कोलैट्ज़ अनुक्रम सिमुलेट करें", "Prove": "कोलैट्ज़ अनुमान साबित करें", "Exit": "बाहर"},
        "Arabic": {"Analyze": "تحليل سلسلة كولاتز", "Simulate": "محاكاة سلسلة كولاتز", "Prove": "إثبات فرضية كولاتز", "Exit": "خروج"},
        "Bengali": {"Analyze": "কলাটজ সিকোয়েন্স বিশ্লেষণ", "Simulate": "কলাটজ সিকোয়েন্স অনুকরণ", "Prove": "কলাটজ অনুমান প্রমাণ", "Exit": "প্রস্থান"},
        "Portuguese": {"Analyze": "Analisar Sequência Collatz", "Simulate": "Simular Sequência Collatz", "Prove": "Provar Conjectura de Collatz", "Exit": "Sair"},
        "Russian": {"Analyze": "Анализ последовательности Коллатца", "Simulate": "Симуляция последовательности Коллатца", "Prove": "Доказать гипотезу Коллатца", "Exit": "Выход"},
        "Japanese": {"Analyze": "コラッツ数列を解析", "Simulate": "コラッツ数列をシミュレート", "Prove": "コラッツ予想を証明", "Exit": "終了"},
        "Punjabi": {"Analyze": "ਕੋਲੈਟਜ਼ ਕ੍ਰਮ ਵਿਸ਼ਲੇਸ਼ਣ", "Simulate": "ਕੋਲੈਟਜ਼ ਕ੍ਰਮ ਸਿਮੂਲੇਟ ਕਰੋ", "Prove": "ਕੋਲੈਟਜ਼ ਉਮੀਦ ਸਾਬਤ ਕਰੋ", "Exit": "ਬਾਹਰ"}
    }
    
    # Beispieloption: Hintergrundfarbe – hier per Farbauswahl
    color_label = ttk.Label(settings_win, text="Background Color:")
    color_label.pack(pady=(20, 5))
    color_var = tk.StringVar(value="#f0f0f0")
    def choose_color():
        chosen = colorchooser.askcolor(initialcolor=color_var.get())
        if chosen[1]:
            color_var.set(chosen[1])
    color_btn = ttk.Button(settings_win, text="Choose Color", command=choose_color)
    color_btn.pack(pady=5)
    
    # Beispieloption: Schriftgröße
    font_label = ttk.Label(settings_win, text="Font Size:")
    font_label.pack(pady=(20, 5))
    font_var = tk.IntVar(value=12)
    font_spinbox = ttk.Spinbox(settings_win, from_=8, to=30, textvariable=font_var)
    font_spinbox.pack(pady=5)
    
    def apply_settings():
        # Anwenden der Spracheinstellungen: Aktualisiere die Texte der Hauptbuttons
        trans = translations.get(lang_var.get(), translations["English"])
        # Aktualisiere z. B. Button-Texte (Annahme: btn_analyze, btn_simulate, etc. sind in einem globalen Scope oder können per root.nametowidget() geholt werden)
        try:
            root.nametowidget(".!frame.!button").config(text=trans["Analyze"])
            root.nametowidget(".!frame.!button2").config(text=trans["Simulate"])
            root.nametowidget(".!frame.!button3").config(text=trans["Prove"])
            root.nametowidget(".!frame.!button4").config(text=trans["Exit"])
        except Exception:
            pass  # Falls die widget Namen fehlen, nur Info anzeigen
        messagebox.showinfo("Settings", f"Language: {lang_var.get()}\n"
                                        f"Background Color: {color_var.get()}\n"
                                        f"Font Size: {font_var.get()}")
        settings_win.destroy()
    
    apply_btn = ttk.Button(settings_win, text="Apply", command=apply_settings)
    apply_btn.pack(pady=20)
    
def main():
    display_intro()  # Optionaler Konsolen-Intro
    root = tk.Tk()
    root.title("Collatz Tool")
    
    # Entferne alle benutzerdefinierten Titelleistenanpassungen.
    # Verwende die native Titelleiste.
    
    # Moderne ttk-Styles anwenden
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TFrame", background="#f0f0f0")
    style.configure("TLabel", background="#f0f0f0", font=("Segoe UI", 14))
    style.configure("TButton", font=("Segoe UI", 12), padding=6)
    
    # Fluides Layout und Fensterzentrierung
    root.update_idletasks()
    w = 500
    h = 400
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws // 2) - (w // 2)
    y = (hs // 2) - (h // 2)
    root.geometry(f"{w}x{h}+{x}+{y}")
    
    frame = ttk.Frame(root, padding=20)
    frame.pack(expand=True, fill="both")
    
    def analyze_sequence_callback():
        try:
            number = simpledialog.askinteger("Analyze Sequence", "Enter a starting number for analysis:", minvalue=1, parent=root)
            if number is None: 
                return
            analyzer = CollatzAnalyzer(number)
            analyzer.analyze()
        except Exception as e:
            messagebox.showerror("Error", str(e), parent=root)
    
    def simulate_sequence_callback():
        try:
            start_value = simpledialog.askinteger("Simulate Sequence", "Enter a starting value for simulation:", minvalue=1, parent=root)
            if start_value is None:
                return
            sequence = CollatzSequence(start_value).generate()
            messagebox.showinfo("Simulated Sequence", f"Generierte Collatz-Sequenz:\n{sequence}", parent=root)
        except Exception as e:
            messagebox.showerror("Error", str(e), parent=root)
    
    def prove_conjecture_callback():
        try:
            n = simpledialog.askinteger("Prove Conjecture", "Enter a number to test:", minvalue=1, parent=root)
            if n is None:
                return
            progress = tk.Toplevel(root)
            progress.title("Processing...")
            progress_label = ttk.Label(progress, text=f"Überprüfung der Collatz-Reihe für {n} läuft.\nFalls das Programm hängt, kontaktieren Sie: vinzenz.schaechner@web.de")
            progress_label.pack(padx=20, pady=20)
            
            def prove_single_number_worker(n, result_callback):
                output = ""
                try:
                    sequence = CollatzSequence(n).generate()
                    if sequence[-1] != 1:
                        output = f"Collatz-Reihe für {n} endet nicht mit 1. Test wird abgebrochen."
                    else:
                        output = f"Collatz-Reihe für {n} verifiziert.\nSequenz: {sequence}"
                except Exception as e:
                    output = f"Fehler bei n={n}: {e}"
                result_callback(output)
            
            def on_result(output):
                progress.destroy()
                result_window = tk.Toplevel(root)
                result_window.title("Proof Results")
                text_area = scrolledtext.ScrolledText(result_window, width=80, height=30)
                text_area.pack(expand=True, fill="both")
                text_area.insert(tk.END, output)
            
            threading.Thread(target=prove_single_number_worker, args=(n, on_result), daemon=True).start()
        except Exception as e:
            messagebox.showerror("Error", str(e), parent=root)
    
    def alternative_proof_callback():
        try:
            import sympy as sp
            a = sp.symbols('a', positive=True, integer=True)
            expr = sp.Piecewise((a//2, sp.Eq(sp.Mod(a, 2), 0)), (3*a + 1, True))
            info = ("Alternativer Ansatz mittels symbolischer Methoden:\n\n"
                    f"Definierter Ausdruck:\n{sp.pretty(expr)}\n\n"
                    "Hinweis: Dieser Ansatz demonstriert, wie man mit sympy arbeiten kann. "
                    "Ein vollständiger Beweis (oder Gegenbeweis) der Collatz-Vermutung ist damit jedoch nicht möglich. "
                    "Weitere mathematische Werkzeuge oder Beweissysteme (z. B. Lean oder Coq) wären nötig.")
            messagebox.showinfo("Alternative Proof", info, parent=root)
        except Exception as e:
            messagebox.showerror("Error", str(e), parent=root)
    
    def exit_callback():
        root.destroy()
    
    # Modernisierte, zentral ausgerichtete Widgets
    label = ttk.Label(frame, text="Collatz Tool Menu:")
    label.pack(pady=10)
    
    btn_analyze = ttk.Button(frame, text="Analyze Collatz Sequence", command=analyze_sequence_callback)
    btn_analyze.pack(pady=5, fill="x")
    
    btn_simulate = ttk.Button(frame, text="Simulate Collatz Sequence", command=simulate_sequence_callback)
    btn_simulate.pack(pady=5, fill="x")
    
    btn_prove = ttk.Button(frame, text="Prove Collatz Conjecture", command=prove_conjecture_callback)
    btn_prove.pack(pady=5, fill="x")
    
    btn_exit = ttk.Button(frame, text="Exit", command=exit_callback)
    btn_exit.pack(pady=5, fill="x")
    
    # Neues Zahnradsymbol in der linken unteren Ecke und Fragezeichen in der rechten unteren Ecke
    settings_btn = ttk.Button(root, text="⚙", command=settings_callback, width=3)
    settings_btn.place(relx=0.02, rely=0.98, anchor="sw")
    
    question_btn = ttk.Button(root, text="?", command=alternative_proof_callback, width=3)
    question_btn.place(relx=0.98, rely=0.98, anchor="se")
    
    root.mainloop()

if __name__ == "__main__":
    main()