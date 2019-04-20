from collections import deque
from itertools import islice

import time


state = deque(list('##.#..#.#..#.####.#########.#...#.#.#......##.#.#...##.....#...#...#.##.#...##...#.####.##..#.#..#.'))
rules = {i[0]: i[2] for i in map(str.split, open('input.txt').readlines())}
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

    new_state = deque([])

    # adjust state to have more data that can be used for matching
    state.extend(["."]*4)
    state.extendleft(["."]*4)


    left_index += -2

    for i in range(2, len(state)-2):
        s = "".join(islice(state, i-2, i+3))

        if s in rules:
            new_state.append(rules[s])
        else:
            new_state.append('.')




    # remove empty pots from front and back; adjust real_index
    first_occ = new_state.index("#")
    for i in range(first_occ):
        new_state.popleft()

    new_state.reverse()

    last_occ = new_state.index('#')



    for i in range(last_occ):
        new_state.popleft()
    new_state.reverse()


    
    left_index += first_occ

    state = new_state


    

total = 0
for i in range(len(state)):
    if state[i] == '#':
        total += i+left_index

print(total)

