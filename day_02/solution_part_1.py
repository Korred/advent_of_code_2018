from collections import Counter

identificators = []
two_count = 0
three_count = 0

with open('input.txt') as inp:
    for line in inp:
        identificators.append(line.strip())

for identificator in identificators:
    counted = set(Counter(identificator).values())

    if 2 in counted:
        two_count += 1

    if 3 in counted:
        three_count += 1


checksum = two_count * three_count

print("Checksum for list of box IDs:", checksum)
