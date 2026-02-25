from map import Map
import time
import os
import json
from pynput import keyboard 
from helicopter import Helicopter as Helico
from clouds import Clouds

TICK_SLEEP = 0.05
TREE_UPDATE = 10
FIRE_UPDATE = 100
CLOUDS_UPDATE = 100
MAP_W, MAP_H = 20, 10

field = Map(MAP_W, MAP_H)
field.generate_forest(3, 10)
field.generate_rivers(10)
field.generate_rivers(10)
field.generate_hosp()
field.generate_upgrade()

helico = Helico(MAP_W, MAP_H)
clouds = Clouds(MAP_W, MAP_H)
score = 0
lives = 5

MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}

def load_game():
    global field, helico, clouds, score, lives
    with open("save.json", "r") as f:
        data = json.load(f)
        if data:
            field = Map(MAP_W, MAP_H, data["field"])
            helico = Helico(MAP_W, MAP_H, data["helico"])
            clouds = Clouds(MAP_W, MAP_H, data["clouds"])
            score = data["score"]
            lives = data["lives"]
        else:
            field = Map(MAP_W, MAP_H)
            field.generate_forest(3, 10)
            field.generate_rivers(10)
            field.generate_rivers(10)
            field.generate_hosp()
            field.generate_upgrade()
            helico = Helico(MAP_W, MAP_H)
            clouds = Clouds(MAP_W, MAP_H)
            score = 0
            lives = 5

def save_game():
    global field, helico, clouds, score, lives
    data = {
        "field": field.cells,
        "helico": {"x": helico.x, "y": helico.y, "tank": helico.tank, "mxtank": helico.mxtank},
        "clouds": clouds.cells,
        "score": score,
        "lives": lives
    }
    with open("save.json", "w") as f:
        json.dump(data, f)

def on_press(key):
    global helico, field, score, lives, clouds
    if hasattr(key, 'char') and key.char:
        c = key.char.lower()
        if c in MOVES:
            dx, dy = MOVES[c]
            if helico.move(dx, dy):
                if field.cells[helico.x][helico.y] == 3:
                    shop_menu('hosp')
                if field.cells[helico.x][helico.y] == 4:
                    shop_menu('upgrade')
        elif c == 'f':
            save_game()
        elif c == 'r':
            load_game()

def shop_menu(type):
    global score, helico, lives
    os.system("cls" if os.name == 'nt' else "clear")
    
    if type == 'hosp':
        price = 30
        if lives < 5 and score >= price:
            lives_to_add = min(5 - lives, score // price)
            if lives_to_add > 0:
                cost = lives_to_add * price
                score -= cost
                lives += lives_to_add
        
    elif type == 'upgrade':
        price = 50
        if score >= price:
            score -= price
            helico.mxtank += 1

listener = keyboard.Listener(on_press=on_press)
listener.start()

tick = 1

while True:
    os.system("cls")
    
    score, lives = field.process_helicopter(helico, score, lives)
    
    if clouds.check_lightning(field, helico):
        lives -= 1
        if lives <= 0:
            print(f"Game Over! Cчет: {score}")
            break
    
    print(f"Резервуар: {helico.tank}/{helico.mxtank} | Очки: {score} | Жизни: {'❤️' * lives}")
    
    field.print_map(helico, clouds)
    
    tick += 1
    time.sleep(TICK_SLEEP)
    
    if tick % TREE_UPDATE == 0:
        if field.generate_tree():
            pass
    
    if tick % FIRE_UPDATE == 0:
        burned = field.update_fires()
        if burned > 0:
            score -= burned * 10
    
    if tick % CLOUDS_UPDATE == 0:
        clouds.update_clouds()