from modules.event import Event

polymer = 'dabAcCaCBAcCcaDA'

filename = 'input'
in_filepath = f'data/{filename}.plain'
polymer = open(in_filepath).read().split('\n')[0]

result = Event().trigger_units_of(polymer)

print(f'result: {result}')
print(f'result: {len(result)}')
