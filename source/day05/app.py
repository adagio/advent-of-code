from string import ascii_lowercase

from modules.event import Event

filename = 'input'
in_filepath = f'data/{filename}.plain'
polymer = open(in_filepath).read().split('\n')[0]

result = Event().trigger_units_of(polymer)

# print(f'result: {result}')

print('Part 1')

print(f'result: {len(result)}')

print('= = = = =')

print('Part 2')

min_len = len(polymer)

for c in ascii_lowercase:
    opposite_uniy_type = c.swapcase()
    processed_polymer = polymer.replace(c, '').replace(opposite_uniy_type, '')
    result = Event().trigger_units_of(processed_polymer)
    result_len = len(result)
    min_len = min(min_len, result_len)

print(f'min len: {min_len}')
