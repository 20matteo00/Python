from game_config import *
from shapely.geometry import Point

# Funzione per ripristinare la posizione del quadrato
def reset_position():
    global quad_x, quad_y
    quad_x, quad_y = 100, 100

# Controlla collisione con nemici o coins
def check_collision(x, y, target):
    return (x < target[0] + ball_radius and x + width_quad > target[0] - ball_radius) and \
           (y < target[1] + ball_radius and y + height_quad > target[1] - ball_radius)

# Funzione per limitare il movimento all'interno del livello
def limit_movement_within_polygons(x, y, width, height, polygons):
    # Crea un punto per ogni angolo del rettangolo del giocatore
    corners = [
        Point(x, y),
        Point(x + width, y),
        Point(x, y + height),
        Point(x + width, y + height),
    ]
    
    # Controlla se almeno un angolo è all'interno di uno dei poligoni permessi
    for polygon in polygons:
        if all(polygon.contains(corner) for corner in corners):
            return x, y  # Movimento consentito
    return None  # Movimento bloccato