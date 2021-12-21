with open("20.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

iea = lines[0]


def initGrid():
    G = []
    for i in range(2, len(lines)):
        G.append(list(lines[i]))
    return G


def expandGrid(G, fillChar):
    X = []
    for i in range(0, 4):
        row = [fillChar] * (len(G[0]) + 4)
        X.append(row)
    for i in range(0, len(G)):
        row = [fillChar] * 2 + list(G[i]) + [fillChar] * 2
        X.append(row)
    for i in range(0, 24):
        row = [fillChar] * (len(G[0]) + 4)
        X.append(row)
    return X


def strToChar(binstr):
    binstr = binstr.replace(".", "0")
    binstr = binstr.replace("#", "1")
    return iea[int(binstr, 2)]


def transform(G, step):
    if iea[0] == "#" and step % 2 == 1:
        G = expandGrid(G, "#")
    else:
        G = expandGrid(G, ".")
    X = []
    for r in range(1, len(G) - 1):
        row = []
        for c in range(1, len(G[0]) - 1):
            binstr = ""
            for i in range(-1, 2):
                for j in range(-1, 2):
                    binstr += G[r + i][c + j]
            row.append(strToChar(binstr))
        X.append(row)
    return X


def printLit(G):
    lit = 0
    for r in range(0, len(G)):
        for c in range(0, len(G[0])):
            if G[r][c] == "#":
                lit += 1
    print(lit)


# Part 1
G = initGrid()
for i in range(0, 2):
    G = transform(G, i)
printLit(G)


# Part 2
G = initGrid()
for i in range(0, 50):
    G = transform(G, i)
printLit(G)
