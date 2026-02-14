class Kassa:
    def __init__(self, money):
        self.money = money
    
    def top_up(self, X):
        self.money += X
    
    def count_1000(self):
        return self.money // 1000
    
    def take_away(self, X):
        if X <= self.money:
            self.money -= X
            return True
        else:
            return False

k = Kassa(5000)
k.top_up(2500)
print(f"Тысяч: {k.count_1000()}")
if k.take_away(3000):
    print("Деньги сняты")
else:
    print("Недостаточно денег")