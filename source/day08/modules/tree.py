class Tree:
    """
    Base on code by @aspittel
    https://dev.to/aspittel/comment/7e75
    """
    def __init__(self, data):
        n_children = data.popleft()
        n_metadata = data.popleft()
        self.children = [ Tree(data) for _ in range(n_children) ]
        self.metadata = [ data.popleft() for _ in range(n_metadata) ]

    def get_total(self):
        return sum(self.metadata) + sum( child.get_total() for child in self.children )

    def get_child_value(self, child_idx):
        if child_idx < len(self.children):
            return self.children[child_idx].get_root_value()
        return 0

    def get_root_value(self):
        if not self.children: return sum(self.metadata)
        total = 0
        for idx in self.metadata:
            total += self.get_child_value(idx - 1) # Index starts at 1 not 0 :(
        return total

