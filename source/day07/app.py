from parse import parse
import networkx as nx

filename = 'input'
filepath = f'data/{filename}.plain'



steps = nx.DiGraph()

for line in open(filepath):
    result = parse(pattern, line)
    steps.add_edge(result['start'], result['stop'])

gen = nx.lexicographical_topological_sort(steps)
step_list = list(gen)

step_string = ''.join(step_list)

print(step_string)

