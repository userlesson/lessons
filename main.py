from map import Map
import time
import os
from pynput import keyboard 
from helicopter import Helicopter as Helico

TICK_SLEEP = 0.05
TREE_UPDATE = 10
FIRE_UPDATE = 100
MAP_W, MAP_H = 20, 10

field = Map(MAP_W, MAP_H)
field.generate_forest(3, 10)
field.generate_rivers(10)
field.generate_rivers(10)

helico = Helico(MAP_W, MAP_H)

MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}

def on_press(key):
    global helico
    if hasattr(key, 'char') and key.char:
        c = key.char.lower()
        if c in MOVES:
            dx, dy = MOVES[c]
            helico.move(dx, dy)

listener = keyboard.Listener(on_press=on_press)
listener.start()

tick = 1

while True:
    os.system("cls")
    
    field.process_helicopter(helico)
    helico.print_menu()
    field.print_map(helico)
    tick += 1
    time.sleep(TICK_SLEEP)
    
    if tick % TREE_UPDATE == 0:
        field.generate_tree()
    
    if tick % FIRE_UPDATE == 0:
        field.update_fires()