from collections import deque
from itertools import islice

to_do = 74501
#to_do = 9

elf_1 = 0  # green
elf_2 = 1  # red

scores = deque([3, 7])

while len(scores) < to_do + 10 + 1:

    new_scores = [int(d) for d in str(scores[elf_1] + scores[elf_2])]
    scores.extend(new_scores)

    elf_1 = ((elf_1 + scores[elf_1] + 1) % len(scores)) 
    elf_2 = ((elf_2 + scores[elf_2] + 1) % len(scores)) 


print(f"Last scores of the ten recipes immediately after {to_do} recepies: {list(islice(scores,to_do,to_do+10))}")