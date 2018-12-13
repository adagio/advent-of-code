from collections import deque
from collections import defaultdict


def get_max_score(last_marble, n_players):
    """
    based on solution by @aspittel in dev.to
    rotation based on solution by u/marcusndrews
    """
    circle = deque([0])  # 0 placed in the circle
    scores = defaultdict(int)

    # current marble is at the end of the deque
    # the end is the right end
    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            # player is given the marble 7 steps counter-clockwise
            circle.rotate(7)
            current_player = marble % n_players
            scores[current_player] += marble + circle.pop()
            # new current is to the right of removed marble
            # it is inmediately clockwise
            circle.rotate(-1)
        else:
            # placing between the marbles that are 1 and 2 marbles clockwise of the current marble
            circle.rotate(-1)
            circle.append(marble)

    scores_values = scores.values()

    return max(scores_values)

