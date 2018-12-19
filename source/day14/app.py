n = 580741
scores = [3, 7]
elf1_idx = 0
elf2_idx = 1


while len(scores) < n + 10:
    total = scores[elf1_idx] + scores[elf2_idx]
    scores.extend(list(map(int, str(total))))
    elf1_idx = (elf1_idx + 1 + scores[elf1_idx]) % len(scores)
    elf2_idx = (elf2_idx + 1 + scores[elf2_idx]) % len(scores)

last_ten_string = ''.join(map(str, scores[n:n+10]))
print(last_ten_string)
