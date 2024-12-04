# gioco.py
import random

def gioca_partita(squadra1, squadra2):
    # Simula un risultato in base alla forza
    risultato_squadra1 = random.randint(0, 100) + squadra1.forza
    risultato_squadra2 = random.randint(0, 100) + squadra2.forza

    print(f"{squadra1.nome} {risultato_squadra1} - {risultato_squadra2} {squadra2.nome}")
    
    if risultato_squadra1 > risultato_squadra2:
        squadra1.punti += 3
        squadra1.vinte += 1
        squadra2.perse += 1
    elif risultato_squadra2 > risultato_squadra1:
        squadra2.punti += 3
        squadra2.vinte += 1
        squadra1.perse += 1
    else:
        squadra1.punti += 1
        squadra2.punti += 1
        squadra1.pari += 1
        squadra2.pari += 1
    
    squadra1.gol_fatti += max(risultato_squadra1 - risultato_squadra2, 0)
    squadra2.gol_fatti += max(risultato_squadra2 - risultato_squadra1, 0)
    squadra1.gol_subiti += max(risultato_squadra2 - risultato_squadra1, 0)
    squadra2.gol_subiti += max(risultato_squadra1 - risultato_squadra2, 0)
