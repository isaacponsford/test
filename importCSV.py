import csv

def incrementClassCapacity(classNum, capacityArray):

    exists = False

    for i in capacityArray:
        if i[0] == classNum:
            exists = True
            i[1] += 1

    if not exists:
        capacityArray.append([classNum,1])

def planeMetrics(csv_file):

    csv_file = "C:/Users/Alan/Documents/_Isaac/planeLayouts/" + csv_file + ".csv"
    capacity = 0
    noOfRows = 0
    noOfColumns = 0
    capacityArray = []
    planeLayout = []

    with open(csv_file, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        for row in reader:
            
            rowNumber = int(row[0])
            
            if rowNumber > noOfRows:
                noOfRows = rowNumber
                
            rowLayout = row[1::]
            planeLayout.append(rowLayout)
            
            noOfColumns = len(rowLayout)
            
            for seat in rowLayout:
                if seat != '':
                    capacity = capacity + 1
                    incrementClassCapacity(seat, capacityArray)

    return[noOfRows, noOfColumns, capacity, capacityArray, planeLayout]