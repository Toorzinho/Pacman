import pygame


# Game start
pygame.init


# Create the display
screen = pygame.display.set_mode((800,600))

# Player 
player = pygame.image.load('pacman.png')
playerX = 400
playerY = 300

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((255,125,0))
    
    
    if playerX <= 0:
        playerX = 768
    if playerX >= 768:
        playerX = 0
    
    pygame.display.update
    