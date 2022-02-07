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

    capacity = 0
    noOfRows = 0
    noOfColumns = 0
    capacityArray = []
    planeLayout = []
    rowTitles = []

    csv_file = "plane_layouts/" + csv_file + ".csv"

    with open(csv_file, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)

        columnTitles = next(reader)

        for row in reader:
            
            rowNumber = row[0]
            rowTitles.append(rowNumber)

            try:
                if int(rowNumber) > noOfRows:
                    noOfRows = int(rowNumber)
            except:
                pass

            rowLayout = row[1::]
            planeLayout.append(rowLayout)

            noOfColumns = len(rowLayout)
            
            for seat in rowLayout:
                if seat != '':
                    capacity = capacity + 1
                    incrementClassCapacity(seat, capacityArray)
    


    return[noOfRows, noOfColumns, capacity, capacityArray, planeLayout, rowTitles,columnTitles]

