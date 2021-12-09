import re

with open("5.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def createMap():
    map = []
    for i in range(0, 1000):
        row = [0] * 1000
        map.append(row)
    return map


def fillMap(map, lines, partTwo):
    for line in lines:
        pattern = "([0-9]*),([0-9]*) -> ([0-9]*),([0-9]*)"
        search = re.search(pattern, line)
        x1 = int(search.group(1))
        y1 = int(search.group(2))
        x2 = int(search.group(3))
        y2 = int(search.group(4))
        if y1 == y2:
            if x1 <= x2:
                for i in range(0, x2-x1+1):
                    map[x1+i][y1] += 1
            else:
                for i in range(0, x1-x2+1):
                    map[x2+i][y1] += 1
        elif x1 == x2:
            if y1 <= y2:
                for i in range(0, y2-y1+1):
                    map[x1][y1+i] += 1
            else:
                for i in range(0, y1-y2+1):
                    map[x1][y2+i] += 1
        elif partTwo:
            if (x1 <= x2 and y1 <= y2):
                for i in range(0, x2-x1+1):
                    map[x1+i][y1+i] += 1
            if (x1 <= x2 and y1 >= y2):
                for i in range(0, x2-x1+1):
                    map[x1+i][y1-i] += 1
            if (x1 > x2 and y1 <= y2):
                for i in range(0, x1-x2+1):
                    map[x1-i][y1+i] += 1
            if (x1 > x2 and y1 >= y2):
                for i in range(0, x1-x2+1):
                    map[x1-i][y1-i] += 1
    return map


def countOverlapping(map):
    count = 0
    for i in range(0, 1000):
        for j in range(0, 1000):
            if map[i][j] > 1:
                count += 1
    return count


def calculate(partTwo):
    map = createMap()
    map = fillMap(map, lines, partTwo)
    print(countOverlapping(map))


# Part 1
calculate(False)

# Part 2
calculate(True)
