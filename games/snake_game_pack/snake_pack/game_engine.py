import random

import pygame
from snake import Snake
from food import ImageFood, Food


class Game:
    def __init__(self, window_width, window_height):
        pygame.init()
        self.window_width = window_width
        self.window_height = window_height
        self.window = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption('BATCH2_SNAKE WITH CLASS BASED APPROACH')
        self.score = 0
        self.level = 1
        self.running = True
        self.clock = pygame.time.Clock()
        self.snake = Snake(
            pos=[window_width/2, window_height/2],
            size=10,
            speed=7,
            color=(0, 255, 0)
        )
        # self.food = Food(
        #     size=20,
        #     color=(255, 0, 0),
        #     window_width=window_width,
        #     window_height=window_height
        # )
        self.egg = ImageFood(
            size=20,
            color=(255, 0, 0),
            window_width=window_width,
            window_height=window_height,
            image_path='egg.png'
        )

        self.mouse = ImageFood(
            size=20,
            color=(255, 0, 0),
            window_width=window_width,
            window_height=window_height,
            image_path='mouse.png'
        )

        self.milk = ImageFood(
            size=20,
            color=(255, 0, 0),
            window_width=window_width,
            window_height=window_height,
            image_path='milk.png'
        )

        self.food = random.choice([self.egg, self.milk, self.mouse])

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and self.snake.direction != 'LEFT':
                    self.snake.direction = 'RIGHT'
                elif event.key == pygame.K_LEFT and self.snake.direction != 'RIGHT':
                    self.snake.direction = 'LEFT'
                elif event.key == pygame.K_UP and self.snake.direction != 'DOWN':
                    self.snake.direction = 'UP'
                elif event.key == pygame.K_DOWN and self.snake.direction != 'UP':
                    self.snake.direction = 'DOWN'

    def update_score(self):
        font = pygame.font.Font(None, 30)
        text = font.render('Score: ' + str(self.score), True, (255, 255, 255))
        self.window.blit(text, (10, 10))

    def update_level(self):
        font = pygame.font.Font(None, 30)
        text = font.render('Level: ' + str(self.score), True, (255, 255, 255))
        self.window.blit(text, (self.window_width-100, 10))

    def update_game(self):
        self.window.fill((0, 0, 0))
        self.snake.draw(window=self.window)
        self.food.draw(window=self.window)
        self.update_score()
        self.update_level()
        pygame.display.update()

    def check_collision(self):
        if self.snake.check_collision(window_height=self.window_height, window_width=self.window_width):
            self.running = False

    def eat_food(self):
        if self.snake.eat_food(self.food.pos):
            self.score += 1
            if self.score % 5 == 0:
                self.level += 1
                self.snake.speed += 5
            self.food = random.choice([
            ImageFood(
                size=20,
                color=(255, 0, 0),
                window_width=self.window_width,
                window_height=self.window_height,
                image_path='egg.png'
            ),
            ImageFood(
                size=20,
                color=(255, 0, 0),
                window_width=self.window_width,
                window_height=self.window_height,
                image_path='mouse.png'
            ),
            ImageFood(
                size=20,
                color=(255, 0, 0),
                window_width=self.window_width,
                window_height=self.window_height,
                image_path='milk.png'
            )
            ])

            self.update_game()

    def run(self):
        while self.running:
            self.handle_events()
            self.snake.move()
            self.check_collision()
            self.eat_food()
            self.update_game()
            self.clock.tick(self.snake.speed)
        pygame.quit()


if __name__ == "__main__":
    game = Game(window_width=600, window_height=600)
    game.run()
