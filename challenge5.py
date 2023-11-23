import random
import math
import pygame

screenSize = [1000, 1000]


class Circle:
    def __init__(self):
        self.x = random.randint(0, screenSize[0])
        self.y = random.randint(0, screenSize[1])
        self.r = random.randint(50, 100)
        self.xv = random.uniform(0.01, 0.1) * (random.randint(0, 1)*2 - 1)
        self.yv = random.uniform(0.01, 0.1) * (random.randint(0, 1)*2 - 1)

    def draw(self):
        pygame.draw.circle(screen, "green", (self.x, self.y), self.r)

    def move(self):
        if (self.x >= screenSize[0] or self.x <= 0):
            self.xv *= -1

        if (self.y >= screenSize[1] or self.y <= 0):
            self.yv *= -1

        self.x += self.xv
        self.y += self.yv


def click(pos):
    for circle in circles:
        if (((circle.x) - pos[0])**2 + ((circle.y) - pos[1])**2 <= circle.r ** 2):
            circles.remove(circle)
            if (len(circles) == 0):
                print("YOU WIN!")
            return

    for rectangle in rectangles:
        if (pos[0] >= rectangle.x and pos[0] <= rectangle.x + rectangle.w):
            if (pos[1] >= rectangle.y and pos[1] <= rectangle.y + rectangle.h):
                pygame.quit()
                print("YOU LOSE!")


def loop():
    running = True
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
