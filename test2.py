def testSum(list):
    cumSum = 0

    for x in list:
        cumSum =cumSum +x [1]

    print(cumSum)

def moveDown(passengers, seats, downgradeAmount, index, upDowns):
    inputVal = 0

    if downgradeAmount == 0:
        pass
    else:
        currentExcess = seats[index][1]  - passengers[index][1] 
        if currentExcess > 0 :

            if currentExcess > downgradeAmount:
                inputVal = downgradeAmount
            else:
                inputVal = currentExcess

            downgradeAmount = downgradeAmount - inputVal
            passengers[index][1] = passengers[index][1] + inputVal
            
        if index != 1:
            upDowns[index-1][1] = inputVal

        moveDown(passengers, seats, downgradeAmount, index+1, upDowns)

def moveUp(passengers, actual, index, upgradeAmount, seats, upDowns):

    if index < 0:
        if upgradeAmount == 0:
            pass
        else:  
            moveDown(actual, seats, upgradeAmount, 0, upDowns)
    else:
        if passengers[index][1] + upgradeAmount < seats[index][1]:
            actual[index][1] = passengers[index][1] + upgradeAmount
            upgradeAmount = 0
        else:
            actual[index][1] = seats[index][1]
            upgradeAmount = upgradeAmount +  (passengers[index][1] - actual[index][1])

        if index != 0:
            upDowns[index-1][0] = upgradeAmount
        else:
            upDowns[0][1] = upgradeAmount

        moveUp(passengers, actual, index-1, upgradeAmount, seats, upDowns)
        
def getPlaneActual(seats, passengers):
    actual = []
    upDowns = []

    length = max(len(seats),len(passengers))
    
    for i in range(length):
        actual.append([i+1,0])

    for i in range(length-1):
        upDowns.append([0,0])

    moveUp(testPassenger, actual, length-1, 0, testPlane, upDowns)

    return[actual, upDowns]


testPlane = [[1,50], [2,20], [3,60], [4,200],[5,80]]
testPassenger = [[1,0],[2,40],[3,60],[4,150],[5,100]]

testSum(testPassenger)

actual, upDowns = getPlaneActual(testPlane, testPassenger)

print(actual)
testSum(actual)

# for x in upDowns:
#     currentUp, currentDown = x

#     if currentUp != 0 and currentDown != 0:
#         if currentUp > currentDown:
#             currentUp = currentUp - currentDown
#             currentDown = 0
#         elif currentUp < currentDown:
#             currentDown = currentDown - currentUp
#             currentUp = 0

print(upDowns)