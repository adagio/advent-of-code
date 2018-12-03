from collections import Counter

def process(text):
    """
    Given a text
    get the frequency array.
    eg. "abcdef" -> [0,0]
    """
    counter = Counter(text)   # get frequencies
    values = counter.values() # get values 
    values = list(values)     # convert dict_values to list

    # prepare response
    count2 = 0
    count3 = 0
    if 2 in values:
        count2 = 1
    if 3 in values:
        count3 = 1
    response = [count2, count3]    

    return response