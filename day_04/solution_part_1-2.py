from collections import defaultdict
from datetime import datetime, timedelta
import re

# timestamp container for initial reading, sorting and grouping
timestamps = []

# dict to hold timestamps grouped by guard
guard_timestamps = defaultdict(dict)

# read input file and extract timestamps
with open('input.txt') as inp:
    for line in inp:
        dt, action = line[1:].strip().split('] ')
        dt = datetime.strptime(dt, '%Y-%m-%d %H:%M')
        timestamps.append([dt, action])

# sort by date
timestamps.sort(key= lambda x: x[0])

# create timetables for each guard
# 0: guard awake, 1: guard sleeping
current_guard = None
for t in timestamps:

    # check if there is a guard id for this timestamp
    num = re.search(r'#[\d]*', t[1])

    date = t[0].date()
    minute = t[0].minute

    # shift start information
    if num:
        current_guard = num.group(0)
        
        # adjust day if shift starts before midnight
        if t[0].hour != 0: 
            date += timedelta(days=1)

        # create empty
        guard_timestamps[current_guard][date] = [0]*60

    else:
        if t[1] == 'wakes up':
            guard_timestamps[current_guard][date][minute:] = [0]*(60-minute)
        if t[1] == 'falls asleep':
            guard_timestamps[current_guard][date][minute:] = [1]*(60-minute)


''' Part 1 '''

# find longest sleeper overall - (guard, time)
longest_asleep = (None, 0)
for guard in guard_timestamps:
    asleep = 0

    for timestamp in guard_timestamps[guard]:
        asleep += sum(guard_timestamps[guard][timestamp])

    if asleep >= longest_asleep[1]:
        longest_asleep = (guard, asleep)

# once longest sleeper is found - find minute the guard likes to sleep the most
sum_minute = list(map(sum, zip(*[guard_timestamps[longest_asleep[0]][ts] for ts in guard_timestamps[longest_asleep[0]]])))
max_sleepy_minute = max(range(60), key=lambda x: sum_minute[x])

print("Part 1: ID of the guard you chose multiplied by the minute you chose:", int(longest_asleep[0][1:]) * max_sleepy_minute)


''' Part 2 '''
# find guard most frequently asleep on the same minute - (guard, minute, time)
max_freq_asleep = (None, 0, 0)

for guard in guard_timestamps:
    sum_minute = list(map(sum, zip(*[guard_timestamps[guard][ts] for ts in guard_timestamps[guard]])))
    max_sleepy_minute = max(range(60), key=lambda x: sum_minute[x])
    max_asleep = sum_minute[max_sleepy_minute]

    if max_asleep >= max_freq_asleep[2]:
        max_freq_asleep = (guard, max_sleepy_minute, max_asleep)

print("Part 2: ID of the guard you chose multiplied by the minute you chose:", int(max_freq_asleep[0][1:]) * max_freq_asleep[1])
