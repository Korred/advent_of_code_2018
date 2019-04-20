def manhattan(p1, p2): return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


coordinates = []

# read input file and extract all coordinates
with open('input.txt') as inp:
    for target in inp:
        data = tuple(map(int, target.strip().split(',')))
        coordinates.append(data) 
    coordinates.sort()

valid_targets = 0

# coordinates for min bounding rectangle
min_x = min([c[0] for c in coordinates])
max_x = max([c[0] for c in coordinates])
min_y = min([c[1] for c in coordinates])
max_y = max([c[1] for c in coordinates])

# calculate manhattan-dist for each coordinate in min bounding rectangle against
# all available input coordinates and get the sum
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        distance_sum = sum([manhattan(c, (x, y)) for c in coordinates])

        if distance_sum < 10000:
            valid_targets += 1
        

print(valid_targets)
