from utils import randbool, randcell, randcell2

CELL_TYPES = "🟩🌲🌊🏩⭐🔥⚡⛅"

class Map:
    def __init__(self, width, height, cells=None):
        self.width = width
        self.height = height
        if cells:
            self.cells = cells
        else:
            self.cells = [[0 for _ in range(width + 2)] for _ in range(height + 2)]
    
    def check_bounds(self, x, y):
        return (1 <= x <= self.height and 1 <= y <= self.width)

    def generate_rivers(self, l):
        rc = randcell(self.width, self.height)
        rx, ry = rc[0] + 1, rc[1] + 1
        if self.check_bounds(rx, ry):
            self.cells[rx][ry] = 2
            while l > 1:
                rc2 = randcell2(rx-1, ry-1, self.width, self.height)
                rx2, ry2 = rc2[0] + 1, rc2[1] + 1
                if self.check_bounds(rx2, ry2):
                    self.cells[rx2][ry2] = 2
                    rx, ry = rx2, ry2
                    l -= 1

    def generate_forest(self, r, mxr):
        for ri in range(1, self.height + 1):
            for ci in range(1, self.width + 1):
                if randbool(r, mxr):
                    self.cells[ri][ci] = 1
    
    def generate_hosp(self):
        c = randcell(self.width, self.height)
        cx, cy = c[0] + 1, c[1] + 1
        if self.check_bounds(cx, cy) and self.cells[cx][cy] == 0:
            self.cells[cx][cy] = 3

    def generate_upgrade(self):
        c = randcell(self.width, self.height)
        cx, cy = c[0] + 1, c[1] + 1
        if self.check_bounds(cx, cy) and self.cells[cx][cy] == 0:
            self.cells[cx][cy] = 4

    def add_fire(self):
        for _ in range(50):
            c = randcell(self.width, self.height)
            cx, cy = c[0] + 1, c[1] + 1
            if self.check_bounds(cx, cy) and self.cells[cx][cy] == 1:
                self.cells[cx][cy] = 5
                return True
        return False

    def spread_fire(self):
        fire_cells = []
        for ri in range(1, self.height + 1):
            for ci in range(1, self.width + 1):
                if self.cells[ri][ci] == 5:
                    fire_cells.append((ri, ci))
        
        spread_dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for x, y in fire_cells:
            for dx, dy in spread_dirs:
                nx, ny = x + dx, y + dy
                if self.check_bounds(nx, ny) and self.cells[nx][ny] == 1:
                    if randbool(1, 3):
                        self.cells[nx][ny] = 5

    def update_fires(self):
        self.spread_fire()
        
        burned_trees = 0
        for ri in range(1, self.height + 1):
            for ci in range(1, self.width + 1):
                if self.cells[ri][ci] == 5:
                    if randbool(1, 2):
                        self.cells[ri][ci] = 0
                        burned_trees += 1
        
        fires_added = 0
        for i in range(3):
            if self.add_fire():
                fires_added += 1
        
        return burned_trees
            
    def generate_tree(self):
        for _ in range(10): 
            c = randcell(self.width, self.height)
            cx, cy = c[0] + 1, c[1] + 1
            if self.check_bounds(cx, cy) and self.cells[cx][cy] == 0:
                self.cells[cx][cy] = 1
                return True
        return False
            
    def print_map(self, helico, clouds):
        print("⬛" * (self.width + 2))
        
        for ri in range(1, self.height + 1):
            print("⬛", end="")  
            for ci in range(1, self.width + 1):
                cell = self.cells[ri][ci]
                cloud = clouds.cells[ri][ci]
                if (helico.x == ri and helico.y == ci):
                    print("🚁", end="")
                elif cloud > 0:
                    print(CELL_TYPES[cloud], end="")
                elif 0 <= cell < len(CELL_TYPES):
                    print(CELL_TYPES[cell], end="")
            print("⬛")  
        
        print("⬛" * (self.width + 2))

    def process_helicopter(self, helico, score, lives):
        if not self.check_bounds(helico.x, helico.y):
            return score, lives
        
        c = self.cells[helico.x][helico.y]
        
        if c == 2:
            helico.tank = helico.mxtank
            
        elif c == 5:
            if helico.tank > 0:
                helico.tank -= 1
                self.cells[helico.x][helico.y] = 1
                score += 30

        return score, lives