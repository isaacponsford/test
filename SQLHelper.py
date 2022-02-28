from msilib import sequence
import sqlite3
import csv

from importCSV import planeMetrics

#select columnTitle, rowTitle, class from airplaneLayout where flightNumber = "BA1"
#columnTitles = (planeMetrics("emb145")[6][1::])
# def titleClean(array):
#     cleanArray = []

#     for element in array:
#         if element != '':
#             cleanArray.append(element)
    
#     return(cleanArray)

conn = sqlite3.connect("seatSelector.db", check_same_thread=False)
cur= conn.cursor()

def insertPlaneLayout(data_tuple):
    base_sql = """insert into airplaneLayout (flightNumber, columnTitle, rowTitle, class, type, sequenceNumber) VALUES (?,?,?,?,?,?)"""
    cur.execute(base_sql, data_tuple)
    conn.commit()

def cleanup(temp, titles):

    if len(temp) == 1:
        return([temp[0],'','',''])
    elif len(temp) == 3:
        return([temp[0],'',temp[1],temp[2]])

def getPlaneInfo(flightNo):
    cur.execute("SELECT columnTitle, rowTitle, class, type from airplaneLayout WHERE flightNumber = ? ORDER By sequenceNumber", (flightNo,))
    all_data = cur.fetchall()

    layout = [] 
    temp = []
    titles = []
    count = 0

    blank = ['','','','']

    while count < len(all_data):

        current_data = all_data[count]
        temp.append(str(current_data[2]))
        titles.append(str(current_data[0]))

        if current_data[3] == 1:
            try:
                if all_data[count+1][1] > current_data[1]: #Comparing
                    temp = cleanup(temp, titles)
                    layout.append(temp)
                    temp = []
                    titles = []
                else:
                    pass
            except IndexError:
                temp = cleanup(temp, titles)
                layout.append(temp)
        elif current_data[3] == 99:
            layout.append(blank)
            temp = []
            titles = []

        count = count + 1

    return(layout)

def CSVtoSQL(flight_number, csv_add):

    Metrics = planeMetrics(csv_add)
    noOfColumns = Metrics[1]
    planeLayout = Metrics[4]
    rowTitles = Metrics[5]
    columnTitles = Metrics[6]

    columnCounter = 0
    rowCounter = 0
    seqNum = 1

    blank = ['','','','']

    while rowCounter < len(planeLayout):

        if planeLayout[rowCounter] == blank:
          
            insert_row = int(rowTitles[rowCounter-1]) + 1
            print(insert_row)
            insert_data = (flight_number, "", insert_row, "", 99, seqNum)
            insertPlaneLayout(insert_data)
            seqNum = seqNum + 1
        
        else:

            columnCounter = 0
            while columnCounter < noOfColumns:
                current = planeLayout[rowCounter][columnCounter]

                if current != '':
                    
                    insert_column = columnTitles[columnCounter+1]
                    insert_row = rowTitles[rowCounter]
                    insert_class = current
                    insert_type = 1

                    insert_data = (flight_number, insert_column, insert_row, insert_class, insert_type, seqNum)
                    insertPlaneLayout(insert_data)
                    seqNum = seqNum + 1

                columnCounter+=1
        
        rowCounter+=1

def getDistinctFlights():
    distinct_flights = []

    cur.execute("SELECT DISTINCT flightNumber from airplaneLayout")
    all_flights = cur.fetchall()

    for flight in all_flights:
        distinct_flights.append(flight[0])

    return(distinct_flights)

def getDistinctPlanes():
    distinct_planes = []

    cur.execute("SELECT DISTINCT planeModel from airline_models")
    all_planes = cur.fetchall()

    for plane in all_planes:
        distinct_planes.append(plane[0])

    return(distinct_planes)