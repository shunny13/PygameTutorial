from animations import *
import collisions


class Ennemy(object):
    walkRight = [pygame.image.load('assets/R1E.png'), pygame.image.load('assets/R2E.png'), pygame.image.load('assets/R3E.png'),
                 pygame.image.load('assets/R4E.png'), pygame.image.load(
                     'assets/R5E.png'), pygame.image.load('assets/R6E.png'),
                 pygame.image.load('assets/R7E.png'), pygame.image.load(
                     'assets/R8E.png'), pygame.image.load('assets/R9E.png'),
                 pygame.image.load('assets/R10E.png'), pygame.image.load('assets/R11E.png')]

    walkLeft = [pygame.image.load('assets/L1E.png'), pygame.image.load('assets/L2E.png'), pygame.image.load('assets/L3E.png'),
                pygame.image.load('assets/L4E.png'), pygame.image.load(
                    'assets/L5E.png'), pygame.image.load('assets/L6E.png'),
                pygame.image.load('assets/L7E.png'), pygame.image.load(
                    'assets/L8E.png'), pygame.image.load('assets/L9E.png'),
                pygame.image.load('assets/L10E.png'), pygame.image.load('assets/L11E.png')]

    def __init__(self, x, y, width, height, end, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = vel
        self.health = 10
        self.visible = True

        self.hitx = self.x+17
        self.hity = self.y+2
        self.hitw = 31
        self.hith = 57

        self.hitbox = (self.hitx, self.hity, self.hitw, self.hith)

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            self.hitx = self.x+17
            self.hity = self.y+2
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1]-20, 50, 10))
            pygame.draw.rect(win, (0, 125, 0),
                             (self.hitbox[0], self.hitbox[1]-20, 50-((50/10)*(10-self.health)), 10))
            self.hitbox = (self.x+17, self.y+2, 31, 57)
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 1)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print("hit")

    def attacks(self, player):
        return (collisions.collides(self, player))

    def bite(self):
        print("BITE")
