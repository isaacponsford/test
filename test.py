from SQLHelper import CSVtoSQL, insertPlaneLayout, getPlaneInfo, getDistinctFlights, getDistinctPlanes, insertLinkTable, getFlightAirlineModel, getClassArray, populateSeat, insertPassengerTable
from importCSV import planeMetrics, getPassengerCSV
from random import randint

# fNo = "LK90"

# cArray = getClassArray(fNo)
# print(cArray)
# pArray = []

# for i in cArray:
#     dTuple = i[0], randint(0, i[1])
#     pArray.append(dTuple)
# print(pArray)

#populateSeat('L', '2', "NRM45")

#print(getPlaneInfo("PLANE56"))
print(getClassArray("EXT45"))