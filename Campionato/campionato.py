# campionato.py
import random
from gioco import gioca_partita

class Campionato:
    def __init__(self, squadre):
        self.squadre = squadre
        self.calendario = []
    
    def genera_calendario(self):
        self.calendario = []
        for i in range(len(self.squadre)):
            for j in range(i + 1, len(self.squadre)):
                self.calendario.append((self.squadre[i], self.squadre[j]))
    
    def visualizza_calendario(self):
        print("Calendario del campionato:")
        for partita in self.calendario:
            print(f"{partita[0].nome} vs {partita[1].nome}")
    
    def visualizza_classifica(self):
        print("Classifica:")
        # Ordinamento in base ai punti
        classifica = sorted(self.squadre, key=lambda s: s.punti, reverse=True)
        for squadra in classifica:
            print(f"{squadra.nome} - Punti: {squadra.punti}")
    
    def gioca_giornata(self):
        if not self.calendario:
            print("Il campionato è terminato!")
            return
        partita = self.calendario.pop(0)
        print(f"Giocando partita: {partita[0].nome} vs {partita[1].nome}")
        gioca_partita(partita[0], partita[1])
