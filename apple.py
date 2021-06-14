import pygame
import random


cell_size = 30
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load('assets/images/arthur_santos_apple.png').convert_alpha()
ball = pygame.image.load('assets/images/ball.png').convert_alpha()
ball = pygame.transform.scale(ball, (30, 30))


class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.position.x * cell_size), int(self.position.y * cell_size), cell_size,
                                 cell_size)
        screen.blit(apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.position = pygame.math.Vector2(self.x, self.y)
