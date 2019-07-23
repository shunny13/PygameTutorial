from animations import *


class Player(object):
    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x+20, self.y+15, 25, 45)

    def draw(self, win):
        if self.walkCount+1 >= 27:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            elif self.left:
                win.blit(walkLeft[0], (self.x, self.y))
            # When the game begins the first shot is right so making him face right
            else:
                win.blit(walkRight[0], (self.x, self.y))

        self.hitbox = (self.x+20, self.y+15, 25, 45)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 1)
