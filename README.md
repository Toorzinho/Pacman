Lavet af Jadbinder, Baker og Gabriel

2.p - Sukkertoppen Gymnasium

VsCode - Python


# Pacman

**Beskrivelse af spillet**

Spillet er en simpliceret version af pacman, hvor spilleren går efter spøgelset i stedet for pengene. Spillet har flere funktioner som: 

- "Score" der tæller antal point du har. 
- "Timer" som tæller ned til 0, hvis tiden rammer 0, vil spillet slutte
- "Retry" som genstarter spillet efter man er død
- Spillet har også basale bevægelses mekanismer  
- Teleportation fra en side til den anden (Når man rammer højre væg, teleporteres man til venstre væg)
- "Enemy Respawn" som henter en ny fjende når den første er død, og det sker ved hjælp af "randint"
- "Colission" som sker hvis spilleren og fjenden mødes

==========================================

**Starten**

Vi begyndnte med at diskutere hvad vi skulle begynde med at kode. Vi startede med et simpelt display screen som er 800x600, og importede pygame. Vi så den Space Invaders koden og fik inspiration fra den til at kode vores program. Vi lavede "sprites" eller billeder til spilleren og fandt et billede af en af spøgelserne fra spillet. Derefter begyndte vi med "while" loopen. Derefter begyndte vi på player mechanics, og gav spilleren en x og y værdi, og indsatte pacman billedet, så spilleren kan bevæge den rundt, og det gjorde vi ved hjælp af "pygame.image.load("")"

==========================================
### Dokumentation af koden

```
    # Game Over
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  # Calculate elapsed time in seconds
    remaining_time = max(0, time_value - elapsed_time)  # Calculate remaining time
    if remaining_time == 0:
        game_over = True  # Set game_over to True
        screen.fill((0, 0, 0))  # Fill the screen with black color
        gameOverText()  # Display the game over text
        tryAgainText()
        pygame.display.update()  # Update the display
```

Variablen start_time initialiseres med den aktuelle tid i millisekunder ved hjælp af pygame.time.get_ticks() i begyndelsen af spille loopet.
Inde i funktionen showTimer() beregnes den forløbne tid ved at trække start_time fra det aktuelle tidspunkt ved hjælp af pygame.time.get_ticks(). Resultatet divideres med 1000 for at konvertere det til sekunder.
Den resterende tid opnås ved at trække den forløbne tid fra den indledende time_value.
Den resterende tid vises på skærmen.

```
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
```

Med denne kode, når spilleren trykker på Enter tasten, efter at game over skærmen er vist, nulstilles spilvariablerne, og spillet starter igen fra starttilstanden.

```
def showScore(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))  # Adds 1 for each collision
    screen.blit(score, (x, y))
```

Den definerede variabel skal kunne vise antal point, og en smart metode for at opnå det er ved hjælp af strings. Koden bruger strings og plusser dem med de nuværende point

```
def isCollision(ghost_x, ghost_y, pacman_x, pacman_y):
    distance = math.sqrt(math.pow(ghost_x - pacman_x, 2)) + ((math.pow(ghost_y - pacman_y, 2)))
    if distance < 32:  # If the distance which is defined above is less than 35, then there is a collision
        return True
    else:  # If not, then distance equals false
        return False

    # Collision
    collision = isCollision(ghost_x, ghost_y, pacman_x, pacman_y)
    if collision:
        score_value += 1
        time_value += 3
        ghost_x = random.randint(0, 736)
        ghost_y = random.randint(0, 568)
```

Funktionen isCollision bruges til at afgøre, om der er en kollision mellem spøgelset og Pacman i spillet.
Funktionen tager fire parametre: ``ghost_x og ghost_y`` repræsenterer koordinaterne for spøgelset, og ``pacman_x og pacman_y`` repræsenterer koordinaterne for Pacman.
Når de 2 støder sammen, vil spøgelsen befinde sig i et nyt område på skærmen ved hjælp af ``random.randint()``. Hver gang spilleren stødder ind i spøgelsen, ville spillers points stige med 1. 
Spillern får også 3 ekstra sekunder til sin ``remaining_time``.

```
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
```

Koden her viser spillerns input og bevægelsesmekanisme, den er simpel men virker altid perfekt, dog metoden er lidt anderledes. 

```
 if player_x > screen_width:
        player_x = 0
    elif player_x < 0:
        player_x = screen_width
    if player_y > screen_height:
        player_y = 0
    elif player_y < 0:
        player_y = screen_height
```

Her teleporteres spilleren til den omvendte side. Når spilleren rører skærmgrænsen, ville han teleportere til den anden side hved hjælp af en simpel kode.
Variablerne ``screen_hight`` og ``screen_width``bliver brugt i starten til at kode skærmen, og bliver også brugt her, så det er smart at bruge en variabel i stedet for bare at skrive tal ned

```
    # Render graphics
    screen.fill((0, 0, 0))  # Fill the screen with black color
    screen.blit(pacman_image, (pacman_x, pacman_y))  # Render Pacman image
    screen.blit(ghost_image, (ghost_x, ghost_y))  # Render Ghost image
    showScore(text1X, text1Y)  # Display the score
    showTimer(text2X, text2Y)  # Display the timer
```

Her bliver alle billeder så som ghosten, scoren, timeren, bagrunden og pacman tegnet

#### Flowdiagram

![image](https://github.com/Toorzinho/Pacman/assets/146086727/e384f0a1-76d1-4db6-a3bb-c4b28ffc53d6)

==========================================

### Beskrivelse af udviklingsprocessen




