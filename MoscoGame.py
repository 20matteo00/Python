import pygame
import sys
from shapely.geometry import Point, Polygon

# Inizializzazione di Pygame
pygame.init()

# Impostazioni dello schermo
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gioco a Livelli")

# Colori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
LIGHT_GREEN = (144, 238, 144)
LIGHT_YELLOW = (255, 255, 87)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Dimensioni oggetti
quad_size = 20
ball_radius = 10

# Posizione del quadrato
quad_x, quad_y = 100, 100
width_quad, height_quad = quad_size, quad_size
speed = 3


# Stato del gioco
paused = False
game_over = False
level_win = False
current_level = 1
game_started = False

# Font
font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 36)

# Schermata Home
def home_screen():
    global game_started
    reset_position()
    screen.fill(WHITE)

    # Titolo del gioco
    title_text = font.render("Benvenuto nel Gioco!", True, BLACK)
    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, screen_height // 2 - 100))

    # Istruzioni per i tasti
    play_text = font.render("Premi INVIO per Giocare", True, BLACK)
    quit_text = font.render("Premi Q per Uscire", True, BLACK)

    screen.blit(play_text, (screen_width // 2 - play_text.get_width() // 2, screen_height // 2))
    screen.blit(quit_text, (screen_width // 2 - quit_text.get_width() // 2, screen_height // 2 + 50))

    pygame.display.flip()

    # Ciclo per aspettare input dell'utente
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Invio per iniziare il gioco
                    game_started = True
                    waiting_for_input = False
                elif event.key == pygame.K_q:  # 'Q' per uscire
                    pygame.quit()
                    sys.exit()


# Funzione per ripristinare la posizione del quadrato
def reset_position():
    global quad_x, quad_y
    quad_x, quad_y = 100, 100

# Disegna il titolo del livello
def draw_title(title):
    level_text = font.render(title, True, BLACK)
    screen.blit(level_text, (screen_width // 2 - level_text.get_width() // 2, 20))

# Livello 1
def level1():
    title = "Livello 1"
    start_position = (100,200)
    total_area = [(20, 100), (780, 100), (780, 580), (20, 580)]
    start_area = [(20, 100), (150, 100), (150, 580), (20, 580)]
    end_area = [(650, 100), (780, 100), (780, 580), (650, 580)]
    enemies = [(400, 300)]
    coins = [(750, 300)]
    return title, start_position, start_area, end_area, total_area, enemies, coins

# Livello 2
def level2():
    title = "Livello 2"
    start_position = (100,500)
    total_area = [(20, 100), (780, 100), (780, 580), (20, 580)]
    start_area = [(20, 100), (200, 100), (200, 580), (20, 580)]
    end_area = [(600, 100), (780, 100), (780, 580), (600, 580)]
    enemies = [(300, 150), (500, 450)]
    coins = [(700, 300)]
    return title, start_position, start_area, end_area, total_area, enemies, coins

# Controlla collisione con nemici o coins
def check_collision(x, y, target):
    return (x < target[0] + ball_radius and x + width_quad > target[0] - ball_radius) and \
           (y < target[1] + ball_radius and y + height_quad > target[1] - ball_radius)

# Disegna un livello
def draw_level(title, start_area, end_area, total_area, enemies, coins):
    draw_title(title)
    if len(total_area) >= 3 or len(start_area) >= 3 or len(end_area) >= 3:
        pygame.draw.polygon(screen, WHITE, total_area)  # Area totale
        pygame.draw.polygon(screen, LIGHT_GREEN, start_area)  # Area di partenza
        pygame.draw.polygon(screen, LIGHT_GREEN, end_area)    # Area di arrivo
    for enemy in enemies:
        pygame.draw.circle(screen, BLUE, enemy, ball_radius)  # Nemici
    for coin in coins:
        pygame.draw.circle(screen, YELLOW, coin, ball_radius)  # Punto di arrivo
    pygame.draw.polygon(screen, RED, total_area, 5)  # Bordi neri con spessore di 5 pixel

# Gestisce il livello corrente
def handle_level():
    if current_level == 1:
        return level1()
    elif current_level == 2:
        return level2()
    else:
        return None

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

# Ciclo principale
def main():
    global paused, game_over, level_win, current_level, quad_x, quad_y, game_started

    clock = pygame.time.Clock()
    running = True
    game_started = False

    # Mostra la schermata iniziale
    home_screen()

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Pausa o riprendi
                    paused = not paused
            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_ESCAPE:  # torna alla home
                    game_started = False
                    current_level = 1
                    home_screen()
                    
        # Se il gioco non è ancora iniziato, resta nella schermata iniziale
        if not game_started:
            continue  # Torna all'inizio del ciclo per rimanere nella home screen

        # Mostra la schermata di pausa
        if paused:
            pause_text = font.render("Gioco in Pausa", True, BLACK)
            resume_text = small_font.render("Premi P per riprendere", True, BLACK)
            screen.blit(pause_text, (screen_width // 2 - pause_text.get_width() // 2, screen_height // 2 - 50))
            screen.blit(resume_text, (screen_width // 2 - resume_text.get_width() // 2, screen_height // 2))
            pygame.display.flip()
            clock.tick(10)  # Limita i frame in pausa
            continue  # Salta il resto del ciclo se in pausa

        keys = pygame.key.get_pressed()
        new_x, new_y = quad_x, quad_y

        if not game_over and not level_win:
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:  # Freccia sinistra o 'A'
                new_x -= speed
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:  # Freccia destra o 'D'
                new_x += speed
            if keys[pygame.K_UP] or keys[pygame.K_w]:  # Freccia su o 'W'
                new_y -= speed
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:  # Freccia giù o 'S'
                new_y += speed

        # Ottieni informazioni sul livello corrente
        hl = handle_level()
        if hl is not None:
            title, start_position, start_area, end_area, total_area, enemies, coins = hl
            quad_x, quad_y = start_position
        else :  # Fine del gioco
            victory_text = font.render("Hai completato tutti i livelli!", True, BLACK)
            screen.blit(victory_text, (screen_width // 2 - victory_text.get_width() // 2, screen_height // 2))
            pygame.display.flip()
            pygame.time.wait(3000)
            current_level = 1
            game_started = False  # Torna alla schermata iniziale dopo aver completato tutti i livelli
            home_screen()  # Ritorna alla home screen per dare all'utente una scelta

        # Crea poligoni per le aree valide
        polygons = [Polygon(total_area)]

        # Limita il movimento ai poligoni definiti dal livello
        limited_position = limit_movement_within_polygons(new_x, new_y, width_quad, height_quad, polygons)
        if limited_position:
            quad_x, quad_y = limited_position
        
        # Disegna il livello
        draw_level(title, start_area, end_area, total_area, enemies, coins)

        # Controlla collisioni
        for enemy in enemies:
            if check_collision(quad_x, quad_y, enemy):
                game_over = True

        for coin in coins:
            if check_collision(quad_x, quad_y, coin):
                level_win = True

        # Gestione Game Over
        if game_over:
            game_over_text = font.render("Game Over!", True, RED)
            restart_text = small_font.render("Premi Spazio per riprovare", True, BLACK)
            screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - 50))
            screen.blit(restart_text, (screen_width // 2 - restart_text.get_width() // 2, screen_height // 2))
            if keys[pygame.K_SPACE]:  # Tasto per resettare
                reset_position()
                game_over = False

        # Gestione Vittoria Livello
        if level_win:
            win_text = font.render("Livello Completato!", True, BLACK)
            next_text = small_font.render("Premi Invio per il prossimo livello", True, BLACK)
            screen.blit(win_text, (screen_width // 2 - win_text.get_width() // 2, screen_height // 2 - 50))
            screen.blit(next_text, (screen_width // 2 - next_text.get_width() // 2, screen_height // 2))
            if keys[pygame.K_RETURN]:  # Tasto per livello successivo
                current_level += 1
                reset_position()
                level_win = False

        # Disegna il giocatore
        pygame.draw.rect(screen, RED, (quad_x, quad_y, width_quad, height_quad))

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()