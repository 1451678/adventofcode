with open("9.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def createMap():
    map = []
    for line in lines:
        l = [int(x) for x in line]
        row = []
        for i in range(0, len(l)):
            row.append(l[i])
        map.append(row)
    return map


def isLowPoint(map, x, y):
    return (x == 0 or map[x-1][y] > map[x][y]) and (y == 0 or map[x][y-1] > map[x][y]) and (x == len(map)-1 or map[x+1][y] > map[x][y]) and (y == len(map[0])-1 or map[x][y+1] > map[x][y])


def fillBasin(basinPoints, basinPoint):
    x = int(basinPoint[0])
    y = int(basinPoint[1])
    if (x != 0 and map[x-1][y] != 9 and (x-1, y) not in basinPoints):
        basinPoints.append((x-1, y))
        fillBasin(basinPoints, (x-1, y))
    if (y != 0 and map[x][y-1] != 9 and (x, y-1) not in basinPoints):
        basinPoints.append((x, y-1))
        fillBasin(basinPoints, (x, y-1))
    if (x != len(map)-1 and map[x+1][y] != 9 and (x+1, y) not in basinPoints):
        basinPoints.append((x+1, y))
        fillBasin(basinPoints, (x+1, y))
    if (y != len(map[0])-1 and map[x][y+1] != 9 and (x, y+1) not in basinPoints):
        basinPoints.append((x, y+1))
        fillBasin(basinPoints, (x, y+1))


def removeDuplicates(lst):
    return [t for t in (set(tuple(i) for i in lst))]


# Part 1
sum = 0
map = createMap()
for i in range(0, len(map)):
    for j in range(0, len(map[0])):
        if isLowPoint(map, i, j):
            sum += 1 + map[i][j]
print(sum)

# Part 2
basins = []
for i in range(0, len(map)):
    for j in range(0, len(map[0])):
        if isLowPoint(map, i, j):
            basins.append([(i, j)])
for i in range(0, len(basins)):
    fillBasin(basins[i], basins[i][0])
basins.sort(key=lambda s: len(s))
print(len(basins[len(basins)-1]) * len(basins[len(basins)-2])
      * len(basins[len(basins)-3]))
