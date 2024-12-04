import pygame
import sys
from game_config import *
from object_screen import *
from manage_level import *
from check_object import *
from shapely.geometry import Polygon

quad_x, quad_y = 100, 100  # Posizione iniziale del giocatore
clock = pygame.time.Clock()
running = True

# Mostra la schermata di benvenuto
livello = show_welcome_screen()

# Flag
paused = False
game_over = False
level_win = False

# Variabile per la posizione iniziale del giocatore
start_position = (quad_x, quad_y)

# Flag che indica se il gioco è stato resettato
level_started = False
l = 0

while running:
    screen.fill(WHITE)
    
    # Gestisce gli eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Pausa o riprendi
                paused = not paused

            if event.key == pygame.K_ESCAPE:  # Torna alla home
                livello = show_welcome_screen()
                # Ripristina la posizione iniziale del giocatore quando torni alla home
                quad_x, quad_y = start_position
                level_started = False  # Imposta il flag a False quando si torna alla home
                
    # Mostra la schermata di pausa
    if paused:
        display_text(pause_text, (screen_width // 2 - pause_text.get_width() // 2, screen_height // 2 - 50))
        display_text(resume_text, (screen_width // 2 - resume_text.get_width() // 2, screen_height // 2))
        pygame.display.flip()
        clock.tick(10)  # Limita i frame in pausa
        continue  # Salta il resto del ciclo se in pausa          

    # Gestisce il livello
    if l != livello:
        hl = handle_level(livello)
        if hl is not None:
            title, start_position, total_area, safe_area, enemies, coins = hl
            l = livello
            # Solo quando carichi un nuovo livello, aggiorna la posizione di partenza
            if not level_started:  # Solo la prima volta che carichi il livello
                quad_x, quad_y = start_position  # Inizializza la posizione del giocatore
                level_started = True  # Imposta il flag per evitare di resettare la posizione continuamente
        else:  # Fine del gioco
            screen.fill(WHITE)
            display_text(victory_text, (screen_width // 2 - victory_text.get_width() // 2, screen_height // 2))
            pygame.display.flip()
            pygame.time.wait(3000)
            livello = show_welcome_screen()  # Ritorna alla home screen per dare all'utente una scelta
            # Ripristina la posizione del giocatore alla home
            quad_x, quad_y = start_position
            level_started = False  # Resetta il flag per il livello successivo

    # Gestione degli input da tastiera
    keys = pygame.key.get_pressed()
    new_x, new_y = quad_x, quad_y

    # Movimento del giocatore
    if not game_over and not level_win:
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:  # Freccia sinistra o 'A'
            new_x -= speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:  # Freccia destra o 'D'
            new_x += speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:  # Freccia su o 'W'
            new_y -= speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:  # Freccia giù o 'S'
            new_y += speed

    # Limita il movimento all'interno dell'area valida
    polygons = [Polygon(total_area)]
    limited_position = limit_movement_within_polygons(new_x, new_y, width_quad, height_quad, polygons)
    if limited_position:
        quad_x, quad_y = limited_position

    # Disegna il livello (con la mappa, nemici, ecc.)
    draw_level(title, total_area, safe_area, enemies, coins)    
    
    # Controlla collisioni
    for enemy in enemies:
        if check_collision(quad_x, quad_y, enemy):
            game_over = True

    for coin in coins:
        if check_collision(quad_x, quad_y, coin):
            level_win = True

    # Gestione Game Over
    if game_over:
        display_text(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - 50))
        display_text(restart_text, (screen_width // 2 - restart_text.get_width() // 2, screen_height // 2))
        if keys[pygame.K_SPACE]:  # Tasto per resettare
            quad_x, quad_y = start_position  # Reset della posizione alla posizione iniziale
            game_over = False

    # Gestione Vittoria Livello
    if level_win:
        display_text(win_text, (screen_width // 2 - win_text.get_width() // 2, screen_height // 2 - 50))
        display_text(next_text, (screen_width // 2 - next_text.get_width() // 2, screen_height // 2))
        if keys[pygame.K_RETURN]:  # Tasto per livello successivo
            livello += 1
            hl = handle_level(livello)
            level_win = False
            if hl is not None:
                title, start_position, total_area, safe_area, enemies, coins = hl
                # Solo quando carichi un nuovo livello, aggiorna la posizione di partenza
                quad_x, quad_y = start_position  # Inizializza la posizione del giocatore alla start_position del livello
                level_started = True  # Imposta il flag per evitare di resettare la posizione continuamente
            else:  # Fine del gioco
                screen.fill(WHITE)
                display_text(victory_text, (screen_width // 2 - victory_text.get_width() // 2, screen_height // 2))
                pygame.display.flip()
                pygame.time.wait(3000)
                livello = show_welcome_screen()  # Ritorna alla home screen per dare all'utente una scelta
                # Ripristina la posizione del giocatore alla home
                quad_x, quad_y = start_position
                level_started = False  # Resetta il flag per il livello successivo

    # Disegna il giocatore (quadro rosso)
    pygame.draw.rect(screen, RED, (quad_x, quad_y, width_quad, height_quad))

    pygame.display.flip()  # Aggiorna lo schermo
    clock.tick(60)  # Imposta il framerate (60 FPS)