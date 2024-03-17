import pygame
import random


class Food:
    def __init__(self, size, color, window_width, window_height):
        self.size = size
        #foods = [(egg_image, "EGG")]
        self.color = color
        self.pos = [random.randrange(0, window_width-size, size), random.randrange(0, window_height-size, size)]
        #food_image, food_type = random.choice(foods)

    def draw(self, window):
        pygame.draw.rect(window, self.color, pygame.Rect(self.pos[0], self.pos[1], self.size, self.size))


class EggFood(Food):
    pass


if __name__ == "__main__":
    egg = EggFood(
        size=20,
        color=(0, 255, 255),
        window_width=600,
        window_height=600
    )
