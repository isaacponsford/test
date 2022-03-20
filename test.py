from SQLHelper import clearAll, clearPassengersFlightNumber, getAssignedClassTicket, getClassSeats,  getDistinctPassengersRef, getFlightPassengerRef, getIndividualTicketRefs, getLayoutClassArray, getPassengerArray, getPassengerGroupDecending, getPassengersWithRef, getPlaneSeatClasses, groupHappinessFunction, happinessFunction, insertPassengerRefFlight, insertPlaneLayout, getPlaneInfo, getDistinctFlights, getDistinctPlanes, insertLinkTable, getFlightAirlineModel, getClassArray, passengerAlertData, passengerExists, populateSeat, insertPassengerTable, getPassengerCount, getPassengerClassArray, unassignedPlanes
from importCSV import planeMetrics, getPassengerCSV
from tools import createPassCSVArray, createPassengerCSV, getFullActualArray, getFullClassArray, getPlaneActual, totalCapacity
import sqlite3
# happinessFunction("5-1UP1DOWN-S")

# conn, cur = sqlite3.connect()

# cur.execute("SELECT p.ticketID, a.class, p.class, a.aw, p.preference, p.happiness from passengers as p LEFT JOIN airplaneLayout as a ON a.passengerRef = p.ticketID WHERE p.flightRef = ?", (passRef,))
# conn.close()

groupHappinessFunction("5-1UP1DOWN-S", 0.1)

#array = [(681, 27, 'A'), (682, 27, 'C'), (680, 27, 'D'), (683, 28, 'A')]

# print(ord('C'))