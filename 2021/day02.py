with open("2.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

# Part 1
x = 0
y = 0
for line in lines:
    command, power = line.split(" ")
    power = int(power)
    if command[0] == "f":
        x += power
    elif command[0] == "u":
        y -= power
    elif command[0] == "d":
        y += power
print(x*y)

# Part 2
x = 0
y = 0
aim = 0
for line in lines:
    command, power = line.split(" ")
    power = int(power)
    if command[0] == "f":
        x += power
        y += (aim*power)
    elif command[0] == "u":
        aim -= power
    elif command[0] == "d":
        aim += power
print(x*y)
