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
        for event in pygame.event.get():
                self.mousePos = pygame.mouse.get_pos()

        angle = math.atan2(self.mousePos[1] - self.y, self.mousePos[0] - self.x)
        distance = (self.y - self.mousePos[1])**2 + (self.x - self.mousePos[0])**2

        self.x += math.cos(angle) * 0.5
        self.y += math.sin(angle) * 0.5

    def draw(self):
        pygame.draw.circle(screen, "green", (self.x, self.y), self.r)


class Food:
    def __init__(self):
        self.x = random.randint(0, screenSize[0])
        self.y = random.randint(0, screenSize[1])
        self.r = random.randint(5, 25)
    def draw(self):
        pygame.draw.circle(screen, "green", (self.x, self.y), self.r)

foodArr = []
player = Player()
for n in range(50):
    foodArr.append(Food())


def generateFood():
    foodArr.append(Food())
    print("test")

def draw():
    screen.fill("white")
    player.draw()
    for food in foodArr:
        food.draw()
    pygame.display.flip()


def loop():
    t = Timer(1, generateFood)
    t.start()
    running = True
    while running:
        draw()
        player.move()

loop()