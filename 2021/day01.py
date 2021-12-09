with open("1.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

# Part 1
increases = 0
for i in range(0, len(lines)-1):
    if int(lines[i]) < int(lines[i+1]):
        increases += 1
print(increases)

# Part 2
increases = 0
for i in range(0, len(lines)-3):
    if (int(lines[i]) + int(lines[i+1]) + int(lines[i+2])) < (int(lines[i+1]) + int(lines[i+2]) + int(lines[i+3])):
        increases += 1
print(increases)
