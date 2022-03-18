import csv

def planeMetrics(csv_file):

    noOfRows = 0
    noOfColumns = 0
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

    return[noOfColumns, rowTitles,columnTitles]


def getPlaneLayout(csv_file):

    planeLayout = []

    csv_file = "plane_layouts/" + csv_file + ".csv"

    with open(csv_file, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)

        columnTitles = next(reader)

        for row in reader:
            
            rowNumber = row[0]

            rowLayout = row[1::]
            planeLayout.append(rowLayout)
    

    return planeLayout
        
def getPassengerCSV(csv_file):

    passengerData = []
    
    csv_file = "passengerCSV/" + csv_file + ".csv"
    with open(csv_file, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)

        headings = next(reader)

        for row in reader:
            passengerData.append(row)

        return passengerData

def tempValid(csv_file):

    minVal = maxVal = 1

    csv_file = "plane_layouts/" + csv_file + ".csv"

    with open(csv_file, 'r', encoding='utf-8-sig') as file:
        
        reader = csv.reader(file)

        for row in reader:

            rowLayout = row[1::]
            for seat in rowLayout:
                
                if seat.isnumeric() == True:
                    
                    seat = int(seat)
                    if seat > maxVal:
                        maxVal = seat
                    elif seat < minVal:
                        minVal = seat
    
    return((minVal, maxVal))
    