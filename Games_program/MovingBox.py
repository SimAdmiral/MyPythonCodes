import pygame
import sys
import keyboard


pygame.init()
pygame.display.set_caption("My Game")
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()
BLUE = pygame.Color('dodgerblue3')
ORANGE = pygame.Color('sienna3')

BLACK = (0, 0, 0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (13, 255, 0)
YELLOW = (0, 255, 20)
BRIGHT_YELLOW = (255, 255, 20)
a = 0
width = 40
height = 40

class MovingRect(pygame.Rect):

    def __init__(self, x, y, w, h, vel):
        # Calling the __init__ method of the parent class
        super().__init__(x, y, w, h)
        self.vel = vel

    def update(self):
        self.x += self.vel  # Moving
        if self.right > 600 or self.left < 320:  # If it's not in this area
            self.vel = -self.vel  # Inverting the direction


    def update2(self):
        self.x += self.vel
        if self.right > 1180 or self.left < 620:
            self.vel = -self.vel


    def update3(self):
        self.y += self.vel
        if self.top > 20 or self.bottom < 400:
            self.vel = -self.vel
            print(self.top)

def quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()



def quit_game():
    pygame.quit()
    sys.exit()

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
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

def restart():

    print('restart')

    while True:
        quit()

        screen.fill(BLUE)

        keys = pygame.key.get_pressed()
        if keyboard.is_pressed('R') or keys[pygame.K_SPACE]:
            menu()

        button("Restart", 525, 250, 150, 60, BRIGHT_YELLOW, YELLOW, menu)
        button("Quit", 525, 350, 150, 60, BRIGHT_YELLOW, YELLOW, quit_game)

        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

def front_page():
    print('start')

    while True:
        quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            menu()

        screen.fill(WHITE)

        button("Začiatok", 525, 250, 200, 60, BRIGHT_YELLOW, YELLOW, menu)
        button("Quit", 525, 350, 150, 60, BRIGHT_YELLOW, YELLOW, quit_game)

        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

def menu():
    print('game')
    c = False
    but = False
    a = 0
    vel = 4
    vel_left = 5
    vel_right = -5
    x = 40
    y = 45
    width = 30
    height = 30
    player = pygame.Rect(x, y, width, height)

    walls = [
        pygame.Rect(0, 0, 1200, 20), pygame.Rect(0, 0, 20, 600),
        pygame.Rect(0, 580, 1200, 20), pygame.Rect(1180, 0, 20, 600),
        pygame.Rect(300, 0, 20, 530), pygame.Rect(20, 100, 230, 20),
        pygame.Rect(70, 200, 230, 20), pygame.Rect(20, 300, 230, 20),
        pygame.Rect(70, 400, 230, 20), pygame.Rect(600, 100, 20, 500)
    ]

    finish = [                                          #1200x600
        pygame.Rect(1150,550, 50, 50)
    ]
    movingrects = [
        MovingRect(320, 120, 30, 30, vel_left),
        MovingRect(320, 240, 30, 30, vel_left),
        MovingRect(320, 360, 30, 30, vel_left),
        MovingRect(570, 180, 30, 30, vel_right),
        MovingRect(570, 300, 30, 30, vel_right),
        MovingRect(570, 420, 30, 30, vel_right)
    ]

    movingrects2 = [
        MovingRect(1140, 120, 30, 30, vel_left),
        MovingRect(1140, 240, 30, 30, vel_left),
        MovingRect(1140, 360, 30, 30, vel_left),
        MovingRect(620, 180, 30, 30, vel_right),
        MovingRect(620, 300, 30, 30, vel_right),
        MovingRect(620, 420, 30, 30, vel_right),
    ]

    movingrects3 = [  # BLACK BOX MOOVING
        MovingRect(700, 20, 30, 30, vel_left), #UPPER BOX
        MovingRect(820, 20, 30, 30, vel_left),
        MovingRect(940, 450, 30, 30, vel_right), #DOWN BOX
        MovingRect(1060, 480, 30, 30, vel_right)
    ]

    while True:
        screen.fill(WHITE)
        quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]  and width == 30 and height == 30 :
            a += 1
            if a == 1:
                width, height = 10, 10
                player = pygame.Rect(player.x + 30/3 , player.y + 30/3, width, height)

        #TO X A Y JE V PLAYER.X A PLAYER.Y
        if keys[pygame.K_SPACE] and width == 10 and height == 10:
            a += 1
            if a == 1:
                width, height = 30, 30
                player = pygame.Rect(player.x - 30/3, player.y - 30/3, width, height)

        if not keys[pygame.K_SPACE]:
            a = 0

        # Player coordinates

        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= vel
        if keys[pygame.K_RIGHT] and player.x < 1200 - player.width:            #PROBLE S COLIDER JE TEN žE AK MAM VIAC
            player.x += vel                                                    #BOXOV TAK TO Už NEFUNGUJE IDE TO LEBO nvm
        if keys[pygame.K_UP] and player.y > 0:
            player.y -= vel
        if keys[pygame.K_DOWN] and player.y < 600 - player.height:
            player.y += vel


        #////////////////   FOR LOOP ////////////////--------------------------------------------------------------------------


        for wall in walls:
            if player.colliderect(wall):
                break

        for fin in finish:                                              #if player.colliderect(fin) or player.colliderect(wall):
            if player.colliderect(fin):                                 #   but = True
                pass                                                   #   c = True
            if player.colliderect(wall) or player.colliderect(fin):     #     break
                but = True
                c = True                                                #if not player.colliderect(fin) and not player.colliderect(wall):
            else:                                                       #     but = False
                but = False                                             #     c = False
                c = False

        #     # Check if the player rectangle collides with a wall rectangle
        #      if player.colliderect(wall):
        #         print("Game overkkkk")
        #         #pygame.time.wait(500)
        #         #restart()
        #
        # for fin in finish:
        #     if player.colliderect(fin):
        #         but = True
        #         c = True
        #         break
        #     if not player.colliderect(fin):
        #         but = False
        #         c = False




        for movingrect in movingrects:
            movingrect.update()                     # Movement and bounds checking
            if player.colliderect(movingrect):      # If green box collider with you
                print("Game oveasdr")
                pygame.time.wait(1000)
                restart()
        # TO DO #
        for movingrect2 in movingrects2:
            movingrect2.update2()
            if player.colliderect(movingrect2):
                print("Gamsadase over")         #If you collider with second green box
                pygame.time.wait(1000)
                restart()

        for movingrect3 in movingrects3:
            movingrect3.update2()
            if player.colliderect(movingrect3):
                print("roh")                     #Roh if you collider with black box
                pygame.time.wait(1000)
                restart()

        # Drawing everything
        for fin in finish:
            pygame.draw.rect(screen, (255, 40, 66 ), fin)


        for wall in walls:
            pygame.draw.rect(screen, BLACK, wall)

        #
        # for fin in finish:
        #     pygame.draw.rect(screen, (255, 40, 66), fin)

        for movingrect in movingrects:
            pygame.draw.rect(screen, GREEN, movingrect)

        for movingrect2 in movingrects2:
            pygame.draw.rect(screen, GREEN, movingrect2)

        for movingrect3 in movingrects3:
            pygame.draw.rect(screen, BLACK, movingrect3)

        if but == True:
            button("Next", 550, 250, 150, 100, BRIGHT_YELLOW, YELLOW, menu)
            vel = 0
            if keys[pygame.K_SPACE]:
                restart()

        pygame.draw.rect(screen, RED, player)
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

def main():
    print('main')

    scene = front_page  # Set the current scene.
    while scene is not None:
        # Execute the current scene function. When it's done
        # it returns either the next scene or None which we
        # assign to the scene variable.
        scene = scene()

main()
pygame.quit()