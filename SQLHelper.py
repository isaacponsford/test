import sqlite3
from importCSV import planeMetrics, getPlaneLayout
from tools import isBlank

def connect():
    conn = sqlite3.connect("seatSelector.db", check_same_thread=False)
    cur= conn.cursor()
    return (conn, cur)

def insertPlaneLayout(data_tuple):
    conn, cur = connect()
    print(data_tuple)
    base_sql = """insert into airplaneLayout (flightNumber, columnTitle, rowTitle, class, type, sequenceNumber, occupied) VALUES (?,?,?,?,?,?,?)"""
    cur.execute(base_sql, data_tuple)
    conn.commit()
    conn.close()

def cleanup(temp, titles, columnTitles):
    out = []

    x = 0 #temp point
    y = 0 #cT point

    while x < len(columnTitles):

        if y > len(titles)-1:
            out.append('')
            x = x + 1
        elif columnTitles[x] == titles[y]:
            out.append(temp[y])
            x = x + 1
            y = y + 1
        else:
            out.append('')
            x = x + 1

    return(out)

def getPlaneInfo(flightNo):
    conn, cur = connect()

    cur.execute("SELECT columnTitle, rowTitle, class, type, occupied from airplaneLayout WHERE flightNumber = ? ORDER By sequenceNumber", (flightNo,))
    all_data = cur.fetchall()

    airlineModel = getFlightAirlineModel(flightNo)
    noOfColumns, rowTitles, columnTitles = planeMetrics(airlineModel)

    blank = []

    for i in range(noOfColumns):
        blank.append('')

    layout = [] 
    temp = []
    titles = []
    count = 0

    while count < len(all_data):

        current_data = all_data[count]

        occupiedData = current_data[4]
        classData = current_data[2]
        
        try:
            inputData = (occupiedData * 20) + classData
        except:
            pass
        
        temp.append(str(inputData))
        titles.append(str(current_data[0]))

        if current_data[3] == 1:
            try:
                if all_data[count+1][1] > current_data[1]:
                    temp = cleanup(temp, titles, columnTitles[1::])
                    layout.append(temp)
                    temp = []
                    titles = []
                else:
                    pass
            except IndexError:
                temp = cleanup(temp, titles, columnTitles[1::])
                layout.append(temp)

        elif current_data[3] == 99:

            layout.append(blank)
            temp = []
            titles = []

        count = count + 1

    conn.close()
    return(layout)

def CSVtoSQL(flight_number, csv_add):

    noOfColumns, rowTitles, columnTitles = planeMetrics(csv_add)
    planeLayout = getPlaneLayout(csv_add)
    
    columnCounter = 0
    rowCounter = 0
    seqNum = 1


    while rowCounter < len(planeLayout):

        if isBlank(planeLayout[rowCounter]):
            insert_row = int(rowTitles[rowCounter-1]) + 1
            insert_data = (flight_number, "", insert_row, None , 99, seqNum, None)
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
                    occupied = 0

                    insert_data = (flight_number, insert_column, insert_row, insert_class, insert_type, seqNum, occupied)
                    insertPlaneLayout(insert_data)
                    seqNum = seqNum + 1

                columnCounter+=1
        
        rowCounter+=1

def getDistinctFlights():
    conn, cur = connect()

    distinct_flights = []

    cur.execute("SELECT DISTINCT flightNumber from airplaneLayout")
    all_flights = cur.fetchall()

    for flight in all_flights:
        distinct_flights.append(flight[0])

    conn.close()
    return(distinct_flights)

def getDistinctPlanes():
    conn, cur = connect()

    cur.execute("SELECT DISTINCT planeModel, planeLayoutCSV from airlineModels")
    all_planes = cur.fetchall()

    conn.close()
    return(all_planes)

def insertLinkTable(data_tuple):
    conn, cur = connect()

    base_sql = ("""insert into airplaneLinkTable VALUES (?,?)""")
    cur.execute(base_sql, data_tuple)
    conn.commit()
    conn.close()

def getFlightAirlineModel(flightNo):
    conn, cur = connect()

    cur.execute("SELECT airplaneModel from airplaneLinkTable WHERE flightNo = ?", (flightNo,))
    airlineModel = cur.fetchone()
    conn.close()
    return(airlineModel[0])

def getClassArray(flightNo):
    conn, cur = connect()

    cur.execute("SELECT class, COUNT(columnTitle) FROM airplaneLayout WHERE flightNumber = ? AND class >= 1 GROUP BY class", (flightNo,))
    all_data = cur.fetchall()
    conn.close()
    return(all_data)
    
def populateSeat(column, row, flightNo): 
    conn, cur = connect()

    data_tuple = (column, row, flightNo)
    base_sql = ("UPDATE airplaneLayout set occupied = 1 WHERE columnTitle = ? AND rowTitle = ? AND flightNumber = ?")

    cur.execute(base_sql, data_tuple)
    conn.commit()
    conn.close()

def insertModelTable(planeName, filename):
    conn, cur = connect()

    data_tuple = (planeName, filename)
    base_sql = ("INSERT INTO airlineModels (planeModel, planeLayoutCSV) VALUES (?,?)")

    cur.execute(base_sql, data_tuple)
    conn.commit()
    conn.close()