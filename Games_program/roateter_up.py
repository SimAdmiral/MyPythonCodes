import pygame
import random
pygame.init()

win_x = 1000
win_y = 700

screen = pygame.display.set_mode((win_x,win_y))
img = pygame.transform.scale2x(pygame.image.load("sprites/L3.png"))
img = pygame.transform.flip(img, False, False)
vel = 0
y = 250
x = 100
screen.fill((255,255,255))

class Player():

    def __init__(self, x, y, w, h):
        # Calling the __init__ method of the parent class
        self.y = y
        self.x = x
        self.h = h
        self.w = w
        self.vel = 0
        self.a = 1

    def rotat(self):
        if keys[pygame.K_RIGHT]: #otočka do prava 'odčitava sa'
            self.vel -= 0.5
        if keys[pygame.K_LEFT]: #otočka do ľava 'sčítava sa'
            self.vel += 0.5

        if self.vel < -180:
            self.vel = -self.vel
        else:
            if self.vel > 180:
                self.vel = -self.vel


    def movee(self):
        if keys[pygame.K_SPACE]:
            self.a = 2
        else:
            if not keys[pygame.K_SPACE]:
                self.a = 1

        if keys[pygame.K_UP]:
            if self.vel > 0 and self.vel < 90:
                self.y -= (1 - (self.vel/90)) * self.a
                self.x -= (self.vel / 90) * self.a
            else:
                if self.vel > 90 and self.vel < 180:
                    self.x -= (1 - (self.vel/90 - 1)) * self.a
                    self.y -= (1 - (self.vel/90)) * self.a
            if self.vel < 0 and self.vel > -90:
                self.y += (-1 - (self.vel/90)) * self.a
                self.x += (1- (self.vel/90) - 1) * self.a
            else:
                if self.vel < -90 and self.vel > -180:
                    self.x += ((self.vel / 90) + 2) * self.a
                    self.y -= ((self.vel / 90) + 1) * self.a
            if self.vel == 0:
                self.y -= 1 * self.a
            else:
                if self.vel == 180 or self.vel == -180:
                    self.y += 1  * self.a
            if not keys[pygame.K_SPACE]:
                self.a = 1

        if keys[pygame.K_DOWN]:
            if self.vel > 0 and self.vel < 90:
                self.y += 1 - (self.vel/90)
                self.x += self.vel / 90
            else:
                if self.vel > 90 and self.vel < 180:
                    self.x += 1 - (self.vel/90 - 1)
                    self.y += 1 - (self.vel/90)
            if self.vel < 0 and self.vel > -90:
                self.y -= -1 - (self.vel/90)
                self.x -= 1- (self.vel/90) - 1
            else:
                if self.vel < -90 and self.vel > -180:
                    self.x -= (self.vel / 90) + 2
                    self.y += (self.vel / 90) + 1
            if self.vel == 0:
                self.y += 1
            else:
                if self.vel == 180 or self.vel == -180:
                    self.y -= 1

    def drawe(self):
        rotated_image = pygame.transform.rotate(img, self.vel)
        new_rect = rotated_image.get_rect(center=img.get_rect(topright=(self.x, self.y)).center)
        screen.blit(rotated_image, new_rect.topright)

p = img.get_rect()
p.x, p.y = 200,200
pleyer = Player(p.x, p.y, p.w, p.h)

e_x, e_y, e_w, e_h = 500, 100, 50, 50
enemy = pygame.Rect(e_x, e_y, e_w, e_h)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    keys = pygame.key.get_pressed()

    # if pleyer.colliderect(enemy):
    #     print('collider rect')
    pleyer.rotat()
    pleyer.movee()
    pygame.time.delay(1)
    screen.fill((255,255,255))
    pleyer.drawe()
    pygame.draw.rect(screen, (255,0,0), enemy)
    pygame.display.update()





#
# #TO ISE IBA V  JE AJ STARY KOD
# import pygame
# import random
# pygame.init()
#
# win_x = 1000
# win_y = 700
#
# screen = pygame.display.set_mode((win_x,win_y))
# pygame.display.set_caption('ROCKER->FLY')
#
# #player
# img = pygame.image.load("rocket.png").convert_alpha()
# img_mask = pygame.mask.from_surface(img)
# img_rect = img.get_rect()
# px = win_x - img_rect.center[0]
# py = win_y - img_rect.center[1]
#
# #enemy
# enemy = pygame.image.load("shotting_star.png").convert_alpha()
# enemy_mask = pygame.mask.from_surface(enemy)
# enemy_rect = enemy.get_rect()
# enemy_color = enemy
# ox = (win_x/2) - enemy_rect.center[0]
# oy = (win_y/2) - enemy_rect.center[1]
#
# vel = 0
# screen.fill((255,255,255))
#
# class Player(pygame.Rect):
#
#     def __init__(self, x, y, w, h):
#         # Calling the __init__ method of the parent class
#         super().__init__(x, y, w, h)
#         self.vel = 0
#
#     def drawee(self, vel, x,y):
#         self.vel = vel
#         self.x = x
#         self.y = y
#         rotated_image = pygame.transform.rotate(img, self.vel)
#         new_rect = rotated_image.get_rect(center=img.get_rect(topleft=(self.x,self.y)).center)
#         screen.blit(rotated_image, new_rect.topleft)
#
# def rotat():
#     global vel
#     if keys[pygame.K_RIGHT]:
#         vel -= 0.5
#
#     if keys[pygame.K_LEFT]:
#         vel += 0.5
#
#     if vel < -180:
#         vel = -vel
#     else:
#         if vel > 180:
#             vel = -vel
#
# def movee():
#     global vel, x, y
#     if keys[pygame.K_UP]:
#         if vel > 0 and vel <= 90:
#             y -= 1 - (vel/90)
#             x -= vel / 90
#
#         else:
#             if vel > 90 and vel < 180:
#                 x -= 1 - (vel/90 - 1)
#                 y -= 1 - (vel/90)
#
#         if vel < 0 and vel >= -90:
#             y += -1 - (vel/90)
#             x += 1- (vel/90) - 1
#         else:
#             if vel < -90 and vel > -180:
#                 x += (vel / 90) + 2
#                 y -= (vel / 90) + 1
#
#         if vel == 0:
#             y -= 1
#         else:
#             if vel == 180 or vel == -180:
#                 y += 1
#
#     if keys[pygame.K_DOWN]:
#         if vel > 0 and vel <= 90:
#             y += 1 - (vel/90)
#             x += vel / 90
#
#         else:
#             if vel > 90 and vel < 180:
#                 x += 1 - (vel/90 - 1)
#                 y += 1 - (vel/90)
#
#         if vel < 0 and vel >= -90:
#             y -= -1 - (vel/90)
#             x -= 1- (vel/90) - 1
#         else:
#             if vel < -90 and vel > -180:
#                 x -= (vel / 90) + 2
#                 y += (vel / 90) + 1
#
#         if vel == 0:
#             y += 1
#         else:
#             if vel == 180 or vel == -180:
#                 y -= 1
#
# p = img.get_rect()
# p.x, p.y = 200,200
# pleyer = Player(p.x, p.y, p.w, p.h)
# x,y = p.x, p.y
#
#
# while True:
#
#     print(x)
#     offest = int(x- ox), int(y-oy)
#     result = img_mask.overlap(img_mask, offest)
#
#     print(offest, result)
#     if result:
#         print('saf')
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             quit()
#     keys = pygame.key.get_pressed()
#
#     rotat()
#     movee()
#
#     #if pleyer.colliderect(enemy):
#      #   print('ZLE!!')
#
#     pygame.time.delay(1)
#     screen.fill((255,255,255))
#     pleyer.drawee(vel, x, y)
#     screen.blit(enemy_color, (win_x/2, win_y/2))
#     pygame.display.update()
#     pygame.display.flip()