from collections import Counter

def process(text):
    """
    Given a text
    get the frequency array.
    eg. "abcdef" -> [False,False]
    """
    counter = Counter(text)   # get frequencies
    values = counter.values() # get values
    values = list(values)     # convert dict_values to list

    # prepare response
    count2 = False
    count3 = False
    if 2 in values:
        count2 = True
    if 3 in values:
        count3 = True
    response = [count2, count3]

    return response
