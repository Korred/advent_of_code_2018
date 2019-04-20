from PIL import Image, ImageDraw

import re

# regex to find all numbers
num_re = re.compile(r'[-]{0,1}[\d]+')

points_original = list()
points_info = list()
curr_points = set()


def star_printer(i, min_x, max_x, min_y, max_y, curr_points):

    width = abs(min_x-max_x)+1 
    height = abs(min_y-max_y)+1

    print(width, height)
    print("Starting image generation...")
    image = Image.new('1', (width, height), "black")

    print("Load pixels...")
    pixels = image.load()

    print("Writing pixels...")
    for ey, y in enumerate(range(min_y, max_y+1)):
        for ex, x in enumerate(range(min_x, max_x+1)):
            if (x, y) in curr_points:
                pixels[ex, ey] = 1

    image.save(f"starfield{i}.png")





# read input file and extract all points
with open('input.txt') as inp:
    for pos in inp:
        x, y, h_v, v_v = map(int, re.findall(num_re, pos))
        curr_points.add((x, y))
        points_info.append([x, y, h_v, v_v])
        points_original.append([x, y, h_v, v_v])





smallest_field = None


# first find smallest relevant starfield

for i in range(10515):

    # reset points
    curr_points = set()

    for e, point in enumerate(points_info):
        new_x = point[0]+point[2]
        new_y = point[1]+point[3]
        points_info[e][:2] = [new_x, new_y]
        curr_points.add((new_x, new_y))

    minx = min(x for (x, y) in curr_points)
    maxx = max(x for (x, y) in curr_points)
    miny = min(y for (x, y) in curr_points)
    maxy = max(y for (x, y) in curr_points)

    print(minx, maxx, miny, maxy)

    if i >= 10400 and i <= 10515:
        star_printer(i, minx, maxx, miny, maxy, curr_points)

    if i == 10515:
        break



"""
i = 0
while True:
    # print current starfield
    # star_printer(i, min_x, max_x, min_y, max_y, curr_points)

    # reset points
    curr_points = set()

    for e, point in enumerate(points_info):
        new_x = point[0]+point[2]
        new_y = point[1]+point[3]
        points_info[e][:2] = [new_x, new_y]
        curr_points.add((new_x, new_y))


    # manual continue
    input("Next?")
    i += 1
"""





















