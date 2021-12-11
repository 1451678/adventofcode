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


def flash(x1, y1):
    global flashes
    G[x1][y1] = 0
    flashes += 1
    for i in range(-1, 2):
        for j in range(-1, 2):
            x2 = x1+i
            y2 = y1+j
            if x2 >= 0 and x2 < len(G) and y2 >= 0 and y2 < len(G[0]):
                if G[x2][y2] != 0:
                    if G[x2][y2] >= 9:
                        flash(x2, y2)
                    else:
                        G[x2][y2] += 1


def synchronized(G):
    for x in range(0, len(G)):
        for y in range(0, len(G[0])):
            if G[x][y] != 0:
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
