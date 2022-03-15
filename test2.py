def calculateExcess(testPlane, testPassenger):
    excess = []
    for i in range(len(testPlane)):
        excess.append([testPlane[i][0], (testPassenger[i][1] - testPlane[i][1])])
    return(excess)

def aboveCapacity(list, index):
    ac = 0
    index = index - 1

    while index > -1:
        ac = ac + list[index][1]
        index = index - 1

    return(ac)

def moveAbove(passengers, excess, index, amount):

    if amount == 0:
        return(passengers)
    else:
        currentExcess = excess[index][1]
        if currentExcess < 0 :
            if (currentExcess*-1) > amount:
                inputVal = amount
            else:
                inputVal = currentExcess*-1
            amount = amount - inputVal
            passengers[index][1] = passengers[index][1] + inputVal
            moveAbove(passengers, excess, index-1, amount)

def moveDown(passengers, excess, index, amount):

    if amount == 0:
        return(passengers)
    else:
        currentExcess = excess[index][1]
        if currentExcess < 0 :
            if (currentExcess*-1) > amount:
                inputVal = amount
            else:
                inputVal = currentExcess*-1
            amount = amount - inputVal
            passengers[index][1] = passengers[index][1] + inputVal
            moveAbove(passengers, excess, index+1, amount)

def fix(testPlane, testPassenger):
    excess = calculateExcess(testPlane, testPassenger)

    l = 4

    for i in range(l):

        index = l-1-i

        curr = excess[index][1]

        if curr > 0:
            ac = -1 * aboveCapacity(excess, index)
            if ac > 0:
                if ac > curr:
                    testPassenger[index][1] = testPassenger[index][1] - curr
                    moveAbove(testPassenger, excess, index-1, curr)
                elif ac < curr:
                    testPassenger[index][1] = testPassenger[index][1] - ac
                    moveAbove(testPassenger, excess, index-1, ac)

                    downAmount = curr - ac

                    testPassenger[index][1] = testPassenger[index][1] - downAmount
                    moveDown(testPassenger, excess, index+1, downAmount)
            else:
                downAmount = curr
                testPassenger[index][1] = testPassenger[index][1] - downAmount
                moveDown(testPassenger, excess, index+1, downAmount)
            
            excess = calculateExcess(testPlane, testPassenger)

    print(testPassenger)

testPlane = [[1,20], [2,40], [3,50], [4,100]]
testPassenger = [[1,5],[2,10],[3,90],[4,40]]

fix(testPlane, testPassenger)


# testPlane = [[1,20], [2,40], [3,50], [4,100]]
# testPassenger = [[1,5],[2,10],[3,90],[4,60]]
# #excess = [[1, -15], [2, -30], [3, 40], [4, -40]]

# def arrayAdd(list1,list2, index):
#     return [list1[index][0], (list1[index][1] + list2[index][1])]

# excess = []
# x = len(testPlane)

# for i in range(x):
#     excess.append([testPlane[i][0], (testPassenger[i][1] - testPlane[i][1])])

# actual = []

# for i in range(x):

#     index = x-(i+1)
#     curentClass = excess[index]

#     print(testPassenger[index][0], testPassenger[index][1] , excess[index][1], testPlane[index][1])

#     if curentClass[1] > 0:
#         actual.append(testPlane[index])
#     else:
#         if (testPassenger[index] + excess[index]) > testPlane[index]:
#             actual.append(testPlane[index])
#             excess[index-1][1] = excess[index-1][1]  + (testPassenger[index][1] + excess[index][1]) - testPlane[index][1]
#         else:
#             actual.append(arrayAdd(testPassenger, excess, index))