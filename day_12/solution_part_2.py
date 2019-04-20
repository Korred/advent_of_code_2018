import numpy as np
from itertools import islice

import time


def rep_hd(inp): return inp.replace('#', '1').replace('.', '0')


inp = '##.#..#.#..#.####.#########.#...#.#.#......##.#.#...##.....#...#...#.##.#...##...#.####.##..#.#..#.'
state = np.array(list(map(int, list(rep_hd(inp)))),dtype=int)
rules = set(tuple(map(int, list(rep_hd(i[0])))) for i in map(str.split, open('input.txt').readlines()) if i[2] == '#')
generations = 50000000000
left_index = 0
t0 = time.time()

for g in range(generations):

    if g%100000 == 0 and g != 0:
        print(g)
        t1 = time.time()
        total = t1-t0
        print("Total time:", total)
        break

    new_state = np.array([], dtype=int)

    state = np.concatenate(([0]*4, state, [0]*4))
    left_index += -2

    for i in range(2, len(state)-2):
        slice = tuple(state[i-2:i+3])
        if slice in rules:
            new_state = np.append(new_state, 1)
        else:
            new_state = np.append(new_state, 0)

    
    plants_occ = np.argwhere(new_state)
    first_occ = plants_occ[0][0] 
    last_occ = plants_occ[-1][0]

    state = new_state[first_occ:last_occ+1]

    left_index += first_occ



total = 0
for i in range(len(state)):
    if state[i] == 1:
        total += i+left_index

print(total)

