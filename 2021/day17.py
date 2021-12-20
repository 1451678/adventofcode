import re

with open("17.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

pattern = "target area: x=([\-]?[0-9]*)\.\.([\-]?[0-9]*)\, y=([\-]?[0-9]*)\.\.([\-]?[0-9]*)"
search = re.search(pattern, lines[0])
x1 = int(search.group(1))
x2 = int(search.group(2))
y1 = int(search.group(3))
y2 = int(search.group(4))


def fire(px, py, x, y):
    lane = []
    while px <= x2 and py >= y1:
        lane.append((px, py))
        px = px + x
        py = py + y
        if x > 0:
            x = x-1
        y = y-1

    return lane


def inTargetArea(lane):
    for i in range(0, len(lane)):
        x = lane[i][0]
        y = lane[i][1]
        if x >= x1 and x <= x2 and y >= y1 and y <= y2:
            return True
    return False


def findHighestY(lanes):
    maxY = 0
    for i in range(0, len(lanes)):
        for j in range(0, len(lanes[i])):
            y = lanes[i][j][1]
            if y > maxY:
                maxY = y
    return maxY


# Part 1
lanes = []
velocities = []
for x in range(0, 1000):
    for y in range(-1000, 1000):
        lane = fire(0, 0, x, y)
        if inTargetArea(lane):
            lanes.append(lane)
            velocities.append(lane[1])
print(findHighestY(lanes))

# Part 2
print(len(velocities))
