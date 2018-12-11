def draw(positions_nda):

    x_min, y_min = positions_nda.min(axis=0)
    x_max, y_max = positions_nda.max(axis=0)
    
    for y in range(y_min, y_max + 1):
        line = ''
        for x in range(x_min, x_max + 1):
            if [x, y] in positions_nda.tolist():
                line += '#'
            else:
                line += '.'
        print(line)

