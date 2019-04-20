import numpy as np
serial = 6878

w, h = (300, 300)
grid = np.zeros((w, h), dtype=int)

max_power = (0, None, 0)
      

# generate grid
for y in range(1, h+1):
    for x in range(1, w+1):
        rack_id = x + 10
        power_level = ((rack_id * y) + serial) * rack_id
        power_level = 0 if len(str(power_level)) < 3 else int(str(power_level)[-3])
        power_level -= 5

        grid[y-1][x-1] = power_level

# find max_power in i x i squares
for i in range(1, h+1):
    #print(f"Checking {i}x{i} grids")

    for y in range(0, h + 1 - i):
        for x in range(0, w + 1 - i):

            power_level = np.sum(grid[y:y+i, x:x+i])

            if power_level > max_power[0]:
                max_power = (power_level, (x+1, y+1), i)


print(max_power)
