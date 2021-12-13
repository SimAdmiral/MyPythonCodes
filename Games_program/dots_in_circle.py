import pygame
import random
import math
import sys
pygame.init()

pygame.display.set_caption('Dots in circle')
win_x, win_y = 500, 500

screen = pygame.display.set_mode((win_x,win_y))
dots = 1000
dotest = []
c = 50
c1 , c2 = win_x/2, win_y/2

class Circle:
    def __init__(self):
        global m1, m2
        self.x, self.y = int(random.randint(0, 500)),int(random.randint(0, 500))
        self.r = 4


    def cdraw(self):
        self.color = (0, 255, 255)
        mous = pygame.mouse.get_pos()
        pres = pygame.mouse.get_pressed()
        if pres[0] == 1:
            pygame.draw.circle(screen, (0, 0, 0), (int(mous[0]), int(mous[1])), c, 2)
            self.x1, self.y1 = mous[0]- self.x , mous[1] - self.y
            if self.x1 <= 0:
                self.x1 = -self.x1
            if self.y1 <= 0:
                self.y1 = -self.y1

            self.sq = math.sqrt(self.x1 ** 2 + self.y1 ** 2)
            if self.sq + 4 <= c: #+4 lebo započitavame aj hrúbku strany
                # self.color = (0, 0, 20)
                dotest.remove(self)
        pygame.draw.circle(screen, self.color, (self.x,self.y), self.r)

        # try:
        #     pygame.draw.circle(screen, self.color, (self.x,self.y), self.r)
        # except:
        #     print('afs')

for i in range(dots):
    circle = Circle()
    dotest.append(circle)

def close():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
go = True
n = True
while True:
    close()
    mous = pygame.mouse.get_pos()
    pres = pygame.mouse.get_pressed()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and go:
        circle = Circle()
        dotest.append(circle)
        go = False
    else:
        if not keys[pygame.K_UP]:
            go = True

    if keys[pygame.K_r]:
        dotest.clear()
    if keys[pygame.K_n] and n:
        for i in range(dots):
            circle = Circle()
            dotest.append(circle)
        n = False
    if not keys[pygame.K_n]:
        n = True
    for i in dotest:
        i.cdraw()
    pygame.draw.circle(screen, (0, 0, 0), (int(mous[0]), int(mous[1])), c, 2) #kresli kruh cireny

    pygame.display.update()
    screen.fill((255,255,255))
