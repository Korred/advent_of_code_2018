from itertools import combinations

identificators = []

with open('input.txt') as inp:
    for line in inp:
        identificators.append(line.strip())

# create and check all possible combinations
for pair in combinations(identificators, 2):

    # calculate differences
    diff = sum([1 for letter_pair in zip(*pair) if len(set(letter_pair)) != 1])

    # correct boxes will have IDs which differ by exactly one character at the same position in both strings
    if diff == 1:

        # find and join only common letters
        common = "".join([letter_pair[0] for letter_pair in zip(*pair) if len(set(letter_pair)) == 1])

        print("Letters common between the two correct box IDs:", common)
        break
