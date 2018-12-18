def get_lines(filename):
    filepath = f'data/{filename}.plain'

    data = None

    with open(filepath, 'r') as f:
        data = f.readlines()

    return data
