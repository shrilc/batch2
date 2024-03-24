import pygame
import random


class Food:
    def __init__(self, size, color, window_width, window_height):
        self.size = size
        # egg_image = pygame.image.load('snake_images/egg.png').convert_alpha()
        # egg_image = pygame.transform.scale(egg_image, (40, 40))
        #foods = [(egg_image, "EGG")]
        self.color = color
        self.pos = [random.randrange(0, window_width-size, size), random.randrange(0, window_height-size, size)]
        #food_image, food_type = random.choice(foods)

    def draw(self, window):
        pygame.draw.rect(window, self.color, pygame.Rect(self.pos[0], self.pos[1], self.size, self.size))


class ImageFood(Food):
    def __init__(self, size, color, window_width, window_height, image_path):
        super().__init__(size, color, window_width, window_height)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

    def draw(self, window):
        window.blit(self.image, self.pos)


if __name__ == "__main__":
    pass
