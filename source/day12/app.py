from modules.evolution import step
from modules.evolution import trend_sum
from modules.utils import get_lines


filename = 'input'
lines = get_lines(filename)
cadena = lines[0].split()[-1]  # -1 to get the last element
print(cadena)

initial_state = set(i for i, x in enumerate(cadena) if x == '#')

print(initial_state)

rules = dict(line.split()[::2] for line in lines[2:])  # for lines 2 and below
    
# part 2

result = trend_sum(initial_state, rules)
print(result)

