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

'''
def showTimer(x, y):
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  # Calculate elapsed time in seconds
    remaining_time = max(0, time_value - elapsed_time)  # Calculate remaining time
    timer = font.render("Timer: " + str(remaining_time), True, (255, 255, 255))
    screen.blit(timer, (x, y))
  '''







#### Flowdiagram

![image](https://github.com/Toorzinho/Pacman/assets/146086727/e384f0a1-76d1-4db6-a3bb-c4b28ffc53d6)





