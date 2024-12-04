import random
from game_config import *

# Funzione per generare la posizione casuale all'interno dell'area, considerando il raggio della pallina
# e controllando che non venga generata due volte la stessa posizione
def generate_random_position(x_min, x_max, y_min, y_max, ball_radius, previous_positions):
    while True:
        # Genera una posizione casuale dentro l'area
        x = random.randint(x_min + ball_radius, x_max - ball_radius)
        y = random.randint(y_min + ball_radius, y_max - ball_radius)
        new_position = (x, y)
        
        # Verifica se la posizione è già stata generata
        if new_position not in previous_positions:
            previous_positions.add(new_position)  # Aggiungi la nuova posizione
            return new_position  # Restituisci la posizione unica


# Livello
def level(num):
    title = "Livello " + str(num)
    start_position = (margin + grandezza_area//2, margin_top + grandezza_area//2)
    total_area = [
        (margin, margin_top),
        (screen_width - margin, margin_top),
        (screen_width - margin, screen_height - margin),
        (margin, screen_height - margin),
    ]
    safe_area = [
        (margin + grandezza_area, margin_top + grandezza_area),
        (screen_width - margin - grandezza_area, margin_top + grandezza_area),
        (screen_width - margin - grandezza_area, screen_height - margin - grandezza_area),
        (margin + grandezza_area, screen_height - margin - grandezza_area),
    ]
    # Estrai i limiti del rettangolo
    x_min = margin + grandezza_area
    y_min = margin_top + grandezza_area
    x_max = screen_width - margin - grandezza_area
    y_max = screen_height - margin - grandezza_area

    # Set per tracciare le posizioni già generate
    previous_enemy_positions = set()
    previous_coin_positions = set()

    # Genera le posizioni per i nemici
    enemies = [generate_random_position(x_min, x_max, y_min, y_max, ball_radius, previous_enemy_positions) for _ in range(num * difficulty)]

    # Genera le posizioni per le monete
    coins = [generate_random_position(x_min, x_max, y_min, y_max, ball_radius, previous_coin_positions) for _ in range(1)]
    
    return title, start_position, total_area, safe_area, enemies, coins


# Gestisce il livello corrente
def handle_level(current_level):
    if current_level <= num_levels:
        return level(current_level)
    else:
        return None