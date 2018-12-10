import copy

with open('input') as f:
    data = f.readlines()


class Node:
    def __init__(self, name, parents, children):
        self.name = name
        self.parents = parents
        self.parents_copy = parents
        self.children = children

    def __repr__(self):
        parents = [p.name for p in self.parents] if self.parents else None
        children = [c.name for c in self.children] if self.children else None
        return 'Node(name={}, parents={}, children={})'.format(
            self.name, parents, children)

    def add_parent(self, parent):
        if self.parents:
            self.parents.append(parent)
        else:
            self.parents = [parent]
        self.parents_copy = self.parents[:]

    def remove_parent(self, parent):
        if self.parents_copy:
            self.parents_copy.remove(parent)

    def add_child(self, child):
        if self.children:
            self.children.append(child)
        else:
            self.children = [child]

    def is_root(self):
        return self.parents_copy == []


nodes = {}

for d in data:
    node = nodes.get(d[5], Node(d[5], [], []))
    child = nodes.get(d[36], Node(d[36], [], []))
    node.add_child(child)
    child.add_parent(node)
    nodes[d[5]] = node
    nodes[d[36]] = child

nodes_bak = copy.deepcopy(nodes)

# Part 1:
# Traverse the tree:
path = []
job_times = {}
while len(nodes):
    # Find roots:
    roots = [n for n in nodes.values() if n.parents_copy == []]
    first_root = min(roots, key=lambda n: n.name)
    # Execute first_node and remove it as parent from its children:
    for c in first_root.children:
        c.remove_parent(first_root)
    # Remove node from global nodes list:
    del nodes[first_root.name]
    path.append(first_root.name)

print('Part 1:')
print(''.join(path))
