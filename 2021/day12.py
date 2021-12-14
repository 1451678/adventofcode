with open("12.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def fillDict():
    for i in range(0, len(lines)):
        start, end = lines[i].split("-")
        if start != "end" and end != "start":
            if start not in dict:
                dict[start] = [end]
            else:
                dict[start].append(end)
        if start != "start" and end != "end":
            if end not in dict:
                dict[end] = [start]
            else:
                dict[end].append(start)


def search(visited, cave, twice):
    if (cave.isupper() or cave not in visited or not twice):
        if cave.islower() and cave in visited:
            twice = True
        visited.append(cave)
        if cave == "end":
            paths.append(visited)
        else:
            for i in range(0, len(dict[cave])):
                path = visited[:]
                search(path, dict[cave][i], twice)


# Part 1
dict = {}
paths = []
fillDict()
search([], "start", True)
print(len(paths))


# Part 2
paths = []
search([], "start", False)
print(len(paths))
