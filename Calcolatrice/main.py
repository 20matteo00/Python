# main.py
from gui import create_calculator_window

def main():
    # Avvia la finestra della calcolatrice
    root = create_calculator_window()
    root.mainloop()

if __name__ == "__main__":
    main()
