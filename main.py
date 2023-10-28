import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pacman")

# Load images
pacman_image = pygame.image.load("pacman.png")
ghost_image = pygame.image.load("ghost.png")

# Set up game variables
pacman_x = 400
pacman_y = 300
ghost_x = 200
ghost_y = 200

# Score
score_value = 0  # The score starts at 0 and will increase with collisions
font = pygame.font.Font('freesansbold.ttf', 26)
text1X = 10
text1Y = 10

# Game Over Text
overFont = pygame.font.Font('freesansbold.ttf', 64)
retryFont = pygame.font.Font('freesansbold.ttf',32)

# Timer
time_value = 5  # The initial timer value is 5 seconds
start_time = pygame.time.get_ticks()  # Get the initial time in milliseconds
text2X = 10
text2Y = 40

def isCollision(ghost_x, ghost_y, pacman_x, pacman_y):
    distance = math.sqrt(math.pow(ghost_x - pacman_x, 2)) + ((math.pow(ghost_y - pacman_y, 2)))
    if distance < 32:  # If the distance which is defined above is less than 35, then there is a collision
        return True
    else:  # If not, then distance equals false
        return False

def gameOverText():
    overText = overFont.render("GAME OVER", True, (255, 255, 255)) # Creates the game over text
    screen.blit(overText, (200, 250)) # Locates it on the x and y axis
    
def tryAgainText():
    retryText = retryFont.render("Press Enter To Try Again", True, (255, 255, 255)) # Creates the game over text
    screen.blit(retryText, (205, 310)) # Locates it on the x and y axis

def showScore(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))  # Adds 1 for each collision
    screen.blit(score, (x, y))

def showTimer(x, y):
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  # Calculate elapsed time in seconds
    remaining_time = max(0, time_value - elapsed_time)  # Calculate remaining time
    timer = font.render("Timer: " + str(remaining_time), True, (255, 255, 255))
    screen.blit(timer, (x, y))

# Game loop
game_over = False  # Initialize game_over variable
while not game_over:
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Game logic

    # User input handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_x -= 0.2
    if keys[pygame.K_RIGHT]:
        pacman_x += 0.2
    if keys[pygame.K_UP]:
        pacman_y -= 0.2
    if keys[pygame.K_DOWN]:
        pacman_y += 0.2

    # Collision
    collision = isCollision(ghost_x, ghost_y, pacman_x, pacman_y)
    if collision:
        score_value += 1
        time_value += 3
        ghost_x = random.randint(0, 736)
        ghost_y = random.randint(0, 568)

    # Update ghost position regardless of collision
    ghost_x += 0
    ghost_y += 0

    # Borders
    # Ghost
    if ghost_x > screen_width:
        ghost_x = 0
    elif ghost_x < 0:
        ghost_x = screen_width
    if ghost_y > screen_height:
        ghost_y = 0
    elif ghost_y < 0:
        ghost_y = screen_height

    # Player
    if pacman_x > screen_width:
        pacman_x = 0
    elif pacman_x < 0:
        pacman_x = screen_width
    if pacman_y > screen_height:
        pacman_y = 0
    elif pacman_y < 0:
        pacman_y = screen_height

    # Render graphics
    screen.fill((0, 0, 0))  # Fill the screen with black color
    screen.blit(pacman_image, (pacman_x, pacman_y))  # Render Pacman image
    screen.blit(ghost_image, (ghost_x, ghost_y))  # Render Ghost image
    showScore(text1X, text1Y)  # Display the score
    showTimer(text2X, text2Y)  # Display the timer

    # Game Over
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  # Calculate elapsed time in seconds
    remaining_time = max(0, time_value - elapsed_time)  # Calculate remaining time
    if remaining_time == 0:
        game_over = True  # Set game_over to True
        screen.fill((0, 0, 0))  # Fill the screen with black color
        gameOverText()  # Display the game over text
        tryAgainText()
        pygame.display.update()  # Update the display
        
        # Wait for the user to press Enter
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # Reset the game variables
                        pacman_x = 400
                        pacman_y = 300
                        ghost_x = 200
                        ghost_y = 200
                        score_value = 0
                        start_time = pygame.time.get_ticks()
                        game_over = False
                        waiting = False
                        
    pygame.display.update()  # Update the display

# Keep the window open until the user closes it
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
