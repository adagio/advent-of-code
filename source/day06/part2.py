from modules.utils import Utils
from modules.part2.medidor import Medidor

filename = 'input'
filepath = f'data/{filename}.plain'
# lines = Utils.get_lines(filepath)
# coords = Utils.get_coords(lines)

coords = Utils.get_np_coords(filepath)
# cota = 32
cota = 10000

area = Medidor(coords, cota).get_largest_area()  # area represented by coordinates in area
# print(area)
size_of_area = len(area)
print(size_of_area)
