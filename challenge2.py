# CHALLENGE 1
import pygame
import random
import math
startingPos = [50, 50]
screenSize = [1000, 1000]
pygame.init()
screen = pygame.display.set_mode((screenSize[0], screenSize[1]))


class wall:
    def __init__(self):
        self.x = random.randint(0, screenSize[0])
        self.y = random.randint(0, screenSize[1])
        self.w = random.randint(50, 100)
        self.h = random.randint(50, 100)
        self.sides = {
            "left": [self.x-player.w, float("inf")],
            "right": [self.x + self.w, float("inf")],
            "top": [float("inf"), self.y-player.h],
            "bottom": [float("inf"), self.y + self.h]
        }

    def draw(self):
        pygame.draw.rect(screen, "grey", (self.x, self.y, self.w, self.h))

    def collision(self):
        if (player.x + player.w > self.x and player.x < self.x + self.w):
            if (player.y + player.h > self.y and player.y < self.y + self.h):

                newCoords = [player.x - player.v[0], player.y - player.v[1]]

                shortestTime = float("inf")
                closestWall = ""
                for key, value in self.sides.items():
                    times = [(value[0] - newCoords[0]) / player.v[0] if player.v[0] else float(
                        "inf"), (value[1] - newCoords[1]) / player.v[1] if player.v[1] else float("inf")]

                    if (times[0] < 0):
                        times[0] = float("inf")
                    if (times[1] < 0):
                        times[1] = float("inf")

                    if (times[0] < shortestTime):
                        shortestTime = times[0]
                        closestWall = key
                    elif (times[1] < shortestTime):
                        shortestTime = times[1]
                        closestWall = key

                if (closestWall == "right"):
                    player.x = self.x + self.w
                if (closestWall == "left"):
                    player.x = self.x - player.w
                if (closestWall == "bottom"):
                    player.y = self.y + self.h
                if (closestWall == "top"):
                    player.y = self.y - player.h


class playerClass:
    def __init__(self):
        self.x = startingPos[0]
        self.y = startingPos[1]
        self.w = 20
        self.h = 20
        self.v = [0, 0]

    def draw(self):
        pygame.draw.rect(screen, "blue", (self.x, self.y, self.w, self.h))

    def move(self):
        self.v = [0, 0]
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_w]):
            self.v[1] = -0.5
        if (keys[pygame.K_s]):
            self.v[1] = 0.5
        if (keys[pygame.K_a]):
            self.v[0] = -0.5
        if (keys[pygame.K_d]):
            self.v[0] = 0.5
        self.y += self.v[1]
        self.x += self.v[0]


def generateWalls():
    for n in range(5):
        walls.append(wall())


def draw():
    screen.fill("white")
    for wall in walls:
        wall.draw()
    player.draw()
    pygame.display.flip()


def loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw()
        player.move()
        for wall in walls:
            wall.collision()


player = playerClass()
walls = []
generateWalls()
loop()
