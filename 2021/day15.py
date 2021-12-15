from collections import defaultdict
from heapq import *

import copy

with open("15.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def fillGrid():
    for line in lines:
        G.append(list([int(x) for x in line]))


def createEdges(G):
    edges = []
    for r in range(0, len(G)):
        for c in range(0, len(G[0])):
            if c-1 >= 0:
                edges.append((r*len(G[0])+c-1, r*len(G[0])+c, G[r][c]))
            if r-1 >= 0:
                edges.append(((r-1)*len(G[0])+c, r*len(G[0])+c, G[r][c]))
            if r+1 < len(G):
                edges.append(((r+1)*len(G[0])+c, r*len(G[0])+c, G[r][c]))
            if c+1 < len(G[0]):
                edges.append((r*len(G[0])+c+1, r*len(G[0])+c, G[r][c]))
    return edges


def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))
    q, seen, mins = [(0, f, [])], set(), {f: 0}
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = [v1] + path
            if v1 == t:
                return (cost, path)
            for c, v2 in g.get(v1, ()):
                if v2 in seen:
                    continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))
    return (float("inf"), [])


# Part 1
G = []
fillGrid()
edges = createEdges(G)
print(dijkstra(edges, 0, len(G)*len(G[0])-1)[0])


# Part 2
G2 = copy.deepcopy(G)

for i in range(1, 5):
    for r in range(0, len(G)):
        line = [x+i for x in G[r]]
        for c in range(0, len(line)):
            if line[c] > 9:
                line[c] = line[c] - 9
        G2[r].extend(line)
for i in range(1, 5):
    for r in range(0, len(G)):
        line = [x+i for x in G2[r]]
        for c in range(0, len(line)):
            if line[c] > 9:
                line[c] = line[c] - 9
        G2.append(line)

edges = createEdges(G2)
print(dijkstra(edges, 0, len(G2)*len(G2[0])-1)[0])
