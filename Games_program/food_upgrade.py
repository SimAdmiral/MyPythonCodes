#Dal by som že tvojou ulohou by bolo udržat si nejake určité skore a vtedy by si zyňho dostával +body
import pygame, sys, random
from pygame.locals import *

# Set up pygame.
pygame.init()
mainClock = pygame.time.Clock()

# Set up the window.
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),
  0, 32)
pygame.display.set_caption('Collision Detection')

# Set up the colors.
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Set up the player and food data structures.
s = 0
foodCounter = 0
NEWFOOD = 20 # HODNOTA URCUJUCA V AKOM INTERVALE SA NEM BUDU SPAVNOVAT JEDLO
FOODSIZE = 20
a = 10
player = pygame.Rect(300, 100, a, a)

#FOODS
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE),
      random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))
#ENEMY
enemy = []
for e in range(5):
    enemy.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE),random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))


# Set up movement variables.
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6

def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

def score(s):
    font = pygame.font.Font('freesansbold.ttf', 16)
    text = font.render('Score: '+ str(s), True, (0,0,0), (255, 192, 203))
    windowSurface.blit(text, [0,0])

def foodS(foods, s):
    font = pygame.font.Font('freesansbold.ttf', 16)

    if len(foods) >= 100:
        text1 = font.render('Foods: ' + str(len(foods)), True, (255, 0, 0), (255, 192, 203))
    else:
        text1 = font.render('Foods: '+ str(len(foods)), True, (0, 0, 255), (255, 192, 203))

    windowSurface.blit(text1, [16*(len(str(s) + 'score')-1), 0])


# Run the game loop.
while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
           pygame.quit()
           sys.exit()
        if event.type == KEYDOWN:
            # Change the keyboard variables.
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == K_w:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True

            #ZMENA  HODNOTY SPAVNOVANIA JEDLA
            if event.key == K_SPACE:
                NEWFOOD -= 1
                MOVESPEED += 0.3

                print(NEWFOOD, MOVESPEED)
                if NEWFOOD == 0:
                    NEWFOOD = 20
                    MOVESPEED = 6


        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_x:
                player.top = random.randint(0, WINDOWHEIGHT -
                  player.height)
                player.left = random.randint(0, WINDOWWIDTH -
                  player.width)

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0], event.pos[1],
              FOODSIZE, FOODSIZE))

    foodCounter += 1
    if len(enemy) < 5:
        enemy.append(pygame.Rect(random.randint(0, WINDOWWIDTH -
            FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

    if foodCounter >= NEWFOOD:
        # Add new food.
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH -
          FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE),
          FOODSIZE, FOODSIZE))

    # Draw the white background onto the surface.
    windowSurface.fill(WHITE)

    # Move the player.
    if moveDown and player.bottom< WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top> 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED
    # Draw the player onto the surface.
    pygame.draw.rect(windowSurface, BLACK, player)

    # Check whether the player has intersected with any food squares.
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            s += 1
            a += 1
            player = pygame.Rect(player.x, player.y, a, a)

    for enem in enemy[:]:
        if player.colliderect(enem):
            enemy.remove(enem)
            if a >= 4:
                a -= a/2
                player = pygame.Rect(player.x, player.y, a, a)

    # Draw the food.
    for i in range(len(foods)):
        pygame.draw.rect(windowSurface, GREEN, foods[i])

    for i in range(len(enemy)):
        pygame.draw.rect(windowSurface, (255,0,0), enemy[i])

    score(s)
    foodS(foods, s)
    # Draw the window onto the screen.
    pygame.display.update()
    mainClock.tick(40)
