import collections
import copy
import math

with open("14.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def addOrSet(dict, key, value):
    if key in dict:
        dict[key] += value
    else:
        dict[key] = value


def solve(steps):
    start = lines[0]
    after = {}
    for i in range(0, len(start)-1):
        addOrSet(after, start[i:i+2], 1)

    insertions = {}
    for i in range(2, len(lines)):
        pair, insertion = lines[i].split(" -> ")
        insertions[pair] = insertion

    counter = {}
    for i in range(0, steps):
        before = copy.deepcopy(after)
        for j in range(0, len(list(insertions))):
            insertion = list(insertions)[j]
            if insertion in before and before[insertion] > 0:
                addOrSet(after, insertion[0] + list(insertions.values())[j], before[insertion])
                addOrSet(after, list(insertions.values())[j] + insertion[1], before[insertion])
                after[insertion] -= before[insertion]

    for i in range(0, len(after)):
        addOrSet(counter, list(after.keys())[i][0], list(after.values())[i])
        addOrSet(counter, list(after.keys())[i][1], list(after.values())[i])

    for i in range(0, len(counter)):
        counter[list(counter.keys())[i]] = math.ceil(
            list(counter.values())[i]/2)
    s = sorted(counter.items(), key=lambda item: item[1])
    print(s[len(s)-1][1]-s[0][1])


# Part 1
solve(10)

# Part 2
solve(40)