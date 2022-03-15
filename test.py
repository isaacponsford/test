from calendar import c
from wsgiref.headers import tspecials
from SQLHelper import getClassSeats, CSVtoSQL, getDistinctPassengersRef, getPassengerGroupDecending, insertPlaneLayout, getPlaneInfo, getDistinctFlights, getDistinctPlanes, insertLinkTable, getFlightAirlineModel, getClassArray, populateSeat, insertPassengerTable, getPassengerCount, getPassengerClassArray, unassignedPlanes
from importCSV import getValidCSV, planeMetrics, getPassengerCSV
from random import randint
from tools import createPassengerCSV, totalCapacity

# createPassengerCSV()    

# x=45
# flightNo = "NRM45"

# classSeats = getClassSeats(flightNo, 4)
# NoOfseats = len(classSeats)

# if NoOfseats > x:
#     for i in range(x):
#         r = randint(0,NoOfseats)
#         cur = classSeats[r]
#         populateSeat(cur[0], cur[1], flightNo)


# newFlight = "109"
# createPassengerCSV(newFlight, 90)
# passengerArray = getPassengerCSV(newFlight)

# for passenger in passengerArray:
#     insertPassengerTable(passenger)

#print(getPassengerGroupDecending("804"))

testPlane = [[1,20], [2,40], [3,50], [4,100]]
testPassenger = [[1,5],[2,10],[3,90],[4,60]]
#excess = [[1, -15], [2, -30], [3, 40], [4, -40]]

def arrayAdd(list1,list2, index):
    return [list1[index][0], (list1[index][1] + list2[index][1])]

def arraySubtract(list1,list2, index):
    return [list1[index][0], (list1[index][1] - list2[index][1])]

excess = []
x = len(testPlane)

for i in range(x):
    excess.append([testPlane[i][0], (testPassenger[i][1] - testPlane[i][1])])

print("\nPre Excess: ")
print(excess)

actual = []

for i in range(x):

    index = x-(i+1)
    curentClass = excess[index]

    print(testPassenger[index][0], testPassenger[index][1] , excess[index][1], testPlane[index][1])

    if curentClass[1] > 0:
        actual.append(testPlane[index])
    else:
        if (testPassenger[index] + excess[index]) > testPlane[index]:
            actual.append(testPlane[index])
            excess[index-1][1] = excess[index-1][1]  + (testPassenger[index][1] + excess[index][1]) - testPlane[index][1]
        else:
            actual.append(arrayAdd(testPassenger, excess, index))
            
print("\nPost Excess: ")
print(excess)
print("\nActual: ")
print(actual)