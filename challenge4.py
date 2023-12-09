import pygame
import random
import math
from threading import Timer
startingPos = [50, 50]
screenSize = [1000, 1000]
pygame.init()
screen = pygame.display.set_mode((screenSize[0], screenSize[1]))


class Player:
    def __init__(self):
        self.x = screenSize[0]/2
        self.y = screenSize[1]/2
        self.r = 20
        self.mousePos = (0, 0)

    def move(self):
        self.mousePos = pygame.mouse.get_pos()

        angle = math.atan2(
            self.mousePos[1] - self.y, self.mousePos[0] - self.x)
        self.x += math.cos(angle)
        self.y += math.sin(angle)
        distance = (self.y - self.mousePos[1]
                    )**2 + (self.x - self.mousePos[0])**2
        if (distance <= 50):
            self.x = self.mousePos[0]
            self.y = self.mousePos[1]

    def draw(self):
        pygame.draw.circle(screen, "black", (self.x, self.y), self.r)

    def eat(self, foodSize):
        self.r += (foodSize / 8)


class Food:
    def __init__(self):
        self.x = random.randint(0, screenSize[0])
        self.y = random.randint(0, screenSize[1])
        self.r = random.randint(5, 25)
        self.eaten = False
        self.rgb = (random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255))

    def draw(self):
        pygame.draw.circle(screen, self.rgb, (self.x, self.y), self.r)

    def collide(self):
        if (player.x - self.x)**2 + (player.y - self.y)**2 <= (player.r + self.r)**2:
            player.eat(self.r)
            self.eaten = True


foodArr = []
player = Player()
for n in range(5):
    foodArr.append(Food())


def generateFood():
    foodArr.append(Food())


def draw():
    screen.fill("white")
    player.draw()
    for food in foodArr:
        food.draw()
    pygame.display.flip()


def checkCollision():
    for food in foodArr:
        food.collide()
        if (food.eaten):
            foodArr.remove(food)


def loop():
    frameCount = 0
    running = True
    while running:
        draw()
        player.move()
        frameCount += 1
        if (frameCount % 100 == 0):
            generateFood()
        checkCollision()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


loop()
