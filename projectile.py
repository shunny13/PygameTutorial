from animations import *


class Projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (int(self.x), int(self.y)), self.radius)

    def hits(self, goblin):
        if self.y-self.radius < goblin.hitbox[1]+goblin.hitbox[3] and self.y + self.radius > goblin.hitbox[1]:
            if self.x + self.radius > goblin.hitbox[0] and self.x-self.radius < goblin.hitbox[0]+goblin.hitbox[2]:
                return True
        return False
