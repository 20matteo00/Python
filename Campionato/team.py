# team.py
class Team:
    """
    Rappresenta una squadra con nome, forza e statistiche di campionato.
    """
    def __init__(self, name: str, strength: int):
        self.name = name
        self.strength = strength
        self.played = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.goals_for = 0
        self.goals_against = 0

    @property
    def points(self) -> int:
        return self.wins * 3 + self.draws

    def update_stats(self, scored: int, conceded: int):
        """Aggiorna le statistiche dopo una partita."""
        self.played += 1
        self.goals_for += scored
        self.goals_against += conceded
        if scored > conceded:
            self.wins += 1
        elif scored == conceded:
            self.draws += 1
        else:
            self.losses += 1
