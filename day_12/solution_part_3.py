from collections import deque
from itertools import islice


def rep_hd(inp): return inp.replace('#', '1').replace('.', '0')


inp = '##.#..#.#..#.####.#########.#...#.#.#......##.#.#...##.....#...#...#.##.#...##...#.####.##..#.#..#.'

state = deque(map(int, list(rep_hd(inp))))
rules = set(tuple(map(int, list(rep_hd(i[0])))) for i in map(str.split, open('input.txt').readlines()) if i[2] == '#')
generations = 50000000000
left_index = 0

total = 0
last_diff = 0
repeating_diff = False


for g in range(generations):
    if repeating_diff:
        total = total + (last_diff*(generations-g))
        print(total)
        break

    new_state = deque([])

    # adjust state to have more data that can be used for matching
    state.extend([0]*4)
    state.extendleft([0]*4)

    left_index += -2

    for i in range(2, len(state)-2):
        s = tuple(islice(state, i-2, i+3))

        if s in rules:
            new_state.append(1)
        else:
            new_state.append(0)

    # remove empty pots from front and back; adjust real_index
    first_occ = new_state.index(1)
    for i in range(first_occ):
        new_state.popleft()
    new_state.reverse()


    last_occ = new_state.index(1)
    for i in range(last_occ):
        new_state.popleft()
    new_state.reverse()


    
    left_index += first_occ

    state = new_state

    new_total = 0
    for i in range(len(state)):
        if state[i] == 1:
            new_total += i+left_index

    diff = abs(total-new_total)
    if diff == last_diff:
        repeating_diff = True
    else:
        last_diff = diff

    total = new_total


