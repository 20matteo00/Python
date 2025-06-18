# match.py
class Match:
    """
    Rappresenta una singola partita tra due squadre.
    """
    def __init__(self, home: Team, away: Team):
        self.home = home
        self.away = away
        self.home_goals = None
        self.away_goals = None

    def __str__(self):
        h = self.home_goals if self.home_goals is not None else '-'
        a = self.away_goals if self.away_goals is not None else '-'
        return f"{self.home.name} {h} - {a} {self.away.name}"

    def set_result(self, home_goals: int, away_goals: int):
        """Imposta il risultato e aggiorna le statistiche delle squadre."""
        self.home_goals = home_goals
        self.away_goals = away_goals
        self.home.update_stats(home_goals, away_goals)
        self.away.update_stats(away_goals, home_goals)
