import pygame
import random
from settings import *

class Food:
    def __init__(self):
        self.spawn()

    def spawn(self):
        self.position = (
            random.randint(0, (WIDTH - TILE_SIZE) // TILE_SIZE) * TILE_SIZE,
            random.randint(0, (HEIGHT - TILE_SIZE) // TILE_SIZE) * TILE_SIZE
        )

    def draw(self, screen):
        pygame.draw.rect(screen, FOOD_COLOR, (*self.position, TILE_SIZE, TILE_SIZE))
