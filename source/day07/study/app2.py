from collections import defaultdict

filename = 'input1'
in_filepath = f'data/{filename}.plain'

_prev = defaultdict(list)
_next = defaultdict(list)
prev_pos = 5
next_pos = 36

with open(in_filepath) as in_file:
    line = in_file.readline()
    while line:
        p = line[prev_pos]
        n = line[next_pos]
        _prev[n].append(p)
        _next[p].append(n)
        line = in_file.readline()


print(f'_prev: {_prev}')
print(f'_next: {_next}')


def get_root():

    min_key = min(_prev)
    # print(min_key)

    prevs = _prev[min_key]
    # print(prevs)

    root = min(prevs)

    return root


root = get_root()
# print(root)

serie = []
serie.append(root)

def print_next(node):
    print(f'node: {node}')
    if node in _next:
        nexts = _next[node]
        nexts.sort()
        print_next(nexts[0])
        if len(nexts) > 1:
            for other_node in nexts[1:]:
                print_next(other_node)

print_next(root)
