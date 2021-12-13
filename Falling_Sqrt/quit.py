import  pygame
import sys
pygame.init()

def quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()

def quit_game():
    pygame.quit()
    sys.exit()

def escape():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        from start import front_page
        front_page()