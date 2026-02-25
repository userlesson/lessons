from utils import randcell

class Helicopter:
    def __init__(self, w, h, data=None):
        if data:
            self.x = data["x"]
            self.y = data["y"]
            self.tank = data["tank"]
            self.mxtank = data["mxtank"]
        else:
            rc = randcell(w, h)
            rx, ry = rc[0], rc[1]
            self.x = rx + 1
            self.y = ry + 1
            self.tank = 0
            self.mxtank = 1
        self.w = w
        self.h = h

    def move(self, dx, dy):
        nx, ny = self.x + dx, self.y + dy
        if 1 <= nx <= self.h and 1 <= ny <= self.w: 
            self.x, self.y = nx, ny
            return True
        return False