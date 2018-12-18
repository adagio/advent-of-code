class Cart:

    def __init__(self, p, d):
        self.p = p  # position
        self.d = d  # direction
        self.i = 0  # turn index
        self.ok = True  # ok is set to False after a collision

