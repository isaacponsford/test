import csv
from random import randint

def createPassengerCSV(passengerNum, passengerMax):

    passengerCount = 0

    prefArray = ['W', 'A']
    maxGroupSize = 4
    csv_file = "passengerCSV/" + passengerNum + ".csv"

    file = open(csv_file, 'w', encoding='UTF8', newline='')
    writer = csv.writer(file)
    
    while passengerCount < passengerMax:
        
        groupSize = randint(1, maxGroupSize)
        classNum = randint(1,4)

        codeLetter = (chr(96 + randint(1,26)))
        codeNum = randint(0,9)
        code = str(codeLetter) + str(codeNum)

        for i in range(groupSize):
            #if passengerCount < passengerMax:
            keyNum = randint(1,100)
            if keyNum < 70:
                key = 'A'
            else:
                key = 'C'
            
            prefNum = randint(0,1)
            pref = prefArray[prefNum]

            row = [code,passengerNum,key,str(classNum),"", pref]
            writer.writerow(row)
            passengerCount = passengerCount + 1

    file.close()

def createPassCSVArray(passengerNum, array):

    #array = [[1,20],[2,40],[3,40],[4,120]]

    passengerCount = 0

    prefArray = ['W', 'A']
    maxGroupSize = 4
    csv_file = "passengerCSV/" + passengerNum + ".csv"

    file = open(csv_file, 'w', encoding='UTF8', newline='')
    writer = csv.writer(file)

    for i in array:

        currentClass = i[0]
        currentAmount = i[1]
        passengerCount = 0

        while True:
            groupSize = randint(1, maxGroupSize)

            codeLetter = (chr(96 + randint(1,26)))
            codeNum = randint(0,9)
            code = str(codeLetter) + str(codeNum)

            for i in range(groupSize):
                
                if passengerCount > currentAmount:
                    break
                else:

                    keyNum = randint(1,100)
                    if keyNum < 70:
                        key = 'A'
                    else:
                        key = 'C'
                    
                    prefNum = randint(0,1)
                    pref = prefArray[prefNum]

                    row = [code,passengerNum,key,str(currentClass),"", pref]
                    writer.writerow(row)
                    passengerCount = passengerCount + 1
            break

def isBlank(array):
    blank = True

    for element in array:
        if element != "":
            blank = False
    
    return blank

def totalCapacity(array):
    total = 0
    for i in array:
        total = total + i[1]

    return(total)

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

    moveUp(passengers, actual, length-1, 0, seats, upDowns)

    return[actual, upDowns]

def getFullClassArray(classArray, passengerClassArray):
    fullClassArray = []
    
    seatCumSum = 0
    passCumSum = 0

    if len(classArray) < len(passengerClassArray):
        longest = passengerClassArray
    else:
        longest = classArray

    for i in range(len(longest)):
        classTitle = longest[i][0]

        try:
            seatNum = classArray[i][1]
        except:
            seatNum = 0
        
        try:
            passengerNum = passengerClassArray[i][1]
        except:
            passengerNum = 0
        
        diffNum = (seatNum-passengerNum)

        seatCumSum = seatCumSum + seatNum
        passCumSum = passCumSum + passengerNum

        fullClassArray.append([classTitle,seatNum,passengerNum,diffNum])

    fullClassArray.append(["Total", seatCumSum, passCumSum, (seatCumSum - passCumSum)])

    return(fullClassArray)

def getFullActualArray(seats, passengers, actual, upDowns):
    fullActualArray = []

    seatCumSum = 0
    passCumSum = 0

    for i in range(len(seats)):
        classTitle = seats[i][0]

        seatNum = seats[i][1]
        passengerNum = passengers[i][1]
        actualNum = actual[i][1]

        diffNum = (seatNum - actualNum)

        seatCumSum = seatCumSum + seatNum
        passCumSum = passCumSum + passengerNum

        fullActualArray.append([classTitle, seatNum, passengerNum, actualNum, diffNum])

    fullActualArray.append(["Total", seatCumSum, passCumSum,passCumSum, (seatCumSum - passCumSum)])

    return(fullActualArray)