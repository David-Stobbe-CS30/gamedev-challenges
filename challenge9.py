import pygame

screenSize = [1000, 500]

pygame.init()
screen = pygame.display.set_mode((screenSize[0], screenSize[1]))


class Player:
    def __init__(self):
        self.x = background.w / 2
        self.y = screenSize[1] - 100
        self.w = 20
        self.h = 20
        self.startY = 0
        self.g = 0.0090
        self.jumping = False
        self.onPlatform = False
        self.v = [0, 0]
        self.drawX = 0
        self.xside = False
        self.yside = True

    def draw(self):

        if (background.x <= 100 and self.x - background.x <= screenSize[0]/2) or (
                (background.x >= background.w - screenSize[0] and self.x - background.x >= screenSize[0]/2)):
            self.xside = True
        else:
            self.xside = False

        if (background.y >= -50 and self.y - background.y >= screenSize[1]/2) or (
                background.y <= -450 and self.y - background.y <= screenSize[1]/2):
            self.yside = True
        else:
            self.yside = False

        pygame.draw.rect(
            screen, "blue", (self.x - background.x, self.y - background.y, self.w, self.h))

    def move(self):
        self.v[0] = 0
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a]):
            if (player.x - background.x > 0):
                self.v[0] = -1
        elif (keys[pygame.K_d]):
            if (player.x - background.x <
                    background.w - screenSize[0] - player.w):
                self.v[0] = 1
        self.x += self.v[0]

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
        self.w = 2000
        self.x = (self.w / 2) - (screenSize[0]/2)
        self.top = - 380
        self.y = 0
        self.platforms = []

    def createPlatforms(self):
        platY = self.top
        while platY < screenSize[1] - 80:
            platX = 0
            n = 0
            while platX < self.w:
                if n % 2 == 0:
                    y = platY
                else:
                    y = platY + 50
                self.platforms.append(Platform(platX, y, 100, 10))
                platX += 100
                n += 1
            platY += 100

    def draw(self):
        player.onPlatform = False
        for platform in self.platforms:
            platform.draw()
            platform.collisionCheck()

        if (not player.xside):
            self.x = player.x - screenSize[0]/2

        if (not player.yside):
            self.y = player.y - screenSize[1]/2
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
        pygame.draw.rect(
            screen, "grey", (self.x - background.x, self.y - background.y, self.w, self.h))

    def collisionCheck(self):
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
                    player.v[1] = 0
                if (closestWall == "top"):
                    player.y = self.y - player.h
                    player.jumping = False
                    player.v[1] = 0
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
