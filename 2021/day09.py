with open("9.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def createGrid():
    G = []
    for line in lines:
        G.append(list([int(x) for x in line]))
    return G


def isLowPoint(G, x, y):
    return (x == 0 or G[x-1][y] > G[x][y]) and (y == 0 or G[x][y-1] > G[x][y]) and (x == len(G)-1 or G[x+1][y] > G[x][y]) and (y == len(G[0])-1 or G[x][y+1] > G[x][y])


def fillBasin(basinPoints, basinPoint):
    x = int(basinPoint[0])
    y = int(basinPoint[1])
    if (x != 0 and G[x-1][y] != 9 and (x-1, y) not in basinPoints):
        basinPoints.append((x-1, y))
        fillBasin(basinPoints, (x-1, y))
    if (y != 0 and G[x][y-1] != 9 and (x, y-1) not in basinPoints):
        basinPoints.append((x, y-1))
        fillBasin(basinPoints, (x, y-1))
    if (x != len(G)-1 and G[x+1][y] != 9 and (x+1, y) not in basinPoints):
        basinPoints.append((x+1, y))
        fillBasin(basinPoints, (x+1, y))
    if (y != len(G[0])-1 and G[x][y+1] != 9 and (x, y+1) not in basinPoints):
        basinPoints.append((x, y+1))
        fillBasin(basinPoints, (x, y+1))


# Part 1
sum = 0
G = createGrid()
for i in range(0, len(G)):
    for j in range(0, len(G[0])):
        if isLowPoint(G, i, j):
            sum += 1 + G[i][j]
print(sum)

# Part 2
basins = []
for i in range(0, len(G)):
    for j in range(0, len(G[0])):
        if isLowPoint(G, i, j):
            basins.append([(i, j)])
for i in range(0, len(basins)):
    fillBasin(basins[i], basins[i][0])
basins.sort(key=lambda s: len(s))
print(len(basins[len(basins)-1]) * len(basins[len(basins)-2])
      * len(basins[len(basins)-3]))
