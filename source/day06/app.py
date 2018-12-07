from modules.bearofjade import bear_run
from modules.marcus import part1
# from modules.mastermedo import mastermedo_run
from modules.protectedmethod import method

filename = 'input1'
filepath = f'data/{filename}.plain'

# @bearofjade
bear_run(filepath)

print('= '*3)

lines = []
with open(filepath) as f:
    while True:
        line = f.readline().strip('\n')
        if line != '':
            lines.append(line)
        else:
            break

# @marcus
print(part1(lines))

print('= '*3)

# @MasterMedo
# mastermedo_run(filepath)

# @ProtectedMethod
method(filepath)
""" 1 1 8 9
{(3, 4): 9, (1, 1): 1, (5, 5): 17}
((5, 5), 17) """
