import pygame


class Snake:
    def __init__(self, pos, size, speed, color):
        self.size = size
        self.pos = pos
        self.speed = speed
        self.color = color
        self.body = [pos.copy(), [pos[0]-size, pos[1]], [pos[0] - 2 * size, pos[1]]]
        self.direction = 'RIGHT'

    def draw(self, window):
        for pos in self.body:
            pygame.draw.rect(window, self.color, pygame.Rect(pos[0], pos[1], self.size, self.size))

    def move(self):
        head = self.body[0].copy()
        if self.direction == 'RIGHT':
            head[0] += self.size
        elif self.direction == 'LEFT':
            head[0] -= self.size
        elif self.direction == 'UP':
            head[1] -= self.size
        elif self.direction == 'DOWN':
            head[1] += self.size

        self.body.insert(0, head)
        self.body.pop()

    def check_collision(self, window_width, window_height):
        if self.body[0][0] < 0 or self.body[0][0] >= window_width or self.body[0][1] < 0 or self.body[0][1] >= window_height:
            return True
        return False

    def eat_food(self, food_pos):
        if self.body[0] == food_pos:
            self.body.append(self.body[-1])
            return True
        return False

