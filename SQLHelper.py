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
    cur.execute("SELECT columnTitle, rowTitle, class from airplaneLayout WHERE flightNumber = ? ORDER By sequenceNumber", (flightNo,))
    rows = cur.fetchall()

    layout = [] 
    temp = []
    titles = []
    count = 0

    blank = ['','','','']

    while count + 1 < len(rows):

        current_row = rows[count]
        temp.append(str(current_row[2]))
        titles.append(str(current_row[0]))

        if rows[count+1][1] > current_row[1]: #Comparing rows
            temp = cleanup(temp, titles)
            layout.append(temp)
            temp = []
            titles = []
        else:
            pass
        count = count + 1

    return(layout)

def CSVtoSQL(flight_number, csv_add):

    Metrics = planeMetrics(csv_add)
    #noOfRows = Metrics[0]
    noOfColumns = Metrics[1]
    planeLayout = Metrics[4]
    rowTitles = Metrics[5]
    columnTitles = Metrics[6]

    columnCounter = 0
    rowCounter = 0
    seqNum = 1

    while rowCounter < len(planeLayout):
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