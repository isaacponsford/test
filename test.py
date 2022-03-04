from SQLHelper import CSVtoSQL, insertPlaneLayout, getPlaneInfo, getDistinctFlights, getDistinctPlanes, insertLinkTable, getFlightAirlineModel, getClassArray, populateSeat
from importCSV import planeMetrics
from random import randint

#noOfRows, noOfColumns, capacity, capacityArray, planeLayout, rowTitles,columnTitles

# fNo = "LK90"

# cArray = getClassArray(fNo)
# print(cArray)
# pArray = []

# for i in cArray:
#     dTuple = i[0], randint(0, i[1])
#     pArray.append(dTuple)

# print(pArray)

populateSeat('L', '2', "LK90")