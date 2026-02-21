from utils import randbool, randcell, randcell2

CELL_TYPES = "🟩🌲🌊🏩⭐🔥"

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[0 for _ in range(width + 2)] for _ in range(height + 2)]
    
    def check_bounds(self, x, y):
        return (1 <= x <= self.height and 1 <= y <= self.width)

    def generate_rivers(self, l):
        rc = randcell(self.width, self.height)
        rx, ry = rc[0] + 1, rc[1] + 1
        if self.check_bounds(rx, ry):
            self.cells[rx][ry] = 2
            while l > 1:
                rc2 = randcell2(rx, ry, self.width, self.height)
                rx2, ry2 = rc2[0], rc2[1]
                if self.check_bounds(rx2, ry2):
                    self.cells[rx2][ry2] = 2
                    rx, ry = rx2, ry2
                    l -= 1

    def generate_forest(self, r, mxr):
        for ri in range(1, self.height + 1):
            for ci in range(1, self.width + 1):
                if randbool(0, mxr):
                    self.cells[ri][ci] = 1

    def add_fire(self):
        for _ in range(50):
            c = randcell(self.width, self.height)
            cx, cy = c[0] + 1, c[1] + 1
            if self.check_bounds(cx, cy) and self.cells[cx][cy] == 1:
                self.cells[cx][cy] = 5
                return True
        return False

    def update_fires(self):
        for ri in range(1, self.height + 1):
            for ci in range(1, self.width + 1):
                if self.cells[ri][ci] == 5:
                    self.cells[ri][ci] = 0
        
        fires_added = 0
        for i in range(5):
            if self.add_fire():
                fires_added += 1
        
        
    def generate_tree(self):
        for _ in range(10): 
            c = randcell(self.width, self.height)
            cx, cy = c[0] + 1, c[1] + 1
            if self.check_bounds(cx, cy) and self.cells[cx][cy] == 0:
                self.cells[cx][cy] = 1
                return True
        return False
            
    def print_map(self, helico):
        print("⬛" * (self.width + 2))
        
        for ri in range(1, self.height + 1):
            print("⬛", end="")  
            for ci in range(1, self.width + 1):
                cell = self.cells[ri][ci]
                if (helico.x == ri and helico.y == ci):
                    print("🚁", end="")
                elif 0 <= cell < len(CELL_TYPES):
                    print(CELL_TYPES[cell], end="")
            print("⬛")  
        
        print("⬛" * (self.width + 2))

    def process_helicopter(self, helico):
        if not self.check_bounds(helico.x, helico.y):
            return
        
        c = self.cells[helico.x][helico.y]
        
        if c == 2:
            helico.tank = helico.mxtank
            
        elif c == 5:
            if helico.tank > 0:
                helico.tank -= 1
                self.cells[helico.x][helico.y] = 1
            