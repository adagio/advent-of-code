def process(items):
    """
    Given a array of strings ["+1", "-2"]
    calculate the addition
    """

    sum = 0

    for item in items:
        sum = sum + int(item)       
    
    return sum
