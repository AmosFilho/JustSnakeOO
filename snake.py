import pygame
from pygame.math import Vector2

cell_size = 30
cell_number = 20
ball_speed_x = 2
ball_speed_y = 1

screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load('assets/images/arthur_santos_apple.png').convert_alpha()
ball = pygame.image.load('assets/images/ball.png').convert_alpha()
ball = pygame.transform.scale(ball, (30, 30))


game_font = pygame.font.Font('assets/fonts/Boldfinger.ttf', 48)
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 125)

def draw_ball():
    ball_rect = pygame.Rect(cell_size * cell_number / 2 - cell_size, cell_size * cell_number / 2 - cell_size, cell_size,
                            cell_size)
    screen.blit(ball, ball_rect)

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

        self.head_up = pygame.image.load('assets/images/snake/1.png').convert_alpha()
        self.head_up = pygame.transform.scale(self.head_up, (30, 30))
        self.head_right = pygame.image.load('assets/images/snake/2.png').convert_alpha()
        self.head_right = pygame.transform.scale(self.head_right, (30, 30))
        self.head_down = pygame.image.load('assets/images/snake/3.png').convert_alpha()
        self.head_down = pygame.transform.scale(self.head_down, (30, 30))
        self.head_left = pygame.image.load('assets/images/snake/4.png').convert_alpha()
        self.head_left = pygame.transform.scale(self.head_left, (30, 30))

        self.tail_up = pygame.image.load('assets/images/snake/8.png').convert_alpha()
        self.tail_up = pygame.transform.scale(self.tail_up, (30, 30))
        self.tail_right = pygame.image.load('assets/images/snake/9.png').convert_alpha()
        self.tail_right = pygame.transform.scale(self.tail_right, (30, 30))
        self.tail_left = pygame.image.load('assets/images/snake/10.png').convert_alpha()
        self.tail_left = pygame.transform.scale(self.tail_left, (30, 30))
        self.tail_down = pygame.image.load('assets/images/snake/7.png').convert_alpha()
        self.tail_down = pygame.transform.scale(self.tail_down, (30, 30))

        self.body_vertical = pygame.image.load('assets/images/snake/5.png').convert_alpha()
        self.body_vertical = pygame.transform.scale(self.body_vertical, (30, 30))
        self.body_horizontal = pygame.image.load('assets/images/snake/6.png').convert_alpha()
        self.body_horizontal = pygame.transform.scale(self.body_horizontal, (30, 30))

        self.curved_body_tail_left = pygame.image.load('assets/images/snake/12.png').convert_alpha()
        self.curved_body_tail_left = pygame.transform.scale(self.curved_body_tail_left, (30, 30))
        self.curved_body_tail_right = pygame.image.load('assets/images/snake/13.png').convert_alpha()
        self.curved_body_tail_right = pygame.transform.scale(self.curved_body_tail_right, (30, 30))
        self.curved_body_left = pygame.image.load('assets/images/snake/14.png').convert_alpha()
        self.curved_body_left = pygame.transform.scale(self.curved_body_left, (30, 30))
        self.curved_body_right = pygame.image.load('assets/images/snake/11.png').convert_alpha()
        self.curved_body_right = pygame.transform.scale(self.curved_body_right, (30, 30))

    def draw_snake(self):
        self.update_head_sprites()
        self.update_tail_sprites()
        for index, block in enumerate(self.body):
            x_position = int(block.x * cell_size)
            y_position = int(block.y * cell_size)
            block_rect = pygame.Rect(x_position, y_position, cell_size, cell_size)
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.curved_body_tail_left, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.curved_body_tail_right, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.curved_body_right, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.curved_body_left, block_rect)

    def update_head_sprites(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_sprites(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

