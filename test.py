from SQLHelper import clearAll, clearPassengersFlightNumber, getAssignedClassTicket, getClassSeats, CSVtoSQL, getDistinctPassengersRef, getFlightPassengerRef, getIndividualTicketRefs, getLayoutClassArray, getPassengerArray, getPassengerGroupDecending, getPassengersWithRef, getPlaneSeatClasses, insertPassengerRefFlight, insertPlaneLayout, getPlaneInfo, getDistinctFlights, getDistinctPlanes, insertLinkTable, getFlightAirlineModel, getClassArray, passengerAlertData, passengerExists, populateSeat, insertPassengerTable, getPassengerCount, getPassengerClassArray, unassignedPlanes
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

# array = [(1, 8), (2, 2), (3, 10), (4, 5), (5, 25)] 
createPassCSVArray("5-1UP1DOWN", array)

# # # # print()

# # # # for x in getPassengerCSV(passRef):
# # # #     insertPassengerTable(x)

# # flightRef = "EMB5-62"

# # passRef = getFlightPassengerRef(flightRef)

# # #     #Return a list of passgerers grouped by Group ID, at the current class or lower (greater class number), in order of group size deceding, where passenger are unassigned a seat 
# # # all_pass = getPassengerGroupDecending(passRef, str(5), flightRef)

# # print(getClassArray("EMB5-62"))

# print(getLayoutClassArray("EMB5-62"))

# passRef = getFlightPassengerRef("EMB5-62")

# #Return a list of passgerers grouped by Group ID, at the current class or lower (greater class number), in order of group size deceding, where passenger are unassigned a seat 
# all_pass = getPassengerGroupDecending(passRef, str(1), "EMB5-62")
# print(all_pass)

print(getPassengersWithRef("1o2", "5-1UP1DOWN"))

#print(getClassSeats("EMB5-62", 1))
