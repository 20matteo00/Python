import pygame
import sys
from game_config import *

# Funzione per visualizzare il testo
def display_text(label, position):
    screen.blit(label, position)

# Funzione che mostra la schermata di benvenuto
def show_welcome_screen():
    running = True

    while running:
        screen.fill(WHITE)

        # Visualizzazione del messaggio di benvenuto
        display_text(title_text, (screen_width // 2 - title_text.get_width() // 2, 50))
        display_text(per_iniziare, (screen_width // 2 - per_iniziare.get_width() // 2, screen_height // 2))
        display_text(per_chiudere, (screen_width // 2 - per_chiudere.get_width() // 2, screen_height // 2 + 50))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False  # Esce dal programma se premi Q
                if event.key == pygame.K_RETURN:
                    running = False  # Inizia il gioco o passa alla schermata successiva
                    return show_level_screen()
                    
    pygame.quit()  # Chiude Pygame
    sys.exit()  # Esce dal programma
    

# Funzione che mostra la schermata con i livelli disponibili, visualizzati in blocchi
def show_level_screen():
    running = True
    screen.fill(WHITE)

    # Visualizzazione del testo dei livelli
    display_text(levels_text, (screen_width // 2 - levels_text.get_width() // 2, 50))

    while running:
        # Mostra i livelli in blocchi
        for i in range(1, num_levels + 1):
            # Calcola la posizione del blocco (se i blocchi non devono sovrapporsi)
            row = (i - 1) // blocks_per_row  # Calcola la riga
            col = (i - 1) % blocks_per_row  # Calcola la colonna

            # Posizione del blocco
            x_pos = start_x + col * (block_width + margin)  # Posizione orizzontale
            y_pos = start_y + row * (block_height + margin)  # Posizione verticale

            # Crea un rettangolo per ogni bottone
            button_rect = pygame.Rect(x_pos, y_pos, block_width, block_height)

            # Disegna il bottone
            pygame.draw.rect(screen, BLACK, button_rect)
            label = font.render(f"Livello {i}", True, WHITE)

            # Calcola la posizione per centrare il testo all'interno del blocco
            x_position = x_pos + (block_width - label.get_width()) // 2
            y_position = y_pos + (block_height - label.get_height()) // 2

            # Visualizza il testo centrato nel blocco
            display_text(label, (x_position, y_position))


            # Gestisce l'interazione con i bottoni (clic del mouse)
            if button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                return i

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()  # Chiude Pygame
    sys.exit()  # Esce dal programma
    
# Disegna un livello
def draw_level(title, start_area, end_area, total_area, enemies, coins):
    level_text = font.render(title, True, BLACK)
    display_text(level_text, (screen_width // 2 - level_text.get_width() // 2, 50))
    if len(total_area) >= 3 or len(start_area) >= 3 or len(end_area) >= 3:
        pygame.draw.polygon(screen, WHITE, total_area)  # Area totale
        pygame.draw.polygon(screen, LIGHT_GREEN, start_area)  # Area di partenza
        pygame.draw.polygon(screen, LIGHT_GREEN, end_area)    # Area di arrivo
    for enemy in enemies:
        pygame.draw.circle(screen, BLUE, enemy, ball_radius)  # Nemici
    for coin in coins:
        pygame.draw.circle(screen, YELLOW, coin, ball_radius)  # Punto di arrivo
    pygame.draw.polygon(screen, RED, total_area, 1)  # Bordi neri con spessore di 5 pixel