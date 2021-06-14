from apple import FRUIT
from snake import SNAKE
import pygame
import sys
from pygame.math import Vector2

cell_size = 30
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load('assets/images/arthur_santos_apple.png').convert_alpha()
ball = pygame.image.load('assets/images/ball.png').convert_alpha()
ball = pygame.transform.scale(ball, (30, 30))
game_font = pygame.font.Font('assets/fonts/Boldfinger.ttf', 48)

def draw_ball():
    ball_rect = pygame.Rect(cell_size * cell_number / 2 - cell_size, cell_size * cell_number / 2 - cell_size, cell_size,
                            cell_size)
    screen.blit(ball, ball_rect)
class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        main_game.check_collision()
        main_game.check_fail_collision()

    def draw_elements(self):
        self.draw_gass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        if int(len(self.snake.body) - 3) % 5 == 0 and int(len(self.snake.body) - 3) != 0:
            draw_ball()
        self.draw_score()

    def check_collision(self):
        if self.fruit.position == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()

    def check_fail_collision(self):
        if (not 0 <= self.snake.body[0].x < cell_number) or (not 0 <= self.snake.body[0].y < cell_number):
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

    def draw_gass(self):
        grass_color = (75, 75, 75)
        for row in range(cell_number):
            if row % 2 == 0:
                for column in range(cell_number):
                    if column % 2 == 0:
                        grass_rect = pygame.Rect(column * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for column in range(cell_number):
                    if column % 2 != 0:
                        grass_rect = pygame.Rect(column * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (192, 252, 203))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        screen.blit(score_surface, score_rect)


pygame.init()
main_game = MAIN()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 125)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SCREEN_UPDATE:
            main_game.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_s:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_a:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_d:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)

    screen.fill((93, 93, 93))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)

if __name__ == '__main_game__':
    main_game()