import random
import math
import pygame

screenSize = [1000, 1000]
boundaries = [1000, 900]
pygame.init()
screen = pygame.display.set_mode((screenSize[0], screenSize[1]))


class Circle:
    def __init__(self):
        self.x = random.randint(0, boundaries[0])
        self.y = random.randint(0, boundaries[1])
        self.r = random.randint(5, 25)
        self.xv = random.uniform(0.01, 0.1) * (random.randint(0, 1)*2 - 1)
        self.yv = random.uniform(0.01, 0.1) * (random.randint(0, 1)*2 - 1)
        self.rgb = (random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255))

    def draw(self):
        pygame.draw.circle(screen, self.rgb, (self.x, self.y), self.r)

    def move(self):
        if (self.x + self.r >= boundaries[0] or self.x - self.r <= 0):
            self.xv *= -1

        if (self.y + self.r >= boundaries[1] or self.y - self.r <= 0):
            self.yv *= -1

        self.x += self.xv
        self.y += self.yv


class Player:
    def __init__(self):
        self.x = boundaries[0] / 2
        self.y = boundaries[1] + 50
        self.r = 20

    def draw(self):
        pygame.draw.circle(screen, "black", (self.x, self.y), self.r)

    def shoot(self):
        bullets.append(Bullet())

    def move(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a]):
            self.x -= 1
        elif (keys[pygame.K_d]):
            self.x += 1

        if (self.x - self.r < 0):
            self.x = self.r
        elif (self.x + self.r > boundaries[0]):
            self.x = boundaries[0] - self.r


class Bullet:
    def __init__(self):
        self.x = player.x
        self.y = player.y
        self.r = 5
        self.hit = False

    def draw(self):
        pygame.draw.circle(screen, "black", (self.x, self.y), self.r)

    def collide(self):
        for circle in circles:
            if (circle.x - self.x)**2 + (circle.y - self.y)**2 <= (circle.r + self.r)**2:
                circles.remove(circle)
                self.hit = True

    def move(self):
        self.y -= 1


circles = []
for n in range(10):
    circles.append(Circle())
player = Player()
bullets = []


def update():
    for circle in circles:
        circle.draw()
        circle.move()
    for bullet in bullets:
        if (bullet.y < 0):
            bullets.remove(bullet)
            continue
        bullet.draw()
        bullet.move()
    player.draw()
    player.move()


def checkCollision():
    for bullet in bullets:
        bullet.collide()
        if (bullet.hit):
            bullets.remove(bullet)


def loop():
    running = True
    while running:
        screen.fill("white")
        update()
        checkCollision()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                player.shoot()


loop()
