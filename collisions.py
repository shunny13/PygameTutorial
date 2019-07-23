def collides(rect1, rect2):
    return (rect1.hitx < rect2.hitx + rect2.hitw and
            rect1.hitx + rect1.hitw > rect2.hitx and
            rect1.hity < rect2.hity + rect2.hith and
            rect1.hity + rect1.hith > rect2.hity)
