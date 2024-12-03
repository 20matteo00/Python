import pygame

# Inizializzazione di pygame
pygame.init()

# Impostazioni dello schermo
screen_width, screen_height = 1920, 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("MoscoGame")

# Font
font = pygame.font.SysFont("Arial", 40)
font_small = pygame.font.SysFont("Arial", 30)

# Colori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
LIGHT_GREEN = (144, 238, 144)
LIGHT_YELLOW = (255, 255, 87)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
RED = (255, 0, 0)

# Frasi
title_text = font.render("Benvenuto in MoscoGame!", True, BLACK)
per_iniziare = font.render("Premi Invio per iniziare", True, BLACK)
per_chiudere = font.render("Premi Q per chiudere", True, BLACK)
levels_text = font.render("Livelli", True, BLACK)
pause_text = font.render("Gioco in Pausa", True, BLACK)
resume_text = font.render("Premi P per riprendere", True, BLACK)
game_over_text = font.render("Game Over!", True, RED)
restart_text = font.render("Premi Spazio per riprovare", True, BLACK)
win_text = font.render("Livello Completato!", True, BLACK)
next_text = font.render("Premi Invio per il prossimo livello", True, BLACK)
victory_text = font.render("Hai completato tutti i livelli!", True, BLACK)

# Dimensioni oggetti
width_quad = height_quad = 20
ball_radius = 10

# Dettagli
speed = 3
grandezza_area = screen_height // 10
difficulty = 5
num_levels = 100
margin = screen_height // 40  # Margine
margin_top = screen_height // 8 # Margine dall'alto

# Blocchi Livelli
blocks_per_row = 5  
start_x = margin  # Posizione di partenza sull'asse X
start_y = margin_top  # Posizione di partenza sull'asse Y
block_width = (screen_width - (blocks_per_row + 1) * margin) // blocks_per_row
block_height = screen_height // 10