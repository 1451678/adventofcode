with open("8.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def containsAll(a, b):
    for letter in b:
        if letter not in a:
            return False
    return True


def difference(a, b):
    return "".join(set(a).symmetric_difference(b))


# Part 1
count = 0
for line in lines:
    before, after = line.split("|")
    after = after.strip().split(" ")
    numbers = [2, 3, 4, 7]
    for s in after:
        if len(s) in numbers:
            count += 1
print(count)

# Part 2
result = 0
for line in lines:
    before, after = line.split("|")
    before = before.strip().split(" ")
    before = list(sorted(before, key=len))
    after = after.strip().split(" ")

    dict = {}
    for s in before:
        s = "".join(sorted(s))
        if len(s) == 2:
            dict[s] = "1"
        elif len(s) == 3:
            dict[s] = "7"
        elif len(s) == 4:
            dict[s] = "4"
        elif len(s) == 5:
            if (containsAll(s, before[0])):
                dict[s] = "3"
            elif (containsAll(s, difference(before[0], before[2]))):
                dict[s] = "5"
            else:
                dict[s] = "2"
        elif len(s) == 6:
            if (containsAll(s, before[0])):
                if containsAll(s, before[2]):
                    dict[s] = "9"
                else:
                    dict[s] = "0"
            else:
                dict[s] = "6"
        elif len(s) == 7:
            dict[s] = "8"

    number = ""
    for s in after:
        number += dict[''.join(sorted(s))]

    result += int(number)

print(result)
