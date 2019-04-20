from collections import defaultdict

graph = defaultdict(set)
requirements = defaultdict(set)

# read input file and create directed graph
with open('input.txt') as inp:
    for line in inp:
        parts = line.strip().split()
        graph[parts[1]].add(parts[7])
        requirements[parts[7]].add(parts[1])

# find source vertex/vertices
source_vertices = set([v for v in graph]) - set([v for v in requirements])

order = []
queue = sorted(source_vertices)

while queue:
    for i in range(len(queue)):

        if queue[i] in requirements:
            # step cannot be executed yet since requirements are not met yet
            if set(requirements[queue[i]]) & set(queue):
                continue

        v = queue.pop(i)
        order.append(v)

        queue[i:i] = graph[v]
        queue = sorted(set(queue))
        break

print("".join(order))