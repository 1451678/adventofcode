with open("13.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def initGrid():
    i = 0
    rmax = 0
    cmax = 0
    while(lines[i] != ""):
        r = int(lines[i].split(",")[0])
        c = int(lines[i].split(",")[1])
        if r > rmax:
            rmax = r
        if c > cmax:
            cmax = c
        i += 1

    G = []
    for i in range(0, cmax+1):
        row = [0] * (rmax+1)
        G.append(row)
    return G


def foldX(G, line):
    X = []
    for r in range(0, len(G)):
        row = [0] * line
        X.append(row)
    for r in range(0, len(G)):
        for c in range(0, line):
            X[r][c] = G[r][c]
    for r in range(0, len(G)):
        for c in range(2*line, line, -1):
            if len(G[0]) > c and X[r][2*line-c] == 0:
                X[r][2*line-c] += G[r][c]
    return X


def foldY(G, line):
    X = []
    for r in range(0, line):
        row = [0] * len(G[0])
        X.append(row)
    for r in range(0, line):
        for c in range(0, len(G[0])):
            X[r][c] = G[r][c]
    for r in range(2*line, line, -1):
        for c in range(0, len(G[0])):
            if len(G) > r and X[2*line-r][c] == 0:
                X[2*line-r][c] += G[r][c]
    return X


def fold(index):
    global G
    direction, line = lines[index].split("=")
    if "x" in direction:
        G = foldX(G, int(line))
    else:
        G = foldY(G, int(line))


# Part 1
G = initGrid()

index = 0
while(lines[index] != ""):
    c = int(lines[index].split(",")[0])
    r = int(lines[index].split(",")[1])
    G[r][c] = 1
    index += 1

fold(index+1)

result = 0
for i in range(0, len(G)):
    result += sum(G[i])
print(result)

# Part 2
for j in range(index+2, len(lines)):
    fold(j)

for r in range(0, len(G)):
    out = ""
    for c in range(0, len(G[0])):
        if G[r][c] == 0:
            out += "  "
        else:
            out += "##"
    print(out)
