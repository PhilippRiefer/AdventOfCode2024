input = "day3/inputday3.txt"

data = ""

with open(input, "r") as file:
    for line in file:
        for char in line.strip():
            data += char
            # print(char)

# print(data)

multipliedNumbers = []

for i, char in enumerate(data):
    j = 0
    number1 = ""
    number2 = ""
    if data[i+j] == "m":
        j += 1
        if data[i+j] == "u":
            j += 1
            if data[i+j] == "l":
                j += 1
                if data[i+j] == "(":
                    j += 1
                    while data[i+j].isnumeric():
                        number1 += data[i+j]
                        j += 1
                    if data[i+j] == ",":
                        j += 1
                        while data[i+j].isnumeric():
                            number2 += data[i+j]
                            j += 1
                        if data[i+j] == ")":
                            multipliedNumbers.append(int(number1)*int(number2))

print(f"Day 3, Problem 1: Sum of the uncorrupted multiplication instructions: {sum(multipliedNumbers)}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

do = True
multipliedNumbers = []

for i, char in enumerate(data):
    j = 0
    number1 = ""
    number2 = ""
    if data[i+j] == "d":
        j += 1
        if data[i+j] == "o":
            j += 1
            if data[i+j] == "(":
                j += 1
                if data[i+j] == ")":
                    do = True
                    j = 0
            elif data[i+j] == "n":
                j += 1
                if data[i+j] == "'":
                    j += 1
                    if data[i+j] == "t":
                        j += 1
                        if data[i+j] == "(":
                            j += 1
                            if data[i+j] == ")":
                                do = False
                                j = 0

    if data[i+j] == "m":
        j += 1
        if data[i+j] == "u":
            j += 1
            if data[i+j] == "l":
                j += 1
                if data[i+j] == "(":
                    j += 1
                    while data[i+j].isnumeric():
                        number1 += data[i+j]
                        j += 1
                    if data[i+j] == ",":
                        j += 1
                        while data[i+j].isnumeric():
                            number2 += data[i+j]
                            j += 1
                        if data[i+j] == ")":
                            if do:
                                multipliedNumbers.append(int(number1)*int(number2))
                            j = 0

print(f"Day 3, Problem 2: Sum with dos and donts: {sum(multipliedNumbers)}")