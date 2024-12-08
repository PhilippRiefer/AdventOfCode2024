import numpy as np

input = "day4/inputday4.txt"

crossword = np.zeros((140,140), dtype='U1')

with open(input, "r") as file:
    for y, line in enumerate(file):
        for x, char in enumerate(line.strip()):
            crossword[x][y] = char

def inBounds(x, y):
    if (0 <= x < len(crossword)) and (0 <= y < len(crossword[x])):
        return True
    else:
        return False

# print(inBounds(139, 139))

XMASCounter = 0

for x in range(len(crossword)):
    for y in range(len(crossword[x])):
        # print(crossword[x][y])
        if crossword[x][y] == "X":
            for i, char in enumerate("MAS"):
                # check top left
                # x-i y-i
                # if inBounds(x-(i+1), y-(i+1)):
                #     print(crossword[x-(i+1)][y-(i+1)])
                if inBounds(x-(i+1), y-(i+1)) and crossword[x-(i+1)][y-(i+1)] == char:
                    # print(char, i)
                    if i == 2:
                        XMASCounter += 1
                else:
                    break
            for i, char in enumerate("MAS"):
                # check top center
                # x-i y
                # if inBounds(x-(i+1), y):
                #     print(crossword[x-(i+1)][y])
                if inBounds(x-(i+1), y) and crossword[x-(i+1)][y] == char:
                    # print(char, i)
                    if i == 2:
                        XMASCounter += 1
                else:
                    break
            for i, char in enumerate("MAS"):
                # check top right
                # x-i y+i
                # if inBounds(x-(i+1), y+(i+1)):
                #     print(crossword[x-(i+1)][y+(i+1)])
                if inBounds(x-(i+1), y+(i+1)) and crossword[x-(i+1)][y+(i+1)] == char:
                    # print(char, i)
                    if i == 2:
                        XMASCounter += 1
                else:
                    break
            for i, char in enumerate("MAS"):
                # check right
                # x   y+i
                # if inBounds(x, y+(i+1)):
                #     print(crossword[x][y+(i+1)])
                if inBounds(x, y+(i+1)) and crossword[x][y+(i+1)] == char:
                    # print(char, i)
                    if i == 2:
                        XMASCounter += 1
                else:
                    break
            for i, char in enumerate("MAS"):
                # check bottom right
                # x+i y+i
                # if inBounds(x+(i+1), y+(i+1)):
                #     print(crossword[x+(i+1)][y+(i+1)])
                if inBounds(x+(i+1), y+(i+1)) and crossword[x+(i+1)][y+(i+1)] == char:
                    # print(char, i)
                    if i == 2:
                        XMASCounter += 1
                else:
                    break
            for i, char in enumerate("MAS"):
                # check bottom center
                # x+i y
                # if inBounds(x+(i+1), y):
                #     print(crossword[x+(i+1)][y])
                if inBounds(x+(i+1), y) and crossword[x+(i+1)][y] == char:
                    # print(char, i)
                    if i == 2:
                        XMASCounter += 1
                else:
                    break
            for i, char in enumerate("MAS"):
                # check bottom left
                # x+i y-i
                # if inBounds(x+(i+1), y-(i+1)):
                #     print(crossword[x+i][y-i])
                if inBounds(x+(i+1), y-(i+1)) and crossword[x+(i+1)][y-(i+1)] == char:
                    # print(char, i)
                    if i == 2:
                        XMASCounter += 1
                else:
                    break
            for i, char in enumerate("MAS"):
                # check left
                # x   y-i
                # if inBounds(x, y-(i+1)):
                #     print(crossword[x][y-(i+1)])
                if inBounds(x, y-(i+1)) and crossword[x][y-(i+1)] == char:
                    # print(char, i)
                    if i == 2:
                        XMASCounter += 1
                else:
                    break

print(f"Day 4, Problem 1: Occurences of \"XMAS\": {XMASCounter}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

X_MASCounter = 0

for x in range(len(crossword)):
    for y in range(len(crossword[x])):
        if crossword[x][y] == "A":
            MAS_Counter = 0
            if inBounds(x-1, y-1) and crossword[x-1][y-1] == "M":
                if inBounds(x+1, y+1) and crossword[x+1][y+1] == "S":
                    MAS_Counter += 1
            if inBounds(x+1, y+1) and crossword[x+1][y+1] == "M":
                if inBounds(x-1, y-1) and crossword[x-1][y-1] == "S":
                    MAS_Counter += 1
            if inBounds(x+1, y-1) and crossword[x+1][y-1] == "M":
                if inBounds(x-1, y+1) and crossword[x-1][y+1] == "S":
                    MAS_Counter += 1
            if inBounds(x-1, y+1) and crossword[x-1][y+1] == "M":
                if inBounds(x+1, y-1) and crossword[x+1][y-1] == "S":
                    MAS_Counter += 1
            if MAS_Counter == 2:
                X_MASCounter += 1
print(f"Day 4, Problem 2: Occurences of \"X-MAS\": {X_MASCounter}")