import pygame
pygame.init()
pygame.display.set_caption("My Game")

win_y = 500
win_x = 500
screen = pygame.display.set_mode((win_x,win_y))
clock = pygame.time.Clock()

def front_page1():
    print('info')

    while True:
        from quit import quit, escape
        quit()
        escape()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            import FALLDAWN
        screen.fill((255,0,255))
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

