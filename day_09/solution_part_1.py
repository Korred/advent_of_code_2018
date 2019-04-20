from itertools import cycle
from collections import deque

# player count and target marble score
players_cnt = 462
target_score = 71938 * 100


# players
players = cycle([i for i in range(1, players_cnt + 1)])

# player scores
scores = {i: 0 for i in range(1, players_cnt + 1)}

# marbles played so far and last played  lowest-numbered marble
circle = deque([0])
lowest_marble = 0

# current marble position
curr_marble_pos = 0

for lowest_marble in range(1, target_score + 1):
    player = next(players)


    if lowest_marble % 23 == 0:
        circle.rotate(7)
        scores[player] += lowest_marble + circle.pop()
        circle.rotate(-1)


    else:
        circle.rotate(-1)
        circle.append(lowest_marble)



print(max(scores, key=scores.get), scores[max(scores, key=scores.get)])