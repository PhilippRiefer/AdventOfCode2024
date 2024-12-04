input = "day2/inputday2.txt"

reports = []

with open(input, "r") as file:
    for line in file:
        reports.append(line.split())

# print(reports)

# Change the strings into numbers

for i, line in enumerate(reports):
    for j, number in enumerate(line):
        reports[i][j] = int(number)

# print(reports)

safeCounter = 0
increasing = 0 # if the set is increasing, increasing = 1, if its decreasing, increasing = 2
unsafe = False

for i in range(len(reports)):
    for j in range(len(reports[i]) - 1):
        if reports[i][j] == reports[i][j+1]:
            unsafe = True
            break
        if reports[i][j] > reports[i][j+1]:
            if increasing == 1:
                unsafe = True
                break
            increasing = 2
            if (reports[i][j] - reports[i][j+1]) > 3 or (reports[i][j] - reports[i][j+1]) < 1:
                unsafe = True
                break
        if reports[i][j] < reports[i][j+1]:
            if increasing == 2:
                unsafe = True
                break
            increasing = 1
            if (reports[i][j+1] - reports[i][j]) > 3 or (reports[i][j+1] - reports[i][j]) < 1:
                unsafe = True
                break
    if not unsafe:
        safeCounter += 1
    unsafe = False
    increasing = 0

print(f"Day 2, Problem 1: Number of safe reports = {safeCounter}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

safeCounter = 0
increasing = 0 # if the set is increasing, increasing = 1, if its decreasing, increasing = 2
unsafeCounter = 0

for i in range(len(reports)):
    for j in range(len(reports[i]) - 1):
        if reports[i][j] == reports[i][j+1]:
            unsafeCounter += 1
        if reports[i][j] > reports[i][j+1]:
            if increasing == 1:
                unsafeCounter += 1
            else:
                increasing = 2
                if (reports[i][j] - reports[i][j+1]) > 3 or (reports[i][j] - reports[i][j+1]) < 1:
                    unsafeCounter += 1
        if reports[i][j] < reports[i][j+1]:
            if increasing == 2:
                unsafeCounter += 1
            else:
                increasing = 1
                if (reports[i][j+1] - reports[i][j]) > 3 or (reports[i][j+1] - reports[i][j]) < 1:
                    unsafeCounter += 1
    if unsafeCounter <= 1:
        safeCounter += 1
    unsafeCounter = 0
    increasing = 0

print(f"Day 2, Problem 2: Number of safe reports with Problem Dampener = {safeCounter}")