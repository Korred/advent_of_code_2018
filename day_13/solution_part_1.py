intersect_rules = {
    'none': 'left',
    'left': 'straight',
    'straight': 'right',
    'right': 'left'
}

direction_lkp = {
    '>': ('right', '-'),
    '<': ('left', '-'),
    '^': ('up', '|'),
    'v': ('down', '|')
}

rotation_lkp = {
    ('<', 'straight'): ('<', 'left', 0, -1),
    ('<', 'left'): ('v', 'down', 1, 0),
    ('<', 'right'): ('^', 'up', -1, 0),

    ('^', 'straight'): ('^', 'up', -1, 0),
    ('^', 'left'): ('<', 'left', 0, -1),
    ('^', 'right'): ('>', 'right', 0, 1),

    ('>', 'straight'): ('>', 'right', 0, 1),
    ('>', 'left'): ('^', 'up', -1, 0),
    ('>', 'right'): ('v', 'down', 1, 0),

    ('v', 'straight'): ('v', 'down', 1, 0),
    ('v', 'left'): ('>', 'right', 0, 1),
    ('v', 'right'): ('<', 'left', 0, -1),    
}

carts = {}
tracks = []
crash_loc = None

# read input file and create directed graph
with open('input.txt') as inp:
    for y, l in enumerate(inp):
        data = l.strip('\n')
        line = []

        for x, c in enumerate(data):
            # found cart
            if c in ('<', '>', '^', 'v'):
                direction = direction_lkp[c]
                line.append(direction[1])

                # cart at pos with current direction and last made turn
                carts[(y, x)] = [c, direction[0], 'none']

            else:
                line.append(c)
                    

        tracks.append(line)

        #parts = line.strip().split()
        #graph[parts[1]].add(parts[7])
        #requirements[parts[7]].add(parts[1])


def free_pos(carts, pos):
    if pos in carts:
        return False
    else:
        return True

"""
print(carts)
for y, t in enumerate(tracks):
    for x, c in enumerate(t):
        if (y,x) in carts.keys():
            print(carts[(y,x)][0], end='')
        else:
            print(c, end='')
    print()
"""

while True:
    to_check = sorted(carts.keys())

    for pos in to_check:
        y, x = pos
        s, d, r = carts[pos]


        ny, nx = None, None
        ns, nd, nr = None, None, None
        

        # remove old pos
        del(carts[pos])

        if tracks[y][x] == '+':
            nr = intersect_rules[r]
            rot = rotation_lkp[(s, nr)]
            ny, nx = (y+rot[2], x+rot[3])
            ns, nd, nr = [rot[0], rot[1], nr]

        elif tracks[y][x] == '-':
            if d == 'right':
                ny = y
                nx = x+1
                ns, nd, nr = [s, d, r]
            elif d == 'left':
                ny = y
                nx = x-1
                ns, nd, nr = [s, d, r]

        elif tracks[y][x] == '|':
            if d == 'up':
                ny = y-1
                nx = x
                ns, nd, nr = [s, d, r]
            elif d == 'down':
                ny = y+1
                nx = x
                ns, nd, nr = [s, d, r]

        elif tracks[y][x] == '/':
            if d == 'up':
                ny = y
                nx = x + 1
                ns, nd, nr = ['>', 'right', r]
            elif d == 'left':
                ny = y + 1
                nx = x
                ns, nd, nr = ['v', 'down', r]
            elif d == 'down':
                ny = y
                nx = x - 1
                ns, nd, nr = ['<', 'left', r]
            elif d == 'right':
                ny = y-1
                nx = x
                ns, nd, nr = ['^', 'up', r]

        elif tracks[y][x] == "\\":
            if d == 'right':
                ny = y + 1
                nx = x 
                ns, nd, nr = ['v', 'down', r]
            elif d == 'up':
                ny = y
                nx = x - 1
                ns, nd, nr = ['<', 'left', r]
            elif d == 'left':
                ny = y - 1
                nx = x
                ns, nd, nr = ['^', 'up', r]
            elif d == 'down':
                ny = y
                nx = x + 1
                ns, nd, nr = ['>', 'right', r]


        if free_pos(carts, (ny, nx)):
            carts[(ny,nx)] = [ns, nd, nr]
        else:
            crash_loc = (ny, nx)
            break

    """
    for y, t in enumerate(tracks):
        for x, c in enumerate(t):
            if (y,x) == crash_loc:
                print('X', end='')
            elif (y,x) in carts.keys():
                print(carts[(y,x)][0], end='')
            else:
                print(c, end='')
        print()
    print()
    input()
    """

    if crash_loc:
        break

print(f"Crash Location at {crash_loc[::-1]}")