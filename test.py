from SQLHelper import clearAll, clearPassengersFlightNumber, getClassSeats, CSVtoSQL, getDistinctPassengersRef, getFlightPassengerRef, getIndividualTicketRefs, getPassengerArray, getPassengerGroupDecending, getPlaneSeatClasses, insertPassengerRefFlight, insertPlaneLayout, getPlaneInfo, getDistinctFlights, getDistinctPlanes, insertLinkTable, getFlightAirlineModel, getClassArray, passengerAlertData, passengerExists, populateSeat, insertPassengerTable, getPassengerCount, getPassengerClassArray, unassignedPlanes
from importCSV import planeMetrics, getPassengerCSV
from tools import createPassCSVArray, createPassengerCSV, getFullActualArray, getFullClassArray, getPlaneActual, totalCapacity

# #populatePlaneClass(4, 20, "ADD90")

#print(getPassengerGroupDecending("444", str(4)))


#all_tickets = getAssignedClassTicket(3, 70, "DDD70")

# planeRef = "EMB5-622"
# passRef = "5-54-4"

# # seats = getClassArray(planeRef)
# # passengers = getPassengerClassArray(passRef)

# # array = getPlaneActual(seats, passengers)[0]

# # print(array)

# #EMB5-62 Actual Array: [[1, 6], [2, 14], [3, 12], [4, 8], [5, 10]]

# # for i in reverse(array):
# #     getAssignedClassTicket(i[0], i[1], "EMB5-62")


# # Plane Array: [(1, 5), (2, 12), (3, 12), (4, 12), (5, 21)]
# array = [(1, 4), (2, 12), (3, 8), (4, 12), (5, 14)] 
# createPassCSVArray("5-AllOK2s", array)

# # # print()

# # # for x in getPassengerCSV(passRef):
# # #     insertPassengerTable(x)

# flightRef = "EMB5-62"

# passRef = getFlightPassengerRef(flightRef)

#     #Return a list of passgerers grouped by Group ID, at the current class or lower (greater class number), in order of group size deceding, where passenger are unassigned a seat 
# all_pass = getPassengerGroupDecending(passRef, str(5), flightRef)

# all_seat = getClassSeats(flightRef, 5)

# print(all_seat)

# print(getPlaneSeatClasses("EMB5-62"))

# print(getFlightPassengerRef("X800"))

# print(getPassengerGroupDecending("3-55", "2", "EMB5-62"))

# print(getClassArray("ORD5-62"))s

print(getPassengerArray("5-AllOK"))