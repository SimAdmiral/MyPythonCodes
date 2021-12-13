import pygame
import random
import sys
import os
from Mouse import drawText
pygame.init()

win_x, win_y = 500,500
screen = pygame.display.set_mode((win_x,win_y))
pygame.display.set_caption("TICTACTOE")


text  = [[1,1,1,
          0,0,0,
          0,0,0],
         [0,0,0,
          1,1,1,
          0,0,0],
         [0,0,0,
          0,0,0,
          1,1,1],
         [1,0,0,
          0,1,0,
          0,0,1],
         [0, 0, 1,
          0, 1, 0,
          1, 0, 0],
         [1, 0, 0,
          1, 0, 0,
          1, 0, 0],
         [0, 1, 0,
          0, 1, 0,
          0, 1, 0],
         [0, 0, 1,
          0, 0, 1,
          0, 0, 1]]

def quit_game():
    pygame.quit()
    sys.exit()

padding = 40
# [padding,padding,win_x-padding, padding]
borderPosition = [[0+padding,0 + padding,win_x-padding, 0 + padding], [0+padding,(win_y/3)+(padding/3),win_x-padding, (win_y/3)+(padding/3)],
                  [0+padding,(win_y/3*2)-(padding/3),win_x-padding, (win_y/3*2)-(padding/3)], [0+padding,win_y - padding,win_x-padding, win_y - padding],
                  [0+padding, 0+padding,0+padding, win_y - padding],[(win_x/3)+(padding/3),0+padding, (win_x/3)+(padding/3), win_y-padding],
                  [(win_x/3*2)-(padding/3),0+padding, (win_x/3*2)-(padding/3), win_y-padding],[win_x - padding,0+padding,win_x-padding, win_y - padding]]

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()

    # print(pygame.display.get_surface().get_size())

    #Game Border
    # for i in borderPosition:
    #     pygame.draw.line(screen, (0,0,0), (i[0], i[1]),(i[2],i[3]),15 )

    text_to_draw = drawText(pygame.display.get_surface().get_size(), pygame.mouse.get_pos(), 16, (0,0,0))
    screen.blit(text_to_draw[0], text_to_draw[1])

    pygame.display.update()
    pygame.display.flip()
    screen.fill((255,255,255))
