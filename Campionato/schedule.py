# schedule.py
from team import Team
from match import Match

def generate_round_robin(teams: list[Team]) -> list[list[Match]]:
    """
    Genera il calendario con algoritmo round-robin (all'andata e ritorno).
    Restituisce una lista di giornate, ciascuna contenente una lista di Matches.
    """
    if len(teams) % 2:
        teams.append(Team("Riposo", 0))  # bye week
    n = len(teams)
    half = n // 2
    giornate = []
    rotation = teams[1:]

    for round in range(n - 1):
        pairs = []
        left = [teams[0]] + rotation[:half-1]
        right = rotation[half-1:][::-1]
        for i in range(half):
            pairs.append(Match(left[i], right[i]))
        giornate.append(pairs)
        rotation = rotation[1:] + rotation[:1]

    # ritorno (invertiamo le partite)
    ritorno = []
    for giornata in giornate:
        rev = [Match(m.away, m.home) for m in giornata]
        ritorno.append(rev)

    return giornate + ritorno


def print_calendario(calendar: list[list[Match]]):
    """Stampa a video il calendario."""
    for i, giornata in enumerate(calendar, start=1):
        print(f"\nGiornata {i}")
        for m in giornata:
            print(f"  - {m.home.name} vs {m.away.name}")