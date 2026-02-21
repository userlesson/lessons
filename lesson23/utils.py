from random import randint as rand

def randbool(r, intrand):
    t = rand(0, intrand)
    return (t <= r)

def randcell(height, width):
    tw = rand(0, width)
    th = rand(0, height)
    return (th, tw)

def randcell2(x, y, w, h):
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    t = rand(0, 3)
    dx, dy = moves[t][0], moves[t][1]
    new_x, new_y = x + dx, y + dy
    if 0 <= new_x < w and 0 <= new_y < h:
        return (new_x, new_y)
    return (x, y)