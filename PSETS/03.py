# Task 03: Find the shortest and hightest number in the list

myList = [9, 3, 6, 4, 7, 2, 8, 1, 9]

def getShortestAndHightest():
    low = myList[0]
    high = myList[0]
    for num in myList:
        if num < low:
            low = num
        elif num > high:
            high = num
    print("Highest:", high, "Lowest:", low)

getShortestAndHightest()