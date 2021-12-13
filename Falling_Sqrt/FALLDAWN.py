import pygame
import time
import sys
import keyboard
import random
pygame.init()
pygame.display.set_caption("My Game")

win_y = 500
win_x = 500
screen = pygame.display.set_mode((win_x,win_y))
clock = pygame.time.Clock()
BLUE = pygame.Color('dodgerblue3')
ORANGE = pygame.Color('sienna3')
score = 0
missed = 0

#----------TEXT STYLING----------------------
def C_text():
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Falling square', True, (0, 0, 0), (255,255,255))
    textRect = text.get_rect()
    textRect.center = (win_y/2, win_x/2)
    screen.blit(text, textRect)

def S_text():
    global score
    font = pygame.font.Font('freesansbold.ttf', 32)
    text2 = font.render('Score: ' + str(score), True, (0, 0, 0), (0, 0, 250))
    missed_score1 = text2.get_rect()
    missed_score1.center = (75, 32/2)
    screen.blit(text2, missed_score1)


def M_text(missed):

    font = pygame.font.Font('freesansbold.ttf', 32)
    text2 = font.render('Missed: ' + str(missed), True, (0, 0, 0), (0, 0, 250))
    missed_score1 = text2.get_rect()
    missed_score1.center = (410, 32 / 2)
    screen.blit(text2, missed_score1)


class MovingRect(pygame.Rect):

    def __init__(self, x, y, w, h, vel):
        # Calling the __init__ method of the parent class
        super().__init__(x, y, w, h)
        self.vel = vel

    def update(self, enem, enemy):

        self.y += self.vel
        if self.y >= 480:     # If it's not in this area
            global missed
            self.y = 0
            self.x = random.randint(1,470)
            missed += 1



    def update1(self, player):
        self.y = 0
        self.x = random.randint(1, 470)

    def redBox(self, player):
        self.y += self.vel
        if self.y >= win_y:
            self.y = 0
            self.x = random.randint(1,470)

        #------PLAYER COLLIDER SCORE = 0
        if self.colliderect(player):
            self.y = 0
            self.x = random.randint(1,470)
            global score, width
            player.width = 50
            score = 0

    def heals(self, player):
        self.y += self.vel
        if self.colliderect(player):
            player.width += 1



def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()


    if x + w > mouse[0] > x and y + h  > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf",50)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)


def game():

    print('game')
    global score, missed
    score = 0
    missed = 0
    vel = 3
    vel_down = 4
    vel_killer = 3
    score = 0

    #------PLAYER---------------
    height = 20
    width = 100
    x = win_y/2 - width/2
    y = win_y - height - 10

    player = pygame.Rect(x, y, width, height)
    #----Enemy--------------------
    Ex = random.randint(1,win_x - 30)
    Ey = 0
    enemy = [MovingRect(Ex, Ey, 30, 30, vel_down)]
    #---------Killer-------------
    killer = []
    healer = []

    H_time = time.time()
    while True:
        H_time1 = time.time()
        from quit import quit, escape
        quit()
        escape()



        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player.x >= 0:
            player.x -= vel
        if keys[pygame.K_RIGHT] and player.x + player.width <= win_x:
            player.x += vel

        for enem in enemy:
            enem.update(enem, enemy)


            #---------------------VŠETKY TIETO SOMARINY DAJ DO DEFINICII-------------------!!!!!!!!!!!!!!!!!

            if player.colliderect(enem):
                #enem.S_update(player, enemy, enem, killer)
                player.width = 100
                enem.update1(player)
                score += 1

                if score > 1 and score < 3 and len(enemy) < 5: #POZOR MNE S APOTOM VYNULUJE SKORE A SA ZAS PRIDA BOX
                    enemy.append(MovingRect(random.randint(1,win_x - 30), random.randint(-100, -30), 30, 30, vel_down))
                    break

                if score > 10 and score < 12 and len(enemy) < 5: #POZOR MNE S APOTOM VYNULUJE SKORE A SA ZAS PRIDA BOX
                    enemy.append(MovingRect(random.randint(1,win_x - 30), random.randint(-100, -30), 30, 30, vel_down))
                    break

                if score > 5 and score < 7 and len(killer) < 5:
                    killer = [MovingRect(random.randint(1,win_x - 30), Ey, 30, 30, vel_killer)]

        screen.fill((2,200,1))

        if H_time1 - H_time >= 5:
            healer = [MovingRect(random.randint(1,win_x - 15), random.randint(-30,0), 15, 15, vel_killer)]
            H_time = time.time()

        for heal in healer:
            heal.heals(player)

        for heal in healer:
            pygame.draw.rect(screen, (0,255,10), heal)

        for kill in killer:
            kill.redBox(player)

        for kill in killer:
            pygame.draw.rect(screen, (255,0,0), kill)

        for enem in enemy:
            pygame.draw.rect(screen, (25,55,25), enem)

        C_text()
        M_text(missed)
        S_text()

        pygame.draw.rect(screen, (255,40,1), player)
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)  #   TO JE ASI   PINK

def main():
    print('main')
    scene = game  # Set the current scene.

    while scene is not None:
        # Execute the current scene function. When it's done
        # it returns either the next scene or None which we
        # assign to the scene variable.
        scene = scene()

main()
pygame.quit()