from utils import randbool

class Clouds:
    def __init__(self, w, h, cells=None):
        self.w = w
        self.h = h
        if cells:
            self.cells = cells
        else:
            self.cells = [[0 for _ in range(w + 2)] for _ in range(h + 2)]
    
    def update_clouds(self, r=1, mxr=20, g=1, mxg=5):
        for ri in range(1, self.h + 1):
            for ci in range(1, self.w + 1):
                if randbool(r, mxr): 
                    if randbool(g, mxg): 
                        self.cells[ri][ci] = 6
                    else:
                        self.cells[ri][ci] = 7 
                else:
                    self.cells[ri][ci] = 0
    
    def check_lightning(self, field, helico):
        for ri in range(1, self.h + 1):
            for ci in range(1, self.w + 1):
                if self.cells[ri][ci] == 6:
                    if ri == helico.x and ci == helico.y:
                        self.cells[ri][ci] = 0
                        return True
        return False