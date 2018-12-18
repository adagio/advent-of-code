from modules.cart import Cart


# define up, down, left, right
U = ( 0, -1)
D = ( 0,  1)
L = (-1,  0)
R = ( 1,  0)

# map input characters to directions
directions = {
    '^': U,
    'v': D,
    '<': L,
    '>': R
}

grid = {}  # grid maps (x, x) positions to characters from the input
carts = []  # carts is a list of Carts instances

import fileinput
for y, line in enumerate(fileinput.input()):
    for x, c in enumerate(line):
        grid[(x, y)] = c
        if c in directions:
            carts.append(Cart((x, y), directions[c]))

breakpoint()

