from parse import parse
import networkx as nx

from modules.planner import get_time


filename = 'input'
filepath = f'data/{filename}.plain'

pattern = 'Step {start} must be finished before step {stop} can begin.'

steps = nx.DiGraph()

for line in open(filepath):
    result = parse(pattern, line)
    steps.add_edge(result['start'], result['stop'])

gen = nx.lexicographical_topological_sort(steps)
step_list = list(gen)

steps_string = ''.join(step_list)

print(steps_string)

workers_n = 5

time = get_time(steps, workers_n)

print(f'Finishing all the work took {time} seconds')

