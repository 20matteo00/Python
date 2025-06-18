# results.py
from match import Match

def inserisci_risultati(calendar: list[list[Match]]):
    """
    Menu per scegliere la giornata e inserire i risultati.
    """
    while True:
        print("\nSeleziona giornata (0 per tornare indietro):")
        for i in range(1, len(calendar)+1):
            print(f"{i}) Giornata {i}")
        sel = int(input("> "))
        if sel == 0:
            break
        if 1 <= sel <= len(calendar):
            giornata = calendar[sel-1]
            for idx, match in enumerate(giornata, start=1):
                print(f"{idx}) {match.home.name} vs {match.away.name}")
            msel = int(input("Seleziona partita (0 per tornare): "))
            if msel == 0:
                continue
            if 1 <= msel <= len(giornata):
                match = giornata[msel-1]
                hg = int(input(f"Gol {match.home.name}: "))
                ag = int(input(f"Gol {match.away.name}: "))
                match.set_result(hg, ag)
                print("Risultato salvato!")
            else:
                print("Partita non valida.")
        else:
            print("Giornata non valida.")
