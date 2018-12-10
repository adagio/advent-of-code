
filename = 'input1'
in_filepath = f'data/{filename}.plain'

precedence_rules = []
p_pos = 5
d_pos = 36

with open(in_filepath) as in_file:
    line = in_file.readline()
    while line:
        p = line[p_pos]
        d = line[d_pos]
        precedence = p, d
        precedence_rules.append(precedence)
        line = in_file.readline()

print(precedence_rules)
