# pri skuku musim urobit to aby skakyl o menej ale ryhclejsie
#potom dat ak sa y==y1 tak zastane
import pygame
pygame.init() 

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")


#player SET
x = 200
y = 500 - 30
width = 30
height = 30
vel = 5

#box SET
width1 = 60
height1 = 20
x1 = 100
y1 = 440

isJump = False
jumpCount = 50

run = True
while run:
    pygame.time.delay(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    keys = pygame.key.get_pressed()

    #tento program funguje ak neskace
    if keys[pygame.K_LEFT] and not(isJump) and x >= vel and (x >= x1 + 65 or x + 30 <= x1 or y >= y1 + height1 or y + height <= y1): #ak by sme pridali aj x > vel tak byto potom bolo vzdialene 2px od x
        pygame.time.delay(15)
        x -= vel

    if keys[pygame.K_LEFT] and isJump and x >= vel and (x >= x1 + 65 or x + 30 <= x1 or y >= y1 + height1 or y + height <= y1): #ak by sme pridali aj x > vel tak byto potom bolo vzdialene 2px od x
        pygame.time.delay(5)
        x -= vel



    #tento program funguje ak neskace
    if keys[pygame.K_RIGHT] and not(isJump) and x + 35 <= 500 and (x + 35 <= x1 or x >= x1 + 60 or y >= y1 + height1 or y + height <= y1):# and x + 30 <= 500- vel or x + 30 + vel <= x1: # ak by sme dali - vel tak by to bolo potom vzdialene 5px
        pygame.time.delay(15)
        x += vel


    if keys[pygame.K_RIGHT] and isJump and x + 35 <= 500 and (x + 35 <= x1 or x >= x1 + 60 or y >= y1 + height1 or y + height <= y1): # ak by sme dali - vel tak by to bolo potom vzdialene 5p
        pygame.time.delay(5)
        x += vel

    #JUMP ---------------------------------------------/
    if not(isJump):
        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            isJump = True
            a = 0
            b = 0
            hod = True
            pos = y
            print(y)
            teraz = False
    else:
        #ked ide DOLE            
        if teraz:               
            a += 1          #HODNOTA KTORA POTOM UKONCI SKAKANIE
            neg = -1
            y -= neg * 2
            jumpCount -= 1
            print('dole')
         #PROCES NA UKONČENIE SKAKANIA
            if b == a:
                isJump = False
                jumpCount = 50
        #Ked ide HORE
        elif jumpCount >= -10 and y >= pos - 80 and (y != y1 + height1 or x > x1 + 60 or x + 30 < x1) :#and y - 20 >= y1 and x >= x1 and x <= x1 + width and hod == True:
            b += 1          #HODNOTA KTORA POTOM UKONCI SKAKANIE
            neg = 1
            y -= neg * 2
            jumpCount -= 1

        else:
            teraz = True


    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0) ,(x, y, width, height))
    pygame.draw.rect(win, (59, 0, 225), (x1, y1, width1, height1))
    pygame.display.update()
pygame.quit() 







