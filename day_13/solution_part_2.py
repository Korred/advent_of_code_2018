from colorama import init
from colorama import Fore, Back, Style
init()

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


def free_pos(carts, pos):
    if pos in carts:
        return False
    else:
        return True


counter = 0
while True:
    counter += 1
    to_check = sorted(carts.keys())

    if len(to_check) == 1:
        print(f'\nLast surviving cart at {to_check[0][::-1]}!')
        break
    while to_check:
        # pop first cart from list
        pos = to_check.pop(0)
        y, x = pos
        s, d, r = carts[pos]

        # calc new position, roration

        ny, nx = None, None
        ns, nd, nr = None, None, None

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

        # if new position is free, remove old one and add to new cart pos
        if free_pos(carts, (ny, nx)):
            # remove old pos
            del(carts[pos])
            carts[(ny,nx)] = [ns, nd, nr]

        else:
            print(f"CRASH! Cart moving from \t{(y,x)}\t crashed with cart at \t{(ny,nx)}")

            # remove first pos
            del(carts[pos])
            del(carts[(ny,nx)])
            
            try:
                to_check.pop(to_check.index((ny,nx)))
            except ValueError:
                continue
