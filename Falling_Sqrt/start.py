import pygame
import sys
pygame.init()
pygame.display.set_caption("My Game")

win_y = 500
win_x = 500
screen = pygame.display.set_mode((win_x,win_y))
clock = pygame.time.Clock()
#Aquí comensamos
def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()


    if x + w > mouse[0] > x and y + h  > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))

        if click[0] == 1 and msg == 'Play':
            from FALLDAWN import game           #importuje game a potom sa spusti
            game()

        if click[0] == 1 and msg == 'Setting':
            print('SETTING')

        if click[0] == 1 and msg == 'Info':
            from helper import front_page1
            front_page1()

        if click[0] == 1 and msg == 'Quit':
            from quit import quit_game           #importuje game a potom sa spusti
            quit_game()

    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf",50)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)


def front_page():
    print('start')
    while True:
        from quit import quit
        quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            from FALLDAWN import game
            game()

        screen.fill((255,255,255))

        button("Play", win_x/2 - 100, win_y/2 - 110, 200, 60, (70,75,88), (99,199,200))
        button("Setting", win_x/2 - 100, win_y/2 - 40, 200, 60, (70,75,88), (99,199,200))
        button("Info", win_x/2 - 75, win_y/2 + 30, 150, 60, (70,75,88), (90,199, 200))
        button("Quit", win_x/2 - 75, win_y/2 + 100, 150, 60, (70,75,88), (90,199, 200))
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
