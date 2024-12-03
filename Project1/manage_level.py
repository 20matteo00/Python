from game_config import *

# Livello 1
def level1():
    title = "Livello 1"
    start_position = (100, 200)
    total_area = [(margin, 100), (780, 100), (780, 580), (20, 580)]
    start_area = [(20, 100), (150, 100), (150, 580), (20, 580)]
    end_area = [(650, 100), (780, 100), (780, 580), (650, 580)]
    enemies = [(400, 300)]
    coins = [(750, 300)]
    return title, start_position, start_area, end_area, total_area, enemies, coins

# Livello 2
def level2():
    title = "Livello 2"
    start_position = (100, 500)
    total_area = [(20, 100), (780, 100), (780, 580), (20, 580)]
    start_area = [(20, 100), (200, 100), (200, 580), (20, 580)]
    end_area = [(600, 100), (780, 100), (780, 580), (600, 580)]
    enemies = [(300, 150), (500, 450)]
    coins = [(700, 300)]
    return title, start_position, start_area, end_area, total_area, enemies, coins

# Gestisce il livello corrente
def handle_level(current_level):
    if current_level == 1:
        return level1()
    elif current_level == 2:
        return level2()
    else:
        return None