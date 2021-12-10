with open("10.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

# Part 1
luc = {"(": ")", ")": "(", "[": "]", "]": "[",
       "{": "}", "}": "{", "<": ">", ">": "<"}
lup = {")": 3, "]": 57, "}": 1197, ">": 25137}

score = 0
for line in lines:
    stack = []
    for i in range(0, len(line)):
        if line[i] in ["(", "[", "{", "<"]:
            stack.append(line[i])
        elif len(stack) > 0 and luc[line[i]] == stack[len(stack)-1]:
            stack.pop(len(stack)-1)
        else:
            score += lup[line[i]]
            break
print(score)


# Part 2
lup = {")": 1, "]": 2, "}": 3, ">": 4}

scores = []
for line in lines:
    stack = []
    score = 0
    for i in range(0, len(line)):
        if line[i] in ["(", "[", "{", "<"]:
            stack.append(line[i])
        elif len(stack) > 0 and luc[line[i]] == stack[len(stack)-1]:
            stack.pop(len(stack)-1)
        else:
            break
    if i == len(line)-1:
        for i in range(len(stack)-1, -1, -1):
            score = score * 5 + lup[luc[stack[i]]]
        scores.append(score)
scores.sort()
print(scores[int((len(scores) - 1)/2)])
