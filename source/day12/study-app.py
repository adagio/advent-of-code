from study.trend import plot_trend
from modules.utils import get_lines


filename = 'input'
lines = get_lines(filename)
cadena = lines[0].split()[-1]  # -1 to get the last element
print(cadena)

initial_state = set(i for i, x in enumerate(cadena) if x == '#')

print(initial_state)

rules = dict(line.split()[::2] for line in lines[2:])  # for lines 2 and below
    
# line = lines[3].split()
# print(line[0:None:2])  # slice to get first and last element

plot_trend(initial_state, rules)

