from SQLHelper import clearPassengersFlightNumber, getClassSeats, CSVtoSQL, getDistinctPassengersRef, getFlightPassengerRef, getPassengerGroupDecending, insertPassengerRefFlight, insertPlaneLayout, getPlaneInfo, getDistinctFlights, getDistinctPlanes, insertLinkTable, getFlightAirlineModel, getClassArray, populateSeat, insertPassengerTable, getPassengerCount, getPassengerClassArray, unassignedPlanes
from importCSV import getValidCSV, planeMetrics, getPassengerCSV
from random import randint
from tools import createPassengerCSV, getFullClassArray, totalCapacity

def getAssignedClassTicket(classRef, amount, flightRef):
    seatCount = 0
    passRef = getFlightPassengerRef(flightRef)
    
    all_pass = getPassengerGroupDecending(passRef, str(classRef))
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

    return (assigned_tickets)


# #populatePlaneClass(4, 20, "ADD90")

# #insertPassengerRefFlight("EXT45", "C", 6, "x78")

# all_tickets = getAssignedClassTicket(4, 20, "ADD90")

# for group_tickets in all_tickets:
#     group = group_tickets[1]
#     for ticket in group:
#         insertPassengerRefFlight("ADD90", ticket[0], ticket[1], group_tickets[0])

print(getPlaneInfo("ADD90"))

# {% if seatData[0] == "XX" %}
#     { % set passengerData = "Seat is unoccupied" % }
# {% else %}
#     { % set passengerData = seatData[0] % }
# {% endif %}    