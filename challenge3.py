import pygame
import random
startingPos = [50, 50]
screenSize = [1000, 1000]
pygame.init()
screen = pygame.display.set_mode((screenSize[0], screenSize[1]))

circles = []
rectangles = []
amount = 1
running = True

def generate():
    for n in range(amount):
        circles.append(Circle())
        rectangles.append(Rectangle())

class Rectangle:
    def __init__(self):
        self.x = random.randint(0, screenSize[0])
        self.y = random.randint(0, screenSize[1])
        self.w = random.randint(5, 25)
        self.h = random.randint(5, 25)
        self.xv = random.uniform(0.1, 0.5) * (random.randint(0, 1)*2 -1)
        self.yv = random.uniform(0.1, 0.5) * (random.randint(0, 1)*2 -1)
    def draw(self):
        pygame.draw.rect(screen, "red", (self.x, self.y, self.w, self.h))
    def move(self):
        if(self.x >= screenSize[0]):
            self.x = 0
        elif(self.x <= 0):
            self.x = screenSize[0]

        if(self.y >= screenSize[1]):
            self.y = 0
        elif(self.y <= 0):
            self.y = screenSize[1]
        
        self.x += self.xv
        self.y += self.yv







class Circle:
    def __init__(self):
        self.x = random.randint(0, screenSize[0])
        self.y = random.randint(0, screenSize[1])
        self.r = random.randint(50, 100)
        self.xv = random.uniform(0.01, 0.1) * (random.randint(0, 1)*2 -1)
        self.yv = random.uniform(0.01, 0.1) * (random.randint(0, 1)*2 -1)
    def draw(self):
        pygame.draw.circle(screen, "green", (self.x, self.y), self.r)
    def move(self):
        if(self.x >= screenSize[0] or self.x <= 0):
            self.xv *= -1

        if(self.y >= screenSize[1] or self.y <= 0):
            self.yv *= -1
        
        self.x += self.xv
        self.y += self.yv


def click(pos):
    for circle in circles:
        if(((circle.x) - pos[0])**2 + ((circle.y) - pos[1])**2 <= circle.r ** 2):
            circles.remove(circle)



    
def loop():
    while running:
        screen.fill("white")
        for rectangle in rectangles:
            rectangle.draw()
            rectangle.move()

        for circle in circles:
            circle.draw()
            circle.move()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("click")
                click(pygame.mouse.get_pos())


generate()
loop()