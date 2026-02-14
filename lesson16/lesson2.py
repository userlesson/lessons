class Turtle:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s
    
    def go_up(self):
        self.y += self.s
    
    def go_down(self):
        self.y -= self.s
    
    def go_left(self):
        self.x -= self.s
    
    def go_right(self):
        self.x += self.s
    
    def evolve(self):
        self.s += 1
    
    def degrade(self):
        if self.s > 1:
            self.s -= 1
    
    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        
        steps_x = dx // self.s
        if dx % self.s != 0:
            steps_x += 1
            
        steps_y = dy // self.s
        if dy % self.s != 0:
            steps_y += 1
        
        return steps_x + steps_y

t = Turtle(0, 0, 3)

t.go_up()  
t.go_right()  
t.evolve()  
t.go_up()     
t.go_right()  

print(f"Позиция: ({t.x}, {t.y})")
print(f"Шаг: {t.s}")
print(f"До (10, 10): {t.count_moves(10, 10)} шагов")

t.degrade() 
t.degrade()
t.degrade() 
t.degrade()
print(f"После уменьшений: {t.s}")