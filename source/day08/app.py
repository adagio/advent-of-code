from modules.utils import get_data
from modules.tree import Tree


filename = 'input'
data = get_data(filename)

tree = Tree(data)
total = tree.get_total()
print(f'total: {total}')

