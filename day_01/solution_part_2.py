from itertools import cycle

frequency_changes = [] 

# read input file and extract frequency changes
with open('input.txt') as inp:
    for line in inp:
        frequency_changes.append(int(line.strip()))

# set of unique frequencies
unique_frequencies = set()

# curren frequency
current_frequency = 0

# pool (cycle) of available frequencies changes
pool = cycle(frequency_changes)

while current_frequency not in unique_frequencies:
    unique_frequencies.add(current_frequency)
    current_frequency += next(pool)

print("First frequency that is reached twice: ", current_frequency)