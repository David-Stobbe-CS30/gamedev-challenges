import random
import math
import pygame

screenSize = [1500, 1000]
pygame.init()
screen = pygame.display.set_mode((screenSize[0] - 500, screenSize[1]))


class Player:
    def __init__(self):
        self.x = (screenSize[0] - 500) / 2
        self.y = screenSize[1] - 100
        self.w = 20
        self.h = 20
        self.yv = 0
        self.startY = 0
        self.g = 0.005
        self.jumping = False
        self.onPlatform = False

    def draw(self):
        pygame.draw.rect(screen, "blue", (self.x, self.y, self.w, self.h))
        pygame.draw.line(
            screen, "red", (0, screenSize[1] - 100 + self.h), (screenSize[0], screenSize[1] - 100 + self.h))
        pygame.draw.line(screen, "red", (self.x + self.w, 0),
                         (self.x + self.w, screenSize[1]))

    def move(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a]):
            if (background.x >= screenSize[1] or background.x <= -screenSize[1]):
                self.x -= 1
            else:
                background.x += 1
        elif (keys[pygame.K_d]):
            if (background.x >= screenSize[1] or background.x <= -screenSize[1]):
                self.x += 1
            else:
                background.x -= 1
            # background.x -= 1
        if (keys[pygame.K_w]):
            if (not self.jumping):
                self.startY = self.y
                self.yv = -1
                self.jumping = True
        if (not self.onPlatform and self.y < screenSize[1] - 100):
            self.jumping = True

        if (self.jumping):
            self.jump()

    def jump(self):
        self.yv += self.g
        self.y += self.yv
        if (self.y >= screenSize[1] - 100):
            self.y = screenSize[1] - 100
            self.jumping = False
            self.yv = 0
        elif (self.onPlatform):
            self.jumping = False
            self.yv = 0


class Background:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = screenSize[0]
        self.h = screenSize[1]
        self.platforms = []

    def createPlatforms(self):
        platX = 0
        for n in range(15):
            platX += 200
            if n % 2 == 0:
                platY = screenSize[1] - 200
            else:
                platY = screenSize[1] - 150
            self.platforms.append(Platform(platX, platY, 100, 10))

    def draw(self):
        player.onPlatform = False
        for platform in self.platforms:
            platform.draw()
            platform.collisionCheck()
        player.draw()


class Platform:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = "grey"

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x +
                         background.x, self.y, self.w, self.h))

    def collisionCheck(self):
        if (player.x + player.w - background.x >= self.x and player.x - background.x <= self.x + self.w):
            if (player.y + player.h >= self.y and player.y <= self.y + self.h):
                player.y = self.y - player.h
                player.jumping = False
                player.yv = 0
                player.onPlatform = True


background = Background()
player = Player()


def loop():
    running = True
    background.createPlatforms()
    while running:
        screen.fill("white")
        background.draw()
        player.move()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


loop()
