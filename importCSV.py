import csv

# def incrementClassCapacity(classNum, capacityArray):

#     exists = False

#     for i in capacityArray:
#         if i[0] == classNum:
#             exists = True
#             i[1] += 1

#     if not exists:
#         capacityArray.append([classNum,1])

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
            #print(row)
            passengerData.append(row)

        return passengerData