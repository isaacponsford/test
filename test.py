from SQLHelper import CSVtoSQL, insertPlaneLayout, getPlaneInfo, getDistinctFlights, getDistinctPlanes, insertLinkTable, getFlightAirlineModel, getClassArray, populateSeat, insertPassengerTable
from importCSV import planeMetrics, getPassengerCSV
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

#populateSeat('L', '2', "NRM45")

#print(getPlaneInfo("PLANE56"))

# d = getPassengerCSV("567")
# for i in d:
#     insertPassengerTable(i)
# #insertPassengerTable(('X1', '567', 'A', '3', '', ''))

print(getClassArray("EXT45"))

# {% if intSeat == 1 %}
#                 {% set seatColour = [0, 0, 255] %}
#             {% elif intSeat == 2 %}
#                 {% set seatColour = [25, 214, 25] %}
#             {% elif intSeat == 3 %}
#                 {% set seatColour = [214, 25, 25] %}
#             {% elif intSeat == 4 %}
#                 {% set seatColour = [150, 15, 229] %}
#             {% endif %}