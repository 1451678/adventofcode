with open("11.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def fillGrid():
    for line in lines:
        G.append(list([int(x) for x in line]))


def step():
    for x in range(0, len(G)):
        for y in range(0, len(G[0])):
            G[x][y] += 1
    for x in range(0, len(G)):
        for y in range(0, len(G[0])):
            if G[x][y] > 9:
                flash(x, y)


def flash(r1, c1):
    global flashes
    G[r1][c1] = 0
    flashes += 1
    for i in range(-1, 2):
        for j in range(-1, 2):
            r2 = r1+i
            c2 = c1+j
            if r2 >= 0 and r2 < len(G) and c2 >= 0 and c2 < len(G[0]):
                if G[r2][c2] != 0:
                    if G[r2][c2] >= 9:
                        flash(r2, c2)
                    else:
                        G[r2][c2] += 1


def synchronized(G):
    for r in range(0, len(G)):
        for c in range(0, len(G[0])):
            if G[r][c] != 0:
                return False
    return True


# Part 1
G = []
fillGrid()
flashes = 0
for i in range(0, 100):
    step()
    all = True
print(flashes)

# Part 2
G = []
fillGrid()
isSynchronized = False
steps = 0
while not isSynchronized:
    step()
    steps += 1
    isSynchronized = synchronized(G)
print(steps)
