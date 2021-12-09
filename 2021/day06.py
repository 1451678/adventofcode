with open("6.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def calculate(days):
    fish = [int(x) for x in lines[0].split(',')]
    next = 0
    amounts = []

    for i in range(0, 9):
        amounts.append(0)

    for j in range(0, len(fish)):
        amounts[fish[j]] += 1

    for k in range(0, days):
        next = [0] * 9
        for l in range(0, 8):
            next[l] = amounts[l+1]
        next[6] += amounts[0]
        next[8] = amounts[0]
        amounts = next
    print(sum(amounts))


# Part 1
calculate(80)

# Part 2
calculate(256)
