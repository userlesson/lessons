from utils import randcell

class Helicopter:
    def __init__(self, w, h):
        rc = randcell(w, h)
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.y = ry
        self.w = w
        self.h = h
        self.tank = 0
        self.mxtank = 1

    def move(self, dx, dy):
        nx, ny = self.x + dx, self.y + dy
        if 1 <= nx <= self.h and 1 <= ny <= self.w: 
            self.x, self.y = nx, ny
            return True
        return False

    def print_menu(self):
        print(" 💧", self.tank, "/", self.mxtank, sep="")