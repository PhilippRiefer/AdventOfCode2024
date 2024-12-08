import math

input = "day5/inputday5.txt"

pageOrderRules = []
printOrders = []

with open(input, "r") as file:
    for line in file:
        if '|' in line:
            # print(line.strip())
            # get the first parts, like 48|74
            # pageOrderRules.append([int(x) for x in line.strip().split("|")])
            pageOrderRules.append(list(map(int, line.strip().split('|'))))
        elif ',' in line:
            # print(line.strip())
            # printOrders.append([int(x) for x in line.strip().split(",")])
            printOrders.append(list(map(int, line.strip().split(','))))

# print(pageOrderRules[3])
# print(printOrders[3])

for printOrder in printOrders:
    print(printOrder)

# for pageOrderRule in pageOrderRules:
#     print(f"{pageOrderRule[0]}|{pageOrderRule[1]}")

# print(f"Number of print orders: {len(printOrders)}")

# # to confirm that there are no duplicates in the printOrder, set() throws out duplicates:
# for printOrder in printOrders:
#     if len(printOrder) != len(set(printOrder)):
#         print(printOrder)
#         print(set(printOrder))

for i, printOrder in enumerate(printOrders):
    # print(i)
    # print(protocol)
    for j, pageOrderRule in enumerate(pageOrderRules):
        # print(j)
        # print(pageOrderRule[0])
        # print(pageOrderRule[1])
        if pageOrderRule[0] in printOrder:
            # print()
            # print(f"{pageOrderRule[0]} is in {printOrder}")
            if pageOrderRule[1] in printOrder:
                # print()
                # print(f"{pageOrderRule[1]} is in {printOrder}")
                if printOrder.index(pageOrderRule[0]) > printOrder.index(pageOrderRule[1]):
                    # print()
                    # print(pageOrderRule)
                    # print(f"{pageOrderRule[0]} at position {printOrder.index(pageOrderRule[0])}")
                    # print(f"{pageOrderRule[1]} at position {printOrder.index(pageOrderRule[1])}")
                    # print(f"in {printOrder}")
                    printOrders.remove(printOrder)
                    # print(f"remaining print orders: {len(printOrders)}")
                    break
                # else:
                #     print()
                #     print(pageOrderRule)
                #     print(f"{pageOrderRule[0]} at position {printOrder.index(pageOrderRule[0])}")
                #     print(f"{pageOrderRule[1]} at position {printOrder.index(pageOrderRule[1])}")
                #     print(f"in {printOrder}")
                #     print("is correct!")
                #     print()
        #     else:
        #         print()
        #         print(f"{pageOrderRule[1]} not in {printOrder}")
        # else:
        #     print()
        #     print(f"{pageOrderRule[0]} not in {printOrder}")

# print(f"Remaining print orders: {len(printOrders)}")

sumOfMiddleNumbers = 0

for printOrder in printOrders:
    # print(f"length of the printOrder: {len(printOrder)}, half of that: {len(printOrder)/2}, middle index: {math.floor(len(printOrder)/2)} = {printOrder[math.floor(len(printOrder)/2)]}")
    # print(printOrder)
    sumOfMiddleNumbers += printOrder[math.floor(len(printOrder)/2)]

print(f"Day 5, Problem 1: Sum of the middle numbers of the correct print orders = {sumOfMiddleNumbers}")