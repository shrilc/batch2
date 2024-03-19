import pygame
import random


class Food:
    def __init__(self, size, color, window_width, window_height):
        self.size = size
        self.color = color
        self.pos = [random.randrange(0, window_width-size, size), random.randrange(0, window_height-size, size)]

    def draw(self, window):
        pygame.draw.rect(window, self.color, pygame.Rect(self.pos[0], self.pos[1], self.size, self.size))


class EggFood(Food):
    def __init__(self,size, color, window_width, window_height):
        super().__init__(size, color, window_width, window_height)
        self.egg_image = pygame.image.load('batch2-main\games\snake_game_pack\egg.png')
        self.egg_image = pygame.transform.scale(self.egg_image, (self.size, self.size))
        self.food_image, self.food_type = (self.egg_image, "EGG")

    def draw(self, window):
        window.blit(self.food_image, self.pos)

if __name__ == "__main__":
    pass
