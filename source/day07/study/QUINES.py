# u/PM_ME_UR_QUINES

import networkx as nx
def solve(lines):
    G = nx.DiGraph([(s[1], s[7]) for s in map(str.split, lines)])
    return ''.join(nx.lexicographical_topological_sort(G))

