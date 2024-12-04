input = "day1/inputday1.txt"
leftList = []
rightList = []
distances = []

with open(input, "r") as file:
    for line in file:
        # print(line.split())
        leftList.append(int(line.split()[0]))
        rightList.append(int(line.split()[1]))

leftList.sort()
rightList.sort()
# print(leftList)
# print(rightList)

for i in range(len(leftList)):
    distance = abs(leftList[i] - rightList[i])
    distances.append(distance)

# print(distances)
print(f"Day 1, Problem 1: Sum of distances = {sum(distances)}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

similarityScore = 0

for i in range(len(leftList)):
    similarityScore += leftList[i] * rightList.count(leftList[i])

print(f"Day 1, Problem 2: Similarity Score = {similarityScore}")