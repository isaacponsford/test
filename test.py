from SQLHelper import clearPassengersFlightNumber, getClassSeats, CSVtoSQL, getDistinctPassengersRef, getFlightPassengerRef, getPassengerGroupDecending, insertPassengerRefFlight, insertPlaneLayout, getPlaneInfo, getDistinctFlights, getDistinctPlanes, insertLinkTable, getFlightAirlineModel, getClassArray, passengerExists, populateSeat, insertPassengerTable, getPassengerCount, getPassengerClassArray, unassignedPlanes
from importCSV import planeMetrics, getPassengerCSV
from tools import createPassCSVArray, createPassengerCSV, getFullActualArray, getFullClassArray, getPlaneActual, totalCapacity

# # {% if seatData[0] == "XX" %}
# #     { % set passengerData = "Seat is unoccupied" % }
# # {% else %}
# #     { % set passengerData = seatData[0] % }
# # {% endif %}    

# #populatePlaneClass(4, 20, "ADD90")

#print(getPassengerGroupDecending("444", str(4)))


#all_tickets = getAssignedClassTicket(3, 70, "DDD70")

planeRef = "EMB5-622"
passRef = "5-54-4"

# seats = getClassArray(planeRef)
# passengers = getPassengerClassArray(passRef)

# array = getPlaneActual(seats, passengers)[0]

# print(array)

#EMB5-62 Actual Array: [[1, 6], [2, 14], [3, 12], [4, 8], [5, 10]]



# for i in reverse(array):
#     getAssignedClassTicket(i[0], i[1], "EMB5-62")

#Plane Array: [(1, 6), (2, 14), (3, 12), (4, 15), (5, 15)] | 62
array = [(1, 10), (2, 0), (3, 16), (4, 8), (5, 15)] 
createPassCSVArray("5-50", array)

# print()

# for x in getPassengerCSV(passRef):
#     insertPassengerTable(x)