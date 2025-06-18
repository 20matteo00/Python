# standings.py
from team import Team

def print_classifica(teams: list[Team]):
    """Stampa la classifica ordinata per punti, differenza reti e gol fatti."""
    sorted_teams = sorted(
        [t for t in teams if t.name != "Riposo"],
        key=lambda x: (x.points, x.goals_for - x.goals_against, x.goals_for),
        reverse=True
    )
    header = f"{'Pos':<4}{'Squadra':<20}{'Pti':<4}{'G':<4}{'V':<4}{'N':<4}{'P':<4}{'GF':<4}{'GS':<4}{'DR':<4}"
    print(header)
    print('-'*len(header))
    for idx, t in enumerate(sorted_teams, start=1):
        dr = t.goals_for - t.goals_against
        print(f"{idx:<4}{t.name:<20}{t.points:<4}{t.played:<4}{t.wins:<4}{t.draws:<4}{t.losses:<4}{t.goals_for:<4}{t.goals_against:<4}{dr:<4}")
