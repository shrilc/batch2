import pygame
import random
import time

# Initialize game
pygame.init()

# Set up the game window
window_width = 400
window_height = 400
window = pygame.display.set_mode((window_width, window_height)) # positonal arugments
pygame.display.set_caption('BATCH2_SNAKE')

# Set up the game variables
snake_size = 10
snake_speed = 10
snake_color = (0, 255, 0)
snake_pos = [window_width/2, window_height/2]
snake_body = [snake_pos.copy(), [snake_pos[0]-snake_size, snake_pos[1]], [snake_pos[0]-2*snake_size, snake_pos[1]]] # List of list structure - [[1, 2], [3, 4], [5, 6]] - 2d matrix
direction = 'RIGHT'

food_size = snake_size
food_color = (255, 0, 0)
food_pos = [random.randrange(0, window_width-food_size, snake_size), random.randrange(0, window_height-food_size, snake_size)]

score = 0

running = True # Flag
clock = pygame.time.Clock()


def draw_snake(snake_body):
    for pos in snake_body:
        pygame.draw.rect(window, snake_color, pygame.Rect(pos[0], pos[1], snake_size, snake_size))


def draw_food(food_pos):
    pygame.draw.rect(window, food_color, pygame.Rect(food_pos[0], food_pos[1], food_size, food_size))


def move_snake(direction, snake_body):
    head = snake_body[0].copy() # [window_width/2, window_height/2]
    if direction == 'RIGHT':
        head[0] += snake_size
    elif direction == 'LEFT':
        head[0] -= snake_size
    elif direction == 'UP':
        head[1] -= snake_size
    elif direction == 'DOWN':
        head[1] += snake_size
    snake_body.insert(0, head)
    snake_body.pop()


def check_collision(snake_body):
    # [window_width/2, window_height/2] Snake head [x, y]
    if snake_body[0][0] < 0 or snake_body[0][0] >= window_width or snake_body[0][1] < 0 or snake_body[0][1] >= window_height or snake_body[0] in snake_body[1:]:
        return True
    return False


def eat_food(snake_body, food_pos):
    if snake_body[0] == food_pos:
        snake_body.append(snake_body[-1])
        return True
    return False


def update_score(score):
    font = pygame.font.Font(None, 30)
    text = font.render('Score: ' + str(score), True, (255, 255, 255))
    window.blit(text, (10, 10))


# Game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'

    move_snake(direction, snake_body)

    if check_collision(snake_body):
        running = False

    if eat_food(snake_body, food_pos):
        score += 1
        food_pos = [random.randrange(0, window_width-food_size, snake_size), random.randrange(0, window_height-food_size, snake_size)]

    # Draw everything

    window.fill((0, 0, 0))
    draw_snake(snake_body)
    draw_food(food_pos)
    update_score(score)
    pygame.display.update()

    # Set the game speed
    clock.tick(snake_speed)


# Quit Game
pygame.quit()
