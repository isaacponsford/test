import sqlite3

from importCSV import planeMetrics


#select columnTitle, rowTitle, class from airplaneLayout where flightNumber = "BA1"

# from importCSV import planeMetrics
# Metrics = planeMetrics("emb145")
# planeLayout = Metrics[4]
# print(planeLayout)

conn = sqlite3.connect("seatSelector.db", check_same_thread=False)
cur= conn.cursor()

columnTitles = (planeMetrics("emb145")[6][1::])

def cleanup(temp, titles):

    #print(temp)
    #print(titles)
    #print(columnTitles)

    if len(temp) == 1:
        return([temp[0],'','',''])
    elif len(temp) == 3:
        return([temp[0],'',temp[1],temp[2]])

def function ():
    cur.execute("SELECT columnTitle, rowTitle, class from airplaneLayout")
    rows = cur.fetchall()

    layout = [] 
    temp = []
    titles = []
    count = 0

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