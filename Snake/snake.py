import pygame
from settings import *

class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100)]
        self.direction = (TILE_SIZE, 0)

    def update(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        self.body.append(self.body[-1])

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, SNAKE_COLOR, (*segment, TILE_SIZE, TILE_SIZE))

    def check_collision(self, position):
        return self.body[0] == position
