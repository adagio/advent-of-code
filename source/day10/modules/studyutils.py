def get_lines(filename):

    filepath = f'data/{filename}.plain'

    lines = []

    for line in open(filepath):
        lines.append(line)

    return lines
