# main.py
from team import Team
from schedule import generate_round_robin, print_calendario
from standings import print_classifica

def main():
    print("Benvenuto al generatore di campionato!")
    n = int(input("Quante squadre partecipano? "))
    teams = []
    for i in range(1, n+1):
        name = input(f"Nome squadra {i}: ")
        strength = int(input(f"Forza squadra {i} (1-100): "))
        teams.append(Team(name, strength))

    calendar = generate_round_robin(teams)

    while True:
        print("\nScegli un'opzione:")
        print("1) Mostra calendario")
        print("2) Mostra classifica")
        print("3) Inserisci risultati")
        print("0) Esci")
        choice = input("> ")

        if choice == '1':
            print_calendario(calendar)
        elif choice == '2':
            print_classifica(teams)
        elif choice == '3':
            from results import inserisci_risultati
            inserisci_risultati(calendar)
        elif choice == '0':
            break
        else:
            print("Scelta non valida.")

if __name__ == '__main__':
    main()

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
