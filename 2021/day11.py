with open("11.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def fillGrid():
    for line in lines:
        G.append(list([int(x) for x in line]))


def step():
    for r in range(0, len(G)):
        for c in range(0, len(G[0])):
            G[r][c] += 1
    for r in range(0, len(G)):
        for c in range(0, len(G[0])):
            if G[r][c] > 9:
                flash(r, c)


def flash(r, c):
    global flashes
    G[r][c] = 0
    flashes += 1
    for i in range(-1, 2):
        for j in range(-1, 2):
            nr = r+i
            nc = c+j
            if nr >= 0 and nr < len(G) and nc >= 0 and nc < len(G[0]) and G[nr][nc] != 0:
                if G[nr][nc] >= 9:
                    flash(nr, nc)
                else:
                    G[nr][nc] += 1


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
print(flashes)

# Part 2
G = []
fillGrid()
steps = 0
while not synchronized(G):
    step()
    steps += 1
print(steps)
