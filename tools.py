import csv
from random import randint

def createPassengerCSV(passengerNum, passengerMax):

    # passengerMax = 200
    # passengerNum = "656"
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

def getFullClassArray(classArray, passengerClassArray):
    #Which Array, need to sort out
    fullClassArray = []
    
    seatCumSum = 0
    passCumSum = 0

    for i in range(len(classArray)):
        classTitle = classArray[i][0]
        seatNum = classArray[i][1]
        passengerNum = passengerClassArray[i][1]
        diffNum = (seatNum-passengerNum)

        seatCumSum = seatCumSum + seatNum
        passCumSum = passCumSum + passengerNum

        fullClassArray.append([classTitle,seatNum,passengerNum,diffNum])

    fullClassArray.append(["Total", seatCumSum, passCumSum, (seatCumSum - passCumSum)])

    return(fullClassArray)