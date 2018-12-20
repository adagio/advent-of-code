n = 580741
scores = [3, 7]
elf1_idx = 0
elf2_idx = 1


"""while len(scores) < n + 10:
    total = scores[elf1_idx] + scores[elf2_idx]
    scores.extend(list(map(int, str(total))))
    elf1_idx = (elf1_idx + 1 + scores[elf1_idx]) % len(scores)
    elf2_idx = (elf2_idx + 1 + scores[elf2_idx]) % len(scores)
last_ten_string = ''.join(map(str, scores[n:n+10]))
print(last_ten_string)"""

score = '580741'

score_len = len(score)

i = 0
while score not in ''.join(map(str, scores[-score_len:])):
    i = i + 1
    total = scores[elf1_idx] + scores[elf2_idx]
    scores.extend(list(map(int, str(total))))
    elf1_idx = (elf1_idx + 1 + scores[elf1_idx]) % len(scores)
    elf2_idx = (elf2_idx + 1 + scores[elf2_idx]) % len(scores)

all_scores_str = ''.join(map(str, scores))
print(all_scores_str)
score_str = ''.join(map(str, scores[-score_len:]))
print(score_str)
index = all_scores_str.index(score_str)

print(index)
# 20330673
# 281 s
