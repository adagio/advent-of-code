import networkx as nx

with open("input.txt") as f:
    edges = [(l[5], l[36]) for l in f]

u, v = zip(*edges)
G = nx.DiGraph()
G.add_edges_from(edges)

def get_next_fullfilled_node(seen, open_nodes):
    for n in sorted(open_nodes):
        if all(k in seen for k in G.predecessors(n)):
            return n

open_nodes = set(u)-set(v)

seen = set()

while open_nodes:
    n = get_next_fullfilled_node(seen, open_nodes)
    print(n, end="")
    seen.add(n)
    for k in G[n]:
        open_nodes.add(k)
    open_nodes -= seen

