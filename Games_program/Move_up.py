import pygame
import sys
import random
pygame.init()
pygame.display.set_caption('Move_Up')
clock = pygame.time.Clock()         #----FPS----

win_y = 500
win_x = 500
screen = pygame.display.set_mode((win_x,win_y))

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


class MovingRect(pygame.Rect):
    def __init__(self, x,y,w,h,vel):
        super().__init__(x,y,w,h)
        self.vel = vel

    def update(self, vel_down, movingrect, movingrects):
        #MUSÍ BYŤ UDANE TIETO ÚDAJE KTORE SU HORE CO SA COMU ROVNA
        self.y += vel_down
        self.x = self.x
        self.w = self.w
        self.h = 20

        #LINA KTORA DELETUJE BLOKY KTORE ODÝDU Z SCREENU
        if self.y > 500:
            movingrects.remove(movingrect)

def front_page():
    print('start')
    pygame.init()
    while True:
        quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game()

        screen.fill((255,255,255))

        button("Play", win_x/2 - 100, win_y/2 - 110, 200, 60, (70,75,88), (99,199,200), game)
        button("Setting", win_x/2 - 100, win_y/2 - 40, 200, 60, (70,75,88), (99,199,200), quit_game)
        button("Info", win_x/2 - 75, win_y/2 + 30, 150, 60, (70,75,88), (90,199, 200), quit_game)
        button("Quit", win_x/2 - 75, win_y/2 + 100, 150, 60, (70,75,88), (90,199, 200), quit_game)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)

def game():
    x = 0
    vel_Up = 3
    vel_D = 3
    vel_L = 3
    vel_R = 3
    vel_down = 1
    vel_D1 = 2
    player = pygame.Rect(win_x/2 - 10, 460, 20, 20)
    # movingrects = [
    #     MovingRect(0, i, random.randint(0, win_x-100), 30, vel_down),
    #     MovingRect(0, i - 200, random.randint(0, win_x - 100), 30, vel_down),
    #     MovingRect(0, i - 200, random.randint(0, win_x - 100), 30, vel_down)
    # ]
    movingrects = []
    movingrects.append(MovingRect(0, 0, random.randint(200, win_x-100), 20, vel_down))

    while True:
        quit()
        keys = pygame.key.get_pressed()

        #MOVING CONTROLS

        if keys[pygame.K_RIGHT] and player.x + 20 + vel_R <= win_x:
            player.x += vel_R

        if keys[pygame.K_LEFT] and player.x - vel_L >= 0:
            player.x -= vel_L

        if keys[pygame.K_DOWN] and player.y <= 470:
            player.y += vel_D

        if keys[pygame.K_UP] and vel_Up == 3:
            player.y -= vel_Up

        #ABY NEUSTALE IšIEL DOLE
        else:

            if not keys[pygame.K_DOWN] and player.y <= 470:
                player.y += vel_D1

        # -----------------------UP SECTION---------------------------------
        for movingrect in movingrects:
            player.y -= 5
            if player.colliderect(movingrect) and keys[pygame.K_UP]:
                vel_Up = 0
                player.y += 5
                break
            else:
                if player.colliderect(movingrect):
                    vel_Up = 0
                    player.y += 5
                    break
                else:
                    vel_Up = 3
            player.y += 5

            # -----------------------LEFT SECTION---------------------------------
            player.x-= 3
            if player.colliderect(movingrect) and keys[pygame.K_LEFT]:
                vel_L = 0
                player.x += 3
                break
            else:
                if player.colliderect(movingrect):
                    vel_L = 0
                    player.x += 3
                    break
                else:
                    vel_L = 3
            player.x += 3

            # -----------------------RIGHT SECTION---------------------------------
            player.x += 3
            if player.colliderect(movingrect) and keys[pygame.K_RIGHT]:
                vel_R = 0
                player.x -= 3
                break
            else:
                if player.colliderect(movingrect):
                    vel_R = 0
                    player.x -= 3
                    break
                else:
                    vel_R = 3
            player.x -= 3

            #-----DOWN SECTION-------------------------
            player.y += 2
            if player.colliderect(movingrect) and keys[pygame.K_DOWN]:
                vel_D = 0
                player.y -= 2
                break
            else:
                if player.colliderect(movingrect):
                    vel_D = 0
                    vel_D1 = 1
                    player.y -= 2
                    break
                else:
                    vel_D = 3
                    vel_D1 = 2
            player.y -= 2

        for movingrect in movingrects:
            movingrect.update(vel_down, movingrect, movingrects)
            if movingrect[1] == 100:
                x = random.randint(0,2)
                if x == 0:
                    movingrects.append(MovingRect(0, 0, random.randint(200, win_x - 100), 20, vel_down))

                if x == 1:
                    a = random.randint(200, win_x - 100)
                    movingrects.append(MovingRect(500-a, 0, a, 20, vel_down))

                if x == 2:
                    a = random.randint(100,350)
                    movingrects.append(MovingRect(random.randint(200, win_x - 100), 0, a, 20, vel_down))


        screen.fill((255,255,255))
        pygame.draw.rect(screen, (0,255,0), player)
        for movingrect in movingrects:
            pygame.draw.rect(screen, (0,0,0), movingrect)

        pygame.draw.rect(screen, (0,255,0), player)
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)


def main():
    print('main')
    scene = front_page  # Set the current scene.

    while scene is not None:
        scene = scene()

main()
pygame.quit()