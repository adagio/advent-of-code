import re
from modules.game import get_max_score
from study.mandrews import play_game


def run(filename, factor=1):

    filepath = f'data/{filename}.plain'

    max_scores = []

    with open(filepath, 'r') as f:
        for line in f:
            print(line.replace('\n',''))
            n_players, last_marble = [int(n) for n in re.findall(r'\d+', line)]
            last_marble = last_marble * factor
            max_score = get_max_score(last_marble=last_marble, n_players=n_players)
            # max_score = play_game(max_players=n_players, last_marble=last_marble)
            print(f'max score: {max_score}\n')
            break

