import pygame
import os
import sys
from pygame.locals import *

pygame.init()

win_x, win_y = 500, 500

screen = pygame.display.set_mode((win_x, win_y))
pygame.display.set_caption('Moving_sprites')

def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

class image:
    def __init__(self, filename, cols , rows, img_c=None):
        self.img = pygame.image.load(filename).convert_alpha()
        self.cols = cols
        self.rows = rows
        self.total = rows*cols
        self.ix = 0
        self.iy = 0
        self.go = True
        self.img_rect = self.img.get_rect()
        self.w = int(self.img_rect.width / cols)
        self.h = int(self.img_rect.height / rows)

        if img_c != None:
            self.img_c = img_c
        else:
            self.img_c = None

    def skip(self):

        if (keys[pygame.K_RIGHT] or keys[pygame.K_UP]) and self.go:
            self.ix += self.w
            self.go = False

            if self.img_c != None and self.ix >= (self.img_c-1) * self.w and self.iy >= (self.rows-1)*self.h:
                self.ix = 0
                self.iy = 0

            if self.ix >= self.cols * self.w:
                self.ix = 0
                self.iy += self.h
                if self.iy >= self.rows * self.h:
                    self.ix, self.iy = 0, 0

        if (keys[pygame.K_LEFT] or keys[pygame.K_DOWN]) and self.go:
            self.ix -= self.w
            self.go = False
            if self.ix < 0:
                self.ix = self.w * (self.cols - 1)
                self.iy -= self.h
                if self.iy < 0:
                    self.iy = self.h * (self.rows - 1)
                    if self.img_c != None:
                        self.ix = self.w * (self.img_c - 1)
                        #self.iy = self.h * self.rows

        if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            self.go = True

    def draw(self): #              pozicie obrazkov ktore vykresľuje           (poxeli)
        screen.blit(self.img, (200, 200), (self.ix, self.iy, self.w, self.h)) #self.w, self.h to je pozícia kde sú umiestnený
        pygame.display.update()

path = '..\sprites'
#pet = image(path + "RainbowIslandsCharacter.png",  7,4 )
pet1 = image("sprites/rocks.png",  2,3 , 1)
l = [pet1]#, pet]

while True:

    events()
    keys = pygame.key.get_pressed()

    for i in l:
        i.skip()
        i.draw()

    pygame.display.update()
    screen.fill((255,255,255))
    pygame.time.delay(50)