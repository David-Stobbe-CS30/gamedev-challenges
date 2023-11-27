import random
import math
import pygame

screenSize = [1500, 1000]
pygame.init()
screen = pygame.display.set_mode((screenSize[0] - 500, screenSize[1]))

class Player:
    def __init__(self):
        self.x =100
        self.y = screenSize[1] - 100
        self.w = 20
        self.h = 20
    def draw(self):
        pygame.draw.rect(screen, "blue", (self.x, self.y, self.w, self.h))
    def move(self):
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_a]):
            background.x += 1
        elif(keys[pygame.K_d]):
            background.x -= 1
        elif(keys[pygame.K_w]):
            ##JUMP
            self.y -= 0.5


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
                platY = screenSize[1] - 300
            else:
                platY = screenSize[1] - 200
            self.platforms.append(Platform(platX, platY, 100, 10))
    def draw(self):
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
    def draw(self):
        pygame.draw.rect(screen, "grey", (self.x + background.x, self.y, self.w, self.h))
    def collisionCheck(self):
        if(player.x >= self.x and player.x <= self.x + self.w):
            print("Test")
            if(player.y <= self.y and player.y >= self.y + self.h):
                player.y = self.y + player.h
                print("test")

    





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
