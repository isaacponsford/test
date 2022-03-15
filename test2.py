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
testPassenger = [[1,15],[2,45],[3,55],[4,40]]

fix(testPlane, testPassenger)

#aboveCapacity(testPlane, 2)