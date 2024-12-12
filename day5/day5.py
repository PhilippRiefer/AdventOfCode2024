import math

input = "day5/inputday5.txt"

pageOrderRules = []
printOrders = []

with open(input, "r") as file:
    for line in file:
        if '|' in line:
            pageOrderRules.append(list(map(int, line.strip().split('|'))))
        elif ',' in line:
            printOrders.append(list(map(int, line.strip().split(','))))

# iterating over printOrders while removing objects causes to skip, since the indices get messed up.
# iterating over a copy only works with:
newPrintOrders = printOrders[:]
# and not with:
# newPrintOrders = printOrders
# because the [:] creates a shallow copy of the list, so a new list with the same elements
# the new list is then independent of the original
# newPrintOrders = printOrders creates a reference (or pointer) to the original list
# so modifying newPrintOrders also affects printOrders

for printOrder in printOrders:
    for pageOrderRule in pageOrderRules:
        if pageOrderRule[0] in printOrder:
            if pageOrderRule[1] in printOrder:
                if printOrder.index(pageOrderRule[0]) > printOrder.index(pageOrderRule[1]):
                    if printOrder in newPrintOrders:
                        newPrintOrders.remove(printOrder)

sumOfMiddleNumbers = 0

for printOrder in newPrintOrders:
    sumOfMiddleNumbers += printOrder[math.floor(len(printOrder)/2)]

print(f"Day 5, Problem 1: Sum of the middle numbers of the correct print orders = {sumOfMiddleNumbers}")