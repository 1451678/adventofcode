import array

with open("4.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def buildBoards(lines):
    boards = []
    for i in range(1, len(lines)):
        line = lines[i]
        if line == "":
            board = []
            boards.append(board)
            continue
        sline = line.strip().replace("  ", " ").split(" ")
        bline = []
        for j in range(len(sline)):
            bline.append(int(sline[j]))
        board.append(bline)
    boards.append(board)
    return boards


def checkWinH(board, winners):
    for r in range(len(board)):
        result = True
        column = board[r]
        for i in range(len(column)):
            number = column[i]
            if number not in winners:
                result = False
                break
        if result:
            return True
    return False


def checkWinV(board, winners):
    for c in range(len(board)):
        result = True
        for r in range(len(board)):
            number = board[r][c]
            if number not in winners:
                result = False
                break
        if result:
            return True
    return False


def sumUnmarked(board, winners):
    sum = 0
    for c in range(len(board)):
        for r in range(len(board)):
            number = board[c][r]
            if number not in winners:
                sum += number
    return sum


def printWinner(board, winners):
    sum = sumUnmarked(board, winners)
    lastWinner = winners[len(winners)-1]
    print(sum * lastWinner)


# Part 1
winners = []
index = 0
firstWinner = False
boards = buildBoards(lines)
numbers = [int(x) for x in lines[0].split(',')]

while not firstWinner:
    for board in boards:
        if checkWinH(board, winners) or checkWinV(board, winners):
            printWinner(board, winners)
            firstWinner = True
    winners.append(numbers[index])
    index += 1

# Part 2
winners = []
won = []
index = 0
lastWinner = False
while not lastWinner:
    for i in range(len(boards)):
        if i not in won:
            board = boards[i]
            if (checkWinH(board, winners) or checkWinV(board, winners)):
                won.append(i)
                if len(won) == len(boards):
                    lastWinner = True
    if not lastWinner:
        winners.append(numbers[index])
        index += 1

printWinner(board, winners)
