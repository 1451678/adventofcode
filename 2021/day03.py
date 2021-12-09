with open("3.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def checkPattern(line, pattern):
    for i in range(len(pattern)):
        if line[i] != pattern[i]:
            return False
    return True


def getRating(lines, f1, f2):
    pattern = ""
    lastNumber = ""
    for i in range(len(lines[0])):
        c0 = 0
        c1 = 0
        for line in lines:
            if checkPattern(line, pattern):
                if line[i] == "0":
                    c0 += 1
                else:
                    c1 += 1
                lastNumber = line
        if int(c0) + int(c1) == 1:
            return lastNumber
        elif int(c0) <= int(c1):
            pattern += f1
        else:
            pattern += f2
    return lastNumber


# Part 1
gamma = ""
epsilon = ""
for i in range(len(lines[0])):
    c0 = 0
    c1 = 0
    for line in lines:
        if line[i] == "0":
            c0 += 1
        else:
            c1 += 1
    if int(c0) < int(c1):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
print(int(gamma, 2)*int(epsilon, 2))

# Part 2
print(int(getRating(lines, "1", "0"), 2)*int(getRating(lines, "0", "1"), 2))
