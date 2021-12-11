with open("9.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def createGrid():
    G = []
    for line in lines:
        G.append(list([int(x) for x in line]))
    return G


def isLowPoint(G, r, c):
    return (r == 0 or G[r-1][c] > G[r][c]) and (c == 0 or G[r][c-1] > G[r][c]) and (r == len(G)-1 or G[r+1][c] > G[r][c]) and (c == len(G[0])-1 or G[r][c+1] > G[r][c])


def fillBasin(basinPoints, basinPoint):
    r = int(basinPoint[0])
    c = int(basinPoint[1])
    if (r != 0 and G[r-1][c] != 9 and (r-1, c) not in basinPoints):
        basinPoints.append((r-1, c))
        fillBasin(basinPoints, (r-1, c))
    if (c != 0 and G[r][c-1] != 9 and (r, c-1) not in basinPoints):
        basinPoints.append((r, c-1))
        fillBasin(basinPoints, (r, c-1))
    if (r != len(G)-1 and G[r+1][c] != 9 and (r+1, c) not in basinPoints):
        basinPoints.append((r+1, c))
        fillBasin(basinPoints, (r+1, c))
    if (c != len(G[0])-1 and G[r][c+1] != 9 and (r, c+1) not in basinPoints):
        basinPoints.append((r, c+1))
        fillBasin(basinPoints, (r, c+1))


# Part 1
sum = 0
G = createGrid()
for r in range(0, len(G)):
    for c in range(0, len(G[0])):
        if isLowPoint(G, r, c):
            sum += 1 + G[r][c]
print(sum)

# Part 2
basins = []
for r in range(0, len(G)):
    for c in range(0, len(G[0])):
        if isLowPoint(G, r, c):
            basins.append([(r, c)])
for r in range(0, len(basins)):
    fillBasin(basins[r], basins[r][0])
basins.sort(key=lambda s: len(s))
print(len(basins[len(basins)-1]) * len(basins[len(basins)-2])
      * len(basins[len(basins)-3]))
