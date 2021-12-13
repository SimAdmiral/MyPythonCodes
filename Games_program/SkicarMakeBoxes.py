import pygame
import random
import math
import sys
pygame.init()

pygame.display.set_caption('Skicár')
win_x, win_y = 500, 500
screen = pygame.display.set_mode((win_x, win_y))
drawMode = None
buttonClick=False

class NewButton():

    def __init__(self, msg, x, y, w, h, ic, ac, action=None):
        self.msg = msg
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.ic = ic
        self.ac = ac
        self.action = action
        self.drawee = False

    def DrawButton(self):
        global drawMode, buttonClick, imageList

        smallText = pygame.font.Font("freesansbold.ttf", 17)
        textSurf, textRect = text_objects(self.msg, smallText)
        textRect.center = ((self.x + (self.w / 2)), (self.y + (self.h / 2)))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
            pygame.draw.rect(screen, self.ac, (self.x, self.y, self.w, self.h))

            if click[0] == 1 and buttonClick==False:
                buttonClick = True
                drawMode = self.action
                if drawMode == "Clear":
                    imageList.clear()
                    drawMode=None
            else:
                buttonClick = False
        else:
            pygame.draw.rect(screen, self.ic, (self.x, self.y, self.w, self.h))

        screen.blit(textSurf, textRect)

def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

def DrawBox():
    global p, index, x,y
    mous = pygame.mouse.get_pos()

    if press[0] == 1:
        if p == True:
            p = False
            x, y = mous[0], mous[1]
            imageList.append([x, y, mous[0] - x, mous[1] - y, drawMode.__name__])
            index += 1

        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
            imageList[len(imageList)-1][2] = mous[0] - x
            imageList[len(imageList)-1][3] = mous[0] - x
        else:
            imageList[len(imageList)-1][2] = mous[0] - x
            imageList[len(imageList)-1][3] = mous[1] - y
    else:
        pass

def DrawCircel():
    global p,index, x, y
    mous = pygame.mouse.get_pos()
    if press[0] == 1:
        if p == True:
            p = False
            x,y = mous[0], mous[1]
            imageList.append([x,y, mous[0] - x, mous[1] - y , drawMode.__name__])

            index += 1

        if pygame.key.get_mods() & pygame.KMOD_SHIFT:

            imageList[len(imageList)-1][2] = mous[0] - x
            imageList[len(imageList)-1][3] = mous[0] - x
        else:
            imageList[len(imageList)-1][2] = mous[0] - x
            imageList[len(imageList)-1][3] = mous[1] - y

def DrawPolygon():
    global p,index, x, y
    mous = pygame.mouse.get_pos()
    if press[0] == 1:
        if p == True:
            p = False
            x,y = mous[0], mous[1]
            imageList.append([x,y, mous[0] - x, mous[1] - y, drawMode.__name__])

            index += 1

        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
            imageList[len(imageList)-1][2] = mous[0] - x
            imageList[len(imageList)-1][3] = mous[0] - x
        else:
            imageList[len(imageList)-1][2] = mous[0]
            imageList[len(imageList)-1][3] = mous[1]

p = True
imageList = []
index = -1

but1 = NewButton("Box", 10,10,90,40, (255,0,0), (0,255,0), DrawBox)
but2 = NewButton("Circel", 105,10,90,40, (255,0,0), (0,255,0),DrawCircel)
but3 = NewButton("Polygon", 200,10,90,40, (255,0,0), (0,255,0),DrawPolygon)
but4 = NewButton("Clear", 295,10,90,40, (255,0,0), (0,255,0),"Clear")

butlist = [but1, but2, but3, but4]

while True:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.KEYDOWN:
            print("Aaa")

    mous = pygame.mouse.get_pos()
    press = pygame.mouse.get_pressed()

    pygame.draw.rect(screen, (0,150,255) ,(0,0,win_x,60))

    for i in butlist:
        i.DrawButton()

    if press[0] == 0:
        p = True

    if press[0] == 1 and mous[1] > 60 and buttonClick == False and drawMode != None:
        drawMode()

    for i in imageList:
        if i[len(i)-1] == "DrawBox":
            print("DrawBox1")
            pygame.draw.rect(screen, (255, 0, 0), (i[0], i[1], i[2], i[3]), 2)

        if i[len(i)-1] == "DrawPolygon":
            print("DrawPolygon")
            try:
                pygame.draw.polygon(screen, (255, 0, 0), ((i[0], i[3]), (i[2], i[3]), ((i[2] - i[0]) // 2 + i[0], i[1])), 10)
            except:
                print("zle")

        if i[len(i)-1] == "DrawCircel":
            print("DrawCircel")
            pygame.draw.circle(screen, (255, 0, 0), (i[0] + int(i[2] / 2), i[1] + int(i[3] / 2)), int(i[2] / 2))
            # pygame.draw.ellipse(screen, (255, 0, 0), (i[0], i[1], mous[0] - i[0], mous[1] - i[1]))

    pygame.display.update()
    screen.fill((255,255,255))