import csv
from random import randint

def createPassengerCSV():

    passengerNum = "656"
    maxGroupSize = 5
    prefArray = ['W', 'A']

    csv_file = "passengerCSV/" + passengerNum + ".csv"

    file = open(csv_file, 'w', encoding='UTF8')
    writer = csv.writer(file)

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

        row = code + "," + passengerNum + "," + key + "," + str(classNum) + "," + "," + pref + "\n"
        writer.writerow(row)

    file.close()

def isBlank(array):
    blank = True

    for element in array:
        if element != "":
            blank = False
    
    return blank