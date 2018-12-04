def process(id1, id2):
    """
    Given 2 IDs
    verify if they differ by exactly 1 character
    """
    repeated = True
    differ = 0
    length = len(id1)
    for i in range(0, length):
        if id1[i] != id2[i]:
            differ += 1
            if differ > 1:
                repeated = False
                break
    return repeated
