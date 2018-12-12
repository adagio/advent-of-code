class Tree:

    def __init__(self, data):
        self.n_children = data.popleft()
        self.n_metadata = data.popleft()
        self.children = [ Tree(data) for _ in range(self.n_children) ]
        self.metadata = [ data.popleft() for _ in range(self.n_metadata) ]

    def get_total(self):
        return sum(self.metadata) + sum( child.get_total() for child in self.children )

