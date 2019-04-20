recipes = '074501'
score = '37'
elf1 = 0
elf2 = 1
i = 2
while recipes not in score[-7:]:
    new_score = str(int(score[elf1]) + int(score[elf2]))
    score += new_score
    i += len(new_score)
    elf1 = (elf1 + int(score[elf1]) + 1) % len(score)
    elf2 = (elf2 + int(score[elf2]) + 1) % len(score)

print('Part 1:', score[int(recipes):int(recipes)+10])
print('Part 2:', i-7)