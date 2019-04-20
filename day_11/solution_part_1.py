import numpy as np
serial = 6878

w, h = (300, 300)
grid = np.zeros((w, h), dtype=int)

max_power = (0, None)
      

# generate grid
for y in range(1, h+1):
    for x in range(1, w+1):
        rack_id = x + 10
        power_level = ((rack_id * y) + serial) * rack_id
        power_level = 0 if len(str(power_level)) < 3 else int(str(power_level)[-3])
        power_level -= 5

        grid[y-1][x-1] = power_level


# find max_power 3x3 square
for y in range(0, h-2):
    for x in range(0, w-2):

        power_level = np.sum(grid[y:y+3, x:x+3])

        if power_level > max_power[0]:
            max_power = (power_level, (x+1, y+1))


print(max_power)