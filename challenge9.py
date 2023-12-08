import pygame

screenSize = [1000, 1000]

pygame.init()
screen = pygame.display.set_mode((screenSize[0], screenSize[1]))


class Player:
    def __init__(self):
        self.x = (screenSize[0]) / 2
        self.y = screenSize[1] - 100
        self.w = 20
        self.h = 20
        self.startY = 0
        self.g = 0.0075
        self.jumping = False
        self.onPlatform = False
        self.v = [0, 0]
        self.side = False

    def draw(self):
        pygame.draw.rect(screen, "blue", (self.x, self.y, self.w, self.h))
        pygame.draw.line(
            screen, "red", (0, screenSize[1] - 100 + self.h), (screenSize[0], screenSize[1] - 100 + self.h))

    def move(self):
        self.v[0] = 0
        if ((background.x <= 0 and self.x <= screenSize[0]/2) or
                (background.x >= background.w - screenSize[0] and self.x >= screenSize[0]/2)):
            self.side = True
        else:
            self.side = False

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a]):
            self.v[0] = -1

        elif (keys[pygame.K_d]):
            self.v[0] = 1

        if (self.side):
            self.x += self.v[0]
        else:
            background.x += self.v[0]

        if (keys[pygame.K_w]):
            if (not self.jumping):
                self.startY = self.y
                self.v[1] = -1
                self.jumping = True
        if (not self.onPlatform and self.y < screenSize[1] - 100):
            self.jumping = True

        if (self.jumping):
            self.jump()

    def jump(self):
        self.v[1] += self.g
        self.y += self.v[1]
        if (self.y >= screenSize[1] - 100):
            self.y = screenSize[1] - 100
            self.jumping = False
            self.v[1] = 0
        elif (self.onPlatform):
            self.jumping = False
            self.v[1] = 0


class Background:
    def __init__(self):
        self.y = 0
        self.w = 2000
        self.x = (self.w / 2) - (screenSize[0]/2)
        self.h = screenSize[1]
        self.platforms = []

    def createPlatforms(self):
        platX = 0
        n = 0
        while platX < self.w:
            if n % 2 == 0:
                platY = screenSize[1] - 200
            else:
                platY = screenSize[1] - 150
            self.platforms.append(Platform(platX, platY, 100, 10))
            platX += 100
            n += 1

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
        self.sides = {
            "left": [self.x-player.w, float("inf")],
            "right": [self.x + self.w, float("inf")],
            "top": [float("inf"), self.y-player.h],
            "bottom": [float("inf"), self.y + self.h]
        }

    def draw(self):
        pygame.draw.rect(screen, "grey", (self.x -
                         background.x, self.y, self.w, self.h))

    def collisionCheck(self):
        if (player.x + player.w + background.x >= self.x and player.x + background.x <= self.x + self.w):
            if (player.y + player.h >= self.y and player.y <= self.y + self.h):
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

                    print(key, times)

                    if (times[0] < shortestTime):
                        shortestTime = times[0]
                        closestWall = key
                    elif (times[1] < shortestTime):
                        shortestTime = times[1]
                        closestWall = key

                if (closestWall == "right"):
                    print(self.x, background.x, player.x)

                if (closestWall == "left"):
                    print(self.x, background.x, player.x)

                if (closestWall == "bottom"):
                    player.y = self.y + self.h + background.y
                    player.v[1] = 0
                if (closestWall == "top"):
                    player.y = (self.y + background.y) - player.h
                    player.jumping = False
                    player.v[1] = 0
                    player.onPlatform = True
                print(closestWall)


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
