from SQLHelper import getClassSeats, CSVtoSQL, insertPlaneLayout, getPlaneInfo, getDistinctFlights, getDistinctPlanes, insertLinkTable, getFlightAirlineModel, getClassArray, populateSeat, insertPassengerTable, getPassengerCount, getPassengerClassArray
from importCSV import planeMetrics, getPassengerCSV
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



#print(getPassengerCount("567"))

print((getClassArray("NRM45")))
print(getPassengerClassArray("567"))