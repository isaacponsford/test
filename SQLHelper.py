from itertools import count
import sqlite3
from importCSV import planeMetrics, getPlaneLayout
from tools import isBlank, totalCapacity

def connect():
    conn = sqlite3.connect("seatSelector.db", check_same_thread=False)
    cur= conn.cursor()
    return (conn, cur)

def insertPlaneLayout(data_tuple):
    conn, cur = connect()
    base_sql = """insert into airplaneLayout (flightNumber, columnTitle, rowTitle, class, type, sequenceNumber) VALUES (?,?,?,?,?,?)"""
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

def SQLSelectClean(all_data):
    out = []

    for data in all_data:
        out.append(data[0])

    return(out)


def getPlaneInfo(flightNo):
    conn, cur = connect()

    cur.execute("SELECT a.columnTitle, a.rowTitle, a.class, a.type, a.passengerRef, p.class from airplaneLayout AS a LEFT JOIN passengers AS p ON a.passengerRef = p.ticketID  WHERE a.flightNumber = ? ORDER By a.sequenceNumber", (flightNo,))

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

        passengerData = current_data[4]
        
        if passengerData == None:
            occupiedData = 0
            inputPassengerString = 'Unoccupied\\nClass: ' + str(current_data[2])
        else:
            occupiedData = 1
            inputPassengerString = passengerAlertData(passengerData)

        classData = current_data[2]

        try:
            inputData = (occupiedData * 20) + classData
        except:
            pass
        
        inputData = inputPassengerString + ";" + str(inputData) + ";" + str(current_data[5])
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
            insert_data = (flight_number, "", insert_row, None , 99, seqNum)
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

                    insert_data = (flight_number, insert_column, insert_row, insert_class, insert_type, seqNum)
                    insertPlaneLayout(insert_data)
                    seqNum = seqNum + 1

                columnCounter+=1
        
        rowCounter+=1

def getDistinctFlights():
    conn, cur = connect()

    cur.execute("SELECT DISTINCT flightNumber from airplaneLayout")
    all_flights = cur.fetchall()

    distinct_flights = SQLSelectClean(all_flights)

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

    base_sql = ("insert into airplaneLinkTable (flightNo, airplaneModel) VALUES (?,?)")
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

def insertPassengerTable(data):
    conn, cur = connect()
    base_sql = ("INSERT INTO passengers (groupID, flightRef, key, class, requirements, preference) VALUES (?,?,?,?,?,?)")
    cur.execute(base_sql, data)
    conn.commit()
    conn.close()

def unassignedPlanes():
    conn, cur = connect()

    cur.execute("SELECT flightNo FROM airplaneLinkTable WHERE passengerFlightRef IS NUll")
    all_data = cur.fetchall()

    cData = SQLSelectClean(all_data)
    
    conn.close()

    planeArray = []

    for plane in cData:
        capacity = (totalCapacity(getClassArray(plane)))
        string = plane + " (" + str(capacity) + ")"
        planeArray.append([plane, string])

    return(planeArray)

def getDistinctPassengersRef():
    conn, cur = connect()

    cur.execute("SELECT DISTINCT flightRef FROM passengers WHERE flightRef NOT IN (SELECT passengerFlightRef FROM airplaneLinkTable where passengerFlightRef IS NOT NULL)")
    all_data = cur.fetchall()

    passengerRefs = SQLSelectClean(all_data)

    conn.close()

    passengerArray = []

    for passenger in passengerRefs:
            capacity = getPassengerCount(passenger)
            string = passenger + " (" + str(capacity) + ")"
            passengerArray.append([passenger, string])

    return(passengerArray)

def insertPassengerLinkTable(flightNo, passengers):
    conn, cur = connect()

    data_tuple = (passengers, flightNo)
    base_sql = ("UPDATE airplaneLinkTable set passengerFlightRef = ? WHERE flightNo = ?")

    cur.execute(base_sql, data_tuple)
    conn.commit()
    conn.close()

def getClassSeats(flightNo, classNo):
    conn, cur = connect()

    data_tuple = (classNo,flightNo)
    base_sql = ("SELECT columnTitle, rowTitle from airplaneLayout where class = ? AND flightNumber = ? AND passengerRef IS NULL ORDER by rowTitle, columnTitle")

    cur.execute(base_sql, data_tuple)
    all_data = cur.fetchall()
    conn.close()

    return(all_data)

def getPassengerCount(flightRef):
    conn, cur = connect()

    cur.execute("SELECT Count(*) from passengers where flightRef = ?", (flightRef,))
    all_data = cur.fetchall()
    count = all_data[0][0]

    conn.close()

    return(count)

def getPassengerClassArray(flightRef):
    conn, cur = connect()

    cur.execute("SELECT class, COUNT(ticketID) FROM passengers WHERE flightRef = ? AND class >= 1 GROUP BY class", (flightRef,))
    all_data = cur.fetchall()
    conn.close()
    return(all_data)

#passs=067, flight=add90

def getPassengerGroupDecending(passRef, classRef, flightRef):
    #Selects all passengers for current class, and lower classes, where not already been seated and on a given flightRef
    conn, cur = connect()

    data_tuple = (passRef, classRef, flightRef)
    base_sql = ("SELECT groupID, COUNT(*) AS passengerCount, class FROM passengers WHERE flightRef = ? AND class >= ? AND ticketID NOT IN(SELECT passengerRef from airplaneLayout WHERE flightNumber = ? AND passengerRef NOT NULL) GROUP BY groupID ORDER BY class DESC , passengerCount DESC")
    cur.execute(base_sql, data_tuple)
    all_data = cur.fetchall()
    conn.close()
    return(all_data)

def getFlightPassengerRef(flightRef):

    conn, cur = connect()

    cur.execute("SELECT passengerFlightRef from airplaneLinkTable WHERE flightNo = ?", (flightRef,))
    all_data = cur.fetchall()[0][0]
    conn.close()
    return(all_data)

def insertPassengerRefFlight(flight, column, row, passengerRef):
    conn, cur = connect()
    
    data_tuple = (passengerRef, flight, row, column)
    base_sql = ("UPDATE airplaneLayout SET passengerRef = ? WHERE flightNumber = ? AND rowTitle = ? AND columnTitle = ?")

    cur.execute(base_sql, data_tuple)
    conn.commit()
    conn.close()

def passengerPlanes():
    conn, cur = connect()

    #SELECT flightNumber, count(*) from airplaneLayout AS a2 WHERE passengerRef NOT NULL GROUP by flightNumber

    cur.execute("SELECT DISTINCT flightNumber from airplaneLayout")
    all_flights = cur.fetchall()

    distinct_flights = SQLSelectClean(all_flights)

    conn.close()
    return(distinct_flights)

def clearPassengersFlightNumber(flightRef):
    conn, cur = connect()
    
    cur.execute("UPDATE airplaneLayout SET passengerRef = NULL WHERE flightNumber = ?", (flightRef,))
    conn.commit()

    cur.execute("UPDATE airplaneLinkTable SET passengerFlightRef = NULL WHERE flightNo = ?", (flightRef,))
    conn.commit()

    conn.close()

def passengerExists(passRef):
    conn, cur = connect()
    
    cur.execute("SELECT * from passengers WHERE flightRef = ?", (passRef,))
    data = len(cur.fetchall())
    conn.close()

    if data > 0:
        return True
    else:
        return False

def clearAll():
    conn, cur = connect()

    cur.execute("DELETE FROM airlineModels")
    conn.commit()
    cur.execute("DELETE FROM passengers")
    conn.commit()
    cur.execute("DELETE FROM airplaneLinkTable")
    conn.commit()
    cur.execute("DELETE FROM airplaneLayout")
    conn.commit()

    conn.close()

def getIndividualTicketRefs(groupID):
    conn, cur = connect()

    cur.execute("SELECT ticketID from passengers WHERE groupID = ?", (groupID,))
    
    data = cur.fetchall()

    data = SQLSelectClean(data)

    conn.close()

    return data

def getAssignedClassTicket(inClassRef, amount, flightRef):

    seatCount = 0
    passRef = getFlightPassengerRef(flightRef)

    #Return a list of passgerers grouped by Group ID, at the current class or lower (greater class number), in order of group size deceding, where passenger are unassigned a seat 
    all_pass = getPassengerGroupDecending(passRef, str(inClassRef), flightRef)
    
    #Returns location of all empty seats at for a given class 
    all_seat = getClassSeats(flightRef, inClassRef)
    
    # if len(all_seat) < amount:
    #     all_seat.append(getClassSeats(flightRef, seatClassRef-1))
    
    classRef = inClassRef - 1
    
    while len(all_pass) < amount:
        if classRef < 0:
            print("Class Reference Error @getAssignedClassTicket")
            break
        all_pass = getPassengerGroupDecending(passRef, str(classRef), flightRef)
        classRef = classRef - 1

    assigned_tickets =[]

    loop_amount = amount

    # all pass in a array of tuples of passengers, with the first element being the group ID, 
    # and the second being the number of passengers with the corresponding group ID (number of passengers in the group)

    for passenger in all_pass:
        currGroupSize = passenger[1]

        #If there is space to put the entire group into this class, then allocate those seats

        if loop_amount >= currGroupSize:

            loop_amount = loop_amount - currGroupSize
            assigned_tickets.append((passenger[0], all_seat[seatCount:(seatCount+currGroupSize)]))
            seatCount = seatCount + currGroupSize
        else:
            pass
    
    if loop_amount > 0:
        print("Seating Warning @getAssignedClassTicket")

    for group_tickets in assigned_tickets:

        group = group_tickets[1]
        groupId = group_tickets[0]
        ids = getIndividualTicketRefs(groupId)
        counter = 0

        for ticket in group:
            
           insertPassengerRefFlight(flightRef, ticket[0], ticket[1], ids[counter])
           counter = counter + 1

def passengerAlertData(passengerID):
    conn, cur = connect()

    cur.execute("SELECT groupID, flightRef, key, class from passengers WHERE ticketID = ?", (passengerID,))
    
    data1 = cur.fetchall()[0]

    if data1[2] == "A":
        ac = "Adult"
    elif data1[2] == "C":
        ac = "Child"
    else:
        ac = "Error"

    cur.execute("SELECT flightNumber, columnTitle, rowTitle, class from airplaneLayout WHERE passengerRef = ?", (passengerID,))

    data2 = cur.fetchall()[0]

    base_sql = ("SELECT a.passengerRef , a.columnTitle, a.rowTitle, p.key, a.class, p.class from airplaneLayout AS a, passengers AS p WHERE a.passengerRef IN (SELECT ticketID from passengers WHERE groupID = ? AND flightRef = ? AND passengerRef != ?)  AND a.passengerRef = p.ticketID ORDER BY columnTitle, rowTitle")
    data_tuple = (data1[0], data1[1], passengerID)

    cur.execute(base_sql, data_tuple)
    group_data = cur.fetchall()
    
    finalString = "Passenger ID: " + str(passengerID)  + " (" + ac + ")" + "\\nGroup ID: " + data1[0] + " (Group Size: " + str(len(group_data) + 1) + " People)\\nSeat: " + data2[1] + str(data2[2]) + "\\nSeat Class: " + str(data2[3]) 

    if data1[3] != data2[3]:
        finalString = finalString + " (Ticket Class: " + str(data1[3]) + ")"

    if len(group_data) > 0 :
        finalString = finalString + "\\n\\nGroup Members:"
        for data in group_data:

            if data[3] == "A":
                ac = "Adult"
            elif data[3] == "C":
                ac = "Child"
            else:
                ac = "Error"

            finalString = finalString + "\\nSeat: " + data[1] + str(data[2]) + " - ID: " + data[0] + " (" + ac + ") - Seat Class: " + str(data[4])
            if data[4] != data[5]:
                finalString = finalString + " (Ticket Class: " + str(data[5]) + ")"
    else:
        finalString = finalString + "\\n\\nOnly Passenger"
    conn.close()
    return finalString

def getPlaneSeatClasses(flightNo):
   

    conn, cur = connect()

    cur.execute("SELECT DISTINCT class from airplaneLayout WHERE flightNumber = ? AND class NOT NULL ORDER BY class", (flightNo,))

    all_data = cur.fetchall()
    all_data = SQLSelectClean(all_data)
    conn.close()
    return(all_data)

def getPassengerArray(passRef):
    conn, cur = connect()

    cur.execute("SELECT groupID, count(*) AS amount, class from passengers WHERE flightRef = ? GROUP BY groupID ORDER by class, amount", (passRef,))
    all_data = cur.fetchall()
    conn.close()
    return(all_data)