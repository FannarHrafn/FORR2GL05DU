
#Fannar Hrafn Haraldsson
#5.2.18
#skila verkefni 2
import pygame
from random import *
pygame.init()   # we always need this

window_size = window_width, window_height = 1000, 500
window = pygame.display.set_mode(window_size, pygame.RESIZABLE)  # the screen is now resizable

pygame.display.set_caption('FOR3G3U')   # The window has a caption

# Create some color constants for later use.
# The colors are created by RGB mixture.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
drawList=[
    #upper outer wall
    (100,0,100,10),(200,0,100,10),(300, 0, 100, 10),(400, 0, 100, 10),(500, 0, 100, 10),
    (600, 0, 100, 10),(700, 0, 100, 10),(800, 0, 100, 10),(900, 0, 100, 10),
    #bottom outer wall
    (0, 490, 100, 10),(100, 490, 100, 10),(200, 490, 100, 10),(300, 490, 100, 10),(400, 490, 100, 10),
    (500, 490, 100, 10),(600, 490, 100, 10),(700, 490, 100, 10),(800, 490, 100, 10),
    #left outer wall
    (0, 0, 10, 100),(0, 100, 10, 100),(0, 200, 10, 100),(0, 300, 10, 100),(0, 400, 10, 100),
    #right outer wall
    (990, 0, 10, 100),(990, 100, 10, 100),(990, 200, 10, 100),(990, 300, 10, 100),(990, 400, 10, 100),
    #y 100 horizontal walls
    (100,100,100,10),(400,100,100,10),(700,100,100,10),(800,100,100,10),
    #y 200 horizontal walls
    (100,200,100,10),(200,200,100,10),(300,200,100,10),(500,200,100,10),(900,200,100,10),
    #y 300 horizontal walls
    (0,300,100,10),(300,300,100,10),(600,300,100,10),(700,300,100,10),
    #y 400 horizontal walls
    (100,400,100,10),(200,400,100,10),(500,400,100,10),(600,400,100,10),(800,400,100,10),(900,400,100,10),
    #x 100 vertical walls
    (100,100,10,100),
    #x 200 vertical walls
    (200,200,10,100),
    #x 300 vertical walls
    (300,0,10,100),(300,100,10,100),(300,300,10,110),
    #x 400 vertical walls
    (400,200,10,110),(400,400,10,100),
    #x 500 vertical walls
    (500,100,10,100),(500,300,10,100),
    #x 600 vertical walls
    (600,0,10,100),(600,200,10,100),(600,400,10,100),
    #x 700 vertical walls
    (700,100,10,100),(700,300,10,110),
    #x 800 vertical walls
    (800,100,10,100),(800,200,10,110),
    #x 900 vertical walls
    (900,200,10,100)
          ]
#horizontal walls
wallList=[]
for x in drawList:
    wall=pygame.draw.rect(window,WHITE,pygame.Rect(x[0],x[1],x[2],x[3]))
    wallList.append(wall)

x_position = 310
y_position = 230

x_velocity = 0
y_velocity = 0

clock = pygame.time.Clock()
running = True  # loop control variable(for the game loop)
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_velocity = -2
            elif event.key == pygame.K_RIGHT:
                x_velocity = 2
            elif event.key == pygame.K_UP:
                y_velocity = -2
            elif event.key == pygame.K_DOWN:
                y_velocity = 2
        elif event.type == pygame.KEYUP:
            x_velocity = 0
            y_velocity = 0

    x_position += x_velocity
    y_position += y_velocity


    pygame.draw.rect(window, RED, pygame.Rect(x_position, y_position, 20, 20))

    pygame.display.update()
    clock.tick(60)
pygame.quit() # When the game loop is no longer running this causes the program to quit.
