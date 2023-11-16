#CHALLENGE 1
import pygame
import random
startingPos = [50, 50]
screenSize = [1000, 1000]
pygame.init()
screen = pygame.display.set_mode((screenSize[0], screenSize[1]))

class wall:
    def __init__(self):
        self.x = random.randint(0, screenSize[0])
        self.y = random.randint(0, screenSize[1])
        self.w = random.randint(10, 50)
        self.h = random.randint(10, 50)
    def draw(self):
        pygame.draw.rect(screen, "grey", (self.x, self.y, self.w, self.h))
    def collision(self):
        #Collision logic
        if((player.x + player.w > self.x or player.x < self.x + self.w) and (player.y + player.h > self.y or player.y < self.y + self.h)):
            print("x collision")
            # if(player.y + player.h > self.y or player.y < self.y + self.h):
                # player.x = startingPos[0]
                # player.y = startingPos[1]

class playerClass:
    def __init__(self):
        self.x = startingPos[0]
        self.y = startingPos[1]
        self.w = 20
        self.h = 20
    def draw(self):
        pygame.draw.rect(screen, "blue", (self.x, self.y, self.w, self.h))
    def move(self):
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_w]):
            self.y -= 1
        elif(keys[pygame.K_s]):
            self.y += 1
        elif(keys[pygame.K_a]):
            self.x -= 1
        elif(keys[pygame.K_d]):
            self.x += 1


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
        for wall in walls:
            wall.collision()
        player.move()

walls = []
for n in range(5):
    walls.append(wall())
player = playerClass()
loop()