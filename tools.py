# Name: Isaac Ponsford
# Student ID: 201458733
# Title: tools.py
# Description: Miscellaneous tools and functions for the rest of the code

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

    prefArray = ['W', 'A']
    maxGroupSize = 5
    csv_file = "passengerCSV/" + passengerNum + ".csv"

    file = open(csv_file, 'w', encoding='UTF8', newline='')
    writer = csv.writer(file)

    row = ["groupID","flightRef","key","class","splitable", "preferences"]
    writer.writerow(row)

    for i in array:

        currentClass = i[0]
        currentAmount = i[1]
        currentGroupSize = 0
        groupSize = 0

        for j in range(currentAmount):
            
            if currentGroupSize == groupSize or groupSize == 0:

                groupSize = randint(1, maxGroupSize)

                codeLetter = (chr(96 + randint(1,26)))
                codeNum = randint(0,9)
                code = str(currentClass) + str(codeLetter) + str(codeNum)

                currentGroupSize = 0

            keyNum = randint(1,100)
            if keyNum < 70:
                key = 'A'
            else:
                key = 'C'
            
            prefNum = randint(0,1)
            pref = prefArray[prefNum]

            row = [code,passengerNum,key,str(currentClass),"", pref]
            writer.writerow(row)
            currentGroupSize = currentGroupSize + 1

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
    
    length = len(seats)
    
    for i in range(9):
        actual.append([i+1,0])

    for i in range(9):
        upDowns.append([0,0])

    passengersTemp = listExtend(passengers, 9)
    seatsTemp = listExtend(seats, 9)

    moveUp(passengersTemp, actual, 8, 0, seatsTemp, upDowns)

    for x in upDowns:
        currentUp, currentDown = x
        if currentUp != 0 and currentDown != 0:
            if currentUp > currentDown:
                x[0] = currentUp - currentDown
                x[1] = 0
            elif currentUp < currentDown:
                x[1] = currentDown - currentUp
                x[0] = 0
            else:
                x[0] = 0
                x[1] = 0

    actual = actual[0:length]
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

    length = max(len(seats), len(passengers), len(actual)) 

    seats = listExtend(seats, length)
    passengers = listExtend(passengers, length)
    actual = listExtend(actual, length)

    fullActualArray = []

    seatCumSum = 0
    passCumSum = 0

    for i in range(length):
        classTitle = seats[i][0]

        seatNum = seats[i][1]
        passengerNum = passengers[i][1]
        actualNum = actual[i][1]

        diffNum = (seatNum - actualNum)

        seatCumSum = seatCumSum + seatNum
        passCumSum = passCumSum + passengerNum

        try:
            upNum = upDowns[i][0]
        except:
            upNum = 0
        
        try:
            downNum = upDowns[i][1]
        except:
            downNum=0

        fullActualArray.append([classTitle, seatNum, passengerNum, actualNum, diffNum, upNum, downNum])

    fullActualArray.append(["Total", seatCumSum, passCumSum,passCumSum, (seatCumSum - passCumSum)])

    return(fullActualArray)

def listExtend(array, desiredLength):

    out = []

    for i in range(desiredLength):
        try:
            out.append(array[i])
        except:
            out.append((i+1, 0))

    return out

def getPreferedSeats(passIDs, seats):

    wA = []
    aA = []
    bA = []
    awA = []

    wC = 0
    aC = 0
    bC = 0
    awC = 0

    for x in range(len(seats)):
        curr = seats[x]
        if curr[2] == 'W':
            wA.append(x)
        elif curr[2] == 'A':
            aA.append(x)
        elif curr[2] == '':
            bA.append(x)
        elif curr[2] == 'AW':
            awA.append(x)

    outArray = []
    remainingPassengers = []

    for passID in passIDs:

        if passID[1] == 'W':
            if wC < len(wA):
                outArray.append((passID[0], seats[wA[wC]][0],seats[wA[wC]][1]))
                wC = wC + 1
                continue
            else:
                if awC < len(awA):
                    outArray.append((passID[0], seats[awA[awC]][0],seats[awA[awC]][1]))
                    awC = awC + 1
                    continue
        
        if passID[1] == 'A':
            if aC < len(aA):
                outArray.append((passID[0], seats[aA[aC]][0],seats[aA[aC]][1]))
                aC = aC + 1
                continue
            else:
                if awC < len(awA):
                    outArray.append((passID[0], seats[awA[awC]][0],seats[awA[awC]][1]))
                    awC = awC + 1
                    continue

        if passID[1] == '':
            if bC < len(bA):
                outArray.append((passID[0], seats[bA[bC]][0],seats[bA[bC]][1]))
                bC = bC + 1
                continue

        remainingPassengers.append(passID)

    for passID in remainingPassengers:

        if awC < len(awA):
            outArray.append((passID[0], seats[awA[awC]][0],seats[awA[awC]][1]))
            awC = awC + 1
            continue

        if wC < len(wA):
            outArray.append((passID[0], seats[wA[wC]][0],seats[wA[wC]][1]))
            wC = wC + 1
            continue
                
        if aC < len(aA):
            outArray.append((passID[0], seats[aA[aC]][0],seats[aA[aC]][1]))
            aC = aC + 1
            continue

        if bC < len(bA):
            outArray.append((passID[0], seats[bA[bC]][0],seats[bA[bC]][1]))
            bC = bC + 1
            continue

    return outArray
    