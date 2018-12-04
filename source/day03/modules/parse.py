import re


def parse(line):
    """
    Given a text
    get a claim object
    eg.
    "#1 @ 3,2: 5x4" -> obj
    obj = {
        "id": 1,
        "left_edge": 3,
        "top_edge": 2,
        "width": 5,
        "height": 4
    }
    """
    line = re.sub('[#@:]', '', line)
    line = re.sub(' +', ' ', line)
    tokens = re.split(' |,|x', line)
    claim_obj = {
        "id": int(tokens[0]),
        "left_edge": int(tokens[1]),
        "top_edge": int(tokens[2]),
        "width": int(tokens[3]),
        "height": int(tokens[4])
    }
    return claim_obj
