import pygame
from settings import *
from snake import Snake
from food import Food

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

snake = Snake()
food = Food()

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != (0, TILE_SIZE):
                snake.direction = (0, -TILE_SIZE)
            elif event.key == pygame.K_DOWN and snake.direction != (0, -TILE_SIZE):
                snake.direction = (0, TILE_SIZE)
            elif event.key == pygame.K_LEFT and snake.direction != (TILE_SIZE, 0):
                snake.direction = (-TILE_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake.direction != (-TILE_SIZE, 0):
                snake.direction = (TILE_SIZE, 0)


    snake.update()
    if snake.check_collision(food.position):
        snake.grow()
        food.spawn()

    screen.fill(BG_COLOR)
    snake.draw(screen)
    food.draw(screen)
    pygame.display.flip()

pygame.quit()
