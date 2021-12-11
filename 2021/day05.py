import re

with open("5.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def createGrid():
    G = []
    for i in range(0, 1000):
        row = [0] * 1000
        G.append(row)
    return G


def fillGrid(G, lines, partTwo):
    for line in lines:
        pattern = "([0-9]*),([0-9]*) -> ([0-9]*),([0-9]*)"
        search = re.search(pattern, line)
        r1 = int(search.group(1))
        c1 = int(search.group(2))
        r2 = int(search.group(3))
        c2 = int(search.group(4))
        if c1 == c2:
            if r1 <= r2:
                for i in range(0, r2-r1+1):
                    G[r1+i][c1] += 1
            else:
                for i in range(0, r1-r2+1):
                    G[r2+i][c1] += 1
        elif r1 == r2:
            if c1 <= c2:
                for i in range(0, c2-c1+1):
                    G[r1][c1+i] += 1
            else:
                for i in range(0, c1-c2+1):
                    G[r1][c2+i] += 1
        elif partTwo:
            if (r1 <= r2 and c1 <= c2):
                for i in range(0, r2-r1+1):
                    G[r1+i][c1+i] += 1
            if (r1 <= r2 and c1 >= c2):
                for i in range(0, r2-r1+1):
                    G[r1+i][c1-i] += 1
            if (r1 > r2 and c1 <= c2):
                for i in range(0, r1-r2+1):
                    G[r1-i][c1+i] += 1
            if (r1 > r2 and c1 >= c2):
                for i in range(0, r1-r2+1):
                    G[r1-i][c1-i] += 1
    return G


def countOverlapping(G):
    count = 0
    for r in range(0, 1000):
        for c in range(0, 1000):
            if G[r][c] > 1:
                count += 1
    return count


def calculate(partTwo):
    G = createGrid()
    G = fillGrid(G, lines, partTwo)
    print(countOverlapping(G))


# Part 1
calculate(False)

# Part 2
calculate(True)
