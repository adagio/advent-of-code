def process(id1, id2):
    """
    Given 2 IDs, that differ by exactly by 1 char
    Return common chars
    """
    length = len(id1)
    common = ''
    for i in range(0, length):
        if id1[i] != id2[i]:
            common = id1[0:i] + id1[i+1:]
            break

    return common