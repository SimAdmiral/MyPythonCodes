import os
import random
import pygame
import sys
ano = False
# Class for the orange dude
class Player(object):

    def __init__(self):
        self.rect = pygame.Rect(16, 16, 16, 16)

    def move(self, dx, dy,end_rect):
        # Move each axis separately. Note that this checks for collisions both times.

        if dx != 0:
            self.move_single_axis(dx, 0,end_rect)

        if dy != 0:
            self.move_single_axis(0, dy,end_rect)


    def move_single_axis(self, dx, dy,end_rect):

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy
        global ano


        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                    ano = True
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                    ano = True
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                    ano = True
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
                    ano = True
        if self.rect.colliderect(end_rect):
            print('collider')
            ano = True
            pygame.draw.rect(screen, (255, 200, 0), player.rect)

    def P_end(self, end_rect):
        if player.rect.colliderect(end_rect):
            print('a')
            pygame.draw.rect(screen, (255, 200, 0), player.rect)
            #pygame.time.delay(1000)
            #self.rect = pygame.Rect(16, 16, 16, 16)

# Nice class to hold a wall rect
class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)


# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

# Set up the display
pygame.display.set_caption("Get to the red square!")

clock = pygame.time.Clock()
walls = []  # List to hold the walls
player = Player()  # Create the player

# Holds the level layout in a list of strings.

level = [
    "WWWWWWWWWWWWWWWWWWWWW",
    "W      W E          W",
    "W      W  WWWWWW    W",
    "W   WWW        W   WW",                #UROB LIST Z KTOREHO SA BUDU NAHODNE NAčITAVAT UROBENE WALLY
    "W   W       WW W    W",                #UROB LIST KDE SA BUDE RANDOM PRIDAVAT WALL
    "W WWW  WWWW         W",
    "W   W  W  W W       W",
    "W   W     W   WWW W W",
    "W   WWW W W   W W   W",
    "W         W   W W   W",
    "WWW   W   WWWWW W   W",
    "W        WW         W",
    "W W   WWWW   WWW    W",
    "W   W          W    W",
    "WWWWWWWWWWWWWWWWWWWWW",
]

# Parse the level string above. W = wall, E = exit
print(*level, sep='\n')
x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16
    x = 0
    i = row

running = True
screen = pygame.display.set_mode((len(i)*16,len(level)*16))

while running:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        while ano == False:
            player.move(-2, 0, end_rect)

    if key[pygame.K_RIGHT]:
        while ano == False:
            player.move(2, 0, end_rect)

    if key[pygame.K_UP]:
        while ano == False:
            player.move(0, -2, end_rect)


    if key[pygame.K_DOWN]:
        while ano == False:
            player.move(0, 2, end_rect)

    # Just added this to make it slightly fun ;)

    # Draw the scene
    screen.fill((0, 0, 255))

    player.P_end(end_rect)

    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)

    pygame.draw.rect(screen, (255, 0, 0), end_rect)
    pygame.draw.rect(screen, (255, 200, 0), player.rect)
    ano = False
    pygame.display.flip()