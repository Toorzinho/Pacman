import pygame


# Game start
pygame.init


# Create the display
screen = pygame.display.set_mode((800,600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((255,125,0))
    
    pygame.display.update
    