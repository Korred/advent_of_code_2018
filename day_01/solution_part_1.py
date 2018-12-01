frequency_changes = [] 

# read input file and extract frequency changes
with open('input.txt') as inp:
    for line in inp:
        frequency_changes.append(int(line.strip()))

# sum all frequency changes
total = sum(frequency_changes)

print("Resulting frequency: ", total)