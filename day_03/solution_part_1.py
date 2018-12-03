# use defaultdict to omit checking whether a dicitionary key exists or not
from collections import defaultdict


# claim object
class Claim():
    def __init__(self, num, left, top, width, height):
        self.num = num
        self.left = left
        self.top = top
        self.width = width
        self.height = height


# claims store
claims = []

# tracks which claims overlap eachother
overlaps = defaultdict(set)

# tracks which fabric 'field' is in use and which claims are using it
fabric = defaultdict(list)

# read input file and extract all claims
with open('input.txt') as inp:
    for claim in inp:
        data = claim.strip().split()
        claims.append(Claim(data[0], *map(int, data[2][:-1].split(',')), *map(int, data[3].split('x'))))

# find overlappings
for claim in claims:

    for y in range(claim.top, claim.top + claim.height):
        for x in range(claim.left, claim.left + claim.width):

            field = fabric[(x, y)]
            
            # if fabric field is already in use / known
            if field:

                # update overlaps based on the claims that are using the current fabric field
                for num in field:
                    overlaps[num].add(claim.num)
                    overlaps[claim.num].add(num)

            # track new in-use fabric field
            fabric[(x, y)].append(claim.num)

print("Square inches of fabric are within two or more claims:", sum(len(fabric[field]) > 1 for field in fabric))