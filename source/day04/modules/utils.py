class Utils:

    def __init__(self):
        pass

    def load_items(filepath):
        with open(filepath) as fp:
            line = fp.readline()
            items = []
            while line:
                line = line.strip()
                items.append(line)
                line = fp.readline()
            return items
