import pygame
import sys


pygame.init()
pygame.display.set_caption("My Game")
screen_width, screen_height = 1200, 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
BLUE = pygame.Color('dodgerblue3')
ORANGE = pygame.Color('sienna3')
BLACK = (0, 0, 0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (13, 255, 0)
YELLOW = (0, 255, 20)
BRIGHT_YELLOW = (255, 255, 20)

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
        if self.top < 20 or self.bottom > screen_height-20:
            self.vel = -self.vel


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
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        screen.fill(BLUE)

        button("Restart", 525, 250, 150, 60, BRIGHT_YELLOW, YELLOW, menu)
        button("Quit", 525, 350, 150, 60, BRIGHT_YELLOW, YELLOW, quit_game)

        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

def front_page():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        screen.fill(WHITE)

        button("Start", 525, 250, 150, 60, BRIGHT_YELLOW, YELLOW, menu)
        button("Quit", 525, 350, 150, 60, BRIGHT_YELLOW, YELLOW, quit_game)

        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)


def menu():
    vel = 4
    vel_left = 5
    vel_right = -5

    player = pygame.Rect(40, 45, 30, 30)

    walls = [
        pygame.Rect(0, 0, 1200, 20), pygame.Rect(0, 0, 20, 600),
        pygame.Rect(0, 580, 1200, 20), pygame.Rect(1180, 0, 20, 600),
        pygame.Rect(300, 0, 20, 530), pygame.Rect(20, 100, 230, 20),
        pygame.Rect(70, 200, 230, 20), pygame.Rect(20, 300, 230, 20),
        pygame.Rect(70, 400, 230, 20), pygame.Rect(600, 100, 20, 500)
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

    movingrects3 = [
        MovingRect(700, 20, 30, 30, vel_left),
        MovingRect(820, 20, 30, 30, vel_left),
        MovingRect(940, 450, 30, 30, vel_right),
        MovingRect(1060, 450, 30, 30, vel_right)
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        keys = pygame.key.get_pressed()

        # Player coordinates
        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= vel
        if keys[pygame.K_RIGHT] and player.x < 1200 - player.width:
            player.x += vel
        if keys[pygame.K_UP] and player.y > 0:
            player.y -= vel
        if keys[pygame.K_DOWN] and player.y < 600 - player.height:
            player.y += vel

        for wall in walls:
            # Check if the player rectangle collides with a wall rectangle
            if player.colliderect(wall):
                print("Game over")
                pygame.time.wait(1000)
                restart()

        for movingrect in movingrects:
            movingrect.update()  # Movement and bounds checking
            if player.colliderect(movingrect):
                print("Game over")

        # TO DO #
        for movingrect2 in movingrects2:
            movingrect2.update2()
            if player.colliderect(movingrect2):
                print("Game over")

        for movingrect3 in movingrects3:
            movingrect3.update3()
            if player.colliderect(movingrect3):
                print("Game over")

        # Drawing everything
        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, player)

        for wall in walls:
            pygame.draw.rect(screen, BLACK, wall)

        for movingrect in movingrects:
            pygame.draw.rect(screen, GREEN, movingrect)

        for movingrect2 in movingrects2:
            pygame.draw.rect(screen, GREEN, movingrect2)

        for movingrect3 in movingrects3:
            pygame.draw.rect(screen, RED, movingrect3)


        pygame.draw.rect(screen, BLACK, player)
        pygame.display.update()

        pygame.display.flip()
        clock.tick(60)


def main():
    scene = front_page  # Set the current scene.
    while scene is not None:
        # Execute the current scene function. When it's done
        # it returns either the next scene or None which we
        # assign to the scene variable.
        scene = scene()


main()
pygame.quit()