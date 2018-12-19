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

straight = {U: U, D: D, L: L, R: R}
left_turn = {U: L, D: R, L: D, R: U}
right_turn = {U: R, D: L, L: U, R: D}
forward_slash_turn = {U: R, D: L, L: D, R: U}
back_slash_turn = {U: L, D: R, L: U, R: D}

class Cart:

    def __init__(self, p, d):
        self.p = p  # position
        self.d = d  # direction
        self.i = 0  # turn index
        self.ok = True  # ok is set to False after a collision

    def step(self, grid):

        self.p = (self.p[0] + self.d[0], self.p[1] + self.d[1])
        c = grid[self.p]
        if c == '+':
            turn = [left_turn, straight, right_turn][self.i%3]
            self.d = turn[self.d]
            self.i += 1
        elif c == '/':
            self.d = forward_slash_turn[self.d]
        elif c == '\\':
            self.d = back_slash_turn[self.d]

    def hits(self, other):
        return self != other and self.ok and other.ok and self.p == other.p


grid = {}  # grid maps (x, x) positions to characters from the input
carts = []  # carts is a list of Carts instances

import fileinput
for y, line in enumerate(fileinput.input()):
    for x, c in enumerate(line):
        grid[(x, y)] = c
        if c in directions:
            carts.append(Cart((x, y), directions[c]))

part1 = part2 = None
tick = 0

crash = False

while True:
    print(f'tick: {tick}')
    carts = sorted(carts, key=lambda x: (x.p[1], x.p[0]))
    # carts on the top row move first (acting from left to right)
    for cart in carts:
        cart.step(grid)
        for other in carts:
            if cart.hits(other):
                cart.ok = other.ok = False
                part1 = part1 or cart.p
    carts = [x for x in carts if x.ok]
    if len(carts) == 1:
        part2 = carts[0].p
        break
    tick = tick + 1

print(part1)
print(part2)

