from SQLHelper import *
from importCSV import *
from tools import createPassCSVArray, getPlaneActual


# createPassCSVArray("AAA50", array)

# passengers = (getPassengerCSV("AAA50"))
            
# for x in passengers:
#     insertPassengerTable(x)

# print(getPassengerClassArray("AAA50"))

passengers = getPassengerClassArray("AAA50")
seats = getClassArray("AXD30")

# print(passengers)
# print(seats)
passengers = listExtend(passengers, 9)
seats = listExtend(seats, 9)
# passLen = len(passengers)
# for i in range(9-passLen):
#     passengers.append((i+passLen+1, 0))

# seatLen = len(seats)
# for i in range(9-seatLen):
#     seats.append((seatLen+i+1, 0))

print(getPlaneActual(seats, passengers)[0][0:4])