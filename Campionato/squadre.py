# squadre.py

class Squadra:
    def __init__(self, nome, forza):
        self.nome = nome
        self.forza = forza
        self.punti = 0
        self.vinte = 0
        self.pari = 0
        self.perse = 0
        self.gol_fatti = 0
        self.gol_subiti = 0
    
    def __str__(self):
        return f"{self.nome} (Forza: {self.forza})"
        
def crea_squadre(numero_squadre):
    squadre = []
    for i in range(numero_squadre):
        nome = input(f"Inserisci il nome della squadra {i+1}: ")
        forza = int(input(f"Inserisci la forza della squadra {nome}: "))
        squadra = Squadra(nome, forza)
        squadre.append(squadra)
    return squadre
