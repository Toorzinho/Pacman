import pygame
import random
import math
from pygame import mixer

# Game start
pygame.init()

# Create the display
screen = pygame.display.set_mode((800,600))

# Player 
playerImg = pygame.image.load('pacman.png')
playerX = 400
playerY = 300
playerY_change = 0
playerX_change = 0

def player(x,y):
    screen.blit(playerImg, (x,y))

# Game loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((255,225,10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    player(playerX,playerY)
    pygame.display.update
    
    
    