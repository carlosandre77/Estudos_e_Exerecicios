import pygame, random
from pygame.locals import *

def on_grid_random():
    x =  random.randint(0,90)
    y = random.randint(0, 90)
    return (x//10*10, y//10* 10)
def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])
def collision2(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

pygame.init()
screen = pygame.display.set_mode([100, 100])
pygame.display.set_caption("snake")

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

snake = [(0, 20),(10, 20),(20, 20) ]
snike1= len(snake)-1
snake2= snake[snike1]
snake_skin = pygame.Surface((10,10))

snake_skin.fill((255,5,255))
my_direction = LEFT

clock = pygame.time.Clock()

apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

fechar= False

while fechar != True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            fechar = True

        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_RIGHT:
                my_direction = RIGHT
            if event.key == K_LEFT:
                my_direction = LEFT
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))

    if collision2(snake2, snake[1:]):
        print('55')

    for i in range(len(snake) -1,0,-1):
        snake[i] = (snake[i -1][0], snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] -10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] +10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] +10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] -10, snake[0][1])

    screen.fill((250,250,250))
    screen.blit(apple,apple_pos)
    for pos in snake:
        screen.blit(snake_skin,pos)
    pygame.display.update()

