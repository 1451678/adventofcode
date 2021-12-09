with open("7.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def calculateFuel(positions, destination, partTwo):
    fuel = 0
    for position in positions:
        n = abs(destination-position)
        fuel += n
        if partTwo:
            fuel += n*(n-1)/2
    return int(fuel)


def search(partTwo):
    positions = [int(x) for x in lines[0].split(',')]
    fuel1 = 0
    fuel2 = 0
    i = 0
    while (fuel1 >= fuel2):
        fuel1 = calculateFuel(positions, i, partTwo)
        fuel2 = calculateFuel(positions, i+1, partTwo)
        i += 1
    print(fuel1)


# Part 1
search(False)

# Part 2
search(True)
