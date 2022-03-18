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

def getAssignedClassTicket(classRef, amount, flightRef):
    
    seatCount = 0
    passRef = getFlightPassengerRef(flightRef)
    
    all_pass = getPassengerGroupDecending(passRef, str(classRef), flightRef)
    all_seat = getClassSeats(flightRef, classRef)

    assigned_tickets =[]

    loop_amount = amount

    for passenger in all_pass:
        currGroupSize = passenger[1]
        if loop_amount >= currGroupSize:
            loop_amount = loop_amount - currGroupSize
            assigned_tickets.append((passenger[0], all_seat[seatCount:(seatCount+currGroupSize)]))
            seatCount = seatCount + currGroupSize
        else:
            pass
    
    if loop_amount > 0:
        print("Seating Waring @getAssignedClassTicket")

    for group_tickets in assigned_tickets:
        group = group_tickets[1]
        for ticket in group:
            insertPassengerRefFlight(flightRef, ticket[0], ticket[1], group_tickets[0])

#all_tickets = getAssignedClassTicket(3, 70, "DDD70")

# seats = getClassArray("PLANE56")
# passengers = getPassengerClassArray("223")

# classArray = getFullClassArray(seats, passengers)

# actual, upDowns = getPlaneActual(seats, passengers)
# actualArray = getFullActualArray(seats, passengers, actual, upDowns)

# print(upDowns)
# print(actualArray)