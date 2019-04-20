from collections import Counter

# mapping for the 8 acres that should be checked
mapping = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# minutes to check
minutes = [10, 1000000000]


for minute in minutes:

    # current area
    area = []

    # already seen areas
    seen_areas = []

    # first repeated area
    repeated_area = None

    # minute when first repetition is seen
    first_rep_min = None

    # minutes between repetitions
    passed = 0

    # read input file
    with open('input.txt') as inp:
        for line in inp:
            acres = list(line.strip())
            area.append(acres)

    # current minute
    i = 0

    # whether last possible repetition minute was found
    last = False



    while i < minute:
        i += 1
        new_area = []

        # calculate new area
        for y, row in enumerate(area):
            new_row = []
            for x, acre in enumerate(row):
                acre = area[y][x]
                found = []

                for m in mapping:
                    y_c = y + m[0]
                    x_c = x + m[1]
                    if y_c >= 0 and y_c < len(area) and x_c >= 0 and x_c < len(area):
                        found.append(area[y_c][x_c])

                found = Counter(found)

                # empty acre
                if acre == '.':
                    if '|' in found:
                        if found['|'] >= 3:
                            new_row.append('|')
                        else:
                            new_row.append('.')
                    else:
                        new_row.append('.')
                    

                # tree acre
                elif acre == '|':
                    if '#' in found:
                        if found['#'] >= 3:
                            new_row.append('#')
                        else:
                            new_row.append('|')
                    else:
                        new_row.append('|')
                    

                # lumberyard acre
                elif acre == '#':
                    if '#' in found and '|' in found:
                        new_row.append('#')
                    else:
                        new_row.append('.')

            new_area.append(new_row)

        # overwrite old area with new
        area = new_area


        # check whether the newly calculated area was already seen
        # if so it is the first seen repetition
        if not repeated_area:
            if new_area in seen_areas:
                first_rep = i
                repeated_area = new_area
                passed += 1
                print(f"First repetition found at minute: {i}\n")
            else:
                seen_areas.append(new_area)
        
        # 1) if a repetition was found, find out how many minutes will pass until it is repeated again
        # 2) based on the mintue of the first found repetition, minutes between repetitions and total minutes to check,
        #    skip calculation by resetting minute index to the last possible repetition minute
        else:
            if new_area == repeated_area:           
                remaining = ((minute - first_rep) % passed)
                i = minute - remaining

                print(f"Minutes between repetitions: {passed}")
                print(f'Remaining minutes: {remaining}')
                print(f'Resetting current minute to {i}\n')

                # indicate last pass
                last = True

            else:
                counted_acres = Counter([acre for row in new_area for acre in row])
                passed += 1



    counted_acres = Counter([acre for row in area for acre in row])
    print(f"Total ressource value after {minute} minutes: {counted_acres['|']*counted_acres['#']}\n")