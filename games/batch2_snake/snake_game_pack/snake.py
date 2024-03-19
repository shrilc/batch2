import pygame


class Snake:
    def __init__(self, pos, size, speed, color):
        self.size = size
        self.pos = pos
        self.speed = speed
        self.color = color
        self.body = [pos.copy(), [pos[0]-size, pos[1]], [pos[0] - 2 * size, pos[1]]]
        self.direction = 'RIGHT'
        self.head=0
        # self.snakehead_image = pygame.image.load('batch2-main\games\snake_game_pack\snake_head.png')
        # self.snakehead_image = pygame.transform.scale(self.snakehead_image, (self.size, self.size))
        # self.snakehead_image = pygame.transform.rotate(self.snakehead_image, 90)
        self.eye1=[self.size-5,self.size-5]
        self.eye2=[self.size-5,5]
        self.rotation=0

    def draw(self, window):
        for i,pos in enumerate(self.body):
            if i==0:
                # self.snakehead_image = pygame.transform.rotate(self.snakehead_image, self.rotation)
                # self.rotation=0
                # window.blit(self.snakehead_image, pos)
                pygame.draw.rect(window, self.color, pygame.Rect(pos[0], pos[1], self.size, self.size))
                pygame.draw.circle(window, (0,0,0), ((pos[0]+self.eye1[0]), (pos[1]+self.eye1[1])),self.size*0.1)
                pygame.draw.circle(window, (0,0,0), ((pos[0]+self.eye2[0]), (pos[1]+self.eye2[1])),self.size*0.1)
            else:
                pygame.draw.rect(window, (128,255,128), pygame.Rect(pos[0], pos[1], self.size, self.size))

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
        if self.body[0][0] < 0 or self.body[0][0] >= window_width or self.body[0][1] < 0 or self.body[0][1] >= window_height or self.body[0] in self.body[1:]:
            return True
        return False

    def eat_food(self, food_pos):
        if self.body[0] == food_pos:
            self.body.append(self.body[-1])
            return True
        return False

