import pygame

def drawText(screen, mouse, fontSize, color, background=None):
    win_x,win_y = screen[0], screen[1]

    font = pygame.font.Font('freesansbold.ttf', fontSize)

    if background == None: text = font.render("{} {}".format(mouse[0], mouse[1]), True, color, (255,255,255))
    else: text = font.render("{} {}".format(mouse[0], mouse[1]), True, color, background)

    t = len("{} {}".format(mouse[0], mouse[1]))
    textPos = [mouse[0] + fontSize, mouse[1] + fontSize]

    if mouse[1] + fontSize*2 >= win_y:
        textPos = [mouse[0],mouse[1] - fontSize]

    if (mouse[0] + (fontSize/2*(t+2)) >= win_x):
        textPos[0] = mouse[0] - (fontSize / 2 * (t))

    return  text, textPos
