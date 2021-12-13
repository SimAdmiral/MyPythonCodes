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

# define some colors
BLACK = (0, 0, 255, 255)
WHITE = (255, 255, 255, 255)

class rocket:

    def __init__(self):
        self.rockets = [pygame.image.load("sprites/roc1.png").convert_alpha(),
                   pygame.image.load("sprites/roc2.png").convert_alpha(),
                   pygame.image.load("sprites/roc3.png").convert_alpha(),
                   pygame.image.load("sprites/roc4.png").convert_alpha()]

        self.rot = 0
        self.x = 10
        self.y = 10
        self.rc = 0
        self.blob_mask = pygame.mask.from_surface(self.rockets[self.rc])
        self.blob_rect = self.rockets[self.rc].get_rect()
        self.blob_color = self.rockets[self.rc]
        self.o = 0  # číslo spritu
        self.vel = 1  # rýchlosť pohybu
        self.rot = 0  # počiatočný smer hore ktorý sa potom meni
        self.rot_v = 1  # rýchlosť otáčania
        self.ano = False

    def rotat(self):
        if keys[pygame.K_RIGHT]:
            self.rot -= self.rot_v

        if keys[pygame.K_LEFT]:
            self.rot += self.rot_v

        if self.rot < -180:
            self.rot = -self.rot
        else:
            if self.rot > 180:
                self.rot = -self.rot

    def movee(self):

        if keys[pygame.K_UP]:
            self.rc += 1
            if self.rc >= 4:
                self.rc = 0

            if self.rot < 0 and self.rot >= -90:
                self.y += (-1 - (self.rot / 90)) * self.vel
                self.x += (1 - (self.rot / 90) - 1) * self.vel
            else:
                if self.rot < -90 and self.rot > -180:
                    self.x += ((self.rot / 90) + 2) * self.vel
                    self.y -= ((self.rot / 90) + 1) * self.vel

            if self.rot > 0 and self.rot <= 90:
                self.y -= (1 - (self.rot / 90)) * self.vel
                self.x -= (self.rot / 90) * self.vel
            else:
                if self.rot > 90 and self.rot < 180:
                    self.x -= (1 - (self.rot / 90 - 1)) * self.vel
                    self.y -= (1 - (self.rot / 90)) * self.vel

            if self.rot == 0:
                self.y -= 1 * self.vel
            else:
                if self.rot == 180 or self.rot == -180:
                    self.y += 1 * self.vel

        if keys[pygame.K_DOWN]:
            if self.rot > 0 and self.rot <= 90:
               self.y += (1 - (self.rot / 90)) * self.vel
               self.x += (self.rot / 90) * self.vel

            else:
                if self.rot > 90 and self.rot < 180:
                    self.x += (1 - (self.rot / 90 - 1)) * self.vel
                    self.y += (1 - (self.rot / 90)) * self.vel

            if self.rot < 0 and self.rot >= -90:
                self.y -= (-1 - (self.rot / 90)) * self.vel
                self.x -= (1 - (self.rot / 90) - 1) * self.vel
            else:
                if self.rot < -90 and self.rot > -180:
                    self.x -= ((self.rot / 90) + 2) * self.vel
                    self.y += ((self.rot / 90) + 1) * self.vel

            if self.rot == 0:
                self.y += 1 * self.vel
            else:
                if self.rot == 180 or self.rot == -180:
                    self.y -= 1 * self.vel

        if not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            rc = 0

    def drawee(self):
        rotated_image = pygame.transform.rotate(self.rockets[self.rc], self.rot)
        new_rect = rotated_image.get_rect(center=self.rockets[self.rc].get_rect(topleft=(self.x, self.y)).center)
        screen.blit(rotated_image, new_rect.topleft)
        pygame.display.update()

ro = rocket()
while True:
    events()
    keys =pygame.key.get_pressed()

    if keys[pygame.K_SPACE]: ro.vel = 4
    else:
        ro.vel = 1
    ro.rotat()
    ro.movee()
    ro.drawee()

    pygame.display.update()
    CLOCK.tick(FPS)
    screen.fill(BLACK)