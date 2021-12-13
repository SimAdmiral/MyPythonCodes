import math, random, sys
import pygame
import os
from pygame.locals import *

# exit the program
def events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


# define display surface
W, H = 820, 680
HW, HH = W / 2, H / 2

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("code.Pylet - Pixel Perfect Collision")
FPS = 120
o = 0       #číslo spritu
vel = 2     #rýchlosť pohybu
rot = 0     #počiatočný smer hore ktorý sa potom meni
rot_v = 1   #rýchlosť otáčania

# define some colors
BLACK = (0, 0, 255, 255)
WHITE = (255, 255, 255, 255)

obstacle = [pygame.image.load("sprites/s1.png").convert_alpha(), pygame.image.load("sprites/s2.png").convert_alpha(), pygame.image.load("sprites/s3.png").convert_alpha(),
pygame.image.load("sprites/s4.png").convert_alpha(), pygame.image.load("sprites/s5.png").convert_alpha()]

obstacle_mask = pygame.mask.from_surface(obstacle[o])
obstacle_rect = obstacle[o].get_rect()

ox = HW - obstacle_rect.center[0]
oy = HH - obstacle_rect.center[1]

rockets = [pygame.image.load("sprites/roc1.png").convert_alpha(), pygame.image.load("sprites/roc2.png").convert_alpha(), pygame.image.load("sprites/roc3.png").convert_alpha(),
           pygame.image.load("sprites/roc4.png").convert_alpha()]
rc = 0
blob_mask = pygame.mask.from_surface(rockets[rc])
blob_rect = rockets[rc].get_rect()
blob_color = rockets[rc]

# main loop
x, y = 400,600

def rotat():
    global rot

    if keys[pygame.K_RIGHT]:
        rot -= rot_v


    if keys[pygame.K_LEFT] :
        rot += rot_v

    if rot < -180:
        rot = -rot
        print('0')

    else:
        if rot > 180:
            rot = -rot
            print('0')

def movee():
    global rot, x, y, rc, vel

    if keys[pygame.K_UP]:

        rc += 1
        if rc >= 4:
            rc = 0
        print(vel)

        if rot > 0 and rot <= 90:
            y -= (1 - (rot/90)) * vel
            x -= (rot / 90 ) * vel
        else:
            if rot > 90 and rot < 180:
                x -= (1 - (rot/90 - 1)) * vel
                y -= (1 - (rot/90)) * vel
        if rot < 0 and rot >= -90:
            y += (-1 - (rot/90)) * vel
            x += (1- (rot/90) - 1) * vel
        else:
            if rot < -90 and rot > -180:
                x += ((rot / 90) + 2) * vel
                y -= ((rot / 90) + 1) * vel
        if rot == 0:
            y -= 1 * vel
        else:
            if rot == 180 or rot == -180:
                y += 1 * vel

    if keys[pygame.K_DOWN]:
        if rot > 0 and rot <= 90:
            y += (1 - (rot/90)) * vel
            x += (rot / 90 ) * vel

        else:
            if rot > 90 and rot < 180:
                x += (1 - (rot/90 - 1)) * vel
                y += (1 - (rot/90)) * vel

        if rot < 0 and rot >= -90:
            y -= (-1 - (rot/90)) * vel
            x -= (1- (rot/90) - 1) * vel
        else:
            if rot < -90 and rot > -180:
                x -= ((rot / 90) + 2) * vel
                y += ((rot / 90) + 1) * vel

        if rot == 0:
            y += 1 * vel
        else:
            if rot == 180 or rot == -180:
                y -= 1 * vel

    if not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
        rc = 0

def drawee():
    global rot,x,y, rc
    rotated_image = pygame.transform.rotate(rockets[rc], rot)
    new_rect = rotated_image.get_rect(center=rockets[rc].get_rect(topleft=(x,y)).center)
    screen.blit(rotated_image,new_rect.topleft)
    screen.blit(obstacle[o], (ox, oy))
    pygame.display.update()

while True:
    events()
    keys =pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        vel = 4
        print('ano')
    else:
        if not keys[pygame.K_SPACE]:
            vel = 2

    movee()
    rotat()

    mx, my = x,y
    offset = int(mx - ox), int(my - oy)
    result = obstacle_mask.overlap(blob_mask, offset)

    if result:
        o += 1
        if o >= 5:
            o = 0
    else:
        o = 0

    drawee()
    pygame.display.update()
    CLOCK.tick(FPS)
    screen.fill(BLACK)
