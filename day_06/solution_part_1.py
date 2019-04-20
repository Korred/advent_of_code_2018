coordinates = []

# read input file and extract all coordinates
with open('input.txt') as inp:
    for target in inp:
        data = tuple(map(int, target.strip().split(',')))
        coordinates.append(data)

"""
coordinates = [
    (1, 1),
    (1, 6),
    (8, 3),
    (3, 4),
    (5, 5),
    (8, 9)
]
"""

def manhattan(p1, p2): return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


# 1 - find finite targets

finite = {}

coordinates.sort()

min_x = min([c[0] for c in coordinates])
max_x = max([c[0] for c in coordinates])
min_y = min([c[1] for c in coordinates])
max_y = max([c[1] for c in coordinates])

for c in coordinates:
    if c[0] not in (min_x, max_x) and c[1] not in (min_y, max_y):
        finite[c] = 1
        
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        distances = sorted([(c, manhattan(c, (x, y))) for c in coordinates], key=lambda x: x[1])
        min_dist = distances[0][1]

        if min_dist != 0:
            if [d[1] for d in distances].count(min_dist) == 1 and distances[0][0] in finite.keys():

                finite[distances[0][0]] += 1

for f in finite:
    print(f, finite[f])