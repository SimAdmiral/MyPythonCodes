import pygame
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
    text = font.render('Falling square', True, (255, 255, 100), (255, 192, 203))
    textRect = text.get_rect()
    textRect.center = (win_y/2, win_x/2)
    screen.blit(text, textRect)

def S_text(score):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text1 = font.render('Score: ' + str(score), True, (0, 0, 0), (0, 0, 250))
    text_score = text1.get_rect()
    text_score.center = (65, 32 / 2)
    text1 = font.render('Score: ' + str(score), True, (0, 0, 0), (0, 0, 250))
    screen.blit(text1, text_score)

def M_text(missed):

    font = pygame.font.Font('freesansbold.ttf', 32)
    text2 = font.render('Missed: ' + str(missed), True, (0, 0, 0), (0, 0, 250))
    missed_score = text2.get_rect()
    missed_score.center = (410, 32 / 2)
    screen.blit(text2, missed_score)


class MovingRect(pygame.Rect):

    def __init__(self, x, y, w, h, vel):
        # Calling the __init__ method of the parent class
        super().__init__(x, y, w, h)
        self.vel = vel

    def update(self):

        self.y += self.vel
        if self.y >= 480:     # If it's not in this area
            global missed
            print(missed)
            self.vel = -self.vel    # Inverting the direction
            missed += 1
            print(missed)


        if self.y < 0:
            self.vel = -self.vel


    # def update2(self, enemy):
    #     self.x += self.vel
    #     if self.right > 1180 or self.left < 620:
    #         self.vel = -self.vel
    #
    # def update3(self):
    #     self.y += self.vel
    #     if self.top > 20 or self.bottom < 400:
    #         self.vel = -self.vel

def quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()



def quit_game():
    pygame.quit()
    sys.exit()

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

def front_page():
    print('start')

    while True:
        quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game()

        screen.fill((255,255,255))

        button("Play", win_x/2 - 100, win_y/2, 200, 60, (70,75,88), (99,199,200), game)
        button("Quit", win_x/2 - 75, win_y/2 + 80, 150, 60, (70,75,88), (90,199, 200), quit_game)
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

def game():

    print('game')

    vel = 5
    vel_down = 5
    score = 0

    #------PLAYER---------------
    height = 20
    width = 100
    x = win_y/2 - width/2
    y = win_y - height - 10
    player = pygame.Rect(x, y, width, height)
    Ex = random.randint(1,win_x - 30)
    Ey = 0

    enemy = [MovingRect(Ex, Ey, 30, 30, vel_down)]

    while True:
        quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player.x >= 0:
            player.x -= vel
        if keys[pygame.K_RIGHT] and player.x + player.width <= win_x:
            player.x += vel

        for enem in enemy:
            enem.update()

            if player.colliderect(enem):
                Ey = 0
                Ex = random.randint(1,win_x - 30)
                score += 1
                enemy = [MovingRect(Ex, Ey, 30, 30, vel_down)]

        screen.fill((2,200,1))

        for enem in enemy:
            pygame.draw.rect(screen, (25,55,25), enem)

        C_text()
        M_text(missed)
        S_text(score)

        pygame.draw.rect(screen, (255,40,1), player)
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

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