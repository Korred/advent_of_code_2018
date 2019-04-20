from collections import defaultdict
from string import ascii_uppercase


graph = defaultdict(set)
requirements = defaultdict(set)
letter_lkp = {i: e+1 for e, i in enumerate(ascii_uppercase)}

# read input file and create directed graph
with open('input.txt') as inp:
    for line in inp:
        parts = line.strip().split()
        graph[parts[1]].add(parts[7])
        requirements[parts[7]].add(parts[1])

# find source vertex/vertices
source_vertices = set([v for v in graph]) - set([v for v in requirements])

order = []
time = -1
workers = {}
queue = sorted(source_vertices)

while queue:
    time += 1
    # update workers and remove ones that are done
    done = []
    current_jobs = list(workers.keys())
    
    for job in current_jobs:

        if workers[job] - 1 == 0:
            done.append(job)
            del workers[job]
        else:
            workers[job] -= 1

    done.sort()
    
    # replace steps that are done with next ones
    for d in done:
        i = queue.index(d)
        queue.pop(i)
        order.append(d)

        # check if not sink vertex
        if d in graph:
            queue[i:i] = graph[d]

    # remove duplicates and sort
    queue = sorted(set(queue))
        
    # continue only when free worker is available
    if len(workers) < 5:
        for i in range(len(queue)):
            if queue[i] in requirements:
                # step cannot be executed yet since requirements are not met yet
                if set(requirements[queue[i]]) & set(queue):
                    continue

            # assign step/job to worker only if free workers are available
            if len(workers) < 5 and queue[i] not in workers:
                workers[queue[i]] = letter_lkp[queue[i]] + 60
            else:
                continue



print("".join(order))
print(time)