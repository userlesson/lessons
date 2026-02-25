from random import randint as rand

def randbool(r, mxr):
    t = rand(0, mxr)
    return (t <= r)

def randcell(w, h):
    tw = rand(0, w - 1)
    th = rand(0, h - 1)
    return (th, tw)

def randcell2(x, y, w, h):
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    t = rand(0, 3)
    dx, dy = moves[t][0], moves[t][1]
    new_x, new_y = x + dx, y + dy
    if 0 <= new_x < w and 0 <= new_y < h:
        return (new_x, new_y)
    return (x, y)